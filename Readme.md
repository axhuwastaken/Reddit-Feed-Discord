# Reddit feed discord
### Get [reddit](http://reddit.com) feed directly into your discord server's!

<br>

## Simple and light weight
Instead of using discord bot for reddit feed, i choose webhooks it is lightweight and requires less resource to run can host easily :)

<br>

## Key features
* `Send reddit' new posts to discord within 10-20s.`
* `NSFW Filter: (helps you to stay away from unwanted stuff)`
* `Local DB for Caching (you don't have to setup)`
<br><br>
## Now let's see how to setup 🚀
1. first let's setup our `config.json`

file will look like this
```json
{
    "webhook-urls": "your webhook url here", //replace the text with your webhook url
    "subreddits": "india", //the subreddits you want to subscribe, for multiple subreddits use: meme+minecraft

    "options": {
        "allow_nsfw": false, //either you want to see nsfw post or not,set it true or false
        "send_embeds": false, // true or false
        "embed_color": "ff5700" //color hex
    },

    "extra": { // optional
        "webhook_name": "Reddit feed", // name of webhook
        "avatar_url": "https://www.designyourway.net/blog/wp-content/uploads/2021/01/reddit-fonts.jpeg" 
    }
}
```

make sure you entered correct information in `config.json`

done?

2. now use this command to install the required libs
```
pip install -r requirements.txt
```
3. final step
```
python main.py
```
Done!

one more thing until you don't know what you are doing don't make any changes in `db.json`
<br><br>

## Some word
**Contributors are heartly welcomed**💓

even tho this is small project but things can get better. feel free to report any bug. 