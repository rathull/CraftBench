<template>
    <b-navbar>
        <template #brand>
            <b-navbar-item
                tag="nuxt-link"
                to="/"
            >
                <b>Craftbench</b>
            </b-navbar-item>
        </template>
        <template #start>
            <b-navbar-item
                tag="nuxt-link"
                to="/event"
            >
                Event
            </b-navbar-item>
            <b-navbar-item
                tag="nuxt-link"
                to="/projects"
            >
                Projects
            </b-navbar-item>
        </template>

        <template #end>
            <b-navbar-item tag="div">
                <b-field v-if="!state.token">
                    <p class="control">
                        <b-button
                            type="is-success"
                            tag="nuxt-link"
                            to="/auth/signup"
                        >
                            Signup
                        </b-button>
                    </p>
                    <p class="control">
                        <b-button
                            type="is-dark"
                            tag="nuxt-link"
                            to="/auth/login"
                        >
                            Login
                        </b-button>
                    </p>
                </b-field>
                 <b-field v-else>
                    <p class="control">
                        <b-button
                            type="is-primary"
                            @click="logout()"
                        >
                            Log Out
                        </b-button>
                    </p>
                </b-field>
            </b-navbar-item>
        </template>
    </b-navbar>
</template>

<script>
import state from "../state"
export default {
    computed: {
        state(){
            return state;
        }
    },
    methods: {
        async logout(){
            state.token = false
            this.$router.push("/")
        }
    }
}
</script>