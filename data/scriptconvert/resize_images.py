import os
from PIL import Image

new_width = 640
new_height = 640
def resize_images(input_dir, output_dir, size=(new_width,new_height), output_format='JPEG'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image_file in os.listdir(input_dir):
        image_path = os.path.join(input_dir, image_file)
        try:
            with Image.open(image_path) as img:
                img_resized = img.resize(size)
                output_path = os.path.join(output_dir, os.path.splitext(image_file)[0] + '.jpg')
                img_resized.save(output_path, format=output_format)
                print(f"Resized and saved {image_file} to {output_path}")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

input_dir = "C:/Users/User/VisualStudioCode/SS24_AI Project/hazmat-project/data/scriptconvert/img_bef"
output_dir = "C:/Users/User/VisualStudioCode/SS24_AI Project/hazmat-project/data/scriptconvert/img_after"
resize_images(input_dir, output_dir)
