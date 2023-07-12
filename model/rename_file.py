import os
# Label Anak Laki-Laki Folder (Anak L)
def anakL():
    folder = "model/dataset/voice/Anak (L)"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Anak-L-{str(count)}.wav"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
anakL()

# Label Anak Perempuan Folder (Anak P)
def anakP():
    folder = "model/dataset/voice/Anak (P)"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Anak-P-{str(count)}.wav"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
anakP()

# Label Remaja Laki-Laki Folder (Remaja L)
def remajaL():
    folder = "model/dataset/voice/Remaja (L)"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Remaja-L-{str(count)}.wav"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
remajaL()

# Label Remaja Perempuan Folder (Remaja P)
def remajaP():
    folder = "model/dataset/voice/Remaja (P)"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Remaja-P-{str(count)}.wav"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
remajaP()

# Label Dewasa Laki-Laki Folder (Dewasa L)
def dewasaL():
    folder = "model/dataset/voice/Dewasa (L)"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Dewasa-L-{str(count)}.wav"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
dewasaL()

# Label Dewasa Perempuan Folder (Dewasa P)
def dewasaP():
    folder = "model/dataset/voice/Dewasa (P)"
    for count, filename in enumerate(os.listdir(folder)):
        dst = f"Dewasa-P-{str(count)}.wav"
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"
         
        # rename() function will
        # rename all the files
        os.rename(src, dst)
dewasaP()