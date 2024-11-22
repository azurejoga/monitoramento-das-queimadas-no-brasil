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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f13f6742-a778-3a30-bdd7-0fcccc1b11ff | -1.93841 | -49.52358 | 2024-11-22 05:59:00 | AQUA_M-M | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| cf777a91-d4f1-3e54-bf3e-aa044eeec611 | -3.21455 | -54.2491 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 1b3acc20-dc1c-32f2-9b6f-09000fc5dc6f | -1.07549 | -53.35732 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 173b74a6-b924-3eb7-a492-daf7d9b00c37 | -1.72819 | -52.69959 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e3837e13-747c-3060-8801-6fba2ef6c231 | -1.20141 | -53.68834 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5aeb3eba-9802-3799-a4b3-63a160234307 | -3.57593 | -54.6749 | 2024-11-22 05:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6d5a0f02-3f13-30ee-a2f4-a9220d0f5f47 | -2.49709 | -48.99764 | 2024-11-22 05:59:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 456b9ea4-eadf-360b-88bb-9179a8fcc1d7 | -3.10426 | -53.99433 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a2d98b1e-b743-3173-a16e-1b55346d8141 | -3.54359 | -50.52193 | 2024-11-22 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e2d259aa-170f-3fb4-82eb-4b96d291a850 | -1.11696 | -53.39658 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 443982ac-e1c3-3905-8339-f1f583d446cf | -3.30145 | -50.35886 | 2024-11-22 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 69f504cd-a998-3d77-8feb-386da232fb5c | -2.80425 | -54.02334 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c2238acf-2fcd-3d98-a01b-6144f625b292 | -1.73593 | -52.71039 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 88f9cf8d-710e-3399-a4b6-6dbecf0d8b04 | -1.80864 | -52.16348 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2f7fbd31-6ea8-337c-9492-96302170eb9e | -3.56165 | -54.21586 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 371eb306-fdd0-3468-a395-821ca4807cd2 | -2.69653 | -51.86668 | 2024-11-22 05:59:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3995bcb6-ad71-3423-9fe3-44c44ce66c48 | -3.28441 | -53.84127 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7382d7d1-5206-310a-8a69-8a513b005ab4 | -1.07414 | -53.3663 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| b7bc3d5d-fb72-399a-ba62-5eab27b2ddc4 | -3.11869 | -45.0612 | 2024-11-22 05:59:00 | AQUA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 89144d36-7205-37c8-8407-24509170aa9c | -3.2795 | -53.81296 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| d7db689d-f944-354a-a945-f537926e6586 | -3.26924 | -53.82064 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a977cc60-a91f-3690-831b-93630b4b7772 | -4.11093 | -51.05865 | 2024-11-22 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 67609d1f-974b-3921-afa5-99d63e3a3fad | -1.50787 | -53.12689 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a246380-172c-3344-92eb-3f133e06076a | -2.85164 | -53.96341 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 975b0c86-eeba-3721-887d-2c1a83920fb0 | -2.58062 | -54.04171 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 12ede8a1-3794-30e3-b22a-310f997d6b32 | -1.25979 | -53.35979 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 47efe6f6-bb7e-3b1c-bc58-f65cc8d9373d | -4.10588 | -51.05102 | 2024-11-22 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 45a029c3-3d42-3ba4-9849-a7d6756b3f17 | -3.50219 | -53.80252 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| c07a58ec-306f-3648-9126-b15f5418ee4f | -3.24243 | -54.24415 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9b033142-b771-309c-81e3-356aac15e9f4 | -3.52223 | -53.79345 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 583d3908-0bdb-3794-98fa-577d48566f37 | -3.57462 | -54.68369 | 2024-11-22 05:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cf477def-437a-3f73-b477-952bf662fcfb | -1.63876 | -52.62144 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 14e7fda9-6135-3431-9051-e67dd96049af | -3.22603 | -54.23275 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| d6fbd365-d7ab-380b-bdee-b90da133743e | -3.23226 | -54.25167 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 109.2 |
| e0707269-caa5-3319-9e15-a4153263c033 | -3.09705 | -53.73737 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f5a60904-6db7-3050-85e7-16d92c09e74d | -1.44008 | -53.389 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f3671884-79b3-3403-bec0-857e1ec31193 | -2.78312 | -51.40595 | 2024-11-22 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5c0fc51a-7ce2-3ab6-9e41-7e2d7d622bee | -3.54005 | -50.51583 | 2024-11-22 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1370fc8d-d7f3-3a8a-9635-b5b7a024bd78 | -2.59475 | -54.00764 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e60a7d4-0651-3e9b-964d-4b80ba690abb | -3.2234 | -54.25039 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 75dfc613-7fb2-32be-9b4c-6843ca23dba0 | -1.38454 | -52.34007 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d0ba5423-2ce4-372f-802e-59943915adb1 | -3.56033 | -54.22473 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 567e1005-cca2-3fa9-b2d2-f301076db856 | -3.22472 | -54.24157 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 67ca9a2e-363c-3a8c-88cd-ade431d3c9e9 | -1.20724 | -51.96731 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7402acbe-8373-3a73-aed2-0adcb9849477 | -3.8247 | -52.25388 | 2024-11-22 05:59:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 871a0bba-31fe-3fff-927f-1a856c387587 | -2.79671 | -54.01319 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f8c393bb-5d9f-39c8-8b59-cf172b4cbf4c | -1.6514 | -52.66219 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eefdb517-2f39-3cbb-8100-6420b6ffe7b8 | -2.76085 | -54.07133 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4e06cee5-5265-3b0d-a93a-35b269c171d4 | -2.19673 | -53.64563 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 256bc394-bd9e-3d5a-8f49-4df93c5b0322 | -2.82332 | -54.01704 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a05c2396-f027-3073-b012-98932fb605c2 | -2.61092 | -54.26241 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 56b031a1-267d-3165-b27d-384f4b338159 | -3.33595 | -50.50229 | 2024-11-22 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| fd3e10dc-32e5-3687-8a93-fceb53b53fa0 | -0.92121 | -51.73408 | 2024-11-22 05:59:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fc89cb9e-f9b0-3d44-8c8c-82d5c258b5c8 | -1.18608 | -51.94711 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d6d36109-45dd-3083-9814-feb653574633 | -1.71357 | -52.48203 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 72795ef7-34f9-3f5e-ae9e-49a6ab66e291 | -1.73871 | -52.37617 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b38233c1-0b2e-3157-86f0-c963f53e87b1 | -3.28574 | -53.83229 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 59fd24c1-ee37-3c6c-b1c0-ea14b9395242 | -3.66068 | -54.65135 | 2024-11-22 05:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| adfddcf2-4e0e-3c1a-b806-d027d6109854 | -2.54271 | -53.98441 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fbd44fbf-7e79-3e27-b63a-1ff97217d53a | -2.22033 | -53.73124 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 4f94c3a2-5f6d-3dfd-ba04-cb0e4ac9c475 | -3.63734 | -54.32381 | 2024-11-22 05:59:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6d89dc64-310b-3832-82bc-e8a21cbded71 | -3.17746 | -54.31581 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 8284ae06-646b-3ae4-9c9f-c4aa1aa38e52 | -1.24019 | -51.74137 | 2024-11-22 05:59:00 | AQUA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 31d34c63-8b59-389e-84d0-316ada9dc802 | -1.63338 | -52.40397 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 05a41401-54dc-367a-9d9b-9f93a143c612 | -1.19554 | -51.94846 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 4cccb99d-1fa3-3539-8b5d-b97a55166062 | -1.20346 | -51.95995 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| af7311ba-d95e-3631-93f4-c3ea32fa4f9e | -2.84505 | -54.00782 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 809ecd0c-abe5-378c-bf38-883dac2a0f58 | -3.23621 | -54.2252 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 2e12686d-fc62-3c4e-ba26-94b6dd853d39 | -3.19384 | -54.32722 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e0af154c-6048-3265-afde-e40c97775097 | -2.91013 | -53.06316 | 2024-11-22 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8e2b4a8e-7daa-3cca-a48d-4cc951593fb0 | -1.72677 | -52.70907 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 07a3eb27-3729-380c-8793-9ae2b40c79b9 | -1.12454 | -53.40682 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 3be5b8e2-3d50-35d1-b62e-4dd1df9661d6 | -0.95294 | -51.71753 | 2024-11-22 05:59:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c606015-43ac-3256-bea3-4a18f0424bf1 | -2.45562 | -53.70224 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 54fb9441-e0a8-3a5e-8756-cf5289fc5849 | -1.13345 | -53.40812 | 2024-11-22 05:59:00 | AQUA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 2f0d952c-0d64-37fe-9a07-3de5f4c5ede1 | -2.74496 | -51.87363 | 2024-11-22 05:59:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 574f5265-3ecc-3946-822b-55a982d78eb7 | -1.7451 | -52.39709 | 2024-11-22 05:59:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| b53daf77-f306-31a2-954f-c67e687b3112 | -0.05335 | -51.23449 | 2024-11-22 05:59:00 | AQUA_M-M | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 39.3 |
| aed5a3ad-ece5-3477-9b1b-d22de0bcf00c | -2.6949 | -51.85987 | 2024-11-22 05:59:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4741a950-5525-34dd-9419-baf716b3ef88 | -3.28174 | -53.85921 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d98bad99-8c11-3ec3-9623-701f39b59ca6 | -2.58193 | -54.03289 | 2024-11-22 05:59:00 | AQUA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bff03772-9c3c-31ba-b304-fe781008976f | -3.207 | -54.23902 | 2024-11-22 05:59:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 668bde7a-50a1-3d35-aca0-367242074095 | -3.5098 | -53.81274 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6f39946b-c26f-3548-a336-f8c0fa690d38 | -3.50084 | -53.81152 | 2024-11-22 05:59:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 43a1ecdb-e716-3633-9bc3-a77f3f2b56e7 | -3.185 | -54.32593 | 2024-11-22 05:59:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7d0d46e0-37df-3bdb-9ebf-3d4ba5435a17 | -3.33174 | -53.33588 | 2024-11-22 05:59:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5a43caed-245d-3f8d-8eb8-2f56b9af5cf9 | -3.2768 | -53.8199 | 2024-11-22 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a357bb25-b960-3209-acd3-830a71d6d6df | -3.3266 | -50.5132 | 2024-11-22 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| bcb7d765-95a0-3d81-b114-f161d9146718 | -3.2384 | -54.2632 | 2024-11-22 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| a7d3a40d-63c4-3cc9-83d0-a4bfe21e79cc | -3.2386 | -54.223 | 2024-11-22 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 42214cb8-df12-3f68-af89-3ef318fd5044 | -3.5159 | -53.8132 | 2024-11-22 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 9e66249a-b491-3df4-b958-cd6631f6c976 | -3.22 | -54.2636 | 2024-11-22 06:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b75a6200-2c90-360d-bea7-30060cf684e8 | -3.8535 | -52.3596 | 2024-11-22 06:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 706569ee-40b7-3647-8d19-2918eccbb993 | -3.8719 | -52.3589 | 2024-11-22 06:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 3e88a88e-e07f-3f61-a928-a2075ad70fc0 | -1.1287 | -53.3951 | 2024-11-22 06:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 3c377035-7d5b-34b4-a28a-c5ffa8aaec85 | -3.3451 | -50.5126 | 2024-11-22 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| ac8701e7-b7f5-3727-80e0-c6f2555e4de3 | -3.3452 | -50.4917 | 2024-11-22 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| f5eadcc9-1c34-3d7e-b986-14bd738d9331 | -3.3635 | -50.512 | 2024-11-22 06:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 72bb76d5-cade-3140-a12c-e587bf79f19d | -3.2385 | -54.2431 | 2024-11-22 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 169.2 |
| 2c0c0feb-8273-35aa-9ed2-c6a3ce9f1009 | -3.2201 | -54.2436 | 2024-11-22 06:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |


[Clique aqui para ver as próximas entradas](README67.md)
