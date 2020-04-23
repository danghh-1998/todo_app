<template>
    <div class="signup">
        <div class="signup-form">
            <p class="form-title">Create your account</p>
            <b-field label="Email" label-position="on-border">
                <b-input type="email" v-model="email" maxlength="30"></b-input>
            </b-field>
            <b-field label="Name" label-position="on-border">
                <b-input maxlength="30" v-model="name"></b-input>
            </b-field>
            <b-field label="Password" label-position="on-border">
                <b-input type="password" v-model="password" password-reveal maxlength="30"></b-input>
            </b-field>
            <b-field label="Password confirmation" label-position="on-border">
                <b-input type="password" v-model="passwordConfirmation" password-reveal maxlength="30"></b-input>
            </b-field>
            <b-field label="Tel" label-position="on-border">
                <b-input maxlength="30" v-model="tel"></b-input>
            </b-field>
            <b-button type="is-primary" expanded @click="signup">Sign up</b-button>
        </div>
    </div>
</template>

<script>
    export default {
        name: "SignUp",
        data: function () {
            return {
                email: '',
                name: '',
                password: '',
                passwordConfirmation: '',
                tel: '',
            }
        },
        methods: {
            signup: function (e) {
                e.preventDefault();
                this.$store.dispatch('users/signup', {
                    email: this.email,
                    name: this.name,
                    password: this.password,
                    password_confirmation: this.passwordConfirmation,
                    tel: this.tel
                }).then(() => {
                    this.$router.push('/verify-email');
                })
            }
        }
    }
</script>

<style scoped>
    .signup {
        text-align: center;
        width: 400px;
        height: 500px;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        position: absolute;
        top: 0;
        bottom: 100px;
        left: 0;
        right: 0;
        margin: auto;
    }

    .form-title {
        font-size: 24px;
        margin-bottom: 20px;
        font-weight: lighter;
    }

</style>