"""
These are public functions, everyone can use it
"""
import wx


def detectFont(size: list[float], panel: wx.Window, string: str, ratio=0.9):
    """
    set font in panel to make string "tall enough,"
        but character that outside the rectangle won't be shown
    :param size: size of rectangle
    :param panel: panel whose font will be adjusted
    :param string: string to put into rectangle
    :param ratio:
    :return: corner of the string
    """
    textSize = panel.GetTextExtent(string)
    corner, times = putRectangle(*textSize, size, ratio)
    f = panel.GetFont()
    f.Scale(times)
    panel.SetFont(f)
    return corner


def putPartString(size: list[float], panel: wx.Window, string: str, ratio=0.9):
    """
    :param size: size of rectangle
    :param panel:
    :param string: (part of) string to put into rectangle
    :param ratio: height of string, and shown part of string
    :return: (
        y axis of where string should putted,
        string to be shown
    )
    """
    textSize = panel.GetTextExtent(string)
    times = size[1] / textSize.y * ratio
    headY = size[1] - times * textSize.y
    s = string[:int(size[0] / textSize.x)]
    f = panel.GetFont()
    f.Scale(times)
    panel.SetFont(f)
    return headY, s


def putRectangle(rx: float, ry: float, rect: list[float], ratio=0.9):
    """
    Put biggest rectangle with size (rx, ry) into center of [rect] * [ratio]
    :param rx:
    :param ry:
    :param rect:
    :param ratio:
    :return: (corner of rectangle, times that (rx, ry) should be scaled)
    """
    times = min(rect[0] / rx, rect[1] / ry) * ratio
    size = (rx * times, ry * times)
    corner = (
        (rect[0] - size[0]) / 2,
        (rect[1] - size[1]) / 2
    )
    return corner, times


def toInts(nums: list[float]):
    """
    make every elements integer, since some drawing function accept int only
    """
    return [round(c) for c in nums]


def toTimeFormat(now):
    """
    :param now: time in millisceonds
    :return: now in m: ss.ss
    """
    T = [now // 60000, now // 10]
    s = str(T[0])
    s2 = str(T[1] / 100)
    if T[1] < 1000:
        s2 = '0' + s2
    return s + ':' + s2
