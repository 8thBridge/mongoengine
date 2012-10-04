from __future__ import absolute_import
from django.dispatch.dispatcher import Signal

__all__ = ['pre_init', 'post_init', 'pre_save', 'post_save',
           'pre_delete', 'post_delete']


pre_init = Signal('pre_init')
post_init = Signal('post_init')
pre_save = Signal('pre_save')
post_save = Signal('post_save')
pre_delete = Signal('pre_delete')
post_delete = Signal('post_delete')


