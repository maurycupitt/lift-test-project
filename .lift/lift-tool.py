import sys

def main(argv):

    if argv[0] == "version":
        version()
    elif argv[0] == "application":
        if applicable:
            print("true")
    elif argv[0] == "run":
        run()
    else:
        print("Must supply argument!")
    
def version():
    print("1")

def applicable():
    print("true")

def run():
    lift_results = []
    result_type, result_message, result_file, result_line, result_detailed_url = 'TYPE' , 'MESSAGE', 'FILE', 'LINE', 'DETAILED_URL'
    result = {
        "type": result_type,
        "message": result_message,
        "files": result_file,
        "line": result_line,
        "details_url" : result_detailed_url
    }
    print(result)

def version():
    return 1

def applicable():
    return True

if __name__ == '__main__':
    main(sys.argv[1:])
