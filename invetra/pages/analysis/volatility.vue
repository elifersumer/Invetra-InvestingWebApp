<template>
    <div class="h-screen bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <Volatility/>
        <Footer/>
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