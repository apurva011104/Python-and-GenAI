inp = input("Enter log string: ").replace("\"","")

logs_list = inp.split("\\n")

formatted_logs_list = []

for logs in logs_list:
    idx = 0
    while(idx<len(logs) and logs[idx].isupper()):
        idx+=1
    l = logs[0].upper()+""+logs[1:idx].lower()
    idx += 4
    l = l + ": " + logs[idx:idx+4]
    idx += 4
    i = idx
    while(idx<len(logs) and logs[idx].isdigit()):
        idx += 1
    l = l + " " + logs[i:idx] + " -" + logs[idx+1:]
    formatted_logs_list.append(l)
    
for logs in formatted_logs_list:
    print(logs)
    