import time
import keyboard
try:
    with open('sentences.TXT', 'r') as myfile:
        pass
        cnt = 1
        for line in myfile:
            word_count = len(line.split())
            print("Line {}: {}".format(cnt, line.strip()), sep='')
            cnt += 1
            k = 0
            z = line.strip()
            t0 = time.time()  # start time
            while True:
                if keyboard.is_pressed(z[k]):
                    print(z[k], end='')
                    k += 1
                    if k == len(z):
                        break
                    if k > len(z):
                        pass
                else:
                    pass
            t1 = time.time()  # stop time
            timeTaken = t1 - t0
            wordPM = (word_count / timeTaken)
            print('   ' + 'speed: ' + '{:.1f}'.format(wordPM))
            print('Enter "m" if you want to move to the next sentence:  ')
            while True:
                    try:
                        if keyboard.is_pressed('m'):
                                break
                        else:
                                pass
                    except:
                        break
    myfile.close()

except IOError as e:
    print("File doesn't exist!!")
