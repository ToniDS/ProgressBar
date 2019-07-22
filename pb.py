import sys


class ProgressBar:
    def __init__(self, maxim):
        self.steps = maxim // 10
        self.maxim = maxim

    def render(self, i):
        filling_size = i // self.steps + 1
        filling = '#' * filling_size + ' ' * (10-filling_size)
        sys.stdout.flush()
        sys.stdout.write("["+ filling + "]  " + str(i) + "/"+ str(self.maxim) + "\n")



