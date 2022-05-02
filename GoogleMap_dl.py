# -*- coding: utf-8 -*-
# from urllib import request
from concurrent import futures
import os, random, math, queue, time
from tqdm import tqdm
import urllib.request
from urllib.error import HTTPError
import utils,parm

class ThreadPoolExecutor(futures.ThreadPoolExecutor):
    """
    重写线程池修改队列数
    """
    def __init__(self, max_workers=None, thread_name_prefix=''):
        super().__init__(max_workers, thread_name_prefix)
        # 队列大小为最大线程数的两倍
        self._work_queue = queue.Queue(self._max_workers * 1000)


def get_image(dl_site, tile_file, x, y, proxy_addr):
    if(os.path.exists(tile_file)):
        # print("文件已存在，跳过下载\n")
        return
    
    httpproxy_handler = urllib.request.ProxyHandler(
        {
            "http" : proxy_addr,
            "https": proxy_addr
        },)
    opener = urllib.request.build_opener(httpproxy_handler)
    req = urllib.request.Request(dl_site)
    req.add_header('User-Agent', random.choice(parm.agents))  # 换用随机的请求头

    try:
        if proxy_addr == False:
            pic = urllib.request.urlopen(req, timeout=3000)
        else:
            pic = opener.open(req, timeout=3000)
        with open(tile_file, 'wb') as f:
            f.write(pic.read())
        # print(str(x) + '_' + str(y) + ' 图片下载成功')
    except HTTPError as e:
        # print('Error code: ', e.code)
        if e.code != 200:
            # print(str(x) + '_' + str(y) + ' 图片下载失败')
            # print('Reason: ', e.reason)
            os.remove(tile_file)
            return False
    return True

# 说明
def print_info(z, left_top, right_bottom, download_path):
    # global keyIndex
    print("视野级别为：", z)
    print("左上角顶点经纬度为：", left_top)
    print("右下角顶点经纬度为：", right_bottom)
    print("经度差为：", math.fabs(left_top[0] - right_bottom[0]))
    print("纬度差为：", math.fabs(left_top[1] - right_bottom[1]))
    print("存储路径为：", download_path)
    # print("keyIndex:  " + str(keyIndex))

def delay(n):
    time.sleep(n)
    return f'result: {n}'

# 下载
def image_dl(z, left_top_geo, right_bottom_geo, download_path, thread_num,proxy_addr):
    # serverId = list(range(0,8))
    start_position = utils.deg2num(left_top_geo)
    end_position = utils.deg2num(right_bottom_geo)
    total_count = int((math.fabs(start_position[0] - end_position[0])+1) * (math.fabs(start_position[1] - end_position[1])+1))
    fn_args = [[None]*total_count for i in range(5)]
    # tasks = [None]*total_count
    # results = []
    i = 0
    for x in range(start_position[0], end_position[0]+1):
        for y in range(start_position[1], end_position[1]+1):
            fn_args[0][i] = 'https://www.google.com/maps/vt?lyrs=s@189&gl=cn&x=' + str(x) + '&y=' + str(y) + '&z=' + str(z)
            fn_args[1][i] = os.path.join(utils.storing_path(download_path, z, x),str(y) + ".png")
            fn_args[2][i] = x
            fn_args[3][i] = y
            fn_args[4][i] = proxy_addr
            i = i + 1

    with tqdm(total=total_count) as pbar:
        with futures.ThreadPoolExecutor(max_workers=thread_num) as pool:
             for i in range(total_count):
                future = pool.submit(get_image,fn_args[0][i],fn_args[1][i],fn_args[2][i],fn_args[3][i],fn_args[4][i])
                future.add_done_callback(lambda p: pbar.update())
                # tasks[i] = future
            #  for future in tasks:
            #     results.append(future.result())
    print('完成')