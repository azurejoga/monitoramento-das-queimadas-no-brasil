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
| f0ce3754-4cfd-351e-a9c7-d36f08639df6 | -17.8974 | -45.024 | 2025-10-13 00:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 86623455-8108-3fff-b473-755271035718 | -17.3582 | -53.7893 | 2025-10-13 00:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9330fd42-6d77-3cdd-b8ac-3ac667dbf106 | -17.3578 | -53.8106 | 2025-10-13 00:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 81.6 |
| e6c86db9-7c91-3d1c-b422-192535d3509b | -19.0316 | -57.5589 | 2025-10-13 00:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 2f60ca02-2c7d-3866-9829-852fa3a953b3 | -14.206 | -51.5059 | 2025-10-13 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 87d531ad-f064-3d80-90bc-251ef991769a | -11.7497 | -64.9571 | 2025-10-13 00:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 8e6bdddc-3d04-3fe2-9437-802eef2abc7d | -3.1433 | -50.2044 | 2025-10-13 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 36211d47-f4a2-3c30-9b66-0abd576450df | -17.338 | -53.8135 | 2025-10-13 00:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 317.7 |
| b6f73ec4-e0c0-3e65-b666-9c9267a4bbac | -17.3187 | -53.7951 | 2025-10-13 00:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 99.3 |
| e2c0c5c6-621e-330a-bdb1-997279070f65 | -8.8915 | -45.2768 | 2025-10-13 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| a1be92d7-c795-3555-a5cf-2d5c5fb3a68f | -3.0726 | -49.404 | 2025-10-13 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 121.4 |
| daeee205-183d-3d9f-bb57-f0917b6f7d6c | -17.3384 | -53.7922 | 2025-10-13 00:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 299.1 |
| 4978fa75-5c02-316a-b4ab-577740946133 | -11.7495 | -64.976 | 2025-10-13 00:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 87ab69d1-4a9a-38c4-a4e5-befa56470484 | -4.6881 | -43.1547 | 2025-10-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 4dd97a49-8d80-3452-bee5-ae1ecc5b5a0d | -5.2485 | -45.5924 | 2025-10-13 00:00:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 3fc80a8f-8642-3216-8ee6-c9a2c77a77fd | -8.4658 | -46.1134 | 2025-10-13 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 4dff5240-316a-3b7b-89f2-0896bedce4f3 | -8.4655 | -46.1359 | 2025-10-13 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 99.3 |
| f0684a5b-fecc-303a-8de0-bfda1ac9763e | -10.8093 | -43.9744 | 2025-10-13 00:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| ee4b2c25-2aba-3e93-abe3-6b99b848d3ae | -4.707 | -43.1302 | 2025-10-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| df7b115e-da62-3011-a4bb-0032f2448737 | -4.6883 | -43.1314 | 2025-10-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 744.5 |
| 68b116a3-30ef-3662-b2fa-e2a549373649 | -2.5239 | -47.7899 | 2025-10-13 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| bbe9d4a3-1e8b-39e4-af48-2e9e3387c5b4 | -5.3223 | -43.4153 | 2025-10-13 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 32497c15-2450-31a3-82bd-57977c35b18e | -17.3183 | -53.8163 | 2025-10-13 00:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 8beb87a8-f5f8-347b-8e80-8e002a983dc5 | -2.5238 | -47.8115 | 2025-10-13 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 726b1315-14d5-30a7-93ec-189931c1ecb8 | -4.6698 | -43.1092 | 2025-10-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 70c595ec-3e79-33fc-9581-d8c014ef3bc4 | -5.5684 | -45.2783 | 2025-10-13 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| f66da7de-137c-3fcd-be3f-84b00c568bfa | -4.6696 | -43.1326 | 2025-10-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 265.8 |
| 41d72167-6873-3cb6-a489-ecb719f7bc27 | -2.5424 | -47.7893 | 2025-10-13 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 9a25ff5a-9b0f-3e9c-ac69-555200d18e37 | -11.7309 | -64.9579 | 2025-10-13 00:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 1b939022-0c89-34a6-b7b2-1ee5ea921468 | -3.1248 | -50.205 | 2025-10-13 00:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 533ea17c-4aec-3fa7-97ee-bdb46d05abc5 | -14.2056 | -51.5273 | 2025-10-13 00:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 408f15e1-9434-3d0d-9e0a-2564f7da7e15 | -2.5423 | -47.811 | 2025-10-13 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 2063f34f-fe7d-351e-b37d-45028e706e3f | -8.4847 | -46.1115 | 2025-10-13 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 489fb14b-4261-3c3c-be92-b51cf4722353 | -5.3221 | -43.4386 | 2025-10-13 00:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| e6c15c30-4ebf-358a-8d7f-46d7568d7550 | -15.5428 | -41.8179 | 2025-10-13 00:00:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 100.6 |
| f450af65-5747-3d8b-b703-bf30f43f6b3a | -8.4844 | -46.134 | 2025-10-13 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| d58044a6-8678-3e3d-9549-c055af7885b7 | -5.5686 | -45.2557 | 2025-10-13 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| d129c294-d649-3877-acc7-e61e0e457d4d | -8.8909 | -45.3224 | 2025-10-13 00:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| ef93d581-f57e-3d0c-9ca3-ecfe70b67ec4 | -4.6885 | -43.108 | 2025-10-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 292.6 |
| b76963b6-2c94-3f53-8505-0c330592f081 | -4.6696 | -43.1326 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 393.6 |
| ef49ec56-424e-3c00-86fc-6a58e9ee91d3 | -3.1433 | -50.2044 | 2025-10-13 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 154cba6e-5d54-34ef-a297-84be07af8bde | -2.5423 | -47.811 | 2025-10-13 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 175.7 |
| f596e765-b52b-35f1-9b9e-8b3f1657d79a | -3.0726 | -49.404 | 2025-10-13 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| a2333646-68f7-34be-8331-84639c380f81 | -3.1057 | -50.3735 | 2025-10-13 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| bac91a9c-9f45-3e2a-982f-abc4500993dd | -2.5424 | -47.7893 | 2025-10-13 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 51b2f92e-04e2-3781-a226-a872a0db6034 | -4.6885 | -43.108 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 245.7 |
| 051a69b4-40c2-38e8-a987-ae4623223a5e | -17.3183 | -53.8163 | 2025-10-13 00:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 0f3b06c5-1481-35c5-ae68-c25dbdc66fbe | -17.3187 | -53.7951 | 2025-10-13 00:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 2ffaa496-826d-305d-b42d-e25df9425e92 | -4.6883 | -43.1314 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 399.1 |
| ac6ce58f-d3f1-38b7-990b-70078dbc4369 | -11.7308 | -64.9769 | 2025-10-13 00:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 16e5d1cf-5f6a-312a-a1de-09cf8a31686a | -4.6694 | -43.1559 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 9859a4c0-ecbf-38d3-a7dc-b76923d7ffc5 | -5.0992 | -43.2211 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 10be2bc8-accc-348f-83e0-62ee0565d886 | -3.1248 | -50.205 | 2025-10-13 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.7 |
| abb61efa-af8a-387a-a5cf-b3812627fadc | -5.1181 | -43.1964 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| d3e7b73f-b85a-319a-9b87-d1de26c3f5c0 | -4.6698 | -43.1092 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 079a453b-b082-3664-ab11-165160741e15 | -17.338 | -53.8135 | 2025-10-13 00:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 215.7 |
| f2cfd23a-1beb-3dc0-baf6-c935d9bfeae8 | -11.7495 | -64.976 | 2025-10-13 00:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 19c0f6ac-af99-3314-a07a-59376da796e9 | -17.3582 | -53.7893 | 2025-10-13 00:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 74.8 |
| f909c60e-a712-3649-8491-9b1d8bafbef5 | -11.7497 | -64.9571 | 2025-10-13 00:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 124.2 |
| a45d5cd7-2118-3787-9444-76dc0ef5c3a3 | -5.0994 | -43.1977 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.2 |
| 99d486b6-526a-32b9-b726-2947329ca401 | -4.707 | -43.1302 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 38303855-156e-31f7-acea-6de5fa3fdf3a | -2.5239 | -47.7899 | 2025-10-13 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 160.0 |
| c78f66e5-c853-3979-ab88-ff050a44c125 | -11.7309 | -64.9579 | 2025-10-13 00:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 81f9c092-ba26-3eb2-9432-ead4cb47d472 | -17.3578 | -53.8106 | 2025-10-13 00:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b47918e1-3196-37e4-9dac-14eb6d9a3ac2 | -15.5428 | -41.8179 | 2025-10-13 00:10:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| 567590b0-844a-3d15-83c8-7a5859a0aba0 | -17.3384 | -53.7922 | 2025-10-13 00:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 167.9 |
| a42ce2db-0670-3c8c-a47b-d85d13cbf1b6 | -4.6881 | -43.1547 | 2025-10-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 17dd0fb4-3184-3d3a-b5bc-948d9c4591d4 | -5.2485 | -45.5924 | 2025-10-13 00:10:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 46.3 |
| f48c2772-2e58-3500-bfdc-b71020e0ad6e | -2.5238 | -47.8115 | 2025-10-13 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 218.2 |
| f24b6c80-f791-32f0-a455-9335b59e13df | -17.4198 | -40.0136 | 2025-10-13 00:20:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 221.5 |
| 7ae88df4-8a5d-3b13-8fcc-6220ce737008 | -17.3183 | -53.8163 | 2025-10-13 00:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 182eb856-17e1-3228-a21e-aa6441c26c50 | -17.3578 | -53.8106 | 2025-10-13 00:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 1b231525-1897-3061-851c-ab60fc2ba585 | -4.6698 | -43.1092 | 2025-10-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.9 |
| 51a4137a-2425-3481-acf9-bc6b31bffb20 | -3.1248 | -50.205 | 2025-10-13 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 0238d8d0-c882-3a00-a23d-aa3283a4888d | -2.5424 | -47.7893 | 2025-10-13 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 157.4 |
| 30044132-4810-3387-98b0-ed9b58d06190 | -11.7309 | -64.9579 | 2025-10-13 00:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 130.2 |
| b7e27e30-f2f8-3ed1-b1b0-04e4b60802cc | -3.1057 | -50.3735 | 2025-10-13 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 20e75f64-2c99-3763-b913-11156263e45b | -2.5423 | -47.811 | 2025-10-13 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 158.2 |
| 689e6967-76c1-314e-86be-576b8dbc84b3 | -17.4004 | -39.993 | 2025-10-13 00:20:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 151.9 |
| 75ac3449-03f2-3c47-be3c-367d87453f75 | -4.6885 | -43.108 | 2025-10-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 201.7 |
| 44a52338-ba94-3fe4-8397-cc263d736617 | -4.707 | -43.1302 | 2025-10-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| edfc1931-0887-3806-bff8-d6c43e6f493b | -14.2822 | -51.5599 | 2025-10-13 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 3404e711-bab0-3d75-a4e3-f03490e438eb | -11.7308 | -64.9769 | 2025-10-13 00:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| b1a1e0f2-eb82-3ab2-af3d-44850c2f7c00 | -3.1433 | -50.2044 | 2025-10-13 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ae8e24e5-a8c0-3ca4-8113-d60a8001e3c4 | -17.3582 | -53.7893 | 2025-10-13 00:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 903fbda0-2cea-375d-ac02-9c64751e75f0 | -14.2825 | -51.5384 | 2025-10-13 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 2cc81201-ca7f-3868-a9bc-5a0593e720f0 | -11.7495 | -64.976 | 2025-10-13 00:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 133.1 |
| e4f84bbf-7e3b-36a4-abe8-220f20681b7b | -2.5238 | -47.8115 | 2025-10-13 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 172.5 |
| e96de5da-cc6a-304c-8e05-046faa6dece3 | -3.0726 | -49.404 | 2025-10-13 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 7b3b5274-a535-3e1e-a0ad-97527e52f969 | -5.2485 | -45.5924 | 2025-10-13 00:20:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 6094104d-e7ed-3142-b59f-06a75815ecf5 | -15.5428 | -41.8179 | 2025-10-13 00:20:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.5 |
| 85985bf2-f7fe-3fec-8508-544f7af7c7c5 | -17.3996 | -40.019 | 2025-10-13 00:20:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 163.9 |
| 6dddf2b2-b7f4-3935-9899-fb1c775485fa | -13.4977 | -51.2992 | 2025-10-13 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 5e334fb5-e1c7-320b-bff9-7693c778270c | -14.3015 | -51.5573 | 2025-10-13 00:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| dcab14fe-a072-3db2-8ecd-ee765f1e913b | -17.3384 | -53.7922 | 2025-10-13 00:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 163.9 |
| f9bb9714-76bc-3289-b458-8f4e93c39f51 | -11.7497 | -64.9571 | 2025-10-13 00:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 181.5 |
| 561ec849-2d9e-3063-8922-27d7b3ec083d | -4.6696 | -43.1326 | 2025-10-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 279.8 |
| 0bff3f77-fa33-3203-a68c-4a394f90872d | -17.4206 | -39.9875 | 2025-10-13 00:20:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 197.8 |
| 49485817-30e9-3778-b336-9b2e8cf2eed2 | -17.338 | -53.8135 | 2025-10-13 00:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 173.8 |
| 033a1455-5a6c-38a7-9b0c-d7b4585e18b8 | -17.3187 | -53.7951 | 2025-10-13 00:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 72.6 |


[Clique aqui para ver as próximas entradas](README2.md)
