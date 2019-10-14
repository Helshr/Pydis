from collections import namedtuple


class SdsImp:
    def __init__(self):
        self.sds = namedtuple('Sds', 'len buf')
        self.SDS_MAX_PREALLOC = (1024 * 1024)

    # 根据已有字符串创建新的字符串
    def sdsnew(self, s):
        s = self.sds(len(s), s)
        return s

    # 创建一个空字符串
    def sdsempty(self):
        s = self.sds(0, '')
        return s

    # 返回 sds以使用的字节数
    def sdslen(self, sds):
        return sds.len

    # 拼接两个sds字符串
    def sdscat(self, sds1, sds2):
        sds = self.sds(sds1.len + sds2.len, sds1.buf + sds2.buf)
        return sds

    # 判断两个 sds是否相同
    def sdscmp(self, sds1, sds2):
        return sds1 == sds2


if __name__ == '__main__':
    log = print
    s = SdsImp.sdsempty()
    log("len: {}; free: {}, value: {}".format(s.len, s.free, s.buf))
