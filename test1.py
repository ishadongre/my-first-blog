from Savoir import Savoir
rpcuser = 'multichain'
rpcpasswd = 'pass1234'
rpchost = '192.168.43.191'
rpcport = '4776'
chainname = 'blockchain1'

api = Savoir(rpcuser, rpcpasswd, rpchost, rpcport, chainname)
api.getinfo()

reg_exchange_ip(exchange_ip)
request_ecoin_issue(qty)
accept_exchange(index)
api.getmultibalances()