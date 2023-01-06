from requests_html import HTMLSession, HTML
from concurrent.futures import ThreadPoolExecutor
import random, os, threading, time
from datetime import datetime
from playsound import playsound

runnable_file = __file__
scripts_path = os.path.dirname(runnable_file)
mp3File = os.path.join(scripts_path, "Bike Horn.mp3")

def get_frames(parent_url, count=20):

    urls = []
    
    session = HTMLSession()
    r = session.get(parent_url)

    matches = r.html.find("div.thumb a", first=False)

    for match in matches:
        frame_url = match.attrs['href']
        urls.append(frame_url)

    print("finished")
    return urls

def get_pagination(max_page=6, parent_url=None):

    session = HTMLSession()
    r = session.get(parent_url)

    pagination_urls = []
    page_count = 0
    for html in r.html:
        page_url = html.url
        pagination_urls.append(page_url)
        page_count += 1

        if page_count >= max_page:
            break
    
    print("Done getting paginations")
    return pagination_urls

def download_frame(source_file, options):

    command = f"youtube-dl -a {source_file} {options}"
    print(f"Command that is to be run = {command}")
    print("\nStaring download... Please wait..")
    os.system(command)

def main():

    serach_url = input("Enter the search url eg: https//google.com?query=pages\n>>>")
    parent_url = input("Enter the parent url eg: https//google.com\n>>>")

    if parent_url.endswith("/"):
        parent_url = "/".join(parent_url.split("/")[:-1])
    
    max_pages = 6
    asked_pages = input("How many pages should we visit? eg:6 or skip for default\n>>>")

    if asked_pages == "":
        pages_to_get_frames_from = get_pagination(parent_url=serach_url)
    else:
        asked_pages = int(asked_pages)
        pages_to_get_frames_from = get_pagination(max_page=asked_pages, parent_url=serach_url)
    print(f"Getting pages...Please Wait...")

    with ThreadPoolExecutor(max_workers=25) as executor:
        results = executor.map(get_frames, pages_to_get_frames_from)
    
    all_urls = []
    for x in results:
        for item in x:
            all_urls.append(item)

    new_comlete_urls_list = []
    for url in all_urls:
        complete_url = f"{parent_url}{url}"
        new_comlete_urls_list.append(complete_url)
    count = 0

    new_comlete_urls_string = "\n\n".join(new_comlete_urls_list)
    
    print("Done getting the individual frame links.")
    choise = input("Enter the path where you want to download the frames (Default in /Pictures/Frames)\n>>>")
    if choise == "":
        destination = "C:\\Users\\royalstate\\Pictures\\Frames"
    else:
        destination = choise
    
    print(f"Destination set to {destination}")

    random_choise = input("How do you want to download your frames?\n1) Choose urls randomly\n2) Select urls by yourself\n>>>")
    
    temp_dest = f"{destination}\\temp_file.txt"
    source_file = f"{destination}\\source_file.txt"
    defaults = f"-f hls-360p/mp4-low/hls-480p -o \"{destination}{os.sep}%(title)s.%(ext)s\""
    
    sleep_time = input("Fo how long do you want to sleep before the start of the download? (blank is none)\n>>>(seconds)>>>")

    sleep_time = int(sleep_time)

    if random_choise == "1":
        frames_count = input("How many frames should be selected randomly for download? (default=10)\n>>>")
        max_frames_count = int(frames_count)
        final_frames_url = random.sample(new_comlete_urls_list, max_frames_count)
        final_frames_url_string = "\n\n".join(final_frames_url)

        with open(source_file, 'w') as f2:
            f2.write(final_frames_url_string)

        options = input(f"Now lets get some youtube-dl options from you...\n Empty for default ie: {defaults})\n>>>")
        
        if options == "":
            options = defaults
        
        print(f"sleeping for {sleep_time}, download will begin at {datetime.fromtimestamp(time.time()+sleep_time).strftime('%A, %B %d, %Y %I:%M:%S')}")
        time.sleep(sleep_time)


        print("\n\nRunning the download for the firts time...")
        download_frame(source_file, options)
        print("\n\nDone.\nNow Runnig for the second time....")
        download_frame(source_file, options)
        print("\n\nDone.\nRunni g for the thisd and final time...")
        download_frame(source_file, options)
        
        playsound(mp3File)
        print("Done with all operations")

    elif random_choise == "2":
        
        

        proceed = input("\n\tNOW COPY THE URLS YOU WANT TO DOWNLOAD TO THE EMPTY TEXT FILE OPENED...\nPress Enter to continue once finised coping..")

        with open(temp_dest, 'w') as f1:
            f1.write(new_comlete_urls_string)
        with open(source_file, 'w') as f2:
            f2.write("#  PASTE THE SELCECTED URLS HERE...")

        th1 = threading.Thread(target=lambda: os.system(f"notepad {temp_dest}"))
        th1.start()
        th2 = threading.Thread(target=lambda: os.system(f"notepad {source_file}"))
        th2.start()
        th1.join()
        th2.join()

        options = input(f"Now lets get some youtube-dl options from you...\n Empty for default ie: {defaults})\n>>>")
        
        if options == "":
            options = defaults
        
        print(f"sleeping for {sleep_time}, download will begin at {datetime.fromtimestamp(time.time()+sleep_time).strftime('%A, %B %d, %Y %I:%M:%S')}")
        time.sleep(sleep_time)

        print("\n\nRunning the download for the firts time...")
        download_frame(source_file, options)
        print("\n\nDone.\nNow Runnig for the second time....")
        download_frame(source_file, options)
        print("\n\nDone.\nRunnig for the thisd and final time...")
        download_frame(source_file, options)

        playsound(mp3File)
        print("Done with all operations")


    else:
        print("Invalid choice, select frames on your own")

        frames_count = input("How many frames should be selected randomly for download? (default=10)\n>>>")
        max_frames_count = int(frames_count)
        final_frames_url = random.sample(new_comlete_urls_list, max_frames_count)
        final_frames_url_string = "\n\n".join(final_frames_url)

        with open(source_file, 'w') as f2:
            f2.write(final_frames_url_string)

        options = input(f"Now lets get some youtube-dl options from you...\n Empty for default ie: {defaults})\n>>>")
        
        if options == "":
            options = defaults
        
        print(f"sleeping for {sleep_time}, download will begin at {datetime.fromtimestamp(time.time()+sleep_time).strftime('%A, %B %d, %Y %I:%M:%S')}")
        time.sleep(sleep_time)

        print("\n\nRunning the download for the firts time...")
        download_frame(source_file, options)
        print("\n\nDone.\nNow Runnig for the second time....")
        download_frame(source_file, options)
        print("\n\nDone.\nRunni g for the thisd and final time...")
        download_frame(source_file, options)

        playsound(mp3File)
        print("Done with all operations")

    print("\n\n\tFinished.\nNow cleaning Up text files...")

    try:
        os.remove(temp_dest)
        os.remove(source_file)
    except:
        pass
    
    
    print("\n"*100)
    print("Done. Good Bye.")
    time.sleep(10)
    playsound(mp3File)
    input()


main()
