<template>
    <div class="todo-list">
        <page-header></page-header>
        <todo-header></todo-header>
        <todo-body></todo-body>
        <todo-footer></todo-footer>
    </div>
</template>

<script>
    import TodoHeader from "@/components/todos/TodoHeader";
    import TodoFooter from "@/components/todos/TodoFooter";
    import TodoBody from "@/components/todos/TodoBody";
    import PageHeader from "@/components/todos/PageHeader";

    export default {
        name: "TodoList",
        components: {PageHeader, TodoBody, TodoFooter, TodoHeader},
        data: function () {
            return {
                todos: this.$store.getters['todos/filteredTodoList']
            };
        },
        methods: {},
        computed: {},
        mounted: function () {
            this.$store.dispatch('todos/listTodos');
        }
    }
</script>

<style scoped>
    .todo-list {
    }
</style>