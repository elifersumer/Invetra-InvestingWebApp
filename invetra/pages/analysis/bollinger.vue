<template>
    <div class="bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <Bollinger/>
        <Footer class="bottom-0"/>
    </div>
</template>

<script>
import axios from 'axios'
import Bollinger from '@/components/Bollinger.vue'
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
    export default {
        component:{
            Navbar, Footer, Bollinger
        },
        
        }   
    
</script>

<style scoped>

</style>