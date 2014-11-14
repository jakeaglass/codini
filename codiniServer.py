import sublime, sublime_plugin
import json
import socket
import subprocess

# Method to get local LAN IP > http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib/1947766#1947766
import os
import socket
if os.name != "nt":
    import fcntl
    import struct
    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
                s.fileno(),
                0x8915,  # SIOCGIFADDR
                struct.pack('256s', ifname[:15])
            )[20:24])
def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = ["eth0","eth1","eth2","wlan0","wlan1","wifi0","ath0","ath1","ppp0"]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break;
            except IOError:
                pass
    return ip

# Socket configuration
UDP_IP = "0.0.0.0"
UDP_PORT = 8888
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Start Node.js Server
package_path = ["/usr/local/bin/node",sublime.packages_path()+"/codini/broadcastServer/wsBroadcastServer.js"]
process = subprocess.Popen(package_path,shell=False)

# Tell User Where to Connect
def plugin_loaded():
		sublime.ok_cancel_dialog('Codini is active. Connect at '+get_lan_ip(), 'Got it')

# Terminate Node.js Server when sublime quits
def plugin_unloaded():
		print("Shutting Down Node Server")
		process.terminate()

# Main Plugin - Here be Dragons
class Codini(sublime_plugin.EventListener):
	def on_modified_async(self, view):

		#Get the word they are currenty typing
		point = view.sel()[0].begin()
		region = view.word(point)
		word = view.substr(region)

		#Format data to json
		jsonData = {}
		jsonData['syntax'] = view.scope_name(point)
		jsonData['word'] = word

		#Send it off to Node.js
		sock.sendto(str.encode(json.dumps(jsonData)), (UDP_IP, UDP_PORT))