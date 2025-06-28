# Weather Live Wallpaper

A simple Python script that uses the current weather to automatically update your desktop background to a youtube video using scripting.

*** ONLY AVAILABLE ON Windows ***

## Features
- Fetches current weather using available API
- Maps weather conditions to video URLs
- Sets live wallpaper via scripting

## Requirements
- Windows 10 or 11
- Python 3
- `requests` library (`pip install requests`)

## Usage
1. Ensure you have Python 3 and the `requests` library:
2. Run python weather_wallpaper.py in bash
3. On first run, the script will ask if you want to use your approximate location based on your IP address.
	- If you say yes, your coordinates will be automatically fetched and used to find your local weather.
	- If you say no, the program will close.
4. The script will detect your current weather every 90 seconds and automatically change your wallpaper to match using links to youtube videos.

## Future ideas
- Add alternate OS functionality
- Add seasonal themes
- Add time of day changes

## License
MIT
