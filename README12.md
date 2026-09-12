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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8c149ba-93c9-3dbc-bfd6-c4a63011c74d | -6.327 | -43.36204 | 2026-09-12 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a4f9ab09-fc40-3aba-9a56-180a1bd0ef1f | -5.76227 | -45.09223 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 22f8946b-99fd-3a7b-befb-cd3fe8380d6a | -6.8247 | -38.44903 | 2026-09-12 03:47:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5630de81-5b53-358c-a273-44fa3decdc3d | -5.12294 | -41.08246 | 2026-09-12 03:47:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 28ea211f-e5c0-32ad-85a4-90cec00f311d | -7.42181 | -46.15931 | 2026-09-12 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 363a12b5-3aba-3672-a679-af6bc32d9dda | -5.76649 | -45.1008 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| ecc7ff16-9c77-338e-86d3-97b255d3ba14 | -7.46316 | -42.11999 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 61377b83-780d-34d4-942c-8ce340650627 | -7.4219 | -44.56582 | 2026-09-12 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2addd4f-6736-3551-add9-58605a769ecb | -7.30851 | -45.99348 | 2026-09-12 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2fcfe74-ce87-3bb1-8eb8-734bb123f062 | -6.28879 | -41.69609 | 2026-09-12 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5597e5a-311a-32cd-95e9-85b78c31068b | -6.61123 | -44.20648 | 2026-09-12 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c152588c-9d18-3a8a-86f8-1968d2d439e5 | -7.4661 | -42.12179 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 44f79a76-001d-31ed-b997-8e68eeaf092a | -7.44318 | -42.13003 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5014bb58-f882-373f-9cfb-1a604dfa4fe7 | -5.76579 | -45.10468 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 59671c79-4ab6-344e-9588-d0434d5eb2e6 | -7.19075 | -41.31507 | 2026-09-12 03:47:00 | NOAA-20 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd1985f0-7c21-3307-b18e-67655cceb563 | -6.50264 | -47.60299 | 2026-09-12 03:47:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61693a16-9e37-3f13-8a74-f2de95a8dc70 | -7.41602 | -46.15815 | 2026-09-12 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6e555d67-207e-3f4b-99ef-9cc3cf21a8d5 | -6.72151 | -45.43682 | 2026-09-12 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6704f2e9-0850-3a11-b110-4b3c05097156 | -7.271 | -46.80293 | 2026-09-12 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 08935956-6166-3a72-b305-2e2b72827c67 | -6.95475 | -44.55111 | 2026-09-12 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 8bd2848b-bc74-31bb-9892-85f2e0320c50 | -7.17257 | -45.88816 | 2026-09-12 03:47:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dae610b-1336-3e8b-8409-80a52fc21ed0 | -5.54804 | -43.43316 | 2026-09-12 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5f04afe-eda7-3509-8f44-1aca570aabc3 | -5.60739 | -44.84906 | 2026-09-12 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 78f4799c-e120-3363-881a-2a9674c23781 | -8.72018 | -38.69036 | 2026-09-12 03:47:00 | NOAA-20 | ITACURUBA | PERNAMBUCO | Brasil | 2607406 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| deed8091-a634-3adc-b509-bab12504f1f1 | -6.72715 | -45.43768 | 2026-09-12 03:47:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9da39ba2-4204-3c75-9cc5-48a13e701527 | -7.18453 | -45.9203 | 2026-09-12 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e29acfdb-e060-3e97-a701-629e49bae621 | -4.36048 | -47.78125 | 2026-09-12 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.5 |
| d858e639-3221-32bc-80eb-8b831abda6d7 | -4.8321 | -46.78603 | 2026-09-12 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf73ddd2-cd98-3223-b2cb-5410f749800f | -8.92204 | -37.31886 | 2026-09-12 03:47:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5ffd140d-cac3-3c8c-bb25-46b59d8e0c75 | -7.18383 | -45.92417 | 2026-09-12 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9b6e15b0-bb26-3099-9133-d94cc7815500 | -6.95588 | -44.54488 | 2026-09-12 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| cec206ea-c1ff-3ad2-b7a7-f6ff7546c45d | -5.54854 | -43.43025 | 2026-09-12 03:47:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc29978d-7ee2-3c15-bb0a-2a18e17cdf90 | -7.41678 | -46.15407 | 2026-09-12 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c078e820-924b-3219-b397-11e6a110af8a | -7.19463 | -45.9301 | 2026-09-12 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 655afff8-02fe-35b2-bbf8-79c68012fd4e | -5.76787 | -45.09306 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 0adae540-5671-34e6-8c24-6ef6200dc86f | -7.2698 | -46.80537 | 2026-09-12 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 9aafc3b9-4835-3f66-8141-96500e9426b9 | -5.75596 | -45.09535 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9ae8f688-3cb9-3d3d-86df-d37a440a031e | -7.2762 | -46.80861 | 2026-09-12 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3072c3e1-4260-38b3-988c-8899b1da20b3 | -5.60802 | -44.84551 | 2026-09-12 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f606a33d-06cb-329b-a826-ec0e7482a77d | -7.45428 | -42.1185 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 372b28b7-403f-300b-9aad-c59a32dce1c6 | -7.42332 | -46.15115 | 2026-09-12 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d2a9212-be34-3f4d-a8ab-9e50d62267a3 | -5.77278 | -45.09777 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 5cf3f38c-a386-3a0d-8dc8-3ae2dadbcfc6 | -7.18956 | -45.92531 | 2026-09-12 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 626f01c1-3fed-3569-af23-93c2bb0220d8 | -7.18887 | -45.92913 | 2026-09-12 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| afa9e5f1-5967-3075-a87e-7843d7a3cd82 | -5.76718 | -45.09692 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| fa61c760-2d14-3761-8ee0-53a1db1a1738 | -4.92324 | -47.54247 | 2026-09-12 03:47:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3d0a843b-42f0-37ca-a51e-d1edd6791fb8 | -5.77346 | -45.09394 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 67900f75-f993-3b3e-bfe6-d1a7a88fc8fc | -6.95997 | -44.55236 | 2026-09-12 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa844f04-7563-3599-8756-74f30c69d0a9 | -6.5207 | -47.6151 | 2026-09-12 03:47:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 624b3837-73b4-3ec2-b668-33da72b7fa5b | -7.27014 | -46.80747 | 2026-09-12 03:47:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9810c146-9966-32d0-aad5-2439eb20b755 | -6.96055 | -44.54912 | 2026-09-12 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d17f6631-3d68-3164-8300-8624ca8e0b90 | -7.11711 | -42.10894 | 2026-09-12 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b3dc172-b003-3275-a481-2a6e9616bf5f | -7.42717 | -44.56653 | 2026-09-12 03:47:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a246a6a-5e10-3549-8cdd-f5734f351ec9 | -5.7575 | -45.09517 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 4ef32a81-f6a4-3413-97c4-d17795441a5c | -4.28001 | -46.53295 | 2026-09-12 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cd6d4156-22bf-3a1d-b75a-94189ec3859a | -5.76178 | -45.10373 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bc82b7b-eed6-3cd2-86d2-cf6f3a5de1aa | -7.41527 | -46.16221 | 2026-09-12 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe550766-20b2-3f40-b2af-d092a09ae8c2 | -6.61065 | -44.20978 | 2026-09-12 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4057b834-433d-33ff-9600-6126b2543325 | -7.45278 | -42.1196 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e02ad584-7dca-3a24-aeff-04cc09ec0fad | -6.32206 | -43.3613 | 2026-09-12 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 35ce3d71-9fbd-3578-88b3-134c1c9de5f1 | -6.95531 | -44.54802 | 2026-09-12 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4b7f9da6-0e9d-3220-a91e-702912cad007 | -7.45872 | -42.11925 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 757741e7-c11c-3318-9125-dee0e362e9c3 | -7.20607 | -43.69326 | 2026-09-12 03:47:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| abedc2fd-6940-344e-9c2d-885505d3779f | -5.76245 | -45.09984 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 55e1e2f1-0c26-369f-bad0-29e3daa7dbf2 | -6.96114 | -44.54586 | 2026-09-12 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d86157f5-5f97-341e-a083-a11e3a0aeb73 | -5.76856 | -45.08921 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 36.5 |
| f4c8e1c9-d386-34ea-873b-cfaf05e645f6 | -6.95645 | -44.54172 | 2026-09-12 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fe21e6b9-ca6f-376b-b483-e057995a05b7 | -9.12136 | -35.49975 | 2026-09-12 03:47:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8c29966c-d290-3c6a-845e-2582c4758fca | -5.76088 | -45.09998 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 94149bfb-2422-3cbb-8d2e-fda4699a6e2e | -6.51425 | -47.61395 | 2026-09-12 03:47:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e9c81a3-02a5-3fe8-8f13-6eb7ec35e04b | -7.45799 | -42.11599 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1f179e08-a23a-37e9-94b4-4a564b8bedc9 | -7.4676 | -42.12071 | 2026-09-12 03:47:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f3fb19ad-788b-33b0-9738-34fc652f5516 | -3.54437 | -48.18318 | 2026-09-12 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4df15c03-a6db-3830-bfb7-ff4681cf9661 | -4.27279 | -46.53739 | 2026-09-12 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcd88013-9924-3e51-9e38-df13edfa0034 | -8.91016 | -37.36161 | 2026-09-12 03:47:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b15127ec-a1cb-3c3d-937b-78b95714e642 | -6.28439 | -41.69539 | 2026-09-12 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6c88033a-ca95-355d-a4ec-cf4114b901f7 | -6.61643 | -44.2073 | 2026-09-12 03:47:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5bee2f4d-cbb5-34ad-ab21-dee391f3c543 | -6.29319 | -41.69683 | 2026-09-12 03:47:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 285d9152-3a60-3204-9d43-6cc5725d1ea9 | -5.76378 | -45.09207 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 0f16c86e-694f-3f15-bae4-6b08e049f76f | -5.76444 | -45.08822 | 2026-09-12 03:47:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 3f997059-78ac-3def-b784-025fe9c368fd | -5.61353 | -44.84638 | 2026-09-12 03:47:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5c4f0c64-06ba-3392-a1be-b093c49045a0 | -7.42257 | -46.15522 | 2026-09-12 03:47:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2c82addd-c401-398c-a2dc-ff80c97267d6 | -4.82946 | -46.78275 | 2026-09-12 03:47:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 74ec228e-b92b-31b1-b1e9-613f6d57968f | -7.17751 | -45.89362 | 2026-09-12 03:47:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0ab3466-c794-31af-8e82-ccd6177db189 | -6.86191 | -47.43835 | 2026-09-12 03:47:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea412587-7ca9-3708-9333-d61d85b3e789 | -5.12789 | -42.88179 | 2026-09-12 03:47:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15e23b68-b4a4-3df4-9544-fb5bd23514f1 | -7.18313 | -45.92804 | 2026-09-12 03:47:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5f56dfd-e74c-38c9-9b4a-59994922e923 | -6.81151 | -42.95088 | 2026-09-12 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a9165952-6f39-3263-99d3-36fb49aa2582 | -3.53738 | -48.1821 | 2026-09-12 03:47:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a8e70be-13ce-3801-bf64-60afcc2c1ce6 | -6.37406 | -39.24952 | 2026-09-12 03:47:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8979d27d-b0bf-33df-8f04-b566fde82101 | -7.12232 | -42.10527 | 2026-09-12 03:47:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f894bb74-051b-368b-9ab5-6a0ef0daa33e | -13.45657 | -48.50546 | 2026-09-12 03:49:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c21919e4-3f44-37a2-8567-6bc0905c053d | -14.38811 | -43.78568 | 2026-09-12 03:49:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04699559-cb67-3639-afaa-101587a5d6c3 | -14.00993 | -42.14388 | 2026-09-12 03:49:00 | NOAA-20 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 26d4ea18-a2a7-3ad6-a5fd-3175728c87a8 | -13.65398 | -43.92482 | 2026-09-12 03:49:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4281403f-48e5-33f1-8999-f531480ed2d5 | -9.78502 | -42.00332 | 2026-09-12 03:49:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b41ac486-474b-3552-a078-a9dec3167f24 | -3.22481 | -46.95905 | 2026-09-12 03:49:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 56777ab5-9a12-3ab1-a0ed-3c3cb8f3f57c | -12.12807 | -48.96216 | 2026-09-12 03:49:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 442a0483-dffa-3e63-bb06-c704138987f4 | -9.63963 | -49.67891 | 2026-09-12 03:49:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dae73a35-1eb2-3b0b-a6e2-56daa78f2855 | -7.60191 | -46.12379 | 2026-09-12 03:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README13.md)
