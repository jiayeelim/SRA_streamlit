import streamlit as st
import pymongo

# Set page configurations
st.set_page_config(page_title="Student Registration Form", page_icon=":mortar_board:")

#Connect to MongoDB
client = pymongo.MongoClient("mongodb+srv://jiayee:utm12345@cluster0.bp5pdg7.mongodb.net/?retryWrites=true&w=majority")
db = client.SRA

# Save to mergeStudRegAndCourses
def save_to_mergeStudRegAndCourses(output):
    db.mergeStudRegAndCourses.insert_one(output)
    
# Define the function to display the registration form
def registration_form():
    st.title("Student Registration Form")
    st.subheader("Enter details below")

    year_list = ['2013','2014']
    semester = ['2013B', '2013J', '2014B', '2014J']

    with st.form("StudRegAndCourseForm", clear_on_submit=True):
        studentID = st.number_input("Enter student ID")
        code_presentation = st.selectbox('Select semester', semester)
        year = st.selectbox('Select year', year_list)
        withdrawnstatus = st.radio('Select a withdrawn status', ['0', '1'])
        button = st.form_submit_button("Submit")

        if button:
            st.write(studentID)
            if withdrawnstatus:
                st.write(withdrawnstatus)
            if year:
                st.write(year)
            if code_presentation:
                st.write(code_presentation)
        
    # Generate output
    output = {
        "Year" : int(year),
        "id_student" : int(studentID),
        "code_presentation" : code_presentation,
        "WithdrawnStatus" : bool(withdrawnstatus)
     }
        
    # Save output to MongoDB
    save_to_mergeStudRegAndCourses(output)
            

# Save to mergeAssessment
def save_to_mergeAssessment(output):
    db.mergeAssessment.insert_one(output)
    
# Define the function to display the Assessment form
def assessment():
    st.title("Assessment Form")
    st.subheader("Enter details below")

    year_list = ['2013','2014']
    semester = ['2013B', '2013J', '2014B', '2014J']
    code_module = ['AAA','BBB','CCC','DDD','EEE','FFF','GGG']

    with st.form("StudRegAndCourseForm", clear_on_submit=True):
        assessmentID = st.number_input("Enter assessment ID")
        studentID = st.number_input("Enter student ID")
        code_presentation = st.selectbox('Select semester', semester)
        course = st.selectbox('Select code module', code_module)
        year = st.selectbox('Select year', year_list)
        late_submit = st.radio('Select late submission status', ['0', '1'])
        result = st.radio('Select result', ['Pass', 'Fail'])
        button = st.form_submit_button("Submit")

        if button:
            st.write(studentID)
            if code_presentation:
                st.write(code_presentation)
            if course:
                st.write(course)
            if year:
                st.write(year)
            if late_submit:
                st.write(late_submit)
            if result:
                st.write(result)
                
    # Generate output
    output = {
        "id_assessment" : int(assessmentID),
        "code_presentation" : code_presentation,
        "id_student" : int(studentID),
        "Result" : result,
        "code_module" : course,
        "Late_submission" : bool(late_submit),
        "Year" : int(year)
    }
        
    # Save output to MongoDB
    save_to_mergeAssessment(output)

# Save to mergeVle
def save_to_mergeVle(output):
    db.mergeVle.insert_one(output)
    
# Define the function to display the Vle page
def vle():
    st.title("Virtual Learning Environment(VLE) Form")
    st.subheader("Enter details below")

    activity = ['dataplus', 'forumng', 'homepage', 'oucontent','resource','subpage','url','quiz','glossary','ouelluminate','oucollaborate','sharedsubpage']

    with st.form("StudRegAndCourseForm", clear_on_submit=True):
        activity_type = st.selectbox('Select semester', activity)
        sum_click = st.number_input("Enter sum of clicks")
        button = st.form_submit_button("Submit")

        if button:
            if activity_type:
                st.write(activity_type)
            st.write(sum_click)
        
    # Generate output
    output = {
        "activity_type" : activity_type,
        "sum_click" : int(sum_click)
    }
        
    # Save output to MongoDB
    save_to_mergeVle(output)

# Save to studentInfo
def save_to_studentInfo(output):
    db.studentInfo.insert_one(output)
    
def student_info():
    st.title("Student Info Form")
    st.subheader("Enter details below")
  
    year_list = ['2013','2014']
    semester = ['2013B', '2013J', '2014B', '2014J']
    ageband = ['0-35','35-55','55<=']
    numofattempts = ['1','2','3','4','5','6']
    education = ['HE Qualification','Lower Than A Level','A Level or Equivalent','Post Graduate Qualification','No Formal quals']
    code_module = ['AAA','BBB','CCC','DDD','EEE','FFF','GGG']
    region_ = ['East Aglian Region','East Midlands Region','Ireland','London Region','North Region','North Western Region','Scotland','South East Region','South Region','South West Region','Wales','West Midlands Region','Yorkshire Region']

    with st.form("StudentInfoForm", clear_on_submit=True):
        studentID = st.number_input("Enter student ID")
        gender = st.radio('Select gender', ['M', 'F'])
        age_band = st.selectbox('Select age band', ageband)
        highest_education = st.selectbox('Select highest education level', education)
        region = st.selectbox('Select region', region_)
        disability = st.radio('Select disability status', ['Y', 'N'])
        num_of_prev_attempts = st.selectbox('Select number of previous attempts', numofattempts)
        studied_credits = st.number_input("Enter studied credits")
        code_presentation = st.selectbox('Select semester', semester)
        course = st.selectbox('Select code module', code_module)
        sum_click = st.number_input("Enter sum of clicks")
        After_Clicks = st.number_input("Enter sum of after clicks")
        Before_Clicks = st.number_input("Enter sum of before clicks")
        final_result = st.radio('Select result', ['Distinction', 'Pass', 'Fail', 'Withdrawn'])
        submitbutton = st.form_submit_button("Submit")
        
        if submitbutton:
            st.write(studentID)
            if gender:
                st.write(gender)
            if age_band:
                st.write(age_band)
            if highest_education:
                st.write(highest_education)
            if region:
                st.write(region)
            if disability:
                st.write(disability)
            if num_of_prev_attempts:
                st.write(num_of_prev_attempts)
            if code_presentation:
                st.write(code_presentation)
            if course:
                st.write(course)
            if sum_click:
                st.write(sum_click)
            if After_Clicks:
                st.write(After_Clicks)
            if Before_Clicks:
                st.write(Before_Clicks)
            if final_result:
                st.write(final_result)
            if studied_credits:
                st.write(studied_credits)
        
    # Generate output
    output = {
        "gender" : gender,
        "id_student" : int(studentID),
        "code_presentation" : code_presentation,
        "num_of_prev_attempts" : int(num_of_prev_attempts),
        "highest_education" : highest_education,
        "disability" : disability,
        "age_band": age_band,
        "region" : region,
        "sum_click" : int(sum_click),
        "code_module" : course,
        "Before_Clicks" : int(Before_Clicks),
        "code_presentation" : code_presentation,
        "After_Clicks" : int(After_Clicks),
        "final_result" : final_result,
        "studied_credits" : int(studied_credits)
    }
        
    # Save output to MongoDB
    save_to_studentInfo(output)
        
        
#image url
image_url = "https://varteq.com/wp-content/uploads/2020/08/learning_analytics-680x360.png"

# Create the menu items and their respective pages
menu_items = {
    "Home": lambda: (st.header("Welcome to LMS system!"), st.write("Please select menu bar to proceed!"),st.image(image_url, width=800)),
    "Registration Form": registration_form,
    "Assessment Form": assessment,
    "VLE Form": vle,
    "Student Info Form": student_info
}


# Create the sidebar menu
menu_choice = st.sidebar.selectbox("Select a page", list(menu_items.keys()))

# Display the selected page
menu_items[menu_choice]()



