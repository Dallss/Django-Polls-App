<template>
  <div>
    <h1>{{ question.question_text }}</h1>
    <ul>
      <div v-for="choice in question.choices" :key="choice.pk">
        <input type="radio" name="choices" :value="choice.pk" v-model="selectedChoice" />
        <label>{{ choice.choice_text }} (Votes: {{ choice.votes }}) </label>
      </div>
    </ul>

    <button @click="submit()">Submit</button>
    <button @click="addChoice()">Add Choice</button>
    <button @click="deleteQuestion()">Delete Question</button>
  </div>
</template>

<script>
import sileo from 'sileo'
const Question = new sileo.Model('polls', 'questions')
const Choices = new sileo.Model('polls', 'choices')

export default {
  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      question: {},
      selectedChoice: null
    }
  },
  mounted() {
    console.log('PollView has been created')
    this.fetchData()
  },
  methods: {
    async fetchData() {
      const data = await Question.objects.get(this.id)
      const dat = await Choices.objects.filter()

      console.log('fetched using pk')
      console.log(data)
      console.log(dat)
      this.question = data
    },
    async submit() {
      if (this.selectedChoice == null) {
        alert('None selected!')
      } else {
        const selected = await Choices.objects.get(this.selectedChoice)
        console.log(selected)
        let votes = selected.votes + 1
        Choices.objects.update({ pk: this.selectedChoice }, { votes: votes })
        console.log('Updated data')

        this.$router.push('/')
      }
    }
  }
}
</script>
