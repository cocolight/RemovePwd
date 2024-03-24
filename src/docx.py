
def a():
    try:
        m
    except Exception as e:
        raise Exception("拷贝 pptx 文件错误") from e
    

def b():
    try:
        a()
    except Exception as e:
        print('捕获到异常：{}'.format(e))

b()