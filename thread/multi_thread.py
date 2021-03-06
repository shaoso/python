import requests
import threading
import time

link_list = []
with open('url.txt','r') as file:
    file_list = file.readlines()
    for eachone in file_list:
        link = eachone.split('\t')[1]
        link = link.replace('\n','')
        link_list.append(link)

start = time.time()
class myThread(threading.Thread):
    def __init__(self,name,link_range):
        threading.Thread.__init__(self)
        self.name = name
        self.link_range = link_range
    def run(self):
        print("Starting " + self.name)
        crawler(self.name,self.link_range)
        print("Exiting " + self.name)

def crawler(threadName,link_range):
    for i in range(link_range[0],link_range[1]+1):
        try:
            r = requests.get(link_list[i],timeout = 20)
            print(threadName,r.status_code,link_list[i])
        except Exception as e:
            print(threadName,"Error: ",e)

thread_list = []
link_rangs_list = [(0,60),(61,120),(121,180),(181,240),(241,300)]
#创建新线程
for i in range(1,6):
    thread = myThread("Thread-" + str(i),link_rangs_list[i-1])
    thread.start()
    thread_list.append(thread)
#等待所有线程完成
for thread in thread_list:
    thread.join()

end = time.time()
print('简单多线程爬虫的总时间为：',end - start)
print("Exiting Main Thread")