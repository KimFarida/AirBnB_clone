#!/usr/bin/python3
"""Entry level of command line console"""

import cmd
import json
from models import storage

class AirBnBCommand(cmd.Cmd):
    """Command line Processor"""

    prompt = "(hbnb)"
    l_classes = ['BaseModel']

    l_c = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def precmd(self, arg):
        """accepts command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            cls = arg.split('.')
            cnd = cls[1].split('(')
            args = cnd[1].split(')')
            if cls[0] in AirBnBCommand.l_classes and cnd[0] in AirBnBCommand.l_c:
                arg = cnd[0] + ' '+ cls[0] + ' '+ args[0]

        return arg

    def help_help(self):
        """Prints command line help"""
        print("Provides description of a command")

    def emptyline(self):
        """do nothing when it is empty line"""
        pass

    def do_count(self, cls_name):
        """counts the number of instances in a class"""
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            clss = k.split('.')
            if clss[0] == cls_name:
                count += 1
        print(count)

    def do_create(self, type_model):
        """creates an instance based on the class"""

        if not type_model:
            print("** class name is missing **")
        elif type_model not in AirBnBCommand.l_classes:
            print("** class does not exist **")
        else:
            dct = 