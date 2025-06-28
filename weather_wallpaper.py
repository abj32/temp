import json, requests, subprocess, textwrap, string, secrets, tempfile
from pathlib import Path

# Settings
LIVELY_EXE  = r"C:\Users\aidan\AppData\Local\Programs\Lively Wallpaper\Lively.exe"  # Path to Lively Executable. Change this later to detect path

# Weather condition → wallpaper URL map
WALLPAPER_MAP = {
    "Clear": "ipf7ifVSeDU",         # sunny
    "Clouds": "8KrLtLr-Gy8",        # overcast
    "Rain": "clqYeHdZ1zQ",          # rain
    "Snow": "vz91QpgUjFc",          # snowy
    "Thunderstorm": "gVKEM4K8J8A"   # stormy
}

# Ask user for consent to use location 
def ask_for_location_consent():
  while True:
    answer = input("Allow approximate location lookup by IP? (Y/N): ").strip().lower()
    
    if answer == "y":
      return True
    elif answer == "n":
      return False
    else:
      print("Please enter 'Y' or 'N': ")

# Get user's latitude and longitude using API from ip-api that returns geolocation data for user's public IP
def get_location():
  response = requests.get("http://ip-api.com/json/", timeout=5) # Temp API
  data = response.json()
  print(data["city"])
  return float(data["lat"]), float(data["lon"])

# Get weather using user's longitude and latitude using an available API
def get_weather(lat, lon):
  #url
  #response = requests.get(url, timeout=5)
  #data = response.json()
  #condition = data[""]
  #return condition
  return "Clear"

def generate_lively_id():
  alphabet = string.ascii_lowercase + string.digits
  first  = ''.join(secrets.choice(alphabet) for _ in range(8))
  second = ''.join(secrets.choice(alphabet) for _ in range(3))
  return f"{first}.{second}"

# Set wallpaper using AHK to re-parent an opened window
def set_wallpaper(video_id):
  # Create unique folder in wallpaper path
  tmp_dir = Path(tempfile.gettempdir()) / "youtube_wallpaper"
  tmp_dir.mkdir(parents=True, exist_ok=True)

  # Embed youtube video in HTML wrapper and add to directory
  index_path = tmp_dir / "index.html"
  index_html = textwrap.dedent(f'''\
        <!DOCTYPE html><html><body style="margin:0;background:#000;">
          <iframe src="https://www.youtube.com/embed/{video_id}?autoplay=1&mute=1&loop=1&controls=0&rel=0&start=5&playlist={video_id}"
                  allow="autoplay; fullscreen"
                  style="position:absolute;width:100vw;height:100vh;border:none;">
          </iframe>
        </body></html>
  ''')
  index_path.write_text(index_html, encoding="utf-8")

  # 3) Launch Edge in frameless app mode
  html_url = f"file:///{index_path.resolve().as_posix()}"
  subprocess.Popen([
      r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
      f"--app={html_url}",
      "--start-fullscreen"
  ])

# Main
def main():
  consent = ask_for_location_consent()

  # Exit program if location consent not given
  if not consent:
    print("Location permission not granted. Exiting.")
    return

  # Get user latitude and longitude
  try:
    lat, lon = get_location()
  except Exception as e:
    print("Location error:", e)
    return

  # Get user weather
  try:
    condition = get_weather(lat, lon)
    print(f"Current weather: {condition}")
  except Exception as e:
    print("Location error:", e)
    return

  # Set wallpaper if found in WALLPAPER_MAP
  wallpaper_id = WALLPAPER_MAP.get(condition)
  if wallpaper_id:
    set_wallpaper(wallpaper_id)
  else:
    print("No wallpaper mapped for this condition.")

if __name__ == "__main__":
    main()
