import apt_pkg

# 初始化 apt_pkg（在任何 apt_pkg 操作前必須初始化）
apt_pkg.init()

# 創建一個 Cache 來獲取套件資訊
cache = apt_pkg.Cache()

# 創建一個 Policy 來處理套件選擇策略
policy = apt_pkg.Policy()

# 選擇要查詢的套件名稱
package_name = "curl"

# 獲取套件物件
pkg = cache[package_name]

# 獲取候選版本（Policy 會自動決定最佳版本）
candidate_version = policy.get_candidate_ver(pkg)

# 顯示候選版本資訊
if candidate_version:
    print(f"候選版本: {candidate_version.ver_str}")
else:
    print("沒有可用的候選版本")
