import re

# Sample resume text
resume_text = """
Experienced Data Analyst with skills in Python, SQL, Excel, and Power BI.
Worked on dashboards, reporting, and data analysis.
"""

# Skills to search for
required_skills = ["python", "sql", "excel", "power bi"]

def extract_skills(text, skills):
    found_skills = []
    for skill in skills:
        if re.search(skill, text.lower()):
            found_skills.append(skill)
    return found_skills

matched_skills = extract_skills(resume_text, required_skills)

print("Matched Skills:", matched_skills)
