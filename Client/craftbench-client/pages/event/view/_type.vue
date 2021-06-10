<template>
 <div>
      
    <div v-if="event !== false"
        class="overflow-y-scroll has-background-dark text-white h-screen"
        :style="{'backgroundImage':'url(/event/' + currentEventName + '/background.jpg)'}"
    >
        <div class="container">
            <h1
                class="has-text-centered text-7xl p-2 font-bold tracking-in-expand-fwd-top text-sh"
                style="text-shadow: 0 4px 8px rgba(0,0,0,0.12), 0 2px 4px rgba(0,0,0,0.08);"
            >{{ currentEvent.title }}</h1>
            <p
                class="has-text-centered text-2xl"
                style=" text-shadow: 0 2px 4px rgba(0,0,0,0.10);"
            >At {{event.region}}</p>
            <div class="md:grid grid-cols-2 gap-24">
                <section>
                    <div class="max-w-md min-w-md">
                        <img
                            :src="require(`~/assets/event/${currentEventName}/targets/${event.targetId}.png`)"
                            style="margin-top: 4rem;"
                            class="float max-w-md"
                        />
                        <b-progress
                            type="is-success"
                            class="m-4"
                            :value="event.base"
                            :max="event.maxHealth"
                            :show-value="true"
                        ></b-progress>
                    </div>
                    <div class="bg-white text-black has-text-centered p-4 py-20 rounded-2xl shadow-md">
                        <h1 class="text-lg bold">~Activity Log~</h1>
                        <div class="max-h-52 overflow-scroll overflow-x-hidden">
                            <ActivityLog
                                 v-for="(action,i) in event.activityLog"
                                 :key="`action-${i}`"
                                :event="currentEvent"
                                :action="action"
                            />

                        </div>
                    </div>
                </section>
                <section class="hover:bg-white rounded-2xl my-5 py-8 group transition-all ease-in-out duration-200">
                    <h1 class="has-text-centered text-2xl p-2 text-black font-bold text-sh">~{{currentEvent.pending}}~</h1>
                    <div
                        style="max-height: 40rem"
                        class="group-hover:overflow-y-scroll overflow-y-hidden"
                    >
                        <PendingProject v-for="(project,i) in event.projects" :key="`action-${i}`" :project="project" />
                    </div>
                </section>
            </div>
        </div>
    </div>
     <div v-else class="text-center flex h-screen w-screen has-background-light">
            <div class="flex-auto m-auto">
               <p v-if="error" class="text-red-600">
                   {{error}}
                   <nuxt-link to="/">
                    <p class="underline cursor-pointer text-blue-300">Go Back Home -></p>
                   </nuxt-link>
               </p>
               <p v-else>Loading Event...</p>
            </div>
        </div>
 </div>
</template>

<script lang="ts">
import Vue from "vue";
import state from "@/state";
import { IEvent } from "~/@types";
import axios from 'axios'
export default Vue.extend({
     async mounted(){

        if(!this.eventID || this.eventID.trim() == ''){
            this.error = "Whatcha Doing Here?"
            return;
        }

        try{
             const res = await axios.get(state.GLOBALS.BASE_URL + `/event/get_by_region/${this.eventID}`,{
                    headers: {
                        authorization: `Bearer ${state.token}`
                    }
             })
             res.data.data.event.projects = res.data.data.projects
             this.event = JSON.parse(JSON.stringify(res.data.data.event))
        }catch (e) {
            this.error = "Unknown Region. Are you lost?"
        }
    },
    data() {
        return {
            currentType: "dragon",
            error:false as boolean|string,
            event:false,
        }
    },
    computed: {
        eventID(): string {
            return this.$route.params.type;
        },
        currentEvent(): IEvent {
            return state.events[state.currentEventName];
        },
        currentEventName(): string {
            return state.currentEventName;
        }
    }
});
</script>

<style scoped>
.tracking-in-expand-fwd-top {
    -webkit-animation: tracking-in-expand-fwd-top 0.8s
        cubic-bezier(0.215, 0.61, 0.355, 1) both;
    animation: tracking-in-expand-fwd-top 0.8s
        cubic-bezier(0.215, 0.61, 0.355, 1) both;
}
@-webkit-keyframes tracking-in-expand-fwd-top {
    0% {
        letter-spacing: -0.5em;
        -webkit-transform: translateZ(-700px) translateY(-500px);
        transform: translateZ(-700px) translateY(-500px);
        opacity: 0;
    }
    40% {
        opacity: 0.6;
    }
    100% {
        -webkit-transform: translateZ(0) translateY(0);
        transform: translateZ(0) translateY(0);
        opacity: 1;
    }
}
@keyframes tracking-in-expand-fwd-top {
    0% {
        letter-spacing: -0.5em;
        -webkit-transform: translateZ(-700px) translateY(-500px);
        transform: translateZ(-700px) translateY(-500px);
        opacity: 0;
    }
    40% {
        opacity: 0.6;
    }
    100% {
        -webkit-transform: translateZ(0) translateY(0);
        transform: translateZ(0) translateY(0);
        opacity: 1;
    }
}
.float {
    -webkit-animation: float 1.5s infinite alternate;
    -moz-animation: float 1.5s infinite alternate;
    -o-animation: float 1.5s infinite alternate;
    animation: float 1.5s infinite alternate;
    -webkit-animation-timing-function: ease-in-out;
    -moz-animation-timing-function: ease-in-out;
    -o-animation-timing-function: ease-in-out;
    animation-timing-function: ease-in-out;
    -webkit-animation-iteration-count: infinite;
    -moz-animation-iteration-count: infinite;
    -o-animation-iteration-count: infinite;
    animation-iteration-count: infinite;
}
@keyframes float {
    0% {
        -webkit-transform: translateY(0);
        -moz-transform: translateY(0);
        -o-transform: translateY(0);
        transform: translateY(0);
    }
    100% {
        -webkit-transform: translateY(-20px);
        -moz-transform: translateY(-20px);
        -o-transform: translateY(-20px);
        transform: translateY(-20px);
    }
}
@-webkit-keyframes float {
    0% {
        -webkit-transform: translateY(0);
        transform: translateY(0);
    }
    100% {
        -webkit-transform: translateY(-20px);
        transform: translateY(-20px);
    }
}
</style>