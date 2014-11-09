#codini$Python

import sublime, sublime_plugin
import json
import socket

UDP_IP = "0.0.0.0"
UDP_PORT = 8888
MESSAGE = "Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

class Codini(sublime_plugin.EventListener):
	def on_modified_async(self, view):
		point = view.sel()[0].begin()
		region = view.word(point)
		word = view.substr(region)
  
		firstLineRegion = sublime.Region(0,0)
		firstLine = view.substr(view.full_line(firstLineRegion))

		jsonData = {}
		jsonData['syntax'] = view.scope_name(point)
		jsonData['word'] = word
		jsonData['firstLine'] = firstLine
		sock.sendto(str.encode(json.dumps(jsonData)), (UDP_IP, UDP_PORT))