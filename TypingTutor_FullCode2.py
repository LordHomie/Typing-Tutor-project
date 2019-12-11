import time
import platform
import os

if platform.system() == "Windows":
    import msvcrt


    def getch():
        return msvcrt.getch()
else:
    import tty, termios, sys


    def getch():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        return ch

if os.path.isfile('statistics.txt'):
    os.remove('statistics.txt')
try:
    with open('sentences.TXT', 'r') as myfile:
        pass
        cnt = 1

        for line in myfile:
            st = open('statistics.txt', 'a')
            it = 1

            st1 = open('statistics.txt', 'r')
            for lines in st1:
                print("                       Line {}: {}".format(it, lines.strip()), sep='')
                it += 1

            word_count = len(line.split())

            print("\nLine {}: {}".format(cnt, line.strip()), sep='')
            cnt += 1
            k = 0
            error = 0
            z = line.strip()
            t0 = time.time()  # time starts here

            while True:
                if platform.system() == "Windows":
                    c = getch().decode()
                    # print(c, type(c), z[k], type(z[k]), c == z[k])
                    pass
                else:
                    c = getch()
                    # print(c, type(c), z[k], type(z[k]), c == z[k])
                    pass

                if c != z[k]:
                    error += 1
                    print('                      | errors counter: ', error, end='\r')  # counting errors in real-time

                if c == z[k]:
                    t1 = time.time()  # time stops here after each press
                    timeTaken = t1 - t0
                    wordPM = (word_count / timeTaken)
                    speed = 'speed: ' + '{:.1f}'.format(wordPM)  # speed gets updated after each press
                    print(c, "  True,", speed, sep=" ", end='\r')  # printing the correct letter and speed in real-time

                    k += 1
                    if k == len(z):

                        t2 = time.time()  # time stops after finishing typing the entire line
                        timeTaken1 = t2 - t0
                        wordPM1 = (word_count / timeTaken1)
                        print('\n')
                        speed1 = 'speed: ' + '{:.1f}'.format(wordPM1)
                        print(speed1)  # the speed in general after typing every single line
                        Totalerrors = 'Totalerrors: ' + '{}'.format(error)
                        print(Totalerrors, '\n')

                        st.write("{},  {} ".format(speed1, Totalerrors) + '\n')

                        print('press "s" to show your statistcs and to move to the next line OR "e" to exit:  ' + '\n')

                        while True:
                            if platform.system() == "Windows":
                                character = getch()
                                if (character == b"s"):
                                    break

                                if (character == b'e'):
                                    exit()

                                else:
                                    pass

                            else:
                                character = getch()
                                if (character == "s"):
                                    break

                                if (character == 'e'):
                                    exit()

                                else:
                                    pass
                        break

except IOError as e:
    print("File doesn't exist!!")
