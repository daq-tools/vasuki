##############
Vasuki service
##############

************
Installation
************
Install software on server machine.

Install Python3.6 for Debian 9.x stretch:
https://github.com/chriskuehl/python3.6-debian-stretch

Install packages::

    # Stop service.
    systemctl stop vasuki

    # Install virtualenv.
    virtualenv --python=python3.6 /opt/vasuki

    # Install gibberish package from GitHub
    /opt/vasuki/bin/pip install 'https://github.com/greghaskins/gibberish/tarball/3ec39861#egg=gibberish-0.3'

    # Install Vasuki.
    /opt/vasuki/bin/pip install vasuki[service] --upgrade

    # Make available as global command.
    echo 'alias vasuki=/opt/vasuki/bin/vasuki' > /etc/profile.d/vasuki.sh

    # Install and activate systemd unit file.
    wget https://raw.githubusercontent.com/daq-tools/vasuki/master/vasuki.service -O /usr/lib/systemd/system/vasuki.service
    systemctl daemon-reload
    systemctl reenable vasuki

    # Start service and check status.
    systemctl start vasuki
    systemctl status vasuki
