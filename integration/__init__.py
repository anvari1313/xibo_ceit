import os
from os.path import join, dirname
import integration.globs


def read_templates():
    path = join(dirname(__file__), 'xibo_templates/class-content.html')
    f = open(path, 'r')
    globs.class_content_temp = f.read()



read_templates()
