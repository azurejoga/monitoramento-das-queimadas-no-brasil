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
| 619c577f-7b17-31d9-8f6e-b7c9fcad8cf4 | -4.6835 | -46.4074 | 2024-11-08 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 307bb0cf-5ed9-37f7-8864-6cd3c055e828 | -4.2134 | -44.2696 | 2024-11-08 00:00:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 063f23c5-8f23-3770-8209-49b7a71ba7de | -3.9669 | -48.1716 | 2024-11-08 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| dd2fcc69-c6c6-32ee-a750-66cd683ee1e0 | -3.1641 | -54.4854 | 2024-11-08 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| b3047de8-4341-3be8-a4f9-b84401224001 | -3.5631 | -47.3847 | 2024-11-08 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| c45df82a-cfe5-3eb4-b3f9-f041f7790bd7 | -3.7068 | -41.6758 | 2024-11-08 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| c0753ae3-5494-3fa1-96d0-ac48faf2985d | -3.0396 | -53.2805 | 2024-11-08 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 5283ab81-78c7-3e06-8d2c-9917a3b3f70f | -2.603 | -51.7589 | 2024-11-08 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| efe64544-5b36-38b6-8f85-54fd1f1b914d | -3.8047 | -44.0153 | 2024-11-08 00:00:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 47.5 |
| a7aca86f-9d67-3e99-8260-0391d1f39af0 | -4.6647 | -46.4306 | 2024-11-08 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 20508129-8942-3b85-8f73-ac64c9fa8ce4 | -3.0884 | -45.7463 | 2024-11-08 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 72e8e169-56b6-343b-a3cb-250165611110 | -2.6214 | -51.7585 | 2024-11-08 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 35bbb11e-65fe-385a-95dc-15f0a70157f6 | -3.7255 | -41.6748 | 2024-11-08 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 127.6 |
| 70427ba8-f37f-386c-aa61-0b0a74951f15 | -3.1458 | -54.4859 | 2024-11-08 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 8d5113c9-9a14-33a2-b0b8-2aec0fbf1e38 | -3.2373 | -45.6959 | 2024-11-08 00:00:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 814cdebb-bb39-3a4b-a7cc-4ca703b18de7 | -4.6834 | -46.4296 | 2024-11-08 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 161.8 |
| cc253233-893f-3b81-a31e-cb1c6dde11e8 | -3.4881 | -51.5896 | 2024-11-08 00:00:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 591c4743-221b-3d57-ba5f-46f89b01667f | -2.603 | -51.7383 | 2024-11-08 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 7e185e65-af55-3ac1-aa5b-a54714bf3565 | -3.7066 | -41.6997 | 2024-11-08 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 144.7 |
| bb8b81a9-d9b2-3386-aad4-822b0d45505a | -3.1642 | -54.4654 | 2024-11-08 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 75ccabd8-71f6-365d-bfa2-2aef599a6f98 | -3.5632 | -47.3629 | 2024-11-08 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 72cf22b7-2863-3e77-8908-5e2f2f6d9ed2 | -3.1458 | -54.4659 | 2024-11-08 00:00:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| c3a7248e-3c0c-395b-a845-9d3a8f14ea12 | -3.6394 | -50.7536 | 2024-11-08 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 884b521d-fa05-3951-9411-e47f3f010053 | -3.0947 | -53.3196 | 2024-11-08 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| b88e8a4f-c602-3061-9ac9-43866b409d09 | -3.7254 | -41.6987 | 2024-11-08 00:00:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 157.2 |
| 39586fe4-ebf4-3416-91e9-176c6f23038a | -3.967 | -48.15 | 2024-11-08 00:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| faa3b44d-1e21-3d39-bfa3-0de170afc40e | -0.6522 | -52.3826 | 2024-11-08 00:00:00 | GOES-16 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 41.4 |
| a50b3bf1-c442-32fb-9162-95cc0ba141bf | -2.6764 | -51.8189 | 2024-11-08 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 25816f5c-9832-3fc7-8184-341688bc9995 | -6.2642 | -39.3546 | 2024-11-08 00:00:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 8284d218-3b78-3b05-85d4-79b3375cc1c9 | -2.7172 | -45.6922 | 2024-11-08 00:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 39.8 |
| e2d0488a-a6ab-3923-9ed0-16c7278132c7 | -3.5078 | -43.7761 | 2024-11-08 00:00:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 181a0aff-907b-3c37-b3f6-4dd0ed4b8591 | -4.316 | -45.6914 | 2024-11-08 00:00:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 04adfdea-7568-3105-a583-6884155b0f0f | -2.7198 | -45.0628 | 2024-11-08 00:00:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 51d1e802-1120-3fcf-a33c-7231108821d3 | -3.4838 | -52.617 | 2024-11-08 00:00:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f9d0300d-be62-343f-b381-787228e73d52 | -3.5446 | -47.3855 | 2024-11-08 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 6376d965-1b59-3bb0-8993-e8c41a0ba46b | -3.0698 | -45.747 | 2024-11-08 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 5e2c471e-b43b-3d45-9182-759a7be0f36a | -2.6214 | -51.7378 | 2024-11-08 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 91ae67c3-01b0-33aa-a36d-c2e8146d5dbd | -3.7861 | -44.0162 | 2024-11-08 00:00:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 17d721a0-cad8-3f13-8623-38e62b046b5c | -4.6832 | -46.4518 | 2024-11-08 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 253.6 |
| 5f13698c-04d1-38bc-a555-1ac4edfb480d | -3.5447 | -47.3636 | 2024-11-08 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| c8c064f7-f6ba-34cf-bece-d43d84392564 | -5.082 | -47.9433 | 2024-11-08 00:00:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 6342abf2-ae08-34ee-813c-d9b5cf376017 | -4.6646 | -46.4528 | 2024-11-08 00:00:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| f78693df-8c41-3623-9f47-eb8e94f49685 | -2.81 | -52.88 | 2024-11-08 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6c18dcf-2dd8-32f2-8010-74833e1b8ccb | -4.68 | -46.43 | 2024-11-08 00:00:00 | MSG-03 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a4c9570-b06d-31d6-bbfe-4920a307d69b | -2.81 | -52.94 | 2024-11-08 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f27a7b02-413a-3460-a7db-acae3fac0897 | -2.81 | -53.0 | 2024-11-08 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6304161a-66f3-3d4b-bd11-fe1ca13fa290 | -4.49 | -45.7 | 2024-11-08 00:00:00 | MSG-03 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 51e34312-f48c-3bd6-969e-530eb7f7f23a | -3.71 | -41.69 | 2024-11-08 00:00:00 | MSG-03 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 421209f7-3ccd-3565-891a-7ef54a385844 | -2.78 | -52.94 | 2024-11-08 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff72717-3470-33e7-b40e-9d9175a41ce9 | -4.52 | -45.7 | 2024-11-08 00:00:00 | MSG-03 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a8e68224-d019-33b4-9359-d6539e95c4d4 | -2.6764 | -51.8189 | 2024-11-08 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 8c6994d1-7fb6-3e8b-a593-86042da55ffd | -2.6214 | -51.7585 | 2024-11-08 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 14b0167c-6e7e-3298-97cd-ca1f9b083064 | -3.0698 | -45.747 | 2024-11-08 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 1184ce8f-1bb8-3534-b918-d0f755a2ee98 | -3.1642 | -54.4654 | 2024-11-08 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| fb3c1524-085e-3d3c-baf7-d23be02dc7fc | -3.1458 | -54.4659 | 2024-11-08 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 2a370e6c-9a64-3aba-a2f2-5367fc2ae8c5 | -3.5447 | -47.3636 | 2024-11-08 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| ac9225c6-4da6-34d9-aa65-d4f604990379 | -3.4881 | -51.5896 | 2024-11-08 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7e7295d6-c11e-3c48-a93f-071c423ca567 | -3.7255 | -41.6748 | 2024-11-08 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 121.9 |
| 86b6146e-17d7-34e2-a880-f0ea135f4112 | -2.8612 | -46.7746 | 2024-11-08 00:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 94e9e4a5-8b30-365d-9378-0e82c75000e2 | -4.6647 | -46.4306 | 2024-11-08 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 9702ed0e-dc66-34fb-92d0-7c656bc11aef | -3.1462 | -45.3179 | 2024-11-08 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 498ac7ef-cb78-39d9-b59b-7a186a70a4d1 | -4.2975 | -45.67 | 2024-11-08 00:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 3e19f11d-58a9-3e0e-a561-d864d01bea99 | -3.5632 | -47.3629 | 2024-11-08 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 5cc0ae5e-de42-32b1-a66c-7fa6461f93c2 | -2.603 | -51.7383 | 2024-11-08 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 23748a32-2c04-33ff-8c75-e5aa69030ac9 | -4.6834 | -46.4296 | 2024-11-08 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 195.9 |
| e787a53c-c6e0-38af-9fea-dbe117c490ae | -4.316 | -45.6914 | 2024-11-08 00:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 127.4 |
| cbe997d4-1090-3e2d-a608-c547dfd7f3aa | -4.6831 | -46.474 | 2024-11-08 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a8ede4da-b2ab-36da-9a3b-019eb4223536 | -3.4838 | -52.617 | 2024-11-08 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e5957449-63ab-3e3c-b349-372a4715c715 | -4.2974 | -45.6924 | 2024-11-08 00:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 70.0 |
| a1a43e09-9468-35a9-a796-d501b120ee48 | -6.2642 | -39.3546 | 2024-11-08 00:10:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 76.5 |
| f22feb14-a3a6-344a-9e8e-e8033fbf7c33 | -2.7198 | -45.0628 | 2024-11-08 00:10:00 | GOES-16 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 24622eab-ed54-378a-8ef7-2ed2bb52179e | -3.1641 | -54.4854 | 2024-11-08 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| ff618670-14f8-3b3c-84e7-a4a6aad1e6b8 | -3.2373 | -45.6959 | 2024-11-08 00:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| c6471f07-e4d0-34cb-8019-4c480e579932 | -3.967 | -48.15 | 2024-11-08 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 8e84cc87-50d1-31fe-83ed-675c12906b4e | -2.6214 | -51.7378 | 2024-11-08 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| fa2ce7ee-05f2-35ea-bbc0-ae81c3064511 | -3.8047 | -44.0153 | 2024-11-08 00:10:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 76f08980-27b5-3942-b4f1-e86242a8e010 | -4.6646 | -46.4528 | 2024-11-08 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 109.3 |
| a11f4e2a-1091-301c-b629-fd89a9d3241f | -4.6832 | -46.4518 | 2024-11-08 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 281.1 |
| 6c6a8373-90d4-35d0-8def-747719677f97 | -4.6835 | -46.4074 | 2024-11-08 00:10:00 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 72.7 |
| e5e40a06-fa2a-379e-bb89-9caad78dd5d6 | -6.264 | -39.3797 | 2024-11-08 00:10:00 | GOES-16 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 75.5 |
| f8528a74-5527-3694-9607-eab0485a57d7 | -3.9669 | -48.1716 | 2024-11-08 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 8906efcc-46a4-317b-9fd5-79c870e7264c | -3.1463 | -45.2954 | 2024-11-08 00:10:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 1df6ad1d-c5d6-31b4-b85f-d859b133c9e2 | -3.7068 | -41.6758 | 2024-11-08 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 61f638fc-6df8-34a1-8d00-3338f9d75eb4 | -3.7861 | -44.0162 | 2024-11-08 00:10:00 | GOES-16 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| c5c90d06-d7a6-3f37-a2e9-3a6dfa0d69a1 | -4.3161 | -45.669 | 2024-11-08 00:10:00 | GOES-16 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 61b44b89-3c23-3c36-ac07-1755989879dc | -3.7066 | -41.6997 | 2024-11-08 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| cda28d49-2093-335e-89e7-dd2b92e6acf6 | -3.0884 | -45.7463 | 2024-11-08 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 82b05ae0-e11e-336b-b7b3-c7710fa5e168 | -3.1458 | -54.4859 | 2024-11-08 00:10:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 00125caf-96de-3d2a-b59a-bf59f4b1aeb1 | -3.7254 | -41.6987 | 2024-11-08 00:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 151.6 |
| 16dc3cee-4765-3db2-85cd-b4c134f3fa6f | -2.603 | -51.7589 | 2024-11-08 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 352481a2-5e39-3fb1-9592-c6a49571ae7b | -2.6228 | -51.3038 | 2024-11-08 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 0c021619-cee5-3d26-b681-e399b64e2f76 | -3.5631 | -47.3847 | 2024-11-08 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 094b3abf-3e1c-3368-bec9-16fcbd1e58b7 | -1.1489 | -52.0099 | 2024-11-08 00:10:00 | GOES-16 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 11e4b54b-b8d7-35b7-82fe-8c958828bc9a | -3.5446 | -47.3855 | 2024-11-08 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 6eeda853-de5f-35a5-8754-3afad1cc5695 | -10.1793 | -36.3088 | 2024-11-08 00:10:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f1aa986f-6293-3f73-816d-d9054faadab6 | -6.2673 | -39.371498 | 2024-11-08 00:10:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 480f7311-48f7-391e-a053-1b7e33bd85a6 | -6.2656 | -39.363998 | 2024-11-08 00:10:00 | METOP-C | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1b0931a3-ffbb-335b-8210-1b60f4190bc6 | -3.1483 | -44.3894 | 2024-11-08 00:10:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e5d711d8-ea18-3efb-b87c-1d2e5720c87f | -3.1615 | -44.402199 | 2024-11-08 00:10:00 | METOP-C | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b913c578-fa83-3d87-a5be-caa73b09ee1e | -8.5131 | -42.1008 | 2024-11-08 00:10:00 | METOP-C | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
