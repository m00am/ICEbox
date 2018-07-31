"""
"""
import random

class TagSet:
    """
    """
    
    def __init__(self, tags):
        self.tags = set()
        self.not_tags = set()
        self.update(tags)

    def update(self, tags):
        """Update the tag set. Sort tags into the sets
        """
        for tag in tags:
            self.add(tag)

    def add(self, tag):
        """Add a tag. If it starts with '-' consider it a not-tag.
        """
        if tag.startswith("-"):
            not_tag = tag[1:].strip()
            if not_tag in self.tags:
                print(f"Couldn't add {not_tag} to the not-tags since it is already in the tags set.")
                return
            else:
                self.not_tags.add(not_tag)
        else:
            if tag in self.not_tags:
                print(f"Couldn't add {tag} to the tags since it is already in the not tags set.")
                return
            else:
                self.tags.add(tag)

    def remove(self, tag):
        if tag.startswith("-"):
            self.not_tags.remove(tag[1:].strip())
        else:
            self.tags.remove(tag)
    
    def __repr__(self):
        sorted_tags = ", ".join([tag for tag in sorted(self.tags)])
        sorted_not_tags = ", ".join([tag for tag in sorted(self.not_tags)])
        return f"TagSet( +[{sorted_tags}], -[{sorted_not_tags}])"

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def pick_valid(set1, set2):
        # valid_tags = (set1.tags |  set2.tags) - (set1.not_tags | set2.not_tags)
        valid_tags = (set1.tags & set2.tags) - (set1.not_tags | set2.not_tags)
        return random.choice(list(valid_tags))

if __name__ == "__main__":
    ts1 = TagSet(["one", "two", "-three"])
    ts2 = TagSet(["one", "two", "three", "four"])
    for _ in range(10):
        print(TagSet.pick_valid(ts1, ts2))
