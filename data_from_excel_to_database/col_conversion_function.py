from past.builtins import xrange


def col_name_To_num(col_name):
    if type(col_name) is not str:
        return col_name

    col = 0
    power = 1
    for i in xrange(len(col_name)-1, -1, -1):
        ch = col_name[i]
        col += (ord(ch) - ord('A') + 1) *power
        power *= 26
    return col-1

def col_num_To_name(col_num):
    if type(col_num) != int:
        return col_num
    if col_num > 25:
        ch1 = chr(col_num%26+65)
        ch2 = chr(int(col_num/int(26))+64)
        return ch2+ch1
    else:
        return chr(col_num%26+65)

if __name__ == '__main__':
    #out = col_num_To_name(0)
    out = col_name_To_num('A')
    print(out)

# xrange()用法与range()完全相同，不同的是range生成的是一个数组，而xrange()返回生成器
# ord(): 获取参数字符串对应的ASCII数值
# chr(): 返回值是当前整数对应的ascii字符