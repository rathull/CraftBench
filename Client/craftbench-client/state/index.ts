import Vue from "vue";
import { IEvent } from "~/@types";
import axios from "axios";

const state = Vue.observable({
    // globals:
    GLOBALS: {
        BASE_URL: "https://a120oc.deta.dev"
    },
    //loading state
    loading: false,
    // User token:
    token: null as (string | null),

    // User data:
    userData: {
        name: "",
        email: "",
        username: ""
    },

    // Store temporary data for onboarding
    temporarySignupData: {
        username: null as (string | null),
        password: null as (string | null),
        onboardingPhase: false
    },

    // Event data:
    currentEventName: "dragon",
    events: {
        dragon: {
            title: "Dragon's Terror",
            desc: "The lands of Nimrasea, a once peaceful land has become unstable and over run by dragons. In order to keep the balance, the universe has begun to blend these two universes together, and the dragons who once ruled Nimrasea have begun to plunder Earth. Efforts to repel the invaders have been so far, pyrrhic at best. The dragons show no signs of slowing down, and have refused to come with an agreement. The world has put together a task force with one mission: to research and develop more effective measures to keep OUR people safe! ",
            cta: "Join the Mission!",
            pending: "Pending Taskforce Missions",
            words: {
                dealt: "dealt",
                damage: "damage",
            },
            contributions: {
                small: ["Dragon-Piercing Arrows", "Dragon Traps","Warring Equipment", "Long Range Spears"],
                med: ["Hyperspeed Bows", "Enhanced Anti-Dragon Magic", "Ally Summoning"],
                large: ["DRAGON OBLITERATOR", "Orbital Missle Strike", "High Risk Negotiation"], 
            }
        }
      } as Record<string, IEvent>
});

if (!("__state__" in window) && process.env.NODE_ENV !== "production") {
    Object.defineProperty(window, "__state__", {
        get: () => state
    });
}

export default state;

// Methods:
export async function login(username: string, password: string): Promise<void> {
    const res = await axios.post(`${state.GLOBALS.BASE_URL}/users/login`, { username, password });
    state.token = res.data.token;
}