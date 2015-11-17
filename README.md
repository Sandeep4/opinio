# opinio
Python client for APIs of opinioapp.
API Doc (http://deliver.opinioapp.com/api/docs)

### Installation
pip install git+https://github.com/Sandeep4/opinio.git#egg=opinio

### Usage

```python
from opinio import OpinioClient

client = OpinioClient(access_key, secret_key)

params  = {}
client.create_order(params)
client.get_order(order_id)
client.cancel_order(order_id)
client.get_orders()

```