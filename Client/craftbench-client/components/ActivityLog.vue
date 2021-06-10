<template>

  <div>
      <section v-if="action.rawString">
          <p>{{action.rawString}}</p>
      </section>
      <section v-else>
      <span class="bg-blue-400 px-3">{{action.username}}</span> <span>Contributed {{contribution}}!</span>
      <p class="text-gray-300 italic">&nbsp; - And {{event.words.dealt}} {{action.damage}} {{event.words.damage}}</p>
      </section>
  </div>
</template>

<script>
import state from "../state";
export default {
    props:{
        event: Object,
        action:Object
    },
    computed:{
        contribution(){ return state.events[state.currentEventName].contributions[this.action.contributionType][this.action.contribution] }
    }

}
</script>

<style>

</style>