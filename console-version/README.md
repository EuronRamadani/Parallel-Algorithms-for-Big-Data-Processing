# Parallel MapReduce - Console Version

This is the console version of the Parallel MapReduce implementation, which processes text files and outputs results to the console.

## Features

- Parallel processing using Python's multiprocessing
- Simple and efficient word count implementation
- Support for custom map and reduce functions
- Console-based output of results

## Project Structure

- `mapreduce.py`: Core MapReduce implementation
- `examples.py`: Example word count implementation
- Sample text files:
  - `small_text.txt`: Small sample text file
  - `medium_text.txt`: Medium sample text file
  - `large_text.txt`: Large sample text file

## Requirements

- Python 3.6+
- No external dependencies required

## Usage

Run the word count example on any text file:

```bash
python examples.py [input_file]
```

Example usage:

```bash
# Run on small text file
python examples.py small_text.txt

# Run on medium text file
python examples.py medium_text.txt

# Run on large text file
python examples.py large_text.txt
```

The output will show the word count for each word in the text file, sorted alphabetically in the console.

## Performance

- Number of workers defaults to (CPU count - 1)
- The implementation includes local aggregation in mappers to reduce communication overhead
