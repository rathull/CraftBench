        <template>
    <section class="page auth-page">
        <form
            @submit.prevent="authSubmit"
            class="pull-up"
        >
            <h1 class="title brand">Craftbench</h1>
            <h2 class="subtitle">{{ isSignup ? "Signup" : "Login" }}</h2>

            <hr>

            <b-field label="Username">
                <div>
                    <b-input
                        type="text"
                        placeholder="JohnDoe"
                        v-model="fields.username"
                    />
                    <small v-if="!fields.username">Required</small>
                </div>
            </b-field>

            <b-field label="Password">
                <div>
                    <b-input
                        type="password"
                        placeholder="Don't tell anyone!"
                        v-model="fields.password"
                    />
                    <small v-if="!fields.password">Required</small>
                    <small
                        v-else-if="fields.password.length < 8 && isSignup"
                        class="has-text-danger"
                    >At least 8 characters please.</small>
                </div>
            </b-field>

            <b-field
                label="Confirm Password"
                v-if="isSignup"
            >
                <div>
                    <b-input
                        type="password"
                        placeholder="One more time please."
                        v-model="fields.confirmPassword"
                    />
                    <small v-if="!fields.confirmPassword">Required</small>
                    <small
                        v-else-if="fields.password !== fields.confirmPassword"
                        class="has-text-danger"
                    >The passwords don't match.</small>
                </div>
            </b-field>

            <hr>

            <b-field>
                <b-button
                    type="is-success is-fullwidth"
                    native-type="submit"
                    :loading="isSubmitProcessing"
                >
                    Let's Continue ⟶
                </b-button>
            </b-field>

            <small v-if="isSignup">
                <nuxt-link to="/auth/login">Already have an account?</nuxt-link>
            </small>
            <small v-else>
                <nuxt-link to="/auth/signup">Don't have an account?</nuxt-link>
            </small>
        </form>
    </section>
</template>

<script lang="ts">
import axios, { AxiosError } from "axios";
import Vue from "vue";
import state, { login } from "@/state";

export default Vue.extend({
    data() {
        return {
            fields: {
                username: "",
                password: "",
                confirmPassword: "",
            },

            isSubmitProcessing: false
        };
    },

    computed: {
        isSignup() {
            return this.$route.params.type === "signup";
        },
    },

    methods: {
        // Middleman function calls signup or login:
        async authSubmit() {
            this.isSubmitProcessing = true;

            // Validate the form fields:
            if (await this.validateFields()) {
                // Signup:
                if (this.isSignup) await this.continueSignup();

                // Login:
                else await this.continueLogin();
            }

            this.isSubmitProcessing = false;
        },

        async validateFields(): Promise<boolean> {
            // Test for required fields:
            const isSignupConfirmationMissing = this.isSignup && !this.fields.confirmPassword;
            if (!this.fields.username || !this.fields.password || isSignupConfirmationMissing) {
                await this.$swal("Try again.", "Please fill out all fields.", "warning");
                return false;
            };

            // If signing up, check if password and confirmation match:
            if (this.isSignup && (this.fields.password !== this.fields.confirmPassword)) {
                await this.$swal("That didn't work.", "Make sure your password and confirmation match.", "warning");
                return false;
            }

            // Short password:
            if (this.fields.password.length < 8) {
                await this.$swal("Short password.", "For security, please make your password at least 8 characters.", "warning");
                return false;
            }

            return true;
        },

        async continueSignup() {
            try {
                const res = await axios.get(`${state.GLOBALS.BASE_URL}/users/exists_by_username/${this.fields.username}`);
                if (res.data.exists) {
                    await this.$swal("Sorry!", "That username is already taken!", "info");
                }

                else {
                    await this.$swal("Success!", "Press OK to finish creating your account.", "success");
                    state.temporarySignupData.username = this.fields.username;
                    state.temporarySignupData.password = this.fields.password;
                    state.temporarySignupData.onboardingPhase = true;
                    this.$router.push("/onboarding");
                }
            }

            catch (error) {
                await this.$swal("Something went wrong, retry later.", (error as AxiosError).response?.data.msg || (error as AxiosError).message, "error");
            }
        },

        async continueLogin() {
            try {
                const lastRoute = this.$route.query.url as string;
                await login(this.fields.username, this.fields.password);
                if (lastRoute) {
                    this.$router.push(decodeURIComponent(lastRoute));
                    return;
                }
                this.$router.push("/projects/");
            }

            catch (error) {
                await this.$swal("An error occurred.", (error as AxiosError).response?.data.msg || (error as AxiosError).message, "error");
            }
        }
    }
});
</script>

<style scoped>
hr {
    background-color: var(--light) !important;
}

.page {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background: var(--light);
}

form {
    background: var(--dark);
    padding: 2rem 4rem;
    min-width: 25rem;
    border-radius: 20px;
}

:not(small):not(button):not(a) {
    color: var(--light) !important;
}

a:hover,
a:active {
    color: var(--success);
}
</style>

<style>
.page.auth-page label {
    color: var(--light) !important;
}
</style>