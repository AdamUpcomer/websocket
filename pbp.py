import sys
import websocket

ABIOS_WS_LINK = "wss://api.abiosgaming.com/ws?type=dota&token="

if len(sys.argv) != 2:
    print("Please include the access token!")
else:
        def on_message(ws, msg):
            print("Message Arrived:" + msg)

        def on_error(ws, error):
            print(error)

        def on_close(ws):
            print("Connection Closed")

        def on_open(ws):
           ws.send("Hello!")
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp(ABIOS_WS_LINK + sys.argv[1],
                                    on_message=on_message,
                                    on_error=on_error,
                                    on_close=on_close)
        ws.run_forever()