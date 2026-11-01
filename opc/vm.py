import subprocess

def startvm(name, typ):
    print(name, typ)
    cmd = f"VBoxManage startvm {name} --type={typ}".split()
    subprocess.run(cmd)

def listvm():
    cmd = f"VBoxManage list vms".split()
    subprocess.run(cmd)

def shutdown(name):
    cmd = f"VBoxManage controlvm {name} shutdown".split()
    subprocess.run(cmd)