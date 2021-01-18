import requests
from bcschain.models import Block
from django.utils import timezone
from datetime import datetime, timedelta
import pytz
import time


def update_blocks():
    start_date = datetime.strptime('2020-12-21', "%Y-%m-%d")
    current_date = datetime.today()
    first_block = Block.objects.all().first()
    msc = pytz.timezone('Etc/GMT-3')
    if first_block:
        last_timestamp = first_block.timestamp
    else:
        last_timestamp = datetime.fromtimestamp(1606780800).\
            replace(tzinfo=msc)

    while (current_date - start_date).days >= 0:
        datetime_string = f'{current_date.year}-{current_date.month}-{current_date.day}'
        url = f'https://bcschain.info/api/blocks/?date={datetime_string}'
        response = requests.get(url)
        data = response.json()

        for block in data:
            timestamp = datetime.fromtimestamp(int(block['timestamp'])).\
                replace(tzinfo=msc)
            if timestamp < last_timestamp:
                return
            height = block['height']
            if timestamp == last_timestamp:
                try:
                    Block.objects.get(height=height)
                    return
                except Block.DoesNotExist:
                    pass

            obj = Block(height=height,
                        hash=block['hash'],
                        timestamp=timestamp,
                        address=block['miner'],
                        transactions=block['transactionCount'])
            obj.save()

        current_date -= timedelta(days=1)
        time.sleep(1)
