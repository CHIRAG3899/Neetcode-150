#Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
#Please implement encode and decode
#
#Example
#Example1
#
#Input: ["lint","code","love","you"]
#Output: ["lint","code","love","you"]
#Explanation:
#One possible encode method is: "lint:;code:;love:;you"
#Example2
#
#Input: ["we", "say", ":", "yes"]
#Output: ["we", "say", ":", "yes"]
#Explanation:
#One possible encode method is: "we:;say:;:::;yes"

class Solution:

    def encode(self, str):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        if len(str) == 0:
            return ""
        else:
            return "//".join([s.replace("/", "#/#") for s in str]) + "//"


    def decode(self, str):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        if len(str) == 0:
            return []
        return [seg.replace("#/#", "/") for seg in str.split("//")][:-1]
        
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length
        return 