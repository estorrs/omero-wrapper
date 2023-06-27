import argparse
import logging
import os
import subprocess

from omero.gateway import BlitzGateway

import omero_wrapper.utils as utils


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

parser = argparse.ArgumentParser()

parser.add_argument(
    'mode', type=str, choices=['upload', 'download', 'show-channel-thresholds'],
    help='Mode to run.')

#############
## general ##
#############
parser.add_argument(
    '--username', type=str, required=True,
    help='Omero username. If none is provided, then will use value in OMERO_USERNAME environmental variable.')

parser.add_argument(
    '--password', type=str,
    help='Omero password. If none is provided, then will use value in OMERO_PASSWORD environmental variable.')

parser.add_argument(
    '--group', type=str, default='HTAN',
    help='Omero group to import or download with.')

parser.add_argument(
    '--project', type=str, default='Multiplex_Imaging',
    help='Omero project to import or download with.')

parser.add_argument(
    '--host', type=str, default='htan-imaging.wucon.wustl.edu',
    help='Omero host url.')

parser.add_argument(
    '--port', type=str, default='4064',
    help='Omero port.')

parser.add_argument(
    '--filepath', type=str,
    help='File to upload or location to save file.')

parser.add_argument(
    '--image-id', type=str,
    help='ID of image to download')

parser.add_argument(
    '--dataset', type=str,
    help='Omero dataset to upload image to or download image from.')

parser.add_argument(
    '--image-name', type=str,
    help='Name of image in dataset to download')


args = parser.parse_args()


def get_login_info():
    if args.password is None:
        if 'OMERO_PASSWORD' in os.environ:
            password = os.environ['OMERO_PASSWORD']
        else:
            raise RuntimeError('No password provided, and none found in OMERO_PASSWORD.')
    else:
        password = args.password

    if args.username is None:
        if 'OMERO_USERNAME' in os.environ:
            username = os.environ['OMERO_USERNAME']
        else:
            raise RuntimeError('No username provided, and none found in OMERO_USERNAME.')
    else:
        username = args.username

    return username, password


def upload_image():
    if args.filepath is None or args.dataset is None:
        raise RuntimeError('Must specify a --filepath and --dataset to upload.')
    username, password = get_login_info()
    image_name = args.image_name.replace('.ome.tiff', '') if args.image_name is not None else args.dataset
    pieces = [
        'omero', 'import',
        args.filepath,
        '-T', f'Project:name:{args.project}/Dataset:name:{args.dataset}/Image:name:{image_name}',
        '--user', username,
        '--password', password,
        '--host', args.host,
        '--port', args.port,
    ]
    command = ' '.join(pieces)
    logging.info('running {command}')
    outs = subprocess.check_output(command, shell=True)
    logging.info(outs)
    logging.info('finished import')

def download_image():
    if args.filepath is None:
        raise RuntimeError('Must specify a save --filepath')
    if args.image_id is None and (args.dataset is None or args.image_name is None):
        raise RuntimeError('Must specify a --dataset/--image-name or --image-id to download.')
    username, password = get_login_info()

    if args.image_id is not None:
        pieces = [
            'omero', 'export',
            '--user', username,
            '--password', password,
            '--host', args.host,
            '--port', args.port,
            '--file', args.filepath,
            f'Image:{args.image_id}',
        ]
    else:
        pieces = [
            'omero', 'export',
            '--user', username,
            '--password', password,
            '--host', args.host,
            '--port', args.port,
            '--file', args.filepath,
            f'Project:name:{args.project}/Dataset:name:{args.dataset}/Image:name:{args.image_id}'
        ]
    command = ' '.join(pieces)
    logging.info('running {command}')
    outs = subprocess.check_output(command, shell=True)
    logging.info(outs)
    logging.info('finished import')


def show_image_thresholds():
    if args.image_id is None and (args.dataset is None or args.image_name is None):
        raise RuntimeError('Must specify a --dataset/--image-name or --image-id to download.')
    username, password = get_login_info()

    conn = BlitzGateway(username, password, host=args.host, port=args.port,
                    secure=True, group=args.group)
    conn.connect()

    labels, thresholds = utils.get_min_thresholds(
        conn, project=args.project, dataset=args.dataset,
        image_name=args.image_name, image_id=args.image_id)

    for label, thresh in zip(labels, thresholds):
        print(f'{label}\t{thresh}')
    
    conn.close()


def main():
    if args.mode == 'upload':
        upload_image()
    elif args.mode == 'download':
        download_image()
    elif args.mode == 'show-channel-thresholds':
        show_image_thresholds()


if __name__ == '__main__':
    main()
