# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 181d28a7-b56d-3363-9d71-634d2c4df05e | -9.42293 | -65.46364 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 37f88dc3-ccb7-3545-81c7-bda1fc92ef6e | -9.42122 | -65.45189 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b83b8dc-82ad-342e-a57d-0bc1559b5431 | -9.42065 | -65.45563 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9eca210e-6c67-3a64-8da4-6dc4df49dffe | -9.3435 | -65.7325 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d06f7c6f-9f5a-3cf6-ab81-b2335e9040f6 | -10.32634 | -64.54652 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1eed03d-a03a-3538-ad29-23569d7c87a8 | -10.09311 | -64.47359 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4e77c1e-5867-31ab-ab0c-58f3ccd8b42b | -10.08951 | -64.47306 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06bcb99b-3584-39f7-83af-1cf92e9608f0 | -10.08231 | -64.47203 | 2024-09-26 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 457f1737-f6dc-3bef-a7a1-2795ba82537d | -9.42759 | -68.99812 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ba1da55-8d0e-367f-8448-fb198f3f92f2 | -9.42421 | -68.99757 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cbae31a-9cee-3b1f-9a74-9ca1c2d14b9d | -9.42317 | -68.99776 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 775ead94-ea43-3b5f-8d3a-3e2080fb80b8 | -9.38683 | -69.02942 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 437b077a-1ab9-3b76-ae6c-1e406d4cc0dc | -9.36473 | -69.03706 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab028ad8-a236-3207-bf61-f3e57fc8eaf8 | -9.36134 | -69.03651 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3151b19b-e51b-38d9-8960-77ecf4e0a967 | -8.94667 | -68.93233 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67c21382-7156-3a81-bdef-6ed3b77b2be0 | -8.78462 | -68.91725 | 2024-09-26 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c347ffd-b4f2-3274-8c92-018a4ae21104 | -8.78403 | -68.92091 | 2024-09-26 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e77e001b-e199-3446-b651-6a1f6a615272 | -8.78343 | -68.92458 | 2024-09-26 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe71e96e-cc4a-37f6-9359-d9c848be9cc2 | -8.78319 | -68.92117 | 2024-09-26 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a501ff6-cbf1-3bb9-b501-2d402b204f25 | -8.78261 | -68.92484 | 2024-09-26 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c25183a7-01d0-305e-8958-1b38d4b6b505 | -8.77099 | -68.97575 | 2024-09-26 05:48:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4c78b9d-b283-3320-b8e7-dda8bcb0c704 | -8.7704 | -68.97942 | 2024-09-26 05:48:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aca60b83-d2ca-36cc-a55d-02fc1be9eae1 | -8.7676 | -68.9752 | 2024-09-26 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7cd2fddf-b2b7-3cc1-8c22-9ce579ad6b17 | -8.5142 | -70.25126 | 2024-09-26 05:48:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0a95552-fef6-389d-909e-49c2e0b568df | -9.64836 | -68.99973 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 043704a5-655c-3a44-99bf-fc57a0a84f91 | -9.64777 | -69.00338 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2603cd8-e347-348a-ba4c-9f9645954807 | -9.64498 | -68.99917 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5338843c-3d78-3993-bf5b-685f9f430328 | -9.64439 | -69.00283 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9cc6be0b-dbc9-3163-bb07-095624426eb2 | -9.6422 | -68.99498 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b236587d-e27f-3772-9eb1-435733cbc360 | -9.6416 | -68.99863 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73bed92c-57f8-3563-b33d-62ee86d1ab24 | -9.64091 | -68.99578 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01e2822f-9f68-35f0-93b0-6317e13115a6 | -9.64033 | -68.99944 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fbd1e1b-ea4b-31bf-8635-e62a83286329 | -8.40792 | -70.75703 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 97d8e774-5258-398c-8aa1-2645201546d3 | -8.40719 | -70.76141 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bb5754bc-ea51-32b2-a5c7-83b8fb31cdd0 | -8.39024 | -70.81734 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c797808-0c63-3ece-b3bb-8130b81030b2 | -8.33321 | -70.91876 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77961cc5-4100-3de6-bddb-2499de08912e | -8.28269 | -70.85516 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c315237-e1e3-3021-b37f-5efe6dbc6678 | -8.24404 | -70.84696 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50c49144-9eb5-34db-8a2c-95472df37e90 | -8.15122 | -70.92289 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f0ce4ac2-f58e-3b9f-baf1-35fc6ba3ead7 | -8.40424 | -70.75641 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e2b2156-5aed-3b8c-a6dd-1d8e75b2767d | -8.40351 | -70.76079 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2b77106-bd67-3330-8936-b83b292d3850 | -8.38951 | -70.82172 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe458b24-f1fe-3f29-bd2b-d2566ba769e7 | -8.25965 | -70.87881 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cfbbed1-5bff-367b-a5c1-d798ebe5e5ea | -8.02902 | -71.02534 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aa617d6-9765-3505-9684-2d1006829bdc | -8.02527 | -71.02469 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8a498c5-0982-3c1b-a40f-dea74589318a | -7.84407 | -72.77326 | 2024-09-26 05:48:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b31e8283-34c8-36f7-8896-ab5d3bfd8aad | -7.83988 | -72.77248 | 2024-09-26 05:48:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8595357d-f314-3f87-8b0b-0e685760d392 | -7.83568 | -72.77173 | 2024-09-26 05:48:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d783c834-f150-3add-b38d-3266be470f3d | -7.79949 | -72.8302 | 2024-09-26 05:48:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86c0d8e1-343e-3ddd-ac1d-859c61d6c882 | -7.79613 | -71.9531 | 2024-09-26 05:48:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ab70b25-0bd5-3dbc-b610-851e08e5f784 | -7.72605 | -72.77735 | 2024-09-26 05:48:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bbabe9b2-14a8-3f46-92ef-889643b89aa7 | -7.72252 | -72.77268 | 2024-09-26 05:48:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8c89f259-d451-3d8a-adb1-b43cc97f896c | -7.72183 | -72.77665 | 2024-09-26 05:48:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4975762b-d3fc-376c-ac2d-839da139cfd1 | -9.21815 | -67.00789 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5bbdfcc-3f3c-32b6-ba07-0f7d26ae6400 | -9.18504 | -67.04516 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9dc83dc6-8e20-396a-9e3e-3b0e26d22cef | -9.18449 | -67.04864 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fdc62ea0-4e0a-39d7-a05e-de077817cbee | -9.18118 | -67.04812 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b70fc727-862c-3541-bcf6-44a00cd5cc28 | -9.14846 | -65.88225 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0175eac-17ba-3324-bdff-586b616e3bd9 | -9.14028 | -66.19444 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdfda26b-d119-3b2f-a59e-28f0edb3ad44 | -9.05042 | -66.20589 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac1ffe7e-631e-3fa6-8aae-73c46d9ba9db | -9.04987 | -66.20948 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4bcc39c-d667-3987-abac-902430a9b817 | -9.04652 | -66.20896 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbfeb0d9-a86a-3a88-930b-4949c5e835fd | -9.0427 | -67.04411 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3ff5494b-be0e-3f8f-8c89-92690966fef1 | -9.04215 | -67.04759 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56760ccf-2421-3f2b-97c7-d42f7c2d6484 | -9.03662 | -67.03957 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c13939c-f8bb-30b3-884a-02e6330efc62 | -9.01858 | -66.18997 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49d60414-613c-3891-97a1-8ffdc2b46364 | -8.98952 | -65.87344 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97392b39-3fb5-31e5-8879-8290be083ebd | -8.98785 | -65.8843 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab5d4b53-be24-3f87-ba57-846b4704f08f | -8.94986 | -65.95242 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2aba09b3-1ded-34a8-9c8b-a806d1bb4f05 | -8.80216 | -66.67013 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6e9b9f32-e851-33ca-85ae-db4328867184 | -9.14509 | -65.88172 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5644225a-5842-3a13-852d-77f32fc4afb0 | -9.90219 | -67.04099 | 2024-09-26 05:48:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d82796f0-dd90-33cd-a361-b918debff4fc | -9.86888 | -66.97105 | 2024-09-26 05:48:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0649cb93-71fb-3d29-b005-d59680549b0d | -9.86833 | -66.97456 | 2024-09-26 05:48:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82ab8a54-7562-30e3-b773-1a8186d31c17 | -9.71193 | -66.84534 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aadd3548-d03f-3f07-9616-5e04df346ee6 | -9.6374 | -66.84416 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 778cd4ef-3c71-384a-8b35-e9ff44d2499d | -9.63686 | -66.84767 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73031710-6959-305a-aa95-f8b6c60ab72d | -9.5565 | -66.03026 | 2024-09-26 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb440cce-391e-3ee1-bfec-5afc64be4db2 | -9.51084 | -66.76311 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8856b492-c12c-3508-b7c6-a4627344ce8a | -9.51029 | -66.76663 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 021a8a28-6868-302c-bd62-f26a7c62af75 | -9.50751 | -66.7626 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0269a983-3df4-36be-9ba3-38c77e3a0505 | -9.50697 | -66.76611 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e701afc4-baca-3040-ad25-a0953729cb9b | -9.50419 | -66.76207 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7c6b3c50-befd-373c-84c0-9331c21f8eff | -9.50365 | -66.76559 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04d36f3c-ad86-3017-a025-1b4c4ca60156 | -9.47918 | -66.72573 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ee923dd8-3f19-37a8-996e-fee88130d5ca | -9.47864 | -66.72926 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9443092f-1f4c-3ce9-9c31-16b8836a5b9b | -9.47531 | -66.72872 | 2024-09-26 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8e2be7d-c178-3e39-9aa5-e336e028ac92 | -9.83499 | -68.81821 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96742291-112f-3fb7-af9f-b1926a829821 | -9.83163 | -68.81764 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c20d5cc-3865-3d07-a5ff-076fae3025cc | -9.81484 | -68.81487 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ef279ff-cf9c-3baf-9ef7-58b733ca7c9c | -9.81206 | -68.81071 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34862a35-b3f6-3ab9-914c-12a6b2c818ab | -9.81148 | -68.81432 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2978133f-25d8-3529-aed7-ca9310357e3d | -9.8109 | -68.81792 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 341d515e-4415-3160-b12a-4c23bac8b731 | -9.81031 | -68.82153 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd35ee81-2543-35b5-aa66-490bb76e80f6 | -9.80973 | -68.82516 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c88ef220-e148-3309-b88e-8224161ec3c9 | -9.80695 | -68.82098 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4698d346-9aac-3f06-b866-c5505ab79816 | -9.41878 | -68.87363 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84ad929e-02fe-3752-8076-04b9df97c029 | -9.4182 | -68.87727 | 2024-09-26 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ebdf95a5-20aa-34d4-91f6-1ef575c82a66 | -10.22837 | -68.75623 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e5acf5d-94da-361b-aec3-11ce408498f1 | -10.22445 | -68.75924 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README167.md)
