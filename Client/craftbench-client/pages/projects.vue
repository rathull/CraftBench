<template>
    <section class="page has-background-light">
        <div class="hero is-info">
            <div class="hero-body">
                <h1 class="title is-2">Your Projects</h1>
                <h2 class="subtitle is-4">View and edit your upcoming projects here.</h2>
            
                <b-field>
                    <p class="control">
                        <b-button type="is-primary">New Project</b-button>
                    </p>
                    <p class="control">
                        <b-button type="is-success" @click="$fetch">Refresh</b-button>
                    </p>
                    <p class="control">
                        <b-button type="is-dark" @click="$fetch">Logout</b-button>
                    </p>
                </b-field>
            </div>
        </div>

        <div class="section has-text-centered">
            <div 
                v-if="projects.length === 0 && !$fetchState.pending" 
                class="container has-text-centered"
            >
                <h3 class="title">You have no projects!</h3>
                <b-button tag="nuxt-link" to="/project/create" type="warning">
                    Create one!
                </b-button>
            </div>

            <div 
                v-for="(project) in projects" :key="parseInt(project.id)" 
                class="project-card"
            >
                <div 
                    :style="`background-image: url('${project.data.banner}');`" 
                    class="project-banner" 
                />

                <div class="project-body">
                    <h1 class="title is-5">{{ project.data.name }}</h1>
                    <p>
                        <nuxt-link 
                            :to="`/event/view/${project.data.region}`" 
                            style="color: var(--warning) !important;"
                        >
                            ({{ project.data.region }})
                        </nuxt-link>
                    </p>
                    <br>
                    <b-button 
                        tag="nuxt-link" :to="`/project/${project.id}`"
                        type="is-primary">View More
                    </b-button>
                </div>
            </div>
        </div>
    </section>
</template>

<script lang="ts">
import Vue from "vue";
import axios from "axios";
import state from "@/state";

export default Vue.extend({
    middleware: "auth",
    data() {
        return {
            projects: []
        };
    },
    async fetch() {
        const res = await axios.get(`${state.GLOBALS.BASE_URL}/projects/get`, {
            headers: {
                authorization: `Bearer ${state.token}`
            }
        });

        this.projects = res.data.projects;
    }
})
</script>

<style scoped>
.project-card {
    background: var(--dark);
    margin: 2rem;
    display: inline-block;
    width: 20rem;
    border-radius: 20px;
    overflow: hidden;
}

.project-banner {
    width: 20rem;
    height: 20rem;
    background-size: cover;
    background-position: center;
}

.project-body {
    padding: 2rem;
    text-align: center;
    color: white !important;
}

.project-body * {
    color: white !important;
}
</style>