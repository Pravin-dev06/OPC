import subprocess

def startvm(name, typ):
    cmd = f"VBoxManage startvm {name} --type={typ}".split()
    subprocess.run(cmd)

def listvm():
    cmd = f"VBoxManage list vms".split()
    subprocess.run(cmd)