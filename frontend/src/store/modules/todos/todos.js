import actions from "@/store/modules/todos/actions";
import getters from "@/store/modules/todos/getters";
import mutations from "@/store/modules/todos/mutations";
import state from "@/store/modules/todos/state";

export default {
    namespaced: true,
    state, getters, mutations, actions
}