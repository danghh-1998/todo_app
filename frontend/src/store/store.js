import Vue from 'vue'
import Vuex from 'vuex'
import todos from "@/store/modules/todos/todos";
import users from "@/store/modules/users/users";

Vue.use(Vuex);

export const store = new Vuex.Store({
    modules: {
        todos, users
    }
});