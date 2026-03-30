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
| e35b2eb0-767b-3c02-ac8f-93fa17fc1318 | -19.14816 | -53.0046 | 2026-03-30 00:56:00 | TERRA_M-M | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d3655471-4f73-354e-958c-21822bdde8da | 3.80331 | -60.18552 | 2026-03-30 01:05:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f109d254-c77f-3e4e-9d4d-4178b2366ae6 | -19.60511 | -40.10069 | 2026-03-30 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7ad94334-090b-33b8-ad41-f7912c9f526c | -19.60114 | -40.0777 | 2026-03-30 03:40:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e3849395-9838-3b26-995a-aac9da50d0bb | 3.4956 | -59.845 | 2026-03-30 03:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 45fab469-f320-3246-86ac-e93fb0bd1d72 | -12.34182 | -48.22534 | 2026-03-30 03:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db656371-0cd4-3965-b5d6-84484e43046d | -12.63703 | -52.14186 | 2026-03-30 03:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8bf9fa2-1b8a-3d5a-adff-79e3e2047077 | -12.63594 | -52.14702 | 2026-03-30 03:57:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a3e69a3-f5c6-3ccb-ad3a-9c386b6634f3 | -12.8378 | -43.84754 | 2026-03-30 03:57:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 294d2a80-35f8-38d1-8665-ea30f719a3ff | -12.34125 | -48.2283 | 2026-03-30 03:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3246aa27-4c4e-3994-a57d-73791c2a27f7 | -14.8718 | -46.56611 | 2026-03-30 04:00:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ede914b3-e30b-375c-baaa-718ef0f216e7 | -13.65118 | -47.47774 | 2026-03-30 04:00:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 31ba581d-00d5-367d-8040-7ee6eb44325e | -19.59986 | -40.07773 | 2026-03-30 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7bf2956f-4616-347f-a99f-1d81aef13acc | -19.60043 | -40.07394 | 2026-03-30 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d0b2b539-2311-36b6-b7b5-43573e38fcfc | -16.92123 | -43.59941 | 2026-03-30 04:00:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f902359-46ec-3b4f-8d31-ddea5fb27a39 | -19.60381 | -40.0745 | 2026-03-30 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1d693a88-0310-385a-b1c9-b2e0b392e526 | -23.60388 | -52.16734 | 2026-03-30 04:02:00 | NOAA-20 | IVATUBA | PARANÁ | Brasil | 4111605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 81ed3204-45c3-31b6-9f20-a7795fac0114 | -22.91425 | -49.20686 | 2026-03-30 04:02:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a6192d3-a9d0-3fdd-bfae-9ac66dbfa0b3 | -25.47522 | -49.863 | 2026-03-30 04:02:00 | NOAA-20 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0a47ec30-3cc6-37bd-bad0-49ff93e31f15 | -21.22168 | -48.94656 | 2026-03-30 04:02:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a6de9ac9-fe59-3527-b3b7-dc72294adb6f | -22.91861 | -49.20786 | 2026-03-30 04:02:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bed2cad5-981d-3434-bcc3-ea5fdb2b2ad6 | -25.47428 | -49.86757 | 2026-03-30 04:02:00 | NOAA-20 | PALMEIRA | PARANÁ | Brasil | 4117701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 24a013ca-20e4-3587-937e-de571470ee70 | -23.60314 | -52.17071 | 2026-03-30 04:02:00 | NOAA-20 | IVATUBA | PARANÁ | Brasil | 4111605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6ebdab37-d1e7-3de8-a989-5d8489d1d89d | -28.59707 | -49.11214 | 2026-03-30 04:04:00 | NOAA-20 | TREZE DE MAIO | SANTA CATARINA | Brasil | 4218400 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5db3905a-2e53-3503-9c1d-4aa74c308b02 | -9.51003 | -60.19085 | 2026-03-30 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28f8e302-5650-3452-8e17-cc0bf37f22a0 | -12.64 | -52.14391 | 2026-03-30 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 779bb09b-9572-363b-9e40-3be3725d0c59 | -12.63789 | -52.14091 | 2026-03-30 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c9e74ba-b297-380e-b795-5e86191500a9 | -19.41736 | -53.94991 | 2026-03-30 05:21:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecb515d4-c855-3d1d-bcd2-dbd3d206ab00 | -12.63731 | -52.14549 | 2026-03-30 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 29b19d41-7e38-33c1-bdc4-d09cfa93cead | -12.35169 | -54.14452 | 2026-03-30 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5b5f255d-6d9c-3bdd-9ffe-d8bfff5a55c3 | -12.63551 | -52.14326 | 2026-03-30 05:21:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef434fc7-f671-3b57-89df-a0ada29e975e | -19.29411 | -55.16208 | 2026-03-30 05:21:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 867ac2f5-a547-3b98-baac-e8cc4a1b819d | -24.07615 | -52.37974 | 2026-03-30 05:23:00 | NPP-375D | CAMPO MOURÃO | PARANÁ | Brasil | 4104303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7aa38636-b2a2-3ca4-ad8a-a173c9704be6 | 2.53927 | -60.80111 | 2026-03-30 05:36:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1630f5ce-f52b-32d2-b3c0-22c6d67f34e6 | -10.53032 | -43.63463 | 2026-03-30 11:47:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 86f7d83c-1791-321b-b0d2-3280c3d205ec | -12.83354 | -45.88214 | 2026-03-30 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 63.1 |
| ec64bc22-4cf7-3dae-85d9-ebda3840ce83 | -12.83215 | -45.89157 | 2026-03-30 11:47:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 209.5 |
| f36afe08-a08b-3df9-999f-c7d4408bf3cd | -8.43453 | -44.03316 | 2026-03-30 11:47:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 321ce8bf-1a3c-359c-866f-9376619ab96c | -8.43324 | -44.04204 | 2026-03-30 11:47:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 397eb2a6-efed-3516-9421-31b42aa2b067 | -14.87258 | -46.57342 | 2026-03-30 11:49:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2ffb1b82-9c62-3984-9064-c1490e8d681f | -21.82708 | -47.10512 | 2026-03-30 11:49:00 | TERRA_M-M | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 73186423-0b0a-318c-b287-3fe1ba976110 | -22.92556 | -45.79095 | 2026-03-30 11:49:00 | TERRA_M-M | MONTEIRO LOBATO | SÃO PAULO | Brasil | 3531704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| c16bc94f-8eb7-3600-9bae-af91659169f2 | -21.49905 | -45.24773 | 2026-03-30 11:49:00 | TERRA_M-M | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 29f6a69f-a9bb-381f-90f6-915da53f0df0 | -16.64152 | -44.34918 | 2026-03-30 11:49:00 | TERRA_M-M | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e803f59b-dffe-38c3-b8a1-14864b408bbb | -14.87401 | -46.56381 | 2026-03-30 11:49:00 | TERRA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 444c6aed-16c2-3df2-a7ba-4cec43446005 | -21.49772 | -45.25745 | 2026-03-30 11:49:00 | TERRA_M-M | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 3a4c09fb-bf9f-32f7-aa38-712ab271d691 | -12.8251 | -45.8962 | 2026-03-30 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a8fc7964-c080-3886-8f03-23831e10db3e | -12.8255 | -45.8732 | 2026-03-30 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8df81444-62c5-3d06-af2b-428b557ac717 | -12.8251 | -45.8962 | 2026-03-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.3 |
| dfa466e2-54d4-3681-9b79-c21d1856082c | -12.8255 | -45.8732 | 2026-03-30 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ea6caa71-a76f-3a17-8020-7829ecfa084b | -12.8251 | -45.8962 | 2026-03-30 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |


