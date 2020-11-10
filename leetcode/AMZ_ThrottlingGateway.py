'''
AMZ Throttling Gateway
URL: https://leetcode.com/discuss/interview-question/895851/

gateway limits:
  num of transactions in 1sec <= 3
  num of transactions within 10secs <= 20
  num of transactions within 60secs <= 60
  otherwise, dropped

input:
  num - integer number of requests
  requestTime - list of integers representing time of request

'''

def throttler(num, requestTime):
  endTime = max(requestTime)

  # make times count map (index = requestTime)
  times = [0] * (endTime + 1)
  for i in range(num):
    times[requestTime[i]] += 1

  # track max drop of limits
  dropTimes = [0] * (endTime + 1)

  # num of transactions in 1sec <= 3
  for i in range(len(times)):
    if times[i] > 3:
      drops = times[i] - 3
      dropTimes[i] = max(drops, dropTimes[i])

  # num of transactions within 10secs <= 20
    prev = max(0, i - 9)
    spanSum = sum(times[prev : i + 1])
    if spanSum > 20:
      drops = min(times[i], spanSum - 20)
      dropTimes[i] = max(drops, dropTimes[i])

  # num of transactions within 60secs <= 60
    prev = max(0, i - 59)
    spanSum = sum(times[prev : i + 1])
    if spanSum > 60:
      drops = min(times[i], spanSum - 60)
      dropTimes[i] = max(drops, dropTimes[i])

  # print("dropCounts:{}".format(dropTimes))
  return sum(dropTimes)

if __name__ == "__main__":
  num = 27
  requestTime = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
  res = throttler(num, requestTime)
  print(res)