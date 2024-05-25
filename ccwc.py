import sys
import argparse

parser = argparse.ArgumentParser(description="wc parser", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-c", action="store_true", help="return number of bytes in a file")
parser.add_argument("-l", action="store_true", help="return number of lines in a file")
parser.add_argument("-w", action="store_true", help="return number of words in a file")
parser.add_argument("-m", action="store_true", help="return number of characters in a file")
parser.add_argument("file", nargs="?", help="text file location")
args = parser.parse_args()
config = vars(args)

def extractData(fileContent):
    byteCount = lineCount = wordCount = charCount = 0
    for line in fileContent:
        byteCount += len(line)
        lineCount += 1
        wordCount += len(line.split())
        charCount += len(line.decode())
    
    return byteCount, lineCount, wordCount, charCount

def myWordCount():
    countBytes = args.c
    countLines = args.l
    countWords = args.w
    countChars = args.m
    fileName = args.file

    if not (countBytes or countLines or countWords or countChars):
        countBytes = countLines = countWords = True

    if not fileName:
        data = extractData(sys.stdin.buffer)
    else:
        with open(fileName, "rb") as f:
            data = extractData(f)

    byteCount, lineCount, wordCount, charCount = data
    
    if countLines:
        print(lineCount, end=" ")

    if countWords:
        print(wordCount, end=" ")

    if countBytes:
        print(byteCount, end=" ")

    if countChars:
        print(charCount, end=" ")

    if fileName:
        print(fileName)

if __name__ == "__main__":
    myWordCount()