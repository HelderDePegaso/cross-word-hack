class ListAsSet(list):
    def __init__(self, Iterable=[]):
        """Initialize the list as a set to remove duplicates"""
        inSet = set()

        for item in Iterable:
            inSet.add(item)

        super(ListAsSet, self).__init__(list(inSet))

    """A list that doesn't allow duplicates."""
    def append(self, item):
        if item not in self:
            super(ListAsSet, self).append(item)


