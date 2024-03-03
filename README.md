# chat_gpt_code

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
