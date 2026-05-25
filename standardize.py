import os
import glob
import re

files = glob.glob('blueprints/*.py')

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Replace {"error": "msg"} with {"status": "error", "message": "msg"}
    # Need to handle {"error": str(e)} and {"error": "..."}
    # This regex looks for jsonify({"error": <something>}) and if there is no status, it adds it.
    
    # A simple trick: Replace 'jsonify({"error": ' with 'jsonify({"status": "error", "message": '
    # But some have 'jsonify({"error": ..., "detail": ...})'
    # By changing "error" to "message" and adding "status": "error", we preserve detail.
    
    # Let's do it with regex:
    # Match: jsonify({"error": 
    # Replace: jsonify({"status": "error", "message": 
    content = re.sub(r'jsonify\(\{\s*"error"\s*:', r'jsonify({"status": "error", "message":', content)
    
    # Also standardize the auth get_me to include data envelope if needed, or leave it as is if it has "status": "success".
    # Same for detection stats.
    content = re.sub(r'jsonify\(\{"total_detections"', r'jsonify({"status": "success", "total_detections"', content)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
        
print("Standardized jsonify responses.")
