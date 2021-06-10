import state from "@/state";
import { Context } from "@nuxt/types";
export default ({ redirect,route }: Context) => state.token || redirect(`/auth/login?url=${ encodeURIComponent(route.path)}`);