import pprint 
from log_reader import parse_requests
from analyzer import analyze
from client_info import get_info 
 
#Input -> Output: (JSON File) ->  [{IP, 1-4},..., {IP, 1-4}]
def detection():
    #Store each request in the DB and return a list of unique IPs from the json log file
    ip_list = parse_requests()
    ip_value_list = analyze(ip_list)
    print(ip_value_list)

def test_human():
    #Store each request in the DB and return a list of unique IPs from the json log file
     ip_list = parse_requests('humans')
     #ip_value_list = analyze(ip_list)
     info =[]
     tot = 0
     for ip in ip_list:
         val = get_info(ip,'humans',60)
         if val is not None: 
             pprint.pprint(val)
             info.append(val)
     for val in info:
         tot = tot + val["avarage_request_rate"]
     print("Avarage over the human set is: {}".format(str(tot/len(info))))
     print("There are {} unique ips".format(str(len(info))))
     #print(ip_value_list)
 

if __name__ == "__main__":
    test_human()
    #detection()
