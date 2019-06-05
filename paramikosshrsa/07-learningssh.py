#!usr/bin/python3
"""Raddle"""

import os
import paramiko

SRVRS = [{'ip':'10.10.2.3','un':'bender'},{'ip':'10.10.2.4','un':'fry'}]

with open('cmds2issue.txt','r') as cmds:
    CMDLIST = cmds.readlines()

def cmdissue(sshsession,commandtoissue):
    ssh_stdin,ssh_stdout,ssh_stderr = sshsession.exec_command(commandtoissue)
    return ssh_stdout.read().decode('utf-8').rstrip('\n')

def main():
    #harvest RSA key (ssh priv key)
    myprivkey = paramiko.RSAKey.from_private_key_file('/home/student/.ssh/id_rsa')
    
    for server in SRVRS:
        #init connection
        sshsession = paramiko.SSHClient()
        sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        sshsession.connect(hostname=server['ip'], username=server['un'],pkey=myprivkey)
        #touch two files
        

        #get uptime of server
        for commandtoissue in CMDLIST:
            result = cmdissue(sshsession,commandtoissue)
            if result !='':       
                with open('serverresults.log','a') as svrlog:
                    print(result, file=svrlog)

        #close the connection
        sshsession.close()
if __name__ == '__main__':
    main()
