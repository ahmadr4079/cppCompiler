class Style():
    black = lambda x: '\033[30m' + str(x)
    red = lambda x: '\033[31m' + str(x)
    green = lambda x: '\033[32m' + str(x) + '\033[0m'
    yellow = lambda x: '\033[33m' + str(x)
    blue = lambda x: '\033[34m' + str(x)
    magenta = lambda x: '\033[35m' + str(x)
    cyan = lambda x: '\033[36m' + str(x)
    white = lambda x: '\033[37m' + str(x)
    underline = lambda x: '\033[4m' + str(x)
    reset = lambda x: '\033[0m' + str(x)
    bold = lambda x: '\033[1m' + str(x)
    customHeader = lambda x: '\033[0;30;46m' + str(x) + '\033[0m'
