import Home from './components/Home.js';

import InstructorLogin from './components/InstructorLogin.js';
import StudentLogin from './components/StudentLogin.js';
import InstructorSignup from './components/InstructorSignup.js';
import StudentSignup from './components/StudentSignup.js';

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
      },
  {
    path: '/instructor_login',
    name: 'InstructorLogin',
    component: InstructorLogin
  },
  {
    path: '/student_login',
    name: 'StudentLogin',
    component: StudentLogin
  },
  {
    path: '/instructor_signup',
    name: 'InstructorSignup',
    component: InstructorSignup
  },
  {
    path: '/student_signup',
    name: 'StudentSignup',
    component: StudentSignup
  }
];

const router = new VueRouter({
  mode: 'history',
  routes
});

export default router;