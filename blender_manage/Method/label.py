#!/usr/bin/env python
# -*- coding: utf-8 -*-


def getLabelFromName(name):
    if '_' in name:
        try:
            object_label = int(name.split('_')[0])
            return object_label
        except:
            pass

    if '.' in name:
        try:
            object_label = int(name.split('.')[0])
            return object_label
        except:
            pass

    try:
        object_label = int(name)
        return object_label
    except:
        pass

    return None
