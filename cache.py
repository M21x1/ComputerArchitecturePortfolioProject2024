import collections

CACHE_SIZE = 16

class Cache:
    def __init__(self):
        self.cache = collections.deque(maxlen=CACHE_SIZE)
        self.flush_cache()
        
    
    def flush_cache(self):
        for i in range(CACHE_SIZE):
            self.cache.append(("", ""))
    
    def search_cache(self, address):
        for item in self.cache:
            if item[0] == address:
                return item[1]
        return None
    
    def write_cache(self, address, value):
        self.cache.append((address, value))