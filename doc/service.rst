##############
Vasuki service
##############

************
Installation
************
Install software on server machine.

Install packages::

    # Stop service.
    systemctl stop vasuki

    # Install virtualenv.
    python3 -m venv /opt/vasuki

    # Install gibberish package from GitHub
    /opt/vasuki/bin/pip install 'https://github.com/greghaskins/gibberish/tarball/3ec39861#egg=gibberish-0.3'

    # Install Vasuki.
    /opt/vasuki/bin/pip install vasuki[service] --upgrade

    # Display version of Vasuki after installation / upgrade.
    vasuki --version

    # Make available as global command.
    echo 'alias vasuki=/opt/vasuki/bin/vasuki' > /etc/profile.d/vasuki.sh

    # Install and activate systemd unit file.
    wget https://raw.githubusercontent.com/daq-tools/vasuki/master/vasuki.service -O /usr/lib/systemd/system/vasuki.service
    systemctl daemon-reload
    systemctl reenable vasuki

    # Start service and check status.
    systemctl start vasuki
    systemctl status vasuki

    # Display version of Vasuki after system unit start.
    vasuki --version
