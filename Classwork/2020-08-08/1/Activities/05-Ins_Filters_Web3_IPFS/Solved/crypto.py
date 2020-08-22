import requests
import json
import os

from pathlib import Path

from web3.auto import w3

PINATA_API_KEY = "56c11ec5c2b39a503857"
PINATA_SECRET_API_KEY = "e126608d341a31c7bccbc01698e0d8615bd5694fe57918726b22d247e3dd8a8c"
WEB3_PROVIDER_URI = "http://127.0.0.1:8545"
CRYPTOFAX_ADDRESS = "0x6eDc94b5a3626eFAb725ef38dc9Aa6d6f179293C"

headers = {
    "Content-Type": "application/json",
    "pinata_api_key": (PINATA_API_KEY),
    "pinata_secret_api_key": (PINATA_SECRET_API_KEY),
}


def initContract():
    with open(Path("CryptoFax.json")) as json_file:
        abi = json.load(json_file)

    return w3.eth.contract(address=(CRYPTOFAX_ADDRESS), abi=abi)


def convertDataToJSON(time, description):
    data = {
        "pinataOptions": {"cidVersion": 1},
        "pinataContent": {
            "name": "Example Accident Report",
            "description": description,
            "image": "ipfs://bafybeihsecbomd7gbu6qjnvs7jinlxeufujqzuz3ccazmhvkszsjpzzrsu",
            "time": time,
        },
    }
    return json.dumps(data)


def pinJSONtoIPFS(json):
    r = requests.post(
        "https://api.pinata.cloud/pinning/pinJSONToIPFS", data=json, headers=headers
    )
    ipfs_hash = r.json()["IpfsHash"]
    return f"ipfs://{ipfs_hash}"
