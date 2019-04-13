import subprocess
import datetime

def get_file_name(chain):
	now = datetime.datetime.now()
	return chain + "/" + str(now.year) + "_" + str(now.month) + "_" + str(now.day) + "_" + str(now.hour) + "_" + str(now.minute) + "_" + str(now.second) + ".json"

path = "/data0/dsl/ln_measurement/"

#get mainnet data
f = open(path + get_file_name("mainnet"), "w")
cmd = 'docker exec lnd-mainnet ./lncli --no-macaroons --network=mainnet describegraph'.split()
completed = subprocess.run(cmd, stdout=f)

#get testnet data
f = open(path + get_file_name("testnet"), "w")
cmd = 'docker exec lnd_testnet ./lncli --no-macaroons --network=testnet --rpcserver=localhost:10010 describegraph'.split()
completed = subprocess.run(cmd, stdout=f)