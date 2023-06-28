$namespaces:
  sbg: https://www.sevenbridges.com/
arguments: []
baseCommand:
- echo
- $PATH
class: CommandLineTool
cwlVersion: v1.0
id: omero_wrapper_test
inputs:
- default: /miniconda/envs/omero-wrapper/bin:$PATH
  id: environ_PATH
  type: string?
- default: /tmp
  id: environ_OMERO_TMPDIR
  type: string?
label: omero_wrapper_test
outputs:
- id: test_out
  type: stdout
requirements:
- class: DockerRequirement
  dockerPull: estorrs/omero-wrapper:0.0.1
- class: ResourceRequirement
  ramMin: 10000
- class: EnvVarRequirement
  envDef:
    OMERO_TMPDIR: $(inputs.environ_OMERO_TMPDIR)
    PATH: $(inputs.environ_PATH)
stdout: test_out.txt
