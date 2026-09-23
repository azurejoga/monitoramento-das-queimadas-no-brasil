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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fea78215-b2e8-38a6-b8b6-fd0e7e052ad5 | -8.65826 | -50.11789 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 140bcc31-f757-3c6d-89de-35661ba3724c | -5.85448 | -52.02657 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 110de404-4658-3b6f-a88b-89a3c5b4507b | -8.33335 | -50.82449 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f2aa5c9-3d71-3bba-a841-e5d21936889a | -6.77859 | -48.66483 | 2026-09-23 05:04:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dc92698b-742f-3258-90b2-5d9488246906 | -6.10339 | -57.67677 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6be3fe61-048f-32eb-9037-3408d9a487d7 | -6.55061 | -56.03603 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d50ce1b7-5c25-3090-92e3-454360b96073 | -5.77562 | -43.76653 | 2026-09-23 05:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 822c1420-88a3-301f-964e-20164906f3cd | -6.66542 | -58.5662 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21d34aa7-2656-3920-a4f0-e50353080455 | -8.79591 | -48.76051 | 2026-09-23 05:04:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fc3fd57f-f115-3a8f-9391-5a00c22ee26a | -10.26518 | -50.24021 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b9924b7f-d836-3668-ad09-7ae9599b6c42 | -6.61595 | -43.74515 | 2026-09-23 05:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| afbd1474-3c93-3116-9cbb-ecc39679651c | -5.80852 | -52.07989 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de3e1a7c-4158-352e-a431-61782b6cb651 | -6.29978 | -57.74409 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 98b43a22-8173-3206-b444-eb71e7fef0ae | -6.8928 | -43.75352 | 2026-09-23 05:04:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 77c69e8b-5cd1-39ef-a4c9-a63344b62a02 | -4.51415 | -54.97853 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a847308f-e8b0-313f-a533-776189a6859c | -4.27077 | -55.4467 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2f7176b-23f6-3b28-851a-7cdd9d8a5c64 | -3.60954 | -60.56371 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3fc59ef-8918-3d30-924b-5552395da779 | -6.13163 | -59.97001 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53781142-8ea5-3fff-bc15-18350f31da23 | -5.61974 | -45.2508 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8e1edf4f-7366-3aa5-beea-ad785c8a6e4d | -5.76461 | -52.35746 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1491b69b-e2d1-3950-b76f-e8a32f3cce9a | -3.77452 | -60.73285 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bff507e8-0272-3dee-afd4-228d5eb92d33 | -5.88866 | -52.28114 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6d14135-04dc-3aef-ac82-d989120b67f1 | -8.48904 | -57.61192 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 50af266d-ec47-338f-98d1-940c92a0135c | -3.68347 | -60.5739 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4984bd14-33ad-3e2c-b0f2-e17da77aba12 | -6.6982 | -58.92319 | 2026-09-23 05:04:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0504afc3-d737-3d8d-8480-ea9aed24a374 | -5.59961 | -45.37085 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 753360c2-fbf8-3670-bab9-2dc415953e34 | -3.1424 | -60.63101 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60ed1a2c-8c3f-3309-9dfd-2fa8c26b64e6 | -5.1774 | -56.17747 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e93c317-492d-37e8-b03b-8de2baa72fba | -10.70213 | -48.70312 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2a281a81-3085-39df-98a8-5d426950e62c | -5.28316 | -47.25694 | 2026-09-23 05:04:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fbda9e92-8b98-373f-bce4-3f539d6866c9 | -6.44798 | -54.9981 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45845827-e8f5-3b2d-bcc8-cef111f08f52 | -6.29917 | -57.7477 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7055d9ff-8e53-3250-a3f5-ce573d75e398 | -8.12091 | -44.42918 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f905eaa-514c-30a0-bfa4-95f85e4f7fef | -10.2753 | -49.97405 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 10503d1a-126b-39c2-a738-55fe4f92c7c6 | -8.91514 | -45.92337 | 2026-09-23 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57724305-43e3-383f-a2fc-9c1801b217f9 | -7.56982 | -57.68749 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c130fbdf-9eed-359e-b8c4-3eddece43172 | -7.87812 | -61.18208 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1ec4abf8-7e62-3ab4-be34-fa648b5f8014 | -10.26136 | -50.24135 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fd8af409-126b-3bad-833c-a06ccb258b2b | -9.04048 | -65.4136 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39678af4-c378-3747-b4ef-62fa34f405b3 | -11.47822 | -47.34864 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6da56733-891b-3a9e-a26b-6ef1e06ebfe5 | -12.18878 | -47.01423 | 2026-09-23 05:04:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 263bdf0d-fcb8-34e4-a06f-2b1ee2473ed2 | -6.61617 | -59.91242 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cab6df6f-35c0-32d1-add8-a34532c0437a | -9.16364 | -51.53331 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ac2cfc9-9f3f-3f13-84b4-c8a41fe335d2 | -6.32273 | -43.93489 | 2026-09-23 05:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b037e43d-07ba-33b1-8e1c-fb8e1ed90eb4 | -7.41391 | -44.72724 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7e8db846-239b-3e18-8fe6-2f7f65b94d3b | -3.11308 | -61.08812 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 109f483b-40f1-32f3-a383-269315ca91ca | -8.8073 | -44.28046 | 2026-09-23 05:04:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11a920cb-dd59-3029-8573-ced792dbb9a0 | -3.8624 | -58.82259 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4274b7b0-21b0-3473-9395-3d9bf36c9071 | -6.68402 | -55.05452 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2fddaa76-0fea-3475-8f35-1a9f93526f85 | -5.56715 | -56.1829 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ac2ce6a-5fc2-325b-944d-1587365fa442 | -6.66682 | -58.55811 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 582740b0-e423-353b-9689-1b22d068865c | -10.91274 | -53.93764 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c953130-8954-3b63-bc6f-38e72b1f1e11 | -3.19589 | -60.43597 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e89baad-18ad-3ff1-a701-aad99132f8e0 | -11.78439 | -50.98371 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bd9de256-8eb8-37bf-83a7-500040c6aceb | -9.58364 | -46.5334 | 2026-09-23 05:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 754ef867-7865-3daa-a751-78c91ec2ffd4 | -10.71793 | -48.71743 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50bbb6e6-6261-390d-b55b-fa8211fadd34 | -6.6889 | -58.45564 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 376707f4-ba9c-369b-8f44-ff638c5bd884 | -3.774 | -60.73599 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2e42d8b-f194-3d1e-b18f-7dc11399db56 | -8.74115 | -52.36215 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd94858f-2f49-39f6-b9ab-3296cebd1b8f | -10.53777 | -43.97997 | 2026-09-23 05:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eedf6a12-9f46-3106-985b-3feb6b47c973 | -7.08425 | -61.08561 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d09438b9-943b-35e4-9931-5af5064851c5 | -6.89172 | -42.92033 | 2026-09-23 05:04:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 27a6532d-c3be-3b7e-9828-12ce33386631 | -4.28018 | -55.43513 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 876eaaee-24e9-3bb1-98e6-967a3ffe45ec | -7.419 | -44.72875 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 031f3fd3-f035-3e66-abb3-9e50cff50242 | -8.25997 | -45.4335 | 2026-09-23 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f03d37f-b247-3d02-9dd3-91bf59d98ac7 | -8.61529 | -54.62212 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 692e2376-3475-3752-8777-8d3f69cbf65c | -8.4671 | -48.69059 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7b864b7a-2dc8-395e-9ab6-fc080949c277 | -4.15049 | -50.45831 | 2026-09-23 05:04:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b9208025-f6c6-3b8a-8b06-7e0a3d364f95 | -8.25829 | -45.43439 | 2026-09-23 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0033c38f-41bc-3a6e-a2ad-b35b67246a0a | -7.3144 | -55.22089 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c73c4f0e-1fae-3363-b952-45e22be7e55c | -6.67757 | -58.57244 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6cf39f06-5d38-3cbc-ab90-b6c6c40e155e | -5.45481 | -60.14771 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96cf4c6f-e3d6-3f09-bc86-67b1d1e1a094 | -9.9689 | -50.25685 | 2026-09-23 05:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 568b6c4f-57db-3644-b617-161898215a4f | -6.57986 | -44.15152 | 2026-09-23 05:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d7c9ef97-1afe-3ba5-b2e2-1b133d305a7e | -5.24812 | -59.98229 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0fbf9d9-ffb5-3e10-9efc-442963533e88 | -6.4547 | -59.96988 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4b8bec71-0586-385b-b5d4-aa0703fb2b46 | -8.17426 | -54.79745 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4174b97d-e748-3b6d-b530-295b083ed8cb | -10.9053 | -51.5205 | 2026-09-23 05:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cebb7c18-2c6e-3fae-9d22-c7e4a79afb86 | -3.78734 | -60.7536 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c18edd40-7ade-3654-8f1d-a80b416c5e7b | -10.96145 | -50.60846 | 2026-09-23 05:04:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e898907c-d968-3aa8-9ebc-fc15babd9d87 | -4.15848 | -60.7764 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c7686f61-323d-3572-870d-bdbaea19b28b | -7.40331 | -44.73161 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 37585133-99d8-39a8-8a59-52db20c6936a | -11.28852 | -51.37063 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9f1b4045-ab42-3a1e-b01a-762c928c6db7 | -5.21593 | -60.05291 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b5afdfe-007b-30ce-9042-aa9c374768e1 | -12.12911 | -47.38683 | 2026-09-23 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50b2f37d-2e9a-3ec4-a06d-3317a45f2b8f | -3.39425 | -61.05416 | 2026-09-23 05:04:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4fb7026-ab31-3afd-9ec6-bd9e62f58ae6 | -6.08612 | -57.63017 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5bebc137-98d9-3a0c-83ac-66ead97793b1 | -9.70158 | -58.13924 | 2026-09-23 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19eb8d70-781e-3085-af55-cd18cab06845 | -10.69047 | -48.72697 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93ca7775-54c0-3d3d-abe9-554db813f15f | -4.55918 | -54.91913 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77053c0e-f815-3150-a5c5-d001517a3d12 | -3.86898 | -52.25992 | 2026-09-23 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66da8487-ff10-30d2-a796-b6e21ba79164 | -10.91494 | -53.94523 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5004af8e-c08a-3d73-9e37-6dbc4f5a6662 | -6.67041 | -58.56281 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc7d0eec-cc76-3ed2-9b0b-d564efde3665 | -11.40543 | -44.05417 | 2026-09-23 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c55a2b16-35c2-3cef-9df0-2da5f7e91509 | -5.85393 | -52.03005 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b6ecf20-03e8-3e41-a173-42152c78334b | -7.08371 | -61.08858 | 2026-09-23 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9971c7b2-ef94-3eb6-87de-a8120e0e6a7c | -6.17934 | -52.79689 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d9de49e-b5e2-34fd-8075-f00cd1077622 | -5.86881 | -51.93591 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4f51d3e-f192-3334-8bce-99aabbbb8c8d | -9.87007 | -48.39654 | 2026-09-23 05:04:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ba703184-8499-3686-b53b-3f3aaff6ee0b | -4.1307 | -54.24818 | 2026-09-23 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README89.md)
