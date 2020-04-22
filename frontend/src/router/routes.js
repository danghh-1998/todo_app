import VueRouter from "vue-router";
import TodoList from "@/router/views/TodoList";

let routes = [
    {
        path: '/',
        name: 'todo-list',
        component: TodoList,
    }
];

const router = new VueRouter({mode: 'history', routes});

export default router