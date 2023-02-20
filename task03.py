def same_by(charac,objects):
    values = [0,2,10,6]
    listcharacteristic =[charac(i) for i in objects]
    for i in range (len(listcharacteristic )-1):
        if listcharacteristic[i] != listcharacteristic[i + 1]: return False
    return True
values = [0,2,10,6]
if same_by(lambda x: x % 2,values):
     print('same')
else:
    print('diffrent')
