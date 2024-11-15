<template>
  <main class="flex h-[95vh] flex-col items-center justify-center">
    <div class="max-w-[600px] mx-auto text-center">
      <h1>Bubble Sort</h1>
      <form @submit.prevent="handleSort">
        <label for="numbers">Enter comma-separated integers:</label>
        <input id="numbers" v-model="input" type="text" class="w-full p-2 my-2 border border-gray-300 rounded-md"
          placeholder="e.g., 5,3,8,1" />
        <button type="submit"
          class="px-4 py-2 bg-blue-500 text-white border-none rounded-md cursor-pointer hover:bg-blue-700">Sort</button>
      </form>

      <div v-if="errorMessage" class="mt-4 text-red-500">{{ errorMessage }}</div>
      <div v-if="sortedNumbers.length > 0" class="mt-4">
        <h2>Sorted Numbers:</h2>
        <p>{{ sortedNumbers.join(", ") }}</p>
      </div>
    </div>
  </main>
</template>

<script lang="ts">
import { defineComponent, ref } from "vue";

export default defineComponent({
  name: "BubbleSort",
  setup() {
    const input = ref<string>("");
    const sortedNumbers = ref<number[]>([]);
    const errorMessage = ref<string>("");

    const handleSort = async () => {
      errorMessage.value = "";

      if (!input.value.trim()) {
        errorMessage.value = "Please enter some numbers.";
        return;
      }
      const numbers = input.value
        .split(",")
        .map((num) => num.trim())
        .map((num) => Number(num));

      if (numbers.some((num) => !Number.isInteger(num))) {
        errorMessage.value = "Please enter only integers separated by commas.";
        return;
      }

      try {
        const res = await fetch(`${import.meta.env.VITE_API_URL}/sort`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ array: numbers }),
        });

        if (!res.ok) {
          throw new Error(`HTTP error! status: ${res.status}`);
        }

        const data = await res.json();
        sortedNumbers.value = data.sorted_array;
      } catch (err) {
        console.error(err);
        errorMessage.value = "Error: Could not sort numbers.";
      }
    };

    return {
      input,
      sortedNumbers,
      errorMessage,
      handleSort,
    };
  },
});
</script>

