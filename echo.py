# 
import sys  # 引入一个叫 sys 的“工具包”

def echo():
  shout = "-s" in sys.argv # 检查启动参数里有没有 "-s"
  message = input("ComeAndType something: ")
  print(message.upper() if shout else message)

if __name__ == "__main__":
  echo()