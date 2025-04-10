from typing import Optional


def add_white_spaces(s:str, max_len:int, op:Optional[str]=None): 
  if op :
    number_of_w_spaces=max_len-len(s)
    result=op+" "+" "*number_of_w_spaces+s
    #print("result",result)
    return result
  else:
    number_of_w_spaces=max_len-len(s)+2
    result=" "*number_of_w_spaces+s
    #print("result",result)
    return result
  
class Operation:
  def __init__(self, n1, op, n2):
    self.n1 = str(n1).strip()
    self.op = str(op).strip()
    self.n2 = str(n2).strip()
    self.res = str(self.calculate_res())
    self.max_len = int(self.calculate_max_len())
    self.format_properly()
    
  def calculate_res(self):
    if self.op == '+':
      return int(self.n1) + int(self.n2)
    elif(self.op == '-'):
      return int(self.n1) - int(self.n2)
    else: 
      raise Exception("Operator must be '+' or '-'.")

  def calculate_max_len(self):
    curr_max=max(len(str(self.n1)), len(str(self.n2)))
    curr_max=max(curr_max, len(str(self.res)))
    return curr_max

  def print(self):
    print(self.n1)
    print(self.n2)
    print(self.dashed_line)
    print(self.res)
    

  def __repr__(self):
    return f"{self.n1} {self.op} {self.n2} = {self.res}"

  def format_properly(self):
    self.n1=add_white_spaces(self.n1,self.max_len)
    self.n2=add_white_spaces(self.n2,self.max_len,self.op)
    self.res=add_white_spaces(self.res,self.max_len)
    self.dashed_line=str("-"*(self.max_len+2))
        