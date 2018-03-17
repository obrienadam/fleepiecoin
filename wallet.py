import OpenSSL


class Wallet(object):
    def __init__(self):
        self.key = OpenSSL.crypto.PKey()
        self.key.generate_key(OpenSSL.crypto.TYPE_RSA, 2048)

    def dump_publickey(self):
        return OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, self.key)

    def __str__(self):
        return str(self.dump_publickey())


class Transaction(object):
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount

    def __str__(self):
        return str({'sender': str(self.sender), 'receiver': str(self.receiver), 'amount': self.amount})


if __name__ == '__main__':
    w1 = Wallet()
    w2 = Wallet()
    print w1.dump_publickey()
    t = Transaction(w1, w2, 324)

    print t
