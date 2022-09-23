from rosbags.rosbag2 import Reader
from rosbags.serde import deserialize_cdr
import matplotlib.pyplot as plt 
# create reader instance and open for reading
with Reader('/home/georges/Downloads/Data IT3 19sept/VF_04_dep_SE-1663603086') as reader:
    # topic and msgtype information is available on .connections list
    for connection in reader.connections:
        print(connection.topic, connection.msgtype)

    # iterate over messages
    x=[]
    y=[]
    z=[]
    for connection, timestamp, rawdata in reader.messages():
        if connection.topic == '/tf':
            msg = deserialize_cdr(rawdata, connection.msgtype)
            #print(msg.transforms[0].transform.translation.x)
            x.append(msg.transforms[0].transform.translation.x)
            y.append(msg.transforms[0].transform.translation.y)
            z.append(msg.transforms[0].transform.translation.z)
    plt.plot(x,y)
    plt.show()        
