var app = new Vue({
  el: '#app',
  data: {
    message: 'Hello Vue!'
  }
})

var app2 = new Vue({
  el: '#app-2',
  data: {
    message2: 'You loaded this page on ' + new Date().toLocaleString()
  }
})

var app4 = new Vue({
  el: '#app-suggestion',
  data: {
    suggestions: []
  },
  //Adapted from https://stackoverflow.com/questions/36572540/vue-js-auto-reload-refresh-data-with-timer
  created: function() {
        this.fetchSuggestionList();
        this.timer = setInterval(this.fetchSuggestionList, 3000);
  },
  methods: {
    fetchSuggestionList: function() {
        $.get('/suggestions/', function(suggest_list) {
            this.suggestions = suggest_list.suggestions;
            console.log(suggest_list);
        }.bind(this));
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    clearInterval(this.timer)
  }

})
