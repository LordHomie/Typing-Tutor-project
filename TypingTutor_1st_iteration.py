import time
with open('C:\\Users\\ASUS\\untitled13\\venv\\sentences.txt', 'r') as myfile:

    cnt = 1
    for line in myfile:
        word_count = len(line.split())
        print("Line {}: {}".format(cnt, line.strip()))
        cnt += 1
        t0 = time.time()  # start time
        s = str(input())
        t1 = time.time()  # stop time
        accuracy = len(set(s.split()) & set(line.split()))
        accuracy = (accuracy / word_count) * 100
        timeTaken = t1 - t0
        wordPM = (word_count / timeTaken) * 10
        if  s == line.strip():
           print('Correct:)')
           print('speed: ' + '{:.1f}'.format(wordPM), 'Accuracy: ' + '{:.1f}'.format(accuracy) + '%', sep=' , ')
        else:
           print('Oops! it seems that you mistyped something')
           print('speed: ' + '{:.1f}'.format(wordPM), 'Accuracy: ' + '{:.1f}'.format(accuracy) + '%', sep=' , ')
           while str(input('Enter "m" if you want to move to the next sentence:  ')) != 'm':
                exit()

myfile.close()
