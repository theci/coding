# ������
import time


def elapsed(original_func):   # ���� �Լ��� �μ��� �޴´�.
    def wrapper():
        start = time.time()
        result = original_func()    # ���� �Լ��� �����Ѵ�.
        end = time.time()
        print("�Լ� ����ð�: %f ��" % (end - start))  # ���� �Լ��� ����ð��� ����Ѵ�.
        return result  # ���� �Լ��� ���� ����� �����Ѵ�.
    return wrapper

@elapsed
def myfunc():
    print("�Լ��� ����˴ϴ�.")

myfunc()  # �Լ��� ����˴ϴ�.
myfunc("You need python")  # ������ ����. �μ����� wrapper�Լ��� �����߱� ����



### ��� �Է� �μ��� �޴� �Ķ���� ����
import time


def elapsed(original_func):   # ���� �ռ��� �μ��� �޴´�.
    def wrapper(*args, **kwargs):   # *args, **kwargs �Ķ���� �߰�
        start = time.time()
        result = original_func(*args, **kwargs)  # ���޹��� *args, **kwargs�� �Է��Ķ���ͷ� �����Լ� ����
        end = time.time()
        print("�Լ� ����ð�: %f ��" % (end - start))  # ����ð��� ����Ѵ�.
        return result  # �Լ��� ����� �����Ѵ�.
    return wrapper

@elapsed
def myfunc(msg):
    """ ���ڷ����� Ȯ�� �Լ� """
    print("'%s'�� ����մϴ�." % msg)

myfunc("You need python")