# Quellen:
# https://docs.python.org/3/library/argparse.html
# https://stackoverflow.com/questions/4247248/record-streaming-and-saving-internet-radio-in-python
# https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types

import argparse
import requests
import time


def cli_record_parser():
    parser = argparse.ArgumentParser(
        prog='CLI Audio recorder',
        description='''
        You can use this audio recorder to record MP3 streams from the Web. 
        Enter the URL of a stream (please make sure it's a mp3 stream) and the recorder saves the data in an MP3 file. 
        You can customise the recording duration, the file name and the block size for data processing.
        ''',
        epilog='''
        For example:
        1. Simple recording with the URL:  
           python cli_audiorecorder.py http://example.com/stream
           
        2. Recording with user-defined file name, duration and chunk size :
           python cli_audiorecorder.py http://example.com/stream --filename=radioRecord --duration=60 --blocksize=128
           
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('url', type=str, help='URL of the MP3-Stream, you would like to record')

    default_filename = 'myRadioRecording' + time.strftime("%Y%m%d_%H%M%S")
    parser.add_argument('--filename', type=str, default=default_filename,
                        help=f'Name of the saved file (Default: myRadioRecordingTIMESTAMP.mp3)')

    parser.add_argument('--duration', type=int, default=30, help='Recording duration (Default: 30 seconds)')
    parser.add_argument('--blocksize', type=int, default=64,
                        help='Block size for read/write operations in bytes  (Default: 64)')

    return parser


def record_mp3_stream(url, filename, duration, block_size):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        content_type = response.headers.get('Content-Type')
        if content_type not in ['audio/mpeg', 'audio/mp3']:
            print(f"Audio-Stream type not supported: {content_type}")
            return

        print("Stream looks okay. Start recording...")
        with open(filename + '.mp3', 'wb') as file:
            start_time = time.time()
            for block in response.iter_content(block_size):
                file.write(block)
                elapsed_time = time.time() - start_time
                if elapsed_time > duration:
                    break
                    
        print(f"Finshed recording: {filename}.mp3")

    except requests.exceptions.RequestException as e:
        print(f":( - Something went wrong: {e}")


def main():
    parser = cli_record_parser()
    args = parser.parse_args()

    print(f"Start recording {args.url} for {args.duration} seconds...")
    record_mp3_stream(args.url, args.filename, args.duration, args.blocksize)


if __name__ == "__main__":
    main()
