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

## Dados Diários - Página 382

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b685525e-9724-358c-8361-08b51a5b732c | -6.22 | -52.88 | 2026-10-08 17:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a75ada-ce54-3e16-9979-e3a97aea62b1 | -7.21 | -55.13 | 2026-10-08 17:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1771f31c-45d5-3af4-a37f-5d82a841f541 | -6.25 | -52.89 | 2026-10-08 17:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97b5fac0-4073-38c6-b314-d417eb1f394c | -2.07 | -46.57 | 2026-10-08 17:15:00 | MSG-03 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fbdc1b4-85aa-3a34-9066-e206cf9eee78 | -5.99 | -40.97 | 2026-10-08 17:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 95971d79-83c1-3921-a7c3-bee0c3d44504 | -6.18 | -47.91 | 2026-10-08 17:15:00 | MSG-03 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4c5d2b09-ea6a-3e91-946e-6068ec9d9931 | -2.07 | -46.61 | 2026-10-08 17:15:00 | MSG-03 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e18d2978-f060-3b66-b3a3-97c4a3141521 | -7.31 | -43.98 | 2026-10-08 17:15:00 | MSG-03 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3f595f32-83e9-3dfa-b19e-a81408d8ca73 | -6.15 | -47.91 | 2026-10-08 17:15:00 | MSG-03 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bb51ea55-93fe-3ad6-be3e-1f0093736106 | -5.08 | -46.19 | 2026-10-08 17:15:00 | MSG-03 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 361dfe68-6e00-3151-ac74-738a5386093b | -2.73 | -54.14 | 2026-10-08 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d933ed3b-5d3f-3d7e-89f0-a25d9f491728 | -6.15 | -47.96 | 2026-10-08 17:15:00 | MSG-03 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dddaf2b8-8488-3aa4-a293-dca18138203a | -11.63 | -43.71 | 2026-10-08 17:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 74c7e9c0-5fe0-3475-891b-a9350110640e | -2.07 | -46.52 | 2026-10-08 17:15:00 | MSG-03 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c84f68d-5cb7-3c8e-adbd-5acabe16d43d | -2.73 | -54.08 | 2026-10-08 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3d78c38-abe4-3ff2-9cc7-e56d2228953e | -5.99 | -40.93 | 2026-10-08 17:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 345d2c8b-74c3-336b-aa8a-bbe1aeb0cacb | -13.2 | -54.29 | 2026-10-08 17:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 95175c7b-b07f-3c09-bfeb-43279490ae68 | -5.7 | -53.5 | 2026-10-08 17:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee5fef0d-a5fa-3186-b460-8e502e851792 | -3.08 | -53.93 | 2026-10-08 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2540a43f-fec4-351b-b4ce-80d430001cdb | -2.76 | -54.08 | 2026-10-08 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed6b848d-fd31-39f2-9c83-7276012f5673 | -2.76 | -54.15 | 2026-10-08 17:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6543745-68d8-3cf7-b16d-d37dd24ddf12 | -8.27 | -45.73 | 2026-10-08 17:15:00 | MSG-03 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 45dae8e2-cd01-3276-984f-cd753de6e1a8 | -11.08 | -44.08 | 2026-10-08 17:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d700f339-4dad-3a3c-8beb-edb1fd8f109d | -5.7 | -53.44 | 2026-10-08 17:15:00 | MSG-03 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36878731-ad76-3b4a-9b57-dc79907b9823 | -7.31 | -44.03 | 2026-10-08 17:15:00 | MSG-03 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 15d680b8-3ebe-3334-97ae-099922b37f50 | -8.27 | -45.77 | 2026-10-08 17:15:00 | MSG-03 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3666352d-c095-34bb-b074-a540b795acba | -5.97 | -40.93 | 2026-10-08 17:15:00 | MSG-03 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6a4ca46e-d9ef-3c38-99b0-d380f006bd57 | -4.64 | -50.97 | 2026-10-08 17:15:00 | MSG-03 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7d9b0c8-981f-3615-9226-10bb2e2ede42 | -12.2316 | -44.7427 | 2026-10-08 17:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 482.0 |
| 1c7ccee7-17a6-37e6-b655-8e7b0f2ead6a | -12.232 | -44.7194 | 2026-10-08 17:20:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| f7cc79c0-8a88-3cfd-aa38-dd2803fe4b95 | -9.9205 | -44.8124 | 2026-10-08 17:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 14130487-3f40-3c90-9f15-57f7e408dbd3 | -9.5003 | -66.8017 | 2026-10-08 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 178.3 |
| 3e76224c-485e-3467-93ef-c73958ffb561 | 3.7462 | -51.6224 | 2026-10-08 17:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 387cbc7c-3912-39b6-a712-efd423331ce3 | -12.2123 | -44.7457 | 2026-10-08 17:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 275.8 |
| bb4e80be-9d59-37c7-8b77-38338881838b | -9.0988 | -65.3596 | 2026-10-08 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| c0009ede-d770-3a87-8ac2-d29407a2b2a7 | -9.1072 | -67.8141 | 2026-10-08 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 8b6a157d-a3a1-3008-b544-3e9f4b2cf60d | -12.1545 | -44.7547 | 2026-10-08 17:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 136.7 |
| dd0885c0-22c3-38ba-9493-b759051ded64 | 1.6937 | -55.6263 | 2026-10-08 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 3fc221b3-01f2-35b0-87db-1d98d2dc471a | 1.3346 | -50.8503 | 2026-10-08 17:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7be6bfc6-488f-384d-b334-f130727abd69 | -11.2271 | -45.2374 | 2026-10-08 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| e181efd3-bf8f-3fdc-b1c8-b83af8577cb4 | -9.4819 | -66.7836 | 2026-10-08 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 235342b3-63dc-3f6c-bd1e-9dec04b21362 | -8.9501 | -45.1334 | 2026-10-08 17:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 2abd9012-05bd-3b94-8a02-175da27c91dc | -11.2661 | -45.1859 | 2026-10-08 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 41f38da3-1b71-3ef1-a94c-36d18e88e00e | -8.9875 | -65.4006 | 2026-10-08 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 3ffbf3dc-24a1-3a8a-96d8-64202a2becf1 | 1.7121 | -55.6063 | 2026-10-08 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 1e79370f-cfb5-32cb-b790-c04028ef8264 | 1.7488 | -55.5861 | 2026-10-08 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8e00b68e-b071-3e7a-8508-c656c0b5a3a1 | -11.2657 | -45.209 | 2026-10-08 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 3f7f7000-6372-3ef0-8cd5-e8bd6967fd35 | -11.8503 | -43.5598 | 2026-10-08 17:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 364.8 |
| eed291dc-b79c-3d54-bd9b-2fd58f04bf12 | -8.969 | -45.1313 | 2026-10-08 17:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 0b9a9012-5903-34f8-90f5-453cff2fcc09 | -3.4094 | -58.0207 | 2026-10-08 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| b3e1cf83-771a-3dd2-8792-b13eca64a117 | 1.6938 | -55.6066 | 2026-10-08 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b2ed5878-3326-39c6-84c8-76b173b23322 | -2.572 | -56.1646 | 2026-10-08 17:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 262.6 |
| 1f50c7d1-64b3-3cee-bb53-4a71fabe31de | -8.5367 | -67.032 | 2026-10-08 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 3e5b5ef6-32b6-354a-b97a-44d4684f0b0f | 3.5448 | -51.2772 | 2026-10-08 17:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 30c9f460-e01c-3948-bab3-867ca8e8a94a | -9.1257 | -67.8137 | 2026-10-08 17:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 76a6d4b5-f443-3714-a21a-7dfda1613668 | -1.856 | -57.057 | 2026-10-08 17:20:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| cf55c204-2a37-3ce4-85db-4cc881bab1e5 | -3.4095 | -58.0013 | 2026-10-08 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| ab4b1a1a-36ad-3ecc-993c-74f941a3f430 | -3.3912 | -58.0017 | 2026-10-08 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 34925b3c-aeb2-3639-a693-9f8fb202551d | 1.6568 | -55.8045 | 2026-10-08 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3ba90612-4e0c-3b82-9be9-81c1f6ba3849 | -11.2849 | -45.2063 | 2026-10-08 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| b9ce1b7e-34b3-3d25-a09f-30b3b0327ae9 | -2.0447 | -54.3085 | 2026-10-08 17:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| c36fedae-4c71-3eef-880a-5368deac14ec | -3.4464 | -57.9036 | 2026-10-08 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b5c4ac2d-3690-3917-9f38-06c77b28724c | -2.572 | -56.1646 | 2026-10-08 17:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 290.1 |
| 6349b2a4-ba36-3e39-b7e0-0544a6ca2d68 | -11.7738 | -43.5482 | 2026-10-08 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 8e01cf70-5bfb-39bd-808b-bff3b7ac7b80 | -6.2268 | -44.8443 | 2026-10-08 17:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4e8171cc-fb8e-3c22-acda-71297a4da5b5 | -6.2161 | -52.808 | 2026-10-08 17:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 4abb9f5a-3a49-3a74-94e9-5eca01fa160b | -11.755 | -43.5275 | 2026-10-08 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 68d39039-c748-3150-a134-da0dc75c96d2 | -11.6181 | -43.6669 | 2026-10-08 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 236.4 |
| 02e6baa6-9f17-385f-866c-a2520650e10c | -0.4137 | -51.7273 | 2026-10-08 17:30:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 51.9 |
| e1e03474-1eaa-36b2-a93f-e9a90641a617 | -12.232 | -44.7194 | 2026-10-08 17:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 117.3 |
| c8b88b59-3627-3773-8f57-0deb3baecad9 | -9.8821 | -44.8402 | 2026-10-08 17:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| e5baaad2-6753-3ef2-a840-459b8f64b151 | -3.1874 | -58.8358 | 2026-10-08 17:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| eb83d905-fb48-3f68-bfc8-1d6eb739892b | -11.2271 | -45.2374 | 2026-10-08 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| d572d385-878d-3046-9e4f-ad66a88c022e | -3.3911 | -58.0211 | 2026-10-08 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e6acc394-85e2-3dec-9055-be2506ed37af | -11.2657 | -45.209 | 2026-10-08 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 688e451d-3092-3b39-936d-dc828e437707 | -9.9398 | -43.5542 | 2026-10-08 17:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 313.7 |
| fff5c17e-bab8-30b5-83e4-859281a1c825 | -11.0953 | -44.0037 | 2026-10-08 17:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 305.9 |
| 64449866-1af8-3304-8fe4-5114f25a7590 | -9.1072 | -67.8326 | 2026-10-08 17:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 168.2 |
| 631011f1-ea47-3373-bf34-620187fc209e | -9.4819 | -66.7836 | 2026-10-08 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 163.4 |
| 93f45308-6a88-362c-886e-d69648c39642 | -8.537 | -66.9764 | 2026-10-08 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.1 |
| d0e5f6fa-5717-3926-9ed5-391eb4f5e80c | -12.1436 | -43.2992 | 2026-10-08 17:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 399cecba-7253-392f-a71b-edc4a8823b8b | 3.5448 | -51.2772 | 2026-10-08 17:30:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 48001697-bc7e-3315-995a-f46c135bdd2e | -8.9875 | -65.4006 | 2026-10-08 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 408951cd-e3ac-3a0c-a89c-f480ca25b827 | -7.4697 | -42.8315 | 2026-10-08 17:30:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 169.7 |
| d6565f1f-66cd-342c-9531-6454e7f76652 | -11.2337 | -44.8446 | 2026-10-08 17:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| f9f87f83-abb8-3518-a0d5-5a3ffaf9feb8 | 1.6937 | -55.6263 | 2026-10-08 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 4c509769-1e94-352b-a098-3e3da4ea1cec | -12.8303 | -44.6239 | 2026-10-08 17:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| b364e41a-24e7-3d10-bb23-6309096be269 | -9.3739 | -45.9263 | 2026-10-08 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d5cedb19-0903-3295-a7f3-e5a6a1041b62 | -1.1898 | -49.2542 | 2026-10-08 17:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8fc261fc-1628-3cbd-8be0-5cdb78458539 | 1.7304 | -55.6061 | 2026-10-08 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| c33b52d5-bd53-3e48-8479-b7f67bdcc962 | -11.8503 | -43.5598 | 2026-10-08 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 289.4 |
| d83ff266-3629-3e9b-add0-99379ba7442e | -15.3221 | -42.7746 | 2026-10-08 17:30:00 | GOES-19 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 176.6 |
| fdd97d5a-29d6-3dc8-b5a5-9a3f25f8d17f | -9.5003 | -66.8017 | 2026-10-08 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 162.1 |
| f2c8cf0a-8b42-3e80-bb55-6ad2b29ce3ba | -3.0447 | -57.4851 | 2026-10-08 17:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 2c0de72f-c750-3b5b-aa83-415aa3d73e36 | -12.1733 | -44.775 | 2026-10-08 17:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 00848dc7-efa6-3af7-939d-6e0e8518dda7 | 1.7304 | -55.5863 | 2026-10-08 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c1942b16-1323-3ae0-920e-fd56f976caef | -3.0074 | -57.7384 | 2026-10-08 17:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c2047470-3f1b-328c-a891-3b345ecfae24 | 1.7121 | -55.6063 | 2026-10-08 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| ace6943a-3d8f-3f66-a1ff-7c74047b7589 | -3.3912 | -58.0017 | 2026-10-08 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 47b7e7ba-e4e6-39df-8afe-a0ffcc056832 | -1.856 | -57.057 | 2026-10-08 17:30:00 | GOES-19 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |


[Clique aqui para ver as próximas entradas](README383.md)
