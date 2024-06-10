#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6779564142:AAEWYw2Td2LbxboWPlmHDz9i3FXZ_BhEWTM")
    API_ID = int(os.environ.get("API_ID", "27760436"))
    API_HASH = os.environ.get("API_HASH", "8a3ceb4c4937b25d0af363b498f4d3a8")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6526760264")
