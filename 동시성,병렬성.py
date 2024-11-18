# 병렬성 - 2개 cpu 하나씩
# 동시성 - 1개 cpu 여러 작업

# I/O 위주의 작업이 많다면 이때에는 동시성을 사용하는 편이 더 유리할 수 있습니다.
import multiprocessing as mp

class Worker:
    def __init__(self, name):
        print("__init__", mp.current_process().name)
        self.name = name
        self.run()

    def run(self):
        print("run", self.name)
        print("run", mp.current_process().name)


if __name__ == "__main__":
    p = mp.Process(target=Worker, name="SubProcess", args=("bob",))
    p.start()       # __init__ is called
    p.join()