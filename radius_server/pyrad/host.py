# host.py
#
# Copyright 2003 Wichert Akkerman <wichert@deephackmode.org>

import packet

class Host:
        """Generic RADIUS capable host.

        @ivar     dict: RADIUS dictionary
        @type     dict: pyrad.dictionary.Dictionary
        @ivar authport: port to listen on for authentication packets
        @type authport: integer
        @ivar acctport: port to listen on for accounting packets
        @type acctport: integer
        """
        def __init__(self, authport=1812, acctport=1813, dict=None):
                """Constructor

                @param authport: port to listen on for authentication packets
                @type  authport: integer
                @param acctport: port to listen on for accounting packets
                @type  acctport: integer
                @param     dict: RADIUS dictionary
                @type      dict: pyrad.dictionary.Dictionary
                """
                self.dict=dict
                self.authport=authport
                self.acctport=acctport


        def CreateAuthPacket(self, **args):
                """Create a new RADIUS packet.

                This utility function creates a new RADIUS packet which can
                be used to communicate with the RADIUS server this client
                talks to. This is initializing the new packet with the
                dictionary and secret used for the client.

                @return: a new empty packet instance
                @rtype:  pyrad.packet.Packet
                """
                return packet.AuthPacket(dict=self.dict, **args)
        

        def CreateAcctPacket(self, **args):
                """Create a new RADIUS packet.

                This utility function creates a new RADIUS packet which can
                be used to communicate with the RADIUS server this client
                talks to. This is initializing the new packet with the
                dictionary and secret used for the client.

                @return: a new empty packet instance
                @rtype:  pyrad.packet.Packet
                """
                return packet.AcctPacket(dict=self.dict, **args)
        

        def SendPacket(self, fd, pkt):
                """Send a packet.

                @param fd: socket to send packet with
                @type  fd: socket class instance
                @param pkt: packet to send
                @type  pkt: Packet class instance
                """
                fd.sendto(pkt.Packet(), pkt.source)


        def SendReplyPacket(self, fd, pkt):
                """Send a packet.

                @param fd: socket to send packet with
                @type  fd: socket class instance
                @param pkt: packet to send
                @type  pkt: Packet class instance
                """
                fd.sendto(pkt.ReplyPacket(), pkt.source)
