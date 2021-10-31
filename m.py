def composite(num):
  for i in range(2, num):
        if (num % i) != 0:
            print(num, "is  a prime number")
            break
  else:
      print(num, "is a PRIME number")
composite(99)      