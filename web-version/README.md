# Parallel MapReduce - Web Version

This is the web interface version of the Parallel MapReduce implementation, which provides a user-friendly web interface for processing text files and viewing results.

## Features

- Modern web interface for file uploads and result display
- Parallel processing using Python's multiprocessing
- Interactive results display with sorting and statistics
- Support for custom worker count configuration

## Project Structure

- `mapreduce.py`: Core MapReduce implementation
- `app.py`: Flask web application
- `static/`: Frontend files
  - `index.html`: Main web interface
  - `styles.css`: Custom styling
  - `script.js`: Frontend JavaScript
- `uploads/`: Temporary directory for file uploads
- Sample text files:
  - `small_text.txt`: Small sample text file
  - `medium_text.txt`: Medium sample text file
  - `large_text.txt`: Large sample text file

## Requirements

- Python 3.6+
- Flask
- Flask-CORS
- Python-dotenv

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask server:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

3. Use the web interface to:
   - Upload text files
   - Configure number of workers (1-16)
   - View word count results in a sortable table
   - See statistics about the processing

## Performance

- Configurable number of workers (1-16)
- Real-time progress updates
- Efficient parallel processing
- Local aggregation in mappers to reduce communication overhead
