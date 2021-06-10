<template>
   <section class="bg-white my-5 shadow" style="height:15em;">
       <div class="has-background-info border-b-2 duration-100 border-black">
           <h1 v-if="!ui.editingTitle" @click="triggerSwitchTitle(`editTaskTitle-${index}`)" class="text-white text-3xl bold mx-5">&nbsp;{{task.name}} <span v-if="isComplete" class="slide-in-elliptic-bottom-bck">✅🎉</span> </h1>
           <input v-else @focus="(e)=>e.target.value = task.name"  @focusout="e=>{triggerSwitchTitle(`editTaskTitle-${index}`); task.name = e.target.value}" :ref="`editTaskTitle-${index}`" class="seamless-input seamless-tasktitle"/>
       </div>
       <div class="m-5 overflow-y-scroll max-h-28">
                <b-field  v-for="(st,i) in task.subtasks" :key="`${index}-${i}`">
        
                    <b-checkbox v-model="st.completed">{{st.name}}</b-checkbox> 
                    <span class="opacity-0 group-hover:opacity-100 underline text-sm italic text-gray-400 cursor-pointer" @click="removeSubTask(i)">Remove Subtask</span>
            
                </b-field>
       </div>
       <b-field class="mx-5">
            <b-input @input="handleInput" v-model="ui.newTaskName" placeholder="I need to do..." type="search"></b-input>
            <p class="control">
                <b-button @click="addSubTask" class="button is-primary">Add Subtask</b-button>
            </p>
        </b-field>
   </section>
   
</template>

<script>
export default {
    props:['value','index'],
    data(){
        return{
            ui:{
               editingTitle:false,
               newTaskName:""
            },
            task: this.value
        }
    },
    computed:{
        isComplete(){
            return this.task.subtasks.filter(e=>e.completed).length == this.task.subtasks.length && this.task.subtasks.length !== 0
        }
    },
    methods: {
        handleInput(e) {
            this.$emit('input', this.task)
        },
        removeSubTask(i){
            this.task.subtasks.splice(i,1)
        },
        addSubTask(){
            if(this.ui.newTaskName.trim() == ""){
                return
            }
            this.task.subtasks.push({
                name: this.ui.newTaskName,
                completed:false
            })
            this.ui.newTaskName = ""
        },
        triggerSwitchTitle(focus){
            
            this.ui.editingTitle = !this.ui.editingTitle      
            if (this.ui.editingTitle) {
                this.$nextTick(() => {
                    this.$refs[focus].focus()
                })

            }
        }
    }
}
</script>

<style scoped>
input.seamless-tasktitle {
    font-size: 1.875rem;
    line-height: 2.25rem;
    margin-left: 1.25rem;
    margin-right: 1.25rem;
    color:white;
}
.slide-in-elliptic-bottom-bck{-webkit-animation:slide-in-elliptic-bottom-bck .7s cubic-bezier(.25,.46,.45,.94) both;animation:slide-in-elliptic-bottom-bck .7s cubic-bezier(.25,.46,.45,.94) both}
@-webkit-keyframes slide-in-elliptic-bottom-bck{0%{-webkit-transform:translateY(600px) rotateX(-30deg) scale(6.5);transform:translateY(600px) rotateX(-30deg) scale(6.5);-webkit-transform-origin:50% -100%;transform-origin:50% -100%;opacity:0}100%{-webkit-transform:translateY(0) rotateX(0) scale(1);transform:translateY(0) rotateX(0) scale(1);-webkit-transform-origin:50% 500px;transform-origin:50% 500px;opacity:1}}@keyframes slide-in-elliptic-bottom-bck{0%{-webkit-transform:translateY(600px) rotateX(-30deg) scale(6.5);transform:translateY(600px) rotateX(-30deg) scale(6.5);-webkit-transform-origin:50% -100%;transform-origin:50% -100%;opacity:0}100%{-webkit-transform:translateY(0) rotateX(0) scale(1);transform:translateY(0) rotateX(0) scale(1);-webkit-transform-origin:50% 500px;transform-origin:50% 500px;opacity:1}}
</style>