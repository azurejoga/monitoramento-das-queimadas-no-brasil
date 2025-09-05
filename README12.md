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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b11671aa-b7ea-3a60-9170-5dbb8c1a0efe | -9.4552 | -62.342999 | 2025-09-05 01:25:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d58fac89-715b-3837-8af2-c719766e3dee | -12.9784 | -54.828999 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d5cddeec-a838-3423-ba8c-f69df9915834 | -16.3111 | -52.953999 | 2025-09-05 01:25:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 656ee855-fdbd-3d19-b614-15332c2dda38 | -9.204 | -57.086601 | 2025-09-05 01:25:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f119b93-af34-3b5a-bb6d-d4ba5d67cc67 | -15.7495 | -53.663101 | 2025-09-05 01:25:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a546a089-ca63-341e-b5f8-c86c93b734fe | -9.2956 | -56.8167 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a86d70e0-e0e8-3be2-9a3a-30661653c960 | -13.0909 | -57.105801 | 2025-09-05 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f621b74-0c7e-3fcc-8363-1667b0cdb6aa | -16.556999 | -55.1315 | 2025-09-05 01:25:00 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 73633b23-f234-3a36-ac5e-21c037c836eb | -7.2292 | -56.8554 | 2025-09-05 01:25:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3eac3a-264e-3bf0-8862-0992c411a540 | -9.2547 | -57.0826 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17f69e29-ceae-3077-bce8-c3fba969f7c8 | -13.1024 | -57.110699 | 2025-09-05 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e6d9207-ac9c-3701-b456-9a9a95a6f367 | -15.7066 | -53.614799 | 2025-09-05 01:25:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fba8648e-1e0a-371b-9cee-26ca1ae6e56a | -6.268 | -53.439701 | 2025-09-05 01:25:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7702526a-38b9-373d-a157-4a00bd3ee3b7 | -12.9743 | -54.811699 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e4fa412e-5831-32c4-ace8-a721dbd55441 | -15.1892 | -52.361401 | 2025-09-05 01:25:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7252eb25-5c6c-310f-a1d5-9b6435988b07 | -16.5924 | -50.8246 | 2025-09-05 01:25:00 | METOP-C | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d1f9578a-5e45-3d42-bcdd-30fef61211f1 | -13.1007 | -57.1035 | 2025-09-05 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 109baf6c-069f-390d-ad50-acb931cc1b1e | -22.4853 | -52.757702 | 2025-09-05 01:25:00 | METOP-C | ROSANA | SÃO PAULO | Brasil | 3544251 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fb7e63c0-c6eb-3639-aa01-dda070deb011 | -12.9722 | -54.803001 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0837d977-d4a4-38de-9100-dd1f12af7494 | -9.3281 | -55.211601 | 2025-09-05 01:25:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4f91a91-a03f-3a5d-83cd-6dba0c190b30 | -16.298901 | -52.946602 | 2025-09-05 01:25:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4694f0db-6e29-346c-814b-df9a1bc0fa1e | -10.1343 | -54.997601 | 2025-09-05 01:25:00 | METOP-C | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c483dcbe-a8e4-3fc1-9d33-9ccd2653d3d0 | -13.8045 | -56.575401 | 2025-09-05 01:25:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9d02bf4-cd90-3029-aa10-efb7c34142a2 | -12.9701 | -54.794201 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b689e090-44e7-3265-8aa5-e7f5f997ff3b | -9.2057 | -57.094101 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8728dd36-73d2-3b4d-a8e4-5c35d09d7deb | -6.3191 | -58.173401 | 2025-09-05 01:25:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7086dd92-7362-3743-95aa-544e4cd48535 | -17.66 | -52.289799 | 2025-09-05 01:25:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3fea12df-3efe-3777-a9cf-d51ad4ccc5a5 | -13.104 | -57.117901 | 2025-09-05 01:25:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71f62e3b-8f93-3f3b-9147-781d3b739091 | -10.4733 | -53.627399 | 2025-09-05 01:25:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85b1abea-83ba-3acd-a345-48e8f24e4322 | -12.9799 | -54.791801 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 30f2dff7-3dc0-32d7-a169-8877413e809a | -5.4995 | -60.124001 | 2025-09-05 01:25:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| adca43d2-1ff5-335a-b464-03e14d5c9284 | -10.419 | -60.745701 | 2025-09-05 01:25:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46a12d24-0884-315c-b3b9-854c18ee961c | -15.1406 | -52.374199 | 2025-09-05 01:25:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 95c75d2a-b34a-3d9e-bd31-710b1594947f | -6.2583 | -53.442001 | 2025-09-05 01:25:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3813efcd-5e61-3190-9a2f-7adc8b7f4b6a | -12.9938 | -54.8069 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9d900df-fcde-3d61-86bb-75805c36b088 | -16.318399 | -52.941399 | 2025-09-05 01:25:00 | METOP-C | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 17c27d62-707e-361e-b4a1-cbc570733955 | -12.9624 | -54.805401 | 2025-09-05 01:25:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ce0d0174-4b53-3ed0-8568-9c1190a3fc02 | -9.2414 | -57.069801 | 2025-09-05 01:25:00 | METOP-C | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7b46beba-b664-3f8b-89be-b7af3e021967 | -9.457 | -62.351299 | 2025-09-05 01:25:00 | METOP-C | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8b31101b-697a-3d92-b5c3-d034121fdbb6 | -5.6081 | -45.0038 | 2025-09-05 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 638362f4-118b-3801-aad0-86cceb307682 | -5.6079 | -45.0265 | 2025-09-05 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| c63fbf3a-4c6a-388d-9408-1a3170c0af67 | -16.5494 | -55.12 | 2025-09-05 01:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 51.5 |
| fc5d9b75-1173-3bda-991a-e1c7e8d33aa8 | -8.0223 | -45.4354 | 2025-09-05 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 3bf836e4-a0c3-3ec5-bbae-34eed97566f1 | -9.2288 | -57.0906 | 2025-09-05 01:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| dfd3a705-5fc5-3968-a7ee-1f2925aae031 | -5.5892 | -45.0278 | 2025-09-05 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| ec7d1291-fb77-3d3b-b2f7-309ae7bd935d | -5.4917 | -60.138 | 2025-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 1feee6ec-4687-36df-965f-13e54e1dc8ea | -16.569 | -55.1174 | 2025-09-05 01:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 0903f86f-4bf8-3ccd-9d91-5f76aa7d8a3c | -9.2477 | -57.0697 | 2025-09-05 01:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 22ff0d70-6209-34d0-9d0a-201e1c88adc3 | -8.0035 | -45.4373 | 2025-09-05 01:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 7249b067-b901-3a37-ac70-fa7186463aa3 | -5.4918 | -60.1189 | 2025-09-05 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 8dfcad74-512a-3070-94ee-5310af01bbb5 | -6.5856 | -44.564 | 2025-09-05 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 3193c912-0fd7-3151-b4f1-f30575b08b68 | -4.0789 | -48.0369 | 2025-09-05 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| e5ba875f-8f7b-363a-8db7-43f2d28d2052 | -14.2892 | -45.2134 | 2025-09-05 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 58a311ac-83e8-37a4-a19f-d704539dea40 | -16.5686 | -55.1383 | 2025-09-05 01:30:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 45.0 |
| 15313d76-2f43-3ae8-97f6-0e87e009851f | -9.2102 | -57.0918 | 2025-09-05 01:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 42.3 |
| f2cf82f4-2ce0-39f0-a8f6-129bbdf90290 | -5.4917 | -60.138 | 2025-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 72a36464-037e-336c-a012-9f9ef3ff5925 | -5.5892 | -45.0278 | 2025-09-05 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 47.7 |
| d648860d-67b7-3e62-87d6-0bc024050737 | -8.0223 | -45.4354 | 2025-09-05 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 7dced2e6-e683-303c-8f27-936262eec712 | -16.5686 | -55.1383 | 2025-09-05 01:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 73.6 |
| f39ac495-d203-3982-96b5-c1bf4508655d | -5.6079 | -45.0265 | 2025-09-05 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 738c6f72-2ad1-35b7-93e6-42dd48839b83 | -8.0035 | -45.4373 | 2025-09-05 01:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| a00009ee-e88c-3836-aa1e-625b4e7326d6 | -5.6081 | -45.0038 | 2025-09-05 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 0691e9a9-5382-3bd4-99ce-be8962cd936b | -9.2477 | -57.0697 | 2025-09-05 01:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| 759c88b2-f0ad-305e-8b87-defebc3556c5 | -16.549 | -55.1409 | 2025-09-05 01:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| a077a227-c811-3f93-8fb3-21a7d9ab4b95 | -4.0789 | -48.0369 | 2025-09-05 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ccc924b5-8d4b-3425-a819-9c52e6d0f73a | -9.2102 | -57.0918 | 2025-09-05 01:40:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bfee8752-aa8b-34c9-8b2d-e0785300852b | -5.5101 | -60.1183 | 2025-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 86ea033a-aea3-3825-9484-2f5ff34bf31b | -16.569 | -55.1174 | 2025-09-05 01:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 350c18c6-5928-3cb2-a7c8-37945ab0eac8 | -5.4918 | -60.1189 | 2025-09-05 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 992b6184-fcc8-3188-86d9-7e4174cfe709 | -16.5494 | -55.12 | 2025-09-05 01:40:00 | GOES-19 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 102.0 |
| ba005544-35d8-3d47-bf45-8d5a41ee0a57 | -15.1961 | -52.3746 | 2025-09-05 01:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| a35627ce-303f-362c-9fd0-f82f1e690642 | -22.6205 | -47.9297 | 2025-09-05 01:50:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 77.2 |
| de0ecec2-6594-3f26-b4d8-1536fc79d9c5 | -5.4917 | -60.138 | 2025-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 3238b5c0-21a4-3a4c-9240-59e83a115616 | -6.5856 | -44.564 | 2025-09-05 01:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 7a0240d0-d5af-352a-a7fc-afc252aca40f | -5.6079 | -45.0265 | 2025-09-05 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c3b4c306-9786-3209-88c3-23e9fb2818e4 | -5.5892 | -45.0278 | 2025-09-05 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 79908b9f-400a-3227-b815-3e6ff7abcaca | -15.2156 | -52.372 | 2025-09-05 01:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8657b8d9-d16f-3266-8ba2-5ccc2e311650 | -5.5101 | -60.1183 | 2025-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 43facc9a-fe12-304a-af9f-d259a83da955 | -5.4918 | -60.1189 | 2025-09-05 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 256459ee-b4fa-3497-93cf-3c8db217cd23 | -8.0223 | -45.4354 | 2025-09-05 01:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d282f14e-5ebe-35a6-85de-cc0fb356f9eb | -22.6197 | -47.9535 | 2025-09-05 01:50:00 | GOES-19 | SÃO PEDRO | SÃO PAULO | Brasil | 3550407 | 35 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 9dfe3a7b-1387-3c69-a20b-6d6e085e3db9 | -5.6081 | -45.0038 | 2025-09-05 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 80412f69-c807-3f2a-98f4-0fd79079233d | -9.2477 | -57.0697 | 2025-09-05 01:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 0b7bec52-0e73-3c47-a504-197267d59631 | -5.6079 | -45.0265 | 2025-09-05 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| b53b5e09-bc60-3b2e-bbb7-6e6908f1b59a | -8.0035 | -45.4373 | 2025-09-05 02:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 9f116a5a-bc22-3c1b-870b-37839cd06acb | -9.0765 | -46.9891 | 2025-09-05 02:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 4f4b16e8-e6c7-3595-8693-0c314ccac56c | -5.4918 | -60.1189 | 2025-09-05 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 76679c09-fdfb-362e-af09-8a7e63f5a245 | -9.2102 | -57.0918 | 2025-09-05 02:00:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 964f278b-62e5-3f29-a935-9d9db2c12043 | -6.6044 | -44.5624 | 2025-09-05 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| fc1cc7ec-f7f9-3435-83e4-334e6e271010 | -8.05121 | -71.05288 | 2025-09-05 02:09:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ce617b33-a39a-3af1-9948-bbce84fe392d | -8.75509 | -69.33913 | 2025-09-05 02:09:00 | TERRA_M-M | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 80b56b8b-6ab7-3895-a65c-c636287569c3 | -8.05254 | -71.06226 | 2025-09-05 02:09:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 876172ff-bf73-3a87-a4bf-65d961a317b7 | -8.53066 | -70.73244 | 2025-09-05 02:09:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 661a4327-1513-305d-80bb-f6e8f28049a8 | -8.66113 | -68.76817 | 2025-09-05 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 926e659f-e414-383b-aacc-cf09e3b3bd85 | -10.08333 | -67.94534 | 2025-09-05 02:09:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 2378f29a-4550-3dd8-a616-17d603975965 | -8.65751 | -68.74368 | 2025-09-05 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| db365154-179b-3c24-bfc7-02a3a464d19a | -5.5892 | -45.0278 | 2025-09-05 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.1 |
| e5ff9869-e7eb-3a4e-9ba2-a0081ac48c9e | -8.0223 | -45.4354 | 2025-09-05 02:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 9f6840bb-7c09-3ef1-84ee-9853c62f9c66 | -8.5187 | -51.3293 | 2025-09-05 02:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 2a42cfe3-f65f-3f6c-8d18-56840adb1772 | -9.0765 | -46.9891 | 2025-09-05 02:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 53.0 |


[Clique aqui para ver as próximas entradas](README13.md)
