<template>
    <div class="m-5 text-black px-8 inset-0">
        <section class="grid grid-cols-3">
            <div class="col-span-2 my-2">
                <span
                    v-if="project.canViewTitle || project.public"
                    class="bg-yellow-200 px-4 opacity-100"
                >{{project.name}}</span>
                <span
                    v-else
                    class="bg-yellow-200 px-4 italic opacity-100"
                >Title Private</span>
                <p class="opacity-100">{{contribution}}</p>

                <a
                    v-if="project.public"
                    class="underline opacity-0 group-hover:opacity-100"
                    href="/"
                >Project Link</a>
                <p
                    v-else
                    class="italic text-gray-500 opacity-0 group-hover:opacity-100"
                >Project not public</p>
            </div>
            <div>
                <p>Completion</p>
                <radial-progress-bar
                    :diameter="100"
                    :completed-steps="completed"
                    :total-steps="total"
                    startColor="#EDDDD4"
                    stopColor="#EDDDD4"
                >
                </radial-progress-bar>
            </div>
        </section>

    </div>
</template>

<script>
import RadialProgressBar from 'vue-radial-progress'
import state from "../state";
export default {
    props: {
        project: Object,
    },
    components: {
        RadialProgressBar
    },
    computed: {
        contribution(){ return state.events[state.currentEventName].contributions[this.project.contributionType][this.project.contribution] },
        completed() {
            return this.project.tasks.map(e => e.subtasks).reduce((a, b) => a = a.concat(b), []).filter(e => e.completed).length
        },
        total() {
            return this.project.tasks.map(e => e.subtasks).reduce((a, b) => a = a.concat(b), []).length
        }
    }
}
</script>

<style>
</style>