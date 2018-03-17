from block import Block


def mine_block(block, difficulty=1):
    while block.hash[:difficulty] != 'e' * difficulty:
        block.nonce += 1
        block.compute_hash()

    print 'Block mined: {}'.format(block.hash)


if __name__ == '__main__':
    block = Block(2, 432432, '32431434123', {'fdaf': 43})

    mine_block(block, 6)

    print block.hash
