smbfileage.py connects to a Windows share and obtains the last
modified date of the file. If that's older than -c, then a critical
message is produced. If it's older than -w, then a warning. Otherwise,
all is ok.

Example usage:

$ ./smbfileage.py -w 86400 -c 259200 --user=USERNAME --password='PASSWORD' --domain DOMAIN host1 'C$' /path/to/file
smbfileage OK - 7:24:53.548357


$ ./smbfileage.py -w 86400 -c 259200 --user=USERNAME --password='PASSWORD' --domain DOMAIN host2 'C$' /path/to/an/older/file
smbfileage WARNING - file getting old: 2 days, 7:01:03.281406


$ ./smbfileage.py -w 86400 -c 259200 --user=USERNAME --password='PASSWORD' --domain DOMAIN host3 'C$' /invalid/path/to/file
smbfileage CRITICAL - unable to access file
