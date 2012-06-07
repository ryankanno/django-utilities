import os
import time
import logging

DOG_PILE_TTL = 30

logger = logging.getLogger(__name__)

def cache_get(cache, key):
    logger.debug("Attempting to retrieve key=%s from cache" % key)

    stored_val = cache.get(key)

    # key does not exist, immediately return
    if stored_val is None:
        logger.debug("key=%s was not found in the cache" % key)
        return None

    val, expires, being_refreshed = stored_val

    # Prevent dog-pile
    if (time.time() > expires and not being_refreshed):
        logger.debug("Preventing dog-piling by setting stale data for key=%s" % key)
        cache_set(cache, key, val, DOG_PILE_TTL, being_refreshed=True)
        return None

    logger.debug("key=%s found in the cache" % key)
    return val


def cache_set(cache, key, val, ttl=0, being_refreshed=False):
    logger.debug("Attempting to set key=%s in cache for ttl=%s seconds" % (key, ttl))

    real_ttl = time.time() + ttl
    stored_val = (val, real_ttl, being_refreshed)
    return cache.set(key, stored_val)
