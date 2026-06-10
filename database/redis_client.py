import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from redis import Redis

from config.settings import settings


redis_client = Redis.from_url(
    settings.REDIS_URL,
    decode_responses=True
)


def test_connection():
    """
    Test Redis connectivity.
    Run this file directly to verify Redis is working.
    """

    redis_client.set(
        "test_key",
        "hello"
    )

    value = redis_client.get(
        "test_key"
    )

    print(
        f"Redis Connected Successfully: {value}"
    )


if __name__ == "__main__":
    test_connection()