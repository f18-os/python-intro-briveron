#! /usr/bin/env python3

import os, sys, time, re

pid = os.getpid()               # get and remember pid


import fileinput

leave=""


def isPipe(userIn):
    for i, Eric in enumerate(userIn):
        if Eric == '|':
            #print("I see the |")
            left,right = userIn.split('|')

            pr,pw = os.pipe()
            for f in (pr, pw):
                os.set_inheritable(f, True)
            print("pipe fds: pr=%d, pw=%d" % (pr, pw))

            rc = os.fork()


            if rc == 0:                   #  child - will write to pipe
                print("Child: My pid==%d.  Parent's pid=%d" % (os.getpid(), pid), file=sys.stderr)
                args = ["wc", "p3-exec.py"]

                os.close(1)                 # redirect child's stdout
                os.dup(pw)
                for fd in (pr, pw):
                    os.close(fd)
                print("hello from child")

            else:                           # parent (forked ok)
                print("Parent: My pid==%d.  Child's pid=%d" % (os.getpid(), rc), file=sys.stderr)
                os.close(0)
                os.dup(pr)
                for fd in (pw, pr):
                    os.close(fd)
                for line in fileinput.input():
                    print("From child: <%s>" % line)

def isRedirect(userIn):
    for i, Eric in enumerate(userIn):
        if Eric == '<':
            print("Do this <")

        elif Eric == '>':
            print("Do this >")

        os.write(1, ("About to fork (pid=%d)\n" % pid).encode())

        rc = os.fork()

        if rc < 0:
            os.write(2, ("fork failed, returning %d\n" % rc).encode())
            sys.exit(1)

        elif rc == 0:                   # child
            os.write(1, ("Child: My pid==%d.  Parent's pid=%d\n" %
                         (os.getpid(), pid)).encode())
            args = ["wc", "p3-exec.py"]

            os.close(1)                 # redirect child's stdout
            sys.stdout = open("p4-output.txt", "w")
            os.set_inheritable(1, True)

            for dir in re.split(":", os.environ['PATH']): # try each directory in path
                program = "%s/%s" % (dir, args[0])
                try:
                    os.execve(program, args, os.environ) # try to exec program
                except FileNotFoundError:             # ...expected
                    pass                              # ...fail quietly

            os.write(2, ("Child:    Error: Could not exec %s\n" % args[0]).encode())
            sys.exit(1)                 # terminate with error

        else:                           # parent (forked ok)
            os.write(1, ("Parent: My pid=%d.  Child's pid=%d\n" %
                         (pid, rc)).encode())
            childPidCode = os.wait()
            os.write(1, ("Parent: Child %d terminated with exit code %d\n" %
                         childPidCode).encode())


while leave!="exit":
    leave=input("[Brian_Shell]$ ")
    print(leave)
    rc = os.fork()

    copylist = leave

    if rc < 0:
        sys.exit(1)

    os.close(1)


    isPipe(leave)

    copylist.split(" ")
    isRedirect(leave)
