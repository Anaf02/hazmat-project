import os
import xml.etree.ElementTree as ET

# Define label map (make sure the order corresponds to the YOLO class IDs)
LABEL_MAP = {
    'poison': 1,
    'oxygen': 2,
    'flammable': 3,
    'flammable-solid': 4,
    'corrosive': 5,
    'dangerous': 6,
    'non-flammable-gas': 7,
    'organic-peroxide': 8,
    'explosive': 9,
    'radioactive': 10,
    'inhalation-hazard': 11,
    'spontaneously-combustible': 12,
    'infectious-substance': 13
}


def voc_to_yolo(input_annotation_dir, output_annotation_dir):
    if not os.path.exists(output_annotation_dir):
        os.makedirs(output_annotation_dir)

    for annotation_file in os.listdir(input_annotation_dir):
        # Process only XML files
        if not annotation_file.endswith('.xml'):
            continue

        annotation_path = os.path.join(input_annotation_dir, annotation_file)
        try: # T: parsing error
            tree = ET.parse(annotation_path)
        except ET.ParseError as e:
            print(f"Error parsing {annotation_file}: {e}")
            continue

        root = tree.getroot()

        # Get image size from annotation file
        size = root.find('size')
        image_width = int(size.find('width').text)
        image_height = int(size.find('height').text)

        yolo_annotations = []

        for obj in root.iter('object'):
            label = obj.find('name').text
            if label not in LABEL_MAP:
                continue
            class_id = LABEL_MAP[label]

            xmlbox = obj.find('bndbox')
            xmin = int(xmlbox.find('xmin').text)
            ymin = int(xmlbox.find('ymin').text)
            xmax = int(xmlbox.find('xmax').text)
            ymax = int(xmlbox.find('ymax').text)

            # Calculate YOLO format (x_center, y_center, width, height)
            x_center = (xmin + xmax) / 2.0 / image_width
            y_center = (ymin + ymax) / 2.0 / image_height
            width = (xmax - xmin) / image_width
            height = (ymax - ymin) / image_height

            yolo_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}")

        # Write YOLO annotations to file
        output_file = os.path.join(output_annotation_dir, os.path.splitext(annotation_file)[0] + ".txt")
        with open(output_file, 'w') as f:
            f.write("\n".join(yolo_annotations))

        #print(f"Converted {annotation_file} to YOLO format")

# Specify directories
input_annotation_dir = "C:/Users/User/VisualStudioCode/SS24_AI Project/hazmat-project/data/scriptconvert/annot_after"
output_annotation_dir = "C:/Users/User/VisualStudioCode/SS24_AI Project/hazmat-project/data/scriptconvert/annot_finish"

# Convert VOC to YOLO
voc_to_yolo(input_annotation_dir, output_annotation_dir)
