class Solution(object):
    def plusOne(self, digits):
        num = ''
        for i in range(len(digits)):
            num += str(digits[i])
        number = int(num) + 1
        num_str = str(number)
        List = []
        for i in range(len(num_str)):
            List.append(int(num_str[i]))
        return List