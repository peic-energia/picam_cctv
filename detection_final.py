from SimpleCV import *
#import time
import py_gmail
import shutil, glob

cam = SimpleCV.Camera()
streaming = JpegStreamer("0.0.0.0:1212")
threshold = 5.0
mailPause = time.time() #start timer
waitTime = 10  #wait time in seconds
src = "pic" #source directory for images
dst = "pic_bkp" #backup  directory for images

if not os.path.exists("pic"):
	os.makedirs("pic")

if not os.path.exists("pic_bkp"):
	os.makedirs("pic_bkp")

while True:
	currentTime = time.time()
	previous = cam.getImage().toGray()
	time.sleep(0.25)
	original = cam.getImage()
	current = cam.getImage().toGray()
	diff = (previous - current).binarize(10).invert()
	matrix = diff.getNumpy()
	mean = matrix.mean()
	blobs = diff.findBlobs()
	if currentTime >= (mailPause + waitTime):
		mailPause = time.time()
		for root, dirs, files in os.walk(src):
			dst_root = root.replace(src, dst)
			if files:
				firstfile = sorted(files)[0]
				img_mailer = os.path.join(root, firstfile)
				py_gmail.gmail(img_mailer)
			for file_ in files:
				src_file = os.path.join(root, file_)
				dst_file = os.path.join(dst_root, file_)
				shutil.move(src_file, dst_root)
	if mean >= threshold:
		if blobs:
			for b in blobs:
				try:
					loc = (b.x,b.y)
					original.drawCircle(loc,b.radius(),Color.RED,2)
				except:
					e = sys.exc_info()[0]
		timestr = time.strftime("%Y%m%d-%H%M%S")
		i = 1
		while os.path.exists("pic/motion%s-%s.png" % (timestr, i)):
			i += 1
		original.save("pic/motion%s-%s.png" % (timestr, i))
		print "Motion Detected"
#		if currentTime >= (mailPause + waitTime):
#			mailPause = time.time()
#			shutil.move("pic", "pic_bkp")
			#py_gmail.gmail("motion01.png")
	original.save(streaming)
	time.sleep(0.1)
