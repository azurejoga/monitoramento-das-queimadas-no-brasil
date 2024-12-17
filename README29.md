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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c4c7ff4-598f-3a8e-9377-75bb0072da2e | -5.09301 | -43.90534 | 2024-12-17 05:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 697c69f1-e381-3ce3-a976-de451eca67b4 | -6.98935 | -43.55926 | 2024-12-17 05:08:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7abb3678-405a-32bf-bc43-64cf0d15d293 | -5.08442 | -43.91695 | 2024-12-17 05:08:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 30a069db-c5e7-3378-b797-3a04b3e8ee09 | -5.21293 | -43.29971 | 2024-12-17 05:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 36572087-7853-3c24-a2a1-08c64c5e6892 | -3.55601 | -54.7249 | 2024-12-17 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b10896bd-aad1-3f5a-9365-ef87e47ce27d | -3.86826 | -47.03645 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| c6679fd5-c35c-3da7-b8ac-4bf1f0af8f74 | -4.06791 | -46.59159 | 2024-12-17 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e76522d-7839-342b-b060-e779e85ca1d7 | -4.89196 | -44.17514 | 2024-12-17 05:08:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9c81932d-8ad7-3187-a619-41cca1ee819a | -4.04246 | -46.92416 | 2024-12-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 79db4be7-eccc-31f9-9a05-7cb92d8dfce3 | -3.95755 | -46.9302 | 2024-12-17 05:08:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ed6b43b-db43-3f37-a214-22000325cb09 | -3.50093 | -53.94706 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a8b7fe79-13aa-3b28-9e64-39fcefa4fcb1 | -2.94036 | -54.17775 | 2024-12-17 05:08:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15182883-f71e-3534-be4d-5b3c2624822d | -2.08039 | -54.23435 | 2024-12-17 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 232c299f-c942-3f52-8e4b-bd061e04c5cb | -3.50324 | -53.95546 | 2024-12-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d11434c-e8dc-30e8-ace2-cdb5026f58b1 | -4.67827 | -44.04501 | 2024-12-17 05:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d583f8e2-9358-3ca3-8fa8-2d7412042595 | -3.29823 | -53.36412 | 2024-12-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 1e46bde1-a2a0-37e4-90bc-f78a01a46656 | -4.97085 | -44.96754 | 2024-12-17 05:08:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3ed31a75-5dc9-3c98-9ed5-99bb59e70281 | -4.76299 | -46.71315 | 2024-12-17 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0125796-23b7-3101-bf26-ea3f43a2cba1 | -5.0936 | -43.9176 | 2024-12-17 05:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 4cc6435e-c754-38c1-bceb-a5e0189c1f1a | 4.4251 | -60.9851 | 2024-12-17 05:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 200a17ff-dc28-35de-a44f-f3278e6337ac | 4.4435 | -60.9657 | 2024-12-17 05:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 3ab8a99c-536c-3aab-bd5e-b2e035b7621e | 4.4435 | -60.9846 | 2024-12-17 05:10:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 115.3 |
| f6863fe3-9c50-3677-bf77-c5efb793100f | -6.9346 | -43.5168 | 2024-12-17 05:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2c0daf3e-3450-39b1-bfa9-51cf09e87dfa | -6.9349 | -43.4934 | 2024-12-17 05:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| f664ab93-59df-3f11-a107-9ba053c200a3 | -5.0938 | -43.8945 | 2024-12-17 05:10:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| b07e69b1-0a1b-386b-a8de-a8f6f4ea3b46 | -15.07065 | -59.64851 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6170b3aa-b44d-319a-a07d-723d1e2cad6f | -15.07397 | -59.64907 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c33f908-5f48-3fd7-867b-9d10cac4071f | -14.86701 | -59.22008 | 2024-12-17 05:10:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93f78537-1fd1-39a1-ab82-a24b41fd0eb1 | -15.07122 | -59.64494 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 259736a1-b399-3699-aea1-1320382bb5cf | -15.10164 | -59.6464 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b6aefd1-7fa9-3cef-ac60-05d9f2066c71 | -15.08003 | -59.65377 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eebf73a7-f5a5-360f-95c0-da6aa4460838 | -15.09397 | -59.63043 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0ddd549-0023-396a-a151-876c39441f0c | -15.07454 | -59.6455 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d156af91-b8dc-3b1a-9f7b-45bfec539322 | -15.07008 | -59.65209 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcddd38c-b850-3138-8647-e66e29efdeef | -15.71394 | -58.92712 | 2024-12-17 05:10:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a4d3012-7c93-3fc7-9ef8-60562f8b6707 | -15.0806 | -59.65019 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09121ef6-db71-3d59-9382-997606c3a93b | -15.87327 | -53.2709 | 2024-12-17 05:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fdf8f84b-a7fc-38ef-a5b0-6134b508ead9 | -15.07511 | -59.64193 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa312923-96c7-32a2-bad3-ac56b93229cb | -15.87524 | -53.27435 | 2024-12-17 05:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 588daeb5-fbce-337f-86c9-9759345ebe8f | -15.06951 | -59.65567 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21090e86-1f33-39ee-a8a8-983c56c547e0 | -15.88006 | -53.27089 | 2024-12-17 05:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a966d701-90b6-3db1-b63d-d96077d043fa | -15.87145 | -53.26966 | 2024-12-17 05:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ba69b4a7-9952-3d3e-9e90-e8c8f2d03fb9 | -15.0734 | -59.65265 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0fd2e89-4150-3c28-9ba8-ed64921366a7 | -15.07729 | -59.64964 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44234e74-8b53-3002-a45b-9883ce9d929f | -15.87953 | -53.27505 | 2024-12-17 05:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 580fc432-2cab-3902-99ff-55df63c9027c | -15.87575 | -53.27029 | 2024-12-17 05:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a73ed8a3-3c5b-3fd3-8c06-ef6f4d5a73f7 | -15.87757 | -53.27153 | 2024-12-17 05:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37f5ca68-df96-3802-a222-cb05f30d168e | -15.09055 | -59.65187 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8249da7a-dd08-3725-b22d-f5cf6d58f165 | -15.09387 | -59.65244 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5b1a30f-1983-3078-833c-0d939bc86cbf | -15.08392 | -59.65075 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb451b57-865d-3551-88b1-6a30b9fa3874 | -15.24232 | -59.91296 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2862ed1f-466e-36a7-bf77-db7567ce6f96 | -15.0989 | -59.64227 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9f03912-3618-3fe0-bbbf-4cb0f22c8bcb | -15.32491 | -60.0157 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74c14b8a-527c-3b98-a475-b88646ec6ff5 | -15.08724 | -59.65131 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 33557a8e-4634-3f26-80ae-43e8db467e63 | -15.23842 | -59.91599 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e1c3c5e-ec0c-3758-904f-d116f9d36b03 | -15.09444 | -59.64886 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b254187-a7f6-3335-8f08-e369ffc6367b | -15.09112 | -59.6483 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c33327d3-2a25-3e5e-8665-4ec7e0116331 | -15.07283 | -59.65622 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32523d04-c86d-334a-bd7b-6f821f5c3c4e | -15.07786 | -59.64606 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db547939-80eb-3827-bf48-bbf029055a6c | -15.09833 | -59.64584 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2895b63-48d0-380e-9c88-ac8038be844d | -15.07179 | -59.64138 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df683f75-40cb-3d85-8bbd-5bd70893067a | -15.91463 | -59.80869 | 2024-12-17 05:10:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9859ff35-8695-3b6b-b9dc-1a9f0566e4ae | -15.87703 | -53.27561 | 2024-12-17 05:10:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95770551-2ec3-331d-aebf-b74ec7414e02 | -15.07843 | -59.64248 | 2024-12-17 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70f45044-f8d9-367a-a052-e576c18b3416 | -19.09185 | -52.86032 | 2024-12-17 05:12:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8d3c8276-38a7-3db2-8e44-3f6ab7fd62a5 | -17.70272 | -54.08434 | 2024-12-17 05:12:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b91c476-cbe2-3998-a055-723e5138f909 | -18.8999 | -56.05108 | 2024-12-17 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ce3adf4d-1fb8-318d-a5c4-501218b542d4 | -17.70159 | -54.08474 | 2024-12-17 05:12:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa173a1b-ef9c-3b96-9e51-383d8359f063 | -19.0641 | -52.85677 | 2024-12-17 05:12:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e619375f-0f17-3279-9ed1-6fa1a5797a56 | -20.91689 | -56.5475 | 2024-12-17 05:12:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a847a3cc-0297-38e4-81dc-8a0401b98711 | -18.89613 | -56.05052 | 2024-12-17 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 13d5c48b-f37f-3127-9903-79f15135057a | -18.01538 | -54.4299 | 2024-12-17 05:12:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ec56f15-68b8-32ee-a6b4-b2d13917ad97 | -19.29968 | -53.26145 | 2024-12-17 05:12:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d4f1b02-739e-3772-a6b0-6c8b3bec6d48 | -19.09589 | -52.86596 | 2024-12-17 05:12:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| bdd91ad9-c105-3035-960b-23ee1a18f766 | -19.08783 | -52.85462 | 2024-12-17 05:12:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 088d1228-4542-3acc-a5de-17ec05d92cdc | -19.05888 | -52.86135 | 2024-12-17 05:12:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1cf8cca-1618-3713-84c6-92b5ab86a8ca | -19.06873 | -52.85733 | 2024-12-17 05:12:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1dc0dfa5-e146-3662-9141-6ca326c63969 | -19.08723 | -52.85972 | 2024-12-17 05:12:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8da0dc0c-b5ee-308f-acbb-2ae8b5bff7cf | -20.56573 | -55.08881 | 2024-12-17 05:12:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f5e6b79-f33b-3606-9541-3c923f7088cc | -18.89678 | -56.04573 | 2024-12-17 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.9 |
| d198d6a6-eb9c-3043-b83f-52001a86a4f4 | -19.09126 | -52.86536 | 2024-12-17 05:12:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 513b963e-84a4-3c30-b25c-2734f0dabeec | -19.16298 | -54.83684 | 2024-12-17 05:12:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e7650717-fc20-344e-88b9-6a5fa7ba617d | -23.85112 | -50.00737 | 2024-12-17 05:12:00 | NOAA-20 | TOMAZINA | PARANÁ | Brasil | 4127809 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| b83cc859-4a74-3766-9ae7-598ecefbeda6 | -19.30421 | -53.26194 | 2024-12-17 05:12:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce9eca55-a5dd-3bf8-b2c0-ebcdb706e9a4 | -19.05946 | -52.85629 | 2024-12-17 05:12:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4673c678-ad64-32df-8f00-25c4ea2131ab | -18.90055 | -56.04629 | 2024-12-17 05:12:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 46854165-0ddf-31be-b54a-c8df47a12e26 | -24.24375 | -50.74226 | 2024-12-17 05:14:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b2d05d6a-bd72-3c4f-913e-251b60fe6011 | -6.9346 | -43.5168 | 2024-12-17 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 6eb99e07-7af6-3c7a-b7ad-d791210b2d00 | -6.9349 | -43.4934 | 2024-12-17 05:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 99996b0f-11a3-39c5-9503-15a7d110af35 | -5.0936 | -43.9176 | 2024-12-17 05:20:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 94751f5b-36c6-3e29-ab6c-2789cc6bacf8 | 4.4435 | -60.9846 | 2024-12-17 05:20:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 43887416-d66f-36d8-b470-0129110271e5 | 4.4435 | -60.9846 | 2024-12-17 05:30:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 1908575e-d1c2-390b-90be-a18f0b82e1bb | -5.0936 | -43.9176 | 2024-12-17 05:30:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| c57eb070-d7fe-34a1-9798-b3780c4556b8 | -3.2968 | -53.3749 | 2024-12-17 05:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 7622e8c5-4c6b-37dc-b508-f99dea27649a | 4.4618 | -60.9842 | 2024-12-17 05:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 3104758a-f338-3fa2-902d-ea7f03d1a679 | -3.2968 | -53.3749 | 2024-12-17 05:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4fb160a3-9c7e-3b3c-aad2-9d3499f9e4f1 | -5.0936 | -43.9176 | 2024-12-17 05:40:00 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 0e31939c-12b1-3454-a0da-0790402bfab9 | 4.4435 | -60.9657 | 2024-12-17 05:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| b3e0a101-7438-30f7-bbdb-a183f4c3ad85 | 4.4435 | -60.9846 | 2024-12-17 05:40:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 7dacd57f-a0cc-3791-a21e-adb590dc81c2 | 4.4251 | -60.9851 | 2024-12-17 05:50:00 | GOES-16 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |


[Clique aqui para ver as próximas entradas](README30.md)
