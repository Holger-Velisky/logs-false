from blessed import Terminal
import os
import time
a=open("n.txt", "r")
n=int(a.read())
a.close()
t=0
def update():
  a=open("n.txt", "r")
  n=int(a.read())
  a.close()
  os.remove("n.txt")
  b=open("n.txt", "x")
  b.close()
  c=open("n.txt", "w")
  c.write(str(n+1))
  c.close()
def logs():
  e=open("logs.txt", "r")
  m=str(e.read())
  e.close()
  m=m+"\n Username: "+h+"\n Password:  "+s+"\n"
  os.remove("logs.txt")
  f=open("logs.txt", "x")
  f.close()
  g=open("logs.txt", "w")
  g.write(m)
  g.close()
while not t==1:
  with Terminal().cbreak(), Terminal().hidden_cursor():
    print("Press |ENTER| to continue, or |esc| to quit.")
    inp = Terminal().inkey()
    os.system("cls" if os.name=="nt" else "clear")
  if repr(inp)=="KEY_ENTER":
    h=str(input("Username:  "))
    s=str(input("Password:  "))
    print("Done!")
    time.sleep(1.000)
    os.system("cls" if os.name=="nt" else "clear")
    logs()
    update()
  elif repr(inp)=="KEY_ESCAPE":
    p=3
    with Terminal().hidden_cursor():
      while p>0:
        print("Ok, closing")
        time.sleep(0.500)
        os.system("cls" if os.name=="nt" else "clear")
        print("Ok, closing.")
        time.sleep(0.500)
        os.system("cls" if os.name=="nt" else "clear")
        print("Ok, closing..")
        time.sleep(0.500)
        os.system("cls" if os.name=="nt" else "clear")
        print("Ok, closing...")
        time.sleep(0.500)
        os.system("cls" if os.name=="nt" else "clear")
        p=p-1
    print("Program closed!")
    os.system("cls" if os.name=="nt" else "clear")
    t=1