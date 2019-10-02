from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_magic,
                                cell_magic, line_cell_magic)
import runner

# The class MUST call this class decorator at creation time
@magics_class
class Ansible(Magics):

    @line_magic
    def a_inventory_remove(self, line):
        params = line.split(" ")
        print("Params: ", params)
        d = dict()
        index = 0
        while index < len(params) - 1:
            if params[index] not in d:
                d[params[index]] = []
            d[params[index]].append(params[index+1])
            index = index + 2
        try:
            new_file = []
            with open("/home/tardis/Desktop/Ansible/Runner/inventory/hosts", "r") as hosts:
                raw = hosts.read()
                lines = raw.split("\n")
                curr_key = ""
                for l in lines:
                    if "[" in l and "]" in l:
                        new_file.append(l)
                        curr_key = l.split("]")[0].split("[")[1]
                        continue
                    if curr_key in d:
                        found = False
                        for ele in d[curr_key]:
                            if l == ele:
                                found = True
                                pass
                        if not found:
                            new_file.append(l)
                    else:
                        new_file.append(l)
                hosts.close()
            print("new_file: ", new_file)
            new_file = "\n".join([str(x).encode('utf-8') for x in new_file])
            print("new_file new: ", new_file)
            with open("/home/tardis/Desktop/Ansible/Runner/inventory/hosts", "w") as hosts:
                hosts.write(new_file)
                hosts.close()
                pass
        except Exception as e:
            print(e)
            return False, "Error, can't open hosts file"
        return True, None

    @line_magic
    def a_inventory_add(self, line):
        params = line.split(" ")
        print("Params: ", params)
        d = dict()
        index = 0
        while index < len(params) - 1:
            if params[index] not in d:
                d[params[index]] = []
            d[params[index]].append(params[index+1])
            index = index + 2
        try:
            new_file = []
            with open("/home/tardis/Desktop/Ansible/Runner/inventory/hosts", "r") as hosts:
                raw = hosts.read()
                lines = raw.split("\n")
                for key in d:
                    key_found = False
                    curr_key = ""
                    line_index = 0
                    curr_key_line_index = 0
                    file_length = len(lines)
                    for l in lines:
                        line_index = line_index + 1
                        if "[" in l and "]" in l:
                            curr_key = l.split("]")[0].split("[")[1]
                            curr_key_line_index = line_index
                            print("Current key: ", curr_key, ", adding key: ", key)
                        if l not in new_file:
                            new_file.append(l)
                        if l.find(key) != -1 and curr_key == key:
                            key_found = True
                            for ele in d[key]:
                                found = False
                                for index in range(curr_key_line_index, file_length):
                                    if "[" in lines[index] and "]" in lines[index]:
                                        break
                                    if ele == lines[index]:
                                        found = True
                                if not found:
                                    print("append 1 line")
                                    new_file.append(ele)
                                    file_length = file_length + 1
                    if not key_found:
                        print("append 2 lines")
                        new_file.append("[{}]".format(key))
                        new_file.append("\n".join(d[key]))
                        file_length = file_length + 2
                hosts.close()
            print("new_file: ", new_file)
            new_file = "\n".join([str(x).encode('utf-8') for x in new_file])
            print("new_file new: ", new_file)
            with open("/home/tardis/Desktop/Ansible/Runner/inventory/hosts", "w") as hosts:
                hosts.write(new_file)
                hosts.close()
                pass
        except Exception as e:
            print(e)
            return False, "Error, can't open hosts file"
        return True, None

    @line_magic
    def ansiblel(self, line):
        "my line magic"
        lines = str(line).splitlines()
        print("Split lines: 1. " + str(lines[0]))
        # runner.create_playbook()
        print("Full access to the main IPython object:", self.shell)
        print("Variables in the user namespace:", list(self.shell.user_ns.keys()))
        return line

    @cell_magic
    def ansiblec(self, line, cell):
        "my cell magic"
        lines = str(cell).splitlines()
        runner.create_playbook(lines[0], lines[1:])
        return line, cell

    @line_cell_magic
    def ansiblelc(self, line, cell=None):
        "Magic that works both as %lcmagic and as %%lcmagic"
        if cell is None:
            print("Called as line magic", line, cell)
            return line
        else:
            print("Called as cell magic", line, cell)
            return line, cell

def load_ipython_extension(ipython):
    ipython.register_magics(Ansible)