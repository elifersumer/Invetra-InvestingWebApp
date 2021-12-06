<template>
    <div class="h-screen bg-lightblue bg-repeat font-oswald">
        <Navbar/>
        <Chart/>
        <Footer/>
    </div>
</template>

<script>
import axios from 'axios'
import Chart from '@/components/Chart.vue'
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
    export default {
        component:{
            Navbar, Footer, Chart
        }
        
    }   
    
</script>

<style scoped>

</style>