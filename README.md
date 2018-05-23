# Tamil TTS Web

## Installation

<pre>
git clone https://github.com/tshrinivasan/tamil-tts-install.git
cd tamil-tts-install
wget https://raw.githubusercontent.com/mohan43u/tamil-tts-install/master/tamil-tts.sh

chmod +x tamil-tts.sh
./tamil-tts.sh
</pre>

Thanks to https://github.com/mohan43u/tamil-tts-install for making the installation procedure simple.
Thanks to Shrinivasan for putting this together.

## Setting up Flask Application

#### Prerequisites

<pre>
pip install requests
</pre>

<pre>
python flask_app.py
</pre>

The Django Application communicates with the Flask which executes the tamil-tts.sh which does the TTS audio file.

## Django Application

#### Prerequisites

<pre>
pip install requests
</pre>

I've added the views.py and urls.py here. Use it in your Django Application.

### Make sure to edit the allowed hosts in settings.py if you are running flask on a different server.
