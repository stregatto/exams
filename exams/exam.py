#!/usr/bin/python 
import os
#import requests
import logging
import argparse
import json
import sys
import cmd
from examSQL import examSQL

"""
TO DO:
    simply ALL

"""

class myCommands(examSQL.sqlCommands):
    
    def do_test(self,line):
        """
        Give the list of the available course.
        """
        print "test"
        return

class ExamShell(cmd.Cmd, myCommands):
    '''
    interactive shell
    '''

    prompt  = "eis ;) "
    intro   = "Exams Interactive Shell.\nType 'help' or ? to obtain generic help\ntype 'command help' to obtain comman usage help\n"

    def emptyline(self):
        """
        emptyline method
        """
        return
    
    def preloop(self):
        #self._scan_checks()
        return
    
    def completedefault(self, text, line, begidx, endidx):
        if not text:
            completios = self.cn.keys()
        else:
            completios = [c for c in self.cn.keys() if c.startswith(text)]
        return completions

    def do_quit(self, line):
        """
        quit from Exam Interactive Shell
        """
        return True

    def run(self,action, *args, **kwdargs):
        print "launching command loop"
        self.cmdloop()


if __name__ == '__main__':
    
    eis =  ExamShell().cmdloop()
    #eis.run(args.action)
    exit(0)
