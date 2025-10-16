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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e876a0b6-82b8-399a-bb21-04236acad568 | -7.4894 | -42.7586 | 2025-10-16 01:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 120.0 |
| b7daf22b-470d-397a-82f9-b0d0d6e48634 | 1.8401 | -55.7429 | 2025-10-16 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| e86db5b8-4ef6-3a7e-8eff-678f64c42e39 | -5.8799 | -43.8844 | 2025-10-16 01:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 153.2 |
| e6207441-d09c-34d9-9bf0-9f5b38374097 | -5.7865 | -45.9827 | 2025-10-16 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 0d91ca75-dccc-3a77-8113-47d2bdf0c1be | -8.4714 | -44.1978 | 2025-10-16 01:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| e63f730c-c89e-3d91-ac25-d636535b6b61 | -4.3874 | -43.3827 | 2025-10-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 471.4 |
| f8d42b31-6ef0-3804-b336-0157c37921c2 | -5.4575 | -42.9381 | 2025-10-16 01:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 58.6 |
| f9b666b8-0137-3a7a-9b8d-3432ddf42478 | -4.3687 | -43.3838 | 2025-10-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 364.1 |
| ec824c05-833f-3481-8922-157ff9f88d7f | -4.4059 | -43.4049 | 2025-10-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f8b4a6f1-6fb6-3e4d-b9be-b93417dcc9f4 | -12.6612 | -43.4268 | 2025-10-16 01:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| b213523d-05f4-34df-985f-8683ad81ddcb | -3.0343 | -45.3896 | 2025-10-16 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 29.6 |
| e8653b04-a2f5-32b7-9583-a6573d4d33f9 | -8.247 | -44.0368 | 2025-10-16 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 61f625e5-62d0-3e0d-8a27-7cf6c4ba7658 | -7.4706 | -42.7605 | 2025-10-16 01:10:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 128.2 |
| 595fccf2-6f13-37b9-b2a7-5ddcd2de7187 | -4.0976 | -48.0144 | 2025-10-16 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 8e0af4b2-5ea4-383b-9feb-aa84fd35ac9d | -5.5147 | -47.3069 | 2025-10-16 01:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 6acb7050-60ff-333e-ada1-d3cbebbf6b45 | 1.8218 | -55.7234 | 2025-10-16 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 6017cd05-6943-3796-9b5b-266ef67c5458 | 1.8218 | -55.7431 | 2025-10-16 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f33347ba-043d-3a3b-9f3e-85215272a93e | -3.0158 | -45.3679 | 2025-10-16 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 111.3 |
| b5c95740-db48-3650-9665-96988a1f14cb | -5.7863 | -46.005 | 2025-10-16 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 257.5 |
| 79515fbb-53ce-3c58-802c-56b67f1e0679 | -4.0974 | -48.0361 | 2025-10-16 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 9011cf43-19bc-3e76-af59-20b721b52072 | -4.116 | -48.0352 | 2025-10-16 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| eae0f164-0839-3d71-b131-16ed13eab2d3 | -4.3871 | -43.4292 | 2025-10-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 8f276a3b-da2a-3627-933b-2aeaa70e1371 | -4.3872 | -43.406 | 2025-10-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 523.7 |
| 81b4416d-3bdc-3a1e-bd59-3e0cb89d0b31 | -12.6801 | -43.4474 | 2025-10-16 01:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 6d2d9f91-05ca-32d5-9bf1-e05817f973a8 | -4.5229 | -45.3882 | 2025-10-16 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 2483147a-a69c-3507-a922-6fd94a2eed63 | -4.8644 | -44.5748 | 2025-10-16 01:10:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 3c8cf237-9d36-39a5-a23f-cbf585814703 | -7.9439 | -44.1381 | 2025-10-16 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 120.6 |
| f3da5c54-7866-3ce5-a819-01cf6586bdd1 | -4.1161 | -48.0136 | 2025-10-16 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 139.0 |
| acc7a07d-57ae-3aac-be42-001a27a32376 | -8.2461 | -44.1064 | 2025-10-16 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 694789da-003b-3d2a-aa4e-630528456a0a | 1.8032 | -55.8815 | 2025-10-16 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| f1f966ee-8bcf-348e-9c62-54b7d8b3f218 | -5.4762 | -42.9367 | 2025-10-16 01:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 101.1 |
| b03ef5a2-dd9f-37f6-8e4f-440b3806e15f | -4.35 | -43.3849 | 2025-10-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| c95bba20-0e88-3c91-8d5c-0f224f74b7aa | -12.6805 | -43.4235 | 2025-10-16 01:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 243.5 |
| 30c0db47-4b16-3e77-906f-79e5b4bfe8b3 | 1.84 | -55.7626 | 2025-10-16 01:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| d3eaac37-0df4-3dc3-be5c-909fe96ed71f | -3.0157 | -45.3903 | 2025-10-16 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 242.5 |
| 12e97064-c2e1-3359-995a-443f71efcb99 | -9.2398 | -63.2489 | 2025-10-16 01:10:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 8b8d457e-1ebb-3264-8f53-a7f7c37ea991 | -4.5042 | -45.3893 | 2025-10-16 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 98.6 |
| ad709812-00a2-3210-81a1-6b2f237fa4e5 | -29.187 | -50.1287 | 2025-10-16 01:10:00 | GOES-19 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 55.9 |
| 9074566b-281c-31ba-bd87-965b4ca7150b | -3.0156 | -45.4128 | 2025-10-16 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 359f32f9-f33a-31c5-a5f9-47546cba7bf0 | -4.5041 | -45.4118 | 2025-10-16 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 101.2 |
| a927465e-46eb-38da-a923-37ef0e17bfc1 | -4.4061 | -43.3816 | 2025-10-16 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 23260fb8-6439-3a2f-a7f9-d790239e1e0b | -4.4854 | -45.4128 | 2025-10-16 01:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 8f229d09-c9e8-37ef-9445-f5aa07fca083 | -8.2464 | -44.0832 | 2025-10-16 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 135.3 |
| fe8b2a09-51c1-395a-b541-57a7e0634b2e | -5.805 | -46.0037 | 2025-10-16 01:10:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2d3da43e-149d-36bb-a4c0-140d9575eaad | -9.23715 | -63.25146 | 2025-10-16 01:11:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 92.5 |
| dcf9e70a-26f0-3f0e-bd35-144756dc4c50 | -11.75755 | -58.42824 | 2025-10-16 01:11:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f6578b2-aae5-3e40-a4a1-a596201fa402 | -10.87856 | -48.8048 | 2025-10-16 01:11:00 | TERRA_M-M | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 4628da77-e62b-3c4c-8f87-4c95a32b4116 | -11.76473 | -61.08228 | 2025-10-16 01:11:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 476b1c55-082b-3215-9cc1-62c73a7a53b3 | -11.75366 | -61.07278 | 2025-10-16 01:11:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 3ad89eb3-d93d-35ae-8d09-166e1eddcd0a | -10.39581 | -58.38063 | 2025-10-16 01:11:00 | TERRA_M-M | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e7df45e0-2334-3a9e-a38b-4368cf78ed71 | -11.53914 | -49.92767 | 2025-10-16 01:11:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 63817187-3b23-301a-aac9-d6d3074ecc70 | -10.77142 | -62.0767 | 2025-10-16 01:11:00 | TERRA_M-M | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d189ec12-4964-35e9-8f7c-9952d51f1596 | -12.72919 | -50.63815 | 2025-10-16 01:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| c8368a28-a490-3102-8565-fa357b148805 | -12.71918 | -48.65097 | 2025-10-16 01:11:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 269cbf52-ec1a-3683-a261-55035cbcffb4 | -9.23888 | -63.26524 | 2025-10-16 01:11:00 | TERRA_M-M | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| f543dc8a-ed93-3804-8bb7-487ffd3507ce | -12.24369 | -49.38663 | 2025-10-16 01:11:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 78d4112a-2594-386e-a6b8-180c7595909a | -11.76331 | -61.07146 | 2025-10-16 01:11:00 | TERRA_M-M | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 28.5 |
| a09f6754-9369-3b79-b586-e837fd7ae0de | -11.38466 | -61.21308 | 2025-10-16 01:11:00 | TERRA_M-M | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 990ad7ec-aec9-3b7f-a7ea-e9bcc02438a9 | -9.2181 | -48.5887 | 2025-10-16 01:11:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 9e3ecad1-146f-3f01-ae63-b3a05192ff75 | -9.22022 | -48.5831 | 2025-10-16 01:11:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 37.7 |
| 0fbb2932-f775-3e78-95d5-051a72b6b3d8 | -12.73922 | -50.65534 | 2025-10-16 01:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.0 |
| bc3c9475-9a85-3643-83f9-50d0332f170a | -10.42047 | -59.6936 | 2025-10-16 01:11:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| a3f239ee-7a52-3bad-bc5d-f976b3b7056d | -12.24015 | -49.38066 | 2025-10-16 01:11:00 | TERRA_M-M | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 86242978-7729-3c4f-9774-bc2e6c9b6ffb | -12.73511 | -50.63153 | 2025-10-16 01:11:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 7c9e2b89-b3b5-30c1-b272-ffc74ce8355d | -9.22727 | -48.62287 | 2025-10-16 01:11:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 35.8 |
| d5b9abd5-49a1-327a-b8cc-199d6bdc3136 | -10.8844 | -48.79685 | 2025-10-16 01:11:00 | TERRA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 040ba22f-55df-308a-9a67-7122e6a64d47 | -2.87984 | -50.73028 | 2025-10-16 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 9cdd9966-4d13-332a-a21b-5fc540501fed | -2.25474 | -56.06235 | 2025-10-16 01:13:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| b869e958-e698-38ae-bf91-ae0ef5d3485c | -1.99126 | -56.92127 | 2025-10-16 01:13:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a6ab78e7-72d8-31f8-af0e-86263b6a6af2 | -4.30775 | -50.41169 | 2025-10-16 01:13:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.6 |
| a6ae9738-219e-3710-8013-8fb1d8ea0336 | -3.51146 | -52.4978 | 2025-10-16 01:13:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| de363b94-cea8-3172-92a5-f3efd9bbb6cc | -2.87335 | -50.73654 | 2025-10-16 01:13:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b25e3e00-de2d-3d51-a2ae-bdf6cce30aa9 | 1.81288 | -55.88842 | 2025-10-16 01:15:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7f3948ed-19e0-3743-8606-b985cd3fa7f7 | 1.84667 | -55.7247 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| e3331074-2aa5-3eaa-8184-ab6c29608e75 | 1.84222 | -55.7581 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 5fb3d737-0de4-3eb1-a96e-9fd6eb0477aa | 1.83369 | -55.76719 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| b94a74b2-0bd9-378e-945c-20950a2cd3cd | 1.83602 | -55.75063 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 1bc0cd66-363b-3792-b6c9-2cabb4d8fac9 | 1.83255 | -55.73977 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 392d87f8-d48e-3221-868f-c38a99f60136 | 1.81504 | -55.87212 | 2025-10-16 01:15:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 81257458-6d8a-3b3f-9848-e099cfa076dd | 1.7517 | -55.7839 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| d61c4e9c-4c94-314a-9807-0dd00218ca52 | 1.84443 | -55.74146 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 28c0db35-c654-33c6-b8a6-6141661c2e02 | 1.84891 | -55.70786 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 14849ab7-83cf-368b-8e46-0205c99c269e | 1.80351 | -55.89682 | 2025-10-16 01:15:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ef3c8ba9-abe5-3c60-a59d-d8acf985dc9a | 1.84071 | -55.71724 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 3738303b-b34a-31bf-b0be-df0366ed055c | 1.83034 | -55.75644 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 307dff23-aa0e-3b8d-b42e-c91508a4a79c | 1.80577 | -55.88067 | 2025-10-16 01:15:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 38647f57-19e8-3665-b40a-99934ff9a5c3 | 1.83836 | -55.73396 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 130.3 |
| 43cdae21-fab1-3e99-a2f1-a60e4fb78d9c | 1.74627 | -55.78883 | 2025-10-16 01:15:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 8929d4eb-0fa5-31b8-9108-626a8a4d26e0 | -4.5042 | -45.3893 | 2025-10-16 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 1ffcf34d-40b0-360f-a654-b67bdbc3578d | -5.8802 | -43.8613 | 2025-10-16 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 270.2 |
| 1607b913-bd07-3621-8dae-5a4b88f55c26 | -7.4706 | -42.7605 | 2025-10-16 01:20:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 131.6 |
| 23171b72-168f-383b-9c0a-3a80e94e2375 | -4.5227 | -45.4108 | 2025-10-16 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 13ab1a2e-f196-330f-97b1-eca3e3bad59c | -12.6612 | -43.4268 | 2025-10-16 01:20:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 5fd83ac8-33f7-34bd-8a94-34b932e87cdb | -7.9439 | -44.1381 | 2025-10-16 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| e38a7d71-8128-3f8d-96d4-ab05ad55d988 | -9.2398 | -63.2489 | 2025-10-16 01:20:00 | GOES-19 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 0ba121d2-8e9f-35f5-8150-ca75d771eccd | -18.5932 | -47.4504 | 2025-10-16 01:20:00 | GOES-19 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 1ec001be-8167-3ed2-bdc8-fb58073f13ac | -5.4762 | -42.9367 | 2025-10-16 01:20:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| c1b24f98-6372-3517-a231-e66ffde5027b | -5.5535 | -47.1068 | 2025-10-16 01:20:00 | GOES-19 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 563b5645-3255-314d-b71d-93e388246c12 | -5.8987 | -43.8829 | 2025-10-16 01:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 88b04f26-c00c-3180-af01-c32877b66f3d | -4.3872 | -43.406 | 2025-10-16 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 321.7 |


[Clique aqui para ver as próximas entradas](README6.md)
