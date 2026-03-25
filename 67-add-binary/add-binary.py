class Solution:
    def addBinary(self,a,b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            sum = carry

            if i >= 0:
                sum += int(a[i])
                i -= 1

            if j >= 0:
                sum += int(b[j])
                j -= 1

            result.append(str(sum % 2))  # binary digit
            carry = sum // 2            # carry

        return ''.join(result[::-1])