from SimpleCV import *
cam = SimpleCV.Camera()
streaming = JpegStreamer("0.0.0.0:1212")
threshold = 5.0

while True:
	previous = cam.getImage().toGray()
	time.sleep(0.25)
	original = cam.getImage()
	current = cam.getImage().toGray()
	diff = (previous - current).binarize(10).invert()
	matrix = diff.getNumpy()
	mean = matrix.mean()
	blobs = diff.findBlobs()

#	if blobs:
#		for b in blobs:
#			loc = (b.x,b.y)
#			original.drawCircle(loc,b.radius(),Color.RED,2)
	if mean >= threshold:
		if blobs:
			for b in blobs:
				loc = (b.x,b.y)
				original.drawCircle(loc,b.radius(),Color.RED,2)
		i = 0
		while os.path.exists("motion%s.png" % i):
			i += 1
		original.save("motion%s.png" %i)
		print "Motion Detected"
	original.save(streaming)
	time.sleep(0.1)
