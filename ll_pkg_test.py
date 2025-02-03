import apt
import apt_pkg
import argparse

# Initialize APT
apt_pkg.init()

# Load cache
cache = apt.Cache()
low_level_cache = cache._cache

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Check APT package statuses.")
parser.add_argument("packages", nargs="+", help="List of package names to check.")
args = parser.parse_args()

# Function to get package status
def get_package_status(pkgname):
    if pkgname in low_level_cache:
        ll_pkg = low_level_cache[pkgname]
        if ll_pkg.current_state == apt_pkg.CURSTATE_INSTALLED:
            print(f"✅ {pkgname} is installed")
        else:
            print(f"❌ {pkgname} is not installed (Status Code: {ll_pkg.current_state})")
    else:
        print(f"❌ {pkgname} is not found in APT cache")

# Check each package from arguments
for pkgname in args.packages:
    get_package_status(pkgname)
