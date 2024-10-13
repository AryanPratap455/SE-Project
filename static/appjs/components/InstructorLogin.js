// components/InstructorLogin.js
export default {
  template: `
    <div class="container mt-5">
      <h2>Instructor Login</h2>
      <form @submit.prevent="login">
        <div class="form-group">
          <input type="text" v-model="username" class="form-control" placeholder="Username" required>
        </div>
        <div class="form-group">
          <input type="password" v-model="password" class="form-control" placeholder="Password" required>
        </div>
        <button type="submit" class="btn btn-primary">Login</button>
      </form>
    </div>
  `,
  data() {
    return {
      username: '',
      password: ''
    };
  },
  methods: {
    login() {
      fetch('/instructor_login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: this.username,
          password: this.password
        })
      })
      .then(response => response.json())
      .then(data => {
        if (data.access_token) {
          localStorage.setItem('token', data.access_token);
          alert('Login successful');
        } else {
          alert('Login failed');
        }
      });
    }
  }
};