import os
import subprocess
import sys

# make sure an argument was given
if len(sys.argv) != 2:
    print("Error: you must indicate a directory within your home directory")
    sys.exit(1)

# clean up the given argument
argPath = sys.argv[1]
if argPath[0] == "/":
    argPath = argPath[1:]

if argPath[len(argPath) - 1] == "/":
    argPath = argPath[:-1]

# create the directory path
repoDir = os.path.join(os.path.expanduser("~"), argPath)

# verify the constructed path exists
if not os.path.exists(repoDir):
    print("Error: specified directory does not exist: " + repoDir)
    sys.exit(1)

os.chdir(repoDir)

# make sure we are in a git repo
if not os.path.exists(repoDir + "/.git"):
    print("Error: specified directory is not a git repo: " + repoDir)
    sys.exit(1)

# pull and verify there was no error
pullResult = subprocess.run(["git", "pull"])
if pullResult.returncode != 0:
    print("Error: git pull errored with code " + pullResult.returncode)
    sys.exit(1)

# add, commit, and push
status = subprocess.run(["git", "status"], stdout=subprocess.PIPE)
if "nothing to commit, working tree clean" not in status.stdout.decode('utf-8'):
    subprocess.run(["git", "add", "-A"])
    subprocess.run(["git", "commit", "-m", "\"auto commit\""])
    subprocess.run(["git", "push"])
