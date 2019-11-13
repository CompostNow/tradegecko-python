import math
import logging

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

from tradegecko import errors


# Disable warnings, they are just annoyance.
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


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
        self.__request = requests.request

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
            raise errors.AuthenticationError(
                message="Authentication failed.", response=self.response
            )
        if self.response.status_code == 422:
            raise errors.ProcessingError(
                message="Processing request failed.", response=self.response
            )
        if self.response.status_code == 429:
            raise errors.RateLimitExceeded(
                message="Rate limit exceeded.", response=self.response
            )
        return self.response.status_code

    # all records
    def all(self, page=1):
        if self._request("GET", self.url % "", params={"page": page}) == 200:
            return self.response.json()[self.name_list]
        raise errors.ListObjectsError(
            message=f"List {self.name_list} failed.", response=self.response
        )

    # records filtered by field value
    def filter(self, **kwargs):
        if self._request("GET", self.url % "", params=kwargs) == 200:
            return self.response.json()[self.name_list]
        raise errors.ListObjectsError(
            message=f"Filter {self.name_list} failed.", response=self.response
        )

    # retrieve a specific record
    def get(self, pk):
        if self._request("GET", self.url % str(pk)) == 200:
            return self.response.json()[self.name]
        raise errors.GetObjectError(
            message=f"Get {self.name} failed.", response=self.response
        )

    # create a new record
    def create(self, data):
        if self._request("POST", self.url % "", data={self.name: data}) == 201:
            return self.response.json()[self.name]
        raise errors.CreateObjectError(
            message=f"Create {self.name} failed.", response=self.response
        )

    # update a specific record
    def update(self, pk, data):
        if (
            self._request("PUT", self.url % str(pk), data={self.name: data})
            == 204
        ):
            return True
        raise errors.UpdateObjectError(
            message=f"Update {self.name} failed.", response=self.response
        )

    # delete a specific record
    def delete(self, pk):
        if self._request("DELETE", self.url % str(pk)) == 204:
            return True
        raise errors.DeleteObjectError(
            message=f"Delete {self.name} failed.", response=self.response
        )

    def page_count(self, limit=100):
        tg_items = self.filter(page="1", limit="1")
        return int(math.ceil(tg_items["meta"]["total"] / float(limit)))
