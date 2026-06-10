import json

from database.redis_client import redis_client


class CacheService:

    @staticmethod
    def get(key):

        value = redis_client.get(key)

        if value:
            return json.loads(value)

        return None

    @staticmethod
    def set(
        key,
        value,
        expiry=300
    ):

        redis_client.set(
            key,
            json.dumps(value),
            ex=expiry
        )