# video will be downloaded to script's directory

from os import system
from colorama import Fore, Style
from pytube import YouTube
from time import sleep

def run():
    # change to desired ouput path
    download_path = ''
    try:
        URL = str(input("\nurl: "))
        yt = YouTube(URL)
        print("Downloading YouTube video ...")
        yt.streams.first().download()
        print(f"{Fore.GREEN}YouTube video successful downloaded.{Style.RESET_ALL}")

        title = yt.streams[0].title
        title = title.replace("'", "").split(" ")
        title = "\ ".join(title)

        title += ".mp4"

        if download_path != ''
            try:
                sleep(2)
                system(f'mv {title} {download_path}')
            except:
                print("Invalid output path")
    except:
        print(f"{Fore.RED}YouTube video could not be downloaded.{Style.RESET_ALL}")
    finally:
        exit()
    

if __name__ == "__main__":
    run()
