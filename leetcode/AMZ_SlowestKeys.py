'''
Slowest Keys (Amazon Variant)
URL: https://leetcode.com/discuss/interview-question/905158/

Amazon engineers have redesigned a keypad used by delivery drivers in urban 
areas. In order to determine which key takes the longest time to press, the 
keypad is tested by a driver.

Given the results of that test which contains encoded key pressed and the time 
at which it was pressed, write an algorithm to determine which key takes the 
longest to press.

Input
The input to the function/method consists of two arguments:
num, an integer representing the number of keys;
keyTimes, a list of pairs of integers where the first element representing the 
encoded key pressed and the second element representing the time at which it was 
pressed.

Output
Return a character representing the key that took the longest time to press.

Note
There will only be one key with the longest time.
keyTimes is sorted in ascending order of keyTimes[i][1].
Encoded key characters in the range ascii[a-z] where a = 0, b = 1, ..., Z = 25.
The starting time of the test is 0.

Constraints
1 <= num <= 10^5
0 <= keyTimes[i][0] <= 25, where keyTimes[i][0] represents the first element of keyTimes.
1 <= keyTimes[i][1] <= 10^8, where keyTimes[i][1] represents the second element of keyTimes.
0 <= i < num

Example
Input:
num= 4
keyTimes = [(0, 2), (1,5), (0, 9), (2, 15)]
Output:
c

Explanation:
Elements in keyTimes[i][0] represent encoded characters in the range ASCII[a-z] 
where a = 0, b = 1,..., z = 25. The second element, key Times (1) represents the 
time the key is pressed since the start of the test. The elements will be given 
in ascending time order. In the example, keys pressed, in order are 0102 and 
encoded as = abac at times 2,5,9, 15. From the start time, it took 2 - 0 = 2 to 
press the first key, 5 - 2 = 3 to press the second, and so on. The longest time 
it took to press a key was key 2, or 'c', at 15 - 9 = 6.
'''
import string

def slowestKeys (keyTimes, num):
  max_keyTime = keyTimes[0]
  for i in range(1, num):
    currTime = keyTimes[i][1]
    prevTime = keyTimes[i-1][1]
    if currTime - prevTime > max_keyTime[1]:
      max_keyTime = keyTimes[i]

  return string.ascii_lowercase[max_keyTime[0]]

if __name__ == "__main__":
  num = 4
  keyTimes = [(0,2), (1,5), (0,9), (2,15)]
  print(slowestKeys(keyTimes, num))