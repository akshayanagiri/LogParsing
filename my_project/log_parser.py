import re
import base64
import json
import os
import pandas as pd


def save_base64_image(base64_data, file_name):
    try:
       
        image_data = base64.b64decode(base64_data)
        with open(file_name, 'wb') as image_file:
            image_file.write(image_data)
        print(f"Image saved as {file_name}")
    except Exception as e:
        print(f"Error saving image: {e}")


def parse_log_entry(log_entry):
 
    log_patterns = {
        "basic_log": re.compile(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d+)\s+([A-Za-z]+)=([^\s]+)\s+([A-Za-z]+)=([^\s]+)\s+([A-Za-z]+)=([^\s]+)'),
        "json_log": re.compile(r'({.*})'),
        "base64_log": re.compile(r'BASE64:([A-Za-z0-9+/=]+)')
    }

    try:
       
        basic_match = log_patterns['basic_log'].search(log_entry)
        if basic_match:
            return {
                "timestamp": basic_match.group(1),
                "user": basic_match.group(3),
                "ip": basic_match.group(5),
                "action": basic_match.group(7)
            }

      
        json_match = log_patterns['json_log'].search(log_entry)
        if json_match:
            try:
                return json.loads(json_match.group(1))
            except json.JSONDecodeError as e:
                print(f"Invalid JSON found: {json_match.group(1)}")
                return {"error": "Invalid JSON", "raw": json_match.group(1)}

        base64_match = log_patterns['base64_log'].search(log_entry)
        if base64_match:
            try:
                base64_data = base64_match.group(1)
                
                
                file_name = f"decoded_image_{hash(base64_data)}.jpg"
                
                
                save_base64_image(base64_data, file_name)
                
                return {"status": "Image saved", "file_name": file_name}

            except (base64.binascii.Error) as e:
                print(f"Error decoding Base64: {base64_match.group(1)}")
                return {"error": "Invalid Base64", "raw": base64_match.group(1)}

    except Exception as e:
        print(f"Unexpected error parsing log: {log_entry}")
        print(f"Error details: {e}")
        return {"error": "Unexpected error", "raw": log_entry}

    return None


def parse_log_file(file_path):
    parsed_data = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  
            if line: 
                parsed_entry = parse_log_entry(line)
                if parsed_entry:
                    parsed_data.append(parsed_entry)
    
    
    return pd.DataFrame(parsed_data)

log_file_path = r"D:\my_project\assessment.log"


parsed_df = parse_log_file(log_file_path)


print(parsed_df)


output_file =  r"D:\my_project\parsed_log_output.csv"
parsed_df.to_csv(output_file, index=False)
print(f"Parsed log data saved to: {output_file}")
