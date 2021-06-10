<template>
  <div class=" w-screen h-screen text-center bg-no-repeat bg-cover bg-center overflow-y-scroll"  :style="{'backgroundImage':'url(/event/' + state.currentEventName + '/banner.jpg)'}">
      <div class="md:grid grid-cols-2">
          <section class="py-10 has-background-light h-screen overflow-y-scroll" >
              <h1 class="text-white text-5xl font-bold font-sans">Welcome to Craftbench</h1>
              <h2 class="text-white text-2xl font-sans">Let's build something awesome! </h2>
              <section class="box m-4 my-12 text-left px-80">
                  <form @submit.prevent="createProject()">
                  <div>
                      <span class="text-gray-500 text-lg text-left font-sans">Project Name : </span>
                      <b-input required v-model="project.name" type="text" class="lined-input focus:border-blue-400" />
                  </div>
                  <div class="scale-in-center" v-if="project.name.trim() !== ''">
                      <span class="text-gray-500 text-lg text-left font-sans">Project Description : </span>
                      <b-input required v-model="project.desc" type="textarea" class="focus:border-blue-400"> </b-input>
                  </div>
                  <div class="scale-in-center" v-if="project.name.trim() !== '' && project.desc.trim() !== ''">
                      <span class="text-gray-500 text-lg text-left font-sans">Project Length (don't worry, you can change this later)</span>
                      <b-field>
                          <b-select required @input.native="(e)=>{project.contributionType = e.target.value; project.contribution = 0}" placeholder="Select a Length">
                              <option value="small">
                                 Short (1 Week)
                              </option>
                              <option value="med">
                                 Medium (1 Week - 1 Month)
                              </option>
                              <option value="large">
                                 Large (1 Month +)
                              </option>
                          </b-select>
                      </b-field>
                  </div>
                <br><br>
                  <div class="scale-in-center"
                      v-if="project.name.trim() !== '' && project.desc.trim() !== '' && project.contributionType.trim() !== ''">
                    <span class="text-gray-500 text-lg text-left font-sans">Project Region (leave as global if none): </span>
                      <b-input required v-model="project.region" type="text" class="lined-input focus:border-blue-400 lowercase" /><br>
                      <p class="text-gray-500 text-lg text-left font-sans">Project Privacy</p>
                      <b-field>
                          <b-checkbox v-model="project.public">Public View Project</b-checkbox>
                      </b-field>

                      <b-field>
                          <b-checkbox v-if="!project.public" v-model="project.canViewTitle">Let others view your project TITLE</b-checkbox>
                      </b-field>
                      <br>
                      <div>
                          <p class="font-bold text-lg">Select an item to build</p>
                          <div class="grid grid-cols-2">
                              <div>
                                  <p @click="project.contribution = i" class="underline cursor-pointer hover:text-blue-500"
                                      v-for="(item,i) in currentContributions" :key="`item-${i}`">
                                      {{item}}
                                  </p>
                              </div>
                              <div>
                                  <img v-if="project.contribution !== false" style="width:10vw"
                                      :src="require(`~/assets/event/${state.currentEventName}/${project.contributionType}-${project.contribution}.svg`)" />
                              </div>
                          </div>
                      </div><br><br>
                      <b-button type="is-success" :loading="state.loading" class="fade" native-type="submit" v-if="project.contribution !== false">Create Project!</b-button>
                      </div>
                      </form>
                  
              </section>
          </section>
          <section class="text-center text-white flex">
              <div class="m-auto flex-auto bg-black p-5 bg-opacity-80">
                <p>{{currentEvent.cta}} In...</p>
                <h1 class="text-6xl text-white fade">{{currentEvent.title}}</h1>
                <nuxt-link to="/event">
                <p class="underline italic cursor-pointer fade" style="animation-delay:1s;opacity: 0;">Learn More</p>
                </nuxt-link>
              </div>
         
          </section>
      </div>

  </div>
</template>

<script>
import state from "../../state"
import axios from "axios"
export default {
    middleware:'auth',
    methods:{
        async createProject(){
            state.loading = true
            try{
                const res = await axios.post(state.GLOBALS.BASE_URL + '/projects/create',{
                    project_id: this.id,
                    ...this.project
                },{
                    headers: {
                        authorization: `Bearer ${state.token}`
                    }
                })
                if(res.data.success){
                   state.loading = false
                   this.$router.push(`/project/${res.data.data.id}`)
                }
            }catch(e){
                this.$swal("Error in Project Creation!",`Try again later`,'error')
                 state.loading = false
            }

        },
    },
    data(){
        return{
            project:{
                name:"",
                desc:"",
                contributionType:"",
                canViewTitle:true,
                public:false,
                region:"global",
                banner:"https://w.wallhaven.cc/full/72/wallhaven-726qly.jpg",
                contribution:false,
            }
        }
    },
    computed: {
        currentEvent(){
            return state.events[state.currentEventName]
        },
        currentContributions(){
            return state.events[state.currentEventName].contributions[this.project.contributionType]
        },
        state(){
            return state;
        }
    }
}
</script>

<style>
input.lined-input{
    border-bottom: solid 2px black;
    outline: none;
    font-size: 1.125rem;
    line-height: 1.75rem;
}
.fade{
    animation: fade 3s ease-in-out 0s forwards;
}
@keyframes fade{
    from{
        opacity: 0
    }
    to{
        opacity: 1;
    }
}
.scale-in-center{-webkit-animation:scale-in-center .5s cubic-bezier(.25,.46,.45,.94) both;animation:scale-in-center .5s cubic-bezier(.25,.46,.45,.94) both}
@-webkit-keyframes scale-in-center{0%{-webkit-transform:scale(0);transform:scale(0);opacity:1}100%{-webkit-transform:scale(1);transform:scale(1);opacity:1}}@keyframes scale-in-center{0%{-webkit-transform:scale(0);transform:scale(0);opacity:1}100%{-webkit-transform:scale(1);transform:scale(1);opacity:1}}
</style>