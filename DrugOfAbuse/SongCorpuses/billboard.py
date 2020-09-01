import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import lyricsgenius
import time

name = 'test' + '.txt'
f = open(name,'ab')
f.write("hi".encode("utf-8") + " ".encode("utf-8"))
print("Started")
n_to_write = 20
#n_to_write is the number of songs between writing to file

df_test = pd.read_excel("billboard_weekly.xlsx")

print("Loaded billboard charts")

"""
year_count = {}
for i in range(320495):
    year = str(df_test.iloc[i]["WeekID"])[0:4]
    if len(year) == 4:
        try:
            year_count[year] = year_count[year] + 1
        except:
            year_count[year] = 1

x = np.zeros(100)
for i in range(100):
    x[i] = i + 1920

y = np.zeros(100)
for key, value in year_count.items():
    try:
        ind = int(key) - 1920
        y[ind] = value
    except:
        print("Error on key:", key)
print(x)
print(y)
plt.title("Is this enough songs?")
plt.xlabel("Year")
plt.ylabel("Number of Songs")
plt.plot(x,y)
plt.show()
"""
genius = lyricsgenius.Genius("wSdSk17B9i8nwJpoDFJUGowo9KDWDNwDb5ycoZcQE8qTiWQj0r-52nBWUL3x2_kG")
genius.remove_section_headers = True
lyrics_dict = {}
start_time = time.time()
for i in range(1205000, 125000): #320495
    current_time = time.time()
    print("Percent Lyrics Found:", (i-175000)/(5000))
    print("Number of songs done", i - 175000)
    try:
        song_name = str(df_test.iloc[i]["Song"])
        artist = str(df_test.iloc[i]["Performer"])
        first_artist = ""
        year = str(df_test.iloc[i]["WeekID"])[0:4]
        for char in artist:
            if char != ',':
                first_artist = first_artist + char
            else:
                break
        try:
            song = genius.search_song(song_name, first_artist)
            if len(song.lyrics) > 250:
                try:
                    lyrics_dict[year] = lyrics_dict[year] + " " + song.lyrics
                except:
                    lyrics_dict[year] = song.lyrics
        except:
            print("")
            print("failed on i =", i)
            print("Failed on Song_name:", song_name)
            print("And artist:", first_artist)
        if ((i % n_to_write) == 0):
            for key, value in lyrics_dict.items():
                name = 'new_lyrics_' + str(key) + '.txt'
                try:
                    f = open(name,'ab')
                    f.write(value.encode("utf-8") + " ".encode("utf-8"))
                    f.close()
                except:
                    print("Failed writing at:", i)
            lyrics_dict = {}
    except:
        print("Weird error")


i = 0
l = len(lyrics_dict)
for key, value in lyrics_dict.items():
    print("Percent Lyrics Written:", i/l)
    name = 'new_lyrics_' + str(key) + '.txt'
    try:
        f = open(name,'a')
        f.write(value)
        f.close()
    except:
        print("Failed writing to file", value);
    i += 1
