import state from "@/state";
import { Context } from "@nuxt/types";
export default ({ redirect }: Context) => state.temporarySignupData.onboardingPhase || redirect("/auth/signup");