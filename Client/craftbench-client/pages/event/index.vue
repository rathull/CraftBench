<template>
    <div
        class="text-left w-screen h-screen bg-no-repeat bg-cover overflow-y-scroll"
        :style="{'backgroundImage':'url(/event/' + currentEventName + '/banner.jpg)'}"
    >
        <div class="md:grid grid-cols-2">
            <section class="p-6 h-screen bg-black bg-opacity-50 rounded-bl-md rounded-br-md">
                <h1 class="text-6xl max-w-min tracking-in-contract-bck text-white my-4 py-3">{{currentEvent.title}}</h1>
                <p class="text-white swing-in-top-fwd text-lg">{{currentEvent.desc}}
                    <br><br>
                    <nuxt-link to="/project/create">
                        <b-button type="is-primary">{{currentEvent.cta}}</b-button>
                    </nuxt-link>
                </p>
            </section>
            <section class="slide-in-right ">
                <div class="p-16 text-center m-24 my-20 shadow-md has-background-light">
                    <h1 class="text-xl">What you can contribute to the task force!</h1><br>
                    <p class="italic text-gray-600">Small Projects (1 Day - 1 Week)</p>
                    <b-carousel
                        :interval="3000"
                        :indicator="false"
                        :pause-hover="false"
                    >
                        <b-carousel-item
                            v-for="(name,i) in currentEvent.contributions.small"
                            :key="`small-${i}`"
                        >
                            <img
                                class="max-h-20 my-5"
                                :src="require(`~/assets/event/${currentEventName}/small-${i}.svg`)"
                            />
                            <p>{{name}}</p>
                        </b-carousel-item>
                    </b-carousel>
                    <br><br>
                    <p class="italic text-gray-600">Medium Projects (1 Week - 1 Month)</p>
                    <b-carousel
                        :interval="4000"
                        :indicator="false"
                        :pause-hover="false"
                    >
                        <b-carousel-item
                            v-for="(name,i) in currentEvent.contributions.med"
                            :key="`med-${i}`"
                        >
                            <img
                                class="max-h-20 my-5"
                                :src="require(`~/assets/event/${currentEventName}/med-${i}.svg`)"
                            />
                            <p>{{name}}</p>
                        </b-carousel-item>
                    </b-carousel>
                    <br><br>
                    <p class="italic text-gray-600">Large Projects (1 Month +)</p>
                    <b-carousel
                        :interval="5000"
                        :indicator="false"
                        :pause-hover="false"
                    >
                        <b-carousel-item
                            v-for="(name,i) in currentEvent.contributions.large"
                            :key="`small-${i}`"
                        >
                            <img
                                class="max-h-20 my-5"
                                :src="require(`~/assets/event/${currentEventName}/large-${i}.svg`)"
                            />
                            <p>{{name}}</p>
                        </b-carousel-item>
                    </b-carousel>
                </div>
            </section>
        </div>

    </div>
</template>

<script lang="ts">
import Vue from "vue";
import state from "@/state";

export default Vue.extend({
    computed: {
        currentEvent() {
            return state.events[state.currentEventName]

        },
        currentEventName() {
            return state.currentEventName
        }
    }
})
</script>

<style scoped>
.slide-in-right {
    -webkit-animation: slide-in-right 1s cubic-bezier(0.25, 0.46, 0.45, 0.94)
        1.5s both;
    animation: slide-in-right 1s cubic-bezier(0.25, 0.46, 0.45, 0.94) 1.5s both;
}
@-webkit-keyframes slide-in-right {
    0% {
        -webkit-transform: translateX(1000px);
        transform: translateX(1000px);
        opacity: 0;
    }
    100% {
        -webkit-transform: translateX(0);
        transform: translateX(0);
        opacity: 1;
    }
}
@keyframes slide-in-right {
    0% {
        -webkit-transform: translateX(1000px);
        transform: translateX(1000px);
        opacity: 0;
    }
    100% {
        -webkit-transform: translateX(0);
        transform: translateX(0);
        opacity: 1;
    }
}
.swing-in-top-fwd {
    -webkit-animation: swing-in-top-fwd 1s
        cubic-bezier(0.175, 0.885, 0.32, 1.275) 1s both;
    animation: swing-in-top-fwd 1s cubic-bezier(0.175, 0.885, 0.32, 1.275) 1s
        both;
}
@-webkit-keyframes swing-in-top-fwd {
    0% {
        -webkit-transform: rotateX(-100deg);
        transform: rotateX(-100deg);
        -webkit-transform-origin: top;
        transform-origin: top;
        opacity: 0;
    }
    100% {
        -webkit-transform: rotateX(0deg);
        transform: rotateX(0deg);
        -webkit-transform-origin: top;
        transform-origin: top;
        opacity: 1;
    }
}
@keyframes swing-in-top-fwd {
    0% {
        -webkit-transform: rotateX(-100deg);
        transform: rotateX(-100deg);
        -webkit-transform-origin: top;
        transform-origin: top;
        opacity: 0;
    }
    100% {
        -webkit-transform: rotateX(0deg);
        transform: rotateX(0deg);
        -webkit-transform-origin: top;
        transform-origin: top;
        opacity: 1;
    }
}
.tracking-in-contract-bck {
    -webkit-animation: tracking-in-contract-bck 1s
        cubic-bezier(0.215, 0.61, 0.355, 1) both;
    animation: tracking-in-contract-bck 1s cubic-bezier(0.215, 0.61, 0.355, 1)
        both;
}
@-webkit-keyframes tracking-in-contract-bck {
    0% {
        letter-spacing: 1em;
        -webkit-transform: translateZ(400px);
        transform: translateZ(400px);
        opacity: 0;
    }
    40% {
        opacity: 0.6;
    }
    100% {
        -webkit-transform: translateZ(0);
        transform: translateZ(0);
        opacity: 1;
    }
}
@keyframes tracking-in-contract-bck {
    0% {
        letter-spacing: 1em;
        -webkit-transform: translateZ(400px);
        transform: translateZ(400px);
        opacity: 0;
    }
    40% {
        opacity: 0.6;
    }
    100% {
        -webkit-transform: translateZ(0);
        transform: translateZ(0);
        opacity: 1;
    }
}
</style>