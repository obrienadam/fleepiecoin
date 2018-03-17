import hashlib


class Block(object):
    @staticmethod
    def calculate_hash(id, timestamp, prev_hash, data, nonce):
        h = hashlib.sha256()
        h.update(str(id))
        h.update(str(timestamp))
        h.update(str(prev_hash))
        h.update(str(data))
        h.update(str(nonce))
        return h.hexdigest()

    def __init__(self, id, timestamp, prev_hash, data):
        self.id = id
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.data = data
        self.nonce = 0
        self.compute_hash()

    def compute_hash(self):
        self.hash = Block.calculate_hash(self.id, self.timestamp, self.prev_hash, self.data, self.nonce)
        return self.hash

    def has_valid_hash(self):
        return self.hash == Block.calculate_hash(self.id, self.timestamp, self.prev_hash, self.data, self.nonce)
