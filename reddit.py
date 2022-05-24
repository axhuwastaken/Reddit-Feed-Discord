import json
import requests
import time
from discord_webhook import DiscordWebhook, DiscordEmbed

def reddit_scan():
    try:
        with open("db.json") as data_base: #reading database
            db = json.load(data_base)
    except FileNotFoundError:
        db = []

    with open("config.json") as config:
        a=json.load(config)
        
    webhook_url = a['webhook-urls']
    subreddits = a['subreddits']
    color = a['options']['embed_color']

    req = requests.get(f"https://www.reddit.com/r/{subreddits}/new/.json", headers={
        "Cache-Control": "no-cache",
        "Pragma": "no-cache",
        "User-Agent": "discord-feed-bot"})

    posts = req.json()['data']['children']

    for post in posts:
        if post['data']['name'] not in db:
            webhook = DiscordWebhook(url=webhook_url, username=a["extra"]["webhook_name"], avatar_url=a["extra"]["avatar_url"])
            permalink = f"https://www.reddit.com{post['data']['permalink']}"

            if a["options"]["send_embeds"] == True:
            # create an appropriate embed object
                if post['data']['thumbnail'] == 'self': # text post
                    embed = DiscordEmbed(title=post['data']['title'], url=permalink, description=post['data']['selftext'], color=color)
                    embed.set_footer(text=f"🔼 {post['data']['ups']}\n🔽 {post['data']['downs']}")
                # elif post['data']['url_overridden_by_dest']:
                #     embed = DiscordEmbed(title=post['data']['title'], url=permalink, color=color)
                #     embed.set_image(url=post['data']['url_overridden_by_dest'])
                #     embed.set_footer(text=f"🔼 {post['data']['ups']}\n🔽 {post['data']['downs']}")
                elif post['data']['is_video']: # video post
                    embed = DiscordEmbed(title=post['data']['title'], url=permalink, color=color)
                    embed.set_image(url=post['data']['thumbnail'])
                    embed.set_footer(text=f"🔼 {post['data']['ups']}\n🔽 {post['data']['downs']}")
                else: # image post
                    embed = DiscordEmbed(title=post['data']['title'], url=permalink, color=color)
                    embed.set_image(url=post['data']['url'])
                    embed.set_footer(text=f"🔼 {post['data']['ups']}\n🔽 {post['data']['downs']}")
                webhook.add_embed(embed)

            elif a["options"]["send_embeds"] == False:

                if post['data']['is_video']: # video post
                    webhook.set_content(post['data']['thumbnail'])
                else: # image post
                    webhook.set_content(post['data']['url'])
                    
            else:
                raise SyntaxError("You have entered invaild argument im config.json\nwrite: true or false in config.json/options/send_embeds!")
            
            if post["data"]["over_18"] == False:
                webhook.execute()
                time.sleep(3) 
            elif post["data"]["over_18"] == True and a["options"]["allow_nsfw"] == True:
                webhook.execute()
                time.sleep(3) 
            elif post["data"]["over_18"] == True and a["options"]["allow_nsfw"] == False:
                pass
            # webhook.execute()
            # time.sleep(3) 
            db.append(post['data']['name'])

    with open('db.json', 'w') as save_file:
        json.dump(db[-50:], save_file, indent=2)