import os
import random
import shutil

label_conversion = {'01': 'neutral',
                    '03': 'happy',
                    '04': 'sad',
                    '05': 'angry',
                    '06': 'fear',
                    '07': 'disgust',
                    '08': 'ps'}
                    
#the path for dataset in my dir

os.chdir('C:\\Users\\Hrishikesh\\Desktop\\Project\\#Project\\dataset')
tess = os.walk('C:\\Users\\Hrishikesh\\Desktop\\Project\\#Project\\dataset')


# Looping through the files to change their name

for files in tess: 
    for filename in files[2]:
        if filename.startswith('OAF'):
            # Separate base from extension
            base, extension = os.path.splitext(filename)
            for key, value in label_conversion.items():
                if base.endswith(value):
                    random_list = random.sample(range(10, 99), 7)
                    file_name = '-'.join([str(i) for i in random_list])
                    file_name_with_correct_emotion = (file_name[:6] + key + file_name[8:] + extension).strip()
                    shutil.move(filename, file_name_with_correct_emotion)

        else:
            base, extension = os.path.splitext(filename)
            for key, value in label_conversion.items():
                if base.endswith(value):
                    random_list = random.sample(range(10, 99), 7)
                    file_name = '-'.join([str(i) for i in random_list])
                    file_name_with_correct_emotion = (file_name[:6] + key + file_name[8:] + extension).strip()
                    shutil.move(filename, file_name_with_correct_emotion)


