import os


def query_images(images_path):
    res = []
    if os.path.exists(images_path):
        files = os.listdir(images_path)
        for file in files:
            extension = file.split('.').pop()
            if extension in ['png', 'jpg', 'jpeg']:
                x1 = os.path.join(images_path, file)
                x2 = os.path.join(images_path, '2.0x', file)
                x3 = os.path.join(images_path, '3.0x', file)
                res.append({'name': file, 'x1': os.path.exists(x1), 'x2': os.path.exists(x2), 'x3': os.path.exists(x3)})
    return res


def delete_image(images_path, name):
    if os.path.exists(images_path):
        x1 = os.path.join(images_path, name)
        x2 = os.path.join(images_path, '2.0x', name)
        x3 = os.path.join(images_path, '3.0x', name)
        if os.path.exists(x1):
            os.remove(x1)
        if os.path.exists(x2):
            os.remove(x2)
        if os.path.exists(x3):
            os.remove(x3)


def rename_image(images_path, old_name, new_name):
    if os.path.exists(images_path):
        x1_o = os.path.join(images_path, old_name)
        x2_o = os.path.join(images_path, '2.0x', old_name)
        x3_o = os.path.join(images_path, '3.0x', old_name)
        x1_n = os.path.join(images_path, new_name)
        x2_n = os.path.join(images_path, '2.0x', new_name)
        x3_n = os.path.join(images_path, '3.0x', new_name)
        if os.path.exists(x1_n) or os.path.exists(x2_n) or os.path.exists(x3_n):
            print('new name is exist')
        else:
            if os.path.exists(x1_o):
                os.rename(x1_o, x1_n)
            if os.path.exists(x2_o):
                os.rename(x2_o, x2_n)
            if os.path.exists(x3_o):
                os.rename(x3_o, x3_n)


def rename_by_name_content(images_path, old, new):
    images = query_images(images_path)
    for i in images:
        name = i['name']
        if old in name:
            new_name = name.replace(old, new)
            rename_image(images_path, name, new_name)

