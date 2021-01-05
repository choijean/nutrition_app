<!-- omit in toc -->
# nutrition_app

Link to site: [Site](https://example.com)

This is a toy application that performs a search against the Nutritionix API to display the nutritional information about a specific food.

<!-- omit in toc -->
## Table of Contents 📖

- [Features ✨](#features-)
- [Technologies ⚙️](#technologies-️)
- [Getting Started 🛠](#getting-started-)
- [Deploy 🚀](#deploy-)
  - [Development 📝](#development-)
  - [Production 🖥](#production-)
- [Contributing 👥](#contributing-)
- [Authors & Acknowledgements ✍](#authors--acknowledgements-)
- [License 📄](#license-)
- [CHEAT SHEET](#cheat-sheet)
  - [Text](#text)
  - [Lists & Tables](#lists--tables)
  - [Code formatting](#code-formatting)
  - [Links](#links)
  - [Embedded Images](#embedded-images)
    - [Pure Markdown](#pure-markdown)
    - [HTML](#html)

## Features ✨

- Search a food item by name
- Display the basic nutrition information
- Dockerized application
- Run on [Google Cloud Platform](https://cloud.google.com/)

## Technologies ⚙️

- [Python3](https://www.python.org)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Jinja2](https://palletsprojects.com/p/jinja/)
- [Google Cloud Run](https://cloud.google.com/run)
- [Google Cloud Container Registry](https://cloud.google.com/container-registry)
- [Google Cloud Build](https://cloud.google.com/cloud-build)
- [Docker](https://hub.docker.com/)

## Getting Started 🛠

Clone the repository and navigate to the project's root directory.

```shell
git clone git@github.com:choijean/nutrition_app.git
cd nutrition_app
```

Create an account at [Nutritionix API](https://developer.nutritionix.com). You will need to keep note of your **Application ID** as well as your **Application Key**

Create a [Docker](https://hub.docker.com/) account.

## Deploy 🚀

### Development 📝

Because the Nutritionix API requires an **Application ID** as well as an **Application Key**, we will need to store them as environment variables before running the application locally.

```shell
export NIX_APP_ID=<YOUR_NUTRITIONIX_APP_ID>
export NIX_API_KEY=<YOUR_NUTRITIONIX_APP_KEY>
```

To run the application locally, run the following code:

```shell
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

Navigate to `http://0.0.0.0:5000/` on a browser.

### Production 🖥

We will use [Google Cloud Run](https://cloud.google.com/run) to deploy our application.

Start a new project at
[Google Cloud Platform](https://console.cloud.google.com/). This [document](https://cloud.google.com/resource-manager/docs/creating-managing-projects#console) explains how to create a new project. Alternatively, you can create projects in Cloud Shell.

```shell
gcloud projects create <YOUR_APP_NAME_HERE>
gcloud config set project <YOUR_APP_NAME_HERE>
```

Activate Cloud Shell, clone the repository and navigate to the project's root directory.

```shell
git clone git@github.com:choijean/nutrition_app.git
cd nutrition_app
```

## Contributing 👥

This is a toy application so I am not taking any contributions.

## Authors & Acknowledgements ✍

Written by [Jean Choi](https://www.github.com/choijean)

## License 📄

This code is licensed under [MIT](https://opensource.org/licenses/MIT)
<!-------------------------------------------------------------->

## CHEAT SHEET

### Text

This is *italic* text.

This is **bold** text.

This is ***bold and italic*** text.

This is ~~strike through~~ text.

This is a [link](example.com)

This is an email <jeanchoiii@gmail.com>

[emojis](https://unicode.org/emoji/charts/full-emoji-list.html) are valid! Press `Ctrl + Cmd + Space` to open emoji keyboard on MacOS.

> This is
>
> a block quote

---

### Lists & Tables

- [x] Banana
- [x] Apple
- [ ] Durian

1. First item
2. Second item
   1. Second item's child

- First item
- Second item
  - Second item's child

1. First item
   - I don't have an order!

- First item
  1. I have an order!

| Left | Center  | Right |
| :--- | :-----: | ----: |
| Hi   |  Hola   |  안녕 |
| Ciao | Bonjour | Aloha |

---

### Code formatting

in-line code: `print("This is code")`

syntax highlighted block code:

```json
{
  "note": "this is json specific code"
}
```

---

### Links

Section [link](https://google.com)

Relative path [link](path/to/file/readme.md)

---

### Embedded Images

#### Pure Markdown

From external resource:
![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

From relative path:
![relative image](images/pigeon.png)

#### HTML

From external resource:

- Advantage: can customize properties
- Disadvantage: Use of HTML is not ideal

<p align="center">
  <img src="https://octodex.github.com/images/yaktocat.png" title="Yaktocat"  width="40%" >
</p>
