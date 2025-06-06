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
| 992ffdb4-9f26-3a12-8c8f-889fafda328b | -7.55238 | -45.82745 | 2025-06-06 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e279f06-3439-3be1-9ee8-1b61a9e03522 | -6.28634 | -44.21643 | 2025-06-06 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56536a00-1b83-3a2d-9cdb-85b1994700d0 | -6.19751 | -48.56723 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c92e668c-79c0-358d-99a8-9300732a8852 | -7.90717 | -50.36379 | 2025-06-06 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c74d96a-ae54-3c52-be0e-8d63025e78b4 | -7.01376 | -44.61198 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ace7ac42-90b7-32ac-bcd6-6f6ef67cbec0 | -6.23543 | -48.56604 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5a356aa7-112a-361a-af3b-a4c85fbcd518 | -6.05292 | -44.16932 | 2025-06-06 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7a26ea9-ceaf-3e9b-be73-02b58bf5e836 | -4.42179 | -47.66425 | 2025-06-06 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba860165-650b-3476-b2a2-532e1c8fcb23 | -8.83901 | -49.83963 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7061b3fd-fc0a-3990-b889-2b97ef099eb8 | -6.23598 | -48.56253 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9003dabb-9184-3e8b-b2f1-3e1f0f2acfe3 | -5.4167 | -47.56937 | 2025-06-06 04:40:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ddab2fbd-06d2-30f3-9088-87d3fe5f8be5 | -7.49971 | -43.31259 | 2025-06-06 04:40:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0850e453-83cc-312e-b236-6b991d377a05 | -8.66959 | -44.26727 | 2025-06-06 04:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6af1d6c2-5ca8-3bfb-b342-1d2e38d2ea48 | -7.71954 | -44.15564 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65b199b8-e604-3acd-a44d-4abe53fa4536 | -7.90328 | -50.36676 | 2025-06-06 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 57b60186-37a9-321f-b82f-22a7c70b4fa2 | -6.12288 | -46.82323 | 2025-06-06 04:40:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6376bf74-6525-35d9-9fc4-43c3a2efefd3 | -6.21396 | -55.65305 | 2025-06-06 04:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 791bd71d-f728-392a-90a9-a0778be441ec | -6.21381 | -55.65211 | 2025-06-06 04:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ea6518a9-0f90-3952-90cc-9811fed1ead0 | -3.13815 | -41.79136 | 2025-06-06 04:40:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cb5f5c75-1e4a-3833-85cf-753cfb0244b4 | -7.02395 | -44.59876 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c33bd15-0ad9-3926-a376-7588e400a5af | -6.66488 | -51.96243 | 2025-06-06 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e521c235-2a58-3976-b79b-971181ae9c43 | -6.19136 | -48.56268 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 199efa27-db5e-38fd-a7a7-cd0c5bc1f807 | -7.721 | -44.17569 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 07f5c438-b8a9-37a6-9374-37b5827455c3 | -7.0153 | -44.6013 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d038ac5e-4f5d-3976-becb-80b559a4a708 | -7.01987 | -44.59833 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fdefdc1d-e9b4-325b-b418-e37053bce992 | -7.00621 | -44.60692 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b06230ed-09eb-3896-a6b3-0debd78adc5c | -7.28643 | -49.27957 | 2025-06-06 04:40:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6008fb1c-cb73-337a-8915-8d6224752808 | -6.12237 | -46.82186 | 2025-06-06 04:40:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 452e9614-3ffd-341c-aa27-7cbee08e4dc3 | -8.67015 | -44.26327 | 2025-06-06 04:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59505b9e-bf02-30ba-88c3-db4dc77f51f0 | -6.20079 | -48.54616 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c288039-90d3-38d8-8f30-ada80e602489 | -4.97699 | -47.81538 | 2025-06-06 04:40:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aa74e87-8414-3925-9935-18fe921121c9 | -6.20754 | -43.33557 | 2025-06-06 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81d5c6fd-6191-3256-bbb1-d51ce3ece290 | -8.67383 | -44.2679 | 2025-06-06 04:40:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9f49920-80f7-3624-a0c5-3284564ff4a2 | -7.20204 | -43.12878 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 60d3308a-7a38-3d1d-9bc6-5b73231cbed9 | -6.63981 | -47.35049 | 2025-06-06 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a95fb3ee-f015-355d-b00c-0ed7bc67a796 | -8.73497 | -47.98907 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9ae547b3-4653-3016-b83a-b8c695b864a4 | -8.87548 | -50.18532 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4fca4e51-a9f0-39c8-8d0c-2eb202059311 | -8.47348 | -49.6062 | 2025-06-06 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4badbccd-4b45-32f2-82e7-c32806235a3e | -6.66138 | -51.96186 | 2025-06-06 04:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9db939e3-7b3e-3596-a38e-d5dc7ace6d56 | -6.20258 | -43.33899 | 2025-06-06 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc6ad116-ae0c-36f3-b2ea-d59c82cdbb90 | -7.20423 | -43.13019 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2498fbc2-3053-3b99-a3c3-d18bc8001b6a | -6.05346 | -44.1657 | 2025-06-06 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f7723bd-c3d0-3cde-ae34-3ba01cf6e6c7 | -7.71368 | -44.16665 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a06d729-fa60-31fe-a837-26dd3a52e7be | -9.21511 | -48.85792 | 2025-06-06 04:40:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17e448f6-d6f0-3fc8-92c1-fee13a2a502a | -6.20801 | -43.33385 | 2025-06-06 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c37fcd6-07c7-3c52-8f48-821fdf0a669c | -7.90384 | -50.36325 | 2025-06-06 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4afa1cac-d378-33c6-a7c3-1de42e7fda9d | -7.19975 | -43.12953 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ef502314-6807-3ce5-9278-97133af6af05 | -3.40448 | -47.58205 | 2025-06-06 04:40:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c6d31c0-edca-3ebc-a1e9-f2efbe8d2281 | -7.20872 | -43.13085 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 15fda808-d3d5-38bd-9759-a0847827ae9e | -6.06365 | -44.23774 | 2025-06-06 04:40:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27853ea8-fef9-3ce8-8123-433bcabc737b | -7.00973 | -44.61124 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| c476454a-0ffe-3226-b609-efd696c1b43b | -7.72521 | -44.17632 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d15526c1-7e5f-3d08-a7bf-51be46a4f17e | -6.20469 | -48.54314 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c93baff7-f81b-380c-aab7-aa2d08be32b8 | -6.18855 | -48.55865 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a518858-bc2e-3f8c-8e25-98bc4eb618aa | -7.77539 | -43.05382 | 2025-06-06 04:40:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f8f84691-8c85-3536-a666-ccfe7be0de81 | -7.01427 | -44.60843 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| f3212053-ca24-31f0-b05b-6af18f2aacbd | -8.94113 | -47.29689 | 2025-06-06 04:40:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2afa7ee-3837-35c7-8a62-777fc3d9426b | -2.91852 | -48.23578 | 2025-06-06 04:40:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5311884b-2662-340b-945e-225b7b5beb0d | -8.7424 | -48.03265 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41636dda-6059-3dc6-b870-02882c99d184 | -6.19299 | -48.55216 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b49186a6-93dc-30fd-88ae-bb7bbe3d8b94 | -7.86037 | -47.89355 | 2025-06-06 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87c9d33c-db51-3e24-8068-f32a80b8c067 | -8.46419 | -46.48324 | 2025-06-06 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1dfceb7-1464-380f-8b7a-a28193a1b0c3 | -7.55617 | -45.82802 | 2025-06-06 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea2c7944-b4a8-3d79-a9d4-a184814c0a35 | -7.71899 | -44.15953 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d13301e-b18e-3a1d-879b-21e5710af316 | -7.71423 | -44.16277 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a5cf57fb-c5dc-39d9-bd94-6c07630cac39 | -7.20081 | -43.1376 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7b598015-b331-3f68-b394-4b48adc4b3e2 | -7.44871 | -55.43991 | 2025-06-06 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9d7de31-faff-3cff-be49-05fae31b0dd2 | -6.22757 | -48.55041 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5870f55d-01f6-3a48-a7ed-9c8f4b132ac9 | -7.72155 | -44.17181 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4e46086d-a481-38de-b2bc-49002015efe1 | -6.19416 | -48.56671 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88c2f36e-1abf-3de0-afe5-9a6313818ac5 | -7.20359 | -43.13459 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e8283bd5-1760-3532-87c5-b78c64418ee9 | -7.00672 | -44.6034 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48491039-285f-3112-b6f2-dda4b682d98e | -6.23092 | -48.55095 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a6187925-133b-35da-935f-cb2156046bb7 | -6.95949 | -42.06781 | 2025-06-06 04:40:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 9e4394c4-dbb6-3eaa-b4a3-e73aa4dbf331 | -6.23933 | -48.56304 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70a83f89-0414-3340-8716-f1e21ae51fb3 | -7.01479 | -44.60487 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c68e3a3-9070-3350-ac83-3fee598e3e6d | -8.92196 | -50.06381 | 2025-06-06 04:40:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ef04d7f-043b-3213-b5bf-bf30cbb933bf | -3.10305 | -53.04843 | 2025-06-06 04:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 748bedf1-f4c2-3a48-a6e3-de77c253ff20 | -4.4247 | -47.73442 | 2025-06-06 04:40:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0fff691d-2325-3613-8c7f-b48cc93cce8b | -7.89995 | -50.36623 | 2025-06-06 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f3518a8b-594e-35e0-89dd-9e20c11bce74 | -7.72887 | -44.18082 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| be24e215-7527-3a70-a866-c90ccca9b608 | -6.20319 | -43.33487 | 2025-06-06 04:40:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70c1242b-0699-306e-beb1-3d08e3b06807 | -5.3795 | -48.32851 | 2025-06-06 04:40:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b1c96b2-2785-3e24-93d0-2119b5720ce6 | -8.96476 | -47.96911 | 2025-06-06 04:40:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a433a79b-ab3d-3025-a135-81c65b4c425c | -7.90273 | -50.37026 | 2025-06-06 04:40:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f496c3c6-5b98-3cb4-b05a-b113c07f27ca | -8.47094 | -46.48865 | 2025-06-06 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32b8ce32-11bf-3fa8-8975-a63379ab009c | -7.01936 | -44.60185 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a9b5af3-9d5c-3941-af97-b352f616aab0 | -7.72942 | -44.17694 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9182714f-2e54-3f6f-90d5-87aa3aaf9e0c | -3.99655 | -43.24197 | 2025-06-06 04:40:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95441ef7-9615-3309-8544-3ccf239420fe | -8.72353 | -47.90185 | 2025-06-06 04:40:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5187b14b-908c-35db-8a97-303beee9dc4c | -8.47463 | -46.48915 | 2025-06-06 04:40:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d69b05f3-b99f-3d9d-9349-d120af734fa8 | -7.71734 | -44.17117 | 2025-06-06 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 013cf0e4-2fcb-3cdc-a4d1-9575cd5cbf85 | -4.00079 | -43.24261 | 2025-06-06 04:40:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d838578-4437-3b80-a926-3c33a91f537e | -7.05126 | -45.72697 | 2025-06-06 04:40:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 329973b3-ffc8-3b5a-8b42-54c385752738 | -6.96211 | -42.90707 | 2025-06-06 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4b9c3ab6-cee0-3320-892f-c30c222c1043 | -6.19245 | -48.55567 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64270602-a66c-39ab-bdea-03990b52c665 | -6.19744 | -48.54565 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d58fb276-0f52-374f-9929-c45c09da6937 | -6.21465 | -55.64889 | 2025-06-06 04:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83926d2e-b72d-3226-91a2-00d78428940b | -6.19689 | -48.54917 | 2025-06-06 04:40:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6af25d75-6371-3f3f-a6b5-575571aa282e | -7.01325 | -44.61554 | 2025-06-06 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README8.md)
