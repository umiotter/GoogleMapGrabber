# -*- coding: utf-8 -*-
import math
import os

# 经纬度追加视野级别用方法
def geo_position(position, z):
    result = list()
    result.extend(position)
    result.append(z)
    return result

def creating_path(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


# 创建细节路径，根据z、x形成2级路径，y用来命名
def storing_path(path, z=0, x=0):
    total_path = str(path) + "\\" + str(z) + "\\" + str(x)  # + "\\" + str(y)
    creating_path(total_path)
    # print("已创建新路径")
    return total_path

# 经纬度反算切片行列号 3857坐标系
def deg2num(geo_position):
    lon_deg = geo_position[0]
    lat_deg = geo_position[1]
    z = geo_position[2]
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** z
    x_tile = int((lon_deg + 180.0) / 360.0 * n)
    y_tile = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    # x_tile = x_tile if x_tile != 0 else 1
    # y_tile = y_tile if y_tile != 0 else 1

    return [x_tile, y_tile]
