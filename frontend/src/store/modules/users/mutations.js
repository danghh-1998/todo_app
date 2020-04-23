export default {
    signin: (state, data) => {
        state.authenticated = true;
        localStorage.setItem('token', `Token ${data}`);
    }
}