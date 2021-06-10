<template>
    <div>
        <div
            v-if="project !== false"
            class="grid grid-cols-5"
        >
            <section
                class="h-screen col-span-2 bg-cover"
                :style="`background-image:url('${project.banner}')` "
            >
                <section class="has-background-info">
                    <h1
                        @click="triggerSwitch('editTitle')"
                        class="bold font-sans break-normal mx-4 text-white inline-block"
                        v-if="!ui.editTitle"
                        :style="`text-shadow: 0 4px 8px rgba(0,0,0,0.12), 0 2px 4px rgba(0,0,0,0.08);font-size:3vw;`"
                    >{{project.name}}</h1>
                    <section v-else>
                        <input
                            v-model="project.name"
                            @focusout="triggerSwitch('editTitle')"
                            ref="editTitle"
                            class="seamless-input seamless-title"
                        />
                    </section>
                    <b-button
                        type="is-primary is-light"
                        class="float-right m-5"
                        :class="{noti:changes}"
                        rounded
                        @click="ui.options = !ui.options"
                    >Options <div
                            class="noti-badge animate-pulse"
                            v-if="changes"
                        ></div>
                    </b-button>
                    <b-collapse :open="ui.options">
                        <section class="w-full py-4">
                            <b-button
                                type="is-primary"
                                @click="addTask()"
                            >Add Task</b-button>
                            <b-button
                                type="is-success"
                                :disabled="!changes"
                                :loading="state.loading"
                                :class="{'animate-bounce':changes}"
                                @click="saveProject()"
                            >Save</b-button>
                            <b-dropdown aria-role="list">
                                <template #trigger="{ active }">
                                    <b-button
                                        label="More"
                                        type="is-primary"
                                        :icon-right="active ? 'menu-up' : 'menu-down'"
                                    />
                                </template>
                                <b-dropdown-item
                                    aria-role="listitem"
                                    @click="ui.share = true"
                                >Share</b-dropdown-item>
                                <b-dropdown-item
                                    aria-role="listitem"
                                    @click="ui.changeImage = true"
                                >Change Background Image</b-dropdown-item>
                                <b-dropdown-item
                                    aria-role="listitem"
                                    class="has-background-danger"
                                    @click="deleteProject()"
                                >Delete Project</b-dropdown-item>
                            </b-dropdown>
                            <b-button
                                icon-right="sword"
                                @click="submitProject()"
                                v-if="project.tasks.filter(e=>e!==undefined && e!==false).map(e => e.subtasks).reduce((a, b) => a = a.concat(b), []).length == completed"
                                type="is-success"
                            >
                                Submit Project
                            </b-button>
                        </section>
                    </b-collapse>
                    <nuxt-link :to="`/event/view/${project.region}`">
                        <b-button>View Region Event</b-button>
                    </nuxt-link>
                </section>
                <section
                    v-if="ui.share"
                    class="bg-white shadow-md p-10"
                >
                    <form @submit.prevent="">
                        <b-button
                            class="float-right"
                            @click="ui.share = false"
                            icon-right="close"
                        />
                        <b-field label="Share Project Via Username">
                            <b-input
                                v-model="forms.username"
                                required
                            >
                            </b-input>
                        </b-field>
                        <b-button
                            type="is-success"
                            native-type="submit"
                        >Share</b-button>
                    </form>
                </section>
                <section
                    v-if="ui.changeImage"
                    class="bg-white shadow-md p-10"
                >
                    <form @submit.prevent="project.banner = forms.banner; ui.changeImage = false">
                        <b-button
                            class="float-right"
                            @click="ui.changeImage = false"
                            icon-right="close"
                        />
                        <b-field label="Change Background Image">
                            <b-input
                                type="url"
                                v-model="forms.banner"
                                required
                            >
                            </b-input>
                        </b-field>
                        <b-button
                            type="is-success"
                            native-type="submit"
                        >Save</b-button>
                    </form>
                </section>
                <section class="opacity-20 hover:opacity-100 h-screen duration-200 bg-gray-500 hover:-translate-y-20 transform translate-y-52 ">
                    <div class="container p-7 text-white">

                        <br><br>
                        <p
                            @click="triggerSwitch('editDesc')"
                            v-if="!ui.editDesc"
                            class="max-h-100 overflow-y-scroll break-normal "
                        >{{project.desc}}</p>
                        <section v-else>
                            <textarea
                                class="bg-transparent h-96"
                                style="min-width: 35vw"
                                v-model="project.desc"
                                @focusout="triggerSwitch('editDesc')"
                                ref="editDesc"
                            ></textarea>
                        </section>
                    </div>
                    <radial-progress-bar
                        :diameter="175"
                        :completed-steps="completed"
                        :total-steps="project.tasks.filter(e=>e!==undefined && e!==false).map(e => e.subtasks).reduce((a, b) => a = a.concat(b), []).length"
                        startColor="#EDDDD4"
                        stopColor="#EDDDD4"
                        class="inline-block"
                    >
                        <p
                            class="text-white text-center"
                            style="text-shadow: 0 4px 8px rgba(0,0,0,0.12), 0 2px 4px rgba(0,0,0,0.08);"
                        >Project Completion!</p>
                    </radial-progress-bar>
                </section>
            </section>
            <section class="col-span-3 h-screen has-background-light overflow-y-scroll">
                <div
                    v-if="project.tasks.filter(t =>t !== false).length == 0 "
                    class="p-52"
                >
                    <img
                        class="max-h-96 max-w-96"
                        src="@/assets/images/no-tasks.svg"
                    />
                    <br>
                    <h1 class="italic bold text-gray-400 text-2xl text-center">You have no tasks, add some by clicking <br> "Add Task" on the left!</h1>
                </div>
                <div
                    v-else
                    class="mx-32"
                >
                    <div
                        v-for="(task,i) in project.tasks"
                        :key="`taskview-${i}-${task.name}`"
                        class="group"
                    >
                        <template v-if="task">
                            <p
                                class="del inline-block underline text-sm italic text-gray-400 cursor-pointer opacity-0 group-hover:opacity-100 duration-300 group-hover:translate-y-0 transform translate-y-52 "
                                @click="removeTask(task)"
                            >Remove Task</p>
                            <TaskView
                                v-model="project.tasks[i]"
                                :index="i"
                            />
                        </template>
                    </div>
                </div>
            </section>
        </div>
        <div
            v-else
            class="text-center flex h-screen w-screen has-background-light"
        >
            <div class="flex-auto m-auto">
                <p
                    v-if="error"
                    class="text-red-600"
                >
                    {{error}}
                    <nuxt-link to="/">
                        <p class="underline cursor-pointer text-blue-300">Go Back Home -></p>
                    </nuxt-link>
                </p>
                <p v-else>Loading Project...</p>
            </div>
        </div>
    </div>
</template>

<script>
import RadialProgressBar from 'vue-radial-progress'
import state from '../../state'
import axios from 'axios'
import { ToastProgrammatic as Toast } from 'buefy'


export default {
    middleware: 'auth',
    async mounted() {

        if (!this.id || this.id.trim() == '') {
            this.error = "Whatcha Doing Here?"
            return;
        }

        try {
            const res = await axios.get(state.GLOBALS.BASE_URL + `/projects/get_project_from_id/${this.id}`, {
                headers: {
                    authorization: `Bearer ${state.token}`
                }
            })

            this.oldProject = JSON.parse(JSON.stringify(res.data.data))
            this.project = JSON.parse(JSON.stringify(res.data.data))
        } catch (e) {
            this.error = "Unknown Project. Are you lost?"
        }
    },
    data() {
        return {
            active: false,
            error: false,
            globalIndex: 0,
            forms: {
                username: "",
                banner: "",
            },
            ui: {
                options: false,
                editTitle: false,
                editDesc: false,
                changeImage: false,
                share: false,
            },
            oldProject: false,
            project: false,
        }
    },
    components: {
        RadialProgressBar
    },
    methods: {
        async saveProject() {
            if (!this.changes) {
                return;
            }
            state.loading = true

            try {
                const res = await axios.post(state.GLOBALS.BASE_URL + '/projects/save', {
                    project_id: this.id,
                    data: this.project
                }, {
                    headers: {
                        authorization: `Bearer ${state.token}`
                    }
                })
                if(res.data.success){
                    Toast.open({message:'Your project has been saved',type:'is-success'})
                }
                this.oldProject = JSON.parse(JSON.stringify(this.project))
                state.loading = false
            }catch(e){
                this.$swal("Error in Saving!",`We couldn't save! Try again later`,'error')
                 state.loading = false
            }

        },
        async shareProject() {
            if (this.forms.username.trim() == '') {
                return;
            }
            state.loading = true

            try {
                const res = await axios.post(state.GLOBALS.BASE_URL + '/projects/add_user', {
                    project_id: this.id,
                    username: this.forms.username
                }, {
                    headers: {
                        authorization: `Bearer ${state.token}`
                    }
                })
                Toast.open({ message: res.data.msg, type: 'is-success' })
                this.forms.username = ''
                state.loading = false
            } catch (e) {
                this.$swal("Error in Sharing!", `Try again later`, 'error')
                this.forms.username = ''
                state.loading = false
            }

        },
        async deleteProject() {
            const confirm = await this.$swal({
                title: 'Are you sure?',
                text: "Only the owner can delete this project, and you can't recover it!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'I want to delete this project'
            })

            if (confirm.isConfirmed) {
                try {
                    const res = await axios.post(state.GLOBALS.BASE_URL + '/projects/delete', {
                        project_id: this.id,
                    }, {
                        headers: {
                            authorization: `Bearer ${state.token}`
                        }
                    })
                    if (res.data.success) {
                        Toast.open("Project Deleted")
                        this.$router.push("/projects")
                    } else {
                        this.$swal("Error in Deleting!", `${e.msg} Try again later`, 'error')
                    }
                } catch (e) {
                    this.$swal("Error in Deleting!", `Try again later`, 'error')
                }

            }
        },
        async submitProject() {
            const confirm = await this.$swal({
                title: 'Are you sure?',
                text: "Only the owner can submit this project, and you can't modify it after it is sent!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'I want to submit this project'
            })

            if (confirm.isConfirmed) {
                try {
                    const res = await axios.post(state.GLOBALS.BASE_URL + '/projects/submit_project', {
                        project_id: this.id,
                    }, {
                        headers: {
                            authorization: `Bearer ${state.token}`
                        }
                    })
                    if (res.data.success) {
                        Toast.open("Project Submited")
                        this.$router.push(`/event/view/${this.project.region}`)
                    } else {
                        this.$swal("Error in Submitting!", `${e.msg} Try again later`, 'error')
                    }
                } catch (e) {
                    this.$swal("Error in Submitting!", `Try again later`, 'error')
                }

            }
        },
        requestGlobalIndex() {
            this.globalIndex++
            return this.globalIndex
        },
        addTask() {
            this.project.tasks.push({
                name: "Click me to edit!",
                subtasks: []
            })
        },
        removeTask(t) {

            this.project.tasks = this.project.tasks.filter(tsk => tsk !== t)
            this.$forceUpdate()
        },
        triggerSwitch(focus) {
            this.ui[focus] = !this.ui[focus]

            if (this.ui[focus]) {
                this.$nextTick(() => {
                    this.$refs[focus].focus()
                })

            }
        }
    },
    computed: {
        state() {
            return state
        },
        changes() {
            return JSON.stringify(this.oldProject) !== JSON.stringify(this.project)
        },
        id() {
            return this.$route.params.id
        },
        finalTasks() {
            return this.project.tasks.filter(t => t !== false)
        },
        completed() {
            return this.project.tasks.map(e => e.subtasks).reduce((a, b) => a = a.concat(b), []).filter(e => e && e.completed).length
        }
    }
}
</script>

<style>
.noti-badge {
    position: absolute;
    top: -2.5px;
    right: -2.5px;
    width: 15px;
    height: 15px;
    background-color: var(--warning);
    border-radius: 50%;
}
.noti {
    position: relative;
}
input.seamless-input {
    background-color: transparent;
    outline: none;
    border-bottom: solid 2px;
}
input.seamless-title {
    font-size: 3vw;
    color: white;
    text-shadow: 0 4px 8px rgba(0, 0, 0, 0.12), 0 2px 4px rgba(0, 0, 0, 0.08);
}

::-webkit-scrollbar-track {
    background: #f1f1f1;
}
</style>