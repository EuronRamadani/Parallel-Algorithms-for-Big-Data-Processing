# Parallel MapReduce Implementation

This project implements a parallel MapReduce framework in Python, inspired by the Google MapReduce paper. It provides a simple yet powerful way to process large datasets in parallel using the MapReduce programming model.

## Features

- Parallel processing using Python's multiprocessing
- Automatic chunk size estimation based on available memory
- Local aggregation in mappers to reduce communication overhead
- Adaptive partitioning for balanced workload distribution
- Support for custom map and reduce functions
- Example implementations for word count and matrix multiplication

## Project Structure

- `mapreduce.py`: Core MapReduce implementation
- `utils.py`: Helper functions for sampling and partitioning
- `examples.py`: Example MapReduce jobs and test cases

## Requirements

- Python 3.6+
- numpy
- cloudpickle
- psutil
- tqdm
- requests (for example that downloads Moby Dick)

Install dependencies:

```bash
pip install numpy cloudpickle psutil tqdm requests
```

## Usage

1. Import the MapReduce framework:

```python
from mapreduce import ParallelMapReduce
```

2. Define your map and reduce functions:

```python
def map_func(item):
    # Process input item and return list of (key, value) pairs
    return [(key, value) for ...]

def reduce_func(key, values):
    # Process values for a key and return result
    return result
```

3. Create and execute a MapReduce job:

```python
mapreduce = ParallelMapReduce(n_workers=4)
result = mapreduce.execute(dataset, map_func, reduce_func)
```

## Examples

The project includes several example MapReduce jobs:

1. Word Count: Count word frequencies in text documents
2. Matrix Multiplication: Multiply large matrices in parallel

Run the examples:

```bash
python examples.py
```

## Performance Considerations

- The framework automatically estimates optimal chunk sizes based on available memory
- Local aggregation in mappers reduces communication overhead
- Adaptive partitioning helps balance workload across workers
- Number of workers defaults to (CPU count - 1) but can be customized

## License

MIT License
