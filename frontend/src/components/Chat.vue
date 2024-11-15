<template>
  <main class="flex h-screen flex-col items-center justify-center">
    <section
      class="shadow-md bg-gray-100 flex flex-col origin:w-[800px] w-full origin:h-[735px] h-full rounded-md p-2 md:p-6">
      <div class="border-b border-gray-300 pb-6">
            <h1 class="text-black text-xl md:text-2xl font-medium">
              Chat
            </h1>
      </div>

      <div ref="chatContainer" class="flex-1 relative overflow-y-auto my-4 md:my-6">
        <div class="absolute w-full">
          <Message v-for="(msg, index) in history" :key="index" :isUser="msg.from_ === 'user'" :message="msg.message"
            :processing="msg.processing" />
        </div>
      </div>

      <form class="flex h-[40px] gap-2" @submit.prevent="handleSend">
        <input v-model="input"
          class="border border-gray-300 flex-1 text-sm md:text-base outline-none bg-transparent rounded-md p-2"
          placeholder="Send a message..." />
        <button type="submit"
          class="bg-blue-500 text-white hover:bg-blue-800 flex rounded-md items-center justify-center px-2.5 origin:px-3">
          <svg width="20" height="20" viewBox="0 0 20 20">
            <path
              d="M2.925 5.025L9.18333 7.70833L2.91667 6.875L2.925 5.025ZM9.175 12.2917L2.91667 14.975V13.125L9.175 12.2917ZM1.25833 2.5L1.25 8.33333L13.75 10L1.25 11.6667L1.25833 17.5L18.75 10L1.25833 2.5Z" />
          </svg>
          <span class="font-semibold text-sm ml-2">
            Send
          </span>
        </button>
      </form>
    </section>
  </main>
</template>

<script lang="ts">
import { defineComponent, ref, nextTick } from "vue";
import Message from "./Message.vue";

export default defineComponent({
  name: "Chat",
  components: {
    Message,
  },
  setup() {
    const input = ref<string>("");
    const history = ref<
      { from_: "user" | "bot"; message: string; processing?:boolean }[]
    >([]);
    const chatContainer = ref<HTMLDivElement | null>(null);

    const scrollToBottom = () => {
      if (chatContainer.value) {
        chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
      }
    };

    const handleSend = async () => {
      if (!input.value.trim()) return; 

      history.value.push({ from_: "user", message: input.value,processing: false});
      history.value.push({ from_: "bot", message: "", processing: true });

      const botIndex = history.value.length - 1;
      nextTick(scrollToBottom);

      try {

        const historyToSend = history.value.slice(0,-2).map(({ from_, message }) => ({
          from_,
          message,
        }));

        const res = await fetch(`${import.meta.env.VITE_API_URL}/chat`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            history: historyToSend,
            new_message: input.value,
          }),
        });

        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }

        const data = await res.json();

        const lastBotMessage = data.updated_history[botIndex];
        history.value[botIndex] = {...lastBotMessage, processing: false};

        nextTick(scrollToBottom);

        input.value = ""; 
      } catch (err) {
        console.error(err);
        history.value[botIndex] = {
          from_: "bot",
          message: "Error: Could not fetch response. ", 
          processing: false
        };

        nextTick(scrollToBottom);
      }
    };

    return {
      input,
      history,
      handleSend,
      chatContainer,
    };
  },
});
</script>

