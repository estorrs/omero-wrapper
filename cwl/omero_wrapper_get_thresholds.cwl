$namespaces:
  sbg: https://www.sevenbridges.com/
arguments:
- position: 1
  valueFrom: show-channel-thresholds
baseCommand:
- python
- /omero-wrapper/omero_wrapper/omero.py
class: CommandLineTool
cwlVersion: v1.0
id: omero_wrapper_get_thresholds
inputs:
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
label: omero_wrapper_get_thresholds
outputs:
- id: channel_thresholds
  type: stdout
requirements:
- class: DockerRequirement
  dockerPull: estorrs/omero-wrapper:0.0.1
- class: ResourceRequirement
  ramMin: 10000
- class: EnvVarRequirement
  envDef:
    PATH: $(inputs.environ_PATH)
stdout: channel_thresholds.txt
