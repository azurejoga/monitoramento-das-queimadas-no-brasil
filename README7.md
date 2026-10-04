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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a0ad632c-67a4-35e5-8baf-a3f3b3e7a926 | -3.1839 | -54.0839 | 2026-10-04 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 6ede5b19-2f86-3be7-9c2c-80fb6aec87bd | -4.2559 | -46.3633 | 2026-10-04 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 239.2 |
| 268b26ed-521b-344b-8db6-ddf63d55c1c9 | -4.3072 | -50.2668 | 2026-10-04 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8f8d9879-d208-39ec-8259-837c49beb902 | -4.4845 | -45.5478 | 2026-10-04 00:10:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 102.0 |
| cad65f02-3376-306d-aa57-8b48f678b874 | -7.7551 | -49.2067 | 2026-10-04 00:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 50.5 |
| a91bc17d-00f6-3867-b102-784d8b403dd8 | -9.9175 | -65.0313 | 2026-10-04 00:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 6489aed4-3602-323a-b0f2-fa583652eb6b | -4.2558 | -46.3855 | 2026-10-04 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 5d76b919-f7ee-3129-89c7-7720d737ec04 | -3.0364 | -54.2282 | 2026-10-04 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 5c9a0816-36de-3431-b08d-ef9a4f9c5adf | -2.5842 | -51.8623 | 2026-10-04 00:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 142.0 |
| c9beda43-f5c0-3e0b-88d9-fd14cd29f84c | -3.4761 | -50.1094 | 2026-10-04 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 7ff37342-3b14-39ec-b960-32b2519821e7 | -2.8163 | -54.1129 | 2026-10-04 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 137.0 |
| d030b75f-0363-34a2-8d42-8d1f4322a25b | -2.5842 | -51.8829 | 2026-10-04 00:10:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.4 |
| a6169714-ccee-3275-a4c2-db58a5a3c7b5 | -14.5877 | -52.8789 | 2026-10-04 00:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| e9b710d2-4321-3f2e-8cc6-18874ef04ca8 | -2.8164 | -54.0929 | 2026-10-04 00:10:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 797d5a28-786f-3f38-85df-5236459668e1 | -3.0906 | -49.5307 | 2026-10-04 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| c6d41854-5ad8-3ee3-9b11-07b40bfce86b | -3.14 | -53.75 | 2026-10-04 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7697e223-8567-3c1a-a7d4-f5adcf20b976 | -4.27 | -46.39 | 2026-10-04 00:15:00 | MSG-03 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 11766a6a-ba91-3ad8-a4e0-8b4bce821ca3 | -3.11 | -53.75 | 2026-10-04 00:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93b8475a-771b-3cbd-b85d-a82c2a7677f6 | -6.0074 | -53.5325 | 2026-10-04 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| cc1fe581-da19-358b-96a9-c2f991e669d5 | -2.5843 | -51.8417 | 2026-10-04 00:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1fb1183a-cb91-34cf-bb9a-ba37155342b5 | -5.8642 | -55.7071 | 2026-10-04 00:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 416a3b28-efde-3bff-b4cd-cc0272f06533 | -9.1332 | -65.9559 | 2026-10-04 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.9 |
| f5c1b600-9310-337b-a73b-3df753512c3e | -3.8757 | -55.7986 | 2026-10-04 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 83aeceaf-57eb-35f1-b313-09e9c2315162 | -4.2744 | -46.3846 | 2026-10-04 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.5 |
| bc69e1ff-0dea-30a0-b5f2-3592261d2a22 | -4.2745 | -46.3624 | 2026-10-04 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 123.1 |
| 62301307-6932-3b5f-b66c-a0d8271cdf4d | -3.1115 | -53.7637 | 2026-10-04 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| a2fb2091-ca6c-3136-98db-d5fbdca07454 | -9.899 | -65.0132 | 2026-10-04 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.4 |
| cf5454f0-37c7-3a42-be12-66cce2660eef | -2.5657 | -51.8833 | 2026-10-04 00:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| a205c230-442e-33c9-ad90-481ba7a0d430 | -3.1839 | -54.0839 | 2026-10-04 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a58b6d2c-016b-3d90-844a-8423c28b4c26 | -3.4762 | -50.0883 | 2026-10-04 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 0d3a2c56-70db-3a0d-ba17-2fa8e448ca1e | -3.4761 | -50.1094 | 2026-10-04 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 2d21764d-4d73-3324-b7c8-a1b65502ed21 | -4.4845 | -45.5478 | 2026-10-04 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 5a889868-fcb1-39a6-b115-6002b183cf75 | -3.5128 | -54.6162 | 2026-10-04 00:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 035a508b-461b-3376-abcf-2598eef68630 | -2.8164 | -54.0929 | 2026-10-04 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 792f1e1b-38d1-322c-aad2-e8e2c9b61bb3 | -3.0721 | -49.5313 | 2026-10-04 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 0dfe82ee-519b-3fef-b812-449e14e223d2 | -3.8756 | -55.8184 | 2026-10-04 00:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 76a76ca0-cab7-3b67-b420-1f522a2f018a | -4.2887 | -50.2675 | 2026-10-04 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 203.3 |
| cd0b5125-3a98-3eef-99f5-efb1ca7b42ef | -3.1116 | -53.7234 | 2026-10-04 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 276.1 |
| ab338f2c-ad1a-3f01-b679-180ea0e25784 | -8.593 | -66.8081 | 2026-10-04 00:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 596e07d4-c331-35db-8170-d57637014f83 | -4.4847 | -45.5253 | 2026-10-04 00:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 68.3 |
| b011d751-a737-3aea-8f2d-45ed0eb24fc6 | -3.0548 | -54.2277 | 2026-10-04 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 8624bb72-5111-3656-bb80-64ea1adc1607 | -3.13 | -53.7229 | 2026-10-04 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 157.0 |
| d8aec138-2851-3906-9c01-a12f6f85fbba | -2.5658 | -51.8628 | 2026-10-04 00:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| fcfa033e-1e62-3c43-bb5d-d75b234a58be | -2.798 | -54.0933 | 2026-10-04 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| d19b5375-02d5-376e-90de-1a8d0825bdc8 | -8.5551 | -67.0686 | 2026-10-04 00:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 4d6aac2e-572d-34b8-adf2-664fde76aa4f | -3.514 | -59.8065 | 2026-10-04 00:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 5089a9ae-5863-3227-9392-18dddc76d724 | -4.2886 | -50.2886 | 2026-10-04 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 13f88ebd-b500-32b0-b7f9-a70a631e036f | -7.7551 | -49.2067 | 2026-10-04 00:20:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ea2649cf-75a4-3c56-9ff0-361161c45430 | -3.0364 | -54.2282 | 2026-10-04 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| bc7cc518-59eb-3f14-9e78-4720ee3c86a4 | -15.241 | -40.5346 | 2026-10-04 00:20:00 | GOES-19 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| 5deee42b-86b7-3326-a4ae-7b70bc4ab572 | -2.8163 | -54.133 | 2026-10-04 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 2f9403e8-1000-3fe5-92ec-a6aeee52a4aa | -14.5683 | -52.8814 | 2026-10-04 00:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 332b79eb-aea6-35d9-bbb2-8943fc8836ea | -1.0911 | -54.1001 | 2026-10-04 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 903046b1-02b8-31d3-b9aa-f37b3e1d11d0 | -2.5842 | -51.8829 | 2026-10-04 00:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 642d9e38-c596-31ba-adf7-723da2dc1b14 | -2.8163 | -54.1129 | 2026-10-04 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| 0fa7c21f-d586-345b-baca-a91320840869 | -3.072 | -49.5525 | 2026-10-04 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 633e8ba4-9b7f-385d-843d-63da9d21df07 | -3.1299 | -53.7431 | 2026-10-04 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 7d34840b-0755-30e7-9c27-d5a48f1c3d3d | -1.0911 | -54.1202 | 2026-10-04 00:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2af2daca-1f9d-3958-9655-fb5957741d6a | -4.2558 | -46.3855 | 2026-10-04 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| add61e77-d3d1-315a-9c77-e07f45d841b7 | -8.3526 | -62.8302 | 2026-10-04 00:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 36da7a4d-d3e2-31ed-bd99-a3a3713f3398 | -3.4577 | -50.089 | 2026-10-04 00:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a20c347f-4323-317b-bae9-b4085295c26f | -4.2559 | -46.3633 | 2026-10-04 00:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 5bdb3110-3c4b-31e6-a9b0-7def658700bb | -3.1117 | -53.7032 | 2026-10-04 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| e3b92382-7435-302c-8557-a17652be302b | -2.6026 | -51.8619 | 2026-10-04 00:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 1291dbca-a16b-35d3-b32e-aeb447f9d6fa | -2.2297 | -53.7026 | 2026-10-04 00:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 1e4757e8-5644-3b94-aedd-74a7d5c69014 | -3.1838 | -54.104 | 2026-10-04 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| cd51186e-4240-38e0-8edf-30ab1689ea93 | -3.8848 | -49.6933 | 2026-10-04 00:20:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 618cd52e-a588-346d-bc7f-d5adcf9c58dc | -3.1116 | -53.7436 | 2026-10-04 00:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 300.8 |
| 9dcd66f1-5ff8-3067-a19a-25cba548a554 | -2.5842 | -51.8623 | 2026-10-04 00:20:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 2a9d89cc-c9d4-3c55-8821-6e6f98534557 | -2.7979 | -54.1134 | 2026-10-04 00:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 49211a5d-4ae7-350f-ba3d-8ef4811089f8 | -6.0741 | -47.2703 | 2026-10-04 00:30:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 12c620ac-2516-37dd-91fc-5b0e4cc3839e | -4.2745 | -46.3624 | 2026-10-04 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 1716e3ec-1fa9-3940-b4c0-1d26893f8b4f | -2.8164 | -54.0929 | 2026-10-04 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 827d3e2f-0689-32c0-a5a3-1018389ce2db | -14.5683 | -52.8814 | 2026-10-04 00:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| a0ecda24-54e0-3db3-90a9-aaa7a9c84bde | -3.1115 | -53.7637 | 2026-10-04 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 03eaa674-a41c-3d58-b277-d067e9b37a26 | -2.8163 | -54.133 | 2026-10-04 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 144c21c1-b9d4-3027-af75-0046dcd8bafc | -3.514 | -59.8065 | 2026-10-04 00:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 7178abc4-6253-37a3-83b1-f96a393dd065 | -3.2951 | -53.8395 | 2026-10-04 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1cd99b62-0bc7-3dde-a16c-74ae6d18b5b2 | -3.072 | -49.5525 | 2026-10-04 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| c9a25624-f851-3f98-8f3c-1f2c85a689a9 | -6.0739 | -47.2922 | 2026-10-04 00:30:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 71c6cb38-60e7-3311-b866-6857a34aedaf | -9.0857 | -61.1629 | 2026-10-04 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 643e94d1-5f94-3ff2-922d-f52c466a0b5b | -3.5128 | -54.6162 | 2026-10-04 00:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| f66558ad-7d14-349a-aa15-06800d6e2ae4 | 1.767 | -55.6451 | 2026-10-04 00:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 7e166425-3096-39ea-9cb2-80ffab1b68fa | -3.1839 | -54.0839 | 2026-10-04 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| bbe2082f-98fd-3590-a4c3-b209bbcab168 | -4.4845 | -45.5478 | 2026-10-04 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 765a3383-6ec2-33d2-b175-96ae8a28997b | -4.4847 | -45.5253 | 2026-10-04 00:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 3242238a-86f0-3c50-a958-1161d76945c6 | -2.798 | -54.0933 | 2026-10-04 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| aef9c95a-daee-39a4-b505-661fb0bb1641 | -2.5842 | -51.8829 | 2026-10-04 00:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 1709855c-61e8-3888-987d-5037473818a7 | -3.9033 | -49.6925 | 2026-10-04 00:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 798feb62-1c7c-37a0-a59a-a6c7477a4e7f | -2.2113 | -53.7029 | 2026-10-04 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| c851f5d4-783b-351b-a80e-6cbc66189707 | -2.5843 | -51.8417 | 2026-10-04 00:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| b09b4bf0-9d35-38c7-aa55-515870081cde | -8.5551 | -67.0686 | 2026-10-04 00:30:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| b6f95156-ae55-3b44-a5ad-7a081798ef88 | -3.1299 | -53.7431 | 2026-10-04 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| bbf830ca-e177-318c-a26c-2a7fce6f0a6c | -3.1838 | -54.104 | 2026-10-04 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b74f83e5-827f-3aba-9b1b-d5d6d7289dcf | -3.7559 | -49.5711 | 2026-10-04 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| b188216e-199f-3690-9e8d-b6814c8cfd0b | -3.1116 | -53.7436 | 2026-10-04 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 265.5 |
| 012a12d3-6647-362b-adc5-04f370c98b6e | -2.6026 | -51.8619 | 2026-10-04 00:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 364212c8-3d0a-3116-b171-ba24b96f535a | -4.2887 | -50.2675 | 2026-10-04 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 194.0 |
| be509fc5-c349-37f2-b021-ec10c4f34c9a | -5.8642 | -55.7071 | 2026-10-04 00:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 07439743-5da9-3219-8c84-aeb197464c69 | -2.7979 | -54.1134 | 2026-10-04 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |


[Clique aqui para ver as próximas entradas](README8.md)
