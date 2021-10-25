<template>
    <div class="container font-oswald fixed h-12 inset-0 z-50">
        <div class="h-16 bg-primary w-screen flex flex-col pr-4">
            <div class="flex flex-row justify-between mx-3 mt-1 -mb-2 h-6">
                <div class="flex flex-row">
                    <img src="@/assets/Invetra.png" class="w-icon h-icon -mt-1">
                    <router-link class="text-lg text-white font-bold" to="/">INVETRA</router-link>
                </div>
                <input class="bg-secondary h-6 px-5 pr-16 rounded-lg text-sm focus:outline-none placeholder-gray" 
                            type="search" name="search" placeholder="Search">
                <div class="flex flex-row justify-center">
                    <button class=" font-bold text-xs text-white bg-orange active:bg-darkorange w-btn h-btn rounded align-middle mr-1">
                        Sign Up
                    </button>
                    <button class="text-xs text-white bg-darkblue w-btn h-btn rounded align-middle active:bg-black">Sign In</button>
                    <img src="@/assets/british.png" class="w-flag h-flag mt-1 ml-1" alt="EN">
                </div>
            </div>
            <div class="flex flex-row justify-between text-white">
                <div class="h-6 w-screen flex flex-row justify-center font-semibold mt-3">
                    <router-link class="p-1 text-md my-auto mr-16 hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out" to="/">Home</router-link>
                    <router-link class="p-1 text-md my-auto mr-16 hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out" to="/markets">Markets</router-link>
                    <router-link class="p-1 text-md my-auto mr-16 hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out" to="/markets">Watchlist</router-link>
                    <router-link class="p-1 text-md my-auto mr-16 hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out" to="/news">News</router-link>
                    <router-link class="p-1 text-md my-auto mr-16 hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out" to="/markets">Analysis</router-link>
                    <router-link class="p-1 text-md my-auto mr-16 hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out" to="/markets">Charts</router-link>
                    <router-link class="p-1 text-md my-auto mr-16 hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out" to="/markets">Tools</router-link>
                    <router-link class="p-1 text-md my-auto hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out" to="/markets">Robo Advisor</router-link>
                </div>
                <router-link class="text-xs mr-4 mt-5 text-gray hover:text-darkblue transition duration-700 ease-in-out" to="/markets">HelpSupport</router-link>
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