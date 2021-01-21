#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
import pandas as pd

conn = sqlite3.connect('sqlite/reddit-comments.sqlite')
sql = 'SELECT COUNT(id), subreddit FROM May2015 GROUP BY subreddit_id'
# read into pandas dataframe
df = pd.read_sql(sql, conn)
df.to_csv('csv/reddit-comment-count-by-subreddit.csv')