from pydis.utils import ensure
from pydis.datastruct.sds import SdsImp
from pydis.datastruct.adlist import AdlistImp


def sdsnew_test1():
    sds_imp = SdsImp()
    s = sds_imp.sdsnew('hello')
    ensure(s.buf == 'hello' and s.len == 5, 'sds new test1')


def sdsnew_test2():
    sds_imp = SdsImp()
    s = sds_imp.sdsempty()
    ensure(s.buf == '' and s.len == 0, 'sds new test2')


def sdslen_test1():
    sds_imp = SdsImp()
    s = sds_imp.sdsnew('hello')
    l = sds_imp.sdslen(s)
    ensure(l == 5, 'sds len test1')


def sdslen_test2():
    sds_imp = SdsImp()
    s = sds_imp.sdsempty()
    l = sds_imp.sdslen(s)
    ensure(l == 0, 'sds len test2')


def sdscat_test1():
    sds_imp = SdsImp()
    s1 = sds_imp.sdsnew('hello')
    s2 = sds_imp.sdsnew(' world')
    s = sds_imp.sdscat(s1, s2)
    ensure(s.len == 11 and s.buf == 'hello world', 'sds concat test1')


def sdscat_test2():
    sds_imp = SdsImp()
    s1 = sds_imp.sdsnew('')
    s2 = sds_imp.sdsnew('')
    s = sds_imp.sdscat(s1, s2)
    ensure(s.len == 0 and s.buf == '', 'sds concat test2')


def sdscmp_test1():
    sds_imp = SdsImp()
    s1 = sds_imp.sdsnew('hello')
    s2 = sds_imp.sdsnew('hello')
    s = sds_imp.sdscmp(s1, s2)
    ensure(s == True, 'sds cmp test1')


def sdscmp_test2():
    sds_imp = SdsImp()
    s1 = sds_imp.sdsnew('hello')
    s2 = sds_imp.sdsnew(' hello')
    s = sds_imp.sdscmp(s1, s2)
    ensure(s == False, 'sds cmp test2')


def test_asd():
    sdsnew_test1()
    sdsnew_test2()
    sdslen_test1()
    sdslen_test2()
    sdscat_test1()
    sdscat_test2()
    sdscmp_test1()
    sdscmp_test2()


def aslistpush_test1():
    adlist_Imp = AdlistImp()
    adlist_Imp.push('hello1')
    adlist_Imp.push('hello2')
    adlist_Imp.push('hello3')
    ensure(adlist_Imp.len == 3, 'sdslist push test1')


def aslistpush_test2():
    adlist_Imp = AdlistImp()
    adlist_Imp.push('hello1')
    adlist_Imp.push('hello2')
    adlist_Imp.push('hello3')
    ensure(adlist_Imp.head.next.next.value == "hello2", 'sdslist push test2')


def aslistpush_test3():
    adlist_Imp = AdlistImp()
    adlist_Imp.push('hello1')
    adlist_Imp.push('hello2')
    adlist_Imp.push('hello3')
    ensure(adlist_Imp.tail.prev.prev.value == "hello2", 'sdslist push test3')


def aslistpop_test1():
    adlist_Imp = AdlistImp()
    adlist_Imp.push('hello1')
    adlist_Imp.push('hello2')
    adlist_Imp.push('hello3')
    adlist_Imp.pop()
    ensure(adlist_Imp.len == 2, 'sdslist pop test1')


def aslistpop_test2():
    adlist_Imp = AdlistImp()
    adlist_Imp.push('hello1')
    adlist_Imp.push('hello2')
    adlist_Imp.push('hello3')
    v = adlist_Imp.pop()
    ensure(v == "hello3", 'sdslist pop test2')


def aslistpop_test3():
    adlist_Imp = AdlistImp()
    adlist_Imp.push('hello1')
    adlist_Imp.push('hello2')
    adlist_Imp.push('hello3')
    adlist_Imp.pop()
    adlist_Imp.pop()
    adlist_Imp.pop()
    ensure(adlist_Imp.len == 0, 'sdslist pop test3')


def aslistshift_test1():
    adlist_Imp = AdlistImp()
    adlist_Imp.push('hello1')
    adlist_Imp.push('hello2')
    adlist_Imp.push('hello3')
    adlist_Imp.shift()
    ensure(adlist_Imp.len == 2, 'sdslist shift test1')


def aslistshift_test2():
    adlist_Imp = AdlistImp()
    adlist_Imp.push('hello1')
    adlist_Imp.push('hello2')
    adlist_Imp.push('hello3')
    v = adlist_Imp.shift()
    ensure(v == "hello1", 'sdslist shift test2')


def aslistshift_test3():
    adlist_Imp = AdlistImp()
    adlist_Imp.push('hello1')
    adlist_Imp.push('hello2')
    adlist_Imp.push('hello3')
    adlist_Imp.shift()
    adlist_Imp.shift()
    adlist_Imp.shift()
    ensure(adlist_Imp.len == 0, 'sdslist shift test3')


def aslistunshift_test1():
    adlist_Imp = AdlistImp()
    adlist_Imp.unshift('hello1')
    adlist_Imp.unshift('hello2')
    adlist_Imp.unshift('hello3')
    ensure(adlist_Imp.len == 3, 'sdslist unshift test1')


def aslistunshift_test2():
    adlist_Imp = AdlistImp()
    adlist_Imp.unshift('hello1')
    adlist_Imp.unshift('hello2')
    adlist_Imp.unshift('hello3')
    ensure(adlist_Imp.head.next.next.next.value == "hello1", 'sdslist unshift test2')


def aslistunshift_test3():
    adlist_Imp = AdlistImp()
    adlist_Imp.unshift('hello1')
    adlist_Imp.unshift('hello2')
    adlist_Imp.unshift('hello3')
    ensure(adlist_Imp.head.next.next.value == "hello2", 'sdslist unshift test3')



def test_adlist():
    # aslistpush_test1()
    # aslistpush_test2()
    # aslistpush_test3()
    # aslistpop_test1()
    # aslistpop_test2()
    # aslistpop_test3()
    # aslistshift_test1()
    # aslistshift_test2()
    # aslistshift_test3()

    aslistunshift_test1()
    aslistunshift_test2()
    aslistunshift_test3()


def test_all():
    # test_asd()
    test_adlist()


if __name__ == '__main__':
    test_all()