<template>
  <div class="mainHeader">
    <h1>Desafio IntuitiveCare</h1>
  </div>

  <div class="mainContent">

    <div class="searchContainer">
      <div class="searchInputContainer">
        <input 
          type="text" 
          v-model="searchTerm" 
          @input="onSearchInput"
          @keyup.enter="searchByRazaoSocial()"
          placeholder="Pesquisar por razão social..."
          class="searchInput"
        />
        <button @click="searchByRazaoSocial()" class="searchButton">
          Buscar
        </button>
      </div>
    </div>

    <div class="buttonContainer">
      <button @click="loadFirstQuery()">test_3_query_1</button>
      <button @click="loadSecondQuery()">test_3_query_2</button>
    </div>

    <div v-if="loading" class="loading">Carregando dados. Espere.</div>
    
    <div v-else>
      <div v-if="items.length === 0 && searchExecuted" class="loading">
        Nenhum resultado encontrado.
      </div>
      <div v-for="(item, index) in items" :key="index" class="queryContainer">
        <div class="queryHeaderContainer">
          <p>{{ item.razao_social }}</p>
          <button class="expandButton" @click="expandIndex(index)">{{ expandedIndex === index ? 'Fechar' : 'Expandir'}}</button>
        </div>
        

        <div v-if="expandedIndex === index" class="itemDetails">
          <pre>{{ JSON.stringify(item, null, 2) }}</pre>
        </div>
      </div>

      
    </div>
    
  </div>

  
</template>

<script>
export default {
  name: 'QueryData',
  props: {},

  data() {
    return {
      items: [],
      loading: true,
      expandedIndex: null,
      firstQuery: null,
      secondQuery: null,
      searchExecuted: false,
      searchTerm: ''
    }
  },

  methods: {
    async fetchData() {
      try {
        this.loading = true;
        const [firstResponse, secondResponse] = await Promise.all([
          this.$http.get('/primeira_query'),
          this.$http.get('/segunda_query'),
        ]);
        
        this.firstQuery = firstResponse.data;
        this.secondQuery = secondResponse.data;
        
      } catch (error) {
        console.error('Error: ', error);
      } finally {
        this.loading = false;
      }
    },

    async searchByRazaoSocial() {
      try {
        this.loading = true
        this.searchExecuted = true
        const response = await this.$http.get('/search_by_razao_social', {
          params: {
            razao_social: this.searchTerm
          }
        });
        this.items = response.data;
        this.searchTerm = ''
      } catch (error) {
        console.error('Search error:', error);
        this.items = []
      } finally {
        this.loading = false
      }
    },

    loadFirstQuery(){
      this.items = this.firstQuery
      this.expandedIndex = null
      this.searchExecuted = false
    },

    loadSecondQuery(){
      this.items = this.secondQuery
      this.expandedIndex = null
      this.searchExecuted = false
    },

    expandIndex(index){
      if (this.expandedIndex === index){
        this.expandedIndex = null
      } else {
        this.expandedIndex = index
      }
    } 
  },

  async created() {
    await this.fetchData()
  }
}
</script>

<style scoped>

.mainHeader{
  display: flex;
  height: 75px;
  padding: 0 0 0 15px;
  background-color: rgb(84, 11, 255);
  color: white;
}

.mainContent{
  display: flex;
  flex-direction: column;
  width: 50%;
  margin: 50px auto 0 auto;
}

.searchInputContainer {
  display: flex;
  gap: 10px;
  width: 100%;
  border: red solid 1px;
  justify-content: center;
  margin: 0 0 20px 0;
  align-items: center;
}

.searchInput {
  padding: 10px 15px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

.searchButton{
  height: 35px;
  padding: 10px 20px;
  background-color: rgb(84, 11, 255);
  color: white;
  border: 1px solid black;
  border-radius: 5px;
  cursor: pointer;
}

.buttonContainer {
  display: flex;
  gap: 15px;
  margin-bottom: 20px;
  margin: 0 auto
}

.buttonContainer button {
  padding: 10px 20px;
  background-color: rgb(84, 11, 255);
  color: white;
  border: 1px solid black;
  border-radius: 5px;
  cursor: pointer;
}

.queryContainer{
  display: flex;
  flex-direction: column;
  margin: 15px 0 15px 0;
}

.queryHeaderContainer{
  display: flex;
  border: 1px black solid;
  border-radius: 16px;
  justify-content: space-between;
  align-items: center;
  padding: 5px 15px 5px 15px;
  background-color: white;
}

.expandButton{
  background-color: rgb(84, 11, 255);
  color: white;
  height: 35px;
  border: 1px black solid;
  border-radius: 5px;
  padding: 0 10px;
  cursor: pointer;
}

.itemDetails {
  margin-bottom: 15px;
  padding: 15px;
  background-color: #f5f5f5;
  border-radius: 0 0 8px 8px;
  word-break: normal;
  border: 1px solid black;
  border-top: none;
}

.loading {
  padding: 20px;
  text-align: center;
  font-style: italic;
  color: #666;
}
</style>