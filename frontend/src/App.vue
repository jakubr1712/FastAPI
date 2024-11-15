<template>
 <Chat/>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Chat from "./components/Chat.vue";

export default defineComponent({
  name: "App",
  components: {
    Chat,
  },
});
</script>


