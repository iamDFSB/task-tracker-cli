import json
from pathlib import Path

def get_database_data(file_path: Path) -> dict:
    if not file_path.exists():
        return {"length": 0, "contents": []}
    
    with open(file_path, "r") as f:
        data = f.read()
        if not data:
            return {"length": 0, "contents": []}
        
        return json.loads(data)

 
def save_database_data(data: dict, file_path: Path):    
    with open(file_path, "w") as f:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))