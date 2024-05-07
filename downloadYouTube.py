import pytube

link = input('Input URL: ')
yt = pytube.YouTube(link)

print(link)