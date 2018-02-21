# coding: utf-8

import os


DEFAULT_TEMPLATE = os.environ.get("DEFAULT_TEMPLATE")
if not DEFAULT_TEMPLATE:
    DEFAULT_TEMPLATE = '''{"id": $count, "ts": "$ts"}'''
