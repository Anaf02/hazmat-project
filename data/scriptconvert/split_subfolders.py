import os
import shutil
from sklearn.model_selection import train_test_split

print("Dataset successfully split into train and val sets.")

# 2 folders -> each will have 2 subfolder
# replace 'path/to/images' and 'path/to/annotations' with the actual paths to your images and annotations folders
# test_size=0.2 parameter specifies that 20% of the data should be used for the validation set

# Define paths
images_path = "C:/Users/User/VisualStudioCode/SS24_AI Project/hazmat-project/data/scriptconvert/img_after"
annotations_path = "C:/Users/User/VisualStudioCode/SS24_AI Project/hazmat-project/data/scriptconvert/annot_finish"

# Create train/val folders
os.makedirs(os.path.join(images_path, 'train'), exist_ok=True)
os.makedirs(os.path.join(images_path, 'val'), exist_ok=True)
os.makedirs(os.path.join(annotations_path, 'train'), exist_ok=True)
os.makedirs(os.path.join(annotations_path, 'val'), exist_ok=True)

# Get list of files
image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]
annotation_files = [f for f in os.listdir(annotations_path) if os.path.isfile(os.path.join(annotations_path, f))]

# Split dataset
train_images, val_images, train_annotations, val_annotations = train_test_split(
    image_files, annotation_files, test_size=0.2, random_state=42)


# Function to move files
def move_files(files, source, destination):
    for f in files:
        shutil.move(os.path.join(source, f), os.path.join(destination, f))


# Move files to train/val folders
move_files(train_images, images_path, os.path.join(images_path, 'train'))
move_files(val_images, images_path, os.path.join(images_path, 'val'))
move_files(train_annotations, annotations_path, os.path.join(annotations_path, 'train'))
move_files(val_annotations, annotations_path, os.path.join(annotations_path, 'val'))

print("Dataset successfully split into train and val sets.")
