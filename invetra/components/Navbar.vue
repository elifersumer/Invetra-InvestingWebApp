<template>
    <div class="container font-oswald fixed top-0 z-30">
        <div class="bg-primary w-screen flex flex-col pr-4">
            <div class="flex flex-row justify-between mx-3 mt-1 -mb-2">
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
                <ul class="w-screen flex flex-row justify-center font-semibold mt-3">
                    <li class="group relative hover:bg-white hover:bg-opacity-50 py-0 px-5 z-0 hover:text-darkblue transition duration-700 ease-in-out">
                        <router-link class="p-1 text-md my-auto" to="/">Home</router-link>
                    </li>
                    <li class="group relative hover:bg-white hover:bg-opacity-50 py-0 px-5 z-0 hover:text-darkblue transition duration-700 ease-in-out">
                        <router-link class="p-1 text-md my-auto" to="/markets">Markets</router-link>
                    </li>
                    <li class="group relative hover:bg-white hover:bg-opacity-50 py-0 px-5 z-0  hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out">
                        <router-link class="p-1 text-md my-auto" to="/news">News</router-link>
                    </li>
                    <li class="group relative hover:bg-white hover:bg-opacity-50 py-0 px-5 z-0  hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out">
                        <a href="#" class="text-md my-auto">Technical Analysis</a>
                        <ul class="group-hover:block hidden absolute top-8 left-0 z-30 bg-white p-2 text-sm">
                            <li class="p-2">
                                <router-link to="/technical-analysis/volatility" class="text-black">Volatility</router-link>
                            </li>
                            <li class="p-2">
                                <a href="#" class="text-black">Bollinger Band</a>
                            </li>
                        </ul>
                    </li>
                    <li class="group relative hover:bg-white hover:bg-opacity-50 py-0 px-5 z-0  hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out">
                        <router-link class="p-1 text-md my-auto" to="/charts">Charts</router-link>
                    </li>
                    <li class="group relative hover:bg-white hover:bg-opacity-50 py-0 px-5 z-0  hover:bg-t-white hover:text-darkblue transition duration-700 ease-in-out">
                        <router-link class="text-md my-auto" to="/markets">Robo Advisor</router-link>
                    </li>
                </ul>
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