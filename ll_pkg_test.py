import apt
import apt_pkg

apt_pkg.init()
cache = apt.Cache()
low_level_cache = cache._cache

# 需要檢查的套件列表
packages = ["curl", "vim", "git"]

for pkgname in packages:
    if pkgname in low_level_cache:
        ll_pkg = low_level_cache[pkgname]
        if ll_pkg.current_state == apt_pkg.CURSTATE_INSTALLED:
            print(f"✅ {pkgname} 已安裝")
        else:
            print(f"❌ {pkgname} 未安裝 (狀態碼: {ll_pkg.current_state})")
    else:
        print(f"❌ {pkgname} 不存在於快取")
