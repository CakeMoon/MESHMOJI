import csv
import random
import numpy as np
import time

def facial_encode(li):
    facial = np.argmax(li)
    eyebrow = [0, 1, 2]
    mouth = [0, 1, 2, 3, 4]
    eye = [0, 1, 2, 3, 4]
    if facial == 0:
        code = [random.choice(eyebrow), 1, 1, 0]
    elif facial == 1:
        code = [random.choice(eyebrow), 1, 1, 1]
    elif facial == 2:
        code = [1, 3, 3, 4]
    elif facial == 3:
        code = [random.choice(eyebrow), random.choice(eye), random.choice(eye), 2]
    elif facial == 4:
        code = [random.choice(eyebrow), random.choice([0,1,2,3]), random.choice([0,1,2,3]), 1]
    elif facial == 5:
        code = [random.choice(eyebrow), random.choice(eye), random.choice(eye), 4]
    else:
        code = [random.choice(eyebrow), random.choice([0,1,3]), random.choice([0,1,3]), 0]

    with open ('encode.csv','w') as f:
        wtr = csv.writer(f, delimiter=',')
        wtr.writerow(code)

count = 0

while count < 100:

    facial_encode([0,1,2,3,4,5,6])
    count += 1
    time.sleep(1)