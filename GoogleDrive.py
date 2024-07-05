from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate and create the PyDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def upload_clip(content, filename):
    file = drive.CreateFile({'title': filename})
    file.SetContentString(content)
    file.Upload()

def download_clip(file_id):
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile('downloaded_clip.txt')
