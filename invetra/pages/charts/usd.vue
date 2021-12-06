<template>
    <div class="h-screen bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <USD/>
        <Footer/>
    </div>
</template>

<script>
import axios from 'axios'
import USD from '@/components/USD.vue'
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
    export default {
        component:{
            Navbar, Footer, USD
        },
        
        
        }   
    
</script>

<style scoped>

</style>