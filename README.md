![travis](https://travis-ci.org/jegorami/tradegecko-python.png?branch=master


# Python wrapper for TradeGecko API.

## Install

```pip install tradegecko-python```


## Usage

```python

from tradegecko import TradeGecko

# Initialize client
tg = TradeGecko(access_token, refresh_token)

# Create company
tg.company.create(**company_data)

# Update company
tg.company.update(company_id, **company_data)
```
