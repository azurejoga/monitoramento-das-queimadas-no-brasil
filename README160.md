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

## Dados Diários - Página 160

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 475bb945-9735-37dd-9ad4-083138a34dc1 | -5.95808 | -46.35002 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8ad022ca-6bce-3853-ade7-0aee14c44c09 | -5.98623 | -40.93377 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 07452e6b-4a2f-3903-b1e8-b7468e27f4db | -4.5832 | -40.77124 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 6c95c75a-d208-3269-bd07-b85b918f9993 | -5.74076 | -41.73809 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 397b360c-77d8-33ba-8694-0684a6a71ce9 | -6.62023 | -37.89888 | 2026-10-07 16:03:00 | NOAA-21 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 47c37af3-6aca-3cbd-bef9-d249970291b6 | -8.31464 | -50.37343 | 2026-10-07 16:03:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 017b7528-c9a1-3aea-aef3-1b02b0d9fef8 | -2.26376 | -48.75181 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1b5f42bd-04f8-33e3-a395-4b65fe446e4b | -7.85884 | -50.22364 | 2026-10-07 16:03:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| ed2fe608-d441-3f60-a97c-51b7e89668b2 | -5.20883 | -48.34105 | 2026-10-07 16:03:00 | NOAA-21 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 917b6609-89be-313b-9e91-09d3e3a68764 | -6.60343 | -41.58259 | 2026-10-07 16:03:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| fe1f61f3-fdfe-38b0-8607-266a56e9001a | -7.50999 | -45.77919 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| d7a04171-3369-37d1-a542-818835c0ab78 | -6.12337 | -44.13836 | 2026-10-07 16:03:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ffd20a6e-e235-3c53-9350-cacaaef2d92c | -5.97609 | -43.73652 | 2026-10-07 16:03:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1a5082ff-3b0e-3fee-9259-264cffea50f2 | -5.48469 | -45.63464 | 2026-10-07 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d6e27e7b-4c06-3923-ba23-b1c488c27432 | -5.51228 | -45.62515 | 2026-10-07 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e7d6fcac-91ed-3229-85fb-47269f6d5d99 | -2.99158 | -42.8348 | 2026-10-07 16:03:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| e2b2ce83-2209-380e-8139-df6735361c59 | -5.96545 | -40.94085 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 15.3 |
| b6057e6e-82dd-385f-ae45-680aaecdee95 | -3.65828 | -50.95254 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| dadb21c4-b2ce-33cf-abb2-9bb46e95dd5d | -3.77069 | -41.77557 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 35f18328-0079-35b6-8047-3cc2c0b54e20 | -3.58289 | -45.47836 | 2026-10-07 16:03:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 15ff5185-0128-37f7-9518-08d664bbd08c | -5.72201 | -45.15799 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 228384fd-1776-385d-8c4a-3913d190a0fd | -5.24467 | -50.91006 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 0c198624-7392-35fc-9fc9-1ffd7b21e7de | -3.88009 | -44.10558 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 6ea0fb11-712c-3638-bb88-383c373834b9 | -5.85245 | -42.65182 | 2026-10-07 16:03:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| be30a70b-beb4-304e-9eff-0fec778bc631 | -5.4681 | -45.68883 | 2026-10-07 16:03:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 57bbd49d-de97-377f-9c8c-6ee335e5ec9d | -6.37653 | -42.5332 | 2026-10-07 16:03:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| fdb8651c-12ec-3248-a090-937179777f35 | -4.26915 | -43.01623 | 2026-10-07 16:03:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5754e0f8-ab20-3ed1-803e-d92a61eeedd8 | -1.62516 | -49.39331 | 2026-10-07 16:03:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 067cd55a-15d4-3996-918e-c0bebcb480d2 | -2.74081 | -44.33584 | 2026-10-07 16:03:00 | NOAA-21 | SÃO LUÍS | MARANHÃO | Brasil | 2111300 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 15da91e1-9864-3b75-8699-52cdb5e032ab | -6.05669 | -47.31944 | 2026-10-07 16:03:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 99093873-745b-3e20-919f-d1d255cc0ebc | -6.67762 | -44.95782 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4bc043e4-8745-33bd-9555-fb1ff6f44458 | -6.94217 | -45.28165 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| df9e183a-7456-3f29-9f17-037c28e2bc0e | -5.96425 | -40.93286 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 9017b26d-1bcd-3bfa-85d9-75ffe07e408a | -5.73105 | -45.15415 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 228.7 |
| 2d06d05e-bba3-302a-8ed8-741c27ce8183 | -7.56362 | -46.70401 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| eb740540-af7d-3104-9c5a-d72d5bb02094 | -7.27518 | -45.57432 | 2026-10-07 16:03:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| cdfe8c77-0dfd-3aeb-adbc-040c05871f0f | -5.97013 | -40.92389 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| 5446cddc-8b41-36bb-9d1f-36bfcb90943c | -5.33803 | -46.19469 | 2026-10-07 16:03:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b7eef5e4-4bdc-3437-aa10-cd0361e5652b | -3.85268 | -50.41544 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 8e144c49-35db-372d-9bfb-fe636dbc742c | -5.9702 | -40.94837 | 2026-10-07 16:03:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 5befcd19-7751-3535-bad3-c0da5eae3b89 | -6.95578 | -45.27579 | 2026-10-07 16:03:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 31eeea45-8538-3ad2-b75e-205fe9be366f | -6.64897 | -43.78998 | 2026-10-07 16:03:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 701ccf0f-6d36-3b29-b079-8e463ad58292 | -3.75921 | -40.7661 | 2026-10-07 16:03:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 5.8 |
| e81ddeb9-3a42-30ab-8e1f-6ea53d6da6e2 | -5.94081 | -41.31683 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| de101323-af37-3538-9d65-d92fa655b83a | -6.33226 | -35.72874 | 2026-10-07 16:03:00 | NOAA-21 | SÃO JOSÉ DO CAMPESTRE | RIO GRANDE DO NORTE | Brasil | 2412302 | 24 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 41d13ece-d334-3cfd-bdd7-a2e570934233 | -7.4116 | -44.44689 | 2026-10-07 16:03:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 00abc822-2978-3cb8-9586-4ac68ae4c3ef | -1.16868 | -47.57227 | 2026-10-07 16:03:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 13705630-e78d-381a-8413-3550e7ddb5e2 | -5.61153 | -39.26967 | 2026-10-07 16:03:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4969dc54-5b68-3999-b219-022ba8e1884e | -2.19459 | -48.78419 | 2026-10-07 16:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d57c7367-0b96-316a-bc7e-b86a5e7a1531 | -3.69618 | -50.66853 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7d6937bd-a2f6-3e3f-a6c7-77a6f028adcc | -3.70277 | -40.83595 | 2026-10-07 16:03:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 255.1 |
| 769e0acf-b223-301e-a7bd-cac54f9586cc | -5.23904 | -37.58164 | 2026-10-07 16:03:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 1eca17fe-29ea-31fa-ae57-796ad59d8cc5 | -3.81003 | -45.39822 | 2026-10-07 16:03:00 | NOAA-21 | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f859dcc9-528a-3d00-ba75-e19283df44da | -5.5032 | -42.84132 | 2026-10-07 16:03:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 96.1 |
| 79412672-9d39-3758-ac48-68a45523da2f | -6.84649 | -39.55195 | 2026-10-07 16:03:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7808d7b6-20cd-3331-8f6a-ac3d4d14e395 | -7.17075 | -47.80421 | 2026-10-07 16:03:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| cccbe92d-a260-346a-914a-2d71fd9386d4 | -4.51168 | -42.89643 | 2026-10-07 16:03:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 71b79769-4b91-31b3-91fa-f3ac7b990e61 | -4.15019 | -48.00292 | 2026-10-07 16:03:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 1696785a-d5b1-3c56-a985-0f9dcc69fb6f | -8.0492 | -45.61194 | 2026-10-07 16:03:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2e9667b6-c30b-3ff9-a5fe-98c9eaf2236a | -3.01887 | -47.46738 | 2026-10-07 16:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6c0bba8-c6c2-3f9d-a34b-47b6ac75607c | -8.01454 | -47.18406 | 2026-10-07 16:03:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d2fa659a-8852-3091-b47e-ea022b164951 | -5.72485 | -41.65639 | 2026-10-07 16:03:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 5b31ea33-86d3-39bd-8e77-f515d2e51d75 | -7.01436 | -43.43968 | 2026-10-07 16:03:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 00ead396-d186-3983-a2d2-daeb4cea9090 | -3.75442 | -40.04101 | 2026-10-07 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.3 |
| fe287e26-a0c9-311f-a79c-b860faa7e189 | -7.10254 | -45.24522 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cfab5d54-65b1-3a22-9355-eaff64fa440e | -3.54447 | -50.1081 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b9c33b1b-48f6-36f3-8bcd-43ec4a6dccab | -6.9955 | -45.12809 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 72857514-d7c2-397e-832f-82c2c8c4db64 | -3.81213 | -49.11502 | 2026-10-07 16:03:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| be57f1d6-3cfc-3f76-9d89-ad4b7d42fc2d | -6.49871 | -43.97585 | 2026-10-07 16:03:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0bca71f3-5b77-31ef-9969-dfafbf3f7ff9 | -5.90558 | -43.27134 | 2026-10-07 16:03:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7279c3a2-0c99-3953-bc21-62f9d11e946f | -1.43729 | -49.03362 | 2026-10-07 16:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 491ccb18-2504-3648-9df9-ddef0418010c | -6.03557 | -44.3837 | 2026-10-07 16:03:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9c3749ff-7c58-31b5-827f-aeb6bedaeb33 | -7.80753 | -45.50297 | 2026-10-07 16:03:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| ebb87b59-c526-3506-8a97-881cf8e9eb59 | -1.92155 | -47.92461 | 2026-10-07 16:03:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30d78fe1-4418-3d2e-8aa3-98643101d8c0 | -7.42087 | -47.37456 | 2026-10-07 16:03:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1c251de8-8005-35dd-979a-c6d668ac8708 | -3.06523 | -44.44812 | 2026-10-07 16:03:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 1be607a1-9ac7-37ca-aa91-ed58d0b5ea00 | -3.58881 | -39.44294 | 2026-10-07 16:03:00 | NOAA-21 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f9b1ec9e-f121-3ccc-91f7-a3b16cb8e26d | -7.27094 | -39.71605 | 2026-10-07 16:03:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2a03c4fe-9918-347d-b91b-990dfd67a3cc | -6.84762 | -45.03299 | 2026-10-07 16:03:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 34c983a5-d902-3083-b22c-56e56e2ea004 | -3.65705 | -50.94849 | 2026-10-07 16:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 6d037778-a388-3dc0-ae50-11413a6e9fba | -7.55837 | -46.70472 | 2026-10-07 16:03:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 74a3375a-dd0d-3196-8355-af260c38736a | -3.88593 | -44.11638 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| cb129918-7c5c-3c7b-932e-eb33cf2a396a | -5.14883 | -37.3266 | 2026-10-07 16:03:00 | NOAA-21 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 17.0 |
| e8e1c8d9-2fe9-3db1-bd8c-774557bf2639 | -7.46825 | -42.82619 | 2026-10-07 16:03:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 2181597b-eaf4-34a6-beb9-67342a475fb4 | -4.58029 | -40.77553 | 2026-10-07 16:03:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 38.1 |
| 7dd9213e-15bd-326d-9ce8-888902870d1d | -5.24331 | -50.91771 | 2026-10-07 16:03:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| ab747aeb-c397-3c2f-87d5-f3215663120d | -3.42986 | -49.26341 | 2026-10-07 16:03:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| b8d3566c-7412-364b-a009-1f035e2d6fb8 | -3.80794 | -40.46251 | 2026-10-07 16:03:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| e7dc16b1-1f67-347a-acfc-4a7db0363fb8 | -5.37308 | -44.17523 | 2026-10-07 16:03:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 45e7e9ea-35f7-3dc1-87bf-0bea6d5acbc1 | -6.55446 | -35.50697 | 2026-10-07 16:03:00 | NOAA-21 | TACIMA | PARAÍBA | Brasil | 2516409 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| bc2968b2-e278-36df-8053-4150e50f5ff2 | -3.68326 | -45.84228 | 2026-10-07 16:03:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| a1f45fde-4276-326d-9dd7-a67923b3123b | -7.3849 | -46.20626 | 2026-10-07 16:03:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f72e3319-905a-3de1-aa2d-6249a1ac2470 | -3.88344 | -44.12833 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fdde8d0d-4ea2-3c4e-ab4b-c5df163ee906 | -3.5303 | -39.50583 | 2026-10-07 16:03:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| e21ff2ad-215f-3cce-a2bf-5fae0104ff45 | -3.1791 | -50.55051 | 2026-10-07 16:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 5a7da32d-d9d5-3f99-8bd3-5d8979829ba4 | -6.59812 | -47.40599 | 2026-10-07 16:03:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6a2f83cb-8f75-3ec2-843c-b7d519d611d3 | -3.87982 | -44.13269 | 2026-10-07 16:03:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d8f1dd73-c1f2-328d-b04d-38a24965172a | -5.86852 | -45.19972 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f4a2445f-47a4-3832-a863-42f3306c0933 | -7.0919 | -46.30604 | 2026-10-07 16:03:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bcd21eeb-f007-3d93-acf1-316743f0a3d4 | -5.73306 | -45.16849 | 2026-10-07 16:03:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |


[Clique aqui para ver as próximas entradas](README161.md)
