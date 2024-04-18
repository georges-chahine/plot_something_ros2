from rclpy.time import Time
from rclpy.duration import Duration
from rosbags.rosbag2 import Reader
from rosbags.rosbag2 import Writer
from rosbags.typesys import Stores, get_typestore
from rosbags.serde import deserialize_cdr
import matplotlib.pyplot as plt
# create reader instance and open for reading

typestore=get_typestore(Stores.LATEST)
String = typestore.types['std_msgs/msg/Float32']

with Writer('/mnt/d/ros_test/test_bag7') as writer:
            topic='/chatter'
            msgtype=String.__msgtype__
            connection=writer.add_connection(topic, msgtype, typestore=typestore)
            eta=(1713439948*1000000000+9084211)
            #timestamp=Time(seconds=eta)  #.to_msg()
            #print (timestamp)
            String.data=24.13 # = String (24.13)
            message=String
            writer.write(connection, eta, typestore.serialize_cdr(message, msgtype))
