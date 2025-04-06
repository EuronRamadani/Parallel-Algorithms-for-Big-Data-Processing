# Parallel MapReduce Implementation

This project implements a parallel MapReduce framework in Python, inspired by the Google MapReduce paper. It provides a simple yet powerful way to process large datasets in parallel using the MapReduce programming model.

## Project Versions

The project includes two implementations:

### 1. Console Version

Located in the `console-version/` directory, this implementation:

- Provides command-line interface
- Has no external dependencies
- Outputs results directly to console
- Perfect for scripting and automation

### 2. Web Version

Located in the `web-version/` directory, this implementation:

- Provides a modern web interface
- Allows file uploads through browser
- Shows interactive results
- Includes configurable worker count
- Requires Flask and related dependencies

## Getting Started

### Console Version

```bash
cd console-version
python examples.py small_text.txt
```

See `console-version/README.md` for more details.

### Web Version

```bash
cd web-version
pip install -r requirements.txt
python app.py
```

Then open `http://localhost:5000` in your browser.
See `web-version/README.md` for more details.

## Features

Both versions include:

- Parallel processing using Python's multiprocessing
- Efficient word count implementation
- Support for custom map and reduce functions
- Local aggregation in mappers to reduce communication overhead
- Configurable number of worker processes

## Project Structure

- `mapreduce.py`: Core MapReduce implementation
- `examples.py`: Example word count implementation
- Text files for testing:
  - `small_text.txt`: Small sample text file
  - `medium_text.txt`: Medium sample text file
  - `large_text.txt`: Large sample text file

## Requirements

- Python 3.6+
- No external dependencies required

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

## Running the Word Count Example

The project includes a word count example that can be run on any text file. To run it:

```bash
python examples.py [input_file]
```

If no input file is specified, it will default to using 'input.txt'.

Example usage:

```bash
# Run on small text file
python examples.py small_text.txt

# Run on medium text file
python examples.py medium_text.txt

# Run on large text file
python examples.py large_text.txt
```

The output will show the word count for each word in the text file, sorted alphabetically.

## Performance Considerations

- The framework uses multiprocessing for parallel execution
- Number of workers defaults to (CPU count - 1) but can be customized
- The implementation includes local aggregation in mappers to reduce communication overhead

## License

MIT License
