<template>
    <div class="bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <Volatility/>
        <Footer class="bottom-0"/>
    </div>
</template>

<script>
import axios from 'axios'
import Volatility from '@/components/Volatility.vue'
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
    export default {
        component:{
            Navbar, Footer, Volatility
        },
        
        }   
    
</script>

<style scoped>

</style>