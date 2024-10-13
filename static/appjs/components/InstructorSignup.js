// components/InstructorSignup.js
export default {
  template: `
    <div class="container mt-5">
      <h2>Instructor Signup</h2>
      <form @submit.prevent="signup">
        <div class="form-group">
          <input type="text" v-model="username" class="form-control" placeholder="Username" required>
        </div>
        <div class="form-group">
          <input type="email" v-model="email" class="form-control" placeholder="Email" required>
        </div>
        <div class="form-group">
          <input type="password" v-model="password" class="form-control" placeholder="Password" required>
        </div>
        <button type="submit" class="btn btn-primary">Signup</button>
      </form>
    </div>
  `,
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    signup() {
      fetch('/instructor_signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: this.username,
          email: this.email,
          password: this.password
        })
      })
      .then(response => response.json())
      .then(data => {
        if (data.access_token) {
          localStorage.setItem('token', data.access_token);
          alert('Signup successful');
        } else {
          alert('Signup failed');
        }
      });
    }
  }
};