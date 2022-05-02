# coding=utf-8
import time
import GoogleMap_dl
import utils
import gdl_parser
from log_helper import *

def main(args):
    utils.creating_path(args.savepath)
    log_save_id = create_log_id(args.log_save_dir)
    logging_config(folder=args.log_save_dir, name='log{:d}'.format(log_save_id), no_console=False)
    logging.info(args)

    for z_level in range(args.z_start, args.z_end + 1):
        left_top_geo = utils.geo_position(args.left_top, z_level)
        right_bottom_geo = utils.geo_position(args.right_bottom, z_level)
        GoogleMap_dl.print_info(z_level, args.left_top, args.right_bottom, args.savepath)
        print('计算下载图片数量并且下载，请稍后...')
        time.sleep(2)
        GoogleMap_dl.image_dl(z_level, left_top_geo, right_bottom_geo, args.savepath, args.thread_num, args.proxy_addr)


# 运行
if __name__ == '__main__':

    # download_path = r".\qkm\地图切片\GoogleEarthMapTlis"
    # # 左上角角点
    # left_top = [113.76867, 23.98104]
    # # 右下角角点
    # right_bottom = [115.44922, 22.40578]
    # # 开始视野级别
    # z_start = 1
    # # 最终视野级别
    # z_end = 20
    # # run(download_path,left_top,right_bottom,z_start,z_end,'google')
    # # default_run()
    args = gdl_parser.parse_args()
    main(args)
