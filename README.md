# GoldenBoy

A social network connecting young football players with the clubs looking for their next talent.

## Overview

GoldenBoy was built to solve a simple problem: young athletes often lack a direct channel to showcase their skills to clubs, while clubs spend significant effort scouting for talent in youth categories. The platform bridges that gap through two dedicated profile types:

- **Athletes** — young players who want to build a public profile, share their stats and information, and get discovered by clubs.
- **Clubs** — organizations looking to scout and recruit new talent for their youth (base) categories.

By giving each side a tailored profile experience, GoldenBoy makes it easier for promising players to get noticed and for clubs to find prospects more efficiently.

## Features

- Two distinct profile types (Athlete and Club), each with its own registration flow
- Athlete profiles for showcasing player information and attracting scouting interest
- Club profiles for browsing and identifying youth talent
- Web interface built with Django's templating system and Bootstrap for a responsive layout

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, Bootstrap

## Project Status

GoldenBoy is a prototype, originally developed as part of a university course. Core profile and navigation flows are implemented; some features are still in progress and the project is not yet production-ready.

## Getting Started

```bash
# clone the repository
git clone https://github.com/<your-username>/GoldenBoy.git
cd GoldenBoy

# create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt

# run migrations and start the server
python manage.py migrate
python manage.py runserver
```

## Author

Nicolas Soares — [LinkedIn](https://linkedin.com/in/nicolasf-soares) · [GitHub](https://github.com/nicolasfsoares)
