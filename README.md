## File Sterm Bot

**• Superfast⚡️ Download and Stream Links.**

**• No ads In Generated Links.**

**• Superfast Interface.**

**• Along With The Links You Also Get File Information Like Name,Size ,etc.**

**• Updates Channel Support.**

**• Mongodb Database Support for Broadcasting.**
    
## • About This Bot :

### Deploy To Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy/)
  
### Deploy To Railway
  
[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2FCode-X-Mania%2Ffilestreambot&envs=API_HASH%2CAPI_ID%2CFQDN%2CDATABASE_URL%2CBOT_TOKEN%2CHAS_SSL%2CNO_PORT%2COWNER_ID%2CPORT%2COWNER_USERNAME%2CSESSION_NAME%2CUPDATES_CHANNEL%2CBIN_CHANNEL&API_HASHDesc=Get+it+from+my.telegram.org&API_IDDesc=Get+it+from+my.telegram.org&FQDNDesc=Your+railway+app+URL&DATABASE_URLDesc=Get+it+from+mongodb.com&BOT_TOKENDesc=Get+it+from+%40botfather&HAS_SSLDesc=Don%27t+touch+this&NO_PORTDesc=keep+default+value.&OWNER_IDDesc=Your+telegram+id+&PORTDesc=Default+is+8080&OWNER_USERNAMEDesc=Your+telegram+username+without+%40&SESSION_NAMEDesc=Keep+default+or+enter+your+name&UPDATES_CHANNELDesc=channel+username+without+%40++else+None&BIN_CHANNELDesc=Private+channels+username&FQDNDefault=EDIT+AFTER+DEPLOYING+THE+BOT+LEAVE+IT+AS+IT+IS+RIGHT+NOW&BOT_TOKENDefault=also+add+bot+to+bin+channel+and+updates+channel+if+any&HAS_SSLDefault=True&NO_PORTDefault=False&OWNER_IDDefault=+get+it+from+%40username_to_id_bot&PORTDefault=8080&OWNER_USERNAMEDefault=adarsh_goel&SESSION_NAMEDefault=I_love_opensource&UPDATES_CHANNELDefault=None&BIN_CHANNELDefault=also+add+bot+to+it&referralCode=ADARSH)
  
 <p><b>Available commands and features:</b>
 
<p>
 
🐬USER COMMANDS<p>
`/start - To start using me` <br>
`/help  -  To know how to use me`

🐬ADMIN COMMANDS<p>
`/status  - to know how many users are using the bot` <br>
`/broadcast - To send message to all the users using the bot`


  
  <b>Host it on VPS Locally :</b></summary>


```py
git clone https://github.com/code-x-mania/FileStreamBot
cd FileStreamBot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
python3 -m Code_X_Mania
```

and to stop the whole bot,
 do <kbd>CTRL</kbd>+<kbd>C</kbd>

Setting up things

If you're on Heroku / Railway, just add these in the Environmental Variables
or if you're Locally hosting, create a file named `.env` in the root directory and add all the variables there.
An example of `.env` file:

```py
DATABASE_URL=  Get this from mongodb.com
PORT=8080
API_ID= Get from my.telegram.org
NO_PORT=False
BOT_TOKEN= Get from botfather
OWNER_ID= your owner id 
API_HASH= Get from my.telegram.org
UPDATES_CHANNEL= Enter Force sub channel username without @ if any  else set value to None
BIN_CHANNEL=-100
SESSION_NAME=Codexmania
HAS_SSL=True
FQDN= Enter Custom domain if any or server ip
```
 <b>Vars and Details :</b>
`API_ID` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`API_HASH` : Goto [my.telegram.org](https://my.telegram.org) to obtain this.

`BOT_TOKEN` : Get the bot token from [@BotFather](https://telegram.dog/BotFather)

`BIN_CHANNEL` : Create a new channel (private/public), add [@missrose_bot](https://telegram.dog/MissRose_bot) as admin to the channel and type /id. Now copy paste the ID into this field.

`OWNER_ID` : Your Telegram User ID
  
`OWNER_USERNAME` : Your telegram username to be displayed in bot  . make one in you dont have.

`DATABASE_URL` : MongoDB URI for saving User IDs when they first Start the Bot. We will use that for Broadcasting to them. I will try to add more features related with Database. If you need help to get the URI you can ask in [Telegram](https://t.me/codexmania).

 Optional Vars

`UPDATES_CHANNEL` : Put a Public Channel Username, so every user have to Join that channel to use the bot. Must add bot to channel as Admin to work properly.

`BANNED_CHANNELS` : Put IDs of Banned Channels where bot will not work. You can add multiple IDs & separate with <kbd>Space</kbd>.

`SLEEP_THRESHOLD` : Set a sleep threshold for flood wait exceptions happening globally in this telegram bot instance, below which any request that raises a flood wait will be automatically invoked again after sleeping for the required amount of time. Flood wait exceptions requiring higher waiting times will be raised. Defaults to 60 seconds.

`WORKERS` : Number of maximum concurrent workers for handling incoming updates. Defaults to `3`

`PORT` : The port that you want your webapp to be listened to. Defaults to `8080`

`WEB_SERVER_BIND_ADDRESS` : Your server bind adress. Defauls to `0.0.0.0`

`NO_PORT` : If you don't want your port to be displayed. You should point your `PORT` to `80` (http) or `443` (https) for the links to work. Ignore this if you're on Heroku.

`FQDN` :  A Fully Qualified Domain Name if present. Defaults to `WEB_SERVER_BIND_ADDRESS` </details>

<b>How to Use :</b>

:warning: **Before using the  bot, don't forget to add the bot to the `BIN_CHANNEL` as an Admin**
 
`/start` : To check if the bot is alive or not.



To get an instant stream link, just forward any media to the bot and boom, its fast af.
  ![image](https://user-images.githubusercontent.com/88939380/137128326-059f9c53-b3d0-40f0-8484-b17709fbcc11.png)


### Channel Support
`Bot also Supports with Channels. Just add bot Channel as Admin. If any new file comes in Channel it will edit it with **Get Download Link** Button.` </details>

### 🔷 Credits : 

- [Adarsh Goel_(me)](https://t.me/codexmania)
- [EverythingSuckz](https://github.com/EverythingSuckz) 
- `Everyone In This Journey !`
- `Feel free to contribute 😀`

  
 
 
