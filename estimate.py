import math
import unittest

def wallis(n):
    sum=1
    def Eq(n):
        a=n**2
        #print(a)
        b=a*4
        c=b-1
        return(b/c)
    for i in range(1,n+1):
        frm=Eq(i);
        #print(f"{i} {frm} {sum*2}")
        sum=sum*frm;
        #print(sum)
    pi=sum*2
    return pi
    
def monte_carlo(n):
  cirdt=0
  sqdt=0
  while cirdt==0 or sqdt==0:
   for i in range(1,n+1):
     x=random.random()
     y=random.random()
     x=2*x
     y=2*y
     x=x-1
     y=y-1
     #print(f"{i} {x} {y}")
     sqrz=x**2+y**2
     z=sqrz**0.5
     if z<1.0:
       cirdt=cirdt+1
     else:
       sqdt=sqdt+1
  Pi=4*cirdt/n
  print (f"{cirdt} {sqdt}")
  return pi

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
