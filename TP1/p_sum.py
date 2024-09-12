import threading
from queue import Queue

def p_sum(l, seuil=1000):
    if len(l) <= seuil:
        return sum(l)
    else:
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        q = Queue()
        def sum_left():
            q.put(sum(left))
        def sum_right():
            q.put(sum(right))

        t1 = threading.Thread(target=sum_left)
        t2 = threading.Thread(target=sum_right)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        return q.get() + q.get()

def main():
    l = [i for i in range(1000000)]
    print(p_sum(l))

if __name__ == "__main__":
    main()