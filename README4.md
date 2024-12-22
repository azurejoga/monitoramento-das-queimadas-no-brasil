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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df310e4f-14bd-36cc-851f-87200040c304 | -1.82486 | -45.71143 | 2024-12-22 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd399964-5451-3de3-9d6e-b8124df0aed4 | -2.72109 | -46.18007 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6cd96823-0e2d-39d9-9f81-1ae033a36911 | -4.03318 | -46.79463 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3848faf-e79b-3c59-b831-612108b613b6 | -3.75075 | -47.18312 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a81a8c88-121a-3ba7-aae0-41c97286d9b6 | -3.7569 | -47.18776 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a1b9ab3-4bef-3ee2-b2ad-e5bdeed1261c | -3.83996 | -46.68193 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be0ba1ea-a647-3c45-a5aa-0e55d79b4830 | -1.15148 | -53.59732 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09739c84-765b-3356-bb9e-094533c04252 | -4.01902 | -47.05836 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a3260acf-a945-33cf-839b-3f6710622467 | -4.03984 | -46.79564 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81ed54c7-8e61-30d9-8c66-1be5ca0efde5 | -3.92211 | -46.91665 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d192c3b-0e5f-391e-9d53-a21d1b8e73d3 | -2.14832 | -53.59251 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1888ead7-f930-3f99-95f6-72dcec75d23c | -2.73854 | -46.87251 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15c3e970-3721-3567-a5f3-4f696b1bc5c6 | -2.06045 | -52.05697 | 2024-12-22 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4b30e725-6fc4-3179-afbf-0f6df3672ee9 | -4.00882 | -46.55891 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e686929a-4de7-3b27-a64c-4b67407e08f0 | -2.79896 | -46.70505 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 565d3be7-4906-3483-8dde-7a22a3103a43 | -1.71627 | -52.56967 | 2024-12-22 04:25:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9e19cb13-1165-3135-a0af-c21c0042ad2a | -2.80174 | -46.74874 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7f0bd6c6-0d6b-3690-ade1-41aa5bf8be8c | -4.04872 | -46.80416 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18c499f1-c896-3406-a0ea-f971dac6524f | -2.55505 | -46.93142 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a184ae49-563c-30b9-b770-5cf8fe2de1ae | -2.58183 | -49.46878 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3b0250b-b63d-3523-9f2e-ef3fca18131c | -2.81723 | -45.9376 | 2024-12-22 04:25:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46b05cfe-47b2-3b39-bc4c-46092005e790 | -4.09618 | -46.74023 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b67fd0d-e3da-3128-8db5-56ff4fe66fd3 | -2.63329 | -48.03029 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| df1ddda0-5536-3d8e-b3c6-d5a4d968e000 | -2.49755 | -48.06516 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bfbc2457-10ef-3965-9a8f-b705014640da | -3.08669 | -46.56046 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af39144e-8034-3bbc-9051-cbf4abc059dd | -3.15517 | -45.9942 | 2024-12-22 04:25:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66367116-d656-31f2-8c89-47ce2df9b3f5 | -2.81909 | -48.2532 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25002430-00d0-3de5-a938-d24d52bc1fc4 | -2.50166 | -48.06182 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 58dca33a-169b-3aaa-8f4a-8907df6e99f4 | -2.6292 | -48.0336 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 21561a81-83e9-314d-9c07-75ce0fe6ee7d | -2.44597 | -51.7897 | 2024-12-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f4ddc397-7db6-3237-b2d8-17b7bdd57a62 | -3.91641 | -46.36749 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3353b2c-e309-30b9-93b6-03798036217a | -2.75115 | -44.76612 | 2024-12-22 04:25:00 | NOAA-21 | BACURITUBA | MARANHÃO | Brasil | 2101350 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36e08680-7d9b-3c68-a761-4d5e62c65528 | -3.88379 | -47.02972 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0605bb35-f6a1-340e-9ce5-92ea20ec7f00 | -3.98781 | -48.40934 | 2024-12-22 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4a6b2579-10d2-3709-acf9-f78996233791 | -3.0114 | -46.99516 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfcd9072-7839-34be-91bf-6d15d944d194 | -2.25045 | -48.31725 | 2024-12-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 943dbdc2-96a2-3a21-b45d-daf8a19c3d16 | -4.04794 | -47.02674 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3b12cb0-4b12-3c65-b027-f2504a5e72e3 | -1.36644 | -53.69997 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c449dc27-15cf-3963-902f-d7f494e31ee5 | -3.85211 | -46.66958 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcb34401-306b-3964-9cf2-c6358d82fb16 | -3.75577 | -47.19488 | 2024-12-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3cbda26-0ba8-3d99-a622-c7ab1c7a19c0 | -2.60261 | -47.0008 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69623d10-c38d-3348-b9f1-292a71c6ae38 | -1.17474 | -52.54613 | 2024-12-22 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eceeae69-2880-321d-8ec4-e445ec40cc7b | -2.63268 | -48.03413 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1e6d24e4-ede3-3d1d-b69f-a11b28f9bc07 | -2.58099 | -49.48071 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da744f77-96a2-3c93-8ef1-8c1cb4c8e185 | -1.36848 | -53.6869 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f1fc25b-cca7-3730-8917-ac2db7bb3e7a | -3.98705 | -46.6764 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57ed8cfc-a3c3-3205-ae25-2344e9a09a8f | -3.92824 | -46.44351 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c481786-8c22-3ba6-9b92-0a2e4c824b33 | -4.04849 | -47.02322 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1134c0f-7994-3478-a014-565a351535ab | -3.95033 | -46.30214 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1dd7aee-e2a0-36f7-be38-b5ac86d37ff9 | -4.09341 | -46.73621 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa2f2368-a729-358b-abf0-859b398a79e9 | -3.92046 | -46.92718 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dcecbb48-defa-34a5-83bf-5f60c1f5235e | -2.8032 | -54.18919 | 2024-12-22 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f4e9b1f-daed-36eb-8cc6-f0750f867ba4 | -4.49844 | -44.11321 | 2024-12-22 04:25:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bbc7030-ae70-3876-bfdb-ae7b993984e2 | -4.00497 | -46.56186 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9016363a-bb25-3aac-9ea0-55721037b17f | -3.91624 | -46.67255 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b76cbec4-7613-3b57-a409-568f01341a6c | -1.3713 | -53.69554 | 2024-12-22 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a8e3111-25e6-31d3-9416-b94f55e53dda | -3.91803 | -46.35713 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| a7aa4342-2e72-3a8c-a8ec-4060e86f01fb | -3.91051 | -46.99043 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1040e0f7-31e7-3a85-bd27-c117ff70afef | -4.10058 | -46.81955 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3058f01e-14b8-3bbf-bc11-151eaacca888 | -2.82063 | -52.86247 | 2024-12-22 04:25:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b277784-c05e-30c4-b57e-56d5171d9c3c | -2.98899 | -51.44142 | 2024-12-22 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1bfaffd3-7118-3577-8b7b-8cde6b2e6916 | -4.01545 | -46.79909 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72673aee-e7d9-35ca-b6fd-ab5592ba2d34 | -1.55065 | -46.13813 | 2024-12-22 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66a964a6-34ca-36f9-a7c2-854f092c89ac | -2.50597 | -49.06563 | 2024-12-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9079d7cd-7c5a-3c1d-ae4c-8544662af89a | -2.58346 | -47.54811 | 2024-12-22 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2fb54464-d5fb-3386-bf0e-9df4992ef0f0 | -3.80016 | -46.71857 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14fa7db1-4ed2-39f9-90a2-be2331d12228 | -2.58042 | -49.47782 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2f39a42-1e32-3e5b-ae75-47b4180f22f5 | -2.74049 | -46.20782 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 623f391e-8817-3a43-a763-ee4df527df18 | -3.90384 | -47.01108 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d824406-37c6-35d4-b40e-1809843c57ea | -3.93153 | -46.90015 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 59d0614e-2a0a-3638-978c-d0ca775e59e2 | -3.80363 | -46.84794 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19193c27-3124-3211-b270-2f5cb90351f4 | -2.65171 | -46.10151 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1eabe99-8b00-34c2-baa5-83e14c321983 | -1.13805 | -54.19767 | 2024-12-22 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae734209-3516-3d97-8daa-1b098f5e0d9b | -2.58112 | -49.4733 | 2024-12-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 838ff8ff-0a61-38c0-aa37-f7caf4a40f10 | -3.91985 | -46.88761 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fe4f9df0-6021-3579-8a12-c69076a98289 | -3.08282 | -46.56344 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60d9a26f-98e8-37ad-911d-6b4e750b2e9e | -0.95858 | -46.85315 | 2024-12-22 04:25:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 749cac47-8ea0-392a-8aff-0811664c51fd | -3.92765 | -46.90314 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0921bf37-e132-3bc4-a9fb-b32b5495cd74 | -4.05389 | -47.09276 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b089fad4-19cd-3db6-9568-2e7a7336ea76 | -2.44092 | -51.79319 | 2024-12-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e876d1d8-4eea-3613-b5a5-e2176d6e1c07 | -4.00828 | -46.56238 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6cb3ddd4-ec31-3582-a402-505e46cae9ad | -4.06448 | -47.09076 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16302f96-5c11-3bfa-b5d8-3ec3718c38da | -1.56363 | -46.77339 | 2024-12-22 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea5cf214-0876-3466-929f-9ba010617184 | 0.00397 | -51.67436 | 2024-12-22 04:25:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea1890c0-efc2-3074-9205-f940cd8e67a4 | -3.79738 | -46.71461 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 72b9d84d-a868-3239-93dd-c114a9d244d7 | -4.02292 | -47.05536 | 2024-12-22 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 658654a5-415b-3d9e-9914-e483f0aceeb3 | -4.939 | -41.34327 | 2024-12-22 04:25:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6dac79cf-af96-302f-9a06-69679fadb596 | -3.08892 | -46.56793 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96c0e13e-5d13-3eed-a367-7d335b3ab164 | -4.10842 | -46.92102 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b77c55f-c377-3c93-ba44-057e2d14813a | -3.87122 | -46.56939 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34ca30f1-66c7-355c-aab0-f06e4b6c78dc | -1.82426 | -46.54214 | 2024-12-22 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b473967-23e2-3329-9e94-f53bdb7e606a | -4.02265 | -46.79664 | 2024-12-22 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db8dbae6-e68f-368f-8ca8-3a41f97c9842 | -2.70772 | -46.13561 | 2024-12-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b6fbf51-84ad-3c2d-895f-94f3b5e39c6f | -2.79842 | -46.70856 | 2024-12-22 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 287de3cf-6052-358b-add4-2e498458d48a | -3.43717 | -45.64761 | 2024-12-22 04:25:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f3cfb82-df4b-3c0b-809f-3d10f8ebb42c | -2.05793 | -46.59306 | 2024-12-22 04:25:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87bd18f7-b54c-3f61-a3ac-0c3ea14c5cb3 | -1.82763 | -45.71537 | 2024-12-22 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd294047-bf59-3aff-8fd6-395ffc3c9a58 | -2.56803 | -45.96166 | 2024-12-22 04:25:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e24a21c-c147-3a5c-b9f6-0b762cdd6581 | -1.92029 | -45.64547 | 2024-12-22 04:25:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3084c6ff-0c39-3780-8bd9-31abbcda7ee5 | -4.60667 | -45.45301 | 2024-12-22 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README5.md)
