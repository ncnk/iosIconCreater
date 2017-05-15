import json
import os
import sys
from PIL import Image


def resize_image(file_in_path, file_out_path, width, height, image_type):
    source_image = Image.open(file_in_path, mode="r")
    new_image = source_image.resize((width, height), Image.ANTIALIAS)
    new_image.save(file_out_path, image_type)


def create_ios_icon(source_image_path, config_file_path):

    try:
        config_file = open(config_file_path)
        config = config_file.read()
    except Exception as error:
        print("failed to open config file \n")
        print(error)
        return
    finally:
        config_file.close()

    try:
        config_dict = json.loads(config)
        images = config_dict['images']
        for image in images:
            size_array = image['size'].split('x')
            width = int(size_array[0])
            height = int(size_array[1])
            output_image_path = os.path.dirname(config_file_path) + "/" + image['filename']
            if image['scale'] == '2x':
                width *= 2
                height *= 2
            elif image['scale'] == '3x':
                width *= 3
                height *= 3
            image_type = "png"
            resize_image(source_image_path, output_image_path, width, height, image_type)
        print("replace icons --- complete \n")
    except Exception as error:
        print("failed to resize icon \n")
        print(error)
        return


if __name__ == "__main__":
    create_ios_icon(sys.argv[1], sys.argv[2])
