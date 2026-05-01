from multiprocessing import Process, Pipe

def child_process(conn):
    print("[Child] Waiting for message...")
    msg = conn.recv()
    print("[Child] Received:", msg)
    reply = msg.upper() + " (from child)"
    conn.send(reply)

if __name__ == "__main__":
    parent_conn, child_conn = Pipe()
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    parent_conn.send("hello child")
    print("[Parent] Sent: hello child")
    print("[Parent] Received:", parent_conn.recv())
    p.join()



[Parent] Sent: hello child
[Child] Waiting for message...
[Child] Received: hello child
[Parent] Received: HELLO CHILD (from child)
