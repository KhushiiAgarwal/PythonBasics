#Return only the 1st non-repeating char
MAX_CHAR = 25
def non_repeat_char(str):
  freq = [0] * MAX_CHAR
  for c in str:
    freq[ord(c) - ord('a')] += 1
  for c in s:
          if freq[ord(c) - ord('a')] == 1:
              return c
  return 'None'

s = input()
print(non_repeat_char(s))
