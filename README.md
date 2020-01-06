# setup

## requirements

-  SimpleCV

https://simplecv.readthedocs.io/en/latest/HOWTO-Install%20on%20RaspberryPi.html

```
raspberry@pi:~$ sudo apt-get install ipython python-opencv python-scipy python-numpy python-setuptools python-pip
raspberry@pi:~$ sudo pip install https://github.com/sightmachine/SimpleCV/zipball/master --no-cache-dir 

raspberry@pi:~$ simplecv

SimpleCV:1> c = Camera()
VIDIOC_QUERYMENU: Invalid argument
VIDIOC_QUERYMENU: Invalid argument
VIDIOC_QUERYMENU: Invalid argument
VIDIOC_QUERYMENU: Invalid argument
VIDIOC_QUERYMENU: Invalid argument
VIDIOC_QUERYMENU: Invalid argument
VIDIOC_QUERYMENU: Invalid argument

SimpleCV:2> c.getImage()
SimpleCV:2: <SimpleCV.Image Object size:(640, 480), filename: (None), at memory location: (0x1335850)>

SimpleCV:3> exit()
```
