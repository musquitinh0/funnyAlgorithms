import socket, random, time
from threading import Thread

HOST = "irc.twitch.tv"
PORT = 6667
NICK = "ALTERAR"
PASS = "ALTERAR FORMATO: oauth:..."
STREAMER = "ALTERAR FORMATO: #NOMEDOSTREAMER"
readbuffer = ""

s = socket.socket()
s.connect((HOST, PORT))
s.send(("PASS " + PASS + "\r\n").encode())
s.send(("NICK " + NICK + "\r\n").encode())
s.send(("JOIN " + STREAMER + "\r\n").encode())

def Send_message(msg):
    s.send(("PRIVMSG "+STREAMER+" :"+msg+"\r\n").encode())
    
while True:
    readbuffer = readbuffer + s.recv(1024).decode()
    temp = readbuffer.split("\n")
    readbuffer = temp.pop()
    for line in temp:
        if (line[0] == "PING"):
            s.send(("PONG %s\r\n" % line[1]).encode())
            continue
        linha = line.split(" :")
        try:
            message = linha[1]
        except:
            message = ""
        print (linha)
        print (message)
        message = message.lower()
        if message == "Bom dia":
            Send_message("Opa meu bom, vem sempre aqui?")
