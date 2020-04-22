<template>
    <div>
        <b-input size="is-large" placeholder="What needs to be done?" :class="{newTodo: true}"
                 @keyup.native.enter="handleNewTodo" v-model="newTodo"></b-input>
    </div>
</template>

<script>
    export default {
        name: "TodoHeader",
        data: function () {
            return {
                newTodo: ''
            }
        },
        methods: {
            handleNewTodo: function () {
                this.$store.dispatch('todos/createNewTodo', this.newTodo);
                this.newTodo = ''
            }
        }
    }
</script>

<style scoped>
    .newTodo {
        width: 800px;
        height: 60px;
    }
</style>