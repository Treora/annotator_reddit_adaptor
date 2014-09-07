# -*- coding: utf-8 -*-

"""
Store interface to plug into Hypothes.is
"""
from __future__ import absolute_import
from annotator_reddit_adaptor import annotator_reddit_adaptor

class RedditStore:
    def __init__(self, request):
        self.request = request

    def index(self):
        return

    def create(self):
        raise NotImplementedError()

    def read(self, key):
        pass

    def update(self, key, data):
        raise NotImplementedError()

    def delete(self, key):
        raise NotImplementedError()

    def search(self, **kwargs):
        query = kwargs['query']
        search_args = {
            'uri': query['uri'],
        }
        if 'limit' in kwargs:
            search_args['limit'] = kwargs['limit']
        results = annotator_reddit_adaptor.search(**search_args)
        total = len(results)
        return {
            'rows': results,
            'total': total,
        }

def includeme(config):
    from h import interfaces

    registry = config.registry

    if not registry.queryUtility(interfaces.IStoreClass):
        registry.registerUtility(AnnotatorStore, interfaces.IStoreClass)
