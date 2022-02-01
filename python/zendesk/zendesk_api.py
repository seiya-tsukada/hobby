#! /usr/bin/env python
# coding: utf-8

import pandas as pd
import re
import subprocess

def output_log(id, res):
    log_file = "zendesk_post.log"
    log_message = "{0}: {1}\r\n".format(id, res.stdout)

    with open(log_file, mode='a') as f:
        f.write(log_message)

    return

def shave_2_html_tag(contents):
    ret = ""

    reg_obj = re.compile(r"<[^>]*?>")
    ret = reg_obj.sub("", contents)
    
    return ret

def post_2_zendesk(title, contents, category, locale):
    
    domain = ""
    url = domain + "/api/v2/help_center/{0}/sections/{1}/articles.json".format(locale, category)
    mail = ""
    user_name = mail + "/" + "token"
    password = ""
    token = "{0}:{1}".format(user_name, password)
    headers = "Content-Type: application/json"

    payload = '''\
    {{
    "article": {{
        "title": "{title}",
        "body": "{contents}",
        "locale": "{locale}",
        "user_segment_id": null,
        "permission_group_id": 4407131572367
    }},
    "notify_subscribers": false
    }}
    '''.format(title=title, contents=contents, locale=locale, category=category)

    cmd = 'curl -X POST {0} -u {1} -H "{2}" -d \'{3}\''.format(url, token, headers, payload)

    print(cmd)

    res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(res)

    return res

excel_file_name = ""
excel_sheet_name = ""

df = pd.read_excel(excel_file_name, sheet_name = excel_sheet_name)

cnt = 0
for row in df.values:

    id = row[0]
    title = row[1]
    category = row[2]
    locale = row[3]
    contents_with_tag = row[4]
    status = row[5]
    contents = ""

    contents = shave_2_html_tag(contents_with_tag)
    res = post_2_zendesk(title, contents, category, locale)

    output_log(id, res)

    cnt = cnt+1
    
    if cnt >= 40:
        break

print("end")