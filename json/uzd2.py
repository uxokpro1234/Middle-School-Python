import json

config = {
    "window_size": (800, 600),
    "fullscreen": False,
    "volume": 0.5
}
try:
  with open("config.json", "r") as f:
      config = json.load(f)
except:
  print("Creating config...")

with open("config.json", "w") as f:
    json.dump(config, f)


print(config)

