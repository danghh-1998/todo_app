<template>
    <div class="verify-email">
        <div class="verify-email-form">
            <p class="form-title">Verify your account</p>
            <b-field label="Token" label-position="on-border">
                <b-input type="text" v-model="token" maxlength="40"></b-input>
            </b-field>
            <b-button type="is-primary" expanded @click="verifyEmail">Verify email</b-button>
        </div>
    </div>
</template>

<script>
    import {ToastProgrammatic as Toast} from 'buefy'

    export default {
        name: "VerifyEmail",
        data: function () {
            return {
                token: ''
            }
        },
        mounted() {
            Toast.open({
                message: 'An email has been sent. Please check your inbox',
                duration: 5000
            })
        },
        methods: {
            verifyEmail: function () {
                this.$store.dispatch('users/verifyEmail', {
                    email_token: this.token
                }).then(() => {
                    this.$router.push('/signin');
                })
            }
        }
    }
</script>

<style scoped>
    .verify-email {
        text-align: center;
        width: 400px;
        height: 200px;
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        position: absolute;
        top: 0;
        bottom: 400px;
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