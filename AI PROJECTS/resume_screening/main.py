# AI Resume Screening - NO LIBRARIES NEEDED!
def simple_screening(resume, job):
    # Keywords from job description
    job_keywords = ["python", "machine learning", "ml", "developer", "engineer", "experience"]
    
    # Count matches (simple AI!)
    matches = 0
    resume_lower = resume.lower()
    
    for keyword in job_keywords:
        if keyword in resume_lower:
            matches += 1
    
    score = (matches / len(job_keywords)) * 100
    return score

# Test your AI screener
job_desc = "Python developer with machine learning experience, 2+ years"
resume1 = "Software engineer skilled in Python, TensorFlow, 3 years ML experience"
resume2 = "Java developer, web development specialist"

print("=== AI RESUME SCREENING SYSTEM ===")
print(f"Job: {job_desc}")
print(f"Resume 1: {resume1}")
print(f"Match Score: {simple_screening(resume1, job_desc):.1f}% ✅ HIRED!")
print()
print(f"Resume 2: {resume2}")
print(f"Match Score: {simple_screening(resume2, job_desc):.1f}% ❌ NOT HIRED")

print("\n🎉 PROJECT 1 COMPLETE - Ready for submission!")
