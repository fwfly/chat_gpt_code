https://www.brendangregg.com/blog/2024-03-24/linux-crisis-tools.html?fbclid=IwAR2CBV7dPdD0cWxn6dYjjx7Hma_cC6_dzcNeeqd8thZxtFr-vjNxlLKyZDQ


# chat_gpt_code

輸出 yaml template
```bash
#!/bin/bash

# 定義輸入的專案名稱列表
projects="p1 p2 p3 p4"

# 定義輸出的 YAML 文件名稱
output_file="projects.yaml"

# 清空或創建輸出文件
> $output_file

# 定義 YAML 模板
template() {
  cat <<EOF
test-$1:
   name: $1
   domiain: xxxx
EOF
}

# 迭代每個專案名稱並生成對應的 YAML 配置
for project in $projects; do
  template $project >> $output_file
done

echo "YAML file generated: $output_file"
```

```python
# 引入所需的模組
import os

# 打開1025個文件
file_handles = []
try:
    for i in range(1025):
        # 使用open函數打開文件，'w'表示寫入模式，文件名使用迴圈的計數器以確保每個文件名不同
        file_handle = open(f'file_{i}.txt', 'w')
        file_handles.append(file_handle)
        print(f"打開文件 file_{i}.txt")
except Exception as e:
    print("發生錯誤：", e)

# 不要關閉文件，讓它們保持打開狀態

# 最後，提示文件已經打開並等待用戶輸入以退出程序
input("1025個文件已經打開，按 Enter 以退出程序...")
```

```python
import os
import sys
import yaml
import csv

def read_yaml_files(folder_path):
    nodes_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.yaml'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                yaml_data = yaml.safe_load(file)
                if 'nodes' in yaml_data:
                    nodes_list.extend(yaml_data['nodes'])
    return nodes_list

def filter_nodes(nodes_list, keywords):
    filtered_nodes = []
    for node in nodes_list:
        for keyword in keywords:
            if keyword in node:
                filtered_nodes.append(node)
                break  # Break the inner loop if one keyword matches
    return filtered_nodes

def output_to_list(nodes_list):
    for node in nodes_list:
        print(node)

def output_to_csv(nodes_list, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for node in nodes_list:
            writer.writerow([node])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <keyword1> <keyword2> ...")
        sys.exit(1)

    keywords = sys.argv[1:]
    folder_path = "/your/folder/path"  # Folder path predefined as a fixed value, you can modify it to your folder path

    nodes_list = read_yaml_files(folder_path)

    if not nodes_list:
        print("No YAML files found or no 'nodes' in the files.")
    else:
        filtered_nodes = filter_nodes(nodes_list, keywords)

        if not filtered_nodes:
            print("No items matching the criteria.")
        else:
            output_format = input("Select output format (list/csv): ")
            if output_format.lower() == 'list':
                output_to_list(filtered_nodes)
            elif output_format.lower() == 'csv':
                output_file = input("Enter the path and name of the CSV file: ")
                output_to_csv(filtered_nodes, output_file)
            else:
                print("Invalid output format.")

```
