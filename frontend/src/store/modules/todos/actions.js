import api from "@/api";

export default {
    createNewTodo: (context, newTodo) => {
        return api.post('todos/create', {content: newTodo})
            .then((res) => {
                context.commit('createNewTodo', res.data.todo);
            });
    },
    listTodos: context => {
        api.defaults.headers.common.Authorization = localStorage.getItem('token');
        return api.get('todos').then(async res => {
            let todos = res.data.todos;
            context.commit('listTodos', todos);
        });
    },
    filterAll: context => {
        context.commit('filterAll')
    },
    filterActive: context => {
        context.commit('filterActive')
    },
    filterComplete: context => {
        context.commit('filterComplete')
    },
    deleteTodo: (context, todo) => {
        return api.delete(`todos/${todo.id}/delete`)
            .then(() => {
                context.commit('deleteTodo', todo)
            });
    },
    updateTodo: (context, todo) => {
        return api.put(`todos/${todo.id}/update`, {
            'content': todo.content,
            'is_complete': todo.isComplete
        }).then(() => {
        });
    },
    deleteCompleted: context => {
        return api.delete('todos/delete_completed')
            .then((res) => {
                context.commit('deleteCompleted', res.data.todos)
            })
    }
}