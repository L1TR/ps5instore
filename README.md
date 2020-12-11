# ps5instore
Build: <code>docker build -t ps5instore .</code>

Save to the file: <code>docker save ps5instore > ps5instore.tar</code>

<h2>Setup</h2>

All configuration variables are stored in the src/common/config.py
1. (required) <b>Telegram</b> bot to receive updates
- Register your own bot: https://core.telegram.org/bots#6-botfather
- Go to the <code>https://api.telegram.org/bot{your_token}/getUpdates</code> to get chat id
- Change variables TELEGRAM_TOKEN and TELEGRAM_CHATID in config

2. (optional) <b>BestBuy</b>
- Register at https://developer.bestbuy.com/
- Update BESTBUY_DEVKEY

3. (optional) You can select <b>stores you want to check</b> by changing list STORES_TO_CHECK

4. (optional) DEFAULT_RETURN_ON_FAULT - if True, script will return "In Store" state <b>in case of any fail</b>

<h3><i>Issues</i></h3>

1. Walmart support requires a fix

2. Amazon blocks from checking its inventory without using its API

3. __debug__ dosen't return False on Synology
