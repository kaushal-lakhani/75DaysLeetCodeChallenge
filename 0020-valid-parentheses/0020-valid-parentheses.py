class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        match = { ")" : "(", "}" : "{", "]":"["}
        stack = []
        for i in s:
            if(i in match):
                if not stack:
                    return False
                if match[i] != stack[-1]:
                    return False
                    break
                stack.pop()
                continue
            stack.append(i)
        if(stack):
            return False
        return True