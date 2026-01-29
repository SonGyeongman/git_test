import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os

class FileImagePublisher(Node):
    def __init__(self):
        super().__init__('file_image_publisher')
        self.publisher_ = self.create_publisher(Image, 'static_image', 10)
        self.timer = self.create_timer(1.0, self.timer_callback) 
        self.cv_bridge = CvBridge()

        self.image_path = "test.jpg" 
        self.cv_image = cv2.imread(self.image_path)

    def timer_callback(self):
        msg = self.cv_bridge.cv2_to_imgmsg(self.cv_image, encoding="bgr8")
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = FileImagePublisher()
    rclpy.spin_once(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()