import ansible_runner
import yaml

def create_playbook(task_name="Some task", shell_code=["touch awesome_script.py"]):
    tasks = [{
        "name": str(task_name),
        "shell": str(code)
    } for code in shell_code]
    # data = [
    #     {
    #         "hosts": "ubuntu@54.193.67.251",
    #         "tasks": [
    #             {
    #                 "name": str(task_name), # "Create new file",
    #                 "shell": str(shell_code) # "touch hello_runner.txt; echo \"Hello World from yaml converter\" > hello_runner.txt;"
    #             }
    #         ]
    #     }
    # ]
    data = [
        {
            # "hosts": "ubuntu@54.193.67.251",
            "hosts": "linux",
            "tasks": tasks
        }
    ]

    # stream = file('/home/tardis/Desktop/Ansible/Trial/project/converted.yaml', 'w')   # only for python2
    stream = open('/home/tardis/Desktop/Ansible/Runner/project/converted.yaml', 'w')
    yaml.dump(data, stream)

    # r = ansible_runner.run(private_data_dir='/home/tardis/Desktop/Ansible/Trial', playbook='touch-playbook.yaml')
    # r = ansible_runner.run(private_data_dir='/home/tardis/Desktop/Ansible/Trial', playbook='converted.yaml')
    r = ansible_runner.run(private_data_dir='/home/tardis/Desktop/Ansible/Runner', playbook='converted.yaml')
    print("{}: {}".format(r.status, r.rc))
    # successful: 0
    for each_host_event in r.events:
        print(each_host_event['event'])
    print("Final status:")
    print(r.stats)
    return r.stats