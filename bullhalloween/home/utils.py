import uuid


def generate_image_filename(instance, filename):
    instance_path = 'uploaded'
    string_length = 15
    filename = str(uuid.uuid4())
    filename = filename.replace("-", "")
    return '{0}/{1}'.format(instance_path, filename[0:string_length]+'.jpg')
