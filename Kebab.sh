#!/bin/bash

# 指定要檢查的目錄，預設為當前目錄
TARGET_DIR=${1:-.}

# 定義符合 kebab-case 的正則表達式
KEBAB_REGEX='^[a-z0-9]+(-[a-z0-9]+)*$'

# 初始化無效名稱計數
INVALID_NAMES=0

# 遞迴檢查檔案和資料夾名稱
check_kebab_case() {
    local DIR="$1"
    
    echo "Checking directory: $DIR"
    
    for ITEM in "$DIR"/*; do
        # 忽略 README.md
        if [[ $(basename "$ITEM") == "README.md" ]]; then
            continue
        fi
        
        # 獲取名稱
        BASENAME=$(basename "$ITEM")
        
        # 檢查是否符合 kebab-case
        if [[ ! $BASENAME =~ $KEBAB_REGEX ]]; then
            echo "Invalid name: $ITEM"
            ((INVALID_NAMES++))
        fi
        
        # 如果是目錄，遞迴進行檢查
        if [[ -d "$ITEM" ]]; then
            check_kebab_case "$ITEM"
        fi
    done
}

# 執行檢查
check_kebab_case "$TARGET_DIR"

# 結果輸出
if [[ $INVALID_NAMES -eq 0 ]]; then
    echo "All file and directory names are valid."
else
    echo "$INVALID_NAMES invalid name(s) found."
fi
