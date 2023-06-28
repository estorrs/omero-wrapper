def get_image(conn, project=None, dataset=None, image_name=None, image_id=None):
    if image_id is not None:
        image = conn.getObject("Image", image_id)
    else:
        project = next(iter(conn.getObjects("Project", attributes={"name": project})))
        dataset = project.findChildByName(dataset)
        image = dataset.findChildByName(image_name)
    return image


def get_min_thresholds(conn, project=None, dataset=None, image_name=None, image_id=None):
    image = get_image(
        conn, project=project, dataset=dataset, image_name=image_name, image_id=image_id)
    
    labels = image.getChannelLabels()
    rendering_defs = image.getAllRenderingDefs()
    channel_metadata = rendering_defs[0]['c']
    thresholds = [c['start'] for c in channel_metadata]

    return labels, thresholds


def get_image_id(conn, project, dataset, image_name):
    image = get_image(
        conn, project=project, dataset=dataset, image_name=image_name)
    return image.getId()