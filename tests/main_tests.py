
import os
import sys
import json

import secretsvault

class TestStorage():
	def __init__(self):
		self.data = {}

	def readConfig(self, k):
		return self.data.get(k,None)

	def writeConfig(self, k, c):
		self.data[k] = c

	def removeData(self, k):
		self.data[k] = None


def test_encoder():
	ts = {}
	enc1 = secretsvault.CreateEncoder(ts, True)
	enc1.serialize(ts)

	print("Storage:")
	print(json.dumps(ts,indent=4))

	enc2 = secretsvault.CreateEncoder(ts, False)
	assert(enc2 != None)

	s1 = enc1.encodeStr("test-value1")
	assert(enc2.decodeStr( s1) == "test-value1")

	s2 = enc2.encodeStr("test-value2")
	assert(enc1.decodeStr(s2) == "test-value2")
	
def test_vault():
	#load public key
	serverConfig = secretsvault.CreateFileStorage("/repo/tests/TestVolume/config", False)
	serverEncoder = secretsvault.CreateEncoder(serverConfig, False)
	assert(serverEncoder != None and serverEncoder.canDecode() == True)
	

	vaultConfig = {
		"url":"http://127.0.0.1:5000",
	}
	vaultConfig.update(serverEncoder.get_public_data())
	print("Vault config:")
	print(vaultConfig)

	v = secretsvault.CreateVault(vaultConfig)

	print("Vault Info:")
	inf1 = v.info()
	print(json.dumps(inf1, indent=4))
	
	assert(inf1 != None)
	assert(inf1.get("dirty", None) != None)
	v.sanitize()
	inf2 = v.info()
	assert(inf2.get("dirty", None) == None)
	
	v["test-key"] = "test-value"
	#assert(v["key"] == "value")

	#st = secretsvault.CreateFileStorage("/repo/vaultserver/TestVolume/data", False)
	#assert(v.vaultEncoder.decodeStr(st['key']) == "value")
	

def main():
	test_encoder()
	test_vault()

main()

#assert(vault.get("test") == None)

"""
#open close
assert(vault.isOpen() == False)
assert(vault.open(False) == False) #false because the vault does not exists, it's going to be created
assert(vault.isOpen() == True)
assert(vault.isEncoded() == False)
vault.set("test-key", "test-value")
assert(vault.close() == True)
assert(vault.isOpen() == False)


#open print
assert(vault.open(False) == True) #because it exists
print(json.dumps(vault.getContent(), indent=4))
assert(vault.get("test-key") == "test-value")
assert(vault.format("{test-key}") == "test-value")
vault.close()

enc.init_with_public_key(public_key)

assert(vault.open(True) == True)
assert(enc.canDecode() == False)
vault.set("test-key2", "test-value2")
print(json.dumps(vault.getContent(), indent=4))
vault.close()

assert(vault.open(False) == False) #should not be able to decode
vault.destroy()

enc.init_with_private_key(private_key)
assert(enc.canDecode() == True)
assert(enc.canDecode() == True)
assert(vault.open(True) == True)
assert(vault.get("test-key2") == "test-value2")
vault.close()
"""