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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efaeb9cf-f956-3fa9-b30d-5804d6defbed | -10.6674 | -44.4835 | 2024-12-01 02:40:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 7d8c64ae-d090-3677-a2ad-617adf324b00 | -2.6578 | -51.8811 | 2024-12-01 02:40:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6680cd8c-a23f-3a91-976a-b03da06b4f46 | -3.2591 | -53.6186 | 2024-12-01 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 6e5ef25b-37ee-36c3-a3ab-f2f295f5ec17 | 1.1621 | -56.0066 | 2024-12-01 02:40:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f52329e7-253b-380c-8d29-16a4ebd9eac8 | -3.259 | -53.6388 | 2024-12-01 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 5f0a3e20-8802-35b2-ba3b-95e85df55963 | 3.2755 | -60.0781 | 2024-12-01 02:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 6cb46c7c-043b-3ea5-8168-5ca6c5516218 | -2.7503 | -51.7553 | 2024-12-01 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4bbef7f3-5482-38b6-9d89-a21afbd8eb55 | -3.2774 | -53.6383 | 2024-12-01 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9835c8a8-29f5-3d2f-bca0-5ba2d55a1927 | -4.5394 | -45.7019 | 2024-12-01 02:40:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 1021dcef-1813-32fe-b813-087bf4f3c250 | -2.9963 | -45.5706 | 2024-12-01 02:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 8080ab47-b3cd-3081-a413-6a214b8f83bb | -3.3134 | -53.8592 | 2024-12-01 02:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 2c428dff-a762-3cdc-ab2a-d29a1cee3ca7 | -2.6578 | -51.8811 | 2024-12-01 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b978f534-27dc-3928-9daa-45f53d961924 | -3.2591 | -53.6186 | 2024-12-01 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| afe05e57-6a19-3e63-8351-f57bb3523d9d | 1.1622 | -55.9869 | 2024-12-01 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2c1360b8-79a8-333c-97df-0cecf36642e7 | 1.1439 | -55.9871 | 2024-12-01 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 2d73b648-ec71-34c1-828f-98aa0dbcc50a | -2.8197 | -53.0425 | 2024-12-01 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| ebd4b496-62c6-3e0d-9469-26268d6a5d29 | -2.8196 | -53.0629 | 2024-12-01 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 08a2844d-083c-3774-9d73-272bca43abf3 | -4.5578 | -45.7232 | 2024-12-01 02:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 129.7 |
| 371686d6-2689-3806-9dd5-dbddc8edf436 | -3.1273 | -54.5264 | 2024-12-01 02:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 32ae7bd9-80a7-3d41-b38c-fc9ee2749063 | -2.9963 | -45.5706 | 2024-12-01 02:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 655b8e85-7daf-3f04-990d-9ebb77f9f0c0 | -4.5562 | -43.3028 | 2024-12-01 02:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 2ea27769-bda1-3ea9-a349-6c0177f0fbe3 | -3.8171 | -52.2583 | 2024-12-01 02:50:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 02c43a99-e968-3df9-9c8a-e9d7d514923e | -3.5158 | -53.8333 | 2024-12-01 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c0b9e085-065c-3632-8430-b71f17042221 | -3.2774 | -53.6383 | 2024-12-01 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 4d63bb91-ee8e-38c4-8f2c-adfb0f18e045 | -2.7503 | -51.7553 | 2024-12-01 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 3c48cb28-b8f9-3345-bb4d-94724846f983 | 3.2755 | -60.0781 | 2024-12-01 02:50:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 69.6 |
| a2f2623a-88cd-307f-8665-6919e4103f74 | -3.4974 | -53.8339 | 2024-12-01 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a97f3a6f-c864-3fad-8a20-e77a34a9c0c1 | -4.5394 | -45.7019 | 2024-12-01 02:50:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 1f4a5c28-7bb4-335e-a46a-ae88fede8c71 | 1.1622 | -55.9672 | 2024-12-01 02:50:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 0d3a935c-755d-3b96-838d-dad9fe9e83f9 | -6.9156 | -43.5418 | 2024-12-01 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 6dcdbe16-4258-38b9-8177-dcea7b597486 | -3.4754 | -50.2776 | 2024-12-01 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| bbc22fa2-fe00-3e3c-904d-6f04dad244ed | -4.5375 | -43.304 | 2024-12-01 02:50:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 59c13d8b-14ce-313d-bcec-fbc35bc1eb6a | -6.9344 | -43.5401 | 2024-12-01 02:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 91d9a06f-6083-367d-91cc-39a7173924a8 | -3.259 | -53.6388 | 2024-12-01 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 686beaba-c5b6-398a-9c1d-45133e216e19 | 3.2755 | -60.0781 | 2024-12-01 03:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 51.7 |
| bacfa139-ddda-3169-815a-a94b989e9ce3 | -3.259 | -53.6388 | 2024-12-01 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| 18020fe8-fa67-32ea-9ca6-00d302ac98d6 | -4.5563 | -43.2795 | 2024-12-01 03:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 171095c6-b4d3-3f73-aa33-f598e9c3e615 | -10.6674 | -44.4835 | 2024-12-01 03:00:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 4f697844-6d9c-3fd7-b751-96850d266763 | -4.5394 | -45.7019 | 2024-12-01 03:00:00 | GOES-16 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 69.6 |
| f336bacf-ae3c-3cfb-a59d-db484aa180ae | -3.2591 | -53.6186 | 2024-12-01 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 16ece315-7ac6-3099-806c-ad60a72694da | -3.1273 | -54.5264 | 2024-12-01 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 964847b8-a174-32da-a576-ad89f776047c | -4.5562 | -43.3028 | 2024-12-01 03:00:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 183.1 |
| ef668492-045a-3fea-a584-0af31591ddf3 | -3.4974 | -53.8339 | 2024-12-01 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 4970a95b-2c90-39f6-9cfe-570fa6cbe749 | -2.6578 | -51.8811 | 2024-12-01 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b6ffd352-84ff-33bd-9594-444dfacaef72 | -6.9156 | -43.5418 | 2024-12-01 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 6dd68108-8d83-3517-b355-c9ad35450657 | -2.8197 | -53.0425 | 2024-12-01 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| aa3a5d63-7bb4-3a04-ad83-f157be5765c1 | -3.2774 | -53.6383 | 2024-12-01 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d3deea19-60ec-3eb3-a46d-9e6ac7ed2892 | 1.1622 | -55.9869 | 2024-12-01 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| d2ba1f33-48d4-3cb0-8b03-ccd4d3af6ca7 | -3.8171 | -52.2583 | 2024-12-01 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| c1133714-27b9-346c-a5c6-937cd6d00074 | -2.8196 | -53.0629 | 2024-12-01 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 119cc002-aa22-3f81-b31b-a7785276eb74 | -4.5578 | -45.7232 | 2024-12-01 03:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 109.4 |
| 264d9653-d58d-32fd-b908-921dda8802ef | -3.8355 | -52.2576 | 2024-12-01 03:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| e2718522-e62d-3278-94f6-38afda0235ab | -2.7503 | -51.7553 | 2024-12-01 03:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 7d21713b-6410-37c1-a4df-d7449b228720 | 1.1439 | -55.9871 | 2024-12-01 03:00:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 71e7276d-4fde-35fd-84e8-c488fdf9d305 | -6.9344 | -43.5401 | 2024-12-01 03:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 60cde36d-4a50-383b-a0cc-af2fff8b9e95 | -3.4754 | -50.2776 | 2024-12-01 03:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 9805d11f-257e-3c60-ba7c-a801754c01e5 | -3.1456 | -54.5259 | 2024-12-01 03:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 909292fb-0ac4-3d98-b96c-548d34433ea6 | -7.34444 | -34.81621 | 2024-12-01 03:04:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b1675a74-11a9-384c-a99b-a2cbe687860f | -8.75641 | -38.7905 | 2024-12-01 03:04:00 | NPP-375D | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 71fe9d26-2a94-34fa-9ac1-7d6aae5ad1d9 | -7.43146 | -39.11667 | 2024-12-01 03:04:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 956209b9-53ed-38d9-9147-0e267c6daff8 | -7.33866 | -34.81814 | 2024-12-01 03:04:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4e337835-535c-332e-b6a2-5611d27e3c07 | -8.55129 | -35.75869 | 2024-12-01 03:04:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3307afd0-f30d-3a64-90f0-06a77e1dcbe4 | -9.5273 | -37.0309 | 2024-12-01 03:04:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8810298d-cfe2-385d-acd5-bc684906f23b | -9.52145 | -37.02971 | 2024-12-01 03:04:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fbc3e40d-22b7-3e5c-bc4a-a39980adc4ac | -9.52541 | -37.03119 | 2024-12-01 03:04:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 488f7036-d3ea-3b8d-a3cc-3f201f53ec00 | -7.33924 | -34.81487 | 2024-12-01 03:04:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a5aa1b46-0c85-349d-9ab7-358d50ed88dc | -10.12698 | -36.32124 | 2024-12-01 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 134f12ec-a856-3d35-9ba7-35e7eea016ff | -7.33816 | -34.8149 | 2024-12-01 03:04:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5c0bc717-e651-31a4-81da-1baa91a720f6 | -7.43123 | -39.117 | 2024-12-01 03:04:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 8d7628f7-c61e-3650-835c-083d920d8954 | -7.33875 | -34.81165 | 2024-12-01 03:04:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7ce804fc-264b-3dd2-8c45-e94069d041d4 | -7.3398 | -34.81165 | 2024-12-01 03:04:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99bea155-19fb-30f5-85ce-9de940856831 | -9.83994 | -36.16003 | 2024-12-01 03:04:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6bfbd13f-395b-3e6e-9354-85a7ce87abb4 | -8.74718 | -35.91818 | 2024-12-01 03:04:00 | NPP-375D | LAGOA DOS GATOS | PERNAMBUCO | Brasil | 2608701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d9d619f5-1b35-332d-be10-c9d0416530e7 | -7.64754 | -38.30625 | 2024-12-01 03:04:00 | NPP-375D | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 997287c4-5188-3f7d-810c-2b365ff6ade6 | -7.6409 | -38.30558 | 2024-12-01 03:04:00 | NPP-375D | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 23eb3185-6b21-38fe-b7bc-43034f05c861 | -8.74984 | -38.789 | 2024-12-01 03:04:00 | NPP-375D | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c8ab0faf-dded-3d62-96e6-f773b454d40f | -7.64582 | -38.30623 | 2024-12-01 03:04:00 | NPP-375D | SANTANA DE MANGUEIRA | PARAÍBA | Brasil | 2513505 | 25 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0d94e75b-b7a7-37a2-870c-efcf87700df6 | -7.33756 | -34.81817 | 2024-12-01 03:04:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 047a260a-4447-3ea7-bf2b-5f509df11a09 | -9.83445 | -36.15885 | 2024-12-01 03:04:00 | NPP-375D | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 96f0b902-742c-310e-85ce-6c1d6832f692 | -7.34337 | -34.81618 | 2024-12-01 03:04:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0bfe36f4-cc5f-3fde-8d35-55f7f8c57ff0 | -10.13251 | -36.32235 | 2024-12-01 03:04:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 23d7c76b-b5d3-3c33-9c20-c5d6707958df | -8.55191 | -35.75528 | 2024-12-01 03:04:00 | NPP-375D | BONITO | PERNAMBUCO | Brasil | 2602308 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 783f0ab4-f8b2-3bf6-acd6-08091476bdf5 | -2.8013 | -53.043 | 2024-12-01 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 73e7397a-d6b1-353e-a8ec-11b12a095d30 | -4.5578 | -45.7232 | 2024-12-01 03:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 91.9 |
| ff735921-5597-3d58-a901-004a995b21e8 | -6.9156 | -43.5418 | 2024-12-01 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 69b78ccb-6ead-3c1d-a1a5-03501c86e15d | -6.9344 | -43.5401 | 2024-12-01 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 5d1c856c-b576-31fa-a755-a1e0992fb2d9 | -4.5562 | -43.3028 | 2024-12-01 03:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 332203c0-7197-3aff-addb-5871cedc8016 | -3.8171 | -52.2583 | 2024-12-01 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 78597555-2827-30ac-be9b-7da71b7e5a2b | -3.1273 | -54.5264 | 2024-12-01 03:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| c949e6fe-6edd-3b7a-b4d5-4ff0e2a9e00d | -3.4974 | -53.8339 | 2024-12-01 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 24f4dcd9-de92-3b03-9940-712ef0b7c3aa | -2.7503 | -51.7553 | 2024-12-01 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 8c9de356-b131-3100-bc22-7e41b65809b1 | -3.259 | -53.6388 | 2024-12-01 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 57f2eb52-b084-3d01-a742-5b76344733fd | -3.2591 | -53.6186 | 2024-12-01 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 77557fd2-d572-3275-8bd5-b91bbd001506 | 1.1439 | -55.9871 | 2024-12-01 03:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f7e2e3aa-d4f1-3786-84f9-7f2f9af5c4f2 | -2.8197 | -53.0425 | 2024-12-01 03:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 69e360e7-cf29-3606-a60b-d4555311b31b | -2.6578 | -51.8811 | 2024-12-01 03:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 29dbef49-651f-3594-b3af-df262fde097e | 1.1622 | -55.9869 | 2024-12-01 03:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 83dd674c-58fa-3f69-bf69-49b0e493d245 | -3.3134 | -53.8592 | 2024-12-01 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 04ae3560-f15f-3820-8799-f70272dcd091 | -4.5375 | -43.304 | 2024-12-01 03:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 595db7cc-9d88-31ba-9d40-7e24949f74d0 | -4.5578 | -45.7232 | 2024-12-01 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 114.1 |


[Clique aqui para ver as próximas entradas](README20.md)
