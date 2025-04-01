const { createApp } = Vue;

createApp({
    data() {
        return {
            operadoras: [],
            search: ''
        };
    },
    mounted() {
        // Consumir a API do backend
        fetch('http://localhost:5000/api/operadoras')
            .then(response => response.json())
            .then(data => {
                this.operadoras = data;
            })
            .catch(error => console.error('Erro:', error));

            fetch(`http://localhost:5000/api/search?q=${this.search}`)
            .then(response => response.json())
            .then(data => {
              this.operadoras = data;
            });
    },
    computed: {
        filteredOperadoras() {
            const searchLower = this.search.toLowerCase();
            return this.operadoras.filter(op => 
                op.razao_social.toLowerCase().includes(searchLower) ||
                op.cnpj.toLowerCase().includes(searchLower)
            );
        }
    }
}).mount('#app');