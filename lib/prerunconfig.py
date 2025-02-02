from os import getcwd
import json


# prerun directory setup
dir_alias = getcwd()
li_sliced = dir_alias.split('\\')
dir_alias = dir_alias.removesuffix(li_sliced[-1])

config_helper = f"{dir_alias}Data\\settings\\supported_file_types.json"
runner_script = f"{dir_alias}Data\\scripts\\runner.bat"
# currently supported loaded type

with open(config_helper,"r") as f:
    cslt = json.loads(f.read())
class Configure:
    def __init__(self,file_name: str) -> None:
        self.file = file_name
        self.f_name = file_name.split(".")
        self.f_name = "."+self.f_name[-1]
        self.identifier = cslt[self.f_name]
        self.to_write = f"""
@echo off && {self.identifier} {'"'+file_name+'"'} && pause && exit

"""
        if self.identifier != "rl" and self.identifier != "stf":
            with open(runner_script,"w") as f:
                f.write(self.to_write)
            self.controller = "ready"
        else:
            self.controller = "nars"
    def run(self):
        import os
        print('"'+runner_script+'"')
        # os.system('start "'+runner_script+'"')
        os.system('"'+runner_script+'"')
    def file_existance_check(self,file_name):
        self.file = file_name
        self.f_name = file_name.split(".")
        self.f_name = "."+self.f_name[-1]
        self.identifier = cslt.get(self.f_name)
        return self.identifier
