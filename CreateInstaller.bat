pyinstaller --noconfirm --log-level=WARN ^
    --onedir --windowed --uac-admin^
    --add-data="README.md;." ^
    --add-data="Logs\tracebacklog.txt;Logs" ^
    --add-data="PowerShell\PrintQueue.ps1;PowerShell" ^
    --distpath="E:\Games HardExternal\Python\PyInstallers" ^
    main.py