# omero-wrapper

A CLI wrapper for omero. Dockerized and used within CWL imaging workflows for the Ding Lab.

## Installation

```bash
pip install git+https://github.com/estorrs/omero-wrapper
```

## Usage

+ mode
  + One of ['upload', 'download', 'show-channel-thresholds']. Determines task to perform.
 
+ --filepath
  + Filepath to upload or download file to.
 
+ --image-id
  + Omero image id to download.
 
+ --dataset
  + Name of dataset --image-name is in. Only used if no --image-id is provided.
 
+ --image-name
  + Name of image in --dataset. Only used if no --image-id is provided.
 
+ --username
  + Omero username. If none is provided, then will use value in OMERO_USERNAME environmental variable.

+ --password
  + Omero password. If none is provided, then will use value in OMERO_PASSWORD environmental variable.

+ --group
  + Omero group to import or download with. Default is HTAN.

+ --project
  + Omero project to import or download in. Default is Multiplex_Imaging.

+ --host
  + Omero host url. Default is htan-imaging.wucon.wustl.edu.
 
+ --port
  + Omero port. Default is 4064.

## Examples

#### Upload image to omero

```bash
omero-wrapper upload --filepath FILEPATH --dataset DATASET --image-name IMAGE_NAME
```

#### Download image from omero

By dataset/image name

```bash
omero-wrapper download --filepath FILEPATH --dataset DATASET --image-name IMAGE_NAME
```

By image id

```bash
omero-wrapper download --filepath FILEPATH --image-id IMAGE_ID
```

#### show channel thresholds

```bash
omero-wrapper show-channel-thresholds --dataset DATASET --image-name IMAGE_NAME
```

## Docker

```bash
docker pull estorrs/omero-wrapper:0.0.1
```
