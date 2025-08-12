from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Sample job data
jobs = [
    {
        "id": 1,
        "title": "Senior Software Engineer",
        "company": "TechCorp Solutions",
        "location": "Remote",
        "salary": "$120,000 - $150,000",
        "type": "Full-time",
        "posted": "2 days ago",
        "description": "We're looking for a senior software engineer to join our team...",
        "requirements": ["5+ years experience", "Python/JavaScript", "Cloud platforms"],
        "logo": "🏢"
    },
    {
        "id": 2,
        "title": "Product Manager",
        "company": "InnovateTech",
        "location": "New York, NY",
        "salary": "$100,000 - $130,000",
        "type": "Full-time",
        "posted": "1 day ago",
        "description": "Join our product team to drive innovation...",
        "requirements": ["3+ years PM experience", "Agile methodology", "Data analysis"],
        "logo": "🚀"
    },
    {
        "id": 3,
        "title": "UX/UI Designer",
        "company": "DesignStudio Pro",
        "location": "San Francisco, CA",
        "salary": "$80,000 - $110,000",
        "type": "Full-time",
        "posted": "3 days ago",
        "description": "Create beautiful and intuitive user experiences...",
        "requirements": ["Portfolio required", "Figma/Sketch", "User research"],
        "logo": "🎨"
    },
    {
        "id": 4,
        "title": "Data Scientist",
        "company": "DataFlow Analytics",
        "location": "Boston, MA",
        "salary": "$90,000 - $120,000",
        "type": "Full-time",
        "posted": "5 days ago",
        "description": "Analyze complex data to drive business insights...",
        "requirements": ["Python/R", "Machine Learning", "Statistics"],
        "logo": "📊"
    },
    {
        "id": 5,
        "title": "Frontend Developer",
        "company": "WebCraft Inc",
        "location": "Austin, TX",
        "salary": "$70,000 - $95,000",
        "type": "Full-time",
        "posted": "1 week ago",
        "description": "Build amazing web applications with modern technologies...",
        "requirements": ["React/Vue.js", "TypeScript", "Responsive design"],
        "logo": "💻"
    },
    {
        "id": 6,
        "title": "Marketing Specialist",
        "company": "GrowthHub",
        "location": "Chicago, IL",
        "salary": "$55,000 - $75,000",
        "type": "Full-time",
        "posted": "4 days ago",
        "description": "Drive marketing campaigns and brand awareness...",
        "requirements": ["Digital marketing", "Social media", "Content creation"],
        "logo": "📈"
    }
]

# Sample ads data
ads = [
    {
        "id": 1,
        "title": "Boost Your Career with TechSkills Pro",
        "description": "Learn in-demand programming skills",
        "image": "📚",
        "link": "#",
        "type": "education"
    },
    {
        "id": 2,
        "title": "Resume Builder Pro",
        "description": "Create professional resumes in minutes",
        "image": "📄",
        "link": "#",
        "type": "tools"
    },
    {
        "id": 3,
        "title": "Career Coaching Services",
        "description": "Get personalized career guidance",
        "image": "👥",
        "link": "#",
        "type": "services"
    },
    {
        "id": 4,
        "title": "Google Workspace for Business",
        "description": "Collaborate efficiently with Google tools",
        "image": "📊",
        "link": "https://workspace.google.com",
        "type": "tools"
    },
    {
        "id": 5,
        "title": "Google Cloud Platform",
        "description": "Build and scale your applications",
        "image": "☁️",
        "link": "https://cloud.google.com",
        "type": "services"
    }
]

@app.route('/')
def index():
    return render_template('index.html', jobs=jobs, ads=ads)

@app.route('/job/<int:job_id>')
def job_detail(job_id):
    job = next((job for job in jobs if job['id'] == job_id), None)
    if job:
        return render_template('job_detail.html', job=job, ads=ads)
    return "Job not found", 404

@app.route('/api/jobs')
def api_jobs():
    search = request.args.get('search', '')
    location = request.args.get('location', '')
    job_type = request.args.get('type', '')
    
    filtered_jobs = jobs
    
    if search:
        filtered_jobs = [job for job in filtered_jobs if 
                        search.lower() in job['title'].lower() or 
                        search.lower() in job['company'].lower()]
    
    if location:
        filtered_jobs = [job for job in filtered_jobs if 
                        location.lower() in job['location'].lower()]
    
    if job_type:
        filtered_jobs = [job for job in filtered_jobs if 
                        job_type.lower() == job['type'].lower()]
    
    return jsonify(filtered_jobs)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
