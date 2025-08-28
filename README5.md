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
| 299131ef-23df-3743-b855-2a8e1d8c3d91 | -4.43046 | -45.27191 | 2025-08-28 00:11:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f9dddac6-e6d5-3bcc-addd-929be012c79e | -7.12364 | -38.53144 | 2025-08-28 00:11:00 | TERRA_M-M | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 14.7 |
| f0b6d21f-1e78-3033-bb9b-852649001586 | -3.78969 | -45.03708 | 2025-08-28 00:11:00 | TERRA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 36.4 |
| d7917144-c95d-3a14-8626-aa5df40d8e4c | -3.79097 | -45.04647 | 2025-08-28 00:11:00 | TERRA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 6eeea624-a453-3ad7-b4be-5803b0b0bb9d | -7.79232 | -43.18556 | 2025-08-28 00:11:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| eb1ce181-8e67-3ff8-af18-d17b3b09c839 | -6.16046 | -44.18336 | 2025-08-28 00:11:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 39d9c3a3-e55e-36e4-b6fc-0b34f8ca35d5 | -8.9479 | -65.9616 | 2025-08-28 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 174.0 |
| 0931fbdb-02c1-3ca3-a971-ff58a1a96230 | -4.8079 | -47.2604 | 2025-08-28 00:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| ffc336b2-5b29-3921-990e-41f2e412f1e6 | -9.0786 | -65.7338 | 2025-08-28 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 14119ab8-79b0-3b5c-a9f7-9460a7adf89f | -8.9664 | -65.961 | 2025-08-28 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| f3d96601-597a-3306-87d0-542f3f58fd97 | -6.9129 | -62.9366 | 2025-08-28 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 84c6f291-90ac-3c70-aeb9-5ee90f56b1ae | -10.5375 | -46.6894 | 2025-08-28 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 172.9 |
| ffa72ef2-a988-30bc-875b-5b90260a410b | -9.406 | -60.5711 | 2025-08-28 00:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 1b692b7e-2ee5-3c8e-b87c-f4580542ff11 | -3.23 | -43.4182 | 2025-08-28 00:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 90.2 |
| b97bd7ea-81ef-365a-a0d3-05aaca9818f0 | -11.3526 | -43.5187 | 2025-08-28 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4d57fc70-ad6a-3a67-b57b-4f1c973ac690 | -9.0971 | -65.7332 | 2025-08-28 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 01fc29f2-bf51-33b6-89aa-c384ecbb8103 | -9.1177 | -65.2842 | 2025-08-28 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 543b5397-e857-37be-b077-a4d75f70e8e2 | -11.3334 | -43.5216 | 2025-08-28 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 4e2c3635-6ac7-3e56-a916-f422ce25585d | -13.7373 | -51.9077 | 2025-08-28 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 86.4 |
| a6281820-5bb2-331a-a1e1-82b2701f01a6 | -13.1837 | -45.2865 | 2025-08-28 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 3f5cafcf-0f45-30c9-98d1-3451f9aae6cc | -8.948 | -65.9429 | 2025-08-28 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b1a50723-84e1-3f42-9656-bfd41e885e82 | -11.2189 | -55.0585 | 2025-08-28 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 8293d72d-073d-39f8-bc63-ee72a1d42a00 | -9.1363 | -65.2835 | 2025-08-28 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 149f00e6-a15a-31f0-b893-6c29f1c807aa | -3.2485 | -43.4406 | 2025-08-28 00:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| f5ebf9c3-9bdb-37df-a79c-937a797f7b00 | -7.3357 | -59.6484 | 2025-08-28 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| d3747dff-4a5e-397d-ba3c-b4964402c765 | -6.8772 | -43.6152 | 2025-08-28 00:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| e0a63725-133a-329a-b0db-9610a03202fc | -8.9478 | -65.9802 | 2025-08-28 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 80d3d0bb-2519-32f5-b09c-2455fd85dab5 | -10.4736 | -57.9563 | 2025-08-28 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 0d6b56b5-1306-3049-b36b-4f01abe6c1ea | -13.1842 | -45.2633 | 2025-08-28 00:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 059d890a-60a4-39f1-a498-857e49da7bd9 | -11.3521 | -43.5423 | 2025-08-28 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1d38b87f-35ee-3e35-b4e9-b19e71e993a0 | -14.3693 | -52.1026 | 2025-08-28 00:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 64498e5c-3da9-3185-8a73-ae8d6d78f077 | -10.5565 | -46.6871 | 2025-08-28 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 6d3b5463-44f3-3e6b-bc02-474add66baad | -10.5371 | -46.7119 | 2025-08-28 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 09f82bd5-c1c6-3b27-be53-e91a5ef9ff8c | -5.3285 | -55.8878 | 2025-08-28 00:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 7b59fee4-c361-3e90-96d3-70f18b1d6f66 | -7.3542 | -59.6476 | 2025-08-28 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b2d31ced-38a8-35ee-aafb-8ad9082d9c15 | -10.8421 | -60.8009 | 2025-08-28 00:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 6d393b13-7de0-3d2e-813a-032a579daccf | -7.4283 | -40.079 | 2025-08-28 00:20:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 81.0 |
| e9578397-e2a2-3e3e-8707-6ca3f9f2ac98 | -12.8032 | -48.1516 | 2025-08-28 00:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e73d70c8-4e8b-3834-8d38-80aa9472379b | -8.9665 | -65.9424 | 2025-08-28 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 5b43ee44-ad44-3f14-8dfd-72646563b7d2 | -10.4738 | -57.9366 | 2025-08-28 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 122.7 |
| db18caaa-ce84-3ac3-936b-658bfa992fae | -9.4864 | -51.9387 | 2025-08-28 00:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| ee43b4cd-7d19-35ae-9095-7aa16c185f6b | -11.2378 | -55.0569 | 2025-08-28 00:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| b7bf168e-3e2f-3934-a98d-03c9c0d04513 | -13.7566 | -51.9053 | 2025-08-28 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 81.8 |
| dfa642aa-9a4f-3c61-891b-dd53068c7bf7 | -4.7893 | -47.2614 | 2025-08-28 00:20:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 94.2 |
| f1a81a4c-4e97-3694-aa47-922b4d27f918 | -3.2299 | -43.4414 | 2025-08-28 00:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 284.9 |
| f06037d4-d5a0-3284-9a33-9eed3d874be1 | -3.2298 | -43.4646 | 2025-08-28 00:20:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e5ca276d-7623-3dc7-8a7a-e42adad71e23 | -11.3329 | -43.5452 | 2025-08-28 00:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| a7d99ab4-5563-3d77-b6c8-3ef49132d46d | -7.6242 | -60.8448 | 2025-08-28 00:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 50859275-c525-3a5b-a016-d3163d0337a6 | -9.1153 | -65.8073 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 86f429c9-ed37-35e7-b772-87e4957ed800 | -7.3357 | -59.6484 | 2025-08-28 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f96cd26d-936d-332a-af72-9ddbe5a1a378 | -9.1363 | -65.2835 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 7d861b1f-ddda-3ae3-9d22-b74aef69738c | -3.2485 | -43.4406 | 2025-08-28 00:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 778d9cb2-09a6-3737-86d8-e6d46b1bca11 | -10.4736 | -57.9563 | 2025-08-28 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 83.7 |
| f6e5bb31-5b79-3acc-9dba-6e932ca3eaa9 | -11.3521 | -43.5423 | 2025-08-28 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 14468bc9-6e99-38c8-86d6-6d5d221f4f75 | -4.8079 | -47.2604 | 2025-08-28 00:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 064f51ec-7428-3884-973e-33a5ba400104 | -12.8032 | -48.1516 | 2025-08-28 00:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 7bbf5342-3024-3429-9899-bb47c16c78ce | -9.1154 | -65.7886 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 447.5 |
| 58f09094-bf76-39a5-a197-559fd02540c8 | -13.1837 | -45.2865 | 2025-08-28 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 227.5 |
| ab5929d3-225a-38a8-b110-c4b82d79c9e7 | -8.9478 | -65.9802 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 414b25bb-3e58-301d-8705-3c916b62acba | -9.3169 | -57.6967 | 2025-08-28 00:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 121b1ade-e456-377c-ad5e-4643b8895736 | -13.7566 | -51.9053 | 2025-08-28 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| acaf293b-b487-32f7-be23-b4c8b042b61e | -9.1338 | -65.8067 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| de61f7eb-b72e-383e-a6c3-3277255a9b57 | -7.4283 | -40.079 | 2025-08-28 00:30:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 6e388a83-7d51-32f7-8916-eb20749276fc | -7.3541 | -59.6669 | 2025-08-28 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| ea0ccb47-bb18-323a-824d-d761812ce6dd | -6.8769 | -43.6385 | 2025-08-28 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 407ee5b7-be72-3a70-b880-d64c97b57035 | -3.2299 | -43.4414 | 2025-08-28 00:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 323.4 |
| 69eb46d0-ab71-3c77-a7f3-216a89bb922d | -4.7893 | -47.2614 | 2025-08-28 00:30:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| ed00f649-51f9-3a2d-9531-d49863fa3215 | -13.1842 | -45.2633 | 2025-08-28 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 61.8 |
| b5ae8e89-9793-39da-9866-36bf8c8b4f51 | -10.4738 | -57.9366 | 2025-08-28 00:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 888e52b7-2181-377e-b078-5bfd1848d62f | -6.9129 | -62.9366 | 2025-08-28 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 0f7c5536-13d9-38db-90fc-55ca398cd176 | -13.7373 | -51.9077 | 2025-08-28 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 2925fff1-2a7b-3589-8e92-cf55359c05f0 | -7.3542 | -59.6476 | 2025-08-28 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| eb0280fc-fca1-3f12-9bfd-6596ced898ca | -9.406 | -60.5711 | 2025-08-28 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 6ffa351c-35fc-3edb-b5d3-e79b0b15a35c | -9.4864 | -51.9387 | 2025-08-28 00:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 38933a78-a5dc-3893-ba22-1717e5a1c1a5 | -8.9479 | -65.9616 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 161.3 |
| a0d12bec-cf92-3194-9bc0-e5381d515b6b | -9.1155 | -65.7699 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 287.8 |
| bcc6cdee-42ce-321b-a519-bde008e9a37c | -10.5375 | -46.6894 | 2025-08-28 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 6e51bf55-2eba-302d-bff5-1e58c768b4cf | -14.3693 | -52.1026 | 2025-08-28 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 213e5849-1e83-3d1a-8e9d-4c6af54c6f84 | -8.948 | -65.9429 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 8ea7410d-7853-316c-a5aa-4bd8ffe393c8 | -11.3334 | -43.5216 | 2025-08-28 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 55b4df93-a93a-3b31-99f9-c2bb04dd8293 | -5.3285 | -55.8878 | 2025-08-28 00:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| af3cded3-eb20-385f-8023-716797120b9e | -10.5371 | -46.7119 | 2025-08-28 00:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4466909f-9ccc-3ba3-96e4-6687adb4a304 | -11.3329 | -43.5452 | 2025-08-28 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 89344b84-2d06-356d-8f16-47fc0a1a85a4 | -9.4061 | -60.5518 | 2025-08-28 00:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 4fb29955-8313-3920-aba1-b4550bda230c | -9.134 | -65.7694 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 346.1 |
| 4b2e1caa-6fd2-3100-8792-836816d05d2e | -11.2378 | -55.0569 | 2025-08-28 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| bc5460f5-7c1d-3327-adbd-e6af44f79cd3 | -9.1339 | -65.788 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 533.2 |
| 86aeba2e-b920-3602-8722-91fd3cd3e716 | -8.9664 | -65.961 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 1f25889c-1a7f-3588-abc7-bca6db7d6624 | -6.8772 | -43.6152 | 2025-08-28 00:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 187a00a3-742c-3010-b13a-0ce7bec87e26 | -9.0971 | -65.7332 | 2025-08-28 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 3315bf07-0f54-3709-8c5a-1cd60fcb0bd4 | -11.3526 | -43.5187 | 2025-08-28 00:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 7167ca01-18da-34ce-8614-60d80e0d07e1 | -11.2189 | -55.0585 | 2025-08-28 00:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 103.7 |
| 30a71d5b-f0ef-3376-ad27-27c53aa333ca | -13.2031 | -45.2834 | 2025-08-28 00:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 976ce391-dae5-3dd7-8f08-0ec057b23dec | -3.23 | -43.4182 | 2025-08-28 00:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| ae7b7f0f-5f2b-30ea-bec8-656e262e1c0b | -3.2298 | -43.4646 | 2025-08-28 00:30:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| ce034db5-ca38-3f6a-b873-7bce37eac51f | -14.3696 | -52.0813 | 2025-08-28 00:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 07f1e225-5c72-3a9b-98bc-946c861826e1 | -6.896 | -43.6135 | 2025-08-28 00:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e6a59afe-c144-312d-a2b8-8e4ca255e54b | -6.9129 | -62.9366 | 2025-08-28 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 57ea711e-5277-3fab-9af0-06009e1d11a3 | -8.9664 | -65.961 | 2025-08-28 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 4c7a9d9e-74b8-390b-b61c-d67663b18e51 | -8.9479 | -65.9616 | 2025-08-28 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 131.8 |


[Clique aqui para ver as próximas entradas](README6.md)
