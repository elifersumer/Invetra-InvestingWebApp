<template>
    <div class="h-screen bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <TSLA/>
        <Footer/>
    </div>
</template>

<script>
import axios from 'axios'
import TSLA from '@/components/TSLA.vue'
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
    export default {
        component:{
            Navbar, Footer, TSLA
        },
        data(){
            return{
                usdList:[],
                aaplList:[]
            }
        },
        mounted(){
            axios.get("http://127.0.0.1:5000/")
                .then(response=>{
                    this.usdList.push(response.data.data.usd)
                    this.aaplList.push(response.data.data.aapl)
                })
                .catch(e=>{
                     console.log(e)
                })

        }
        }   
    
</script>

<style scoped>

</style>