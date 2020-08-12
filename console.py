#!/usr/bin/python3
"""
Contains the entry point of the command interpreter
"""
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage
from datetime import datetime

modelnames = ("BaseModel", "User", "Place", "State", "City",
              "Amenity", "Review")


class HBNBCommand(cmd.Cmd):
    """Command interpreter/Contains the functionality for the HBNB console"""
    prompt = '(hbnb) '

    def do_create(self, line):
        items = line.split(" ")
        if len(items) is 0:
            print("** class name missing **")
            return
        if (items[0] in modelnames):
            model = eval(items[0] + "()")
            i = 1
            while i < len(items):
                prm = items[i]
                list_prm = prm.split("=")
                p1 = list_prm[0]
                p2 = list_prm[1]
                if "\"" in p2:
                    p2 = p2.replace('"', "")
                if "_" in p2:
                    p2 = p2.replace("_", " ")
                setattr(model, p1, p2)
                i = i + 1
            storage.new(model)
            storage.save()
            print(model.id)
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """
        Deletes an instance based on the
        class name and id
        (save the change into the JSON file).
        """
        line_items = line.split()
        if len(line_items) is 0:
            print("** class name missing **")
            return
        if line_items[0] in modelnames:
            if len(line_items) < 2:
                print("** instance id missing **")
                return
            key = line_items[0] + "." + line_items[1]
            if key not in storage.all():
                print("** no instance found **")
                return
            del(storage.all()[key])
            storage.save()
            return
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        updates an instance based on the
        class name and id by adding or updating
        attribute
        """
        parsed_input = line.split()
        if len(parsed_input) > 1:
            key = "{}.{}".format(parsed_input[0], parsed_input[1])
        if len(parsed_input) is 0:
            print("** class name missing **")
            return
        elif len(parsed_input) == 1:
            if parsed_input[0] in modelnames:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(parsed_input) == 2:
            if parsed_input[0] in modelnames:
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print("** attribute name is missing **")
            else:
                print("** class doesn't exist **")
        elif len(parsed_input) is 3:
            if parsed_input[0] in modelnames:
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print("** value missing **")
            else:
                print("** class doesn't exist **")
        elif len(parsed_input) is 4:
            if parsed_input[0] in modelnames:
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    setattr(storage.all()[key], parsed_input[2],
                            parsed_input[3])
                    setattr(storage.all()[key], "updated_at", datetime.now())
                    storage.save()
                    return
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        parsed_input = line.split()
        if len(parsed_input) > 1:
            key = "{}.{}".format(parsed_input[0], parsed_input[1])
        if len(parsed_input) < 1:
            print("** class name missing **")
        elif len(parsed_input) == 1:
            if parsed_input[0] in modelnames:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        elif len(parsed_input) == 2:
            if parsed_input[0] in modelnames:
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])
            else:
                print("** class doesn't exist **")

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        instances = models.storage.all()
        args = line.split()
        class_arg = args[0]
        if class_arg in modelnames:
            for key, value in instances.items():
                # print(str(value))
                class_key = (key.split("."))[0]
                if class_key == class_arg:
                    print(str(value))
        else:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """EOF command to exit the program"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """
        Do none
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
