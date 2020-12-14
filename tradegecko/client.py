import os

from tradegecko import errors
from tradegecko.endpoints import (
    Company,
    Address,
    Variant,
    Product,
    OrderLineItem,
    Order,
    Location,
    PurchaseOrder,
    PurchaseOrderLineItem,
    Invoice,
    Currency,
    PaymentTerm,
    Fulfillment,
    Webhook,
)


class TradeGecko(object):
    def __init__(self, api_url=None, auth_token=None):
        self.api_url = (
            api_url
            or os.environ.get(
                "TRADEGECKO_API_URL", "https://api.tradegecko.com"
            )
        ).rstrip("/")
        self.auth_token = auth_token or os.environ.get(
            "TRADEGECKO_AUTH_TOKEN", None
        )
        if not self.auth_token:
            raise errors.AuthenticationError(
                "No TradeGecko auth token. Pass it into client constructor or "
                "set env var TRADEGECKO_AUTH_TOKEN"
            )

        # Endpoints
        self.company = Company(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.address = Address(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.location = Location(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.variant = Variant(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.product = Product(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.order_line_item = OrderLineItem(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.order = Order(api_url=self.api_url, auth_token=self.auth_token)
        self.invoice = Invoice(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.purchase_order = PurchaseOrder(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.purchase_order_line_item = PurchaseOrderLineItem(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.currency = Currency(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.payment_term = PaymentTerm(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.fulfillment = Fulfillment(
            api_url=self.api_url, auth_token=self.auth_token
        )
        self.webhook = Webhook(
            api_url=self.api_url, auth_token=self.auth_token
        )
