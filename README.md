# Python wrapper for TradeGecko API.

## Install

```pip install tradegecko-python```


## Usage

```python

from tradegecko import TradeGecko

# Initialize client
tg = TradeGecko(auth_token=access_token)

# Create company
tg.company.create(**company_data)

# Update company
tg.company.update(company_id, **company_data)
```
