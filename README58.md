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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80aaabe5-305c-383b-8619-687f51e9095a | -7.19714 | -42.1884 | 2025-10-19 05:23:00 | AQUA_M-M | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| b1a9506f-ade3-36a9-8db9-60375420a6f7 | -2.91475 | -52.72623 | 2025-10-19 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ec568f3e-b7d5-373c-98dd-92d9a20f04d5 | -2.91549 | -52.72136 | 2025-10-19 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 149882f7-7a3d-3d52-b871-ad7e1c41d3e3 | -2.91932 | -52.72712 | 2025-10-19 05:23:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 044bbd9f-0854-31bc-b3b4-8c2cc8e3e859 | -3.54992 | -54.69445 | 2025-10-19 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c53a1c7e-ca9a-3b85-bdec-518c21c87090 | -3.15891 | -49.16732 | 2025-10-19 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 67f06da5-b3af-341a-9690-1702e6357cfe | -3.59419 | -53.95798 | 2025-10-19 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ea1b4862-45b8-3706-99fb-2dea10dd6ac8 | -1.80077 | -57.13441 | 2025-10-19 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 565b9f41-4ad3-36c0-bf9d-1d426078a2fc | -11.37988 | -61.21177 | 2025-10-19 05:23:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cea640e3-df9a-3ac5-a52e-a6df3c0b2e91 | -2.6861 | -49.54598 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 6c63488b-c8a6-30bb-8a28-6a17f469e958 | -2.86414 | -50.7334 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b9cc1ce-3e5c-32e8-ac45-ee3666be666d | -9.7403 | -65.88282 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b147ae8e-92fd-381e-9225-3d74a3417f6b | -8.93943 | -64.12643 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcd0236f-8ed1-3581-9852-4884c8186021 | -4.27243 | -48.88089 | 2025-10-19 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3d0661b-ec98-35f6-bc01-fa81a4e76292 | -3.5266 | -55.47185 | 2025-10-19 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 214a8511-2059-3246-9d1a-082b45e7b4bf | -2.86317 | -50.73995 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 72836d29-8d3d-39b2-94ab-6070024a93ee | -2.59403 | -49.49924 | 2025-10-19 05:23:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db0fdca9-eab4-3f32-ae70-2ab1580ec0bc | -9.22085 | -61.82939 | 2025-10-19 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| bf6fb68b-a333-386e-bc04-75f11227ae9e | -3.80561 | -51.64496 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 921d0767-0ec1-3bcb-9ae1-df069a099bd3 | -3.13948 | -50.24508 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7137f1f7-f3f9-36f2-bc19-534410917c4a | -10.22621 | -44.88803 | 2025-10-19 05:23:00 | AQUA_M-M | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 236f9f11-0315-3216-af20-3cb45d71c2ae | -4.42152 | -47.75265 | 2025-10-19 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f0d29b3c-5128-3c3c-93ec-fb6393a7e853 | -3.0396 | -51.21325 | 2025-10-19 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5fdd00b8-67b7-39c2-b751-726d3e7dcf0f | -2.25286 | -51.91235 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a8358def-454f-37e8-b139-de184fa246da | -2.79199 | -49.64975 | 2025-10-19 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b1acf76c-b0e4-3b7b-b3ec-bf654be619e2 | -2.88043 | -50.7326 | 2025-10-19 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9376bda3-51b7-36e4-bba6-6c41a979f3f1 | -3.52779 | -58.36304 | 2025-10-19 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93710ccd-f0a5-36b7-90c7-9647b54a11d5 | -5.26116 | -50.90451 | 2025-10-19 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a0654fd-6862-3bf7-aa40-357e627708c7 | -9.69001 | -63.30666 | 2025-10-19 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b74bb26-3081-3575-9c64-30c96f3d68a0 | -9.73641 | -65.88213 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 770d4733-aa53-34f4-a528-624142b7526f | -5.35516 | -47.21384 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1bf58307-1ca4-3dce-9cfb-a3428701280a | -2.447 | -49.36159 | 2025-10-19 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 096dc821-aa4d-34ff-b0e9-aabdf3fa64f5 | -5.35378 | -47.21523 | 2025-10-19 05:23:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bcf5c96a-876f-345c-b845-d545409df0ef | -9.26617 | -62.46489 | 2025-10-19 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 48476415-3812-3d81-ae89-433c5dad2036 | -9.64509 | -65.25394 | 2025-10-19 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fefacbd-a22e-38c4-b73f-5768e9c778e8 | -7.17769 | -59.3502 | 2025-10-19 05:25:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98d1897f-12e5-345e-9d16-4447d664d0cc | -9.42685 | -59.0149 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| efb3bd46-ca47-3191-84a2-f29d163499a9 | -7.90022 | -63.44395 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7becde3f-7e13-357f-b18f-fa4141692247 | -8.97336 | -61.97279 | 2025-10-19 05:25:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b59d3fb-05a8-3af6-9d0d-ad8ac9f3a30f | -7.15751 | -59.61591 | 2025-10-19 05:25:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e40b9c2-814c-31d2-b381-269b15e1a42b | -7.12161 | -63.04587 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76e8478f-b5ce-3862-89d8-afc1b8ded0b0 | -16.79901 | -42.8246 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 217ecf84-0fa8-34b2-969e-5bc360457525 | -9.18552 | -61.38444 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5afbb476-2078-3e1b-be96-7b3befab37d8 | -16.75411 | -42.77564 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| a296e312-5220-31df-8d27-10cd2deab95a | -8.05223 | -55.09295 | 2025-10-19 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37745896-600b-3036-be8e-d1a50a5dc2d5 | -9.30935 | -60.87414 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5927d1a-06ea-37f3-8185-0746dae7f3cb | -8.22933 | -61.49057 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04a37803-ada3-3fc1-bcb5-178d133d8975 | -16.76389 | -42.77725 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 384.3 |
| 37fc1180-9547-3664-b0b8-7ec83138efbe | -7.67318 | -63.50122 | 2025-10-19 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a409054b-e207-3e74-9c13-d9307d4e49cd | -8.5423 | -64.13728 | 2025-10-19 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a468e79-df21-340d-905b-c340018dbb0e | -9.23267 | -57.69166 | 2025-10-19 05:25:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df7e0890-49a1-3b18-aa18-f467b6060138 | -7.61828 | -60.94128 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d653c3e4-323a-338b-85ca-f4fab11a942b | -7.82061 | -61.68642 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e43be62-b0ac-3b52-90f6-65b72ba16c4f | -9.18882 | -61.38497 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 7dd8ecee-4f85-317b-8aa4-bc0d791e9a04 | -9.17445 | -60.43077 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4d71e00b-f0fd-3401-a89f-a5d0e99dc187 | -13.01797 | -62.35587 | 2025-10-19 05:25:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b9d0e47-4379-32dc-946d-163ecfc185ce | -7.90704 | -61.67855 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f36af679-a9db-317e-b497-c4d8405524f2 | -16.76576 | -42.76596 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 0043bd3c-db54-350c-bc02-78002fb64a92 | -16.81072 | -42.81486 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5720318a-1c59-372d-b0e4-75e9e2a2ffe4 | -7.62104 | -60.94525 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c0a9c31-9b80-3d12-8df7-fa1bb115dbe8 | -9.14269 | -61.46304 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c1c696d-e728-36b8-923e-986fec62e41e | -7.88341 | -61.18237 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d52f25bd-2506-3074-a157-c5f2805e66de | -7.6238 | -60.94923 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a2815a0a-45dd-397a-822e-94a84e8fda7c | -7.12368 | -63.04568 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dbdfb97e-c527-3a39-81c4-822d8c809ad8 | -8.60444 | -64.08665 | 2025-10-19 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2e9d0ba-1a7b-3e2b-85f9-fce335621720 | -16.75598 | -42.76439 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c8572473-a113-3354-83f4-4da2d615c882 | -8.60802 | -64.08725 | 2025-10-19 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed91c3f6-7ab1-396f-b0cd-f12121c83d18 | -7.62651 | -60.93195 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6faec60a-8ccf-32a0-a36e-ca4867b884df | -7.6767 | -63.50179 | 2025-10-19 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24344a6f-7eb7-30b7-8b80-dd50f4f5c746 | -16.14746 | -41.15466 | 2025-10-19 05:25:00 | AQUA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 1ee8cea0-c3e4-3fb6-874e-c97da05cac02 | -6.74295 | -63.05788 | 2025-10-19 05:25:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e46792e-d8ab-34e6-a186-ffac2744d0ff | -6.64694 | -62.91222 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09f80861-bf5c-30ef-9198-72b743c7066b | -6.73884 | -63.0612 | 2025-10-19 05:25:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7eab09d8-bb42-3818-94ce-ef94464b94a3 | -16.77555 | -42.76744 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1bd96a6c-74b5-3ba6-9e49-06bf10945171 | -7.85882 | -61.59555 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09a30a43-db0e-364b-8c8a-b3014279cb04 | -7.62483 | -60.92108 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e227d20-ee66-3f56-adb2-150f83453666 | -6.6504 | -62.91278 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da09379c-8f24-32c8-aaeb-2cb21faf8ee0 | -8.22548 | -61.49353 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 069a71a3-9350-3e56-bbf6-09247be1d370 | -7.12508 | -63.04643 | 2025-10-19 05:25:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0a7165b-7967-3eaf-980e-93f65131ac9c | -7.87956 | -61.18531 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 537cb109-bbd9-36d7-b1bd-f86944f62aa3 | -7.63482 | -60.96513 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3fe703b-9fd1-3011-8d3a-6a7cf8bb235e | -9.15372 | -61.50042 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3b9be81-866d-3cce-af5f-696a730210dc | -9.30881 | -60.87761 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e45caf3d-049c-36ba-8add-fb4ffdb88d02 | -7.62325 | -60.95268 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28243023-09ca-3a24-8912-6b4dd0e795ad | -7.62822 | -60.9641 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf25fab8-6e8b-3c00-b601-dc2de5a6e754 | -7.63152 | -60.96461 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1785f93-1eec-3542-875c-5f60ebce1d09 | -8.60733 | -64.09138 | 2025-10-19 05:25:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 449e8e6d-c9c6-387c-bf81-c91bbf499503 | -9.15038 | -61.88651 | 2025-10-19 05:25:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81d305a5-87e0-3516-988a-7bc2c62a701a | -16.80092 | -42.81326 | 2025-10-19 05:25:00 | AQUA_M-M | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.8 |
| dfe9c1db-4a54-3e2b-82e3-787a2acf89be | -7.63428 | -60.96859 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2fa561b2-4086-3e5a-9f88-464070b9006f | -9.31211 | -60.87812 | 2025-10-19 05:25:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7f62a10-2e00-350a-9307-66ece321c5bb | -16.13921 | -41.14749 | 2025-10-19 05:25:00 | AQUA_M-M | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| b9a2f045-ce54-3993-be1d-30f778ac97f0 | -9.572 | -58.8886 | 2025-10-19 05:25:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4ebdf31-8343-3e27-86de-16a934f5f21e | -7.86158 | -61.59958 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a284041-d5fd-3f78-8da3-e4516c8d0b2b | -7.81673 | -61.6894 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b030acd9-094f-33e0-bf34-c3fefa2dc06d | -7.81054 | -61.34084 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7d8c9d4-da90-3280-952c-96bd51a9debf | -9.15094 | -61.88299 | 2025-10-19 05:25:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a94ae658-f57b-34e7-9314-13cba09bf9c2 | -15.73712 | -44.6009 | 2025-10-19 05:25:00 | AQUA_M-M | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 153358cd-e613-3e0f-81ed-d56a32a6dfd1 | -7.61996 | -60.95216 | 2025-10-19 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30d7e660-76ab-3fb7-8748-ee8b47e0e4c8 | -7.81 | -61.3443 | 2025-10-19 05:25:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README59.md)
