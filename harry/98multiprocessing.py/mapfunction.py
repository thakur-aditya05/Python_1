

import multiprocessing
import requests
import concurrent.futures
def downloadFile(url,name):
    response=requests.get(url)
    open(f"{name}.jpg","wb").write(response.content)
    open(f"file{name}.jpg","wb").write(response.content)
    open(f"files/file{name}.jpg","wb").write(response.content)
    

url="https://picsum.photos/200/300"
# for _ in range(5)
# _ ==> throw off varibale 

for i in range(5):
    downloadFile(url,i)
# ye thi aaam jindagi downloading ki ab chalte hai projindagi downloading ki 






def downloadFile(url,name):
    print(f"start downloading {name}")
    response=requests.get(url)
    open(f"{name}.jpg","wb").write(response.content)
    open(f"file{name}.jpg","wb").write(response.content)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print(f"finished downloading {name}")
    

url="https://picsum.photos/200/300"


with concurrent.futures.ProcessPoolExecutor() as executor:
    l1=[url for i in range(60)]
    l2=[i for i in range(60)]
    results=executor.map(downloadFile,l1,l2)
    for r in results:
        print(r)


# explore and learn 


















