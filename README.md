
# Subtitle Syncer

Subtitle Syncer is a lightweight Python tool designed to fix desynchronized subtitle files (`.srt`) by shifting the timings either forward or backward. It's an easy-to-use solution for ensuring your subtitles perfectly align with your media.

## Features

- Adjust subtitle timing by specifying a time shift in milliseconds.
- Shift subtitles forward or backward effortlessly.
- Command-line interface for quick and convenient usage.

## Usage

To use the tool, simply run the following command:

    ```
    python3 main.py <filename.srt> <time_shift_in_milliseconds> <direction>
    ```
    
    Parameters

    <filename.srt>: The path to your subtitle file.
    <time_shift_in_milliseconds>: The amount of time (in milliseconds) to shift the subtitles.
    <direction>: Specify forward to move the subtitles forward or backward to move them backward.


    Example

    If your subtitles are delayed by 2 seconds, you can fix them with:
        
        ```
        python3 main.py my_movie.srt 2000 forward
        ```

    Or, if they appear too early by 3 seconds:

        ```
        python3 main.py my_movie.srt 3000 backward
        ```

## Installation

    1.Clone this repository:
        
        ```
        git clone https://github.com/yourusername/subtitle-syncer.git
        cd subtitle-syncer
        ```

    2.Ensure you have Python 3 installed.
    3.Run the script using the provided instructions.

## How It Works

Subtitle Syncer parses your .srt file, adjusts the timings of each subtitle entry by the specified amount, and saves the synchronized file as a new .srt file. Your original file remains untouched.

## Contribution

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License.