#!/usr/bin/python


import zipfile
import os
import psutil
import shutil

import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


# songsFolder = "~/osu/Songs/"
# skinsFolder = "~/zede/osu/Skins/"

# Gettings the home folder.
home = os.path.expanduser("~")

# Settings up folders to import to and import from.
osu_folder = home + "/osu!/"
downloads_folder = home + "/Downloads/"

# Backing up the player data to another folder (I prefer MEGA).
backup_file = "/mnt/zede/steam/steamapps/common/McOsu/scores.db"
upload_file = "/mnt/zede/mega/game-saves/osu/scores.db"

osu_initialized = False


def process_check(processName):
    """Checking if the specified process is running."""
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    return False


def osu_import(file, folder):
    """Selects the specified archived file,
    and extracts it into your osu! folder"""
    zip_ref = zipfile.ZipFile(downloads_folder + file, 'r')
    zip_ref.extractall(folder + file[:-4])
    zip_ref.close()

    print(file[:-4], "has been imported!")
    os.remove(downloads_folder + file)

# Main process function.
while True:
    for file in os.listdir(downloads_folder):
        if file.endswith(".osz"):
            osu_import(file, osu_folder + "Songs")
        elif file.endswith(".osk"):
            osu_import(file, osu_folder + "Skins")
    
    # The program exits after closing McOsu.
    if process_check("McEngine"):
        osu_initialized = True
    elif osu_initialized:
        shutil.copyfile(backup_file, upload_file)
        print("Game exited, uploading data.")
        break
