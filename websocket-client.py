from __future__ import print_function
import websocket, sys, time

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.create_connection("ws://localhost:8080")
    print("Sending 'Hello, World'...")
    ws.send("Hello, World")
    print("Sent")
    print("Receiving...")
    result = ws.recv()
    print("Received '%s'" % result)

    while True:
        try:
            ws.send("still goin...")
            time.sleep(1)
        except KeyboardInterrupt:
            ws.close()
            sys.exit()