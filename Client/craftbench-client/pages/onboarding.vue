<template>
    <section class="page has-background-info">
        <form
            class="section has-background-light"
            @submit.prevent="createAccount"
        >
            <div class="container level">
                <div class="level-item mockup">
                    <img src="@/assets/images/verified.svg">
                </div>
                <div
                    class="level-item"
                    style="display: block;"
                >
                    <h1 class="title has-text-info">Finish setting up your account.</h1>
                    <br>

                    <label class="label is-size-5">Full Name</label>
                    <b-field>
                        <b-input
                            v-model="fields.name"
                            type="text"
                            placeholder="Jonathan Doverman"
                            required
                        />
                    </b-field>

                    <label class="label is-size-5">Email Address</label>
                    <b-field>
                        <b-input
                            v-model="fields.email"
                            type="email"
                            placeholder="john.doe@johndoe.io"
                            required
                        />
                    </b-field>

                    <b-button
                        type="is-success"
                        native-type="submit"
                    >Let's get going!</b-button>
                </div>
            </div>
        </form>
    </section>
</template>

<script lang="ts">
import axios, { AxiosError } from "axios";
import Vue from "vue";
import state, { login } from "~/state";

export default Vue.extend({
    middleware: "onboarding",

    data() {
        return {
            fields: {
                name: "",
                email: ""
            }
        }
    },

    methods: {
        async createAccount() {
            try {
                const signupRes = await axios.post(`${state.GLOBALS.BASE_URL}/users/create`, {
                    name: this.fields.name,
                    email: this.fields.email,
                    username: state.temporarySignupData.username,
                    password: state.temporarySignupData.password,
                });

                const loginToken = await login(
                    state.temporarySignupData.username as string,
                    state.temporarySignupData.password as string
                );

                await this.$swal(
                    `Welcome ${this.fields.name}!`,
                    "Created your account and redirecting...",
                    "success"
                );
                this.$router.push("/projects");
            }

            catch (error) {
                await this.$swal("Something goofed!", (error as AxiosError).response?.data.msg || error.message, "error");
                this.$router.push("/auth/signup");
            }

            finally {
                state.temporarySignupData = { username: null, password: null, onboardingPhase: false };
            }
        }
    }
})
</script>

<style scoped>
.page {
    display: flex;
    flex-direction: column;
}

form {
    margin: auto 0;
}

.mockup {
    width: 15rem;
    margin-right: 2rem;
}
</style>