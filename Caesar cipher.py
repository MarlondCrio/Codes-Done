def caesar_cipher(p,y):
   
   def convert(x):
          import string
          z = string.ascii_lowercase
          y = z.index(x) 
          return y
      
   import string
   word = string.ascii_lowercase
   num = string.digits
   return_list= ''
   x = p.lower()
   
   for alt in x:
         if word.find(alt) >= 0:
            a = convert(alt)
            c = a + y
            if c >25:
                  while c > 0 :
                     c = c - 26
            elif c < 25:
               while c < 0:
                  c = c + 26
            else:
                  pass
            b = word[c]
            return_list = return_list + b
         elif num.find(alt) >= 0:
            g = int(alt)
            b = g + y
            if b == 10:
               b = 0
            elif b > 9:
               while b > 9:
                  b = b - 10
            elif  b < 0:
                  while b < 0:
                     b = b + 10

            return_list = return_list + str(b)
         else:
            return_list = return_list + str(alt)
   return_list        
   return return_list
ans = caesar_cipher('1234567890', 3)
print(ans)

