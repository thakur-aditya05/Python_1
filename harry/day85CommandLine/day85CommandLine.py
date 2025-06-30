# 2 lectures re watch krna padega 


# commond utility   for example: curl --manual

# google--->index of movies  

# curl <link> --output harry.jpg====>to save and download the file 

# commond line utility ka matlab command line de ke kuch computer me kaam kr skte ho 


    # basic structure of command line importing 
# import argparse # to create command utility 

# parser=argparse.ArgumentParser()

# # add command line arguments

# parser.add_argument("arg1",help="description of argument 1")
# parser.add_argument("arg2",help="description of argument 2")

# # parse the arguments 

# args=parser.parse_args()

# #use the arguments in your code 

# print(args.arg1)
# print(args.arg2)





# step 1
import argparse
import requests
# step 5
# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url,local_filename):
    # note the stream=true parameter below
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(local_filename,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
    # if u have chunk encoded response uncomment if
    # and set chunk_size parameter to none.
                f.write(chunk)
    return local_filename

# step2
parser=argparse.ArgumentParser()
# step 3
# # add command line arguments

parser.add_argument("url",help="Url of the file to download")
parser.add_argument("output",help="by which name u want to save your file")
# step4
# parse the argument 
args=parser.parse_args()
print(args.url)
print(args.output)
download_file(args.url,args.output)

# how to use 

  




















# /when file name is not given 


# step 1
import argparse
import requests
# step 5
# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url,local_filename):
    if local_filename is None:
        local_filename=url.split('/')[-1]  
        # note the stream=true parameter below
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(local_filename,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
    # if u have chunk encoded response uncomment if
    # and set chunk_size parameter to none.
                f.write(chunk)
    return local_filename

# step2
parser=argparse.ArgumentParser()

# step 3
# # add command line arguments

parser.add_argument("url",help="Url of the file to download")
parser.add_argument("-o","--output",help="by which name u want to save your file",default=None) # deafult jaise nono hai to waha type =int to int bhi daal skte hai 

# step4
# parse the argument 
args=parser.parse_args()
#use the argument in the  your code 
print(args.url)
print(args.output,type(args.output))
download_file(args.url,args.output)















# /when file name is not given 


# step 1
import argparse
import requests
# step 5
# https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
def download_file(url,local_filename):
    if local_filename is None:
        local_filename=url.split('/')[-1]  
    # note the stream=true parameter below
    with requests.get(url,stream=True) as r:
        r.raise_for_status()
        with open(local_filename,'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
    # if u have chunk encoded response uncomment if
    # and set chunk_size parameter to none.
                f.write(chunk)
    return local_filename

# step2
parser=argparse.ArgumentParser()

# step 3
# # add command line arguments

parser.add_argument("url",help="Url of the file to download")
parser.add_argument("-o","--output",help="by which name u want to save your file",default=None)

# step4
# parse the argument 
args=parser.parse_args()
print(args.url)
print(args.output,type(args.output))
download_file(args.url,args.output)