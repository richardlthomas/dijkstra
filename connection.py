class Connection:
    def __init__(self, node, weight):
        assert weight >= 0
        self.to = node
        self.weight = weight