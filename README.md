
# Instagram Verified Subscription Demo

An independent educational demo with a verified-style
subscription interface.

## Requirements

- Python 3
- Kali Linux or another Linux distribution
- Ngrok (optional)

## Installation

```bash
git clone YOUR_REPOSITORY_URL
cd instagram-verified-demo
```

## Run locally

```bash
python3 server.py
```

Open:

http://localhost:8000

## Demo credentials

Username: demo_user

Demo access code: DEMO-1234

## Ngrok hosting

Open a second terminal:

```bash
ngrok http 8000
```

Open the HTTPS URL displayed by Ngrok.

## Logs

Demo login events are printed in the terminal.

Local logs are saved in:

logs/log.txt

Only the fixed demo password's binary representation
is recorded. Visitor-entered passwords are not logged.

## Disclaimer

This project is an independent educational demo,
not affiliated with Instagram or Meta.
Never enter real account credentials.


cd instagram-verified-demo

mkdir -p logs
touch logs/.gitkeep

python3 server.py
