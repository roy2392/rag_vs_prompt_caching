from datetime import datetime
import statistics
from simulation import RAGSimulator, CacheSimulator

class PerformanceComparison:
    def __init__(self):
        self.rag_simulator = RAGSimulator()
        self.cache_simulator = CacheSimulator()
        self.rag_results = []
        self.cache_results = []
    
    def run_rag_query(self, query):
        execution_time = self.rag_simulator.simulate_query(query)
        self.rag_results.append({
                'query': query,
                'time': execution_time,
                'timestamp': datetime.now()
        })
        return execution_time
    
    def run_cache_query(self, query):
        execution_time = self.cache_simulator.simulate_query(query)
        self.cache_results.append({
                'query': query,
                'time': execution_time,
                'timestamp': datetime.now()
        })
        return execution_time
    
    def analyze_results(self):
        rag_times = [result['time'] for result in self.rag_results]
        cache_times = [result['time'] for result in self.cache_results]
        
        return {
                'rag_avg': statistics.mean(rag_times),
                'cache_avg': statistics.mean(cache_times),
                'rag_std': statistics.stdev(rag_times) if len(rag_times) > 1 else 0,
                'cache_std': statistics.stdev(cache_times) if len(cache_times) > 1 else 0,
                'improvement': ((statistics.mean(rag_times) - statistics.mean(cache_times))
                                / statistics.mean(rag_times)) * 100
        }
