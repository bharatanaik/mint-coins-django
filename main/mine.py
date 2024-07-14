import hashlib, json


class MineBlock:
    def __init__(self, json_data) -> None:
        self.data = json.loads(json_data)
        self.difficulty = self.data["difficulty"]

    def calculateHash(self, nonce) -> str:
        data = self.data
        data["nonce"] = nonce
        return hashlib.sha256(json.dumps(data).encode()).hexdigest()

    def get_block_hash(self):
        nonce = 0
        while True:
            hash = self.calculateHash(nonce)
            if hash.startswith("0"*self.difficulty):
                break
            nonce+=1
        return hash, nonce



if __name__ == "__main__":
    json_data = open("mine.json", "r").read()
    mining = MineBlock(json_data)
    mining.difficulty = 5
    print(mining.get_block_hash())

