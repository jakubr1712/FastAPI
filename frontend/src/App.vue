<template>
  <nav class="flex justify-center gap-4 mb-4">
    <button :class="[currentTab === 'Chat' ? 'px-4 py-2 border-b-2 border-transparent cursor-pointer bg-transparent border-b-2 border-blue-700' : 'px-4 py-2 border-b-2 border-transparent cursor-pointer bg-transparent']" @click="currentTab = 'Chat'">
      Chat
    </button>
    <button :class="[currentTab === 'BubbleSort' ? 'px-4 py-2 border-b-2 border-transparent cursor-pointer bg-transparent order-b-2 border-blue-700' : 'px-4 py-2 border-b-2 border-transparent cursor-pointer bg-transparent']" @click="currentTab = 'BubbleSort'">
      Bubble Sort
    </button>
  </nav>

  <div class="tab-content">
    <Chat v-if="currentTab === 'Chat'" />
    <BubbleSort v-if="currentTab === 'BubbleSort'" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";
import Chat from "./components/Chat.vue";
import BubbleSort from "./components/BubbleSort.vue";

export default defineComponent({
  name: "App",
  components: {
    Chat,
    BubbleSort
  },
  setup() {
    const currentTab = ref<string>("Chat");
    return {
      currentTab,
    };
  },
});
</script>


