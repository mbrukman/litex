from liteeth.common import *
from liteeth.generic.arbiter import Arbiter
from liteeth.generic.dispatcher import Dispatcher
from liteeth.mac import LiteEthMAC
from liteeth.arp import LiteEthARP
from liteeth.ip import LiteEthIP

class LiteEthIPStack(Module, AutoCSR):
	def __init__(self, phy, mac_address, ip_address):
		self.phy = phy
		self.submodules.mac = mac = LiteEthMAC(phy, 8, interface="mac", with_hw_preamble_crc=True)
		self.submodules.arp = arp = LiteEthARP(mac, mac_address, ip_address)
		self.submodules.ip = ip = LiteEthIP(mac, ip_address, arp.table)
		self.sink, self.source = self.ip.sink, self.ip.source
