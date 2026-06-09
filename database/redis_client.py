import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from redis import Redis
from config.settings import settings

try:
    redis_client = Redis.from_url(
        settings.REDIS_URL,
        decode_responses=True
    )

    redis_client.set("test_key", "hello")

    value = redis_client.get("test_key")

    print(f"Redis Connected Successfully: {value}")

except Exception as e:
    print(f"Redis Error: {e}")