#!/bin/env python
# -*- coding: utf8 -*-

import fedmsg

"""
The latest Fedmsg meta code for Fedimg fedmsgs (what a mouthful!):
https://github.com/fedora-infra/fedmsg_meta_fedora_infrastructure/blob/develop/fedmsg_meta_fedora_infrastructure/fedimg.py
"""


def message(image_url, dest, status):
    """ Takes an image name, an upload destination (ex. "EC2-eu-west-1"), and a
    status (ex.  "failed"). Emits a fedmsg appropriate for each image upload
    task. """

    topic = 'image.upload'
    image_name = image_url.split('/')[-1].replace('.raw.xz', '')

    fedmsg.publish(topic=topic, modname='fedimg', msg={
        'image_url': image_url,
        'image_name': image_name,
        'destination': dest,
        'status': status,
    })
