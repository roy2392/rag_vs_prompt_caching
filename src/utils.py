def print_results(query, rag_time, cache_time):
    print(f"📊 {query}:")
    print(f"   RAG: {rag_time:.3f} שניות")
    print(f"   קאש: {cache_time:.3f} שניות")

def print_final_results(results):
    print("\n📈 תוצאות סופיות:")
    print(f"זמן ממוצע RAG: {results['rag_avg']:.3f} שניות")
    print(f"זמן ממוצע קאש: {results['cache_avg']:.3f} שניות")
    print(f"שיפור בביצועים: {results['improvement']:.1f}%")
