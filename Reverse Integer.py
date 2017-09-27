class Solution(object):
    def reverse(self, x):
        rem=0
        ret=0
        maxy=2147483647
        miny=-2147483648
        p=False
        if(x<0):
            p=True
            x=-x
            
        while(x>0):
            rem=x%10
            ret=ret*10+rem
            x=x/10
        
        if(p):
            ret=-ret
        
        if(ret>maxy or ret<miny):
            return 0
        else:
            return ret

import sys
def readlines():
    for line in sys.stdin:
        yield line.strip('\n')

def main():
    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = int(line)
            
            ret = Solution().reverse(x)

            out = str(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()