


document.addEventListener("DOMContentLoaded", function () {
    // Configurações do gráfico de barras
    var totalDespesas = parseFloat(document.getElementById('total_despesas').innerText);
    var totalReceitas = parseFloat(document.getElementById('total_receitas').innerText);
    var saldo = parseFloat(document.getElementById('saldo').innerText);
    const barConfig = {
        type: 'bar',
        data: {
            labels: ['Receitas', 'Despesas', 'Saldo Restante', 'Poupanças'],
            datasets: [{
                label: 'Receitas e Despesas',
                // data: [120, 190, 30, 50],
                data: [totalReceitas, totalDespesas, saldo, 0],
                backgroundColor: [
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(255, 99, 132, 0.2)',
                     'rgba(54, 162, 235, 0.2)',
                     'rgba(255, 206, 86, 0.2)'

                ],
                borderColor: [
                    'rgba(75, 192, 192, 1)',
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)'
                ],
                borderWidth: 1,
                hoverOffset: 4,
                borderRadius: 5
            }]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };

    // Configurações do gráfico de rosquinha
    const doughnutData = {
        labels: ['Dispesas', 'Saldo Restante'],
        datasets: [{
            data: [totalDespesas, saldo],
            backgroundColor: [

                'rgba(255, 99, 132, 0.7)',
                'rgba(54, 162, 235, 0.7)',
            ],
            hoverOffset: 4,
        }],
    };

    const doughnutConfig = {
        type: 'doughnut',
        data: doughnutData,
    };

    // Crie os gráficos
    const barCtx = document.getElementById('myChart').getContext('2d');
    const barChart = new Chart(barCtx, barConfig);

    const doughnutCtx = document.getElementById('doughnutChart').getContext('2d');
    const doughnutChart = new Chart(doughnutCtx, doughnutConfig);
});
