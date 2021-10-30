import os
import shutil
from PIL import Image


def import_action(source, destination):
    if not os.path.exists(source) or not os.path.exists(destination):
        return 'path is not exists'
    if not os.path.exists(os.path.join(destination, '2.0x')):
        os.mkdir(os.path.join(destination, '2.0x'))
    if not os.path.exists(os.path.join(destination, '3.0x')):
        os.mkdir(os.path.join(destination, '3.0x'))
    if os.path.isdir(source):
        files = os.listdir(source)
        for file in files:
            sub_path = os.path.join(source, file)
            import_single_file(sub_path, destination)
    else:
        import_single_file(source, destination)


def import_single_file(path, destination):
    # make sure it png or jpg
    file_name = os.path.basename(path)
    extension = file_name.split('.').pop()
    if extension in ['png', 'jpg', 'jpeg']:
        base_name = file_name.split('.')[0]
        des_name = base_name
        if base_name.endswith('@3x') or base_name.endswith('@2x'):
            des_name = base_name[:-3]
        x3 = os.path.join(os.path.dirname(path), des_name + '@3x.' + extension)
        x2 = os.path.join(os.path.dirname(path), des_name + '@2x.' + extension)
        x1 = os.path.join(os.path.dirname(path), des_name + '.' + extension)
        des_name = des_name + '.' + extension
        if os.path.exists(os.path.join(destination, des_name)):
            return
        if os.path.exists(x1) and os.path.exists(x2) and os.path.exists(x3):
            shutil.copy(x1, os.path.join(destination, des_name))
            shutil.copy(x2, os.path.join(destination, '2.0x', des_name))
            shutil.copy(x3, os.path.join(destination, '3.0x', des_name))
        else:
            origin_img = Image.open(path)
            width = int(origin_img.size[0] / 3)
            height = int(origin_img.size[1] / 3)
            img3x = origin_img
            img2x = origin_img.resize((width * 2, height * 2), Image.ANTIALIAS)
            img1x = origin_img.resize((width, height), Image.ANTIALIAS)
            img1x.save(os.path.join(destination, des_name))
            img2x.save(os.path.join(destination, '2.0x', des_name))
            img3x.save(os.path.join(destination, '3.0x', des_name))

