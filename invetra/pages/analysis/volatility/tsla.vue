<template>
    <div>
        <Navbar/>
        <VltTSLA :tslaList="tslaList"/>
        <Footer/>
    </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
import axios from "axios"
import VltTSLA from "@/components/VltTsla.vue"
export default {
    components:{VltTSLA, Navbar, Footer},
    data(){
        return{
            tslaList:[]
        }
    },
    mounted(){
            axios.get("http://127.0.0.1:5000/")
                .then(response=>{
                    this.tslaList.push(response.data.data.tsla)
                })
                .catch(e=>{
                     console.log(e)
                })

        }
}
</script>

<style>

</style>