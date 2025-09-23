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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c1e81ec-7643-316a-ae6f-f8e77ca2772a | -1.61799 | -54.30415 | 2025-09-23 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| add09794-0029-3012-bf38-691ddbd39430 | -4.15771 | -48.59991 | 2025-09-23 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 18258bf4-27b3-3492-9ed8-3e4c747c0140 | -2.2699 | -57.09491 | 2025-09-23 00:54:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 69a9c724-d8b5-3333-9e61-797ddced29d1 | -3.63558 | -51.90597 | 2025-09-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 88ce1f34-9efc-34c6-89cc-b0fea471abc8 | 2.40445 | -60.70973 | 2025-09-23 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 15ca24fa-7fe4-30f5-b213-0ac07f1856f3 | -4.49782 | -48.13104 | 2025-09-23 00:54:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8fec0aa6-0129-3804-b52b-fd2f936d598c | -3.62751 | -51.91779 | 2025-09-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| f6913d6d-7a0e-335b-99fc-b3c22dcdabcf | -2.83832 | -48.83331 | 2025-09-23 00:54:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| e79f85fb-8ba5-39ad-b729-c6914fa4500e | -4.16552 | -56.13517 | 2025-09-23 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2231c7b4-c663-3f90-89bc-accfe24538f5 | -3.64068 | -51.90992 | 2025-09-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c25f6e94-93e8-339a-ac85-6409d5281404 | -2.5638 | -48.97483 | 2025-09-23 00:54:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| db4da1c3-9e36-3b1a-ab95-682125232eb3 | -3.86605 | -55.35748 | 2025-09-23 00:54:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 37e47536-857b-3403-8a72-5cb66ae9f5ee | -3.87496 | -55.35625 | 2025-09-23 00:54:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| b36870a3-7f46-3a1b-9e17-5cc2a9a144a2 | -3.63703 | -51.91639 | 2025-09-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 67148e95-50e2-3858-b8af-83bc504da754 | -4.12802 | -48.81441 | 2025-09-23 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| b0fd3066-38c3-35c1-af83-9942510bf922 | -3.82479 | -52.1482 | 2025-09-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7744bfe8-0904-3b23-a08f-a8d71c55d365 | -3.92523 | -54.79038 | 2025-09-23 00:54:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3b3145a7-2dbf-3fe9-87e7-76bbff92594b | 2.40659 | -60.70359 | 2025-09-23 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.6 |
| b9881fc3-fd64-3606-9163-b4a371f8d687 | -4.41844 | -56.1707 | 2025-09-23 00:54:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| cffe929e-5dd7-3baf-bbe5-c3568486521f | 0.15697 | -60.67805 | 2025-09-23 00:54:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 90cd82cd-a939-35a3-aaba-512a4ac8f778 | -3.19556 | -54.97744 | 2025-09-23 00:54:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 94f0193a-e39a-3b33-9a87-8e8c4e46c267 | -3.63919 | -51.89955 | 2025-09-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 97248e17-180b-379a-ad6b-4342fc448a9b | -3.92401 | -54.78158 | 2025-09-23 00:54:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 038b065b-60fb-3b5c-9312-dfd0040a4679 | -4.07765 | -48.04856 | 2025-09-23 00:54:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 75c23c68-9111-3cde-9d3f-12373a712663 | -2.24622 | -47.88138 | 2025-09-23 00:54:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| aeeffb82-153d-301e-a128-83aece1655dd | -3.52289 | -49.4605 | 2025-09-23 00:54:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 75b8552a-92c9-3a9e-80c8-8e08a6ef9d06 | -3.8561 | -52.23536 | 2025-09-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| b14ade75-0789-3d41-aadc-869dc65d9bba | -1.08284 | -54.10902 | 2025-09-23 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| aab7d8dd-fc98-3fbf-9fb9-b8bb84f2739e | -4.40563 | -50.69043 | 2025-09-23 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9469436d-ff10-31c2-97f8-0f4bbfd7911f | -5.17736 | -56.05678 | 2025-09-23 00:54:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c631ca58-e290-3bfd-8b23-79d6d6dee994 | -2.74343 | -49.55059 | 2025-09-23 00:54:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 251ed7b5-b731-3c5b-939f-c7c26d69ccbf | -3.62607 | -51.90752 | 2025-09-23 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| b02055ea-e153-36dc-893d-afd80ea1fba1 | 4.30438 | -60.86115 | 2025-09-23 00:56:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6abd70ce-abad-3914-8e2d-c05fe98cc955 | -3.6342 | -51.915 | 2025-09-23 01:00:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 4329a6e6-147c-35fa-a046-d1841802ac01 | -8.5179 | -44.9749 | 2025-09-23 01:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| b6ed5a49-ecc2-359a-9788-12f8620e8877 | -7.8887 | -44.0281 | 2025-09-23 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 346bb153-3dd8-372e-b24b-47f1f009f755 | -3.5162 | -49.4315 | 2025-09-23 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| c913a816-5263-3e0e-b732-df2c2f096e0f | -3.5161 | -49.4528 | 2025-09-23 01:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c7fea851-43b6-3777-ba82-f492f0887c6d | -11.6247 | -52.8624 | 2025-09-23 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 99460b0c-2037-3ffd-97bf-46bd201d66dc | -6.2598 | -45.3184 | 2025-09-23 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| f228c9b0-f099-31c8-ad2f-217228ae6b63 | -6.2596 | -45.341 | 2025-09-23 01:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 1bff616d-a75e-3bc3-adf1-1a8bda607a2a | -11.6439 | -52.8397 | 2025-09-23 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| ed43aa8b-cb57-36fe-870b-3792e3cc8213 | -15.9578 | -59.4888 | 2025-09-23 01:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 92afd532-5b7e-3297-93ca-196c26ca58f1 | -11.6249 | -52.8416 | 2025-09-23 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 76fbeb4f-0ee1-3cac-bb31-0af651501a19 | -7.889 | -44.0049 | 2025-09-23 01:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 2e5e687f-c97c-3316-9200-addeaed674e2 | -10.9522 | -45.7096 | 2025-09-23 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| e5e23f5c-fdb5-3df7-bb6c-62e10c07de42 | -11.6436 | -52.8605 | 2025-09-23 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.8 |
| b218bbc8-fec3-363e-b7d3-fff6873940df | -10.9713 | -45.707 | 2025-09-23 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 17985a97-5faf-3118-93bc-4d56f0207838 | -11.6249 | -52.8416 | 2025-09-23 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| da09cda9-3a31-35f0-8bfa-09021aee43b2 | -12.7758 | -57.86 | 2025-09-23 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 53435b35-8886-30d7-91c0-5614ce0b9798 | -12.7568 | -57.8616 | 2025-09-23 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 1db75ce7-23b7-3864-890b-dbde05065a0b | -3.5161 | -49.4528 | 2025-09-23 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 66be3cfa-2455-37dc-bf5a-16d7a2c1ad9f | -6.2596 | -45.341 | 2025-09-23 01:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c47dd18b-4fab-37c9-9a09-29063488ba62 | -3.6342 | -51.915 | 2025-09-23 01:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 991d84e5-b784-3d15-b1ad-3d0f0df55d10 | -11.6436 | -52.8605 | 2025-09-23 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| f087e56d-7295-3d1b-b49c-bd13f70064cc | -7.889 | -44.0049 | 2025-09-23 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 43a42841-21fa-39e6-8ac4-b56a90c08269 | -6.2598 | -45.3184 | 2025-09-23 01:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 6534d6f3-7dee-3c2d-9364-11821abae9a6 | -7.8887 | -44.0281 | 2025-09-23 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 1220093f-ea0c-3a7f-adde-4b911fe1c72d | -11.6439 | -52.8397 | 2025-09-23 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 014acc47-cf99-30d4-be73-8c21dde2a085 | -11.6247 | -52.8624 | 2025-09-23 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| faa28c12-9b2c-3dc5-91b6-3602057c23e1 | -12.7491 | -46.8849 | 2025-09-23 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 80dd26e2-7a5e-3d6d-800f-9b0438687c0e | -11.2118 | -46.1521 | 2025-09-23 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.1 |
| f0bc8459-35a9-3d3a-9583-0dda632bd5b8 | -7.889 | -44.0049 | 2025-09-23 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 98e6a704-efd6-356a-942a-07072ca23114 | -12.7568 | -57.8616 | 2025-09-23 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 5623b2fd-b552-3ff7-bc0c-026bb3faa401 | -11.6436 | -52.8605 | 2025-09-23 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 75d9c561-24f8-30c5-b8a3-04eab95752b2 | -17.5146 | -40.1945 | 2025-09-23 01:20:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 96.9 |
| 6803f2b2-eab0-3c62-933f-d680d4877b52 | -11.6247 | -52.8624 | 2025-09-23 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| b57f4f1d-3b81-3545-a361-0e617205053c | -11.8946 | -41.2612 | 2025-09-23 01:20:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 51.0 |
| 0d8f7125-17e4-323d-9eb0-793fe49e9a31 | -6.2596 | -45.341 | 2025-09-23 01:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| ba26b192-4151-3c1c-b2ad-d0e12b6dac62 | -17.5154 | -40.1685 | 2025-09-23 01:20:00 | GOES-19 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 109.9 |
| aa32c512-0d57-33af-82f8-ad975d23d889 | -12.7565 | -57.8815 | 2025-09-23 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 86da5aae-8398-3ccc-8c62-017ef2965d51 | -12.7758 | -57.86 | 2025-09-23 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 81963b61-600f-3a71-9fe4-fa7008223409 | -11.6249 | -52.8416 | 2025-09-23 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 5fb1f0c7-86a5-3c34-a859-a1324a854676 | -7.8887 | -44.0281 | 2025-09-23 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 93.5 |
| c62598f1-b693-3076-aa41-03d9babab557 | -6.2598 | -45.3184 | 2025-09-23 01:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 988e59a4-5e6b-3a23-aef7-5b2902d6b4cf | -11.6439 | -52.8397 | 2025-09-23 01:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3d717dfb-b98b-3b6c-85ea-11ab8114a943 | -3.5161 | -49.4528 | 2025-09-23 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 03eb4fde-8bd0-361b-8d2f-4bc6508d8c10 | -11.6249 | -52.8416 | 2025-09-23 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 91.8 |
| f4353217-f276-3cdf-bf14-e891c69e3957 | -10.9713 | -45.707 | 2025-09-23 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 96df39d2-8740-36b1-8c44-04a1c1c98776 | -11.6247 | -52.8624 | 2025-09-23 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| f08f18e5-f0ba-3c55-83e5-fec8f212b8a8 | -6.2596 | -45.341 | 2025-09-23 01:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| aa26e89b-d214-3c82-a7ca-2ba1d520740e | -11.8946 | -41.2612 | 2025-09-23 01:30:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 46.9 |
| eb418f6d-859c-3ed8-b09b-a4bc5b891cd3 | -7.8887 | -44.0281 | 2025-09-23 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 421d4dc5-610a-33dd-94f4-5f4daa1cb2f3 | -10.9522 | -45.7096 | 2025-09-23 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 2f499917-086f-3d32-b1cf-b7d0c64e8255 | -11.6436 | -52.8605 | 2025-09-23 01:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 6790234c-675d-3345-aa1d-84661901f8e7 | -10.9713 | -45.707 | 2025-09-23 01:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 028fa0ec-f872-3574-bc66-4038a137df71 | -7.8887 | -44.0281 | 2025-09-23 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ee1f905d-432b-388d-a2d1-8adbb61ab8b1 | -7.8887 | -44.0281 | 2025-09-23 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 38ccf9bb-e78d-3135-8abe-cd7cf694edf3 | -12.7565 | -57.8815 | 2025-09-23 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 2ab11437-69a1-3c40-8c1a-c126021d11aa | -7.8887 | -44.0281 | 2025-09-23 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3625edda-57f7-3394-88b9-0008bd282d68 | -11.8946 | -41.2612 | 2025-09-23 02:00:00 | GOES-19 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 50.3 |
| df054967-b235-396c-be76-cbb58b4a76c2 | -11.6247 | -52.8624 | 2025-09-23 02:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7aeaadc4-7a1b-3f21-b036-3c0e9948a73d | -12.7568 | -57.8616 | 2025-09-23 02:00:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b0528b09-9076-3671-a222-0868a27e866e | -12.7565 | -57.8815 | 2025-09-23 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 791e9204-cb2b-3a8a-9696-fb8358d959f3 | -8.5179 | -44.9749 | 2025-09-23 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 432554b1-2c12-32fe-8260-2248364ba5ba | -12.7755 | -57.8799 | 2025-09-23 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 390f2c77-d9cd-3ea4-8747-1bd29c22ad31 | -7.8887 | -44.0281 | 2025-09-23 02:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 4819f881-85f1-34a8-9eb4-e2c06f52ff92 | -12.7758 | -57.86 | 2025-09-23 02:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8c242c65-82e6-3e7c-92cc-25dd190d36c4 | -11.6247 | -52.8624 | 2025-09-23 02:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3fa2ffd6-7c32-313a-8f0c-28b6671d2fbf | -11.6436 | -52.8605 | 2025-09-23 02:30:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |


[Clique aqui para ver as próximas entradas](README4.md)
