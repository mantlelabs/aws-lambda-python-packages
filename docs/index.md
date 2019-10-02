# lambda packages

The lambda zip package needs to contain all the code and the libraries
necessary for execution. But AWS lambda imposes several hard limits on us (details [here](https://docs.aws.amazon.com/lambda/latest/dg/limits.html)).
The limited deployment package size (50 MB compressed, 250 MB uncompressed
including all [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)) is reached quickly if you try to install libraries the usual `pip install` way.

#### first attempt: serverless-python-requirements

[Serverless Python Requirements](https://www.npmjs.com/package/serverless-python-requirements)
is a plugin for the Serverless framework that uses docker to create a .zip file with the code and the required libraries. But even with all the options to make the package slim and remove unnecessary files, just adding
`rasterio` and `fiona` results in too large .zip.

#### second attempt: use docker to create package.zip

This is based on the work on [Vincent Sarago](https://github.com/mapbox/aws-lambda-python-packages).
It uses Docker to create packages with certain libraries and tries to delete
all unnecessary files.


**My changes:**

* use the `python3.7` image from [lambci](https://hub.docker.com/r/lambci/lambda) as base image (they try to recreate the lambda environment as close as possible and is always up-to-date)

### Usage

1. Adjust Dockerfile to include code/handler function
2. Run `make <image_name>` for the images defined in `Makefile`
3. Use created .zip file for lambda


