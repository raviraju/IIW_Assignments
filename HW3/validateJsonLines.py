import argparse
import json
#import pprint

def main():
    parser = argparse.ArgumentParser(description="validate Json Lines file")
    parser.add_argument("path", help="path to file to validate")
    args = parser.parse_args()
    filePath = args.path
    fileHandle = open(filePath)
    try:
        for objLine in fileHandle:
            obj = json.loads(objLine)
            #pprint.pprint(obj, indent=4)
    except ValueError:  # includes simplejson.decoder.JSONDecodeError
        print('Decoding JSON has failed. INVALID Json Lines file')
        return
    print('Json Lines file is VALID')
if __name__ == "__main__" : main()