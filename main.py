from pb import ProgressBar

maxim = 1000
pb = ProgressBar(maxim)
for i in range(0, maxim):
	pb.render(i)
