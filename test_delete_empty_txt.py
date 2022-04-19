import glob
import os
for txt_path in glob.glob('/home/kai/Documents/DATASET/chilin/image_log_training_0414_label_0419/165033/165033/*.txt'):
    text_file = open(txt_path, 'r')
    x = len(text_file.readlines())
    if x <= 1:
        os.remove(txt_path)
        os.remove(txt_path[:-4]+ '.jpg')