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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb46e27c-7c98-355d-be37-846fd72baab9 | -10.7175 | -44.916 | 2024-10-30 03:46:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| fa91c609-807d-3517-9a19-a95687c0dbd6 | -19.5662 | -56.7164 | 2024-10-30 03:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.9 |
| 630f3fe2-652d-3f92-99ae-ff158a578115 | -19.5862 | -56.7136 | 2024-10-30 03:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 128.8 |
| 0ea90756-62d8-31ef-8f1f-80f22cfa2edc | -19.6063 | -56.7108 | 2024-10-30 03:46:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 144.8 |
| 950a572d-b3b7-36e9-8375-4ef2f0ed8ed2 | -19.6264 | -56.7079 | 2024-10-30 03:46:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 93.8 |
| 3e02a4a3-88e6-3704-900c-4427c919bc3e | -23.9923 | -54.1106 | 2024-10-30 03:47:18 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 74.9 |
| 1977d9e6-57fb-394c-a1fc-bfbcc600e819 | -1.458 | -54.0763 | 2024-10-30 03:55:14 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 895ed3e5-c627-30b6-912d-0e77ae8e7fa4 | -2.833 | -49.2413 | 2024-10-30 03:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6933877f-494e-3f78-91b5-9621f7b7fcbb | -3.0734 | -54.167 | 2024-10-30 03:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| c5860740-22ed-34a3-9627-79a6b508ff3c | -3.0913 | -54.287 | 2024-10-30 03:55:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 6ec93d9c-ef5e-348f-92b4-72cd3f45d545 | -3.1028 | -51.1041 | 2024-10-30 03:55:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.8 |
| e90168df-5197-3420-899b-9c7be5960134 | -3.1097 | -54.2865 | 2024-10-30 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 28fa270f-045d-3d66-a7d4-c86980a845c8 | -3.1098 | -54.2665 | 2024-10-30 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3b12bf6d-1c70-3fd8-a01a-90f35b923e91 | -3.1281 | -54.266 | 2024-10-30 03:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| fbed16a5-65da-35a3-98d3-5d272ce12a95 | -3.1601 | -50.6021 | 2024-10-30 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 64a23e27-6bf5-37f6-8d05-3dfd6768bb79 | -3.1602 | -50.5812 | 2024-10-30 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| b01d99aa-a408-3001-b9d2-b74bb796affc | -3.1786 | -50.6016 | 2024-10-30 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 5fa81cc3-0ace-3771-ae7e-a03131bafdfc | -3.1787 | -50.5807 | 2024-10-30 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| e56652b3-2134-35dc-a287-ea319c8089b7 | -3.2534 | -50.3689 | 2024-10-30 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| feed9987-be1d-3377-84e9-c1ff64a6b9e5 | -3.2535 | -50.3479 | 2024-10-30 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 4ba2bda9-b164-3ef1-a283-cfba8bb23e0d | -3.2718 | -50.3683 | 2024-10-30 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| e8110717-fdac-3646-a0de-c55b40a6d157 | -3.2719 | -50.3473 | 2024-10-30 03:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 8f7adabd-04aa-3bbd-96e5-efa9d85680cb | -3.5818 | -47.3621 | 2024-10-30 03:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 619e6d29-0935-3381-ba50-6a9e8f9069b8 | -3.5631 | -47.3847 | 2024-10-30 03:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 06e66e7c-10a9-3f34-8df7-26f338e0c0a4 | -3.5632 | -47.3629 | 2024-10-30 03:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| df2e121b-1422-34db-8a51-9360cb1faa40 | -3.5817 | -47.384 | 2024-10-30 03:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 7a8b9968-c63a-3cf4-babe-7196449c8b80 | -3.9486 | -48.1291 | 2024-10-30 03:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a4a98632-b5b5-38af-a54e-3efc735fc318 | -3.9671 | -48.1283 | 2024-10-30 03:55:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| d85f857f-c4a9-306c-a1ff-86644482e40a | -4.0866 | -50.0232 | 2024-10-30 03:55:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| f6d95c0d-b58c-3907-a616-49a2c5515971 | -4.0681 | -50.024 | 2024-10-30 03:55:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 10bb92c1-c338-3cad-aed7-76dd3b20f333 | -4.0682 | -50.0029 | 2024-10-30 03:55:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| f2776f8e-c6ca-368b-a7be-8aa6856e86bb | -4.0867 | -50.0021 | 2024-10-30 03:55:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| eeb79818-e0dd-3d72-b48a-b664978c23f1 | -4.2496 | -50.6677 | 2024-10-30 03:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b7c22b0c-f758-3ce0-bba0-997e9fd75d5d | -4.2681 | -50.6669 | 2024-10-30 03:55:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| ead555cf-9af7-30fb-b4be-b011a13f0a4c | -5.9788 | -45.3621 | 2024-10-30 03:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| a0c61bbc-da11-300d-a437-8f121293adbe | -6.4044 | -42.1035 | 2024-10-30 03:55:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 6e98c9b7-9eaa-3833-bdfb-565ffaf08cdf | -6.4232 | -42.1017 | 2024-10-30 03:55:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 200.9 |
| f400a787-c2f5-320e-a8a7-7de44e26df56 | -6.4235 | -42.0779 | 2024-10-30 03:55:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 41b26844-5a13-34ed-86b2-4cdbb7d53a01 | -8.8533 | -49.8629 | 2024-10-30 03:55:56 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 6da5c6db-98d7-31ae-b589-91847df57c38 | -19.5662 | -56.7164 | 2024-10-30 03:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.6 |
| 6689917e-693f-385d-a54e-e815dae275b8 | -19.5862 | -56.7136 | 2024-10-30 03:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 119.1 |
| 175ed931-97ed-3962-9f84-3d0bed637643 | -19.6063 | -56.7108 | 2024-10-30 03:56:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 144.7 |
| 922050ca-1703-366e-9552-32fab2968b82 | -19.6264 | -56.7079 | 2024-10-30 03:56:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 6c7ef077-e451-396e-9e4c-3c94be92d9c7 | -2.833 | -49.2413 | 2024-10-30 04:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 28be1f09-3d69-3f1a-81be-559f15b32668 | -3.0734 | -54.167 | 2024-10-30 04:05:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 92379b14-9d2d-3acb-b39e-9d2b9322e1ec | -3.0913 | -54.287 | 2024-10-30 04:05:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 17ff7b15-d79f-36a0-914b-17f416fb73a3 | -3.1097 | -54.2865 | 2024-10-30 04:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f4e2553e-31d1-3956-8631-e6550357f38c | -3.1098 | -54.2665 | 2024-10-30 04:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b1265b5e-e63d-3165-baff-7cb9b6cf433c | -3.2719 | -50.3473 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 24710297-9362-3815-b004-f7b25804a0a0 | -3.272 | -50.3263 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 8251b5de-7647-304b-9cff-a7bf2e2ddf4a | -3.1281 | -54.266 | 2024-10-30 04:05:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 25c0ce13-bae0-3869-b1bc-77177264cd43 | -3.1601 | -50.6021 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| a23b5ca5-b081-38fd-ae99-e960e5ae59c2 | -3.2535 | -50.3479 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 1c3e46ae-cf7d-3162-a316-4e4c0a89e9ea | -3.2535 | -50.3269 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| bb9a0fe2-e8a5-328a-a5ac-d3437ff31c0b | -3.2718 | -50.3683 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 856fb2ef-3a38-38a4-bb8e-8e5c01e3f049 | -3.1602 | -50.5812 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 29.8 |
| d7c36d08-8cc2-3dac-8ce3-4a5db589a8c3 | -3.1786 | -50.6016 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| dedb647f-34bd-381c-bcc4-e099f6c62a1c | -3.1787 | -50.5807 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| a2a5c734-c443-3778-a7d6-0ee5342181a9 | -3.2534 | -50.3689 | 2024-10-30 04:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 31d95292-58a1-3e92-8aa5-16bae6f3b7ba | -3.5631 | -47.3847 | 2024-10-30 04:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| e0114205-7f2f-386e-a980-8171e013f122 | -3.5632 | -47.3629 | 2024-10-30 04:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 57d41bc3-4105-3fdb-891f-df005d9168fe | -3.5817 | -47.384 | 2024-10-30 04:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 601396e9-7c65-389d-85bf-de6252b658a6 | -3.5818 | -47.3621 | 2024-10-30 04:05:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 5f1f1688-3ce7-3b81-81cc-873ca78367ad | -3.9486 | -48.1291 | 2024-10-30 04:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 07598832-12bf-35c0-a2a5-a173a8df52bb | -3.9671 | -48.1283 | 2024-10-30 04:05:28 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 31.7 |
| f1f3dcaa-38ab-32c6-868d-464b5bd57982 | -4.0681 | -50.024 | 2024-10-30 04:05:29 | GOES-16 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 9dd64866-e34a-35a7-b414-34111af3f082 | -4.0682 | -50.0029 | 2024-10-30 04:05:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 72a0f170-8834-3878-aacf-fb0557e7d7a8 | -4.0866 | -50.0232 | 2024-10-30 04:05:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| dbfe00e7-74e1-378e-acb0-5dc85d3fbd17 | -4.0867 | -50.0021 | 2024-10-30 04:05:29 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a5ca5c04-462d-314a-9b0c-60814c4c8b5c | -4.2563 | -43.4368 | 2024-10-30 04:05:30 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 96995c94-7349-390d-8a2d-899a882c52a6 | -4.2496 | -50.6677 | 2024-10-30 04:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f6ff4221-2f3d-374c-8fe4-e0609cc7974d | -4.2681 | -50.6669 | 2024-10-30 04:05:30 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| d4f5efe9-63e8-3b7c-afb2-90c5354e1c70 | -5.9788 | -45.3621 | 2024-10-30 04:05:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 46de3d6c-e55c-33cf-95e0-e68feea51b44 | -6.4232 | -42.1017 | 2024-10-30 04:05:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 76.0 |
| 6057edd9-4e0e-36d7-9007-1d9ab16a709d | -6.4235 | -42.0779 | 2024-10-30 04:05:42 | GOES-16 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 57.8 |
| 0ca3f0fc-5ed7-3aac-81c1-b69ad13f603b | -10.7175 | -44.916 | 2024-10-30 04:06:06 | GOES-16 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 31961b26-bbf3-353b-90c1-d786eabbfebb | -19.5662 | -56.7164 | 2024-10-30 04:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 8e745b76-6598-3b46-a1a5-3b76a2900771 | -19.5862 | -56.7136 | 2024-10-30 04:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 117.5 |
| d48e2676-1ce4-3913-a5d2-3b3e0e49cb27 | -19.6063 | -56.7108 | 2024-10-30 04:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 137.2 |
| dc1ea8ec-c1a3-30ac-9f12-b71b282525cb | -19.6067 | -56.6898 | 2024-10-30 04:06:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 88b57322-8413-3195-a261-71d9c075f42e | -19.6264 | -56.7079 | 2024-10-30 04:06:56 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 86.8 |
| 82f6f8fd-5b1d-325b-ab7d-af62f81ded24 | -2.833 | -49.2413 | 2024-10-30 04:15:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7fd8db90-893d-3bef-bdd7-1b6f5ee970f7 | -3.0734 | -54.167 | 2024-10-30 04:15:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 138fab77-2fc6-34a2-9641-29c3aebe4029 | -3.0913 | -54.287 | 2024-10-30 04:15:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 4cbe807e-9796-371b-81f2-ffd9efbe60c4 | -3.1097 | -54.2865 | 2024-10-30 04:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 8a100230-3c55-3a81-834e-13cda60d1dba | -3.1787 | -50.5807 | 2024-10-30 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 972ee665-429e-3626-84eb-c903c3dcd512 | -3.2534 | -50.3689 | 2024-10-30 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| aad75db5-fc57-36ea-a192-f3b37e7c98fe | -3.2535 | -50.3479 | 2024-10-30 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.3 |
| e2d8c8cf-c789-32c8-a89f-3919ecb93fc0 | -3.2535 | -50.3269 | 2024-10-30 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| c4d9ae47-0488-344d-a25d-973b9fbb5410 | -3.2718 | -50.3683 | 2024-10-30 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 839f08ab-1074-343b-94e1-0160a413f0e1 | -3.1098 | -54.2665 | 2024-10-30 04:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7af399d9-4aa0-3a9a-84b4-0385e992c781 | -3.1281 | -54.266 | 2024-10-30 04:15:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| eaaa66c8-d583-34aa-8e2c-0623a353e2f3 | -3.1601 | -50.6021 | 2024-10-30 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| c563ab78-be9e-37c2-a0bd-690da6908ff9 | -3.1602 | -50.5812 | 2024-10-30 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 7811a753-4ac2-369e-b621-74b0000aebda | -3.1786 | -50.6016 | 2024-10-30 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| dca951ae-6560-3c0f-be0d-c87676011042 | -3.2719 | -50.3473 | 2024-10-30 04:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| da01dd4d-f068-34d9-9550-a440e369ef4d | -3.5817 | -47.384 | 2024-10-30 04:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5514e6c8-8801-30df-9793-97b21432eddd | -3.5631 | -47.3847 | 2024-10-30 04:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 5bef925d-27f6-30f9-ae90-ecdfc2c06b16 | -3.5632 | -47.3629 | 2024-10-30 04:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 3377aef9-8580-34ac-9b3d-319af2e22836 | -3.5818 | -47.3621 | 2024-10-30 04:15:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 33.7 |


[Clique aqui para ver as próximas entradas](README32.md)
