# coding=utf-8

import matplotlib.pyplot as plt
import datetime
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#有中文出现的情况，需要u'内容'
def stringToDate(string):
    #example '2013-07-22 09:44:15+00:00'
    dt = datetime.datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
    # print(type(dt))
    # print(dt)
    return dt

if __name__ == '__main__':
    # 输入文件名，保存图片
    file_name = input("请输入文件名")

    # 创建绘图图表对象，可以不显式创建，跟cv2中的cv2.namedWindow()用法差不多
    plt.title(u'资源一天之内的数据量变化曲线')
    plt.xlabel('time')
    plt.ylabel('count')

    lines = {}
    count = 1
    with open("data.txt",mode='r',encoding='utf-8') as file:
        for line in file:
            # 定义数据行集合
            value = {}
            # 分别解析资源名,x和y轴数据，以列表的形式存储值
            data_name = line.split(";")[0]
            data_x = line.split(";")[1].split(",")
            data_y = line.split(";")[2].split(",")
            # 将数据存储至一个字典中
            value['name'] = data_name
            value['x'] = data_x
            value['y'] = data_y
            # 构建行数据key
            key = 'line_' + str(count)
            lines[key] = value
            count += 1
    print("读取到" + str(count-1) + "行数据")
    # 解析读取结果
    if type(lines) == type({}):
        for line in lines:
            # 初始化资源名、行和列数据
            line_x = []
            line_y = []
            # 解析资源名
            if 'name' in lines[line]:
                line_name = lines[line]['name']
                print(line_name)
            else:
                print("data_line hasn't resource_name")
            # 解析x轴数据
            if 'x' in lines[line]:
                # 获取x轴数据
                data_x_tmp = lines[line]['x']
                if len(data_x_tmp) > 0 :
                    for item in data_x_tmp:
                        line_x.append(stringToDate(item))
                else:
                    print("x 轴数据个数为0！")
            else:
                print("data_line hasn't line_x")
            if 'y' in lines[line]:
                # 解析y轴数据
                line_y_tmp = lines[line]['y']
                if len(line_y_tmp) > 0 :
                    for item in line_y_tmp:
                        line_y.append(int(item))
                else:
                    print("y 轴数据个数为0！")
            else:
                print("data_line hasn't line_y")
            plt.plot(line_x,line_y,linewidth=1.0,label=line_name)
    else:
        print("lines isn't dict")

    # p1 = [stringToDate('2018-12-05 20:00:30'),stringToDate('2018-12-05 20:05:30'),stringToDate('2018-12-05 20:10:30')
    #     ,stringToDate('2018-12-05 20:15:30')]
    # p2 = [1,70,10,90]
    plt.legend(loc='best')
    plt.draw()  # 显示绘图

    plt.pause(15)  # 显示5秒

    plt.savefig(file_name+".png")  # 保存图象

    plt.close()

