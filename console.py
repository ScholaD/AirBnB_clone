#!/usr/bin/env python3
"""
doc
"""
import cmd
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

    def do_mytest_(self, line):
        Samp = storage.all()
        print(Samp)

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
        elif len(lines) != 2:
            print("** instance id missing **")
        else:
            obj_a = storage.all()
            for a in obj_a.keys():
                if "{}.{}".format(lines[0], lines[1]) == a:
                    flag = 1
                    print(obj_a[a])
            if flag == 0:
                print("** no instance found **")

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
                            if lines[3][0] == '"' and lines[3][-1] == '"':
                                setattr(obj_c, lines[2], lines[3][1:-1])
                                storage.save()
                        break
            if flag == 0:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
