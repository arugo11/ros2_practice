import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class TrialPub(Node):
    def __init__(self):
        super().__init__("pub_node")
        self.publisher_ = self.create_publisher(String, "helloworld", 10)
        timer_period = 2.0
        self.timer = self.create_timer(timer_period, self.pub_callback)

    def pub_callback(self):
        msg = String()
        msg.data = "Hello World!!"
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    talker = TrialPub()
    try:
        rclpy.spin(talker)
    except KeyboardInterrupt:
        pass
    finally:
        talker.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()