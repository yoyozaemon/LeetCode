class Solution:
    def intToRoman(self, num: int) -> str:
                # lookup table for integer to Roman numeral mapping
        lookup = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        # initialize an empty string for the result
        result = ""
        # iterate through the lookup table
        for i in lookup:
            # add the Roman numeral symbol to the result
            # as many times as it can fit into the input integer
            while num >= i:
                result += lookup[i]
                num -= i
        return result

