from import_images import *
from manage_images import *
import os
import json

config = 'cfg.json'

if __name__ == '__main__':
    source = ''
    destination = ''
    while True:
        if os.path.exists(config):
            with open(config, 'r') as f:
                cfg = json.load(f)
                source = cfg['source']
                destination = cfg['destination']
        s = input('current setup:\nsource: %s\ndestination: %s\n>>' % (source, destination))
        if s == 'q' or s == 'quit':
            break
        if s.startswith('set source'):
            cmds = s.split(' ')
            if len(cmds) == 3:
                source = cmds[2]
                cfg = {"source": source, "destination": destination}
                with open(config, 'w') as f:
                    json.dump(cfg, f)
        if s.startswith('set destination'):
            cmds = s.split(' ')
            if len(cmds) == 3:
                destination = cmds[2]
                cfg = {"source": source, "destination": destination}
                with open(config, 'w') as f:
                    json.dump(cfg, f, indent=2)
        if s.startswith('show'):
            res = query_images(destination)
            for i in res:
                print(i)
        if s.startswith('import'):
            import_action(source, destination)
        if s.startswith('delete'):
            cmds = s.split(' ')
            if len(cmds) == 2:
                delete_image(destination, cmds[1])
        if s.startswith('rename'):
            cmds = s.split(' ')
            if len(cmds) == 3:
                rename_image(destination, cmds[1], cmds[2])
        if s.startswith('rename_batch'):
            cmds = s.split(' ')
            if len(cmds) == 3:
                rename_by_name_content(destination, cmds[1], cmds[2])
        if s.startswith('format'):
            rename_by_name_content(destination, '／', '-')
