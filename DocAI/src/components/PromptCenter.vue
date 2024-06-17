<template>
    <div class="chatscreen">
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
        <div class="conversation">
            <ul style="list-style-type: none;">
                <li>
                    <p class='user_messages'>
                    {{ message }}
                    </p>
                </li>
            </ul>
        </div>
    </div>
    <div class="promptSection">
        <form name="myForm" id="myForm">
            <textarea id="prompt" name="myPrompt" rows="1" placeholder="Ask a Question..."></textarea>
            <input type="file" id="input_file" name="my_file">
            <button type="submit">Submit Prompt</button>
        </form>
    </div>
</template>
<script></script>
<style></style>
