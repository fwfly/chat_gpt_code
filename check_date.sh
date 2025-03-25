#!/bin/bash
set -e

BASE_BRANCH="origin/main"

changed_files=$(git diff --name-only ${BASE_BRANCH}...HEAD | grep -E '\.ya?ml$|\.json$' || true)

if [[ -z "$changed_files" ]]; then
  echo "✅ No config files changed."
  exit 0
fi

echo "🔍 Checking the following config files:"
echo "$changed_files"

error=0
for file in $changed_files; do
  echo "➡️  Checking $file"
  python3 check_date.py "$file" || error=1
done

if [[ $error -eq 1 ]]; then
  echo "❌ Date check failed."
  exit 1
else
  echo "✅ All date checks passed."
fi
