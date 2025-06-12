#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from intern_gmail_agent.crew import InternGmailAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'resume_content': (
            "John Doe\n"
            "Email: johndoe@example.com | Phone: (123) 456-7890\n"
            "Education:\n"
            "- B.Sc. in Computer Science, University of Example, 2025 (expected)\n"
            "Skills:\n"
            "- Python, JavaScript, HTML, CSS\n"
            "- Experience with Flask, React, and Git\n"
            "- Strong problem-solving and teamwork abilities\n"
            "Experience:\n"
            "- Software Developer Intern, TechStart (Summer 2023)\n"
            "  • Built and maintained web application features using Python and JavaScript\n"
            "  • Collaborated with a team of 5 to deliver project milestones on time\n"
            "Projects:\n"
            "- Personal Portfolio Website (React, Flask)\n"
            "- Chatbot using Python and NLP libraries\n"
        ),
        'job_description_content': (
            "Software Developer Intern\n"
            "Company: Innovatech Solutions\n"
            "Responsibilities:\n"
            "- Assist in developing and maintaining web applications using Python and JavaScript.\n"
            "- Collaborate with cross-functional teams to design scalable solutions.\n"
            "- Write clean, efficient, and well-documented code.\n"
            "Requirements:\n"
            "- Pursuing a degree in Computer Science or related field.\n"
            "- Knowledge of Python, JavaScript, and web frameworks.\n"
            "- Familiarity with Git and Agile methodologies.\n"
            "- Strong problem-solving and communication skills.\n"
        )
    }
    
    try:
        InternGmailAgent().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

