from tradegecko.api import ApiEndpoint


class Company(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/companies/%s",
            auth_token=auth_token,
            name="company",
            name_list="companies",
            required_fields=["name", "company_type"],
        )


class Address(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/addresses/%s",
            auth_token=auth_token,
            name="address",
            name_list="addresses",
            required_fields=["company_id", "label"],
        )


class Location(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/locations/%s",
            auth_token=auth_token,
            name="location",
            name_list="locations",
            required_fields=["label"],
        )


class PurchaseOrder(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/purchase_orders/%s",
            auth_token=auth_token,
            name="purchase_order",
            name_list="purchase_orders",
            required_fields=["company_id", "stock_location_id"],
        )


class PurchaseOrderLineItem(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/purchase_order_line_items/%s",
            auth_token=auth_token,
            name="purchase_order_line_item",
            name_list="purchase_order_line_items",
            required_fields=[
                "variant_id",
                "quantity",
                "price",
                "purchase_order_id",
            ],
        )


class Variant(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/variants/%s",
            auth_token=auth_token,
            name="variants",
            name_list="variants",
        )


class Product(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/products/%s",
            auth_token=auth_token,
            name="products",
            name_list="products",
        )


class OrderLineItem(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/order_line_items/%s",
            auth_token=auth_token,
            name="order_line_item",
            name_list="order_line_items",
        )


class Order(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/orders/%s",
            auth_token=auth_token,
            name="order",
            name_list="orders",
        )


class Invoice(ApiEndpoint):
    def __init__(self, api_url, auth_token):
        super().__init__(
            url=f"{api_url}/invoices/%s",
            auth_token=auth_token,
            name="invoice",
            name_list="invoices",
        )
