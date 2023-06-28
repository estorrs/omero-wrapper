$namespaces:
  sbg: https://www.sevenbridges.com/
arguments:
- position: 1
  valueFrom: upload
baseCommand:
- python
- /omero-wrapper/omero_wrapper/omero_wrapper.py
class: CommandLineTool
cwlVersion: v1.0
id: omero_wrapper_upload
inputs:
- id: filepath
  inputBinding:
    position: '0'
    prefix: --filepath
  type: File
- id: dataset
  inputBinding:
    position: '0'
    prefix: --dataset
  type: string
- id: image_name
  inputBinding:
    position: '0'
    prefix: --image-name
  type: string
- default: HTAN
  id: group
  inputBinding:
    position: '0'
    prefix: --group
  type: string?
- default: Multiplex_Imaging
  id: project
  inputBinding:
    position: '0'
    prefix: --project
  type: string?
- default: htan-imaging.wucon.wustl.edu
  id: host
  inputBinding:
    position: '0'
    prefix: --host
  type: string?
- default: '4064'
  id: port
  inputBinding:
    position: '0'
    prefix: --port
  type: string?
- default: /miniconda/envs/omero-wrapper/bin:$PATH
  id: environ_PATH
  type: string?
- default: /tmp
  id: environ_OMERO_TMPDIR
  type: string?
label: omero_wrapper_upload
outputs: []
requirements:
- class: DockerRequirement
  dockerPull: estorrs/omero-wrapper:0.0.1
- class: ResourceRequirement
  ramMin: 10000
- class: EnvVarRequirement
  envDef:
    OMERO_TMPDIR: $(inputs.environ_OMERO_TMPDIR)
    PATH: $(inputs.environ_PATH)
