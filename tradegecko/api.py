import math
import logging

from tradegecko import errors


logger = logging.getLogger(__name__)


class ApiEndpoint(object):
    def __init__(self, url, auth_token, name, name_list, required_fields=None):
        self.url = url
        self.auth_token = auth_token
        self.header = {
            "Authorization": f"Bearer {self.auth_token}",
            "content-type": "application/json",
        }
        self.response = None
        self.json = None
        self.name = name
        self.name_list = name_list
        self.required_fields = required_fields or []

        import requests

        self.__request = requests.request
        # Supress warnings
        import requests
        from requests.packages.urllib3.exceptions import InsecureRequestWarning

        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

    def _request(self, method, uri, data=None, params=None):
        self.response = self.__request(
            method,
            uri,
            json=data,
            headers=self.header,
            params=params,
            verify=False,
        )
        logger.debug(
            'Request: %s %s\nDATA="%s"\nPARAMS="%s"\nRESPONSE="%s"\nSTATUS=%s',
            method,
            uri,
            data,
            params,
            self.response.content,
            self.response.status_code,
        )
        if self.response.status_code == 401:
            raise errors.AuthenticationError(message=self.response.content)
        if self.response.status_code == 422:
            raise errors.ProcessingError(message=self.response.content)
        if self.response.status_code == 429:
            raise errors.RateLimitExceeded(message=self.response.content)
        return self.response.status_code

    # all records
    def all(self, page=1):
        if self._request("GET", self.url % "", params={"page": page}) == 200:
            return self.response.json()[self.name_list]
        raise errors.ListObjectsError(message=self.response.content)

    # records filtered by field value
    def filter(self, **kwargs):
        if self._request("GET", self.url % "", params=kwargs) == 200:
            return self.response.json()[self.name_list]
        raise errors.ListObjectsError(message=self.response.content)

    # retrieve a specific record
    def get(self, pk):
        if self._request("GET", self.url % str(pk)) == 200:
            return self.response.json()[self.name]
        raise errors.GetObjectError(message=self.response.content)

    # create a new record
    def create(self, data):
        if self._request("POST", self.url % "", data={self.name: data}) == 201:
            return self.response.json()[self.name]
        raise errors.CreateObjectError(message=self.response.content)

    # update a specific record
    def update(self, pk, data):
        if (
            self._request("PUT", self.url % str(pk), data={self.name: data})
            == 204
        ):
            return True
        raise errors.UpdateObjectError(message=self.response.content)

    # delete a specific record
    def delete(self, pk):
        if self._request("DELETE", self.url % str(pk)) == 204:
            return True
        raise errors.DeleteObjectError(message=self.response.content)

    def page_count(self, limit=100):
        tg_items = self.filter(page="1", limit="1")
        return int(math.ceil(tg_items["meta"]["total"] / float(limit)))
