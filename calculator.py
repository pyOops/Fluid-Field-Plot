import numpy as np

RADIANS_TO_DEGREES = 0
DEGREES_TO_RADIANS = 1


def convert_angle(angle, mode):
    """
    角度单位换算
    :param angle: 要换算单位的角度值
    :param mode: 转换模式
    :return: 转换后的角度值
    """
    if mode == RADIANS_TO_DEGREES:
        return angle * 180 / np.pi
    elif mode == DEGREES_TO_RADIANS:
        return angle * np.pi / 180
    else:
        raise RuntimeError('模式必须为 RADIANS_TO_DEGREES 或 DEGREES_TO_RADIANS ！')


def integral(f, lower_limit, upper_limit, step_size=5e-3):
    """
    计算函数的定积分
    :param f: 单变量函数
    :param lower_limit: 积分下限
    :param upper_limit: 积分上限
    :param step_size: 步长
    :return: 积分值
    """
    x = np.linspace(lower_limit, upper_limit, int(abs(upper_limit - lower_limit) * (1 / step_size)))
    return np.trapz(f(x), x)