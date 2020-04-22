<template>
    <div class="box">
        <b-checkbox v-model="todo.isComplete" size="is-large" @change.native="updateTodo">
            <span :class="{complete: todo.isComplete}">{{todo.content}}</span>
        </b-checkbox>
        <span class="closable">
            <button @click="deleteTodo">×</button>
        </span>
    </div>
</template>

<script>
    export default {
        name: "TodoItem",
        props: ['todo'],
        data: function () {
            return {}
        },
        methods: {
            updateTodo: function(){
                this.$store.dispatch('updateTodo', this.$props.todo)
            },
            deleteTodo: function () {
                this.$store.dispatch('deleteTodo', this.$props.todo)
            }
        }
    }
</script>

<style scoped>
    .closable button {
        background-color: white;
        border: none;
        outline: none;
        font-size: 24px;
        color: #666;
        cursor: pointer;
        position: absolute;
        top: 20px;
        right: 20px;
        display: none;
    }

    .complete {
        text-decoration: line-through;
        color: #AAAAAA;
    }

    .box:hover button {
        color: #af5b5e;
        display: block;
    }

    .disable {
        display: none;
    }

    .box {
        height: 60px;
        width: 800px;
        position: relative;
    }


    .closable::-moz-focus-inner {
        border: none;
    }

</style>