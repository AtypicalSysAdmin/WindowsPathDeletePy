
#clear-print queue 
#restart-spooler


$HostName ="Server Name"

Stop-Service -InputObject $(Get-Service -ComputerName $HostName -Name Spooler) -Force

# give spooler service time to stop before deleting stuff
Start-Sleep -Seconds 1

$Before = (Get-ChildItem -Path \\$HostName\c$\Windows\System32\spool\PRINTERS).count
Write-Host "Number of files stuck in the queue: $Before"
$After = (Remove-Item -Path \\$HostName\c$\Windows\System32\spool\PRINTERS\* -Verbose).count
Write-Host "Number of files after removing the queue: $Before"
$Total = ($Before - $After)
$Jobs = ($Total / 2)

Write-Output "Done"
Write-Output "$Total items ($Jobs jobs) deleted."

# wait to make sure we're done deleting everything before starting spooler service
Start-Sleep -Seconds 1

Start-Service -InputObject $(Get-Service -ComputerName $HostName -Name Spooler)


#======================================================================================
#clear-printer error

$queue = Get-WMIObject win32_printer -ComputerName $HostName | Where-Object {$_.PrinterState -eq "2"}
 #Do errors exist?
 If ($queue)
 {
    #Clear out errors
    Write-Verbose "Clearing out print jobs with errors..."
    $queue | ForEach-Object {$_.CancelAllJobs() | Out-Null }
 }
 else{
    Write-Verbose "No errors"
 }
 	