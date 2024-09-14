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
    <br><br>

    <label for="question_text"> New Choice: </label>
    <input type="text" v-model="newChoice" name="question_text" id="question_text" /> <br />
    <button @click="addChoice()">Add Choice</button>

    <br /><br />
    <button @click="deleteQuestion()">Delete Question</button>
    <br /><br />
    <button @click="editQuestion()">Edit Question</button>
  </div>
</template>

<script>
import sileo from 'sileo'
const Question = new sileo.Model('polls', 'questions')
const Choices = new sileo.Model('polls', 'choices')

export default {
  props: {
    id: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      question: {},
      selectedChoice: null,
      newChoice: null
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
        selected.votes = selected.votes + 1
        selected.question = this.id
        Choices.objects.update({ pk: this.selectedChoice }, selected)
        console.log('Updated data')

        this.$router.push('/')
      }
    },
    async addChoice() {
      if (!this.newChoice) {
        alert('Type a new choice!')
        return
      }
      try {
        const formData = {
          choice_text: this.newChoice,
          question: this.id,
          votes: 0
        }
        await Choices.objects.create(formData)
        console.log('Success adding choice')

        this.newChoice = ''
        this.question.choices.push(formData)
      } catch (error) {
        console.error('Error adding choice:', error)
        alert('Failed to add choice.')
      }
    },
    async deleteQuestion() {
      try{
        await Question.objects.delete({'pk': this.id})
      }catch(error){
        console.log(error)
      }
  }
  }
}
</script>
