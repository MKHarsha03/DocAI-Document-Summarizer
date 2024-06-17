<template>
    <div class="chatscreen" z-index="0">
        <div class="instructions">
            <div class="instr_boxes">
                <p style="text-align:center">Step 1:</p>
                <p style="text-align:center">Upload the files to the assistant.</p>
            </div>
            <div class="instr_boxes">
                <p style="text-align:center">Step 2:</p>
                <p style="text-align:center">Ask the AI about the document.</p>
            </div>
            <div class="instr_boxes">
                <p style="text-align:center">Step 3:</p>
                <p style="text-align:center">Understand the details of any file in no time.</p>
            </div>
        </div>
        <div>
            <ul style="list-style-type: none;">
                <li v-bind:class="{'user_messages':user.speaker==='User','assistant_messages':user.speaker==='DocAI'}" v-for="user in user_prompts"><p>{{ user.speaker }}:<br>{{ user.message }}</p></li>
            </ul>
        </div>
    </div>
    <div class="promptSection" z-index="1">
        <form name="myForm" id="myForm" @submit.prevent="registerMessage">
            <textarea id="prompt" name="myPrompt" rows="1" placeholder="Ask a Question..." v-model="myPrompt"></textarea>
            <input type="file">
            <input type="submit">
        </form>
    </div>
</template>
<script>
    export default{
        data(){
            return{
                myPrompt:null,
                user_prompts:[
                    {speaker:'DocAI',message:'How can I help you?'}
                ]
            };
        },
        methods:{
            registerMessage(){
                let item={speaker:'User',message:this.myPrompt}
                this.user_prompts.push(item)
                let item2={speaker:'DocAI',message:this.myPrompt}
                this.user_prompts.push(item2)
                this.myPrompt=null
            }
        }
    }
</script>
<style></style>
