import sys
import os
import yaml
import pytest
from types import SimpleNamespace
from pathlib import Path

# 插入 plugin 路徑
sys.path.insert(0, os.path.abspath("role/foo/bar/action_plugins"))

from my_plugin import ActionModule


def load_yaml(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


@pytest.mark.parametrize("data1_file, data2_file, expect_error", [
    ("data1.yaml", "data2.yaml", False),  # 正常 case
    ("data1.yaml", "data3.yaml", True),   # 錯誤 case
])
def test_plugin_with_various_data(data1_file, data2_file, expect_error):
    base = Path(__file__).parent / "test_data" / "my_plugin_test"
    data1 = load_yaml(base / data1_file)
    data2 = load_yaml(base / data2_file)

    plugin = ActionModule(
        task=None,
        connection=None,
        play_context=None,
        loader=None,
        templar=None,
        shared_loader_obj=None,
    )
    plugin._task = SimpleNamespace(args={"data1": data1, "data2": data2})

    if expect_error:
        with pytest.raises(Exception):
            plugin.run()
    else:
        result = plugin.run()
        assert result["changed"] is False
        assert result["data1"]["name"] == "test-config"
        assert result["data2"]["config"]["enabled"] is True
