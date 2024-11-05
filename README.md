# RAG vs Cache Performance Comparison 🚀

## Overview
This project provides a comprehensive performance comparison between Retrieval-Augmented Generation (RAG) and Prompt Caching approaches in AI applications. It simulates and analyzes the execution times and efficiency of both methods.

## Project Structure 📁
```bash
rag-cache-comparison/
│
├── src/
│   ├── performance_comparison.py
│   ├── simulation.py
│   ├── utils.py
│   ├── experiment.py
│   └── main.py
│
├── tests/
│   └── test_performance.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Features ✨
	•	Simulated performance testing of RAG and Cache approaches
	•	Statistical analysis of execution times
	•	Detailed performance metrics and comparisons
	•	Modular and extensible codebase
	•	Comprehensive logging and results visualization

## Installation 🔧
# Clone the repository
```bash
git clone https://github.com/yourusername/rag-cache-comparison.git
cd rag-cache-comparison
```

# Create and activate virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

# Install dependencies
```bash
pip install -r requirements.txt
```

## Usage 🎯
# Run the main comparison
```bash
python src/main.py
```

# To run with custom parameters
from src.experiment import run_experiment
run_experiment(num_queries=20)  # Specify number of test queries

## Results Output 📊
The program outputs detailed performance metrics including:
	•	Individual query execution times
	•	Average processing times for both methods
	•	Performance improvement percentages
	•	Statistical analysis of results
Example output:
```bash
🏃‍♂️ Running comparison experiment...
📊 Query 1:
   RAG: 0.300 seconds
   Cache: 0.050 seconds
...
📈 Final Results:
Average RAG time: 0.300 seconds
Average Cache time: 0.050 seconds
Performance improvement: 83.3%
```
## Contact 📫
	•	GitHub: @roeyzalta
	•	LinkedIn: Roey Zalta
Made with ❤️ by Roey Zalta