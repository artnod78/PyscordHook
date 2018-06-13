#!/usr/bin/python3
#-*- coding: utf-8 -*-
'''
Created on 13 jun. 2018

@author: artnod
'''
import sys, datetime, time, json, requests
from collections import defaultdict
import logging

class Webhook:
    def __init__(self, url, **kwargs):
        """
        Initialise a Webhook Embed Object
        """
        self.logger = logging.getLogger('discord_hook.Webhook')
        self.logger.debug('Init a Webhook object')
        self.url = url 
        self.msg = kwargs.get('msg')
        self.color = kwargs.get('color')
        self.title = kwargs.get('title')
        self.title_url = kwargs.get('title_url')
        self.author = kwargs.get('author')
        self.author_icon = kwargs.get('author_icon')
        self.author_url = kwargs.get('author_url')
        self.desc = kwargs.get('desc')
        self.fields = kwargs.get('fields', [])
        self.image = kwargs.get('image')
        self.thumbnail = kwargs.get('thumbnail')
        self.footer = kwargs.get('footer')
        self.footer_icon = kwargs.get('footer_icon')
        self.ts = kwargs.get('ts')
    
    def add_field(self,**kwargs):
        '''
        Adds a field to `self.fields`
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        name = kwargs.get('name')
        value = kwargs.get('value')
        inline = kwargs.get('inline', True)
        field = {
            'name' : name,
            'value' : value,
            'inline' : inline
        }
        self.fields.append(field)
    
    def set_desc(self,desc):
        '''
        Set description
        '''
        self.logger.debug(sys._getframe().f_code.co_name)   
        self.desc = desc
    
    def set_author(self, **kwargs):
        '''
        Set author
        '''
        self.logger.debug(sys._getframe().f_code.co_name)    
        self.author = kwargs.get('name')
        self.author_icon = kwargs.get('icon')
        self.author_url = kwargs.get('url')
    
    def set_title(self, **kwargs):
        '''
        Set title
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        self.title = kwargs.get('title')
        self.title_url = kwargs.get('url')
    
    def set_thumbnail(self, url):
        '''
        Set thumbnail
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        self.thumbnail = url
    
    def set_image(self, url):
        '''
        Set image
        '''
        self.logger.debug(sys._getframe().f_code.co_name)   
        self.image = url
    
    def set_footer(self,**kwargs):
        '''
        Set footer
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        self.footer = kwargs.get('text')
        self.footer_icon = kwargs.get('icon')
        ts = kwargs.get('ts')
        if ts == True:
            self.ts = str(datetime.datetime.utcfromtimestamp(time.time()))
        else:
            self.ts = str(datetime.datetime.utcfromtimestamp(ts))
    
    def del_field(self, index):
        '''
        Delete field
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        self.fields.pop(index)
    
    @property
    def json(self,*arg):
        '''
        Formats the data into a payload
        '''
        self.logger.debug(sys._getframe().f_code.co_name)  
        data = {}
        data["embeds"] = []
        embed = defaultdict(dict)
        if self.msg: data["content"] = self.msg
        if self.author: embed["author"]["name"] = self.author
        if self.author_icon: embed["author"]["icon_url"] = self.author_icon
        if self.author_url: embed["author"]["url"] = self.author_url
        if self.color: embed["color"] = self.color 
        if self.desc: embed["description"] = self.desc 
        if self.title: embed["title"] = self.title 
        if self.title_url: embed["url"] = self.title_url 
        if self.image: embed["image"]['url'] = self.image
        if self.thumbnail: embed["thumbnail"]['url'] = self.thumbnail
        if self.footer: embed["footer"]['text'] = self.footer
        if self.footer_icon: embed['footer']['icon_url'] = self.footer_icon
        if self.ts: embed["timestamp"] = self.ts 
        if self.fields:
            embed["fields"] = []
            for field in self.fields:
                f = {}
                f["name"] = field['name']
                f["value"] = field['value']
                f["inline"] = field['inline'] 
                embed["fields"].append(f)
        data["embeds"].append(dict(embed))
        empty = all(not d for d in data["embeds"])
        if empty and 'content' not in data:
            print('You cant post an empty payload.')
        if empty: data['embeds'] = []
        return json.dumps(data, indent=4)
    
    def post(self):
        """
        Send the JSON formated object to the specified `self.url`.
        """
        self.logger.debug(sys._getframe().f_code.co_name)  
        headers = {'Content-Type': 'application/json'}
        result = requests.post(self.url, data=self.json, headers=headers)
        if result.status_code == 400:
            self.logger.err("Post Failed, Error 400")
        else:
            self.logger.info("Payload delivered successfuly - Code : "+str(result.status_code))

class Simplehook:
    def __init__(self, conf):
        """
        Initialise a Simplehook Webhook
        """
        self.logger = logging.getLogger('discord_hook.Simplehook')
        self.logger.debug('Init a Simplehook object')
        self.conf = conf
    
    def sendMessage(self):
        """
        Send Message
        """
        self.logger.debug(sys._getframe().f_code.co_name)
        embed = Webhook(self.conf['webhook_url'], color = self.conf['color'])
        embed.set_author(name = self.conf['message']['author']['name'], icon = self.conf['message']['author']['icon'])
        embed.set_desc(self.conf['message']['desc_text'])
        for field in self.conf['message']['fields']:
            embed.add_field(name = field['name'], value = field['value'])
        embed.set_thumbnail(self.conf['message']['thumbnail'])
        embed.set_footer(text = self.conf['message']['footer']['text'], icon = self.conf['message']['footer']['icon'], ts = True)
        embed.post()
        self.logger.info('Message send!')