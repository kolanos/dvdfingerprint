import hashlib
import os
import sys

__VERSION__ = "0.1.0"


def generate_hash(s):
    s = hashlib.md5(s).hexdigest().upper()
    return "-".join([s[:8], s[8:12], s[12:16], s[16:20], s[20:]])


def get_paths(root_dir):
    file_list = []
    for root, subFolders, files in os.walk(root_dir):
        for file in files:
            f = os.path.join(root, file)
            s = os.path.getsize(f)
            f = f.replace(root_dir, '')
            if not f.startswith('/'):
                f = '/%s' % f
            file_list.append("%s:%d" % (f, s))
    return file_list


def combine_files(f):
    f.sort()
    return ":%s" % ":".join(f)


def fingerprint(path):
    p = get_paths(path)
    s = combine_files(p)
    return generate_hash(s)
