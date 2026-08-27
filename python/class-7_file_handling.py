from pathlib import Path
import json

# Define project directories using the / operator
BASE_DIR = Path.cwd() / "class_data"
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"


profile = {
    "agent_name": "Antigravity Research Assistant",
    "version": 2.0,
    "tools": ["web_search", "code_execution", "file_analysis"],
    "is_active": True,
    "temperature": 0.2,
    "metadata": None
}

profile_json_path = DATA_DIR / "agent_config.json"
profile = "data\agent_config.json"

# Write to JSON file with indentation
with open(profile_json_path, "w", encoding="utf-8") as file:
    json.dump(profile, file, indent=1)

print("Saved JSON configuration:")
print(profile_json_path.read_text(encoding="utf-8"))

# Read back from JSON file
with open(profile_json_path, "r", encoding="utf-8") as file:
    loaded_config = json.load(file)

print("Loaded agent name:", loaded_config["agent_name"])
print("Loaded tools:", loaded_config["tools"])