from multiprocessing import Process, Queue
import time

def worker(worker_id, task_queue):
    while True:
        task = task_queue.get()
        if task is None:
            print(f"Worker {worker_id} stopping.")
            break
        print(f"Worker {worker_id} got:", task)
        time.sleep(1)

if __name__ == "__main__":
    q = Queue()

    workers = []
    for i in range(2):
        p = Process(target=worker, args=(i, q))
        p.start()
        workers.append(p)

    for t in range(5):
        print("[Parent] Sending task", t)
        q.put(t)

    for _ in workers:
        q.put(None)

    for p in workers:
        p.join()

    print("All workers finished.")





[Parent] Sending task 0
[Parent] Sending task 1
[Parent] Sending task 2
[Parent] Sending task 3
[Parent] Sending task 4
Worker 0 got: 0
Worker 1 got: 1
Worker 0 got: 2
Worker 1 got: 3
Worker 0 got: 4
Worker 1 stopping.
Worker 0 stopping.
All workers finished.
