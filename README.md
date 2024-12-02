# APICondidats
This project includes two modules:

* Candidate Module: Defines the necessary fields to identify a candidate.
* Recruiter Module: Defines the necessary fields to identify a recruiter.
# Details
Resumes uploaded by users are stored in a /resumes directory.
* This app allows you to:
     * Create, delete, and update a candidate.
     * Create, delete, and update a recruiter.
     * Access individual candidates or recruiters.
  
# Installation
Follow these steps to set up the project:

# Clone the repository
- git clone https://github.com/nina82004/apicondidats.git
- cd apicondidats

# Open the project in VS Code

  code .

# Install dependencies
pip install -r requirements.txt

# Navigate to the project folder
cd recruitement_platform

# Apply migrations and start the server
1-  python3 manage.py makemigrations

2-  python3 manage.py migrate

3-  python3 manage.py runserver

* You can now access the app at http://127.0.0.1:8000/.

