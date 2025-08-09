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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2743b6bf-6dfa-3bff-bf64-74285f11f070 | -10.44285 | -50.97806 | 2025-08-09 05:04:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6cfc550-60b2-3e67-9911-582cbc9d6394 | -6.13216 | -42.97367 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| de7342c1-5c3d-3a0a-a434-aa27fecdc628 | -9.86395 | -44.70567 | 2025-08-09 05:04:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 941eb15c-6d1f-3d2b-b8b0-d7d15a00d9e9 | -7.07523 | -59.17082 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| ddcc27b4-8940-3dd1-a09f-271775d05646 | -7.45861 | -60.40899 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81f2509e-ba52-3947-b7c4-06c5463d7a68 | -6.34529 | -55.56333 | 2025-08-09 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e4049e9-5e42-36e6-bdf5-5fa9ae4909c8 | -6.66802 | -43.34573 | 2025-08-09 05:04:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 10ec8b6c-dcd4-3f99-9216-22a23d468c89 | -5.90331 | -57.71228 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d3d6fd5-ed4f-3e0a-bb18-985c16bfcc66 | -8.92426 | -60.74091 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 337955a9-b90e-3520-af11-843ec810580b | -7.39923 | -60.00019 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8ed94bab-beed-347a-a186-bb6c68190996 | -6.62385 | -47.29314 | 2025-08-09 05:04:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dc08ce5e-af5d-300c-a5c0-557f565f152d | -11.9409 | -44.54668 | 2025-08-09 05:04:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc02eacb-67ea-304f-b3fb-bd816926c570 | -12.49508 | -47.50929 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7b85722-68ba-3b75-bd0d-c851306ab829 | -7.11096 | -46.10849 | 2025-08-09 05:04:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90b46acf-ce0e-3976-8d32-d0de5bc8396b | -11.09164 | -50.46824 | 2025-08-09 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c02591a9-b066-3eb0-b780-850ac6594e52 | -7.08377 | -59.16367 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| da798d84-e06c-3277-bfde-0324655b80df | -7.07456 | -59.17496 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 62167ee8-cca7-38e8-9705-6eadd16f74e6 | -8.92728 | -60.74636 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5550f9ad-0876-3e58-9336-2d4d625ba424 | -12.68736 | -48.20281 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cfe2762-ef51-3c4e-816f-3a3fa57912c8 | -12.48999 | -47.50488 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc92c76a-cc00-3454-a428-831b968c64ae | -12.68801 | -48.20599 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a75f3354-80c3-3a0b-94ee-ac943867ab31 | -9.70983 | -61.30418 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a37fa6ed-eb57-3952-8648-b51f1d2c6572 | -10.44889 | -44.34132 | 2025-08-09 05:04:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d436922-eea6-392c-a27c-1fdd68f22307 | -8.86284 | -47.27681 | 2025-08-09 05:04:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f101f1e-535c-35c6-976b-9a3241666281 | -7.40445 | -60.01503 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4b1a6f-1e3b-379a-a6eb-040de6a28a65 | -9.93857 | -60.50911 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7302927a-d23c-3c59-a7f4-51c29b5c0b11 | -9.9379 | -60.49048 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04cb326f-9a79-34ce-b186-876c185c91d4 | -9.51237 | -45.42723 | 2025-08-09 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3b30a78-5182-340f-af2e-4b762f03e5c9 | -11.93297 | -44.54208 | 2025-08-09 05:04:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22fb6727-5b91-3866-91f1-15006f1a2416 | -9.94391 | -60.47766 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dc02116-4ed3-322d-944d-cd003da85bb9 | -7.05837 | -59.20644 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9b5a2ce6-1944-3fc3-a1a4-0cdcb4436803 | -7.24331 | -60.00168 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2fe3f79-9e82-3352-8995-5b9478300875 | -8.92891 | -60.73675 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4cbce6ea-848c-3f9d-9558-269441128e14 | -9.71155 | -61.29412 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa276d2e-6ad0-39a0-99f1-a78912c0f984 | -5.2377 | -56.06065 | 2025-08-09 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f73225a-aaca-3c60-8aa8-8e9917de0202 | -7.08445 | -59.19192 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| adfb006f-92ed-384e-b9a4-a2b90c9120d6 | -8.72692 | -49.74249 | 2025-08-09 05:04:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 414e7902-a5d8-35de-bbb0-ac68366ed574 | -7.06266 | -59.20284 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 2f83ac76-f7bb-3024-90e2-a702b43e8ad2 | -7.09524 | -59.19374 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ce236307-4257-3e4a-ae80-ff6fdd7306cb | -7.07389 | -59.17911 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 3451e979-9a21-3e49-aa45-dd59b99ecefc | -12.41002 | -47.78543 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b28304d-ddc0-39b1-a4dc-3509c514ac80 | -7.08432 | -59.17052 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.2 |
| 2937a885-0dfa-3473-8c34-3a4a265e6312 | -7.07643 | -59.17352 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| ea77d3d3-49ea-3ed0-ab53-37af649dabac | -7.39847 | -60.00471 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bbdf793b-0ea1-39f5-93e6-f713bf170bd4 | -7.09151 | -59.17171 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 75ada27f-4cad-36e6-af00-895ac1c62712 | -7.05252 | -59.19687 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 9efbba42-3963-30da-978e-afacc6509c6f | -8.05817 | -46.32981 | 2025-08-09 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b3d4b24-7f71-3f7f-8699-674e4653b959 | -7.71788 | -57.74802 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b99b9780-6ae9-3806-a2e5-97f4176699f9 | -7.09303 | -59.18481 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9d991a3c-f26d-3914-8fd4-58b452608ae7 | -7.05162 | -59.17971 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2ad9d86b-3b18-353c-8b7f-75e74175a320 | -8.93273 | -60.73742 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b51eae6c-7169-366a-9629-bce1922098b0 | -13.05006 | -43.84386 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 777ac8bf-d0b0-3f84-9368-c863e9907151 | -9.05883 | -45.07629 | 2025-08-09 05:04:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4ef1751d-c228-3a17-a659-8e416be41686 | -9.94458 | -60.49627 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d750d4e1-84a3-3a5e-823d-7dfa92c2b63e | -6.12105 | -42.95423 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2d56f06a-d729-353a-b12e-784b5de040c3 | -7.40299 | -60.00075 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99383b18-ab24-31b1-8dbf-bc0f2285b00b | -7.05973 | -59.19805 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| ab237b2d-77de-394c-891d-4a1c5f1ee7cf | -7.07435 | -59.18594 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 8691bdb1-0e73-397c-b348-6ace3f812301 | -12.56108 | -47.10231 | 2025-08-09 05:04:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad1559ff-2f95-32aa-93f5-d27ada699bfc | -11.93429 | -44.54587 | 2025-08-09 05:04:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4d1f0fd0-7bf4-3be7-952a-463a872d0681 | -5.8872 | -57.74817 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 174ba918-e908-3d9b-b1f6-5a4d31f84843 | -8.92182 | -60.75528 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f805e2c3-419e-3a8a-bec9-fb75dfbc2281 | -7.05949 | -59.17677 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 8c2c4556-562e-33b9-b56c-9aedcda3c4ce | -8.59635 | -62.66826 | 2025-08-09 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 68cdf148-eb93-37be-b5ed-8ac4f94ff8e2 | -7.05769 | -59.21064 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3e797697-ab3e-3a81-ad02-fe311fb2b41f | -7.40223 | -60.00528 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04a6b841-4560-3fa9-9325-b10f4b6da339 | -7.0651 | -59.16497 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 708feb96-061d-3739-a78e-b9779b3f357a | -12.68313 | -48.20203 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a3fc9681-8cf3-3e0d-b706-cb2e86128ade | -9.46864 | -57.85141 | 2025-08-09 05:04:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2652c556-c52e-3586-bfd3-9a61e86fb8bf | -7.45943 | -57.65783 | 2025-08-09 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be14fa10-580d-36d4-a0b1-f414941cd14d | -7.08085 | -59.19131 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 12782c0e-a572-36d8-95a9-7a610eee8f02 | -11.09181 | -50.4996 | 2025-08-09 05:04:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39eacede-e54b-3a99-a9da-fb7949f0b971 | -6.20419 | -55.6191 | 2025-08-09 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 56d56182-8cfd-31f2-9287-9ba8fc4bc8c1 | -6.92956 | -60.06944 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c2fa10f-d1db-3040-afa9-9c59533b88fb | -7.04823 | -59.20049 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 58836066-9826-3f62-9f44-846eb3200c59 | -7.40146 | -60.00985 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 133aa32f-d4c5-3f1e-ba1a-e21ea67dc430 | -8.91498 | -60.74911 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a06c5a6-9dc1-3a52-b960-25ed17b2aa1e | -6.12213 | -42.96061 | 2025-08-09 05:04:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aa81a696-778d-33a7-bd6f-c40859184421 | -8.93111 | -60.74701 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 4173e285-998b-39bd-a08d-ca8393ef2f41 | -6.09607 | -59.92292 | 2025-08-09 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5ed47e2-0b29-39b3-8f0b-56bbbe8b98bf | -7.06469 | -59.19031 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| c7ffabc4-7356-30b1-b629-77726ba35367 | -8.92647 | -60.75115 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c603e43c-6d1b-31ea-830f-b89d59038c0d | -7.06443 | -59.1691 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b8406a05-6308-3760-8b81-618c49ac3bf2 | -7.0613 | -59.21125 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30006f9c-5031-35d3-8b89-55b5c545e659 | -8.90775 | -60.5423 | 2025-08-09 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42cb48b2-f075-39c2-811e-0058caf9d2ac | -12.05499 | -51.88066 | 2025-08-09 05:04:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 492a248c-cee1-38de-b391-8fb5c1f4ec87 | -11.77421 | -47.40036 | 2025-08-09 05:04:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b76d91d-637b-3cc1-9e90-89c692b9088c | -7.06016 | -59.17266 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| bee11671-356c-3596-a88f-61f9cc81da7e | -7.05228 | -59.17561 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 6d29cd4a-0ce6-3c33-aefe-0e1990fdc66e | -9.52205 | -45.40835 | 2025-08-09 05:04:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53f9e85b-b4d1-3e30-b5fd-79db2ab3c8bc | -7.06803 | -59.16968 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fc42994b-896c-3cfb-b7a7-210aef80a0a6 | -9.94162 | -60.49113 | 2025-08-09 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4920d790-068e-3995-80c0-8c0406652d9f | -5.00356 | -56.0375 | 2025-08-09 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b1992bd-7b82-3547-adfb-5a060b738da2 | -7.09082 | -59.17587 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 92189707-e31f-3e6c-a3ef-81c879e4f3ba | -7.07841 | -59.19698 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0d72764e-7878-33d4-839b-ee5b78e7e1a4 | -7.07586 | -59.19903 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c7ce2e61-61b1-3512-a5df-b085072d5235 | -7.25048 | -44.32167 | 2025-08-09 05:04:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b617ba8d-fb1d-3964-a4ff-38b618232c0f | -7.05476 | -59.20587 | 2025-08-09 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c44a10ae-c69f-3e56-a68c-d07b93eac699 | -12.71784 | -47.79401 | 2025-08-09 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a5006d60-ec1e-3ad3-a88e-ee2fefdf0153 | -13.06433 | -43.83301 | 2025-08-09 05:04:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README28.md)
