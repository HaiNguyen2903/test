import os

"""
    Data folder contains all data subsets
"""
DATA_FOLDER = '../../datasets/wider_face/'
assert os.path.isdir(DATA_FOLDER)

"""
    Annotation folders
"""
TRAIN_ANNOTATION = os.path.join(DATA_FOLDER, 'WIDER_face_split/wider_face_train_bbx_gt.txt')
assert os.path.isfile(TRAIN_ANNOTATION)

VAL_ANNOTATION = os.path.join(DATA_FOLDER, 'WIDER_face_split/wider_face_val_bbx_gt.txt')
assert os.path.isfile(VAL_ANNOTATION)

TEST_ANNOTATION = os.path.join(DATA_FOLDER, 'WIDER_face_split/wider_face_test_filelist.txt')
assert os.path.isfile(TEST_ANNOTATION)

"""
    Images folder
"""
TRAIN_IMAGES = os.path.join(DATA_FOLDER, 'WIDER_train/images/')
assert os.path.isdir(TRAIN_IMAGES)

VAL_IMAGES = os.path.join(DATA_FOLDER, 'WIDER_val/images/')
assert os.path.isdir(VAL_IMAGES)

TEST_IMAGES = os.path.join(DATA_FOLDER, 'WIDER_test/images/')
assert os.path.isdir(TEST_IMAGES)

"""
   Facial Landmarks folders 
"""
RETINA_LANDMARKS = os.path.join(DATA_FOLDER, 'retinaface_gt_v1/')
assert os.path.isdir(RETINA_LANDMARKS)

TRAIN_LANMARKS = os.path.join(RETINA_LANDMARKS, 'train/label.txt')
assert os.path.isfile(TRAIN_LANMARKS)

VAL_LANMARKS = os.path.join(RETINA_LANDMARKS, 'val/label.txt')
assert os.path.isfile(VAL_LANMARKS)

TEST_LANMARKS = os.path.join(RETINA_LANDMARKS, 'test/label.txt')
assert os.path.isfile(TEST_LANMARKS)


"""
   Facial Landmarks folders 
"""


