import time
import random

class BaseSimulator:
    def __init__(self, min_time, max_time):
        self.min_time = min_time
        self.max_time = max_time
    
    def simulate_query(self, query):
        start_time = time.time()
        time.sleep(random.uniform(self.min_time, self.max_time))
        return time.time() - start_time

class RAGSimulator(BaseSimulator):
    def __init__(self):
        super().__init__(0.2, 0.4)

class CacheSimulator(BaseSimulator):
    def __init__(self):
        super().__init__(0.01, 0.1)
