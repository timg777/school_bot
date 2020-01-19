import sys
import os
import time
from termcolor import colored

os.system('clear')

os.system('touch report.txt')
os.system('touch id_database.txt')
os.system('touch err.txt')
os.system('touch mess_dump.txt')
os.system('touch homewk_mess_dump.txt')
os.system('touch 11А.txt')
os.system('touch 11Б.txt')
os.system('touch 11Г.txt')
os.system('touch 11В.txt')

gr_id = input(colored('Enter your group id: ', 'red'))
gr_name = input(colored('Enter your group name: ', 'red'))
your_id = input(colored('Enter your id to send traceback if bot crashed: ', 'red'))
gr_token = input(colored('Enter your group token (you can see it in group settings): ', 'red'))
changed_gr_id = input(colored('Enter your changed group id (optional): ', 'red'))
s_email_addr = input(colored('Enter sender email to send traceback: ', 'red'))
r_email_addr = input(colored('Enter receiver email to send traceback: ', 'red'))
email_pswd = input(colored('Enter sender email password (it still only with you, no fishing): ', 'red'))
changed_gr_id = gr_id if changed_gr_id != None else print('id not cnahged...')

os.system('clear')
print(colored('Thank you for using my bot)', 'green'))
print(colored('Enjoy it!', 'green'))
print(colored('loading...' + '\33[5m', 'green'))
time.sleep(1)
os.system('clear')

with open('pkg/data.txt', 'w') as ouf:
    ouf.write(gr_id + ' ')
    # ouf.write('189837135 ')
    ouf.write(gr_name + ' ')
    # ouf.write('ШК ')
    ouf.write(your_id + ' ')
    # ouf.write('225786165 ')
    ouf.write(gr_token + ' ')
    # ouf.write('244bf1f2fa65586fc4ebc4b87d138e360d6fec8eaaebae75b36ee525e3d53f7106b954ff34ff139048d74 ')
    ouf.write(changed_gr_id + ' ')
    # ouf.write('basicscheme')
    ouf.write(s_email_addr + ' ')
    ouf.write(email_pswd + ' ')
    ouf.write(r_email_addr)

os.system('mv pkg/* .')
os.system('rm -rf pkg run_bot.py')
os.system('clear')
os.system('python3 bot.py')
