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

## API Documentation

Server is running on PORT 8082.

**POST** /upload-file

The following parameters are supported on this end-point:
* `file` - this parameter is REQUIRED
* `threshold` (`float`)
* `noise` (`int`)
* `usegauss` (`boolean`) - supported values: true, false, 0, 1
* `maxcolseps` (`int`)
* `maxseps` (`int`)
* `minscale` (`float`)
* `maxlines` (`int`)

*If some parameters are not transmitted, they will have null value on the AI Layer.*

**Exceptions:**
* `InvalidFileExtensionException` (throwed when file doesn't have an extension):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"status": 400,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"error": "Bad Request",

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"message": "Invalid file extension"

* `UploadException` (throwed when the file cannot be saved on the file system):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"status": 400,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"error": "Bad Request",

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"message": "Error in uploading image"

* `ProcessingException` (throwed when the algorithm doesn't provide a response):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"status": 400,

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"error": "Bad Request",

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"message": "Processing error"
