from os import listdir
#import argparse

printFiles = True

def fileReader(path):
    try:
        filesList = sorted(listdir(path))
        if (printFiles):
            print('')
            print("There are", len(filesList), "files in the given path.")
            print("---------------")
            print("These are the files:")
            print("---------------")
            for file in filesList:
                print(file)
        
    except:
        print("---------------")
        print("Something is wrong. Make sure the data entries are correct and \nthere are all the files in the path.")
        print("---------------")



# Argument Parser

#parser = argparse.ArgumentParser(
#                                 formatter_class=argparse.RawDescriptionHelpFormatter,
#                                 description = 'List the files in certain path',
#                                 epilog = 'An usage example to call this script is as this: \n\t"python fileReader.py --path /somepath/someotherpath"'
#                                 )
##parser.add_argument('--path', help = 'define a certain path to read')
#parser.add_argument("-p", "--string", type=str, required=True)
##parser.add_argument('path string', metavar='str', type=str, nargs='+',
#                    #help='an string as path for the reader')
##parser.add_argument('path string', type=str, nargs='+', help='an string as path for the reader')
#
#
#args = parser.parse_args()
#
#fileReader(args.string)

fileReader("../../Input/")