import math

class Solution(object):
    
    def search_limit_and_count(self, star_str, center_index):
        left_index = center_index
        right_index = center_index
        pali_count = -1 # set to -1 so 2 - 1 = 1 for base case of single char palidrome.
        
        while left_index > -1 and right_index < len(star_str) and star_str[left_index] == star_str[right_index]:
            pali_count += 2
            left_index -= 1
            right_index += 1
        return (pali_count, right_index - 1) # - 1 due to tail decrement.
            

    def search_and_count(self, star_str, center_index, rightmost):
        left_index = center_index
        right_index = center_index
        pali_count = -1 # set to -1 so 2 - 1 = 1 for base case of single char palidrome.
        
        while left_index > -1 and right_index <= rightmost and star_str[left_index] == star_str[right_index]:
            pali_count += 2
            left_index -= 1
            right_index += 1
        return pali_count
    
    def insert_placeholders(self, s):
        ret_str = " " # space used for delimiting split O(n) instead of variable complexity
        for c in s:
            ret_str += c + " "
        return ret_str
    
    def get_next_center(self, s, center, rightmost):
        max_index = center
        max_val = -1
        for i in range(center + 1, rightmost + 1):
            temp_val = self.search_and_count(s, i, rightmost)
            if temp_val > max_val and (math.floor(temp_val/2) + i == rightmost):
                max_val = temp_val
                max_index = i
        return max_index


    def print_pali(self, star_str, max_index, trgt_dist):
        pali_str = ""
        for i in range(max_index - trgt_dist, max_index + trgt_dist + 1):
            if star_str[i] != " ":
                pali_str += star_str[i]
        print(pali_str)

    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # Using Manacher's Algorithm, we can achieve this in O(n) rather than O(n^2)
        pali_table = []
            
        # Create new string wiht * inserted in between characters to cover for even and odd palidromes.
        star_str = self.insert_placeholders(s)
        
        # Intialize table for palidrome length for each character in O(n)
        for i in range(0, len(star_str)):
            pali_table.append(0)

        # Center of current selected palidrome
        pali_center = 0
        
        # Index of the furthest right we have explored and validated (not including non-palidrome exploration)
        furthest_explored = 0
        
        while pali_center < len(star_str) and furthest_explored < len(star_str) - 1:
            pali_length, temp_furthest = self.search_limit_and_count(star_str, pali_center)

            if furthest_explored < temp_furthest:
                furthest_explored = temp_furthest
            pali_table[pali_center] = pali_length
            temp_index = self.get_next_center(star_str, pali_center, furthest_explored)
            if pali_center == temp_index:
                pali_center += 1
            else:
                pali_center = temp_index

        max_count_of_star = max(pali_table)
        index_of_max = pali_table.index(max_count_of_star)
        self.print_pali(star_str, index_of_max, math.floor(max_count_of_star/2))


def main():
    test_str1 = "abba"
    test_str2 = "abbbaaa"
    test_str3 = "cbbd"
    test_str4 = "babad"

    test_str5 = "aabcdefg"
    test_str6 = "abcdefgg"
    test_str7 = "abcd"
    test_str8 = "b"

    sol = Solution()
    sol.longest_palindrome(test_str1)
    sol.longest_palindrome(test_str2)
    sol.longest_palindrome(test_str3)
    sol.longest_palindrome(test_str4)
    sol.longest_palindrome(test_str5)
    sol.longest_palindrome(test_str6)
    sol.longest_palindrome(test_str7)
    sol.longest_palindrome(test_str8)
if __name__ == "__main__":
    main()