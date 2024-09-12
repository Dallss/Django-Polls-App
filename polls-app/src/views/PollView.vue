<template>
  <div>
    <h1>{{ question.question_text }}</h1>
    <ul>
      <li v-for="choice in choices" :key="choice.id">
        {{ choice.choice }} (Votes: {{ choice.votes }})
      </li>
    </ul>
  </div>
</template>

<script>
import sileo from 'sileo'
const Question = new sileo.Model('polls', 'questions')

export default {
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      question: {}
    }
  },
  mounted() {
    console.log('PollView has been created')
    this.fetchData()
  },
  methods: {
    async fetchData() {
      const data = await Question.objects.get(this.id)
      console.log('fetched using pk')
      console.log(data)
      this.question = data
    }
  }
}
</script>
