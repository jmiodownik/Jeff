import socket
import string

network = 'chat.freenode.net'
port = 6667
chan = 'foodybarbaz'
nick = '_jeff_'
irc = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
irc.connect ( ( network, port ) )
print irc.recv ( 4096 )
irc.send ( 'NICK %s\r\n' % nick)
irc.send ( 'USER jeff_____ jeff___ jeff___ :Python IRC\r\n' )
irc.send ( 'JOIN #%s\r\n' % chan )

def parse_jeff(line):
	
	print 'found mention'
	irc.send(bytes("PRIVMSG #%s :Jeff??\r\n" % chan))

readbuffer = ""
while(1):
	readbuffer = readbuffer+irc.recv(1024).decode("UTF-8")
	print str(readbuffer)
	temp = str.split(str(readbuffer), "\n")
	readbuffer=temp.pop()

	for line in temp:
		line = str.rstrip(line)
		line = str.split(line)
		print line
		if 'PRIVMSG' in line:
			line = line[line.index("PRIVMSG") +2:]
			perms = [nick, nick+":", nick+","]
			if line[0][1:] in perms:
				print line[0]
				parse_jeff(line)
				quit()

			for elm in line:
#				if (nick == elm) or (nick + ":" == elm) or (":" + nick + ":" == elm):
#					parse_jeff(line)
#					quit()

				if 'jeff' in elm.lower():
					print "found jeff!!!"
					irc.send(bytes("PRIVMSG #%s :JEFF!!\r\n" % chan))


