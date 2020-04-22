<template>
    <div>
        <div v-for="todo in todos" v-bind:key="todo.id">
            <todo-item v-bind:todo="todo"></todo-item>
        </div>
    </div>
</template>

<script>
    import TodoItem from "@/components/todos/TodoItem";

    export default {
        name: "TodoBody",
        components: {TodoItem},
        data: function () {
            return {}
        },
        computed: {
            todos: function () {
                return this.$store.getters['todos/filteredTodos']
            }
        }
    }
</script>

<style scoped>

</style>