**Due to limitations of AI layer, the only environment that the server-side can be executed is [Linux](https://distrowatch.com/).**

## Requirements - server-side

1. Install [JDK & JRE](https://www.digitalocean.com/community/tutorials/how-to-install-java-with-apt-on-ubuntu-18-04)
2. Install [Maven](https://www.mkyong.com/maven/how-to-install-maven-in-ubuntu/)

## Requirements - ai-layer

For the AI layer to work, the following should be installed:

1. Install [ocropy](https://github.com/tmbdev/ocropy)

&nbsp;&nbsp;&nbsp;&nbsp;Commands in order to install Ocropy:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`mkdir workingcopy/`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cd workingcopy/`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`git init .`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`git pull https://github.com/tmbdev/ocropy`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sudo apt-get install $(cat PACKAGES)`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`wget -nd http://www.tmbdev.net/en-default.pyrnn.gz`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`mv en-default.pyrnn.gz models/`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sudo python setup.py install`

2. Install [Python 2](https://www.python.org/)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`sudo apt install python2.7 python-pip`

## Build and run

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`cd wrSeg\Back-End\server-side`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`mvn package && java -jar target/wrseg-1.0-SNAPSHOT.jar`