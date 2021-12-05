import os
import yaml
from pprint import pprint

"""
Exercise 02: Deploy
There is a list of tasks (todo.yml) that should be placed in a generated "deploy.yml" file in YAML format:
 - Install packages
 - Copy over files
 - Run files on a remote server with a Python interpreter, specifying corresponding arguments
These tasks should be generated in Ansible notation.
"""

this_path = os.getcwd()
path = '/etc'
full_path_file = os.path.join(os.path.dirname(this_path), 'todo.yml')
with open(full_path_file) as fp:
    todo = yaml.safe_load(fp)

# pprint(todo)

server = todo.get('server', {})
files = server.get('exploit_files', [])
packages = server.get('install_packages', [])
bad_guys = todo.get('bad_guys', [])
arguments = ','.join(guy for guy in bad_guys)

tasks = []
to_yaml = {"hosts": "all",
           "tasks": tasks
           }

for pack in packages:
    task = {"name": f'Install {pack}', "apt": {"pkg": pack, "state": "latest"}}
    tasks.append(task)


for file in files:
    task = {"name": f'Copy {file} to remote locations',
            "copy": f'src={os.path.join(this_path, file)} dest={os.path.join(path, file)} mode=0644'}
    tasks.append(task)

for file in files:
    if file == 'consumer.py':
        task = {"name": f'Run {file} on a remote server with a Python interpreter, specifying corresponding arguments',
                "command": f'python3 {file} -e {arguments}'}
    else:
        task = {"name": f'Run {file} on a remote server with a Python interpreter',
                "command": f'python3 {file}'}
    tasks.append(task)


"""
Ansible notation
example of installing packages

- hosts: all
  tasks:
    - name: Install python3
      apt: pkg=python3 state=latest
      
    - name: Install nginx
      apt: pkg=nginx state=latest
           
      or 
      
    - name: Installs necessary packages
      apt: pkg={{ item }} state=latest
      with_items:
        - python3
        - nginx
        
        
example of copying file

    - name: Copy file exploit.py to remote locations
      copy: src={os.path.join(this_path, 'exploit.py')}  dest=/etc/exploit.py  mode=0644
    
example of running files   
      
    - name: Run exploit.py on a remote server with a Python interpreter
      command: python3 exploit.py
      
    - name: Run consumer.py on a remote server with a Python interpreter
      command: python3 consumer.py -e 'bad_guys'
    
"""


full_path_task_file = os.path.join(os.path.dirname(this_path), 'deploy.yml')
with open(full_path_task_file, "w") as fp:
    yaml.safe_dump(to_yaml, fp)


# if __name__ == "__main__":
#     pprint(to_yaml)