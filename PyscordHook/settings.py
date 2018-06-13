#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 13 jun. 2018

@author: artnod
'''

ENABLE_HOOK = [
    'TOPHOOK',
]

TOPHOOK = {
    'webhook_url' : '<webhook url>',
    'color' : 123123,
    'message' : {
        'author' : {
            'name' : 'Toto Le Robot',
            'icon' : 'https://discordapp.com/assets/6debd47ed13483642cf09e832ed0bc1b.png',
        },
        'desc_text' : '@everyone Vous souhaitez nous aider à nous faire connaitre et donc, voter pour le serveur ?',
        'fields' : [
            {
                'name' : 'C\'est possible ici une fois toutes les 2h. Merci à vous !',
                'value' : 'https://gta.top-serveurs.net/the-asylum',
            },
        ],
        'thumbnail' : 'https://cdn.discordapp.com/icons/378553286627950602/7732cab09295ee2dc4dd481c4138c351.png',
        'footer' : {
            'text' : 'The Asylum RP',
            'icon' : 'https://cdn.discordapp.com/icons/378553286627950602/7732cab09295ee2dc4dd481c4138c351.png',
        },
    },
}

LOG_CONF = {
    'log_dir' : 'X:/changeme',
    'max_bytes' : 5000000,
    'backup_count' : 5,
}