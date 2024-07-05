from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate and create the PyDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

def upload_clip(content, filename):
    """Uploads a clip to Google Drive."""
    try:
        file = drive.CreateFile({'title': filename})
        file.SetContentString(content)
        file.Upload()
        print(f"File '{filename}' uploaded successfully.")
    except Exception as e:
        print(f"An error occurred while uploading the file: {e}")

def download_clip(file_id, destination):
    """Downloads a clip from Google Drive."""
    try:
        file = drive.CreateFile({'id': file_id})
        file.GetContentFile(destination)
        print(f"File downloaded successfully to {destination}.")
    except Exception as e:
        print(f"An error occurred while downloading the file: {e}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Upload a clip")
        print("2. Download a clip")
        print("3. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            content = input("Enter the content to upload: ")
            filename = input("Enter the filename to save as: ")
            upload_clip(content, filename)
        elif choice == '2':
            file_id = input("Enter the Google Drive file ID to download: ")
            destination = input("Enter the destination filename: ")
            download_clip(file_id, destination)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
