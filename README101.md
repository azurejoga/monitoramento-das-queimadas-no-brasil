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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 500846af-9d14-32c5-9557-acf4a0d0c66b | 3.51849 | -51.50024 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a02910e2-e990-36ef-8645-75aa6330dba7 | 1.84504 | -55.80634 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ab5ed562-71c8-3b7d-b1c0-19ed967ebc4e | 1.79383 | -50.62423 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 25c974d5-bec6-3d0f-9408-74cb7acec293 | 1.85548 | -50.69143 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f1dfd3db-185d-3a62-8f9b-11fb996e8b48 | 3.58325 | -61.36717 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 87f40deb-5173-39d0-939b-7b2ede988391 | 3.52188 | -51.50076 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 77a138e4-4588-34cf-a455-c549026afb21 | 2.28315 | -55.86131 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c5125f06-3228-369c-97a2-216928c5f84c | -0.73669 | -57.97996 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 272f7321-c70a-30a7-9f06-74b63d035883 | 1.5147 | -55.64085 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a783beaa-350f-3886-a0a5-0d3cf56d6a89 | 1.60423 | -55.78985 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20c239a6-9572-3642-8c31-e82ef51f853e | 3.06853 | -60.60688 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a4238a94-90cb-331c-839e-1ea279d9594e | 1.08102 | -50.08574 | 2026-10-05 16:41:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0aafe7df-8d29-3925-b384-05a30c7bddbc | 1.8445 | -55.81123 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| cb70585e-4ae3-3f1b-a170-338b7af1489b | 2.33287 | -50.81269 | 2026-10-05 16:41:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73d2effe-0fea-3f8d-8918-fdd5bcf8ddc8 | 3.0827 | -60.5955 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a6411c55-f56d-3304-b48f-16d2ae95e7ba | 3.06254 | -60.60597 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 71061d5b-791b-315e-a93c-83c3e434008b | 3.35997 | -51.3422 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| afd62e7b-4ad0-323c-a32d-641cd4615006 | -0.73514 | -57.97003 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4076192b-477c-3c3b-a971-4717994f5a96 | 1.57629 | -55.99784 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5ce6cd63-7f75-342a-9dfd-e14767020b49 | 4.21351 | -60.71334 | 2026-10-05 16:41:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e852cd17-9028-3834-911d-a5cb6835f35b | 1.80943 | -55.55032 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f9dc487d-3ddc-3a9a-a0a6-8bf1825ab511 | -0.68429 | -57.99437 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8ebba467-307b-3b94-96b0-c3cf8007b65f | 1.61373 | -55.78699 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9df2e44f-20f5-3ae8-a9b3-9c990518b941 | 1.50899 | -55.64865 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 53a709d5-5d43-344c-b6ab-9448835ffb17 | 3.53149 | -51.50594 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b171994f-8378-3409-b6cf-7bda611f1279 | 3.53375 | -51.51373 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| a73152e3-b801-347a-b5cf-0a209c72acea | 1.50832 | -55.65292 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| aa874095-32d0-39b8-8849-04d21ad7bdcb | 1.85597 | -55.7947 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 20cbb11f-1cbd-3a23-81a2-a7ded1d37f54 | 2.26929 | -55.86359 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc4ea8c2-2c0d-30b0-8650-5ee03f214695 | 1.45727 | -55.66283 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 8d1da065-99a2-3358-aadb-df0fdc0a304e | 1.76875 | -55.6007 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 91b416e1-978c-3cc9-a094-c8d12f28411f | 0.79981 | -51.15065 | 2026-10-05 16:41:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 8.6 |
| eeb15378-28c4-35ff-8dcf-a60524706a8d | 1.61442 | -55.78259 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6ff4a8bc-0c9e-34b2-bf53-94ae80387dc0 | 3.07893 | -60.58138 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 972229c5-d076-3e2c-9d3b-6be260908f10 | -0.71861 | -57.96906 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 29fa63e0-bc10-3962-afbb-7b693d89fccf | 3.55921 | -61.35825 | 2026-10-05 16:41:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 7be436c0-bd3d-3ae1-bf4d-974b671a8e38 | 2.09048 | -50.90665 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b4ccd2b6-3f43-3f62-a6cc-3027759694a2 | 3.52527 | -51.50127 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 94531201-8898-358b-b520-b582eb88c9f2 | 1.84363 | -55.81497 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc4908dd-d374-3a8c-9f9d-f96b66cffd8a | 1.93685 | -55.71072 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| da357046-25a0-374c-aac7-1524af9b1489 | 2.35109 | -50.76109 | 2026-10-05 16:41:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7145dcb5-9681-3eca-9c3b-a6d7a36e66f5 | 3.78816 | -51.77441 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ca61df43-385b-30a0-b8e6-5274b27298c9 | 1.49075 | -55.65029 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 9b5b2658-8d8c-360d-a65c-ebda86377a88 | 3.80117 | -51.59579 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6c1c3ed3-6ff3-30ba-a45f-eac5c9132626 | 1.48198 | -55.64895 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b8300e34-b826-3c74-8915-1f90c3816e50 | 1.85213 | -50.69093 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e3f426de-a6cf-3197-815f-be92604ab267 | 3.35266 | -51.34479 | 2026-10-05 16:41:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 82ae1fdd-c7e4-3ec0-a322-64d3f725f9fb | 3.11477 | -60.58695 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 3baac4d9-5ca9-3c49-a6f8-e2234a37de3e | 1.47351 | -55.67391 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 7dbfd55d-6de2-3712-af65-429596d27ca7 | 3.07377 | -60.61223 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8a90d127-8f8a-332d-9ee7-7343fd2f5f87 | 1.92815 | -50.92852 | 2026-10-05 16:41:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 3145af13-c644-306c-831c-cae0ffecc666 | 1.90858 | -55.71936 | 2026-10-05 16:41:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 97f1eb5d-67ab-3283-a221-d4140d2d3e95 | 3.06927 | -60.60247 | 2026-10-05 16:41:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.7 |
| bfec7f61-6e85-3df1-96c7-ed0a2e3ee346 | -0.73617 | -57.97664 | 2026-10-05 16:41:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 5bfe279c-8da6-3384-9539-c5e8b3aacc8f | -8.9195 | -64.1473 | 2026-10-05 16:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| db3b736b-2149-3810-b4fd-ce9803ddd5a3 | -9.1408 | -64.3836 | 2026-10-05 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| c4f4f351-bc0d-35dc-bdd9-4fede8fb7be0 | -9.1037 | -64.385 | 2026-10-05 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 3614dd58-05ea-3133-8931-65f8175685d9 | -9.1147 | -65.9379 | 2026-10-05 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 85341c9d-c2c7-3bc7-9051-96e2d2e67221 | -9.4115 | -65.9099 | 2026-10-05 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 32faade3-5f24-3a77-8083-88946fd89e4b | -9.077 | -66.0881 | 2026-10-05 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| fcaca9bb-fd9e-3b3c-b9a0-40601697369d | -9.1221 | -64.4031 | 2026-10-05 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 51f66dfd-7c76-3380-a546-9c7974847223 | 1.9317 | -55.7219 | 2026-10-05 16:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 3ac3a4cd-4810-330b-8003-6837fa489f2f | -9.1147 | -65.9379 | 2026-10-05 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.8 |
| e0253680-e336-379c-aa09-57a9a496b6c4 | 1.9316 | -55.7614 | 2026-10-05 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 12cb6655-43f3-3de6-ae63-54b3949b7ae5 | -8.5918 | -67.1418 | 2026-10-05 17:00:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| aa374958-9d60-331d-b47f-eb52439625b7 | -9.4115 | -65.9099 | 2026-10-05 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 2872fa69-e6ff-32ff-b881-b69e83701382 | 1.8767 | -55.7621 | 2026-10-05 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 906cab91-9548-3674-889d-6c43598beadc | -9.1222 | -64.3843 | 2026-10-05 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 20f16060-c918-302b-869d-cc730404f0c3 | -9.0232 | -65.6982 | 2026-10-05 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 5b535f58-09d1-3b27-8d5c-534a3aa680f9 | -9.1408 | -64.3836 | 2026-10-05 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 3c43bb2b-87ec-3bd1-be56-c89aafc496a1 | -9.1221 | -64.4031 | 2026-10-05 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 44.5 |
| c7514a8e-7cda-3fe0-9f01-b6dd1422e7b3 | -7.4186 | -73.1355 | 2026-10-05 17:00:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 76a0bdde-4d88-3dbd-b348-d735602eacf6 | -30.00864 | -50.66948 | 2026-10-05 17:09:00 | NPP-375 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 4.3 |
| 295171e0-6af6-351b-b9c9-04eb6ec7014d | -29.66118 | -51.04863 | 2026-10-05 17:09:00 | NPP-375 | CAMPO BOM | RIO GRANDE DO SUL | Brasil | 4303905 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 79369270-729f-315c-8fc4-b5cfa1891041 | -30.00924 | -50.67399 | 2026-10-05 17:09:00 | NPP-375 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Pampa | 4.9 |
| 21c44395-63eb-39c0-b063-6ba646ea8573 | -9.1408 | -64.3836 | 2026-10-05 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 85812f28-12ec-310f-885d-694970d8c528 | -8.5918 | -67.1418 | 2026-10-05 17:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| a1881995-912e-3f98-b697-f003e07361de | 1.8766 | -55.7819 | 2026-10-05 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0cc70ad9-83ee-3fe6-a9c1-849823a81eea | -7.3823 | -72.717 | 2026-10-05 17:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 74e34e53-0ae2-316d-89a7-33516ab98f2e | -7.4186 | -73.1355 | 2026-10-05 17:10:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 5fdcd3c5-45c3-399d-8823-984b6de25fec | -9.1147 | -65.9379 | 2026-10-05 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ef10d09a-01f8-3d18-9344-d0b4b0be3726 | -3.6589 | -69.4367 | 2026-10-05 17:10:00 | GOES-19 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 9bc6f309-5188-35f5-8481-5ec8ea534338 | -9.1221 | -64.4031 | 2026-10-05 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.5 |
| e9487d9e-1964-390a-87a4-924d6df1f5ef | -8.5554 | -66.9945 | 2026-10-05 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 2c222811-c693-3082-8597-d760e702077f | -9.1222 | -64.3843 | 2026-10-05 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2045ade6-1c26-3531-9189-b753c0da5ffd | -9.1037 | -64.385 | 2026-10-05 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 6ae466cf-b3d9-3c40-a2e7-59222fc3d083 | 1.7399 | -50.8235 | 2026-10-05 17:10:00 | GOES-19 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 83d6aae6-002a-3d98-ba1b-64476d8b207d | -9.4578 | -68.2314 | 2026-10-05 17:10:00 | GOES-19 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 49b3c95a-c583-3819-9e11-a5d62b1ba8fc | -9.077 | -66.0881 | 2026-10-05 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.5 |
| de5af866-1073-3c1e-be80-55c347a2facb | -9.1076 | -67.7215 | 2026-10-05 17:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f5916d8a-451a-381d-a6f5-549553d836bf | -9.1407 | -64.4024 | 2026-10-05 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| d4dfdfb4-1609-35f0-b060-1a3ab9549653 | -18.37622 | -41.78072 | 2026-10-05 17:11:00 | NPP-375 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1befac55-019f-39be-8bae-660fb318a5ff | -18.02118 | -41.66256 | 2026-10-05 17:11:00 | NPP-375 | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 06916a08-192e-323d-a3f8-1c6fa0f14b55 | -17.67991 | -44.75344 | 2026-10-05 17:11:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5b3e7eb5-ff74-3d0d-bf28-8be4c3168968 | -17.94054 | -39.4822 | 2026-10-05 17:11:00 | NPP-375 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 4b964b59-12e4-3f55-ad43-b02b661bc9ad | -18.3647 | -41.7767 | 2026-10-05 17:11:00 | NPP-375 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e483b4dc-a490-3981-93c2-f69892d38e20 | -17.89791 | -39.42976 | 2026-10-05 17:11:00 | NPP-375 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| 81d15b15-8c30-3dc0-9260-a98a74c2b7f8 | -17.68425 | -42.18312 | 2026-10-05 17:11:00 | NPP-375 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d63b4faa-e890-3506-a561-2be55e0ec612 | -17.6842 | -44.75261 | 2026-10-05 17:11:00 | NPP-375 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c8179f76-19f6-332c-83da-06a56d6138e2 | -18.37113 | -41.78193 | 2026-10-05 17:11:00 | NPP-375 | CAMPANÁRIO | MINAS GERAIS | Brasil | 3110806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README102.md)
