#!/usr/bin/env python3
"""
doc
"""
import cmd
import sys
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    the console for runing commands
    """
    prompt = "(hbnb)"
    __available_class = [
            "BaseModel", "User", "State", "City", "Amenity",
            "Place", "Review"
            ]

    @classmethod
    def handleArg(cls, self, cmd_cls, arg_):
        """
        this method is to be called by 'parseline'
        It handles the case whereby the command has an argument
        exanample: BaseModel.show("1234-1234-12334")
        """
        sep = ['"', "'"]
        arg = arg_.split(',')
        if arg[0][0] not in sep or arg[0][-1]\
                not in sep or arg[0][0] != arg[0][-1]:
            return 'continue_'
        if len(arg) == 1:
            result = cmd.Cmd.parseline(self, f"{cmd_cls} {arg_[1:-1]}")
            return result
        else:
            id_ = arg[0]
            arg[1] = arg[1].strip()
            arg[-1] = arg[-1].strip()
            if arg[1][0] == '{' or arg[-1][-1] == '}':
                arg[1] = arg[1][1:]
                arg[-1] = arg[-1][:-1]
                try:
                    start = len(id_)
                    dict_ = eval(arg_[start:])
                except Exception:
                    return 'continue_'
                for i, j in dict_:
                    HBNBCommand.handleArg(
                            cls, self, cmd_cls, f'{id_}, {i}, {j}')
            else:
                if arg[0][0] not in sep or arg[0][-1] not in sep or\
                        arg[0][0] != arg[0][-1]:
                    return 'continue_'
                id_ = arg[0][1:-1]
                if(len(arg) > 1):
                    if len(arg) != 3:
                        return 'continue_'
                    else:
                        arg[1] = arg[1].strip()
                        if arg[1][0] not in sep or arg[1][-1] not in sep or\
                                arg[1][0] != arg[1][-1]:
                            return 'continue_'
                        arg[1] = arg[1][1:-1]
                        narg = ' '.join(arg[1:])
                        result = cmd.Cmd.parseline(
                                self, f"{cmd_cls} {id_} {narg}")
                        return result

    def parseline(self, line):
        """
        doc
        """
        lists = line.split('.')
        if any(_ == lists[0] for _ in HBNBCommand.__available_class
               ) and len(lists) == 2:
            cls = lists[0]
            nlists = lists[1]
            if '(' in nlists and nlists[-1] == ')':
                temp = nlists.split('(')
                if temp[0] != '':
                    command = temp[0]
                    arg = temp[1][:-1]
                    if arg != '':
                        result = HBNBCommand.handleArg(
                                self, f"{command} {cls}", arg)
                        if result != 'continue_':
                            return result
                    line = f"{command} {cls} {arg}"
        result = cmd.Cmd.parseline(self, line)
        return result

    def do_quit(self, line):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        CTR D to exit  the console
        """
        return True

    def do_create(self, line):
        """
        Creates new instance of BaseModel
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.__available_class:
            print("** class doesn't exist **")
        else:
            new_inst = eval(line)()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        Example: $show BaseModel 1234-1234-1234
        """
        flag = 0
        lines = line.split()
        if not line:
            print("** class name missing **")
        elif lines[0] not in HBNBCommand.__available_class:
            print("** class doesn't exist **")
        elif len(lines) < 2:
            print("** instance id missing **")
        else:
            obj_a = storage.all()
            for a in obj_a.keys():
                if "{}.{}".format(lines[0], lines[1]) == a:
                    flag = 1
                    print(obj_a[a])
            if flag == 0:
                print("** no instance found **")

    def do_count(self, line):
        """
        Prints the amount o instance of a paticular class
        Example: $count BaseModel
        """
        flag = 0
        count = 0
        lines = line.split()
        if not line:
            print("** class name missing **")
        elif lines[0] not in HBNBCommand.__available_class:
            print("** class doesn't exist **")
        else:
            obj_a = storage.all()
            for a in obj_a.keys():
                if "{}".format(lines[0]) == a[:len(lines[0])]:
                    count += 1
        print(f"{count}")

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        Example: destroy BaseModel 1234-1234-1234
        """
        flag = 0
        lines = line.split()
        if not line:
            print("** class name missing **")
        elif lines[0] not in HBNBCommand.__available_class:
            print("** class doesn't exist **")
        elif len(lines) != 2:
            print("** instance id missing **")
        else:
            obj_a = storage.all()
            for a in obj_a.keys():
                if "{}.{}".format(lines[0], lines[1]) == a:
                    flag = 1
                    del obj_a[a]
                    storage.save()
                    break
            if flag == 0:
                print("** no instance found **")

    def do_all(self, line):
        """
        Prints all string representation of all instance
        based or not on the class
        Example: $ all BaseModel or $ all
        """
        flag = 0
        if not line:
            obj_a = storage.all()
            print('[', end='')
            for a in obj_a.keys():

                flag += 1
                if flag < len(obj_a):
                    print('"{}"'.format(obj_a[a]), end=', ')
                else:
                    print('"{}"'.format(obj_a[a]), end='')
            print(']')

        elif line not in HBNBCommand.__available_class:
            print("** class doesn't exist **")
        else:
            obj_a = storage.all()
            new_l = []
            for b in obj_a.keys():
                if "{}".format(line) == b.split('.')[0]:
                    new_l.append(obj_a[b])
            print('[', end='')
            for a in new_l:
                flag += 1
                if flag < len(new_l):
                    print('"{}"'.format(a), end=', ')
                else:
                    print('"{}"'.format(a), end='')
            print(']')

    def do_update(self, line):
        """
        Update an instance based on the class name and id by
        adding or updating attribute
        =====================================================================
        Usage: update <Class name> <id> <attribute name> \"<attribute value>\"
        Example: $ update BaseModel 1234-1234-1234 email \"aibnb@email.com\"
        =====================================================================
        """
        flag = 0
        lines = line.split()
        if not line:
            print("** class name missing **")
        elif lines[0] not in HBNBCommand.__available_class:
            print("** class doesn't exist **")
        elif len(lines) < 2:
            print("** instance id missing **")
        else:
            obj_a = storage.all()
            for a in obj_a.keys():
                if "{}.{}".format(lines[0], lines[1]) == a:
                    flag = 1
                    if len(lines) < 3:
                        print("** attribute name missing **")
                        break
                    elif len(lines) < 4:
                        print("** value missing **")
                        break
                    else:
                        obj_c = obj_a[a]
                        if lines[2] not in ['id', 'created_at', 'updated_at']:
                            try:
                                val = eval(lines[3])
                                setattr(obj_c, lines[2], val)
                                storage.save()
                            except Exception:
                                pass
                        break
            if flag == 0:
                print("** no instance found **")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    else:
        HBNBCommand().cmdloop()
