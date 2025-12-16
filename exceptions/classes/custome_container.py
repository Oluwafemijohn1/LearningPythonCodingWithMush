class TagCloud:
    def __init__(self, tags=None):
        if tags is None:
            self.__tags = {}

    def add(self, tag: str):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag: str):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag: str, count: int):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags.items())


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("JavaScript")
cloud["JavaScript"] = 1  # This line is not needed, as add method handles it


# To make a methode or an attribute private, you can use a double underscore prefix
# Example of private attribute access
try:
    print(cloud.__tags)  # This will raise an AttributeError
except AttributeError as e:
    print(f"Error: {e}")

# This will work, but it's not recommended to access private attributes directly
# print(cloud._TagCloud__tags)
