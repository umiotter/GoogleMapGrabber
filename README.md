# GoogleMapGrabber

Download maps with different z levels from Google map

# Usage 

```shell
usage: main.py [-h] [-s SAVEPATH] [-p [PROXY_ADDR]] [--left_top LEFT_TOP LEFT_TOP]
               [--right_bottom RIGHT_BOTTOM RIGHT_BOTTOM] [--z_start Z_START] [--z_end Z_END] [-t THREAD_NUM] [-l]

Download img from google map.

optional arguments:
  -h, --help            show this help message and exit
  -s SAVEPATH, --savepath SAVEPATH
                        set save path.
  -p [PROXY_ADDR], --proxy_addr [PROXY_ADDR]
                        set proxy address, default: '127.0.0.1:1080'.
  --left_top LEFT_TOP LEFT_TOP
                        set start of left top.
  --right_bottom RIGHT_BOTTOM RIGHT_BOTTOM
                        set end of right bottom.
  --z_start Z_START     set start of z axis level.
  --z_end Z_END         set end of z axis level.
  -t THREAD_NUM, --thread_num THREAD_NUM
                        set number of threads.
  -l, --log             set log flag.
```
