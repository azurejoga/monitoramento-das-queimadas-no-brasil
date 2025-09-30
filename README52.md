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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30f027e6-11ee-3416-aee1-0b13c1ecf363 | -5.70177 | -42.63855 | 2025-09-30 04:38:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d03634d2-6122-389b-92ff-2c8aeba825e1 | -3.21917 | -47.63292 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf3f85a2-4362-3a0f-8e57-4896d3b50019 | -4.75264 | -42.69844 | 2025-09-30 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cac986d8-1161-3a20-85e8-d895780fe25e | -6.70356 | -44.55614 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 578faf6f-78ed-3c39-949b-7bf62a2fee9e | -6.43407 | -43.07834 | 2025-09-30 04:38:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d0eb7282-15e2-31b7-9b61-236eb2aa5a1d | -5.22223 | -45.23154 | 2025-09-30 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc5f01f8-2ef5-3f00-9e3a-75eea48e1608 | -6.37371 | -45.61477 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 973ba710-7ddd-3082-bcdf-44fcb013a135 | -3.68563 | -49.78612 | 2025-09-30 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e642f98-4605-3e50-925c-f8b971ea5eca | -5.7169 | -42.87759 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 2c7f9773-2e50-3c07-832e-0fa15d48bf93 | -3.10042 | -47.01818 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| f0cc80d7-6fa8-3128-b29c-7f6d003208c1 | -6.21257 | -44.21037 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df96d97a-bcf2-3f66-b132-ea563a076071 | -5.52958 | -43.87397 | 2025-09-30 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 03542b5e-ccb5-31f8-8309-1c85c19dba34 | -3.86226 | -40.43813 | 2025-09-30 04:38:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 35146974-b737-38e9-baf7-3930398b8fd2 | -6.36725 | -45.10524 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 071fb343-af46-34ca-9264-c55c0f428855 | -6.16898 | -47.86137 | 2025-09-30 04:38:00 | NOAA-21 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5d3a41b-9d92-3139-916e-c633c415f0c2 | -4.62495 | -43.54822 | 2025-09-30 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 067dcdf2-bd3f-363f-9fff-b17f8241bcf8 | -1.9917 | -44.52623 | 2025-09-30 04:38:00 | NOAA-21 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b456961f-5dc4-383f-8e4c-e5720c6cf985 | -6.65909 | -41.39164 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 514a0f61-05b8-31fe-8e4a-ea8cc870c0a4 | -1.28945 | -54.18075 | 2025-09-30 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15e696b9-bbcd-3629-968a-8aa9a93e6882 | -3.84598 | -52.28689 | 2025-09-30 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| add7993e-63c3-3633-b1e3-8efcc1acdd3d | -6.37606 | -45.62454 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8d4fd5d-42dc-3dea-aeea-04743432df76 | -5.72873 | -43.96273 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 942dfcb7-246b-3b5a-8281-815a833016c2 | -4.67662 | -43.25987 | 2025-09-30 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff5c3061-e9df-31f4-874c-a647fb023141 | -4.00776 | -43.27608 | 2025-09-30 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d3018b40-678c-3333-a768-4be43a8ced1e | -6.53192 | -43.82528 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6eea1648-a3ad-32bb-b6a2-a0a20cca6d02 | -5.40865 | -45.85672 | 2025-09-30 04:38:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88e61a69-e36f-3e76-a17d-497f59a86d2a | -3.6646 | -50.50491 | 2025-09-30 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1da9bad9-c5b3-3ebe-be49-1027b851723a | -6.00797 | -43.80536 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a539d09f-763a-32b9-869a-9c2a2bfdc33c | -2.25905 | -47.85588 | 2025-09-30 04:38:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8d00253-7ac5-32bb-be90-3b66a9e772d6 | -6.04947 | -43.60386 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c184121c-dc9a-333f-9a5d-eb92da657337 | -6.68676 | -42.79847 | 2025-09-30 04:38:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| f1d0f362-e255-3de7-b3ad-ef067298f36f | -4.8973 | -43.4684 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| ff5273a4-4891-3d56-b369-90c55609801a | -6.10793 | -42.65463 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90289d58-c04c-34fd-9844-c09f3de61104 | -4.73183 | -46.47864 | 2025-09-30 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66daee17-df28-3761-9b45-68db8d68edcc | -5.74963 | -42.67145 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 502c6bd5-f07c-3357-9bbd-ee4bb79d6b4a | -5.77416 | -43.82758 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 595000bb-62fe-3588-aeb0-36b3e798adf1 | -2.1354 | -46.47272 | 2025-09-30 04:38:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb386bfa-63e2-3590-bdba-9fc340e39f11 | -3.32968 | -50.25024 | 2025-09-30 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96460e63-7685-356b-a411-04f5791dc26d | -6.70407 | -44.55264 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 11bac30a-4d8d-3805-bd12-dc4f8ad9bc58 | -5.98042 | -42.56342 | 2025-09-30 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d4663be2-b4b9-38fd-bff4-4ed7d44c3209 | -5.82918 | -43.87085 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e4bcfe9-2f77-3622-8d46-e54d2b81e36f | -6.43025 | -43.07597 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d0de395-0486-3ed8-a65b-0ac1b3e4aac7 | -3.50179 | -52.46498 | 2025-09-30 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 6c130962-1dcb-3c6f-9be8-b8bbcaca9aac | -6.0748 | -45.36027 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d36c309-fde7-384b-a1eb-9c9d39a902ff | -3.96106 | -49.44321 | 2025-09-30 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a71afedb-9dd7-35fb-95ad-51d20267d5b2 | -5.87013 | -45.77392 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91f6d127-5efe-30f2-86f0-da8fa7e3e36c | -0.64356 | -47.65308 | 2025-09-30 04:38:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 92f7036a-8b66-3945-be86-a5819d665aae | -6.89595 | -44.52276 | 2025-09-30 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a39be33-215a-30ce-9964-5f1b45c433f7 | -6.15069 | -42.78878 | 2025-09-30 04:38:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 499eac0e-2f84-35b3-a2d8-e3655855e318 | -5.83639 | -43.93734 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 77776cac-00fb-30c2-b82f-4a4c64ba2369 | -3.47643 | -49.96804 | 2025-09-30 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4394035f-8af6-32ab-9572-6f2caa6850c2 | -4.50733 | -40.72333 | 2025-09-30 04:38:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cb47e04d-6fff-3544-af6a-fa45559e1471 | -6.30451 | -43.81283 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f24e3ca8-71d2-3f8b-ae41-d3ff972aacd0 | -6.73595 | -45.63194 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c00a78d1-3586-399c-be79-080ecd103857 | -6.05427 | -43.60057 | 2025-09-30 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b213e85-7503-371e-8bc0-c797c96d7b52 | -5.67003 | -45.2944 | 2025-09-30 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4318ba6c-f37f-344e-ab69-6f331ac7a766 | -5.57342 | -44.84936 | 2025-09-30 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7e4c2adb-1f80-3867-a4bd-fb66b4eeb7ac | -2.5614 | -49.11977 | 2025-09-30 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae7473ac-46f8-3aeb-afd6-70fcf752a9d8 | -5.51721 | -43.87189 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8add04b8-38a5-3e91-a069-0dc71ad4fff1 | -2.4875 | -49.26714 | 2025-09-30 04:38:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d798d56-193f-30ba-976e-2048fa93f5d4 | -5.49965 | -43.43171 | 2025-09-30 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a9619d2-031d-3065-a682-3f5dee3debf2 | -7.04005 | -44.78295 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a109fa3d-cddd-3c28-a76c-952d6b28c598 | -6.27572 | -44.06575 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 011f9fa9-3501-30b6-a43b-8dd4dc7ed4b9 | -5.9089 | -43.71236 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 97a40219-6eb4-3f92-841d-ceab5f30e819 | -6.70761 | -44.55655 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dd699f9a-0e1e-3ded-832a-8d51a1601ac8 | -7.18569 | -41.69684 | 2025-09-30 04:38:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a101c10c-6596-3f1c-8ccd-27e5cdb067bf | -3.0976 | -47.014 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ecb42f82-b757-3bb9-aecf-c3342ee64820 | -5.71637 | -42.87501 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 87604bb0-2d36-3acd-bf3b-810068a364c9 | -6.30174 | -43.44131 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 65da54d6-5ab9-3392-8a14-2d0adc06e671 | -2.96351 | -49.01065 | 2025-09-30 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 49c435db-4fda-3790-b903-fbe53d7f431a | -5.03584 | -43.6105 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4a80d9a2-2991-3003-bbe4-e15b5f3f63c6 | -5.58415 | -48.96634 | 2025-09-30 04:38:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7d5df6ce-b3d2-32f5-a079-560404bc643e | -6.50451 | -44.11612 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e02e5c0-dbb5-33f5-befb-43e159ac1b1b | -6.46678 | -44.5832 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1a012c1-6b6b-38c6-a945-9aaa03c38160 | -6.07967 | -42.61612 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 8a4e55f5-47b3-3248-8e54-482d65f3ccc4 | -5.74446 | -42.67553 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| bf2866f2-7fc1-3e07-98cc-2d1e42a8db3a | -0.39507 | -52.04504 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e78e00a-3e3d-3a44-b546-88078ec66b7a | -5.84744 | -44.87146 | 2025-09-30 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 99cb91e7-86f4-35d6-a66e-e1fd5852d5f4 | -6.42965 | -43.07765 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c9d0aff5-b600-339d-84a6-a16696b4a00b | -5.4817 | -48.66028 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df71be51-d745-3e0b-b5b3-a283620b674a | -3.5058 | -53.45341 | 2025-09-30 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4005bdba-dec2-3cb4-9466-dd76d9fbe31f | -6.05485 | -43.65709 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b26e3c2-4ddd-38b2-b3cb-96cfd3324ae8 | -7.28685 | -42.86904 | 2025-09-30 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 085101ee-4125-38b2-8830-99d93e5a3c20 | -5.7029 | -45.46518 | 2025-09-30 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd0111d6-48a1-3a90-a8e5-4e5f8cdb61c6 | -5.52024 | -43.88005 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 079b6bd2-f936-3805-b4ca-5eaedbaad815 | -6.98715 | -42.80012 | 2025-09-30 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 120abb41-3430-3266-9be2-da70c7ec3258 | -5.76416 | -43.8376 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21c639ea-f2f2-35e1-8c10-67e87c50e157 | -6.80186 | -45.97396 | 2025-09-30 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57b3bcb7-c439-3e42-9a74-ab4fc098c3e7 | -6.30089 | -43.80825 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f6d1bbe7-c762-39ce-8fe3-c8ac519fea3d | -5.47839 | -48.65977 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d8f2aaa2-d085-364d-9d3b-b1d82ba7d378 | -3.49263 | -48.93634 | 2025-09-30 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 98590f2c-8dd8-3d80-b0bf-2a8f0f7e36c7 | -4.86932 | -45.05281 | 2025-09-30 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 75d122f3-439c-3fab-bb13-c157112dd389 | -5.33488 | -43.72677 | 2025-09-30 04:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d848707f-c637-3d7c-b882-8ee7c9be22a8 | -5.41014 | -37.70154 | 2025-09-30 04:38:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d1e2fdb5-dbf3-3100-aff8-9d8d4d8d53fe | -5.91898 | -43.91034 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3368fe4-5ba1-3579-927d-aa1053aa1fc8 | -5.50493 | -44.04034 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a4a3429-9c36-3232-a0d5-a431b31ea03e | -3.55224 | -50.32915 | 2025-09-30 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f8ca6ed-b0c4-38ae-a3dd-5c4c770f0f7c | -3.81116 | -47.5684 | 2025-09-30 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8d1dccde-67d0-317b-b8d4-0e741cce15bf | -6.25281 | -43.6327 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f37d62b4-6d4c-35e4-a7a1-c4df5f58345a | -4.91627 | -48.16206 | 2025-09-30 04:38:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README53.md)
