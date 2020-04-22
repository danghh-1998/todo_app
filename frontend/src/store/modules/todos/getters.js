export default {
    filter: state => state.filter,
    todos: state => state.todos,
    itemLeft: state => state.todos.filter(todo => {
        return !todo.isComplete
    }).length,
    filteredTodos: state => {
        switch (state.filter) {
            case "all":
                return state.todos;
            case "active":
                return state.todos.filter(todo => {
                    return !todo.isComplete
                });
            case "complete":
                return state.todos.filter(todo => {
                    return todo.isComplete
                });
        }
    }
};