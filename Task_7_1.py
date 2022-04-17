import os

preform = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in preform.items():
    if os.path.exists(root):
        print('Уже создан')
    else:
        for folder in folders:
            os.makedirs(os.path.join(root, folder))
