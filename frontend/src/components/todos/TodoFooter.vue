<template>
    <div class="box">
        <div class="footer-filter">
            <span>{{itemLeftText}}</span>
            <div class="filter">
                <b-button type="is-light" :class="{isActive: currentFilter === 'all'}" @click="filterAll"
                >All
                </b-button>
                <b-button type="is-light" :class="{isActive: currentFilter === 'active'}" @click="filterActive"
                >Active
                </b-button>
                <b-button type="is-light" :class="{isActive: currentFilter === 'complete'}" @click="filterComplete"
                >Completed
                </b-button>
            </div>
            <b-button type="is-light" class="clear-completed" @click="deleteCompleted">Clear completed</b-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "TodoFooter",
        data: function () {
            return {}
        },
        props: {},
        methods: {
            filterAll: function () {
                this.$store.dispatch('todos/filterAll')
            },
            filterActive: function () {
                this.$store.dispatch('todos/filterActive')
            },
            filterComplete: function () {
                this.$store.dispatch('todos/filterComplete')
            },
            deleteCompleted: function () {
                this.$store.dispatch('todos/deleteCompleted')
            }
        },
        computed: {
            currentFilter: function () {
                return this.$store.getters['todos/filter']
            },
            itemLeftText: function () {
                let itemLeft = this.$store.getters['todos/itemLeft'];
                if (itemLeft === 1) {
                    return [itemLeft, 'item left'].join(' ')
                } else {
                    return [itemLeft, 'items left'].join(' ')
                }
            }
        }
    }
</script>

<style scoped>
    .box {
        width: 800px;
        height: 60px;
    }

    .isActive {
        border: 1px solid #666666 !important;
    }

    .footer-filter {
        position: relative;
    }

    button {
        background-color: white !important;
        margin-left: 3px;
        margin-right: 3px;
    }

    .filter {
        position: absolute;
        left: 0;
        right: 0;
        top: -5px;
        bottom: 0;
        display: inline-block;
        width: max-content;
        margin: auto;
    }

    .clear-completed {
        position: absolute;
        right: -10px;
        bottom: -6px;
    }

    .clear-completed:hover {
        text-decoration: underline;
    }

    button::-moz-focus-inner {
        border: none;
    }
</style>