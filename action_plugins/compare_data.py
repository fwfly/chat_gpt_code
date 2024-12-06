from ansible.plugins.action import ActionBase
from ansible.errors import AnsibleActionFail

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        # Get parameters from the playbook task
        data1 = self._task.args.get('data1')
        data2 = self._task.args.get('data2')

        # Validate input
        if not isinstance(data1, dict) or not isinstance(data2, dict):
            raise AnsibleActionFail("Both data1 and data2 must be dictionaries.")

        # Compare data
        if data1 != data2:
            diff = {
                "data1_only": {k: v for k, v in data1.items() if k not in data2},
                "data2_only": {k: v for k, v in data2.items() if k not in data1},
            }
            raise AnsibleActionFail(f"Data mismatch:\n{diff}")

        return {"changed": False, "msg": "Datasets are identical."}



#- name: Compare two datasets using custom plugin
#  example_role.compare_data:
#    data1: "{{ data1 }}"
#    data2: "{{ data2 }}"
