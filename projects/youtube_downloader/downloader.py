from pytube import YouTube

print("Starting the program...")

path = "/Users/eglootz/pydev/projects/youtube_downloader/videos"

link = input("Please enter a link: ")
video = YouTube(link)

print("Getting video data...")

# Title of video
print("Title: ", video.title)

# Number of views of video
print("Number of views: ", video.views)

# Length of the video
print("Length: ", video.length, "seconds")

# Rating
print("Rating: ", video.rating)

# Getting the file name
file_name = input("What shall the file be called? ")

# Getting the filter
type = input("Do you want video (v), audio(a), or both (b)? ")

# Getting file extension and type filter
format = input("What format should the file have? (mp3/mp4/webm/)")


if type.lower() == "a":
    print("Getting data...")
    print(video.streams.filter(only_audio=True, mime_type="audio/mp4"))
    quality = input("Please enter the quality by its tag! ")
    print("Converting...")
    stream = video.streams.get_by_itag(quality)
    print("Downloading...")
    stream.download(output_path=path, filename=file_name + f".{format}",
                    filename_prefix="PyTubeDownloader - ")

elif type.lower() == "v":
    print("Getting data...")
    print(video.streams.filter(only_video=True, mime_type=f"video/{format}"))
    quality = input("Please enter the quality by its tag! ")
    print("Converting...")
    stream = video.streams.get_by_itag(quality)
    print("Downloading...")
    stream.download(output_path=path, filename=file_name + f".{format}",
                    filename_prefix="PyTubeDownloader - ")


elif type.lower() == "b":
    print("Getting data...")
    print(video.streams.filter(progressive=True, mime_type=f"video/{format}"))
    quality = input("Please enter the quality by its tag! ")
    print("Converting...")
    stream = video.streams.get_by_itag(quality)
    print("Downloading...")
    stream.download(output_path=path, filename=file_name + f".{format}",
                    filename_prefix="PyTubeDownloader - ")
else:
    print("You probably didnt't enter a,v, or b.")


print("Done.")
