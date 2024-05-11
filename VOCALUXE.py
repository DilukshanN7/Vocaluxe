from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from mailtm import Email
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import YouTube
from selenium.webdriver.chrome.options import Options
from moviepy.editor import AudioFileClip
import os
from selenium.common.exceptions import TimeoutException
import shutil
import requests
import math
import dropbox
import sys
from tkinter import *
from PIL import ImageTk, Image 

w=Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1)

Frame(w, width=427, height=250, bg='#272727').place(x=0,y=0)
label1=Label(w, text='VOCALUXE', fg='white', bg='#272727')
label1.configure(font=("Montserrat", 24, "bold"))  
label1.place(x=110,y=90)

label2=Label(w, text='Powered By Moises AI & Dropbox. Developed by Dilukshan', fg='white', bg='#272727')
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))

for i in range(3):
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update_idletasks()
    time.sleep(0.5)

w.destroy()
w.mainloop()

print("Welcome to VOCALUXE. Powered by Moises AI & Dropbox. Developed by @dilukshann7")

time.sleep(2)

with open("TOKEN.txt", "r") as f:
    TOKEN = f.read()

def authenticate_with_dropbox(token):
    try:
        dbx = dropbox.Dropbox(
            app_key = "##########",
            app_secret = "#########",
            oauth2_refresh_token = "##################################"
        )
        account_info = dbx.users_get_current_account()
        print("Dropbox authentication successful!")

    except dropbox.exceptions.AuthError as e:
        print(f"Dropbox authentication failed: {e}")
        exit()

if __name__ == "__main__":
    authenticate_with_dropbox(TOKEN)

def delete_demofile():
    source_folder_path = os.getcwd() 
    demofile_path = os.path.join(source_folder_path, "demofile1.txt")
    if os.path.exists(demofile_path) and os.path.isfile(demofile_path):
        try:
            os.remove(demofile_path)
            print("File 'demofile1.txt' deleted successfully.")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print("File 'demofile1.txt' does not exist in the source folder.")

if __name__ == "__main__":
    delete_demofile()

def delete_moises_folder():
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    moises_folder_path = os.path.join(downloads_path, 'Moises')
    if os.path.exists(moises_folder_path) and os.path.isdir(moises_folder_path):
        try:
            shutil.rmtree(moises_folder_path)
            print("Folder 'Moises' and its contents deleted successfully.")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print("Folder 'Moises' does not exist in Downloads folder.")

if __name__ == "__main__":
    delete_moises_folder()

def delete_files():
    dbx = dropbox.Dropbox(
            app_key = "w8e4e2983odhb3a",
            app_secret = "hrk8pwssxjdzbt0",
            oauth2_refresh_token = "6oRgIj-R-GwAAAAAAAAAAYcXrmm8E-junR9J3erl-LTdqyd7QXG-uaZKTaRBDb3_"
        )
    files_to_check = [
        "downloaded_audio.mp4",
        "downloaded_audio_chunk_1.mp3",
        "downloaded_audio_chunk_2.mp3",
        "downloaded_audio_chunk_3.mp3"
    ]

    for file_name in files_to_check:
        try:
            metadata = dbx.files_get_metadata(f"/{file_name}")
            dbx.files_delete_v2(f"/{file_name}")
            print(f"File '{file_name}' deleted successfully from Dropbox.")
        except dropbox.exceptions.ApiError as e:
            if e.error.is_path():
                print(f"File '{file_name}' does not exist in Dropbox.")
            else:
                print(f"Error occurred: {e}")

if __name__ == "__main__":
    delete_files()

DROPBOX_ACCESS_TOKEN = 'w8e4e2983odhb3a'

def download_and_convert_to_audio(youtube_url, output_path):
    video = YouTube(youtube_url)
    stream = video.streams.filter(only_audio=True).first()
    if not stream:
        raise Exception("No audio stream found")
        
    file_path = stream.download(output_path=output_path, filename_prefix="temp_")

    file_extension = stream.mime_type.split('/')[-1] 
    audio_file_path = os.path.join(output_path, f"downloaded_audio.{file_extension}")

    os.rename(file_path, audio_file_path)
    
    return audio_file_path

def split_audio_into_chunks(audio_file_path, chunk_length_sec=290):
    audio_clip = AudioFileClip(audio_file_path)
    total_length_sec = audio_clip.duration
    num_chunks = math.ceil(total_length_sec / chunk_length_sec)
    
    for i in range(num_chunks):
        start_time = i * chunk_length_sec
        end_time = min((i + 1) * chunk_length_sec, total_length_sec)
        chunk = audio_clip.subclip(start_time, end_time)
        
        chunk_file_path = f"{audio_file_path.rsplit('.', 1)[0]}_chunk_{i+1}.mp3"
        chunk.write_audiofile(chunk_file_path)
    
    audio_clip.close()

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    print("Downloading the video. Please Wait")
    output_path = os.path.expanduser("~/Downloads/Moises")
    
    audio_file_path = download_and_convert_to_audio(youtube_url, output_path)
    split_audio_into_chunks(audio_file_path)
    print("Audio has been processed and saved into chunks.")

dbx = dropbox.Dropbox(
            app_key = "w8e4e2983odhb3a",
            app_secret = "hrk8pwssxjdzbt0",
            oauth2_refresh_token = "6oRgIj-R-GwAAAAAAAAAAYcXrmm8E-junR9J3erl-LTdqyd7QXG-uaZKTaRBDb3_"
        )

def upload_all_local_files():
    for file in os.listdir(os.path.expanduser("~/Downloads/Moises")):
        with open(os.path.join(os.path.expanduser("~/Downloads/Moises"), file), "rb") as f:
            data  = f.read()
            dbx.files_upload(data, f"/{file}")

print("Uploading the audio files to Dropbox")

upload_all_local_files()

print("All chunks are uploaded to Dropbox")

shared_link_metadata1 = dbx.sharing_create_shared_link("/downloaded_audio_chunk_1.mp3")

error = os.path.expanduser("~/Downloads/Moises")

if os.path.exists(os.path.join(error, "downloaded_audio_chunk_2.mp3")):
    shared_link_metadata2 = dbx.sharing_create_shared_link("/downloaded_audio_chunk_2.mp3")
else:
    print("Chunk 2 does not exist")

if os.path.exists(os.path.join(error, "downloaded_audio_chunk_3.mp3")):
    shared_link_metadata3 = dbx.sharing_create_shared_link("/downloaded_audio_chunk_3.mp3")
else:
    print("Chunk 3 does not exist")

def listener(message):
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'])
    f = open("demofile1.txt", "w")
    f.write(message['text'])
    f.close()

test = Email()
print("\nDomain: " + test.domain)

test.register()
print("\nEmail Adress: " + str(test.address))
print(str(test.address))

test.start(listener)
print("\nWaiting for new emails...")

options = Options()
options.add_argument("--window-size=1920,1080")
options.add_argument("--start-maximized")
options.add_argument("--headless=new")
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://studio.moises.ai/library/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "sign_up_button"))
)

signup = driver.find_element(By.ID, "sign_up_button")
signup.click()

email = driver.find_element(By.ID, "email_address_textbox")
email.send_keys(test.address)

pw = driver.find_element(By.ID, "password_textbox")
pw.send_keys("Whatever@1998")

signup = driver.find_element(By.ID, "signup_button")
signup.click()

def wait_for_file(file_path, timeout=60):
    start_time = time.time()

    while not os.path.exists(file_path):
        if time.time() - start_time > timeout:
            print("Timeout occurred. File not found.")
            return False
        time.sleep(1) 

    return True

def execute_after_file_appears():
    # File to wait for
    file_path = "demofile1.txt"

    # Wait for the file to appear
    if wait_for_file(file_path):
        print(f"File '{file_path}' appeared. Email Verification Process Started.")
        f2 = open("demofile1.txt")
        lini = f2.readlines()
        verifylink = lini[4]
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get(verifylink)
        driver.switch_to.window(driver.window_handles[0])

if __name__ == "__main__":
    execute_after_file_appears()

time.sleep(1)

WebDriverWait(driver, 150).until(
    EC.presence_of_element_located((By.ID, "add_new_song_button"))
)

addsongs = driver.find_element(By.ID, "add_new_song_button")
addsongs.click()

WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.ID, "upload_from_url_tab"))
)

addsongs11221 = driver.find_element(By.ID, "upload_from_url_tab")
addsongs11221.click()

addsongs3 = driver.find_element(By.ID, "url_text_box")
addsongs3.send_keys(str(shared_link_metadata1.url))

addsongs2 = driver.find_element(By.ID, "upload_next_button")
addsongs2.click()

submiturl = driver.find_element(By.ID, "upload_submit_button")
submiturl.click()

if os.path.exists(os.path.join(error, "downloaded_audio_chunk_2.mp3")):
    print("Uploading 2nd Chunk to Moises AI")

    WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.ID, "add_new_song_button"))
        )

    addsongs1123231 = driver.find_element(By.ID, "add_new_song_button")
    addsongs1123231.click()

    time.sleep(3)

    try: 
        WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "modal_button_dismiss"))
        )
    
        addsongs11123231 = driver.find_element(By.ID, "modal_button_dismiss")
        addsongs11123231.click()
    
    except TimeoutException:
        print("Element not found within the timeout period. Continuing with the rest of the script.")
    
    addsongs11221 = driver.find_element(By.ID, "upload_from_url_tab")
    addsongs11221.click()

    addsongs75 = driver.find_element(By.ID, "url_text_box")
    addsongs75.send_keys(str(shared_link_metadata2.url))

    addsongs86 = driver.find_element(By.ID, "upload_next_button")
    addsongs86.click()

    submiturl22 = driver.find_element(By.ID, "upload_submit_button")
    submiturl22.click()
else:
    print("2nd chunk does not exist. Checking the 3rd")

if os.path.exists(os.path.join(error, "downloaded_audio_chunk_3.mp3")):
    print("Uploading 3rd Chunk to Moises AI")
    WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.ID, "add_new_song_button"))
    )

    addsongs1123231 = driver.find_element(By.ID, "add_new_song_button")
    addsongs1123231.click()
    
    time.sleep(3)

    try: 
        WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.ID, "modal_button_dismiss"))
        )
    
        addsongs1112323111 = driver.find_element(By.ID, "modal_button_dismiss")
        addsongs1112323111.click()
    
    except TimeoutException:
        print("Element not found within the timeout period. Continuing with the rest of the script.")

    addsongs11123231 = driver.find_element(By.ID, "upload_from_url_tab")
    addsongs11123231.click()

    addsongs715 = driver.find_element(By.ID, "url_text_box")
    addsongs715.send_keys(str(shared_link_metadata3.url))

    addsongs816 = driver.find_element(By.ID, "upload_next_button")
    addsongs816.click()

    submiturl212 = driver.find_element(By.ID, "upload_submit_button")
    submiturl212.click()
else:
    print("All chunks are uploaded to Moises AI")

WebDriverWait(driver, 100).until(
EC.presence_of_element_located((By.ID, "song_name_button_1"))
)

submiturl21211 = driver.find_element(By.ID, "song_name_button_1")
submiturl21211.click()

WebDriverWait(driver, 100).until(
EC.presence_of_element_located((By.XPATH, "//button[@class='download-task_buttonExport__uY_ZD download-task_onlyDesktop__6IsL2 button_button__FmPkh button_stroke__ZNNbj button_radius1__aX6V7 button_light__4fcuE button_transparent__t1Qv_ button_small__tw9uK']"))
)

export = driver.find_element(By.XPATH, "//button[@class='download-task_buttonExport__uY_ZD download-task_onlyDesktop__6IsL2 button_button__FmPkh button_stroke__ZNNbj button_radius1__aX6V7 button_light__4fcuE button_transparent__t1Qv_ button_small__tw9uK']")
export.click()

downloadvocals = driver.find_element(By.LINK_TEXT, "Vocals")

href_value = downloadvocals.get_attribute("href")

filename = "1st Chunk.m4a"

path_to_downloads = os.path.join(os.path.expanduser('~'), 'Downloads', filename)

response = requests.get(href_value)

if response.status_code == 200:
    with open(path_to_downloads, 'wb') as file:
        file.write(response.content)
    print(f"File has been downloaded successfully to {path_to_downloads}")
else:
    print("Failed to download the file.")

WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.ID, "mixer_back_button"))
)

back = driver.find_element(By.ID, "mixer_back_button")
back.click()

if os.path.exists(os.path.join(error, "downloaded_audio_chunk_2.mp3")):
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "song_name_button_2"))
    )

    submiturl212 = driver.find_element(By.ID, "song_name_button_2")
    submiturl212.click()

    WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='download-task_buttonExport__uY_ZD download-task_onlyDesktop__6IsL2 button_button__FmPkh button_stroke__ZNNbj button_radius1__aX6V7 button_light__4fcuE button_transparent__t1Qv_ button_small__tw9uK']"))
    )

    export2 = driver.find_element(By.XPATH, "//button[@class='download-task_buttonExport__uY_ZD download-task_onlyDesktop__6IsL2 button_button__FmPkh button_stroke__ZNNbj button_radius1__aX6V7 button_light__4fcuE button_transparent__t1Qv_ button_small__tw9uK']")
    export2.click()

    downloadvocals2 = driver.find_element(By.LINK_TEXT, "Vocals")

    href_value2 = downloadvocals2.get_attribute("href")

    filename11 = "2nd Chunk.m4a"

    path_to_downloads111 = os.path.join(os.path.expanduser('~'), 'Downloads', filename11)

    response1 = requests.get(href_value2)

    if response1.status_code == 200:
        with open(path_to_downloads111, 'wb') as file:
            file.write(response1.content)
        print(f"File has been downloaded successfully to {path_to_downloads111}")
    else:
        print("Failed to download the file.")

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "mixer_back_button"))
    )

    back2 = driver.find_element(By.ID, "mixer_back_button")
    back2.click()
else:
    print("No 2nd File. Next")

if os.path.exists(os.path.join(error, "downloaded_audio_chunk_3.mp3")):
    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "song_name_button_3"))
    )

    submiturl2123 = driver.find_element(By.ID, "song_name_button_3")
    submiturl2123.click()
    
    WebDriverWait(driver, 100).until(
    EC.presence_of_element_located((By.XPATH, "//button[@class='download-task_buttonExport__uY_ZD download-task_onlyDesktop__6IsL2 button_button__FmPkh button_stroke__ZNNbj button_radius1__aX6V7 button_light__4fcuE button_transparent__t1Qv_ button_small__tw9uK']"))
    )

    export3 = driver.find_element(By.XPATH, "//button[@class='download-task_buttonExport__uY_ZD download-task_onlyDesktop__6IsL2 button_button__FmPkh button_stroke__ZNNbj button_radius1__aX6V7 button_light__4fcuE button_transparent__t1Qv_ button_small__tw9uK']")
    export3.click()

    downloadvocals3 = driver.find_element(By.LINK_TEXT, "Vocals")

    href_value3 = downloadvocals3.get_attribute("href")

    filename2 = "3rd Chunk.m4a"

    path_to_downloads222 = os.path.join(os.path.expanduser('~'), 'Downloads', filename2)

    response2 = requests.get(href_value3)

    if response2.status_code == 200:
        with open(path_to_downloads222, 'wb') as file:
            file.write(response2.content)
        print(f"File has been downloaded successfully to {path_to_downloads222}")
    else:
        print("Failed to download the file.")

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "mixer_back_button"))
    )

    back3 = driver.find_element(By.ID, "mixer_back_button")
    back3.click()
else:
    print("No 3rd File")

driver.quit()

print("Thanks for using VOCALUXE. Exiting")
time.sleep(2)
sys.exit()