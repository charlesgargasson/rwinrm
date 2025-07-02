from pypsrp.wsman import WSMan
from pypsrp.client import Client
from pypsrp.powershell import PowerShell, RunspacePool
import sys

cmd=[]
skiplist = []
curcmd = -1
auth="negotiate"
password=None
service="HTTP"

for i in range(1,len(sys.argv[1:])):
    if i in skiplist :
        continue

    match sys.argv[i]:
        case "--service":
            service = sys.argv[i+1]
            skiplist.append(i+1)
        case "--auth":
            auth = sys.argv[i+1]
            skiplist.append(i+1)
        case "--user":
            user = sys.argv[i+1]
            skiplist.append(i+1)
        case "--host":
            target = sys.argv[i+1]
            skiplist.append(i+1)
        case "--pass":
            password = sys.argv[i+1]
            skiplist.append(i+1)
        case "--password":
            password = sys.argv[i+1]
            skiplist.append(i+1)
        case "-c":
            val = sys.argv[i+1]
            skiplist.append(i+1)
            curcmd += 1
            cmd.append({
                'cmd':val,
                'params':{
                },
                'args':[
                ]
            })
        case "-p":
            key = sys.argv[i+1]
            val = sys.argv[i+2]
            cmd[curcmd]['params'][key]=val
            skiplist.append(i+1)
            skiplist.append(i+2)
        case "-a":
            val = sys.argv[i+1]
            if curcmd < 0:
                curcmd = 0
                cmd.append({
                    'cmd':'cmd.exe',
                    'params':{
                    },
                    'args':[
                        '/c'
                    ]
                })
            cmd[curcmd]['args'].append(val)
            skiplist.append(i+1)

# print(json.dumps(cmd))

def run_command(cmd):
    wsman = WSMan(target, username=user, password=password, ssl=False, auth=auth, cert_validation=False, negotiate_service=service)

    with RunspacePool(wsman) as pool:
        ps = PowerShell(pool)
        for cmdlet in cmd:
            print(f"[*] => cmdlet: {cmdlet['cmd']}")
            ps.add_cmdlet(cmdlet['cmd'])
            for param, paramvalue in cmdlet['params'].items():
                print(f"[*] -- param: {param}")
                print(f"[*] -- value: {paramvalue}")
                ps.add_parameter(param, paramvalue)
            for argvalue in cmdlet['args']:
                print(f"[*] -- arg: {argvalue}")
                ps.add_argument(argvalue)
        ps.invoke()
        if ps.had_errors:
            print('[!] Error')
        else:
            print('[*] Success')
        if len(ps.output) > 0 :
            print(f"[*] Printing output")
            for x in ps.output: 
                print(x)
        if len(ps.streams.debug) > 0:
            print(f"[*] Printing streams debug")
            for x in ps.streams.debug: 
                print(x)

def main():
    run_command(cmd)

if __name__ == '__main__':
    main()