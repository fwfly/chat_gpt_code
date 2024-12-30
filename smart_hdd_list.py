import subprocess
import json
import sys

import re

def parse_report_line_by_line(lines):
    # 定義正則表達式來匹配目標行
    pattern = r"(\d+):(\d+)\s+(\d+)\s+(\w+)"
    result = []

    # 遍歷每一行並匹配
    for line in lines:
        match = re.search(pattern, line)
        if match:
            eid, slt, _, state = match.groups()  # 提取所需欄位
            result.append({"EID": eid, "Slt": slt, "State": state})
    
    return result


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError:
        return None

def parse_samrctl(output):
    # Placeholder: Adjust parsing logic based on samrctl output format
    return [
        {"capacity": "1TB", "serial": "ABC123", "error": "None"},
        {"capacity": "2TB", "serial": "DEF456", "error": "Error"}
    ]

def parse_ssacli(output):
    # Placeholder: Adjust parsing logic based on ssacli output format
    return [
        {"capacity": "1TB", "serial": "ABC123", "error": "None"},
        {"capacity": "2TB", "serial": "DEF456", "error": "Error"}
    ]

def parse_perccli(output):
    # Placeholder: Adjust parsing logic based on perccli output format
    return [
        {"capacity": "1TB", "serial": "ABC123", "error": "None"},
        {"capacity": "2TB", "serial": "DEF456", "error": "Error"}
    ]

def get_hdd_list():
    commands = [
        ("samrctl show drives", parse_samrctl),
        ("ssacli ctrl all show config", parse_ssacli),
        ("perccli /c0 /eall /sall show", parse_perccli),
    ]

    for command, parser in commands:
        print(f"Trying command: {command}")
        output = run_command(command)
        if output:
            try:
                return parser(output)
            except Exception as e:
                print(f"Failed to parse output from {command}: {e}")
    
    print("All commands failed.")
    return []

def main():
    hdd_list = get_hdd_list()
    if hdd_list:
        print(json.dumps(hdd_list, indent=4))
    else:
        print("No HDD information could be retrieved.")

if __name__ == "__main__":
    main()
