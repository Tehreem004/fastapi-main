import streamlit as st
import pandas as pd
import joblib
import datetime

# Must be the first Streamlit command
st.set_page_config(
    page_title="ELearning Performance Analytics System",
    layout="wide",
    menu_items={},
    initial_sidebar_state="expanded"
)

# Custom CSS combining both hide_st_style and custom_css
st.markdown("""
<style>
    /* Hide Streamlit Components */
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    div[data-testid="stToolbar"] {display: none !important;}
    
    /* Academic color scheme */
    :root {
        --primary-color: #3be1f7;
        --secondary-color: #E74C3C;
        --accent-color: #3498DB;
        --background-color: #ECF0F1;
        --success-color: #27AE60;
    }
    
    /* Main container styling */
    .main {
        background-color: var(--background-color);
        padding: 2rem;
    }
    
    /* University-style header */
    .university-header {
        color: var(--primary-color);
        font-size: 2.2rem;
        font-weight: 700;
        text-align: center;
        padding: 1rem;
        margin-bottom: 2rem;
        border-bottom: 3px double var(--primary-color);
        font-family: 'Times New Roman', serif;
    }
    
    /* Academic department section */
    .department-section {
        background-color: white;
        padding: 1.5rem;
        border-left: 4px solid var(--accent-color);
        margin-bottom: 2rem;
        border-radius: 0 5px 5px 0;
    }
    
    /* Form styling */
    .academic-form {
        background-color: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    
    /* Sidebar academic styling */
    .academic-sidebar {
        background-color: var(--primary-color);
        color: white;
        padding: 1rem;
        border-radius: 5px;
    }
    
    /* Academic button styling */
    .stButton>button {
        background-color: var(--accent-color);
        color: white;
        padding: 0.7rem 2rem;
        font-weight: 500;
        border: none;
        border-radius: 5px;
        width: 100%;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        background-color: #2980B9;
    }
    
    /* Results card */
    .results-card {
        background-color: white;
        padding: 2rem;
        border-radius: 8px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        margin-top: 2rem;
    }
    
    /* Academic info boxes */
    .info-box {
        background-color: #f8f9fa;
        border-left: 3px solid var(--accent-color);
        padding: 1rem;
        margin: 1rem 0;
    }
    
    /* Semester indicator */
    .semester-indicator {
        font-size: 0.9rem;
        color: var(--primary-color);
        text-align: right;
        font-style: italic;
    }
    
    /* Additional result styling */
    .prediction-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin: 20px 0;
        border-left: 4px solid var(--primary-color);
    }
    
    .big-prediction {
        font-size: 2.5rem;
        color: var(--primary-color);
        font-weight: bold;
        margin: 20px 0;
    }
    
    .recommendation-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        border-left: 3px solid var(--accent-color);
    }
    
    .probability-box {
        padding: 10px;
        margin: 5px 0;
        border-radius: 5px;
        background-color: #f8f9fa;
        border-left: 3px solid var(--primary-color);
    }
    
    .metric-card {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# [Previous CSS and imports remain the same as in the last response]

# Load the model
@st.cache_resource
def load_model():
    try:
        return joblib.load('student_performance_model.joblib')
    except FileNotFoundError:
        st.error("Model file not found. Please ensure the model is trained and saved correctly.")
        return None

# Model information
MODEL_INFO = {
    "model_type": "Random Forest Classifier",
    "best_parameters": {
        "max_depth": 10,
        "min_samples_leaf": 4,
        "min_samples_split": 2,
        "n_estimators": 300
    },
    "accuracy": 0.4333,
    "supported_classes": ["Distinction", "Fail", "Pass", "Withdrawn"]
}

def main():
    # Current semester indicator
    current_date = datetime.datetime.now()
    semester = "Spring" if current_date.month < 7 else "Fall"
    academic_year = current_date.year
    
    # University header
    st.markdown(f"""
        <div class="university-header">
            🎓 ELearning Performance Analytics System
            <div class="semester-indicator">
                {semester} Semester {academic_year}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Enhanced sidebar with academic styling
    with st.sidebar:
        try:
            st.image("download-removebg-preview.png", width=150)
        except:
            st.error("Logo image not found. Please check the image path.")
        
        st.markdown("""
        <div class="academic-sidebar">
            <h3>📊 Analytics System</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📚 System Information")
        st.markdown(f"**Model Architecture:** {MODEL_INFO['model_type']}")
        st.markdown(f"**System Accuracy:** {MODEL_INFO['accuracy']:.2%}")
        
        st.markdown("### 🎯 Performance Levels")
        for class_name in MODEL_INFO['supported_classes']:
            st.markdown(f"""
                <div class="performance-level {class_name.lower()}">
                    • {class_name}
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("### 📋 Quick Guide")
        st.markdown("""
        1. Enter student academic details
        2. Submit for performance analysis
        3. Review predictive analytics
        """)
        
        # Academic term information
        st.markdown("---")
        st.markdown("### 📅 Academic Calendar")
        st.markdown(f"**Current Term:** {semester} {academic_year}")
        st.markdown("**Assessment Period:** Active")

    # Main content area
    st.markdown('<div class="academic-form">', unsafe_allow_html=True)
    
    # Department section
    st.markdown("""
        <div class="department-section">
            <h3>📘 ELearning Prediction System</h3>
            <p>Complete the following academic profile for performance analysis.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Create two columns for form inputs
    col1, spacer, col2 = st.columns([1, 0.1, 1])
    
    with col1:
        st.markdown("#### 📝 Academic Information")
        
        code_module = st.selectbox(
            "Module Code",
            ["AAA - Advanced Analytics", "BBB - Business Studies", 
             "CCC - Computer Science", "DDD - Data Science",
             "EEE - Economics", "FFF - Finance", "GGG - Global Studies"]
        )
        
        code_presentation = st.selectbox(
            "Academic Term",
            ["2013J - January Start", "2014J - January Start", 
             "2013B - September Start", "2014B - September Start"]
        )
        
        gender = st.selectbox(
            "Student Gender",
            ["M - Male", "F - Female"]
        )
        
        region = st.selectbox(
            "Academic Region",
            ["East Anglian Region", "Scotland", "North Western Region", 
             "South East Region", "West Midlands Region", "Wales", 
             "North Region", "South West Region", "London Region", 
             "Yorkshire Region", "East Midlands Region", "Ireland"]
        )
        
        highest_education = st.selectbox(
            "Prior Education Level",
            ["A Level or Equivalent", "Lower Than A Level", 
             "HE Qualification", "Post Graduate Qualification"]
        )

    with col2:
        st.markdown("#### 📊 Additional Metrics")
        
        age_band = st.selectbox(
            "Age Category",
            ["0-35 (Traditional)", "35-55 (Mature)", "55<= (Senior)"]
        )
        
        num_of_prev_attempts = st.number_input(
            "Previous Module Attempts",
            min_value=0,
            max_value=10,
            value=0,
            help="Number of previous attempts at this module"
        )
        
        student_sum_click = st.number_input(
            "Learning Platform Engagement",
            min_value=0,
            value=0,
            help="Total interactions with learning materials"
        )
        
        disability = st.selectbox(
            "Special Educational Requirements",
            ["N - None Declared", "Y - Support Required"]
        )

    # Center the analysis button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_button = st.button("📊 Generate Performance Analysis")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Performance analysis section
    if analyze_button:
        model = load_model()
        
        if model is not None:
            try:
                # Clean input data
                input_data = {
                    "code_module": code_module.split(" - ")[0],
                    "code_presentation": code_presentation.split(" - ")[0],
                    "gender": gender.split(" - ")[0],
                    "region": region,
                    "highest_education": highest_education,
                    "age_band": age_band.split(" (")[0],
                    "num_of_prev_attempts": num_of_prev_attempts,
                    "Student_sum_click": student_sum_click,
                    "disability": disability.split(" - ")[0]
                }
                
                input_df = pd.DataFrame([input_data])
                prediction = model.predict(input_df)

                # Results container
                with st.container():
                    col1, col2, col3 = st.columns([1,3,1])
                    
                    with col2:
                        # Main prediction result
                        st.markdown("""
                            <div class="prediction-box">
                                <h2>🎓 Performance Prediction</h2>
                                <div class="big-prediction">
                                    {}
                                </div>
                            </div>
                        """.format(prediction[0]), unsafe_allow_html=True)
                        
                        # Probability distribution if available
                        if hasattr(model, 'predict_proba'):
                            st.markdown("### 📊 Probability Distribution")
                            probabilities = model.predict_proba(input_df)[0]
                            
                            for class_name, prob in zip(MODEL_INFO['supported_classes'], probabilities):
                                st.markdown(f"""
                                    <div class="probability-box">
                                        <div style="display: flex; justify-content: space-between; align-items: center;">
                                            <span style="font-weight: bold;">{class_name}</span>
                                            <span style="color: var(--primary-color); font-weight: bold;">{prob:.1%}</span>
                                        </div>
                                    </div>
                                """, unsafe_allow_html=True)
                                st.progress(float(prob))
                        
                        # Recommendations section with enhanced styling
                        st.markdown("### 📚 Recommended Actions")
                        
                        recommendations = [
                            ("🎯", "Schedule regular check-ins with academic advisor"),
                            ("📚", "Access additional learning resources through the platform"),
                            ("👥", "Join virtual study groups for collaborative learning"),
                            ("💡", "Utilize online tutorial sessions for complex topics")
                        ]
                        
                        for icon, rec in recommendations:
                            st.markdown(f"""
                                <div class="recommendation-box">
                                    <div style="display: flex; align-items: center;">
                                        <span style="font-size: 1.5rem; margin-right: 10px;">{icon}</span>
                                        <span>{rec}</span>
                                    </div>
                                </div>
                            """, unsafe_allow_html=True)
                        
                        # Student profile summary with enhanced styling
                        st.markdown("### 📋 Student Profile Summary")
                        metrics = [
                            ("📚 Module", code_module.split(" - ")[0]),
                            ("🗓️ Term", code_presentation.split(" - ")[0]),
                            ("🎓 Education", highest_education),
                            ("📊 Engagement", f"{student_sum_click} clicks")
                        ]
                        
                        cols = st.columns(2)
                        for i, (label, value) in enumerate(metrics):
                            with cols[i % 2]:
                                st.markdown(f"""
                                    <div class="metric-card">
                                        <div style="color: #666; font-size: 0.9rem;">{label}</div>
                                        <div style="font-size: 1.1rem; font-weight: bold; color: var(--primary-color);">{value}</div>
                                    </div>
                                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"⚠️ Analysis Error: {str(e)}")

if __name__ == "__main__":
    main()
