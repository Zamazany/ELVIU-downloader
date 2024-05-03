import time
import zipfile
from selenium import webdriver
from py_mini_racer import py_mini_racer
ctx = py_mini_racer.MiniRacer()
import requests
from pathlib import Path
import os, shutil

response = requests.get('https://api.tukui.org/v1/addon/elvui')

file = (response.json().get('url'))
print(file)
version = (response.json().get('version'))
driver = webdriver.Chrome()
driver.get(file)
time.sleep(10)
driver.command_executor.set_timeout(10)
driver.close()

print(version)
DOWNLOADS = str(Path.home()) + r"\Downloads"

print(DOWNLOADS)
f = open("config.txt", "r")
AddonsPath = f.read()
print(AddonsPath)

if os.path.isdir(AddonsPath + r"\ElvUI_Options"):
    shutil.rmtree(AddonsPath + r"\ElvUI_Options")

if os.path.isdir(AddonsPath + r"\ElvUI"):
    shutil.rmtree(AddonsPath + r"\ElvUI")

if os.path.isdir(AddonsPath + r"\ElvUI_Libraries"):
    shutil.rmtree(AddonsPath + r"\ElvUI_Libraries")

AddonsPath = AddonsPath + "\\"
print(AddonsPath)
with zipfile.ZipFile(DOWNLOADS + r"\elvui-" + version + ".zip", 'r') as zip_ref:
    zip_ref.extractall(AddonsPath)