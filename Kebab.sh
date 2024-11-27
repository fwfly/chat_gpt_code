#!/bin/bash

# 指定要檢查的目錄，預設為當前目錄
TARGET_DIR=${1:-.}

# 定義符合 kebab-case 的正則表達式
KEBAB_REGEX='^[a-z0-9]+(-[a-z0-9]+)*$'

# 遍歷資料夾中的所有檔案
echo "Checking files in: $TARGET_DIR"
INVALID_FILES=0

for FILE in "$TARGET_DIR"/*; do
    # 獲取檔案名稱
    BASENAME=$(basename "$FILE")
    
    # 檢查是否符合 kebab-case
    if [[ ! $BASENAME =~ $KEBAB_REGEX ]]; then
        echo "Invalid file name: $BASENAME"
        ((INVALID_FILES++))
    fi
done

if [[ $INVALID_FILES -eq 0 ]]; then
    echo "All file names are valid."
else
    echo "$INVALID_FILES invalid file name(s) found."
fi
