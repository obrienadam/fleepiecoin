import time

from block import Block
from mine import mine_block
from wallet import Wallet, Transaction


class Blockchain(object):
    def __init__(self):
        self.blocks = [Block(0, time.time(), None, None)]

    def add_block(self, data):
        block = Block(self.blocks[-1].id + 1, time.time(), self.blocks[-1].hash, data)
        mine_block(block, 4)
        self.blocks.append(block)

    def check_balance(self, public_key):
        balance = 0.
        for block in self.blocks:
            if block.data.to_key == public_key:
                balance += block.data.amount
            elif block.data.from_key == public_key:
                balance -= block.data.amount

        return balance

    def is_valid(self):
        for i in xrange(1, len(self.blocks)):
            prev_block = self.blocks[i - 1]
            curr_block = self.blocks[i]

            if not curr_block.has_valid_hash() or curr_block.prev_hash != prev_block.hash:
                return False

        return True


if __name__ == '__main__':
    bc = Blockchain()

    w1 = Wallet()
    w2 = Wallet()
    w3 = Wallet()

    bc.add_block(Transaction(w1, w2, 443))
    bc.add_block(Transaction(w2, w3, 223))
    bc.add_block(Transaction(w3, w1, 12))
