#!/usr/bin/env python3
#Basic code to draw a circle using turtlesim at a particular velocity and radius
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer = self.create_timer(0.5, self.send_velocity_command)
        self.get_logger().info("Draw circle node has been started")

    def send_velocity_command(self):
        msg = Twist()
        msg.linear.x = self.linear_velocity
        msg.angular.z = self.angular_velocity
        self.cmd_vel_pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DrawCircleNode()

    node.linear_velocity = float(input("Enter linear velocity: "))
    radius = float(input("Enter radius: "))
    node.angular_velocity = node.linear_velocity / radius

    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()