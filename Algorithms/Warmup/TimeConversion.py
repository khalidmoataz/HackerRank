import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    PMorAM = s[-2:]
    two_digits = s[0:2]
    rest_time = s[2:-2]
    
    if PMorAM == 'PM' and two_digits != '12':
        first = int(two_digits) + 12
        new_time = str(first) + rest_time
        return str(new_time)
    elif PMorAM == 'AM' and two_digits == '12':
        first = int(two_digits) - 12
        new_time = str(first) + '0' + rest_time
        return str(new_time)
    else:
        return str(s[:-2:])




if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
