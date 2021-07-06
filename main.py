# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
    foin = open(name="AgoraPrivateTerm.txt", mode="r+")
    fout1 = open(name="AgoraPrivateTermOut1.txt", mode="w")
    fout2 = open(name="AgoraPrivateTermOut2.txt", mode="w")
    fout3 = open(name="AgoraPrivateTermOut3.txt", mode="w")
    fout4 = open(name="AgoraPrivateTermOut4.txt", mode="w")
    fout5 = open(name="AgoraPrivateTermOut5.txt", mode="w")
    print("文件名: {0}".format(foin.name))
    oldLines = foin.readlines()
    lineSize = len(oldLines)
    print "一共{0}行".format(lineSize)
    lineNum = 0
    for line in oldLines:
        line_new = line.replace('\n', '')
        line_new = line_new + r'\n' + '\n'
        # print line_new
        if lineNum < (lineSize / 5):
            fout1.write(line_new)
        elif lineNum < (lineSize * 2 / 5):
            fout2.write(line_new)
        elif lineNum < (lineSize * 3 / 5):
            fout3.write(line_new)
        elif lineNum < (lineSize * 4 / 5):
            fout4.write(line_new)
        elif lineNum < (lineSize * 5 / 5):
            fout5.write(line_new)
        lineNum = lineNum + 1
    foin.close()
    fout1.close()
    fout2.close()
    fout3.close()
    fout4.close()
    fout5.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm老克勒')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
