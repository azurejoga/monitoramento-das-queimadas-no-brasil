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

## Dados Diários - Página 380

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da65ef8f-e5a8-3f74-a8bb-e38cceb3d0d1 | 3.64747 | -60.027 | 2026-10-08 16:41:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 78cdb5cf-42c2-31f5-9e47-6971c8c4c885 | 1.69327 | -55.62827 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d014737e-c770-3e5d-b54f-a7ece3e6780d | 2.75627 | -60.03363 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8ee40dcd-c311-35b5-87d5-1d4f567d2f72 | 4.03543 | -51.60836 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a31327ff-7931-3875-a49a-ef7d2a300493 | 1.67889 | -55.64055 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bf9d832e-45bc-34ee-8e29-3b34a7065129 | 3.71468 | -51.50508 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 301ea9ae-31a2-38fc-ac60-5dd91b4b8ad5 | 1.6424 | -55.77625 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e29ac402-eeb5-3140-924f-b7cdd8eb020d | 1.81453 | -55.5254 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| cfc88547-e0c1-3db1-9ef2-a4c8ec19d763 | 1.70173 | -55.60723 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| db3b287a-bee8-3f26-b6ba-b8837e4a3299 | 3.73924 | -51.63477 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 10ce04aa-0738-3004-b25a-6ca47b7f2dae | 3.20732 | -60.17305 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 08e9a860-3bef-3348-bd72-567c7b787d80 | 1.02821 | -52.60648 | 2026-10-08 16:41:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 17.9 |
| e422cf0e-0e9a-39b9-b73e-1c53f1c81d04 | 1.66853 | -55.80355 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 876ba024-e2ba-3c07-8e0d-e85b223a9806 | 2.00534 | -55.88553 | 2026-10-08 16:41:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 412eac42-b0c8-3855-be29-74980c9b48a3 | 2.75422 | -60.0066 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 9b52122f-c71e-3637-bbd8-6bd74bda5f30 | 3.79379 | -59.80227 | 2026-10-08 16:41:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| e40d6292-2b70-3f4b-8e49-d090a55f679f | 2.00129 | -55.87919 | 2026-10-08 16:41:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 091a2a3b-de9b-36a1-8f93-2944925580cd | 2.26836 | -55.87447 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 82b54340-e950-3f52-bfa5-ef8939d03efc | 2.76268 | -60.03469 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 8f2aff69-2593-392a-a1e7-8ee2fcf2724f | 1.6612 | -55.79277 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fed7e42b-5bce-3abb-bded-0fc23ec55fda | 1.7026 | -55.60186 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f693c806-481d-37f4-9c5a-fa09dcf39b5c | 2.75538 | -60.03893 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 4d2150b8-4241-3e1b-8982-1ba6b36793b5 | 1.68748 | -55.63295 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 1021010a-3173-33b1-bbfc-86f3a9faaf8e | 2.7551 | -60.00139 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e3696bc8-5878-364c-83a4-e32f984f2882 | 2.58156 | -60.12333 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1c8c9a31-0bca-3401-bfd5-7688889e4940 | 1.73362 | -55.59562 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fef9b2a1-49b9-322f-a858-0f6aed5a6744 | 3.54442 | -51.27599 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b701881f-9889-3b96-b159-a7a482626d2e | 1.6604 | -55.79066 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0a5ed91-b8e7-3653-b9cf-69b60bf73335 | 2.75716 | -60.02832 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 9fac64e3-e256-3247-b35c-2318189f4959 | 2.10738 | -50.8377 | 2026-10-08 16:41:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5e8644e5-4078-33bd-82fb-61633dbea02b | 1.20931 | -54.62057 | 2026-10-08 16:41:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca7a9715-a8ea-3bee-a94f-72b6b434b3d0 | 3.73691 | -51.62567 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 50c49c9d-a78a-3937-9de2-0717fdd983b8 | 2.09604 | -50.84011 | 2026-10-08 16:41:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b2975204-ff98-3a82-a41f-ca321914faf3 | 2.14402 | -55.94532 | 2026-10-08 16:41:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3ad598ce-0fef-3d5f-9968-852e473285a0 | 3.61627 | -61.07013 | 2026-10-08 16:41:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a26ee685-0121-3742-923c-02e999f2aa16 | 1.69952 | -55.60476 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 50f5b97c-d74a-3fbf-b262-0f7fa41efebf | 3.6741 | -60.67362 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.3 |
| db3028ff-dbb8-3ccf-9ec0-86eb91db78b1 | 2.00624 | -55.87997 | 2026-10-08 16:41:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 731f065c-a0ac-3aba-b294-1497e6661a9b | 3.20624 | -60.17186 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dbc051ac-00e9-3dc6-aac2-ee95ee17c4ac | 3.67517 | -60.67772 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| bee39d6a-cfb7-3df8-9470-518dea78b988 | 1.76663 | -55.54538 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 90d8249c-8c3e-3c1d-8f49-45f615cca7b7 | 3.73625 | -51.62993 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 87f0d0f6-bbe9-33b2-950b-791ba029c591 | 4.62514 | -60.09341 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 89c84449-8a4a-3249-a74c-70cd07eea790 | 2.76357 | -60.02938 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 996d1ff2-47f5-30cc-9bf7-6a1d99659595 | 4.4501 | -60.93719 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 2f70fc8d-fed8-374f-ad5f-bcb7d2f18f9f | 1.77234 | -55.54078 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| cf198a34-b214-3e49-85c2-61ac805c572c | 4.68691 | -60.57325 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 742a3e45-fd45-30d0-aee0-10d3c66541d9 | 3.31207 | -60.06039 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d2ac2360-a33e-3352-9348-c82bb74de8b1 | 1.81305 | -55.52674 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d2e76d56-5d79-3d96-90c1-8a8113c97933 | 3.64113 | -60.026 | 2026-10-08 16:41:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6ff641d6-60da-37c4-8bee-e4af1a30a4df | 1.63746 | -55.7754 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 086e53a8-a4bb-3a39-bb4e-ce8d77154e19 | 2.75977 | -60.01276 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 21.7 |
| bcf795c3-d2ce-36c6-b275-7c2d7a386d72 | 1.70749 | -55.6026 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6824fdc9-a958-328a-b951-849206bdcf1a | 3.54801 | -51.27655 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 46411e7f-9a3b-351e-aeb3-b0eaa4ff1979 | 4.27932 | -60.3456 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7bc52c69-c1bd-30f9-a109-ed8009efa6fd | 1.7345 | -55.59019 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 76742d4e-31a5-31db-8b66-89c9b08d3b50 | 2.49591 | -50.91987 | 2026-10-08 16:41:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 569c9c9c-8008-3ee7-9673-8e8ee8cfcd1f | 3.68319 | -51.37613 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 58acddac-3709-3432-bf04-2498c2357b6f | 3.74982 | -51.61459 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7c301c12-e70a-31ca-90a4-891882dd2643 | 1.76749 | -55.54002 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f2f163c1-2055-3d51-8dee-1a982551c38b | 1.35208 | -50.83557 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 4cfd844a-eb5a-344d-a11a-2dd163cd1117 | 3.79539 | -59.80475 | 2026-10-08 16:41:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cb5cb35d-2dcf-3a8b-933c-2a862aeb0f31 | 2.76179 | -60.04004 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 861a9751-6acd-39e0-8bcf-6ed40a9f8cbd | 3.55033 | -51.28535 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 7cc7c4eb-a612-3b64-a60d-c2b1a31bd04d | 1.68548 | -55.63049 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 56ceef14-61fe-3dc9-92e9-74a918625e98 | 3.7467 | -51.61275 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 432b4992-57f5-3027-87a3-e34d73cbd8fd | 0.44511 | -60.54111 | 2026-10-08 16:41:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0d3da521-697f-315b-9ca6-6c3db409515c | 1.67975 | -55.63507 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 674e99a5-9ff3-3297-a04f-6459bb488253 | 3.46476 | -51.47697 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 1bb725ea-d80b-38b9-b63d-ded7615f0f20 | 1.69867 | -55.61016 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 22e8eecb-3110-39be-a478-05b04404b5ea | 3.73822 | -51.61714 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 21799908-af57-3998-bc88-20e6c7f45731 | 1.65546 | -55.78986 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8e612423-67b8-3ff3-ac9a-a3deef5bb866 | 1.33405 | -50.83282 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1bc16209-f57c-3a24-857d-596f1df4a555 | 4.45153 | -60.95517 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3bf5d894-3c8d-34ed-b9c3-6820a9b24c5f | 1.20963 | -54.62131 | 2026-10-08 16:41:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 69b74d0b-29ee-3301-abdc-8e9d8a52f34b | 1.3491 | -50.83088 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 3cb748a4-bfbd-32e6-b362-57e195f1c233 | 3.6686 | -60.67658 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| dd303ef5-5094-32a3-b4c0-bf30833cf5ac | 1.03527 | -50.01953 | 2026-10-08 16:41:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 11332fdf-6a15-3530-9576-e31451180482 | 0.95443 | -50.7993 | 2026-10-08 16:41:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d22d6c80-d695-33e6-9f11-b34d83484b9c | 1.53588 | -50.74073 | 2026-10-08 16:41:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ff9ef903-3c82-3418-97c2-4a23c84bf8b5 | 4.62412 | -60.47091 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 17.0 |
| be007d75-1fca-37c1-810a-3f16d6a98588 | 4.44696 | -60.94275 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 15.1 |
| e4895207-9a94-395d-b44d-3f7fedfdf267 | 3.54147 | -51.27131 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1b517350-7022-352c-823e-27de602d8180 | 1.65953 | -55.79626 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a0aced90-28c8-3609-84f9-d2bce2f20a77 | 1.03168 | -52.61058 | 2026-10-08 16:41:00 | NOAA-20 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 2611528b-2db8-35f7-99ae-ec77c42d0235 | 3.33813 | -51.61502 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| c6c22418-691e-31f1-8d0a-235f73cc4d9c | 1.71324 | -55.59799 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 790e3791-a2ac-3f84-aad5-374de7089c9b | 3.72768 | -51.73404 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 577e6971-ccca-33d3-bb7d-a41f506f0f0d | 2.14899 | -55.94608 | 2026-10-08 16:41:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f9d39202-c321-3f59-be96-3d0a1278ab73 | 4.449 | -60.94355 | 2026-10-08 16:41:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 538b06a9-3f8d-376c-9911-75a9ac7b3a49 | 3.51827 | -51.25507 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c8818b72-b10b-3109-89d7-f97521bcc13c | 1.76005 | -55.55539 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9a3bd6e4-8b0d-3f7e-89a8-a462f425e4c2 | 3.7275 | -51.73253 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f579645b-acf2-3d6a-bef8-342abfd1193f | 1.50461 | -55.67811 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fd3cb4b7-3172-34ad-9750-fc3ed3f21468 | 1.68464 | -55.6359 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7a5334e2-ab0c-384d-9f08-ce8018d16fd9 | 3.73559 | -51.63419 | 2026-10-08 16:41:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 8bae1c57-a193-3b18-8246-e898b5af9aa2 | 1.6643 | -55.80481 | 2026-10-08 16:41:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 908bdd82-b703-3633-97b4-52837bbd7404 | 1.7916 | -56.06424 | 2026-10-08 16:41:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d266b26-b95e-3c92-9fb4-9d7be3cbe8e7 | 4.30442 | -60.31461 | 2026-10-08 16:41:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9887e386-4db7-3fae-85b7-a10edb778c48 | 3.31434 | -60.0581 | 2026-10-08 16:41:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 26.2 |


[Clique aqui para ver as próximas entradas](README381.md)
