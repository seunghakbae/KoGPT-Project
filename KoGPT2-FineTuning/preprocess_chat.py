import pandas as pd
import numpy as np
import os
import re
from datetime import datetime
from preprocess import preprocess_sent, clean_message

if __name__ == "__main__":

    folder_dir = 'C:\Programming\Graduation_Project\Data\original_data'
    files = os.listdir(folder_dir)

    for file in files:
        file_path = folder_dir + "\\" + str(file)
        with open(file_path, 'r', encoding='UTF-8') as f:
            lines = f.readlines()

            first_line = lines[0]

            speaker = first_line.replace(' 님과 카카오톡 대화', '')
            print(speaker)


