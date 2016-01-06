# _*_ coding:utf-8 _*_

__author__ = 'Administrator'
from com.common.BaseLoggingObj import BaseLoggingObj
from com.install.absInstaller.TarInstaller import TarInstaller
from com.common.execCommand.ExecUtil import ExecUtil
from com.Config import Config


class MavenInstaller(BaseLoggingObj, TarInstaller, object):
    def __init__(self, config=Config):
        BaseLoggingObj.__init__(self, config)
        TarInstaller.__init__(self)
        self.downloadPath = Config.softServer + Config.soft_java
        self.downloadSavePath = Config.softSavePath + "/" + Config.soft_maven
        self.installPath = Config.softInstallPath
        self.logging.info("add JavaInstaller module!")

    def downloadTar(self):
        down_rt = ExecUtil.execCommand("wget -O " + self.downloadSavePath + " " + self.downloadPath)

    def writeConfig(self):
        f = open("/etc/profile", 'a')
        f.write('export MAVEN_HOME=' + self.installPath + "/maven")
        f.write("export PATH=$MAVEN_HOME/bin:$PATH")
        f.close()
        source_rt = ExecUtil.execCommand("source /etc/profile")

    def make(self):
        tar_rt = ExecUtil.execCommand("tar zxvf " + self.downloadSavePath + " -C " + self.installPath)

    def unTar(self):
        pass
