import datetime
import sys
import optparse
import os


# function (delete file)
def delete_file(date):
    file_name = str(date) + ".txt"
    if os.path.exists(file_name):
        os.remove(file_name)
        print("File removed successfully")
    else:
        print("File not exist (create the file first)")


# function (read content in the files )
def read_file(date):
    try:
        with open(str(date) + ".txt", 'r') as f:
            content = f.read()
            print(content)
    except IOError:
        print("File not exist (create the file first)")


# function (create files , append content )
def diary(date, time):
    with open(str(date) + ".txt", "a") as page:
        _ = input('''You file create : press 'ENTER' to insert content ''')
        print("Write Here....")
        content = input()
        page.write("\n\t" + str(date) + "\t" + str(time) + "\n\n")
        page.write(content)
        page.write("\n\n")
        page.close()

    print("File saved successfully")


# cmd options
parser = optparse.OptionParser()
parser.add_option("-d", "--date", dest="date", default=datetime.date.today(),
                  help="Enter the date (default current date)")
parser.add_option("-t", "--time", dest="time", default=datetime.datetime.now().time(),
                  help="Enter the time (default current time)")
parser.add_option("-r", "--read", dest="read_date", help="Enter the specific date (format : yyyy-mm-dd )")
parser.add_option("--rm", "--remove", dest="delete_file", help="Delete the file mentioned (format : yyyy-mm-dd)")
parser.add_option("--quite ", "-q", dest="quite", help="quite (options = 0)")

opt, arg = parser.parse_args()

if opt.quite:
    sys.exit(0)
elif opt.delete_file:
    delete_file(opt.delete_file)
elif opt.read_date:
    read_file(opt.read_date)
else:
    diary(opt.date, opt.time)
