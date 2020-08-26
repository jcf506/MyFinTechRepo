

import subprocess
import json
import os
from constants import *
from bit import wif_to_key, PrivateKeyTestnet
from bit.network import NetworkAPI
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account


recipient_address = "1EQtKc2FQrhN7HsdYr6CLoQ1cZrSCXWxW7"
sender_address = "0x3A3866Fb8AE7819A4693b85CF6EA974e428beE9F"

#leverage keys in coins object



w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
mnem = os.getenv('MNEMONIC')
php = 'php.exe ./hd-wallet-derive/hd-wallet-derive.php'


#Derive wallet keys


def derive_wallets(mnemonic, coin, numderive):
    cmd = f'{php} -g --mnemonic={mnemonic} --numderive='+str(numderive)+' --coin='+str(coin)+' --cols=all --format=jsonpretty'
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=False)
    (output, err) = p.communicate()
    return json.loads(output)

coins = {ETH: derive_wallets(mnemonic=mnem,coin=ETH,numderive=3), 
         BTCTEST: derive_wallets(mnemonic=mnem,coin=BTCTEST,numderive=3)}

#Extracting keys from coins that represent the output

privkey_BTCTEST = coins['btc-test'][0]['privkey']
privkey_ETH = coins['eth'][0]['privkey']


#Print out information to see what we have

print(json.dumps(coins, indent=4, sort_keys=True))


#Link Transaction to Signing Libraries


def priv_key_to_account(coin, privkey):
    if coin == ETH:
        return Account.privateKeyToAccount(privkey)
    if coin == BTCTEST:
        return PrivateKeyTestnet(privkey)
    
#Calling the function above

ETH_account = priv_key_to_account(ETH, privkey_ETH)
BTCTEST_account = priv_key_to_account(BTCTEST, privkey_BTCTEST)

print(BTCTEST_account)

#Create Library based Function



def create_tx(coin, account, to, amount):
    if coin == ETH:
        
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

    if coin == BTCTEST:
        
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
    

#Create Transaction

create_tx(BTCTEST,BTCTEST_account, sender_address, 0.0001)

create_tx(ETH,ETH_account, sender_address, 0.0001)


#Check Coin and Sign transaction

def send_tx(coin, account, to, amount):
    if coin == ETH:
        raw_tx = create_tx(coin, account.address, to, amount)
        signed_tx = account.sign_transaction(raw_tx)
        
        return w3.eth.sendRawTransactions(signed_tx.rawTransaction).hex()
    
    if coin == BTCTEST:
        raw_tx = create_tx(coin, account, to, amount)
        signed_tx = account.sign_transaction(raw_tx)
                                             
        return NetworkAPI.broaddcast_tx_testnet(signed_tx)
                                             

#Send to designated Blockchain network 
                                             
                                        
send_tx(ETH, ETH_account, recipient_address, 0.0001)
                                             
                                             
# ##
                                             
#In[]:
                                             

