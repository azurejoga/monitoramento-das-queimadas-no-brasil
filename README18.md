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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 628bd8fa-2549-39ee-95ee-a1df14707f39 | -4.13006 | -47.65086 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3bde97a-d0b3-3b71-ba78-919a90d58ae6 | -4.66444 | -41.95657 | 2025-07-19 04:34:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c668e07e-3944-3421-ba62-c493ac823fbb | -5.66002 | -43.71815 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 16d32a9d-571a-3f7b-902a-9ea85552c491 | -8.05433 | -48.40776 | 2025-07-19 04:34:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dfc31d63-c5a5-3370-9f0b-d6075e35358c | -5.9169 | -43.46933 | 2025-07-19 04:34:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10880e8d-ccfd-3ba5-b47f-34e6475216c6 | -7.35114 | -45.31939 | 2025-07-19 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 940e5933-ca7a-3411-8c47-7765680b6662 | -6.68696 | -43.03349 | 2025-07-19 04:34:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 11a9da92-9cd6-3c88-826b-105b2fd9d6a3 | -7.71236 | -47.28831 | 2025-07-19 04:34:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0eb47ac4-e555-36ef-9647-d3775025c75a | -8.64468 | -47.75482 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5b53422c-8e42-3e48-9270-35017cbe48e4 | -7.06511 | -42.99019 | 2025-07-19 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2aad2f31-9960-390e-b941-30e37d3898a0 | -7.95041 | -43.94959 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7e41ebf-655c-383e-aebb-e3b3e581df46 | -5.64868 | -43.71635 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 48624384-4e8d-3924-becc-8305eb3f8f9c | -6.67877 | -43.76379 | 2025-07-19 04:34:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4c91ea1-14d8-30a5-a060-c47fb41bada9 | -7.08846 | -49.17985 | 2025-07-19 04:34:00 | NPP-375D | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 879647c8-5fde-3c57-b2aa-0612f3e05b67 | -7.17491 | -44.09914 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8e23aeba-abe1-32e6-b50a-8a367d601853 | -3.13453 | -47.01 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 8f362462-d339-31e8-bc80-0aacc8ce9d3b | -8.88374 | -50.16048 | 2025-07-19 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dbcd70fc-e773-36a2-8e0c-a9b624952f38 | -7.27725 | -50.33006 | 2025-07-19 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc5372bd-c6ea-305d-8079-7cafff5c44b0 | -3.39552 | -47.47818 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8fcbf3bc-7d26-3a22-809b-05da7cccf512 | -7.12906 | -43.28999 | 2025-07-19 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2019e42-8dfc-3a4a-a611-e9b7bd3c9967 | -6.43901 | -45.32726 | 2025-07-19 04:34:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e760469-7683-35e2-bb51-aafc3293ecbf | -8.0729 | -50.076 | 2025-07-19 04:34:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15a36a82-000f-336f-9e14-42072889972e | -8.01448 | -43.66972 | 2025-07-19 04:34:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78c00ac2-86c6-3c9e-bbea-110b0e585e7d | -3.39165 | -47.48111 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e81126a-9af4-34b2-8038-258754d45b87 | -8.07095 | -50.10994 | 2025-07-19 04:34:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79b34d97-f7cd-3f29-a674-32eb4585ad56 | -4.10303 | -48.20248 | 2025-07-19 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21004463-6777-34ec-9fe8-2736d9d830c7 | -4.82232 | -47.31732 | 2025-07-19 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ef35b1b-415d-3bda-926f-dd0baaf0fef2 | -2.74618 | -48.25033 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1cd637cd-c383-377d-9cde-efe3b88bb185 | -8.05101 | -48.40723 | 2025-07-19 04:34:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c9491803-e213-3c32-a4a2-f5a89f8baf84 | -3.59134 | -47.52351 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a5121ff-cd4f-3bdf-b16b-0b77fa8cd89a | -8.53179 | -47.84828 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db331c6c-f3df-3a45-abd6-cba70045ae89 | -2.90925 | -48.23963 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2dc9097e-5a14-3ce7-87f3-d1cb91dc5380 | -8.33378 | -50.49373 | 2025-07-19 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d175246d-aeee-308d-af56-c0e47de6797b | -8.05013 | -42.15577 | 2025-07-19 04:34:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 22aa4234-f1e9-3fbe-982e-7f41305f7304 | -8.54896 | -47.84742 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f41556ac-bb5c-3ae1-8349-1fff9196e4fc | -7.09973 | -49.93311 | 2025-07-19 04:34:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f2c9c57-de84-3628-966a-0eb6bf42016a | -4.25082 | -48.54821 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 50da7e48-9b9c-3e09-966a-130c3cd9b579 | -8.0723 | -50.07969 | 2025-07-19 04:34:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8921cc30-b23e-393a-b7db-cad2abf7b3fd | -4.87398 | -47.76063 | 2025-07-19 04:34:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92446988-9bdc-33f6-b4bc-73b11f7ed5d0 | -7.17441 | -44.10148 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3295d0f1-6b55-391e-9c54-b2f2e270b669 | -3.61382 | -43.53978 | 2025-07-19 04:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 392754bd-5183-37b5-b826-a244f1a94985 | -5.65624 | -43.71756 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6df2ddb2-e016-35a6-ad9d-c7f6baf7c99e | -6.97286 | -42.80151 | 2025-07-19 04:34:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4685817c-44cc-3806-a13e-637ebeb9610c | -6.1709 | -48.05483 | 2025-07-19 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 046b6217-ad93-3e15-930c-86cda6408d91 | -4.59266 | -47.27094 | 2025-07-19 04:34:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b42bc762-4c23-3e69-af0c-db492b5f13fe | -3.04561 | -49.42086 | 2025-07-19 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eac4d3e8-63dd-36c8-8ac7-bd9f166fc5dd | -7.22744 | -44.13497 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2dd90f6-09eb-3244-8ec6-4c4f71072b2e | -3.3922 | -47.47766 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4bca5a4e-ccb0-3308-827f-c20ca7d048b3 | -6.95296 | -50.46207 | 2025-07-19 04:34:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 655f49ed-d33c-331e-a871-de157880c509 | -2.90868 | -48.24318 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| eaf4c232-d837-3e30-a25e-647dd2b875f8 | -5.74977 | -46.19094 | 2025-07-19 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7cd90a3c-4469-309d-8708-2087a93c241a | -3.58723 | -48.93942 | 2025-07-19 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de3aa895-92dc-3525-bda7-8e3f436b28f0 | -6.91458 | -44.82995 | 2025-07-19 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d3ec6b11-841a-30f2-948b-8d18365758c1 | -5.64936 | -43.71178 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8e4d4862-37b4-34d1-8ae5-a549f4717dea | -6.9182 | -44.83051 | 2025-07-19 04:34:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d69a580d-e80f-3e6a-b860-46719fb90917 | -3.06025 | -40.04618 | 2025-07-19 04:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4be0c6a0-ca04-3ca4-a092-cf08394c8de6 | -3.82764 | -47.74111 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 99892386-2d7e-3654-bc60-b3e3be3d9197 | -3.13731 | -47.01397 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 21f05b95-58bc-3c72-b02b-2a910e51c547 | -8.54563 | -47.84689 | 2025-07-19 04:34:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 331758ba-4e17-3a7e-b5b5-19580e59bf32 | -7.95078 | -43.93806 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44f5be76-dc10-386c-ba17-232644e75f3a | -7.95878 | -43.94605 | 2025-07-19 04:34:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37e1e781-816a-30eb-90b8-543ebc89b7ef | -6.78601 | -58.63372 | 2025-07-19 04:34:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de0d8ab2-9031-3e40-90d2-e4bd2d0202bb | -3.40392 | -43.36829 | 2025-07-19 04:34:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e21dbab9-c6cb-383a-9825-28b1f69252b0 | -3.1618 | -41.83647 | 2025-07-19 04:34:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b23a10d-e325-37c5-908d-93b05f42997d | -7.70568 | -47.28728 | 2025-07-19 04:34:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7cae56a-4e93-3708-b4db-8f27d17e7660 | -5.65246 | -43.71696 | 2025-07-19 04:34:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| e5b05ff3-e0c2-37ca-9f9c-167f0568ac4e | -6.16149 | -48.04979 | 2025-07-19 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8577459b-a8ec-3495-87f0-e1d430efd185 | -9.00644 | -48.72086 | 2025-07-19 04:34:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccd87de4-d786-3044-83cd-9b0727f30bad | -3.51068 | -47.22068 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2d346b30-71b6-3a59-b472-1c667cbc47d9 | -9.24131 | -48.56211 | 2025-07-19 04:34:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 426676e9-fa9a-38ab-9346-69906d2f55c8 | -3.13122 | -47.00948 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 28940476-0827-38d8-8cad-afbefb38fd90 | -6.16318 | -43.75394 | 2025-07-19 04:34:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8ea6a6e-bfe8-35ed-93ac-3b2f661514ba | -7.35468 | -45.31995 | 2025-07-19 04:34:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64354bfd-9a1b-304b-a059-079446e9520e | -6.17695 | -45.86517 | 2025-07-19 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bdeb8ac-1336-3564-9a67-51eaa3ce9252 | -7.18266 | -44.09801 | 2025-07-19 04:34:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0d373dd5-7af5-3611-9778-04c24bf46860 | -8.88434 | -50.15677 | 2025-07-19 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3a4b82b4-491a-3444-84a3-74812fc45505 | -6.16426 | -48.05378 | 2025-07-19 04:34:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 427e5929-e1ba-3d15-8ead-10dcb1aa1897 | -7.70847 | -47.29131 | 2025-07-19 04:34:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2edebda7-233f-33fd-a145-68a40ecf5def | -4.31042 | -48.11008 | 2025-07-19 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| f978a74f-1015-36ba-81d0-fe3d4a7186cb | -3.11409 | -47.01034 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9ab4167-ed3b-315e-a8db-b4d23d3ebcbb | -3.35582 | -51.60004 | 2025-07-19 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ae118a7-283a-3744-9af3-9354e263c7e1 | -3.58265 | -48.94622 | 2025-07-19 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9db5843a-3d40-32ca-9365-b3b0ddc4bcba | -5.74638 | -46.19044 | 2025-07-19 04:34:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb016323-b5b8-3240-94f8-38dff44f0a87 | -3.5908 | -47.52697 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 409e7a15-1f6b-31b4-be6d-5a98b7248409 | -3.98065 | -48.42194 | 2025-07-19 04:34:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53059da8-cc31-3129-af67-6f9cfbf63898 | -2.91877 | -48.24476 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15d7d602-7811-3468-8a2d-6fb7f40ed282 | -7.1123 | -44.38446 | 2025-07-19 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5f99ff98-88da-32b6-8884-5a8e26472193 | -4.67336 | -41.95404 | 2025-07-19 04:34:00 | NPP-375D | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dce14617-8e9e-3d2f-be92-bfc90da34e34 | -7.17584 | -44.09212 | 2025-07-19 04:34:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61cc38a0-6bb6-386b-ac21-8de42c2a18cf | -7.42116 | -43.87224 | 2025-07-19 04:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c51854dc-9ea0-3d98-b6ed-604a254edfc6 | -3.12404 | -47.01189 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 74ddbc3e-12d4-3b7e-bdf7-f385e99462fc | -3.61315 | -43.54423 | 2025-07-19 04:34:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3df55b81-6c86-360c-8086-fd4749b2e4b8 | -6.97233 | -42.80515 | 2025-07-19 04:34:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d5ad6794-4648-3364-9933-17199fc91bfd | -3.51013 | -47.22412 | 2025-07-19 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10884382-8e0a-3167-925b-839bae8fb7ca | -6.87244 | -42.75021 | 2025-07-19 04:34:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 822d12f5-ec2d-3e0b-876d-353ea3e4872a | -5.28045 | -45.12662 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc852b8d-872e-38ea-82ab-189cdf46ee74 | -3.12072 | -47.01138 | 2025-07-19 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c4711e7a-e24a-3d66-a89b-1fcdc370ab6b | -7.07019 | -42.9837 | 2025-07-19 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| db6ffe78-b8a6-31f3-b909-b08e210f168b | -2.91597 | -48.24068 | 2025-07-19 04:34:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3c89daf9-7781-37d1-8aed-f8112d88f863 | -7.49035 | -47.49828 | 2025-07-19 04:34:00 | NPP-375D | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README19.md)
