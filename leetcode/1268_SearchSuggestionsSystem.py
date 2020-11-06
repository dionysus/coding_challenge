'''
1268. Search Suggestions System
Difficulty: Medium
URL: https://leetcode.com/problems/search-suggestions-system/

Given an array of strings products and a string `searchWord`. We want to design 
a system that suggests at most three product names from products after each 
character of `searchWord` is typed. Suggested products should have common prefix
with the `searchWord`. If there are more than three products with a common 
prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of 
`searchWord` is typed.

Example: 
Input: 
  products = ["mobile","mouse","moneypot","monitor","mousepad"]
  searchWord = "mouse"

Output: 
  [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
  ]

Explanation: 
  products sorted lexicographically:
    ["mobile","moneypot","monitor","mouse","mousepad"]
  After typing m and mo all products match and we show user:
    ["mobile","moneypot","monitor"]
  After typing mou, mous and mouse the system suggests:
    ["mouse","mousepad"]
'''

from typing import List

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
  products.sort()
  pre_dict = {}
  for p in products:
    for i in range(min(len(p), len(searchWord))):
      if p[i] == searchWord[i]:
        if i+1 not in pre_dict:
          pre_dict[i+1] = [p]
        else:
          pre_dict[i+1].append(p)
      else:
        break
  
  suggestions = []
  for j in range(1, len(searchWord) + 1):
    if j not in pre_dict:
      suggestions.append([])
    else:
      num = min(3, len(pre_dict[j]))
      suggestions.append(pre_dict[j][:num])

  return suggestions

if __name__ == "__main__":
    print('-' * 80)
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(suggestedProducts(products, searchWord))

    print('-' * 80)
    products = ["havana"]
    searchWord = "havana"
    print(suggestedProducts(products, searchWord))

    print('-' * 80)
    products = ["bags","baggage","banner","box","cloths"]
    searchWord = "bags"
    print(suggestedProducts(products, searchWord))

    print('-' * 80)
    products = ["havana"]
    searchWord = "tatiana"
    print(suggestedProducts(products, searchWord))