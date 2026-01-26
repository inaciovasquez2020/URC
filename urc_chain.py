from urc_ledger import apply_block, revert_block

class Chain:
    def __init__(self, genesis):
        self.blocks = {genesis["hash"]: genesis}
        self.tips = {genesis["hash"]}
        self.parent = {}
        self.height = {genesis["hash"]: 0}
        self.utxo = {}
        self.undo = {}

    def add_block(self, block):
        h = block["hash"]
        p = block["header"]["parent"]

        self.blocks[h] = block
        self.parent[h] = p
        self.height[h] = self.height[p] + 1

        utxo_new, undo = apply_block(block, self.utxo)
        self.utxo = utxo_new
        self.undo[h] = undo

        self.tips.add(h)
        if p in self.tips: self.tips.remove(p)

    def best_tip(self):
        return max(self.tips, key=lambda h: self.height[h])

    def rollback_to(self, h):
        cur = self.best_tip()
        while cur != h:
            self.utxo = revert_block(self.utxo, self.undo[cur])
            cur = self.parent[cur]
