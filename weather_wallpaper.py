import json, requests, pathlib, subprocess, tempfile, textwrap, hashlib, sys

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

# Get user's latitude and longitude using an available API
def get_location():
  response = requests.get("http://ip-api.com/json/", timeout=5) # Temp API
  data = response.json()
  return float(data["lat"]), float(data["lon"])

# Get weather using user's longitude and latitude using an available API
def get_weather(lat, lon):
  #url
  #response = requests.get(url, timeout=5)
  #data = response.json()
  #condition = data[""]
  #return condition
  return "Clear"

# Set wallpaper using Lively via subprocess
def set_wallpaper(url):
  # Create a temp HTML file to wrap a URL in
  tmp_dir = pathlib.Path(tempfile.gettempdir()) / "weather_wp"
  tmp_dir.mkdir(exist_ok=True)
  # Hash URL to create filename
  html_file = tmp_dir / (hashlib.md5(url.encode()).hexdigest() + ".html")

  # Embed the URL in a fullscreen iframe if HTML file doesn't already exist
  if not html_file.exists():
    html_file.write_text(textwrap.dedent(f'''\
      <!doctype html><html><head><meta charset="utf-8">
      <style>html,body{{margin:0;height:100%;background:#000}}</style>
      </head><body>
      <iframe src="https://www.youtube.com/embed/{url}?autoplay=1&controls=0&mute=1&loop=1&rel=0&playlist={url}"
              width="100%" height="100%"
              frameborder="0"
              allow="autoplay;fullscreen"></iframe>
      </body></html>
    '''), encoding="utf-8")

  # CLI arguments
  args = [
      LIVELY_EXE,
      "setwp",
      "--monitor=0",
      f"--file={str(html_file.resolve())}"
  ]

  try:
    subprocess.run(args, check=True)
    print(f"Wallpaper set to: {url}")
  except FileNotFoundError:
    sys.exit("Lively executable not found. Check the LIVELY_EXE path.")
  except subprocess.CalledProcessError as e:
    sys.exit(f"Lively failed to apply wallpaper (exit code {e.returncode}).")

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
    condition = get_weather(conf["lat"], conf["lon"])
    print(f"Current weather: {condition}")
  except Exception as e:
    print("Location error:", e)
    return

  # Set wallpaper if found in WALLPAPER_MAP
  wallpaper_url = WALLPAPER_MAP.get(condition)
  if wallpaper_url:
    set_wallpaper(wallpaper_url)
  else:
    print("No wallpaper mapped for this condition.")

if __name__ == "__main__":
    main()
