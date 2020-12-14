class Version:

    def __init__(self, major, minor, build):
        self.major = major
        self.minor = minor
        self.build = build

    def __str__(self):
        return "{}.{}.{}".format(self.major, self.minor, self.build)


version = Version(0, 0, 9)
__version__ = str(version)
