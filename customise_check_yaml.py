import sys
import yaml

def check_yaml(file_path):
    with open(file_path, 'r') as f:
        content = yaml.safe_load(f)

    if isinstance(content, dict) and 'all' in content:
        if 'host' in content['all']:
            print(f"Error in {file_path}: Found 'host', use 'hosts' instead.")
            sys.exit(1)

if __name__ == "__main__":
    for file in sys.argv[1:]:
        check_yaml(file)
