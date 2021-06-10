import Swal from "sweetalert2";
import Vue from "vue";

Vue.prototype.$swal = (
    title: string, 
    message: string, 
    icon?: "success" | "error" | "warning" | "info" | "question"
) => Swal.fire(title, message, icon);