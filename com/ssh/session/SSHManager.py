# _*_ coding:utf-8 _*_

import pexpect
import os
from com.common.execCommand.ExecUtil import ExecUtil

__author__ = 'Administrator'


class SSHManager(object):
    def __init__(self):
        pass

    def initSSHKey(self):
        home = ExecUtil.execCommand("echo ~")[1]
        if not os.path.exists(home + "/.ssh/id_rsa"):
            child = pexpect.spawnu('ssh-keygen')
            child.expect('(?i)(/root/.ssh/id_rsa):')
            child.sendline('\r')
            child.expect('(?i)Enter passphrase (empty for no passphrase):')
            child.sendline('\r')
            child.expect('(?i)Enter same passphrase again:')
            child.sendline('\r')
            child.expect('(?i)+-----------------+')
            child.close()

    def sshCopyId(self, user, host, passwd):
        child = pexpect.spawnu("ssh-copy-id -i ~/.ssh/id_rsa.pub " + user + "@" + host)
        child.expect('(?i)Are you sure you want to continue connecting (yes/no)?')
        child.sendline("yes")
        child.expect("(?i) password:")
        child.sendline(passwd)
        child.close()
