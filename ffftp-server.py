from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.authorizers import DummyAuthorizer

import os
import json
import socket
import time

class MyHandler(FTPHandler):
    
    def on_connect(self):
        #print "%s:%s connected" % (self.remote_ip, self.remote_port)
        print(f"\t**** {self.remote_ip}:{self.remote_port} is now connected ****")

    def on_disconnect(self):
        # do something when client disconnects
        print("user disconected")
        pass


    def on_login(self, username):
        # do something when user login
        print("logged in")
        pass


    def on_logout(self, username):
        # do something when user logs out
        print("user logs out")
        pass


    def on_file_sent(self, file):
        # do something when a file has been sent
        print("do something when a file has been sent")
        pass
    
    def on_file_received(self, file):
        # do something when a file has been received
        print("do something when a file has been received")

        pass
    
    def on_incomplete_file_sent(self, file):
        # do something when a file is partially sent
        print("do something when a file is partially sent")
        pass



def serve_files(dir="."):

    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Setting up an ftp server at {ip_address}")

    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', homedir=dir, perm='elradfmwMT')
    authorizer.add_anonymous(homedir=dir)

    handler = MyHandler
    handler.authorizer = authorizer

    server = FTPServer(('', 2121), handler)
    server.serve_forever(handle_exit=True)

def main():
    
    ## Ask for directory to serve
    print("\n"*100)
    print("\tFFT SERVER - CUSTOM")
    print("*"*300)
    directory_to_serve = input("Enter the Directory You want to serve (Default is curent dir .)\n>>>")

    print("Starting Server....")
    serve_files()
    
    print("\n"*100)
    print(f"\tSESSION CLOSED [{time.time()}]")
    print("*"*300)

if __name__ == "__main__":
    main()