import numpy as np
import matplotlib.pyplot as plt


def plot_flow(stream_func,
              mask=False,
              h=1e-3,
              xl=np.linspace(-5, 5, 31),
              yl=np.linspace(-5, 5, 31),
              contour=False,
              dpi=250,
              scale: float = None):
    """
    根据流函数绘制流场（速度场）
    :param stream_func: 流场的流函数，该函数务必接收x和y两个参数，其余参数不能是必须参数
    :param mask: 是否隐藏一些不必要绘制的数据点
    :param h: 导数步长
    :param xl: 绘图的x范围
    :param yl: 绘图的y范围
    :param contour: 是否绘制等值线
    :param dpi: 输出图像的DPI
    :param scale: 箭头缩放比例，值越大，箭头越短
    :return: 无返回值，但是会输出图像
    """
    x, y = np.meshgrid(xl, yl)  # make a 2D mesh of points

    if mask:  # hide points where mask(x,y)=True
        x, y = np.ma.masked_where(mask(x, y), x), np.ma.masked_where(mask(x, y), y)  # estimate u,v

    u = (stream_func(x, y + h) - stream_func(x, y - h)) / (2 * h)  # u = d\psi/dy
    v = (stream_func(x - h, y) - stream_func(x + h, y)) / (2 * h)  # v = -d\psi/dx

    plt.figure(figsize=(7, 7), dpi=dpi)
    plt.quiver(x, y, u, v, scale=scale)
    if contour:
        plt.contour(x, y, stream_func(x, y))
    plt.axis('equal')
    return plt.show()


def vortex(x, y, gamma):
    """
    涡流流函数
    :param x: 中心点x坐标
    :param y: 中心点y坐标
    :param gamma: 涡流强度，顺时针为正，逆时针为负
    :return: 涡流流函数
    """
    return gamma * np.log(np.sqrt(x ** 2 + y ** 2)) / (2 * np.pi)


def doublet(x, y, kappa):
    """
    偶极子流函数
    :param x: 中心点x坐标
    :param y: 中心点y坐标
    :param kappa: 偶极子强度
    :return: 偶极子流函数
    """
    angle = np.arctan2(y, x)
    return -kappa / 2 * np.pi * (np.sin(angle) / np.sqrt(x ** 2 + y ** 2))


def source(x, y, _lambda):
    """
    源流（汇流）流函数
    :param x: 中心点x坐标
    :param y: 中心点y坐标
    :param _lambda: 源（汇）流强度，正值为源流，负值为汇流
    :return: 源流（汇流）流函数
    """
    return _lambda * np.arctan(y / x) / 2 * np.pi


def uniform(x, y, velocity, theta=0):
    """
    均匀流流函数
    :param x: 中心点x坐标。无实际意义，但必须指定
    :param y: 中心点y坐标。无实际意义，但必须指定
    :param velocity: 均匀流速度大小（正值为x轴正方向）
    :param theta: 与x轴的夹角（弧度）
    :return: 均匀流流函数
    """
    return velocity * (-x * np.sin(theta) + y * np.cos(theta))
