// components/Home.js
export default {
    template: `
      <div class="container mt-5">
        <h2>Welcome to the Project Management System</h2>
        <p>This application allows instructors to manage projects and students to submit their work. Please use the links below to log in or sign up.</p>
        <ul class="list-group">
          <li class="list-group-item"><router-link to="/instructor_login">Instructor Login</router-link></li>
          <li class="list-group-item"><router-link to="/student_login">Student Login</router-link></li>
          <li class="list-group-item"><router-link to="/instructor_signup">Instructor Signup</router-link></li>
          <li class="list-group-item"><router-link to="/student_signup">Student Signup</router-link></li>
        </ul>
      </div>
    `
  };