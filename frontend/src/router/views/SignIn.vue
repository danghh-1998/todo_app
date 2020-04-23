<template>
    <div class="signin">
        <p class="form-title">Sign in to your account</p>
        <div class="signin-form">
            <b-field label="Email" label-position="on-border">
                <b-input type="email" v-model="email" maxlength="30"></b-input>
            </b-field>
            <b-field label="Password" label-position="on-border">
                <b-input type="password" v-model="password" password-reveal maxlength="30"></b-input>
            </b-field>
            <b-button type="is-primary" expanded @click="signin">Sign in</b-button>
            <div class="form-footer">
                <a href="">Forgot your password?</a>
                <router-link to="/signup">Create account</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SignIn",
        data: () => {
            return {
                email: '',
                password: ''
            }
        },
        methods: {
            signin: function (e) {
                e.preventDefault();
                this.$store.dispatch('users/signin', {
                    email: this.email,
                    password: this.password
                }).then(() => {
                    this.$router.push('/');
                });

            }
        }
    }
</script>

<style scoped>
    .signin {
        text-align: center;
        width: 400px;
        height: 320px;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        position: absolute;
        top: 0;
        bottom: 200px;
        left: 0;
        right: 0;
        margin: auto;
    }

    .signin-form {
        margin: 0 auto;
        align-items: center;
    }

    .form-title {
        font-size: 24px;
        margin-bottom: 20px;
        font-weight: lighter;
    }

    .form-footer {
        margin-top: 10px;
        display: flex;
        justify-content: space-between;
    }
</style>