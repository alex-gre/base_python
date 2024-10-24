
class Calc:
       pass
       
       def sum(self,a: int, b: int) -> int:
              self.a = a
              self.b = b
              return (self.a + self.b)

       def sub(self,a: int, b: int) -> int:
              self.a = a
              self.b = b
              return (self.a  - self.b)       

       
       def mul(self,a: int, b: int) -> int:
              self.a = a
              self.b = b
              return (self.a  * self.b)
              
       def div(self,a: int, b: int) -> int:
              try:
                     self.a = a
                     self.b = b
                     return (self.a  / self.b)       
              except ZeroDivisionError as e:
                     print(e)

if __name__ == '__main__':
       '''==== Main ===='''
       c1 = Calc()

       print(f'Sum = {c1.sum(3,8)}')
       print(f'Sub = {c1.sub(3,8)}')
       print(f'Mul = {c1.mul(3,8)}')
       print(f'Div = {c1.div(3,0)}')
