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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f09c83a2-cc1e-321e-98a8-a9afb600bbd7 | 4.21391 | -60.71794 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| e484ebc7-3550-392f-93fa-9bcee37f7755 | 3.63523 | -61.02441 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 99609d30-006f-364a-9aca-0eb4431bf62f | -1.84875 | -54.95745 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b30464ec-0d62-3ec4-9353-0c07267eb404 | -0.71935 | -57.97192 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e58d0278-2d89-3e86-8c9b-eb4be607c432 | -9.11735 | -68.87787 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7f5e0bb3-f173-35c3-8e90-9ad4168cd450 | -8.64355 | -70.04665 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 17cf5055-11a2-354c-911a-996420d75e0f | -8.70521 | -69.4188 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0e645d15-4937-346e-b515-a92c3e2d8d87 | 1.8606 | -55.77238 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e22ffe23-25d7-3ff9-8ad4-6de92ceacc6f | 1.98078 | -60.61488 | 2026-10-05 17:37:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 2fd9fb5a-9096-3b8a-8d53-cfbb7562d5e5 | -8.64933 | -67.44982 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 76be8f03-6003-34f9-b806-06d2fc06431c | -9.00809 | -65.69175 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 568c63e5-cf81-3f63-b82b-8a8e6e234c58 | -8.72614 | -68.90353 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 787e0ef4-ad9b-3a78-abdf-984367b1e4a1 | 3.40001 | -51.53079 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 583ed8a8-52f7-3987-a0ee-8ef941bb9e0f | 4.56447 | -60.82935 | 2026-10-05 17:39:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a1ab5c42-4904-31ab-b87a-a24ca04db936 | 4.95359 | -60.45759 | 2026-10-05 17:39:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 55acc900-5713-31fb-8bcb-a33f0c854218 | 4.56503 | -60.82566 | 2026-10-05 17:39:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0371e68e-5dd2-3e16-9ce8-40f08659abcb | -9.4819 | -66.7836 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 1fa5bd2c-9a83-36fd-8764-09936b900aa8 | -10.0889 | -68.2715 | 2026-10-05 17:40:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 40.9 |
| e4cf1509-8963-3aeb-abbc-c8c2ea0c77ab | -9.1147 | -65.9379 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7617d5cf-34ed-3a6a-9fbf-df5e06960ef9 | -8.2674 | -71.1215 | 2026-10-05 17:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5e54f66c-5336-3c43-9454-bfa6d122a8bc | -9.1407 | -64.4024 | 2026-10-05 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 7ce45119-605c-3664-b1b0-08940a531ecc | -9.124 | -68.313 | 2026-10-05 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 61ab5006-40f9-3c56-ae02-a69cff3069d1 | -8.5367 | -67.032 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 002e57d4-07de-375e-bdaa-634fdbc03441 | -8.5368 | -67.0135 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 50e38728-bdd7-3b75-af22-99b954de11cd | -9.1243 | -68.2391 | 2026-10-05 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 8b63f9e4-4ee1-3fd6-b28d-43d173754e8b | -9.0585 | -66.0887 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 9ae26264-6906-3db4-bd47-05b124e58106 | 1.8038 | -55.5458 | 2026-10-05 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 0bc8061e-eb9c-3231-bbd8-a32a6d6035f3 | -9.1535 | -65.5634 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f80ab9cc-5b72-3db7-a4e7-0cef973584c6 | -9.4751 | -64.3336 | 2026-10-05 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1a2998d3-d813-3edb-8af1-22785c51d393 | -9.0584 | -66.1073 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 9e29d466-ec12-30a9-b750-ffab7d80f06c | -8.852 | -66.7827 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 138.1 |
| bbf79d08-6d6b-3910-b74a-d2762b5a883e | -8.8519 | -66.8012 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 177.7 |
| aeab4e67-f7cf-31d9-8326-1c69ceeae6b1 | -8.593 | -66.8081 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 3f779685-0a21-3ca9-9770-f09b89f53f44 | -8.5745 | -66.8086 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bf782c97-3a0b-38d4-a14e-6d21cfd09f20 | -9.7498 | -65.0938 | 2026-10-05 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8f37b557-8761-334d-b009-74913d6581be | -10.1075 | -68.271 | 2026-10-05 17:40:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e1405495-4631-3312-b457-67331c183c39 | -9.3431 | -64.7143 | 2026-10-05 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5ffbd781-e7ed-36b5-b3b2-098a18ee6d02 | -0.84 | -48.6394 | 2026-10-05 17:40:00 | GOES-19 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 0f98478e-0294-30c0-b058-664615d0a6b9 | -8.537 | -66.9764 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.3 |
| bd4d46cb-d17d-3943-9569-15fa204b9205 | -9.2828 | -65.6526 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 8ec3e1c7-c032-3a79-b766-534f42f98ac4 | -9.0889 | -67.759 | 2026-10-05 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b763db12-72d7-38d5-a692-2bfb3e1a7495 | -8.6294 | -66.974 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 42c48feb-d5d3-3dfd-9d13-2a6d8d5027d9 | -9.5468 | -64.8196 | 2026-10-05 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0829f323-ce8f-3a16-b3ae-117f3ee6a5da | -9.4565 | -64.3344 | 2026-10-05 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| d1636c0f-4a2a-3970-9318-1b0a1570abf2 | -8.6293 | -66.9926 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 1e33b1f6-f879-3a2d-a61a-27bd05e6731d | -8.8895 | -66.6516 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| d7330551-6e11-34c5-9f72-07def5de409a | -9.1334 | -65.9 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 739fffd7-ef75-3dd8-b756-df5f68b5aa95 | -9.1241 | -68.2946 | 2026-10-05 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 76a74971-96ce-3229-9df8-b0b85b2c0023 | -9.0769 | -66.1068 | 2026-10-05 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5056d5b3-cd38-3a4b-92e5-2e2fcf246b89 | 1.7671 | -55.6056 | 2026-10-05 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 158ea5a9-32ea-38cd-8dc9-3e3046117543 | 1.8221 | -55.5456 | 2026-10-05 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| db303d0a-8bdd-3643-96f9-48174e8d5647 | -9.1076 | -67.7215 | 2026-10-05 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 85f1fdbb-58ab-39fa-85d9-6dfb5622eea9 | -10.814 | -68.6429 | 2026-10-05 17:40:00 | GOES-19 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 47.8 |
| fff24dec-13f7-3e98-81d8-c32be164cdb3 | -9.1076 | -67.703 | 2026-10-05 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 171.7 |
| ed8b1642-eae9-362e-9ef1-ae2aeaa7b9f4 | -5.9606 | -41.3507 | 2026-10-05 17:40:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1514.8 |
| 5e99e544-b6be-3ff0-a046-07514cf027fb | -9.5468 | -64.8196 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 65d230e9-408e-33e8-b5da-ee7c954ba23e | -9.0889 | -67.759 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9d2e201c-0088-3f33-82ec-c76b8a45924a | -5.9606 | -41.3507 | 2026-10-05 17:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 569.1 |
| ce125578-32a4-3c16-b7c0-3ba80daf0851 | -9.2365 | -67.9035 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 276e75ab-4ae7-3d70-86dc-6c146a467fcf | -9.7126 | -65.0951 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 433760cb-a258-3b41-b6ba-ce21c1c095ad | -8.9257 | -66.8549 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 712976e0-828d-3690-920a-abec8e2a236b | -9.1223 | -64.3655 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| da4241cd-f30b-354f-8102-681d7d1f242c | -8.8895 | -66.6516 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 07a418a6-ad63-3d4a-8629-0be1026f6d6f | -8.852 | -66.7827 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 159.9 |
| 86867769-1b68-3e24-a349-3b804c2dc2a6 | -7.5325 | -70.399 | 2026-10-05 17:50:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| c1081252-b4b4-3361-8624-1f26be36875b | -8.5554 | -66.9945 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| efddeb60-6534-38bb-9abe-615ec8ecb2b3 | -8.6665 | -66.936 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| b55457f6-7c86-3134-bea4-93f73fff9132 | -9.1072 | -67.8326 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5a6969e3-86ee-3c26-bc16-6823c01d0fd5 | -8.6493 | -66.5839 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| c98b95f7-0fde-306d-89bc-4a02eb17e611 | -8.5554 | -66.9759 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e9f3df80-f37f-3700-9026-88bc8935151a | -9.1149 | -65.9006 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| a72acab1-c735-3c4d-b40a-55a0ca6754f5 | -9.1407 | -64.4024 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 7d28d761-32f3-3dda-a7ae-6fb2e3e0a697 | -9.1222 | -64.3843 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 1d3d1e8b-ca8e-3e5f-b0b7-62e818bc41c6 | -8.6311 | -66.5101 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e5bd28e7-64f3-31b2-8234-9f3bdb944ae3 | -9.1076 | -67.703 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 196.3 |
| 31931ff4-dcc3-3cd5-a25d-88bfb5af51b1 | -8.9239 | -67.3372 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 44930bb9-a0d4-3730-8e7d-89a1acc8c80e | -9.0585 | -66.0887 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2b17d94b-572f-3f58-9a8c-998bb3e0877b | -8.871 | -66.6521 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 520e2e01-7048-3372-8a29-d5cedb495a43 | -9.3431 | -64.7143 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 082fcc09-4aa4-33d3-8d87-9bc9d4bce0cb | -8.6214 | -69.5026 | 2026-10-05 17:50:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 5f79b569-a91c-3d1d-959b-19e63cdfb569 | -9.4819 | -66.7836 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 7c89c20c-d152-386e-ac85-80ff65f4e280 | -9.0584 | -66.1073 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| bffa32eb-c14a-31ce-8cad-c832745fcea7 | -8.8704 | -66.8007 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| ba59e064-4bab-395a-ac93-7ddbb82a5e88 | -9.2934 | -67.5501 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 3038bb9c-b1e8-302d-a826-63460583fdf9 | -9.1334 | -65.9 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.1 |
| b566638d-aedc-393e-be55-bf0efd694816 | -8.5738 | -66.994 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 254b48d7-68b5-3c15-a69c-46844afaad5f | -9.1038 | -64.3662 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 34c92297-ca65-3cee-a738-a41a1cd664d5 | -9.1243 | -68.2391 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e30a0cf6-273b-3f55-8944-9ceeda90aaf3 | -9.1442 | -67.8317 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d7e8bd13-3813-3816-89f4-477c66db45ce | -9.0769 | -66.1068 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| fa6f382d-71fa-30e3-9433-ad55a53c69d2 | -8.5745 | -66.8086 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d78f35d3-af21-3b2e-b4be-d934716cab46 | -9.1147 | -65.9379 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| d02b1bf2-7707-3fa8-b54f-17140bebb119 | -9.077 | -66.0881 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 3e2b9bbe-42eb-3f82-afa4-43285430384d | -5.7324 | -41.6108 | 2026-10-05 17:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 120.4 |
| 43c38fae-871f-357f-a523-b0560bb98275 | -9.1037 | -64.385 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 967f11cb-94b5-302c-b450-aa904501fa75 | -9.4565 | -64.3344 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| f2e912c9-6488-3593-98ac-208748202b2f | -9.1613 | -68.2383 | 2026-10-05 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 193.8 |
| c26add28-38cd-3bc9-81cf-68e5c934b15a | -9.1408 | -64.3836 | 2026-10-05 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 62304fa8-b8e4-3135-84c0-c2abba18e47a | -2.5353 | -65.8819 | 2026-10-05 17:50:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 6941022c-9b09-302f-b63d-ac422fc877ad | -8.537 | -66.9764 | 2026-10-05 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |


[Clique aqui para ver as próximas entradas](README158.md)
