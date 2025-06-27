# Weather Live Wallpaper

A simple Python script that uses the current weather to automatically update your desktop background to a live video or animation using Lively Wallpaper.

*** YOU MUST HAVE Lively Wallpaper INSTALLED ON WINDOWS TO RUN (Available on Microsoft Store) ***

*** ONLY AVAILABLE ON Windows --- Linux Coming Soon ***

## Features
- Fetches current weather using OpenWeatherMap API
- Maps weather conditions to live video URLs
- Sets wallpaper via Lively's CLI
- Cross-platform logic (tested on Windows 10)

## Requirements
- [Lively Wallpaper] (https://github.com/rocksdanister/lively/releases) (Available on Microsoft Store)
- Python 3
- `requests` library (`pip install requests`)

## Usage
1. Ensure you have Python 3 and the `requests` library:
2. Install Lively Wallpaper (Windows only)
   - Go to the Lively GitHub Releases Page
   - Download the latest .exe installer under Assets and run the installer
4. Run python weather_wallpaper.py in bash
5. On first run, the script will ask if you want to use your approximate location based on your IP address.
	- If you say yes, your coordinates will be automatically fetched and saved to your computer.
   - If you say no, the program will close.
7. The script will detect your current weather every 90 seconds and automatically change your wallpaper to match it using live web backgrounds.

## Future ideas
- Add alternate OS functionality
- Add seasonal themes
- Add time of day changes

## License
MIT
