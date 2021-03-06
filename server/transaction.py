import json
import time
from _blake2 import blake2b


class Transaction:


    def __init__(self, data, owner, group=None):
        """
        :param data:
        :param owner: the public key of the sender
        """
        self.data = data
        self.signer = blake2b(owner.encode()).hexdigest()
        self.timestamp = time.time()
        self.group = group
        self.object_id = time.time() #Todo to be change to something suitable
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        Generates a hash of the transaction
        :return:
        """
        tx_string = json.dumps(self.__dict__, sort_keys=True)

        return blake2b(tx_string.encode()).hexdigest()
