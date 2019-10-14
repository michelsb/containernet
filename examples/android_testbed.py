#!/usr/bin/python
"""
This is the most simple example to showcase Containernet.
"""
from mininet.net import Containernet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.log import info, setLogLevel
setLogLevel('info')

net = Containernet(controller=Controller)

info('*** Adding controller\n')
net.addController('c0')

info('*** Adding docker clients\n')
c1 = net.addDocker('c1', ip='10.0.0.10', dimage="renanalves/android-testbed")
c2 = net.addDocker('c2', ip='10.0.0.11', dimage="renanalves/android-testbed")
c3 = net.addDocker('c3', ip='10.0.0.12', dimage="renanalves/android-testbed")
c4 = net.addDocker('c4', ip='10.0.0.13', dimage="renanalves/android-testbed")

info('*** Adding docker server\n')
serv1 = net.addDocker('serv1', ip='10.0.0.14', dimage="renanalves/server-testbed")

info('*** Adding containers interfaces\n')
if1 = net.addSwitch('if1')
if2 = net.addSwitch('if2')
if3 = net.addSwitch('if3')
if4 = net.addSwitch('if4')
ifserv1 = net.addSwitch('ifserv1')

info('*** Adding switches\n')
s1 = net.addSwitch('s1')
s2 = net.addSwitch('s2')
s2 = net.addSwitch('s3')

info('*** Creating links\n')
net.addLink(c1, if1)
net.addLink(c2, if2)
net.addLink(c3, if3)
net.addLink(c4, if4)
net.addLink(serv1, ifserv1)

net.addLink(if1, s1, cls=TCLink, delay='100ms', bw=1)
net.addLink(if2, s1, cls=TCLink, delay='100ms', bw=1)
net.addLink(if3, s2, cls=TCLink, delay='100ms', bw=1)
net.addLink(if4, s2, cls=TCLink, delay='100ms', bw=1)

net.addLink(s1, s3, cls=TCLink, delay='100ms', bw=5)
net.addLink(s2, s3, cls=TCLink, delay='100ms', bw=5)
net.addLink(ifserv1, s3, cls=TCLink, delay='100ms', bw=10)

info('*** Starting network\n')
net.start()
info('*** Testing connectivity\n')
net.ping([d1, d2])
info('*** Running CLI\n')
CLI(net)
info('*** Stopping network')
net.stop()