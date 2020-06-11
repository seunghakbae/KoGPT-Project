import pandas as pd
import numpy as np
import os
import re
from datetime import datetime
from tqdm import tqdm
# from preprocess import preprocess_sent, clean_message

def clean_message(message):
    """
    remove english and unnecessary letters

    :param message:
    :return: cleaned_message
    """
    # leave only hangul
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')

    cleaned_message = hangul.sub('', message).strip()

    # delete hangul 자음, 모음 삭제
    cleaned_message = re.sub('([ㄱ-ㅎㅏ-ㅣ])+', "", cleaned_message)

    return cleaned_message

if __name__ == "__main__":

    folder_dir = 'C:\Programming\Graduation_Project\Data\original_data'
    files = os.listdir(folder_dir)

    msg_log = []

    for file in tqdm(files):
        file_path = folder_dir + "\\" + str(file)
        with open(file_path, 'r', encoding='UTF-8') as f:
            
            lines = f.readlines()

            first_line = lines[0]
            friend = first_line.replace(' 님과 카카오톡 대화', '')

            msgs = ""

        # for each line, find speaker
        # if speaker does not change, same person is speaking so keep adding msg
        # if speaker has changed, change to speaker's msg
        for index, line in enumerate(lines):
            if '회원님' in line:
                msgs += clean_message(line.split(':')[-1]).strip()
            else:
                if msgs != "":
                    msg_log.append(msgs)
                msgs = ""

    print(len(msg_log))

    with open('my_chat_log.txt', 'w', -1, 'utf-8') as f:
        for msg in msg_log:
            f.write(msg + "\n")