import VueRouter from "vue-router";
import TodoList from "@/router/views/TodoList";
import SignIn from "@/router/views/SignIn";
import SignUp from "@/router/views/SignUp";
import VerifyEmail from "@/router/views/VerifyEmail";


let routes = [
    {
        path: '/',
        name: 'todo-list',
        component: TodoList,
    },
    {
        path: '/signin',
        name: 'signin',
        component: SignIn
    },
    {
        path: '/signup',
        name: 'signup',
        component: SignUp
    },
    {
        path: '/verify-email',
        name: 'verifyEmail',
        component: VerifyEmail
    }
];

const router = new VueRouter({mode: 'history', routes});
router.beforeEach((to, from, next) => {
    const publicPages = ['/signin', '/signup', '/verify-email'];
    let token = localStorage.getItem('token');
    const authRequirePages = !publicPages.includes(to.path);
    if (authRequirePages && !token) {
        return next('/signin');
    } else if (token && !authRequirePages && to.path !== '/') {
        return next('/');
    }
    return next();
});

export default router