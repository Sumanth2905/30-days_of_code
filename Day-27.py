class TestDataEmptyArray(object): 
    @staticmethod
    def get_array():
        return list()
class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        return [2,3,1]
    @staticmethod
    def get_expected_result():
        return 2
class TestDataExactlyTwoDifferentMinimums(object):
    @staticmethod
    def get_array():
        return [1,3,1]
    @staticmethod
    def get_expected_result():
        return 0