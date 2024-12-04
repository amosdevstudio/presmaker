# PresMaker
An AI powerpoint presentation maker.

> [!WARNING]
> This project has no real error handling and is not suited for a production environment (yet).
> Also, the presentations look very ugly and generic.
> That's why I recommend that you give away your data, your life and your dignity to daddy Microsoft and
> use the automatic "designer" interface on https://www.microsoft.com/microsoft-365/powerpoint just to make the
> powerpoint look like it wasn't stolen from your grandpa's Windows XP.

> [!NOTE]
> I like to use my own software to make notes or simple presentations for school.
> People usually expect plagiarised work to look beautiful and beyond your own ability,
> so this tool gives you fantastic opsec at that.

## Setup
Get a free API key at [groq.com](https://groq.com/).
Make a .env file:
```
GROQ_API_KEY=whisperwhisperwhisper...
```
Next, make a virtual environment:
```
python3 -m venv venv
source venv/bin/activate
```
Install the requirements:
```
pip3 install -r requirements.txt
```
Make the "presentations" directory:
```
mkdir presentations
```
Run the server!
```
python3 server.py
```

Now the server is running on port :8080.
