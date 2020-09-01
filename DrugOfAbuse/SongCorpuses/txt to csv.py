import pandas as pd
import io

df = pd.read_csv("lyrics.csv")

file1 = open("lyrics_2012.txt","a")
x = df.shape[0]
n=0
for i in range(df.shape[0]):
    if type(df['lyrics'][i]) == type('lyric') and df['year'][i] == 2012:
        y = df['lyrics'][i].splitlines()
        lyrics = ' '
        for lyric in y:
            lyrics = lyrics + lyric + ' '
        n+=1
        file1.write(str(lyrics.encode('utf8')))
        file1.write('\n')
    print(n, i/x)
