import time


class Store:
    """
    A class to manage a dictionary as an in-memory key-value store.
    """

    _store = {}

    @classmethod
    def get(cls, key):
        """
        Get the value for a key, assuming it hasn't expired
        Each key is stored as a tuple (value, expires); those are the indexes 0
        and 1 used when accessing
        """
        try:
            if cls._store[key][1] > time.time():
                # print(f"tuple for key {key}")
                # print(cls._store)
                return cls._store[key][0]
            else:
                del cls._store[key] # Delete the item if it has expired
                return None
        except KeyError:
            return None

    @classmethod
    def set(cls, key, value, duration=3600):
        """
        Store or update value for a key with an expiry duration in seconds
        """
        try:
            expires = time.time() + duration
        except TypeError:
            raise TypeError("Duration must be numeric")

        cls._store[key] = (value, expires)
        return cls.get(key)

    @classmethod
    def delete(cls, key):
        del cls._store[key]

    @classmethod
    def clean(cls):
        """
        Get rid of all the expired items in the store
        """
        keys = list(cls._store.keys())
        for key in keys:
            cls.get(key) # Attempting to fetch an expired item deletes it

    @classmethod
    def purge(cls):
        """
        Empty the dictionary used by the store
        """
        cls._store = {}
