class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):

        # Initialize variables to hold min and max numbers in array
        max_num = self.__elements[0]
        min_num = self.__elements[0]

        # Find highest and lowest values from array and take difference
        for i in self.__elements:
            max_num = max(max_num, i)
            min_num = min(min_num, i)

        diff = max_num - min_num
        self.maximumDifference = diff


if __name__ == "__main__":
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)