<template>
    <div class="container relative mt-8">
        <div class="h-8 bg-primary w-screen text-white my-auto flex flex-row justify-center">
                <div class="grid grid-cols-2 h-6 w-screen text-sm my-auto">
                    <p class="ml-20 -mr-20 my-auto">Copyright © 2021 Invetra. All rights reserved.</p>
                </div>
                <div class="h-6 w-screen flex flex-row text-sm my-auto bottom-0 right-0">
                    <router-link class="my-auto mr-4 hover:text-darkblue transition duration-700 ease-in-out" to="/">Contact Us</router-link>
                    <p class="my-auto mr-4 text-darkblue">|</p>
                    <router-link class="my-auto mr-4 hover:text-darkblue transition duration-700 ease-in-out" to="/markets">Terms of Service</router-link>
                    <p class="my-auto mr-4 text-darkblue">|</p>
                    <a class="my-auto mr-4 hover:text-darkblue transition duration-700 ease-in-out" href=#>Privacy Policy</a>
                </div>
        </div>
    </div>
    
</template>

<script>
    export default {
        
    }
</script>

<style scoped>

</style>