export default {
    createNewTodo: (state, newTodo) => {
        state.todos.push(newTodo)
    },
    listTodos: (state, todos) => {
        state.todos = todos
    },
    filterAll: state => {
        state.filter = 'all'
    },
    filterActive: state => {
        state.filter = 'active'
    },
    filterComplete: state => {
        state.filter = 'complete'
    },
    deleteTodo: (state, todo) => {
        let index = state.todos.indexOf(todo);
        if (index !== -1) {
            state.todos.splice(index, 1)
        }
    },
    deleteCompleted: (state, todos) => {
        state.todos = todos
    }
};