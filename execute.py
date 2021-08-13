import json
import SN,MN,MME
from threading import Thread
import time
f = open('config.json',)
data = json.load(f)
Nodes = data['Nodes']
MNdict = Nodes[0]
SNdict = Nodes[1]
MMEdict = Nodes[2]
ActiveConnections = []
Connections = data['Connections']
for x in Connections:
    if x['isActive'] == '1':
        ActiveConnections.append(x)
Message = data['Messages']
MessageToSend = ''
for x in Message:
    if x['isActive'] == '1':
        MessageToSend =MessageToSend +  x['message']  + ' '
MessageToSend = MessageToSend.rstrip()
for con in ActiveConnections:
    port = con['port']
    if con['name'] == 'con1': #FROM MN TO SN
        SNid = SNdict['id']
        MNid = MNdict['id']
        Thread(target=SN.main,args= ('0',SNid,port,'MN','')).start()
        Thread(target=MN.main,args=('1',MNid,port,'SN',MessageToSend)).start()
        time.sleep(0.1)
    elif con['name'] == 'con2': #FROM MN TO MME
        MMEid = MMEdict['id']
        MNid = MNdict['id']
        Thread(target=MME.main, args=('0', MMEid, port, 'MN', '')).start()
        Thread(target=MN.main, args=('1', MNid, port, 'SN', MessageToSend)).start()
        time.sleep(0.1)
    elif con['name'] == 'con3': #FROM SN TO MN
        MNid = MNdict['id']
        SNid = SNdict['id']
        Thread(target=MN.main, args=('0', MNid, port, 'SN', '')).start()
        Thread(target=SN.main, args=('1', SNid, port, 'MN', MessageToSend)).start()
        time.sleep(0.1)

    elif con['name'] == 'con4': #FROM SN TO MME
        MMEid = MMEdict['id']
        SNid = SNdict['id']
        Thread(target=MME.main, args=('0', MMEid, port, 'SN', '')).start()
        Thread(target=SN.main, args=('1', SNid, port, 'MME', MessageToSend)).start()
        time.sleep(0.1)

    elif con['name'] == 'con5': #FROM MME TO MN
        MNid = MNdict['id']
        MMEid = MMEdict['id']
        Thread(target=MN.main, args=('0', MNid, port, 'MME', '')).start()
        Thread(target=MME.main, args=('1', MMEid, port, 'MME', MessageToSend)).start()
        time.sleep(0.1)

    elif con['name'] == 'con6': #FROM MME TO SN
        SNid = SNdict['id']
        MMEid = MMEdict['id']
        Thread(target=SN.main, args=('0', SNid, port, 'MME', '')).start()
        Thread(target=MME.main, args=('1', MMEid, port, 'MME', MessageToSend)).start()
        time.sleep(0.1)




# Closing file
f.close()




