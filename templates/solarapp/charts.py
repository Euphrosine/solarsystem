{% block content %}
<br>
<h3>Charts</h3>
<div class="row mt-5">
    <div class="col-md-6">
        <h4>Tem Chart</h4>
        <canvas id="temperatureChart" width="400" height="250"></canvas>
        <script>
            const temperatureLabels = {{ temperature_labels| safe }};
            const temperatureData = {{ temperature_values| safe }};

            const temperatureConfig = {
                type: 'line',
                data: {
                    labels: temperatureLabels,
                    datasets: [{
                        label: 'Temperature',
                        data: temperatureData,
                        fill: false,
                        borderColor: 'rgb(75, 192, 192)',
                        tension: 0.1
                    }]
                }
            };

            const temperatureChart = new Chart(
                document.getElementById('temperatureChart').getContext('2d'),
                temperatureConfig
            );
        </script>
    </div>

    <div class="col-md-6">
        <h4>Humidity Chart</h4>
        <canvas id="humidityChart" width="400" height="250"></canvas>
        <script>
            const humidityLabels = {{ humidity_labels| safe }};
            const humidityData = {{ humidity_values| safe }};

            const humidityConfig = {
                type: 'line',
                data: {
                    labels: humidityLabels,
                    datasets: [{
                        label: 'Humidity',
                        data: humidityData,
                        fill: false,
                        borderColor: 'rgb(255, 159, 64)',
                        tension: 0.1
                    }]
                }
            };

            const humidityChart = new Chart(
                document.getElementById('humidityChart').getContext('2d'),
                humidityConfig
            );
        </script>
    </div>
</div>

