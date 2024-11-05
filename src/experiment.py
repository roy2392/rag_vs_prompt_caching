from performance_comparison import PerformanceComparison
from utils import print_results, print_final_results

def run_experiment(num_queries=10):
    comparison = PerformanceComparison()
    test_queries = [f"שאילתה {i}" for i in range(num_queries)]
    
    print("🏃‍♂️ מריץ ניסוי השוואתי...")
    for query in test_queries:
        rag_time = comparison.run_rag_query(query)
        cache_time = comparison.run_cache_query(query)
        print_results(query, rag_time, cache_time)
    
    results = comparison.analyze_results()
    print_final_results(results)
