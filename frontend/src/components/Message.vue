<template>
  <div class="block mt-4 md:mt-6 pb-[7px] clear-both" :class="isUser ? 'float-right' : 'float-left'">
    <div class="flex justify-end">
      <div
        :class="['rounded-lg max-w-[300px] break-words', isUser ? 'bg-blue-500 text-white' : 'bg-gray-300  text-black', 'p-2 md:p-4']">
        <div v-if="processing" class="w-6 h-6 flex items-center justify-center">
          <div class="relative w-2 h-2 rounded-full bg-gray-800 animate-dot-flashing"></div>
        </div>
        <div v-else>
          {{ message }}
        </div>
        <svg width="12" height="7" viewBox="0 0 12 7" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M0.730278 0.921112C-3.49587 0.921112 12 0.921112 12 0.921112V5.67376C12 6.8181 9.9396 7.23093 9.31641 6.27116C6.83775 2.45382 3.72507 0.921112 0.730278 0.921112Z" />
        </svg>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent,  PropType } from "vue";

export default defineComponent({
  name: "Message",
  props: {
    isUser: {
      type: Boolean as PropType<boolean>,
      required: true,
    },
    message: {
      type: String as PropType<string>,
      required: true,
    },
    processing: {
      type: Boolean as PropType<boolean>,
      default: false,
    },
  },
});
</script>

