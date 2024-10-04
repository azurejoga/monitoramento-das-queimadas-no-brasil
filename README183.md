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

## Dados Diários - Página 183

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10391070-d728-3797-b0ad-35110093ec1b | -17.1577 | -57.3787 | 2024-10-04 07:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| 3e591c71-b452-39d1-8ba1-6da096bc594c | -19.5104 | -42.8691 | 2024-10-04 07:26:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 218.6 |
| 77091306-cd55-306d-b58b-1769b8583630 | -19.5096 | -42.8942 | 2024-10-04 07:26:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 123.1 |
| 18c9fc65-f534-3143-832f-6faffca0d85c | -19.4899 | -42.8746 | 2024-10-04 07:26:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 180.8 |
| a63594dd-e73b-343c-b540-5b63375156f2 | -19.4891 | -42.8997 | 2024-10-04 07:26:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.9 |
| 4277d669-6549-338c-a884-df96296eab2f | -20.5412 | -48.6157 | 2024-10-04 07:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6979961b-5157-381d-96c5-7784583af19b | -20.5207 | -48.6203 | 2024-10-04 07:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 1e6e9a30-5126-35a2-b2bd-709002e6e868 | -20.5201 | -48.6435 | 2024-10-04 07:27:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 12b2817a-e373-33d0-83b1-0d80c40e95eb | -22.4718 | -50.1303 | 2024-10-04 07:27:10 | GOES-16 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 159.8 |
| b9c16bc1-ec1f-3f5c-94a9-e38c6caaf30f | -22.4725 | -50.1072 | 2024-10-04 07:27:10 | GOES-16 | ECHAPORÃ | SÃO PAULO | Brasil | 3514700 | 35 | 33 | nan | nan | nan | Cerrado | 113.7 |
| ee152356-9d2d-3012-8e16-ec2f4eaa5f19 | -11.8242 | -56.6009 | 2024-10-04 07:36:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| f2676e15-74ab-3780-88a6-8073d25deaae | -12.5711 | -53.1171 | 2024-10-04 07:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 8865ca38-0d3c-389f-864c-08d15cba25fb | -12.5898 | -53.1359 | 2024-10-04 07:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 43bf7e60-171b-39f7-b0ec-a1bbe476cddb | -12.5901 | -53.115 | 2024-10-04 07:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| dd373eb4-3a05-34b0-ba92-4801c57cd558 | -12.6089 | -53.1338 | 2024-10-04 07:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 02089216-fb88-31d5-ae0e-14bbb1f200be | -12.6092 | -53.1129 | 2024-10-04 07:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 67406c8c-ba19-3c93-9792-4ea5e8e57f51 | -12.653 | -54.0622 | 2024-10-04 07:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| fbaba255-709f-3f4e-9497-b7b15d9a466d | -12.6532 | -54.0415 | 2024-10-04 07:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 6b4a1a9f-8a9d-31cc-975e-d7b584c6de82 | -12.6723 | -54.0395 | 2024-10-04 07:36:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| c42a7174-3560-31d9-a41d-8d52032a1f22 | -16.5938 | -57.1783 | 2024-10-04 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 488d1c5c-43f2-3803-b3c6-8b1ad01fd7de | -16.613 | -57.1965 | 2024-10-04 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.8 |
| 8926ed27-eae4-3805-a03c-735ace1287a4 | -16.6133 | -57.176 | 2024-10-04 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.5 |
| c6ea3206-47ab-355a-a82c-8beacbfba22c | -16.5935 | -57.1988 | 2024-10-04 07:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.8 |
| c3c7d3f9-aad4-3363-817d-dc844d3f91c6 | -17.0113 | -56.7392 | 2024-10-04 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 51.1 |
| 9b9012f8-6e93-3db8-ad88-0777091cd39d | -17.011 | -56.7598 | 2024-10-04 07:36:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.7 |
| b3a804b9-5dca-3f6c-b47d-90e9ddd1cd65 | -17.1577 | -57.3787 | 2024-10-04 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 25719a5f-c862-311d-8b68-411b7b5d369e | -17.1574 | -57.3993 | 2024-10-04 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| 8134b402-cfe9-3373-b630-6364ec9da11d | -17.1378 | -57.4016 | 2024-10-04 07:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.8 |
| 2ff24584-e8d0-3e84-a6b7-8ea529947ea8 | -19.4891 | -42.8997 | 2024-10-04 07:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| dfb8dd9d-473a-31cb-9f70-f6cd454cf719 | -19.4899 | -42.8746 | 2024-10-04 07:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.9 |
| b744db9b-ff1c-3820-bc3f-d298996cf36a | -19.5096 | -42.8942 | 2024-10-04 07:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 58.6 |
| 74c4714c-42f6-3317-97f8-3b0c0cff963e | -19.5104 | -42.8691 | 2024-10-04 07:36:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 107.3 |
| 0da54806-5c43-393a-b8cf-7db6efdd7239 | -20.5207 | -48.6203 | 2024-10-04 07:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 5e042c72-4b19-3d7b-a96a-8894a35e54f1 | -21.3301 | -48.9207 | 2024-10-04 07:37:04 | GOES-16 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 6f123643-3e14-3eb7-a731-f876a9b6b2bc | -21.3308 | -48.8974 | 2024-10-04 07:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 132.6 |
| b544a050-38d8-391c-b2c4-c166a4051cea | -21.3508 | -48.9159 | 2024-10-04 07:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 957fa2b4-10c4-3f6c-85e1-8a66ca40a880 | -21.3514 | -48.8927 | 2024-10-04 07:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 5edc76b5-be7f-3811-8902-1e3109611bf6 | -21.3521 | -48.8694 | 2024-10-04 07:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 73336891-99a0-39b6-8853-2e62ab22fb12 | -21.3721 | -48.8879 | 2024-10-04 07:37:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 1a52536d-db16-325c-a462-e34ce5562d31 | -21.7988 | -48.3691 | 2024-10-04 07:37:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 7bac5e07-c9d8-3810-a6e0-d953e1bab6a0 | -12.5898 | -53.1359 | 2024-10-04 07:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 17db4230-3ff6-351e-923a-cf610b46f3cd | -12.5901 | -53.115 | 2024-10-04 07:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 6ab87aa8-2ca3-3526-86b8-8f0027e3c088 | -12.6092 | -53.1129 | 2024-10-04 07:46:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| f3540545-8ecc-3c18-b363-d4e8df76b5fa | -12.6532 | -54.0415 | 2024-10-04 07:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 16e252c3-c82e-34d5-a6d8-5d9eb96474c0 | -12.672 | -54.0602 | 2024-10-04 07:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 33cbe833-e2de-3be3-a2b0-ccef225cfcc2 | -12.6723 | -54.0395 | 2024-10-04 07:46:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| f83ab4da-c704-3c1e-8ec3-09e0529cd1a6 | -13.0978 | -51.1361 | 2024-10-04 07:46:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| f9bbc002-4236-355a-8912-77506bb3e451 | -16.5938 | -57.1783 | 2024-10-04 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.2 |
| 5591e10f-244b-37c8-beb5-fbedb90aa0b2 | -16.613 | -57.1965 | 2024-10-04 07:46:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| 2bca69a7-c3a7-32e7-be9b-c5dd5a89c650 | -17.011 | -56.7598 | 2024-10-04 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 41.0 |
| 78552269-1bb8-3d89-8a58-0ddf6b4c569e | -17.0113 | -56.7392 | 2024-10-04 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 56.9 |
| 1550eb38-ac7a-3d3a-be9d-ed800ebad795 | -17.1085 | -56.7892 | 2024-10-04 07:46:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 36.0 |
| 014fb614-1ba0-3c5b-a306-f0b12b48482c | -17.1577 | -57.3787 | 2024-10-04 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 4181466a-6739-373d-8f9c-acb596525249 | -17.1574 | -57.3993 | 2024-10-04 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.8 |
| 1c265fb2-0fb0-312e-8d4c-0b046fc5c52f | -17.1378 | -57.4016 | 2024-10-04 07:46:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.9 |
| 5d363054-6c46-3300-bc03-ab585dda8c56 | -19.5104 | -42.8691 | 2024-10-04 07:46:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.0 |
| fa887922-e6fa-3950-bb7c-66799191970a | -20.5201 | -48.6435 | 2024-10-04 07:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 389cdd74-d0ef-38a1-94a3-04a3a2e1d845 | -20.5207 | -48.6203 | 2024-10-04 07:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 276.7 |
| e164d39d-feeb-3616-9526-e1e5925df0c7 | -20.5406 | -48.6389 | 2024-10-04 07:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 95252184-c3b6-335a-80b8-8477886660cd | -20.5412 | -48.6157 | 2024-10-04 07:47:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 282.4 |
| b19170e2-8f44-32bb-8f1b-3b87e88576f6 | -21.2895 | -48.907 | 2024-10-04 07:47:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 004e4937-46d8-37a6-8c38-e582cfc11246 | -12.5711 | -53.1171 | 2024-10-04 07:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 1b179c90-593b-3b75-be71-a0e43a134bf3 | -12.5898 | -53.1359 | 2024-10-04 07:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 19f3f3a3-8404-350c-ba8b-138de9570d4a | -12.5901 | -53.115 | 2024-10-04 07:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 109.0 |
| b90909a8-11b4-38fc-8172-991662ea4ea4 | -12.6092 | -53.1129 | 2024-10-04 07:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 2b9fc180-0ced-3233-a300-6846364ea855 | -12.6723 | -54.0395 | 2024-10-04 07:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6c44755c-de2b-3b9c-99b2-d309aa7fed31 | -13.0598 | -51.1195 | 2024-10-04 07:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 3d533b59-6670-3770-865b-5abebdb9bdf0 | -13.0786 | -51.1385 | 2024-10-04 07:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 9553adca-d24e-3c83-95ba-8a1b9cdd646b | -13.079 | -51.1171 | 2024-10-04 07:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 751f305d-0b0f-3478-b4a1-7f5f8e481e48 | -13.0793 | -51.0956 | 2024-10-04 07:56:20 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| ee3f4041-02ac-3066-9c36-9cc1b8db291c | -16.5726 | -57.2829 | 2024-10-04 07:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| 0aaa6c31-b7df-3f76-937b-a5e6150ee0e7 | -16.5938 | -57.1783 | 2024-10-04 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.5 |
| 0e88326b-25c9-3e43-b60a-b865cc948d7c | -16.613 | -57.1965 | 2024-10-04 07:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.1 |
| 11d3c514-f4f4-3d83-96b8-ed8ec485bb9f | -17.1085 | -56.7892 | 2024-10-04 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.6 |
| 847004c9-2566-3170-a09a-11eed4cef7ef | -17.0113 | -56.7392 | 2024-10-04 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| a6e148b6-1ed6-3e9c-a0cc-4f9d8a028710 | -17.011 | -56.7598 | 2024-10-04 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 40.8 |
| 615c01b4-8de2-389c-bdf9-ecd1227e0981 | -17.1577 | -57.3787 | 2024-10-04 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 40.3 |
| 67ae75d8-a607-35c6-b324-84453957c40c | -17.1378 | -57.4016 | 2024-10-04 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.5 |
| b9881bf1-c736-32da-90b1-bd69b0320771 | -17.1574 | -57.3993 | 2024-10-04 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.1 |
| 884432b4-a1b9-3bb4-8f7c-ca1853bbdb05 | -20.5207 | -48.6203 | 2024-10-04 07:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 104.0 |
| bc6f7717-1c13-3b5d-bc74-00bb3c5dcf23 | -20.5412 | -48.6157 | 2024-10-04 07:57:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 8fbee015-86ad-35bf-b7a3-b39f3e7c5d63 | -10.45 | -50.76 | 2024-10-04 08:04:27 | MSG-03 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 362a83e7-a8bd-32db-8f7c-2d84e4ddc601 | -12.5901 | -53.115 | 2024-10-04 08:06:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ca5cd6ac-42bf-32d5-b5ad-0d9dc6bb0a7a | -12.6092 | -53.1129 | 2024-10-04 08:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 703b1595-5db1-3211-818e-f2626797e313 | -12.6532 | -54.0415 | 2024-10-04 08:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 79f6e3f8-d685-3cdf-abe0-c8e22ba09eea | -13.0786 | -51.1385 | 2024-10-04 08:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 95f6e3b8-c758-3309-957f-3da581cbf717 | -13.079 | -51.1171 | 2024-10-04 08:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| a19c054b-1e7e-31e8-9a13-987bf11905da | -16.5531 | -57.2851 | 2024-10-04 08:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.9 |
| 31250015-7bd3-3d89-bb97-a1920c0717d1 | -16.613 | -57.1965 | 2024-10-04 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| ec0420b9-baff-32ef-9396-80b1d7836fbd | -16.5938 | -57.1783 | 2024-10-04 08:06:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.6 |
| ea9f0efc-ec4f-339c-9a63-d6a17ca796bb | -16.5726 | -57.2829 | 2024-10-04 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.4 |
| 80199fbb-003d-3c08-91ae-b1091041801d | -16.5723 | -57.3033 | 2024-10-04 08:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.6 |
| 649fe7cd-5f2b-35e3-9089-f9b27e772245 | -17.0113 | -56.7392 | 2024-10-04 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 49.0 |
| f8d509f5-ead4-38de-9a5a-f1731526783c | -17.1577 | -57.3787 | 2024-10-04 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.7 |
| f45765b4-0973-3974-8981-f91ea7dd43fc | -17.1574 | -57.3993 | 2024-10-04 08:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| 55d7799e-3523-32a1-b115-0cd9ccdd02ef | -20.5207 | -48.6203 | 2024-10-04 08:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 8efc60f8-9a87-3f1a-b3dd-1d47f1eb70c2 | -20.5412 | -48.6157 | 2024-10-04 08:07:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 70.5 |
| d52c9f3c-7b38-3c8e-a2a0-0138be6404f7 | -11.8242 | -56.6009 | 2024-10-04 08:16:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a8424b1c-2fef-3d1c-9b0e-bca8caf9e9f8 | -12.5901 | -53.115 | 2024-10-04 08:16:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| a9f45b99-0ad4-31af-a5e8-3289314b09c7 | -12.6092 | -53.1129 | 2024-10-04 08:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |


[Clique aqui para ver as próximas entradas](README184.md)
