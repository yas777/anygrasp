import argparse
import os
import numpy as np
import sys
print(sys.path)
# from manipulation import ObjectHandler
parser = argparse.ArgumentParser()
parser.add_argument('--checkpoint_path', required=True, help='Model checkpoint path')
parser.add_argument('--max_gripper_width', type=float, default=0.1, help='Maximum gripper width (<=0.1m)')
parser.add_argument('--gripper_height', type=float, default=0.03, help='Gripper height')
parser.add_argument('--port', type=int, default = 5556, help='port')
parser.add_argument('--top_down_grasp', action='store_true', help='Output top-down grasps')
parser.add_argument('--debug', action='store_true', help='Enable visualization')
parser.add_argument('--open_communication', action='store_true', help='Use image transferred from the robot')
parser.add_argument('--crop', action='store_true', help='Passing cropped image to anygrasp')
parser.add_argument('--environment', default = '/data/pick_and_drop_exps/Pranav Bedroom', help='Environment name')
parser.add_argument('--method', default = 'voxel map', help='navigation method name')
cfgs = parser.parse_args()
cfgs.max_gripper_width = max(0, min(0.1, cfgs.max_gripper_width))

def main():
    print()
    # object_handler = ObjectHandler(cfgs)
    # object_handler.manipulate()

if __name__ == "__main__":
    main()