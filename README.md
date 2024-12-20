# DSA Quest 👑

Leetcode is hard, everyone can agree on that. However, if you ask anyone what made them "good" at Leetcode, they'll probably answer: 'Practice'.

But, let's face it. No one wants to practice Leetcode. But if you want to land that $100k coding job (*laughs in economic hardship😔*) you just have to.

That's why I have created a tool to help you practice questions in the worst way possible 😀, **Leetcode-style**

## Overview 👨‍🏫

This project is a Django web application that helps users enhance users data structure and algorithm (DSA) skills. Users can:

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

2. **Set Up a Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the Development Server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the Application**:
   - Open a browser and navigate to `http://127.0.0.1:8000`.

---

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
