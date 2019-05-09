#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            attr = s[i]
            if s.count(a) == 1:
                return i
            return -1

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = []
        for l in letters:
            if s.count(l) == 1:
                index.append(s.index(l))
        return min(index) if len(index) > 0 else -1



     #   index=[s.index(l) for l in letters if s.count(l) == 1]
