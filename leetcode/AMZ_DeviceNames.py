'''
AMZ Device Names
URL: https://leetcode.com/discuss/interview-question/896563/

Add an integer (incrementally) to devicenames to make them unique

Input:
num - integer representing number of device names
devicenames - list of strings representing device names

Output:
Return a list of strings representing the usernames in the order assigned
'''

def namer(num, devicenames):
  
  devices = {}
  for d in range(num):
    name = devicenames[d]
    if name not in devices:
      devices[name] = 1
    else:
      devicenames[d] = name + str(devices[name])
      devices[name] += 1

  return devicenames

if __name__ == "__main__":
    num = 6
    devicenames = ["switch", "tv", "switch", "tv", "switch", "tv"]
    res = namer(num, devicenames)
    print(res)