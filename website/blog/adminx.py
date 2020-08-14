import xadmin
from blog.models import Entry


class EntryAdmin(object):
    """博客正文"""
    list_display=['title','author','visiting','created_time','modifyed_time']

xadmin.site.register(Entry,EntryAdmin)