import api from "@/api";

export default {
    signin: (context, data) => {
        return api.post('auth/sign_in', data)
            .then((res) => {
                context.commit('signin', res.data.token);
            })
    },
    signup: (context, data) => {
        return api.post('auth/sign_up', data)
            .then((res) => {
                console.log(res);
            })
    },
    verifyEmail: (context, data) => {
        return api.put('users/verify_email', data)
            .then((res) => {
                console.log(res);
            })
    }
}