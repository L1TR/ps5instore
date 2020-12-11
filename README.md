# ps5instore
Build: docker build -t ps5instore .
Save to the file: docker save ps5instore > ps5instore.tar

<h2>Setup</h2>

All configuration variables are stored in the src/common/config.py
1. (required) <b>Telegram</b> bot to receive updates
- Check your chatid at url: https://api.telegram.org/bot1491939565:AAH7Regr6eomY1-rLC1qtCF2zRF5-rEN3Ac/getUpdates
- Change variable TELEGRAM_CHATID

<b>OR</b> if you don't see chat id

- Register your own bot: https://core.telegram.org/bots#6-botfather
- Change variables TELEGRAM_TOKEN and TELEGRAM_CHATID

2. (optional) <b>BestBuy</b>
- Register at https://developer.bestbuy.com/
- Update BESTBUY_DEVKEY

3. (optional) You can select <b>stores you want to check</b> by changing list STORES_TO_CHECK

4. (optional) DEFAULT_RETURN_ON_FAULT - if True, script will return "In Store" state <b>in case of any fail</b>

<h3><i>Issues</i></h3>
1. Walmart links do not return values anymore
2. Amazon blocks from checking its inventory without using its API
3. __debug__ dosen't return False on Synology
