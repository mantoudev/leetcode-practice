#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s

        leftStr = s[0 : length//2]
        rightStr = s[length//2 : length]
        return self.reverseString(rightStr) + self.reverseString(leftStr)