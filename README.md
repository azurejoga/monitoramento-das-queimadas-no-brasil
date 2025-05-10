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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdd2e49d-33fd-3619-9908-b319ad8ab830 | -13.9902 | -56.8058 | 2025-05-10 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 97.6 |
| ac82bb0a-dd54-3af5-a42d-6a803903dabd | -13.971 | -56.8077 | 2025-05-10 00:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| d6169fae-f37e-35fc-937a-3e58d3abf282 | -12.6816 | -44.3442 | 2025-05-10 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 52.1 |
| a8f2f39c-92da-32b1-89e5-e9bc55702e9a | -12.6821 | -44.3206 | 2025-05-10 00:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| dcf467b7-bed4-34dc-9d34-b3f9c065097e | -6.9592 | -42.9994 | 2025-05-10 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 191.9 |
| 24dd45ef-2d2b-352d-9654-d1fa1b696d19 | -6.9398 | -43.0483 | 2025-05-10 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| ab09296a-562d-3c8b-8ee1-4fdc4b96c40f | -6.9586 | -43.0465 | 2025-05-10 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 7891b7a9-7c1d-39d0-9507-49876830ba09 | -13.971 | -56.8077 | 2025-05-10 00:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 7708bc3c-4d73-3a93-9b68-355e15fc7918 | -6.9403 | -43.0012 | 2025-05-10 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 109.4 |
| b4bafa49-5c77-3f7c-91b4-11d9a827bbcd | -6.9589 | -43.023 | 2025-05-10 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 378.4 |
| b175143b-5be0-3a64-bb23-5b0820991053 | -6.9401 | -43.0247 | 2025-05-10 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 226.7 |
| 75c1f4a1-46aa-3604-967e-53b531ea9a09 | -13.9902 | -56.8058 | 2025-05-10 00:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 95157a3b-9b42-32c6-b9f7-3087a1831fdb | -12.6821 | -44.3206 | 2025-05-10 00:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| c31e8857-c624-3198-8e80-08b3779dee92 | -13.971 | -56.8077 | 2025-05-10 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 170dbce7-eadc-3dda-bb7e-24b042a9decb | -6.9586 | -43.0465 | 2025-05-10 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 432421be-1ef7-31a3-aa07-e7b3762b1c74 | -12.6821 | -44.3206 | 2025-05-10 00:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 9a9ec329-6201-3fd7-bcca-6dcc4a4f78b5 | -6.9589 | -43.023 | 2025-05-10 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 325.0 |
| b2edbc65-9966-3494-adbf-1cbeb14bec0c | -13.9902 | -56.8058 | 2025-05-10 00:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 58cd6fdc-d0c3-35f5-b5a2-3f13b6996ed3 | -6.9592 | -42.9994 | 2025-05-10 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 154.5 |
| bdc52a5d-64e2-3ece-9214-a527d4b62ab5 | -6.9403 | -43.0012 | 2025-05-10 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.0 |
| 7821faf4-7660-39d2-b1fd-a0af7da0b790 | -6.9401 | -43.0247 | 2025-05-10 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 179.5 |
| 72ab5305-9ebf-33d1-ba27-4e7cb38bd961 | -6.9398 | -43.0483 | 2025-05-10 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 287b9825-7b0b-3d98-8c16-7d5fa500374a | -13.9902 | -56.8058 | 2025-05-10 00:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 45c96829-d17d-31d1-97ef-720ef3199c22 | -13.971 | -56.8077 | 2025-05-10 00:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 53.3 |
| b85c8c1b-19c3-3d3b-b54d-1f3fba2f69c2 | -13.971 | -56.8077 | 2025-05-10 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 60a28a78-4506-37b6-b8c1-540caaa29245 | -6.9589 | -43.023 | 2025-05-10 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 316.8 |
| 6a655166-c45a-3742-ba76-7d4a9afaf9bc | -6.9586 | -43.0465 | 2025-05-10 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 6292b1c3-9cfd-3550-ae23-925499d52df3 | -6.9398 | -43.0483 | 2025-05-10 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 62.0 |
| f0de9bba-a0ab-3a5e-8f84-f61d8584f65c | -6.9592 | -42.9994 | 2025-05-10 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 148.0 |
| 2da54f7f-a3b9-378b-b108-10540323eb26 | -22.6377 | -47.3798 | 2025-05-10 00:40:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 1a7fc3f6-6958-37e5-a7b8-d4db4fe075db | -13.9902 | -56.8058 | 2025-05-10 00:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 85cd8671-f111-314c-965c-eb15f2619a01 | -6.9401 | -43.0247 | 2025-05-10 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 136.2 |
| b7c414c7-42c2-3f4f-9f9c-3a9810f7e5c4 | -6.9403 | -43.0012 | 2025-05-10 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 74.4 |
| 18170d77-e84c-3300-9619-e8980dc15ffe | -22.6587 | -47.3742 | 2025-05-10 00:40:00 | GOES-19 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 8fa4d138-3810-3dfa-9815-74134b309cd4 | -13.971 | -56.8077 | 2025-05-10 00:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 50af2da7-70c4-3ab3-86fa-c373143e98fb | -6.9589 | -43.023 | 2025-05-10 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 215.2 |
| 9243e45a-f08c-35e4-bd14-68ff80cd7c9d | -13.9902 | -56.8058 | 2025-05-10 00:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 3479b038-9b8f-31f2-9a1f-6520bc08b09a | -6.9592 | -42.9994 | 2025-05-10 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 118.7 |
| b7a1c333-ce1c-3474-9e19-9b3dbbbd2592 | -6.9403 | -43.0012 | 2025-05-10 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 9bca1a7e-828e-3a57-8538-49292afa8ed4 | -6.9401 | -43.0247 | 2025-05-10 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| ca44b903-3bad-36fa-8d42-44f624c7cbab | -6.9586 | -43.0465 | 2025-05-10 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 4a9620d9-9f49-303d-badc-d7c11dfaecae | -6.9589 | -43.023 | 2025-05-10 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 177.4 |
| c88aeee7-9b6b-3e50-9a42-54b434976b68 | -6.9592 | -42.9994 | 2025-05-10 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| dac9076e-2ddb-38c2-8ad8-f7c3caeb77e8 | -6.9401 | -43.0247 | 2025-05-10 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.3 |
| d034568a-da0b-3476-92c0-7d5750ec5231 | -13.9902 | -56.8058 | 2025-05-10 01:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 17e1a5fa-4219-3cf6-9f9b-2d257e6e62b7 | -13.971 | -56.8077 | 2025-05-10 01:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 9c7d6f28-382c-3b00-ae5a-bfa7fc86dd07 | -6.9403 | -43.0012 | 2025-05-10 01:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 068bab9e-4cf4-30aa-b223-0480811a5482 | -6.9403 | -43.0012 | 2025-05-10 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 163c5803-a587-32c7-a947-4f11b5a30fc4 | -6.9589 | -43.023 | 2025-05-10 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 221.4 |
| f740c604-2e6c-37f9-992c-b16d04632451 | -13.9902 | -56.8058 | 2025-05-10 01:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 77b80e1a-65de-3a07-80d7-836c1350d41f | -8.6973 | -64.1365 | 2025-05-10 01:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 1999c43e-95e3-3f59-a3e2-d28116dda0ea | -6.9592 | -42.9994 | 2025-05-10 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 512690c5-f79c-3f6c-b853-3fef98a757e8 | -6.9586 | -43.0465 | 2025-05-10 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 16ce35a0-41b8-3f4d-a2fd-976b27d07efa | -6.9401 | -43.0247 | 2025-05-10 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 55a9e871-1f44-3d1b-80e1-4ebb503c7178 | -13.9902 | -56.8058 | 2025-05-10 01:20:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| ee6b4c90-68fe-3dff-a381-b74aae2ad36d | -6.9592 | -42.9994 | 2025-05-10 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.4 |
| 6231b5b5-ddbe-3d6e-b3df-a4ff6019404d | -6.9589 | -43.023 | 2025-05-10 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 205.1 |
| 5cd0b307-7dc2-35c4-8f64-ac094660485c | -6.9403 | -43.0012 | 2025-05-10 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.9 |
| 366a6128-53b4-3001-ba5c-824f9c2dcfcf | -6.9401 | -43.0247 | 2025-05-10 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| ba3f9547-0a45-3354-b65f-777b72fe8d02 | -8.6973 | -64.1365 | 2025-05-10 01:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 18ff8969-6c07-3603-ba36-248b7001b283 | -6.9401 | -43.0247 | 2025-05-10 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| dc302829-1d90-3308-9232-a903b1c2d362 | -8.6973 | -64.1365 | 2025-05-10 01:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 857a1c1b-01a5-3664-855d-40ce822e076a | -6.9592 | -42.9994 | 2025-05-10 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 328a74ad-c2a0-3d03-a724-7fb8a3f9ad4b | -6.9586 | -43.0465 | 2025-05-10 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 68cc4740-ed22-346b-8433-4d934ac0e182 | -6.9589 | -43.023 | 2025-05-10 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 159.1 |
| d9ed2583-e00f-3c7f-bea4-4e08eaf76b66 | -6.9403 | -43.0012 | 2025-05-10 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.0 |
| a1465f19-dfdd-3de0-8091-c25e66ae5fca | -13.9902 | -56.8058 | 2025-05-10 01:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 0e3245da-8598-3859-9905-7176e577db75 | -13.971 | -56.8077 | 2025-05-10 01:30:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 7b103817-c98d-397f-893d-bb19162c0bea | -19.05544 | -53.4603 | 2025-05-10 01:30:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 45e26887-734e-3869-b313-57cfd362147e | -19.05343 | -53.45423 | 2025-05-10 01:30:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 30a5e8b8-8d63-39c5-9501-8a74e52298c9 | -12.68728 | -58.13147 | 2025-05-10 01:32:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e2582106-e82a-32ca-bae3-7950138a6ed2 | -13.05605 | -53.72793 | 2025-05-10 01:32:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 81e25b1b-415b-3c11-ba3c-1484965ad123 | -13.97342 | -56.80468 | 2025-05-10 01:32:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 69a43716-49c3-32b8-9f6b-d9c47680ecf7 | -13.62405 | -54.88458 | 2025-05-10 01:32:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| b2db74d2-711d-37c2-8b4d-0dbf2ad09538 | -12.69021 | -58.15131 | 2025-05-10 01:32:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1df3efcc-03cd-3bf6-9c5c-e6d341226668 | -13.09278 | -52.3 | 2025-05-10 01:32:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 29.3 |
| f9a98e6b-9c63-39df-b1be-ffba731ff824 | -13.98319 | -56.80304 | 2025-05-10 01:32:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| a471aaa5-e845-3eb3-9294-bacf64041054 | -13.97513 | -56.81583 | 2025-05-10 01:32:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 6c7d95d4-f09c-3d63-8568-bd88ebf02a0f | -13.04361 | -53.7303 | 2025-05-10 01:32:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 8a1ba971-a575-3ec7-8ab8-ae145d194ef8 | -13.98488 | -56.81415 | 2025-05-10 01:32:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 0ee24c56-6ed1-323d-9c2b-ceaa0f76fe8a | -8.69005 | -64.12887 | 2025-05-10 01:34:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5e2477ee-adbd-32b6-b065-ed3b546a2c5a | -8.6931 | -64.15186 | 2025-05-10 01:34:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 787c24a4-78b2-3599-a9b4-f9ba4e744262 | -8.69157 | -64.14035 | 2025-05-10 01:34:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ba8cbde3-1578-33c1-aea6-80d8387d63b0 | -7.29991 | -55.31675 | 2025-05-10 01:34:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 054cdc2d-40d5-3575-91a1-9beb0f96048e | -6.9589 | -43.023 | 2025-05-10 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 187.4 |
| 505d0010-050b-3a9e-896a-24c2f76b90a7 | -6.9586 | -43.0465 | 2025-05-10 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 52b4ee08-6ffd-38c7-bfcf-c7d9d5b0b82b | -13.9902 | -56.8058 | 2025-05-10 01:40:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 3fc4b7db-a3e2-3fb6-bad5-917c04a7cbaa | -6.9401 | -43.0247 | 2025-05-10 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| 23aacc9f-94d1-3099-9530-56f73bda4de2 | -6.9592 | -42.9994 | 2025-05-10 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.6 |
| e040cbf3-f527-3ff3-8adb-aadb998b4a79 | -6.9403 | -43.0012 | 2025-05-10 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 55.1 |
| bb74f314-22a0-3691-8b24-f904d25f2467 | -8.6973 | -64.1365 | 2025-05-10 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 92f061ee-ff5b-3e1d-a501-d899532a9f66 | -6.9589 | -43.023 | 2025-05-10 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.7 |
| 58f0dd24-63c3-38a0-acbb-ed424143c7f1 | -6.9592 | -42.9994 | 2025-05-10 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.4 |
| c0cfe5dd-0269-30ad-90c1-ef9e5b34995e | -13.9902 | -56.8058 | 2025-05-10 01:50:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 164c6075-25a0-37b3-8f66-0771f676676d | -13.9902 | -56.8058 | 2025-05-10 02:00:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 56456cce-0294-3162-83b6-f93dfa10b7fe | -13.9902 | -56.8058 | 2025-05-10 02:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 6093d897-a25d-3cda-a336-505eb5b6d32b | -13.971 | -56.8077 | 2025-05-10 02:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| e4429139-4223-3a93-bbc3-ed095e64568e | -6.9401 | -43.0247 | 2025-05-10 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 102.8 |
| 50b13031-1fb9-3c8b-8790-d9786a720e5d | -6.9592 | -42.9994 | 2025-05-10 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 26272158-d5bb-3674-8ed8-ae69f6b8e3d6 | -6.9589 | -43.023 | 2025-05-10 02:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 117.8 |


[Clique aqui para ver as próximas entradas](README2.md)
