# barter-game

Text-based trading game

## Usage

To run this program use

	python main.py

You need the module TextBlob, a library for processing textual data, and the necessary NLTK corpora. You can easily install these - check out [TextBlob installation instructions.](https://textblob.readthedocs.io/en/dev/install.html)

## How it works

You are a traveler looking to make money by buying and selling items. As you travel through the market, you come across randomly generated traders.

### Buying

Each trader sells an item for a price, and your goal is to get that price as low as possible so you can buy it cheap. So, of course, you must say nice things to the trader, and get him in a better mood. Offer a price, and if he's happy enough it is more likely that he will accept it, even if it's completely unreasonable.

My troubles with Ondor:

	Ondor from Ondor's Garage is selling empty recycling boxes for $38

	"My name's Ondor," said Ondor. "Got any money?"

	respond: hello Ondor! I think empty recycling boxes are great! I'd like to buy it for $14

	Ondor disagreed. "$36, nothing more, nothing less."

	respond: Oh I don't think so! Would you be so kind to give it to me for $14?

	Ondor disagreed. "I will take $33."

	respond: Well how about $15?

	Ondor scoffed. "You think I'm dumb?"

	respond: I'm sorry Ondor! I did not mean to offend you! How about $17?

	Ondor scoffed. "I don't think so."

	respond: You are a great person, Ondor, and I think you are nice enough to let it go at $17

	Ondor scoffed. "You think I'm dumb?"

	respond: Now, now, Ondor, I am being so nice to you! so you must allow me at most $18?

	Ondor smiled. "I'll accept that"

	You got the price down to $18.0!

### Selling

After you talk to the trader about buying, and either tell him that you're leaving, buy his item, or get kicked out, you have the opportunity to open your "inventory console."

	"I'm Adon," said Adon. "Got any money?"
	
	respond: bye
	
	"You want nothing?", he said, "Good riddens! Leave at once!"
	
	Open inventory console? y/n y
	
	type '/help' for help >>>/help
	/sell <item> - sell an item
	/sellall - sell all items
	/inspect <item> - see basic item info
	/exit - exit inventory console
	/balance - show bank balance
	/inv - show inventory
	/inspectall - inspect all items

This inventory console allows you to look at all your stats by typing in commands, Minecraft-style!
	
	type '/help' for help >>>/balance
	Balance: $298171.59

Here, you can inspect your items and see their basic info, such as their name, description, how much you bought them for, and how much the trader will buy them for. 

	type '/help' for help >>>/inspect gold
	
	gold from the end of the rainbow
	a rainbow was monitored and tracked carefully (by lunatics) to locate this gold
	bought for $200.00, you can sell to Adon for $729.83

You can then sell your items to the trader, and BOOM, profit!

	type '/help' for help >>>/sell gold
	Sell gold from the end of the rainbow to Adon for $729.83? y/n y
	
	type '/help' for help >>>/balance
	Balance: $298901.42

When you're finished, just exit, and you will go find another trader. You might get lucky, and find someone who's selling a time machine or something.

	type '/help' for help >>>/exit

	You leave to find another trading stand.

## Contributing
Check and open issues to discuss any ideas about bugs or features

Fork the repository, make changes, and send pull requests

If you want to, you can add some items or dialog to the game. These are all located in the params.py file. You probably don't even have to know Python - just follow the pattern. I've provided comments to help you.

## Future Developments
In the future, I plan to add the following features:
* More items and dialog
* Better pluralization and capitalization of item and shop names
* More things to do, to make it more of a story
* Make traders more intelligent
