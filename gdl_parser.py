# -*- coding: utf-8 -*-

import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Download img from google map.")

    parser.add_argument('-s', '--savepath', default='.\GoogleEarthMapTlis',
                        help='set save path.')
    parser.add_argument('-p', '--proxy_addr', default=False, nargs="?", const='127.0.0.1:1080',
                        help="set proxy address, default: '127.0.0.1:1080'.")
    parser.add_argument('--left_top', type=float, nargs=2, default=[113.76867, 23.98104],
                        help='set start of left top.')
    parser.add_argument('--right_bottom', type=float, nargs=2, default=[115.44922, 22.40578],
                        help='set end of right bottom.')
    parser.add_argument('--z_start', type=float, nargs=1, default=18,
                        help='set start of z axis level.')
    parser.add_argument('--z_end', type=float, nargs=1, default=18,
                        help='set end of z axis level.')
    parser.add_argument('-t', '--thread_num', type=int, nargs=1, default=30,
                        help='set number of threads.')
    parser.add_argument('-l', '--log', default=False, action='store_true',
                        help='set log flag.')
    
    args = parser.parse_args()

    log_save_dir = './log/'
    args.log_save_dir = log_save_dir
   
    return args