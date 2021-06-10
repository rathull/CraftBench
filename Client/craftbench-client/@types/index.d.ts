import { Route } from "vue-router";

// 1. Make sure to import 'vue' before declaring augmented typesimport { SweetAlertResult } from "sweetalert2";

declare module "vue/types/vue" {
    interface Vue {
        $swal(title: string, message: string, icon: "success" | "error" | "warning" | "info" | "question"): Promise<SweetAlertResult>;
        $route: Route;
    }
}

declare interface IEvent {
    title: string
    desc: string
    cta: string
    contributions: {
        small: string[]
        med: string[]
        large: string[]
    }
}