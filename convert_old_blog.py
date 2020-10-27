import os
import re
import sqlite3
import dateutil.parser

DIR = '/home/rrader/workspace/itkpi.pp.ua/content'
FORMAT = """---
title: "{title}"
date: {date}
draft: false
author: {author}
email: {author_mail}
---

<div class="image-wrapper">
    <img src="{image}" class="post-image full-img">
</div>

{content}

{tag_names}

"""

c = sqlite3.connect('/home/rrader/workspace/itkpi.pp.ua/journey.db')
cur = c.cursor()
for row in cur.execute(
    "select title, slug, markdown, published_at, published_by, image, id from posts where status = 'published'"
):
    path = DIR + '/{}.md'.format(row[1])
    if not os.path.exists(path):
        continue

    with open(path, 'w') as f:
        cont = row[2].decode()
        cont = re.sub(r'\n(\#+)', r'\n\1 ', cont)
        image = ''
        if row[5]:
            image = row[5].decode()
        if '[DRAFT]' in row[0].decode() or '[TODO]' in row[0].decode():
            continue

        cur2 = c.cursor()
        user = tuple(cur2.execute(
            "select name, email from users where id = {}".format(row[4])
        ))
        author = user[0][0].decode()
        author_mail = user[0][1].decode()

        cur3 = c.cursor()
        tags_ids = [
            str(row[0])
            for row in
            cur3.execute(
                "select tag_id from posts_tags where post_id = {}".format(row[6])
            )
        ]
        tag_names = [
            row[0].decode() for row in
            cur3.execute(
                "select name from tags where id in ({})".format(','.join(tags_ids))
            )
        ]
        if tag_names:
            tag_names = 'Tags: ' + ', '.join(tag_names)
        else:
            tag_names = ''

        f.write(FORMAT.format(title=row[0].decode().replace('"', '\\"'), date=dateutil.parser.parse(row[3]).isoformat(),
                              content=cont, image=image, author=author, author_mail=author_mail, tag_names=tag_names))
        print(path, 'saved')
