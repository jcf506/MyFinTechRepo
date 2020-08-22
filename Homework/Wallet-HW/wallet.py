from constants import *
mnemonic = os.getenv('MNEMONIC', 'insert mnemonic here')




import subprocess
import json
import os
from constants import *
from bit import wif_to_key, PrivatekeyTestnet
from bit.network import NetworkAPI
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_acccount import Account






w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
mnem = os.getenv('MNEMONIC')
php = 'php.exe ./hd-wallet-derive/hd-wallet-derive.php'


#Derive wallet keys


def derive_wallets(mnemonic, coin, numderive):
    cmd = f'{php} -g --mnemonic={mnem} --numderive='+str(numderive)+' --coin='+str(coin)+' --cols=all --format=jsonpretty'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)
    (output, err) = p.communicate()
    return json.loads(output)

coins = ('eth':derive_wallets(mnemonic=mnem,coin=ETH,numderives=3), 'btc-test': derive_wallets(mnemonic=mnem,coin=BTCTEST,numderive=3))

privkey_BTCTEST = coins['btc-test'][0]['privkey']
privkey_ETH = coins['eth'][0]['privkey']




print(json.dumps(coins, indent=4, sort_keys=True))





def priv_key_to_account(coin, privkey):
    if coin == ETH
        return Account.privateKeyToAccount(privkey)
    if coin == BTCTEST:
        return PrivateKeyTestnet(privkey)
    
ETH_account = priv_key_to_account(BTCTEST, privkey_BTCTEST)
BTCTEST_account = priv_key_to_account(BTCTEST, privkey_BTCTEST)



#Create Transaction



def create_tx(coin, account, to, amount):
    gasEstimate = w3.eth.estimateGas(
        {"from": account.address, "to": to, "value": amount}
    )
    return {
        "from": account.address,
        "to": to,
        "value": amount,
        "gasPrice": w3.eth.gasPrice,
        "gas": gasEstimate,
        "nonce": w3.eth.getTransactionCount(account.address),
        "chainID": w3.net.chainID
        }

        return tx

    if coin == BTCTEST:
        
        return PrivateKeyTestnet.prepare_transaction(account, address, [(to, amount, BTC)])
    




create_tx(BTCTEST,BTCTEST_account, 'senderAddress',0.0001)

create_tx(ETH,ETH_account, 'senderAddress',0.0001)

#Sign and send transaction


def send_tx(account, to, amount):
    if coin == ETH:
        raw_tx = create_tx(coin, account.address, to, amount)
        signed_tx = account.sign_transaction(raw_tx)
        
        return w3.eth.sendRawTransactions(signed_tx.rawTransaction).hex()
    
    if coin == BTCTEST:
        raw_tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(raw_tx
                                             
        return NetworkAPI.broaddcast_tx_testnet(signed_tx)
                                             

#Send to designated Blockchain network 
                                             
                                        
send_tx(BTCTESTBTCTEST_account, 'recipient address', 0.0001)
                                             
                                             
# ##
                                             
#In[]:
                                             

