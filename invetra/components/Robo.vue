<template>
    <div class="flex flex-col mx-auto font-oswald relative text-darkblue">
        <h class="text-lg font-bold mx-auto mt-24">ROBO-ADVISOR TOOL</h>
        <br>
        <div id="advising" style="display:none;" class="mx-auto text-center bg-white rounded shadow-md w-1/3 mb-10">
            <p class="font-bold text-lg">{{this.result}}</p>
            <p class="text-sm w-1/2 mx-auto">Below is the suggested BENCHMARK PORTFOLIO Asset Group Distribution for your estimated Risk/Return Profile based on the survey results you have completed.</p>
            <p class="font-semibold">{{this.advice}}</p>
        </div>
        <div class="h-full bg-white p-6 px-40 rounded shadow-md mx-auto">
            <p class="text-lg font-bold">Fill the survey and click the submit button for advising.</p>
            <br>
            <ul class="list-decimal" @change="onChange($event)">
                <li>
                    <div id="soru1">
                        <p class="mb-2 font-semibold">What is the main purpose of your investments?</p>
                        <ul class="text-md">
                            <li><input type="radio" id="1a" name="s1" value="1a"><label for="1a"> I don't have any investment instrument</label></li>
                            <li><input type="radio" id="1b" name="s1" value="1b"><label for="1b"> Protecting the the values of my assets</label></li>
                            <li><input type="radio" id="1c" name="s1" value="1c"><label for="1c"> Create an education fund</label></li>
                            <li><input type="radio" id="1d" name="s1" value="1d"><label for="1d"> Increasing financial asset</label></li>
                            <li><input type="radio" id="1e" name="s1" value="1e"><label for="1e"> To fold the main money</label></li>
                        </ul>
                    </div>
                </li>
                <br>
                <li>
                    <div id="soru2">
                        <p class="mb-2 font-semibold">Which of the investment instrument do you perefer?</p>
                            <ul>
                                <li><input type="radio" id="2a" name="s2" value="2a"><label for="2a"> Cash</label></li>
                                <li><input type="radio" id="2b" name="s2" value="2b"><label for="2b"> Currency</label></li>
                                <li><input type="radio" id="2c" name="s2" value="2c"><label for="2c"> Investment fund</label></li>
                                <li><input type="radio" id="2d" name="s2" value="2d"><label for="2d"> Cripto currencies</label></li>
                                <li><input type="radio" id="2e" name="s2" value="2e"><label for="2e"> Derivatives</label></li>
                            </ul>
                    </div>
                </li>
                <br>
                <li>
                    <div id="soru3">
                        <p class="mb-2 font-semibold">What will your attitude be if the your investment that you trust lost value?</p>
                            <ul>
                                <li><input type="radio" id="3a" name="s3" value="3a"><label for="3a"> I will regret it, I will exit the investment immediately.</label></li>
                                <li><input type="radio" id="3b" name="s3" value="3b"><label for="3b"> I will follow for a while, if the downtrend continues, I will exit the investment.</label></li>
                                <li><input type="radio" id="3c" name="s3" value="3c"><label for="3c"> I draw half of the principal, I keep half.</label></li>
                                <li><input type="radio" id="3d" name="s3" value="3d"><label for="3d"> I expect it to gain value.</label></li>
                                <li><input type="radio" id="3e" name="s3" value="3e"><label for="3e"> I reinvest at a low price to compensate for my loss.</label></li>
                            </ul>
                    </div>
                </li>
                <br>
                <li>
                    <div id="soru4">
                        <p class="mb-2 font-semibold">How do you approach the idea of investing by borrowing?</p>
                        <ul>
                            <li><input type="radio" id="4a" name="s4" value="4a"><label for="4a"> I never do</label></li>
                            <li><input type="radio" id="4b" name="s4" value="4b"><label for="4b"> I probably don't</label></li>
                            <li><input type="radio" id="4c" name="s4" value="4c"><label for="4c"> If I expect high earnings, I can</label></li>
                            <li><input type="radio" id="4d" name="s4" value="4d"><label for="4d"> I do it regardless of risk</label></li>
                        </ul>
                    </div>
                </li>
                <br>
                <li>
                    <div id="soru5">
                        <p class="mb-2 font-semibold">Which activity is most suitable for your hobbies?</p>
                        <ul>
                            <li><input type="radio" id="5a" name="s5" value="5a"><label for="5a"> Swimming</label></li>
                            <li><input type="radio" id="5b" name="s5" value="5b"><label for="5b"> Playing football</label></li>
                            <li><input type="radio" id="5c" name="s5" value="5c"><label for="5c"> Cycling</label></li>
                            <li><input type="radio" id="5d" name="s5" value="5d"><label for="5d"> Climb</label></li>
                            <li><input type="radio" id="5e" name="s5" value="5e"><label for="5e"> Bungee jumping</label></li>
                        </ul>
                    </div>
                </li>
                <br>
                <li>
                    <div id="soru6">
                        <p class="mb-2 font-semibold">What percentage of your annual income do you use in your investments?</p>
                        <ul>
                            <li><input type="radio" id="6a" name="s6" value="6a"><label for="6a"> 0-10%</label></li>
                            <li><input type="radio" id="6b" name="s6" value="6b"><label for="6b"> 10-15%</label></li>
                            <li><input type="radio" id="6c" name="s6" value="6c"><label for="6c"> 15-20%</label></li>
                            <li><input type="radio" id="6d" name="s6" value="6d"><label for="6d"> 20-25%</label></li>
                            <li><input type="radio" id="6e" name="s6" value="6e"><label for="6e"> +25%</label></li>
                        </ul>
                    </div>
                </li>
                <br>
                <li>
                    <div id="soru7">
                        <p class="mb-2 font-semibold">In which term would you like to use the return from your investment?</p>
                        <ul>
                            <li><input type="radio" id="7a" name="s7" value="7a"><label for="7a"> 10+ years</label></li>
                            <li><input type="radio" id="7b" name="s7" value="7b"><label for="7b"> 7-10 years</label></li>
                            <li><input type="radio" id="7c" name="s7" value="7c"><label for="7c"> 4-7 years</label></li>
                            <li><input type="radio" id="7d" name="s7" value="7d"><label for="7d"> 1-4 years</label></li>
                            <li><input type="radio" id="7e" name="s7" value="7e"><label for="7e"> 0-1 years</label></li>
                        </ul>
                    </div>  
                </li>
                <br>
                <li>
                    <div id="soru8" class="mb-4">
                        <p class="mb-2 font-semibold">Which stock would you prefer to invest in?</p>
                        <ul>
                            <li><input type="radio" id="8a" name="s8" value="8a"><label for="8a"> A well-established company that pays regular dividends to its investors</label></li>
                            <li><input type="radio" id="8b" name="s8" value="8b"><label for="8b"> A well-known company with growth potential</label></li>
                            <li><input type="radio" id="8c" name="s8" value="8c"><label for="8c"> A newly publicly traded company</label></li>
                            <li><input type="radio" id="8d" name="s8" value="8d"><label for="8d"> A newly formed start-up</label></li>
                            <li><input type="radio" id="8e" name="s8" value="8e"><label for="8e"> A company that has recently experienced a financial crisis</label></li>
                        </ul>
                    </div>
                </li>
                <div class="grid w-full">
                    <button class="bg-darkblue rounded-md py-2 px-10 text-white mx-auto hover:bg-orange font-bold" @click="click($e)" id="submit">Submit</button>
                </div>
                
            </ul>
            
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            data:[
                
            ],
            counter:0,
            result:"",
            advice:""
        }
    },
    methods:{
        onChange(event){
            var temp = event.target.value
            if(temp.includes("1")==true){ 
                this.data.push(temp)
            }else if(temp.includes("2")==true){
                this.data.push(temp)
            }else if(temp.includes("3")==true){
                this.data.push(temp)
            }else if(temp.includes("4")==true){
                this.data.push(temp)
            }else if(temp.includes("5")==true){
                this.data.push(temp)
            }else if(temp.includes("6")==true){
                this.data.push(temp)
            }else if(temp.includes("7")==true){
                this.data.push(temp)
            }else if(temp.includes("8")==true){
                this.data.push(temp)
            }
        },
        click(e){
            var tempdata=this.data
            //quest 1
            if(tempdata[0]=="1a"){
                this.counter+=2.5
            }else if(tempdata[0]=="1b"){
                this.counter+=5
            }else if(tempdata[0]=="1c"){
                this.counter+=7.5
            }else if(tempdata[0]=="1d"){
                this.counter+=10
            }else if(tempdata[0]=="1e"){
                this.counter+=12.5
            }
            //quest 2
            if(tempdata[1]=="2a"){
                this.counter+=2.5
            }else if(tempdata[1]=="2b"){
                this.counter+=5
            }else if(tempdata[1]=="2c"){
                this.counter+=7.5
            }else if(tempdata[1]=="2d"){
                this.counter+=10
            }else if(tempdata[1]=="2e"){
                this.counter+=12.5
            }
            //quest 3
            if(tempdata[2]=="3a"){
                this.counter+=2.5
            }else if(tempdata[2]=="3b"){
                this.counter+=5
            }else if(tempdata[2]=="3c"){
                this.counter+=7.5
            }else if(tempdata[2]=="3d"){
                this.counter+=10
            }else if(tempdata[2]=="3e"){
                this.counter+=12.5
            }
            //quest 4
            if(tempdata[3]=="4a"){
                this.counter+=3.125
            }else if(tempdata[3]=="4b"){
                this.counter+=6.25
            }else if(tempdata[3]=="4c"){
                this.counter+=9.375
            }else if(tempdata[3]=="4d"){
                this.counter+=12.5
            }
            //quest 5
            if(tempdata[4]=="5a"){
                this.counter+=2.5
            }else if(tempdata[4]=="5b"){
                this.counter+=5
            }else if(tempdata[4]=="5c"){
                this.counter+=7.5
            }else if(tempdata[4]=="5d"){
                this.counter+=10
            }else if(tempdata[4]=="5e"){
                this.counter+=12.5
            }
            //quest 6
            if(tempdata[5]=="6a"){
                this.counter+=2.5
            }else if(tempdata[5]=="6b"){
                this.counter+=5
            }else if(tempdata[5]=="6c"){
                this.counter+=7.5
            }else if(tempdata[5]=="6d"){
                this.counter+=10
            }else if(tempdata[5]=="6e"){
                this.counter+=12.5
            }
            //quest 7
            if(tempdata[6]=="7a"){
                this.counter+=2.5
            }else if(tempdata[6]=="7b"){
                this.counter+=5
            }else if(tempdata[6]=="7c"){
                this.counter+=7.5
            }else if(tempdata[6]=="7d"){
                this.counter+=10
            }else if(tempdata[6]=="7e"){
                this.counter+=12.5
            }
            //quest 8
            if(tempdata[7]=="8a"){
                this.counter+=2.5
            }else if(tempdata[7]=="8b"){
                this.counter+=5
            }else if(tempdata[7]=="8c"){
                this.counter+=7.5
            }else if(tempdata[7]=="8d"){
                this.counter+=10
            }else if(tempdata[7]=="8e"){
                this.counter+=12.5
            }
            
            console.log(this.counter)
            
            var tempres=this.counter
            if(tempres=>0 & tempres<=40){
                this.result="Conservative"
                this.advice="50% DIBS\n" + "50% Döviz(50% $ 50% €)"
            }else if(tempres>=40.1 & tempres<=50.0){
                this.result="Protectionist"
                this.advice="65% DIBS\n" + "25% Döviz(50% $ 50% €)\n" + "5% BIST100\n" + "5% Altin"
            }else if(tempres>=50.1 && tempres<=62.0){
                this.result="Balanced"
                this.advice="30% DIBS\n" + "15% Döviz(50% $ 50% €)\n" + "30% BIST100\n" + "25% Altin"
            }else if(tempres>=62.1 && tempres<=80.0){
                this.result="Risk Taker"
                this.advice="30% DIBS\n" + "15% Döviz(50% $ 50% €)\n" + "30% BIST100\n" + "25% Altin"
            }else if(tempres>=80.1 && tempres<=100.0){
                this.result="Aggressive"
                this.advice="10% DIBS\n" + "75% BIST100\n" + "15% Altin"
            }

            var x = document.getElementById("advising");
            if (x.style.display === "none") {
                x.style.display = "";
            } else {
                x.style.display = "none";
            }

            window.scrollTo(0,0)
        }
    }
}
</script>

<style>

</style>