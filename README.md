# CLI Audio Recorder

This CLI Audio Recorder is a Python-based tool designed to record MP3 audio streams from the internet. 

## Features
- Record MP3 streams directly from provided URLs.
- Customize the recording duration.
- Specify output filenames (default includes timestamp).
- Adjust block size for reading and writing data.
- Built-in help and usage information.

## Installation

Clone the repository:

```bash
git clone https://github.com/sophie4075/cli_audiorecorder.git 
cd audiorecorder
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Basic syntax:

```bash
python cli_audiorecorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]
```

### Examples

Record a stream with default settings (30 seconds duration, 64 bytes block size, timestamped filename):

```bash
python cli_audiorecorder.py http://example.com/stream
```

Record a stream with custom filename, duration, and block size:

```bash
python cli_audiorecorder.py http://example.com/stream --filename=myRecording --duration=60 --blocksize=128
```

Display help information:

```bash
python cli_audiorecorder.py --help
```

## Command Line Options

```
Usage:
  cli_audiorecorder.py <url> [--filename=<name>] [--duration=<time>] [--blocksize=<size>]

Options:
  url                   URL of the MP3 stream you want to record.
  --filename=<name>     Name of the saved recording (default: myRadioRecordingTIMESTAMP.mp3).
  --duration=<time>     Recording duration in seconds (default: 30).
  --blocksize=<size>    Block size for read/write operations in bytes (default: 64).
```

## Dependencies
- Python 3.x
- Packages: argparse, requests
- Additional dependencies listed in `requirements.txt`.


## Credits

Resources:
- [Python Argparse Documentation](https://docs.python.org/3/library/argparse.html)
- [Recording and Saving Internet Radio in Python](https://stackoverflow.com/questions/4247248/record-streaming-and-saving-internet-radio-in-python)
- [Common MIME Types](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types)

