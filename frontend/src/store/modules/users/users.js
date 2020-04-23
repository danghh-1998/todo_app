import actions from "@/store/modules/users/actions";
import getters from "@/store/modules/users/getters";
import mutations from "@/store/modules/users/mutations";
import state from "@/store/modules/users/state";

export default {
    namespaced: true,
    actions, getters, mutations, state
}