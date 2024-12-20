# DSA Quest 👑

Leetcode is hard, everyone can agree on that. However, if you ask anyone what made them "good" at Leetcode, they'll probably answer: 'Practice'.

But, let's face it. No one wants to practice Leetcode. But if you're going to land that $100k coding job (*laughs in economic hardship😔*) you have to.

That's why I have created a tool to help you practice questions in the worst way possible 😀, **Leetcode-style**

## Overview 👨‍🏫

This project is a Django web application that helps users enhance their data structure and algorithm (DSA) skills using uv (A Python package installer and resolver).

Some basic features are:

- Select a data structure to receive daily quests on.
- Add Leetcode questions either by adding the question directly or using a link
- Customize notification frequency and the number of questions generated per interval.
- Receive periodic updates and reminders directly on the platform.

---

## Features 🤖

- **User Authentication**: Log in to manage preferences and notifications.
- **Data Structure Selection**: Choose specific topics for question suggestions.
- **Leetcode Integration**: Add Leetcode questions as text or links to scrape and generate similar problems.
- **Customizable Notifications**: Set preferences for notification intervals and question quantities.
- **Periodic Updates**: Receive scheduled updates with new questions based on your selections.

---

## Setup and Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/benj1e/dsa-quest.git
   cd dsa-quest
   ```

2. **Set up Coding Environment**:
   Since I am using uv instead of pip, you should (will) too!

   ```bash
   pip install uv # You should probably install uv, it's really fast (trust me bro.)
   uv sync
   ```

   Once you run `uv sync` it will create a `.venv` folder and install all dependencies for you.

   So you should see an output like this:

   ```bash
   Using CPython 3.12.2 interpreter at: path\to\your\python\interpreter
   Creating virtual environment at: .venv

   # The packages that were installed (it's faster than pip btw)
   ```

3. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: .venv\Scripts\activate
   ```

4. **Install Dependencies**:
   **uv has already handled this...**
   Still unsure?

   You can list out the packages currently installed using this snippet:

   ```bash
   uv pip list    # Yes you can use pip commands in conjunction with uv
   ```

   or if you're better suited to a `requirements.txt` file, you can run

   ```bash
   uv pip freeze > requirements.txt
   ```

   Now that we're done setting up our coding environment, we should probably start using our application now.
   We will run our Django migrations.

5. **Run Migrations**:

   ```bash
   uv run manage.py makemigrations
   uv run manage.py migrate
   ```

   **or**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Development Server**:

   ```bash
   python manage.py runserver
   ```

   **or**

   ```bash
   uv run manage.py runserver
   ```

7. **Access the Application**:
   - Open a browser and navigate to `http://127.0.0.1:8000`.(Duh!)

---

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.
