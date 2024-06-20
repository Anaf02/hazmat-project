
import os
import xml.etree.ElementTree as ET
#import resize_images

#new_width = resize_images.new_width
#new_height = resize_images.new_height

# updates the annotation & label to the new size
def update_annotations(input_annotation_dir, output_annotation_dir, new_size=(640,640)): #new_width, new_height)):
    if not os.path.exists(output_annotation_dir):
        os.makedirs(output_annotation_dir)

    for annotation_file in os.listdir(input_annotation_dir):
        annotation_path = os.path.join(input_annotation_dir, annotation_file)
        output_annotation_path = os.path.join(output_annotation_dir, annotation_file)

        try:
            tree = ET.parse(annotation_path)
            root = tree.getroot()

            # Get original image size from the annotation file
            size = root.find('size')
            original_width = int(size.find('width').text)
            original_height = int(size.find('height').text)

            # Update image size in the annotation file
            size.find('width').text = str(new_size[0])
            size.find('height').text = str(new_size[1])

            for obj in root.iter('object'):
                xmlbox = obj.find('bndbox')
                xmin = int(xmlbox.find('xmin').text)
                ymin = int(xmlbox.find('ymin').text)
                xmax = int(xmlbox.find('xmax').text)
                ymax = int(xmlbox.find('ymax').text)

                # Calculate scale factors
                scale_x = new_size[0] / original_width
                scale_y = new_size[1] / original_height

                # Transform bounding box coordinates
                new_xmin = int(xmin * scale_x)
                new_ymin = int(ymin * scale_y)
                new_xmax = int(xmax * scale_x)
                new_ymax = int(ymax * scale_y)

                xmlbox.find('xmin').text = str(new_xmin)
                xmlbox.find('ymin').text = str(new_ymin)
                xmlbox.find('xmax').text = str(new_xmax)
                xmlbox.find('ymax').text = str(new_ymax)

            tree.write(output_annotation_path)
            #print(f"Updated annotation for {annotation_file}")

        except Exception as e:
            print(f"Error processing {annotation_file}: {e}")

input_annotation_dir = "C:/Users/User/VisualStudioCode/SS24_AI Project/hazmat-project/data/scriptconvert/annot_bef"
output_annotation_dir = "C:/Users/User/VisualStudioCode/SS24_AI Project/hazmat-project/data/scriptconvert/annot_after"

update_annotations(input_annotation_dir, output_annotation_dir)