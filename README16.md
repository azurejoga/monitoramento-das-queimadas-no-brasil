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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf789476-5207-3151-aafd-b3fd1adcaa5f | -3.4791 | -53.8142 | 2024-11-30 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| de2ba8e2-4c0a-35d0-862b-7eff67a09c09 | -3.2591 | -53.6186 | 2024-11-30 03:40:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 51f285fa-4754-31a9-8168-66673dbd2e72 | -6.9341 | -43.5634 | 2024-11-30 03:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 51.4 |
| e1a72061-85a5-3d21-9664-20f0733cd59b | -3.0356 | -45.1193 | 2024-11-30 03:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 198.7 |
| 239dc27c-6a2e-3356-adf9-4efa39d633bc | -3.0171 | -45.0974 | 2024-11-30 03:40:00 | GOES-16 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| a706ee60-89fc-3f7d-b056-af699c12b7cc | -3.6757 | -47.1395 | 2024-11-30 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| feec7987-f0d7-324d-a059-b5aadbcb05ca | -6.8967 | -43.5436 | 2024-11-30 03:40:00 | GOES-16 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.7 |
| 010c1944-d4cc-39ac-972a-38a0f3fcc34c | -3.6758 | -47.1176 | 2024-11-30 03:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 511e9fde-a0b8-369f-b5c8-2caef2b961c0 | -1.6938 | -46.7833 | 2024-11-30 03:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 6feb931a-3e2e-30a1-8e5e-8472964715d2 | -17.6651 | -57.585 | 2024-11-30 03:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| f7086b5c-4fdf-3ce0-a679-f0dfe4c1c6c9 | -6.94171 | -42.83341 | 2024-11-30 03:46:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6355d986-04eb-3c25-9c7d-d2ef0993a71d | -6.89781 | -43.54549 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9622e930-16f6-3dcd-84f9-072fb758d768 | -8.71878 | -44.01741 | 2024-11-30 03:46:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a20824d-3096-3f5a-a6d3-d842b05df0be | -5.0383 | -45.25033 | 2024-11-30 03:46:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01efec77-a1b6-3cf8-a8da-d12a8a15c18e | -11.77039 | -44.63752 | 2024-11-30 03:46:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a6dc91d-0b9c-347d-bba1-42369e8b57af | -3.46442 | -48.93497 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2e7b4175-cd60-3bff-8c90-d720e5055f0b | -4.88486 | -41.30169 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 0d0e8d5e-5e20-3520-98a0-d9177af8ee03 | -3.59515 | -49.99045 | 2024-11-30 03:46:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 69d1212e-1684-3217-8453-a056d8f09cd5 | -5.96893 | -39.68473 | 2024-11-30 03:46:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 706795ca-f7f6-3961-9424-183de8878492 | -3.62099 | -42.73449 | 2024-11-30 03:46:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0aaa04fb-3dce-3777-969f-6b3ee64bb338 | -6.12515 | -44.92165 | 2024-11-30 03:46:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15e8d41e-35f8-39ce-9688-a61849535b3c | -6.91882 | -43.5586 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5e3530f2-730b-3403-be3e-fa42b7aec50e | -4.08101 | -47.02539 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 56e26c1c-964f-356d-853b-8a69fb612815 | -5.55914 | -41.43496 | 2024-11-30 03:46:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 70bbc34a-b317-3756-8c38-c9ae72f37c4f | -3.68688 | -47.14605 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f72e0fd-3f19-3536-bde9-58f6efa27646 | -4.02087 | -47.001 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe94d409-a357-3618-ac65-331303290952 | -4.08616 | -47.03106 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| be428025-0271-3be4-8917-f4f2ee2daba1 | -6.13266 | -43.9561 | 2024-11-30 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 20644427-7405-3fb6-a3e7-282620b8198e | -3.0292 | -45.12102 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 5aac1514-75f7-3f6a-ad78-f2ec074c1ccb | -3.54652 | -45.8163 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c777114-38b4-38ca-8758-48f42d5d151b | -4.87972 | -41.30784 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6464f1e7-0de3-349c-b702-9475b17b350b | -2.62921 | -46.88526 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e2ec845-19c5-30b6-8d85-8786e8a4f033 | -3.69371 | -47.14251 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 41fc74c2-f588-31bb-9bd9-599094229daf | -7.16213 | -38.70955 | 2024-11-30 03:46:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 726ff7e6-6748-31e6-98ee-1c043b9c450c | -2.58438 | -48.20363 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf110d0d-fb02-32b1-be94-1e91ae2e9f8f | -7.0788 | -39.64811 | 2024-11-30 03:46:00 | NOAA-20 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 009b0fb9-f4c5-348a-831f-d5725dd6dece | -4.87236 | -41.27764 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dce01276-90ba-3046-af17-681ebdfc87ec | -4.87575 | -41.28202 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 9f7bd6fe-65f1-3eb7-90e1-b5ffb22d27e8 | -5.74196 | -46.18256 | 2024-11-30 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86e1d934-b645-3def-ae3b-f3dc1b70e672 | -2.76066 | -49.2289 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0510211-be7f-3288-b142-caf7a9b08516 | -6.92178 | -43.56855 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62c6d182-5808-34f7-84fe-c25c31546819 | -2.98177 | -49.59821 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 430d3f19-599e-3622-97d8-770b2fc271c8 | -3.01313 | -45.10095 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 24.8 |
| b06810d1-8582-399c-94c1-f3b1d8ce26ae | -4.64619 | -43.74441 | 2024-11-30 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 393f9a10-85ae-39f7-91f5-a4ff9d3c75a1 | -4.88429 | -41.30515 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| dd98799a-dcb4-3c4a-902e-a61db7175d3b | -2.95927 | -48.04091 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82332a5a-24ff-3043-9aeb-966f3134037e | -7.13507 | -46.4173 | 2024-11-30 03:46:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cf2d19f-d748-3725-91cf-56b1bc81ffdb | -6.22557 | -47.28447 | 2024-11-30 03:46:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6ef5431-6734-3295-b652-fd72155a6438 | -5.46099 | -43.27213 | 2024-11-30 03:46:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75a72696-1294-3ee2-906e-8e41c11b3e35 | -4.85289 | -41.32039 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f44ff92d-7f02-3424-ac8e-a739b82464b8 | -6.07391 | -48.05427 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| e6d99418-937e-321b-a559-bd48b51c1b76 | -2.24914 | -46.45406 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73b08791-51e7-30d9-9e48-b3badffe85c7 | -4.10122 | -46.11291 | 2024-11-30 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 938923bb-85b9-3ac3-83db-52d9ef22f4a1 | -6.83404 | -35.32079 | 2024-11-30 03:46:00 | NOAA-20 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b21d4f40-3972-3040-a13f-3d243c6d686d | -5.98538 | -39.9572 | 2024-11-30 03:46:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f5681976-48ae-328b-accc-d151d12f02a8 | -6.91291 | -43.53867 | 2024-11-30 03:46:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| 02605bc2-4883-3be2-b16f-8b93ca79eb72 | -8.84216 | -44.76297 | 2024-11-30 03:46:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f988a2b5-8cd0-328e-a35f-20eaf525a460 | -6.24489 | -39.85767 | 2024-11-30 03:46:00 | NOAA-20 | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| be7d7c7d-e43c-3acf-86fe-11388c4e3889 | -6.82076 | -46.77291 | 2024-11-30 03:46:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06554a39-6537-3e6b-a7f9-2532d0af6e06 | -6.08184 | -48.04565 | 2024-11-30 03:46:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 72184638-4442-3548-bfd0-1e6fd4e332f1 | -3.02806 | -45.12781 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e4245c6c-4750-3df1-b43a-c0e332bfbd83 | -5.07588 | -44.99389 | 2024-11-30 03:46:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b6534e6-9c8e-3dae-bb0a-eff146b90c42 | -6.92489 | -43.55021 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e91b2e9d-98a7-3d14-b944-81785abb133a | -4.0757 | -50.04023 | 2024-11-30 03:46:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8ae4e7c5-4d60-3ca8-9488-0b6707a8c9b8 | -5.42266 | -44.85519 | 2024-11-30 03:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03d2fcf2-f78e-358e-8e85-c4f5ee73f3d2 | -4.04415 | -46.86622 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 94a6bb7c-98cb-3dc5-8e3d-0a2fae2cdf9a | -6.84702 | -38.79441 | 2024-11-30 03:46:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2be73e20-9853-3d6a-889c-638fe47ff2d2 | -6.92333 | -43.55938 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc45288f-e588-3274-bde4-eb242a07f7dd | -4.59001 | -44.70715 | 2024-11-30 03:46:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 921d4801-da03-37e3-8ea7-8d0fd0942052 | -6.70525 | -47.27574 | 2024-11-30 03:46:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8a4f6ab6-5d07-3eb5-8325-1345c978a3d7 | -6.90978 | -43.55706 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d11f0eb-1f7f-3ffa-99c1-2be92440a233 | -1.6827 | -46.78504 | 2024-11-30 03:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| db363f8c-f3f9-3f98-9ea2-02cae69a193e | -1.51413 | -45.90005 | 2024-11-30 03:46:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f5edcd1-2cb2-3aa6-91db-5615b2ac6871 | -3.02863 | -45.12442 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| d7b21c3a-88a4-3e27-8f4d-0871071ceaf5 | -6.97522 | -39.86153 | 2024-11-30 03:46:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bab43dc9-474e-3ce7-8a03-a4f55dc4f217 | -4.878 | -41.29334 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e5c149b9-c577-3bb8-b685-34f3ab637e60 | -1.8872 | -48.65265 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 712ecc8e-de35-3295-9757-9a0be14b80e9 | -3.13887 | -45.98338 | 2024-11-30 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3227c987-d1aa-386b-a127-b26b29cacd82 | -6.25596 | -44.97004 | 2024-11-30 03:46:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06288472-8300-38c5-8bc5-5ad3dd6aab50 | -3.84056 | -46.52609 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4676c69d-2860-3e6f-b666-c88d5d28ec6b | -4.86837 | -41.3017 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 1f5552c3-6457-3d10-af5f-b8df8dc7b4ab | -4.43488 | -46.01208 | 2024-11-30 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 987d28f8-fc75-30ba-ba12-17539a163266 | -4.44192 | -48.56974 | 2024-11-30 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 338653b6-5d4b-38b8-85bb-e0a7bb4f0714 | -1.30645 | -46.77833 | 2024-11-30 03:46:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6852d598-19c6-32df-abd6-a224f769b151 | -6.99484 | -35.25249 | 2024-11-30 03:46:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 03ad637e-6fe4-3c10-bf34-dc238c83932d | -6.91587 | -43.54861 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.0 |
| bf0b2846-6cee-389e-a984-a56c765ae253 | -4.87688 | -41.2752 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| be34c235-878c-3fd8-a0b4-107c98b27205 | -3.96334 | -48.10107 | 2024-11-30 03:46:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4be6552c-42e3-3493-aef4-f91d15366381 | -12.35954 | -43.7655 | 2024-11-30 03:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e235532d-2459-3e82-9b82-077c4cf0e0da | -3.6214 | -42.74151 | 2024-11-30 03:46:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d9eb2a83-f572-31fe-aa37-acd1b9e19b4d | -3.67635 | -47.1349 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 41b2e7d0-1318-3ed5-be5d-1d4c20e6cc6f | -3.08216 | -49.21737 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| db3fc5e1-26ca-3de2-87de-fd93c45d4f97 | -4.87346 | -41.271 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 305c83d9-66b8-30c9-a52f-cdd7518b1e90 | -2.51602 | -48.18575 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5c891eaf-e314-3f94-a7d2-8ce0137dfc51 | -1.68168 | -45.78283 | 2024-11-30 03:46:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 14d8d566-db79-3497-a2ff-51c8f04e3e9a | -4.8284 | -41.28532 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 91254e41-176a-3848-8e8d-920b045e67f3 | -2.27642 | -46.43655 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21ad6d10-ef7a-3b8c-86ec-689c3bdd36a1 | -6.68564 | -39.26252 | 2024-11-30 03:46:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9d705010-3482-3a8c-979b-5fdb957f1144 | -2.32468 | -44.82949 | 2024-11-30 03:46:00 | NOAA-20 | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc3a3a6a-29eb-3c75-bdd2-dc3ca67fb366 | -3.9194 | -38.66249 | 2024-11-30 03:46:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
