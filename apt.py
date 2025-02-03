import apt

# 創建 APT 快取物件
cache = apt.Cache()

# 選擇要查詢的套件名稱
package_name = "curl"

# 檢查套件是否存在於快取中
if package_name in cache:
    pkg = cache[package_name]
    print(f"套件名稱: {pkg.name}")
    print(f"是否已安裝: {pkg.is_installed}")
    print(f"候選版本: {pkg.candidate.version}")
else:
    print(f"套件 {package_name} 不在快取中")
