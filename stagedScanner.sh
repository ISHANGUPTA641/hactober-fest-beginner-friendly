#! bin/bash
rm 'ScanResults.txt'
echo "-----------------------------------------------" 
echo "Staged scanner 1.0" 
echo "                      Devoloped by Mihir Sahani" 
echo "-----------------------------------------------" 
nmap -T4 -p- $1 | grep 'open' | cut -d '/' -f 1 >> 'ScanResults.txt' 
echo "Quick Scanning..."
port_list=""

while read port; do 
    port_list+=$port
    port_list+=","
done <ScanResults.txt

port_list=${port_list::-1}
rm "ScanResults.txt"
nmap -T4 -A -p $port_list $1 > ScanResult.txt 
echo "Doing Deep Scan...might take some time."

echo "----------------------------------------------" 
echo "Scan Complete!"
echo "Scan Results saved in ScanResults.txt"
