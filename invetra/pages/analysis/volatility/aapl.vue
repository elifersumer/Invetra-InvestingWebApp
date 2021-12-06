<template>
    <div>
        <Navbar/>
        <VltAAPL :aaplList="aaplList"/>
        <Footer/>
    </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
import axios from "axios"
import VltAAPL from "@/components/VltAAPL.vue"
export default {
    components:{VltAAPL, Navbar, Footer},
    data(){
        return{
            aaplList:[]
        }
    },
    mounted(){
            axios.get("http://127.0.0.1:5000/")
                .then(response=>{
                    this.aaplList.push(response.data.data.aapl)
                })
                .catch(e=>{
                     console.log(e)
                })

        }
}
</script>

<style>

</style>