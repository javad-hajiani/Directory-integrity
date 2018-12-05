# fchecker File Integrity Checker

## Getting Started

This script help us for logging changed files realtime and mail it.Its my experience for our servers

You Can Logging Into File or Local Syslog or Directly Send to Syslog Server or finaly send to specific mail.

### Requirements

- Python3
 - Debian Based
  - > sudo apt install python3
 - Redhat Based
  - > sudo yum install python3
 - Arch Based
  - > sudo pacman -Sy python3
- mail command
 - Debian Based
  - > sudo apt install mailutils
 - Redhat Based
  - > sudo yum install mailx
  - > sudo dnf install mailx
 - Arch Based
  - > sudo pacman -Sy mailutils 
### Configuration

##### Run Script to install Python package
- Service Base
 - Run With root Permission > sudo /path/to/run.sh
- crontab -e
 - Run With root Permission > @reboot /usr/bin/python3 /path/to/main 

##### Start fchecker Service
- Service Command
 - > sudo service fchecker start
- INIT File
 - > sudo /etc/init.d/fchecker start

##### Run as Startup
- update-rc.d
 - > sudo update-rc.d fchecker enable
- chkconfig
 - > sudo chkconfig fchecker on
