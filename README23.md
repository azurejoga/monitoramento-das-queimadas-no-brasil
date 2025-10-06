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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4ef39a-fcc8-3f72-89ae-8602539c1e19 | -4.74402 | -46.15441 | 2025-10-06 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9815bfd1-73c2-3e1d-9024-fb8847d875ad | -8.46806 | -45.92323 | 2025-10-06 04:25:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35ad60a0-47e6-3d70-acef-1200f7ea8d6f | -8.62021 | -46.30172 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04fc24c8-5d44-3275-abdf-e12fe6ac628d | -5.88887 | -38.48832 | 2025-10-06 04:25:00 | NOAA-21 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 43780445-d0da-3055-8331-cbe1c53b33d6 | -1.12141 | -53.05684 | 2025-10-06 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9d465de4-b99d-358f-a7de-8df5273d4ea5 | -8.74834 | -47.20331 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 32580a39-a1ad-390b-9826-6b7ac9cd5ebb | -5.20969 | -46.1997 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8b6071d-1819-36f9-96fd-83606a66836c | -6.59029 | -43.73081 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d1efc158-904b-3668-9d89-7f0d1119377e | -8.1941 | -44.19876 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 932fb0e6-f4c5-3b36-9e3c-7a84b2a4d318 | -6.63415 | -41.98611 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| fa487358-11f6-3dbb-bf25-662473f49600 | -5.64141 | -45.96568 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 94d5b4a7-c4a3-35be-b3ca-2127f4b93276 | -7.80092 | -42.58204 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 40cda6be-8a86-3c4f-a0f0-c9817d79b667 | -8.18184 | -44.24538 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0eb4acf-bfb1-3c04-9247-9ba2b8c35dbd | -5.77744 | -45.74345 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84007251-e679-3a18-b269-d5708ee94f3b | -8.07416 | -47.24818 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba2bda45-6117-33e1-b1e9-38a484242c78 | -5.43131 | -45.73847 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f6a7aff-ffdd-3d4a-8ee2-7e0860897eaf | -5.64194 | -45.96224 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 40317b86-9efd-3d9e-a91f-8fb83b285bd0 | -8.5591 | -47.25808 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a91a0c8d-70cd-3bd5-a1b3-e8fcd33c5f0a | -9.65719 | -43.83803 | 2025-10-06 04:25:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fa662568-bce4-3a29-b72b-052520696953 | -8.53269 | -46.29867 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8b6de28-9e46-32e6-80bb-83cdf5240c5d | -8.81787 | -47.32472 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d6ecbf7-d2be-33b0-8eaf-5e572304fa4e | -6.87797 | -47.23489 | 2025-10-06 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0a8ac02-ddda-34eb-a6a2-884392e0c7d7 | -8.55689 | -47.2506 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52b526a9-797b-3c41-8307-03ce808fec50 | -3.91324 | -52.25393 | 2025-10-06 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77eead14-47bc-3c73-8334-d28dd0e2917c | -9.06524 | -46.63555 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b177532f-a056-3b30-bef6-334dc07fb9c9 | -8.92625 | -47.37067 | 2025-10-06 04:25:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a97d7c1-b588-3149-89e1-7c7811ea9a9e | -5.19689 | -46.152 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 036e69fc-7e4b-33a1-9271-92092b0ab4eb | -7.87852 | -44.12923 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d866e4d9-7638-33af-b3cb-6fcf540690fa | -5.25953 | -46.49012 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2417e269-e867-3e2d-b6b9-4317750b5ff8 | -5.43461 | -45.73898 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e2e6792-cec7-35ba-9b05-3811ca753a65 | -5.26406 | -45.59188 | 2025-10-06 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ded4112b-1392-3215-9af1-a4578863513d | -8.53244 | -46.38763 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56617580-c921-31cb-85e6-0852f7c5b90a | -5.54687 | -45.43438 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 826fe73d-e5b1-3d63-bb97-298f4dbedfb6 | -5.97724 | -45.8805 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5813dd16-c071-3ca0-9a10-6739f0dffe3d | -6.66671 | -42.77536 | 2025-10-06 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4aa7e900-70d7-3fd3-be19-115f001182e4 | -7.54592 | -49.92223 | 2025-10-06 04:25:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de78b837-47ed-378d-a028-a2149cdbd52d | -5.79915 | -45.47392 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb5c9cfd-fd63-3b87-af99-ffc8ce1b01ae | -4.64819 | -43.18212 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3f9d77e9-8632-34cc-a45d-77a55e37ea43 | -9.02037 | -47.35766 | 2025-10-06 04:25:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6eb8b992-5149-340e-9ae8-d64b9a2ec4c2 | -8.16377 | -50.16057 | 2025-10-06 04:25:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdcbdbe4-b4c3-344c-9359-c2a9b8e97dad | -7.0343 | -49.30217 | 2025-10-06 04:25:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59e1b15d-cc6a-3bea-b3e5-bc10ae90451e | -8.58222 | -48.70065 | 2025-10-06 04:25:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3448384a-0656-3c86-873c-2718e732a835 | -6.64787 | -41.9733 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| aa168d73-80fb-3123-9537-2cc23dec9ce2 | -5.2749 | -42.91857 | 2025-10-06 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d6878843-b709-3bf2-b3e2-93165d5be983 | -5.26529 | -50.99059 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58847b4c-6439-399b-b736-bb21706b9089 | -5.47411 | -42.89085 | 2025-10-06 04:25:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a020bc07-992b-3f27-8ed7-1e702fb92ba6 | -8.27346 | -43.83103 | 2025-10-06 04:25:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9ccfb1b2-0870-3e38-a61e-b02f196cb5af | -6.69677 | -42.16329 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| c91141a5-504e-390d-bbd5-3a748b75b0c1 | -5.80596 | -46.12864 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c1ec660-d1aa-3523-9c1c-bdedb1713b34 | -8.56019 | -47.25113 | 2025-10-06 04:25:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b0377d0-7d47-3a7a-96f9-17fac9cf592a | -8.88694 | -47.61851 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 32226056-5745-3720-b917-db1497721000 | -5.99405 | -45.46836 | 2025-10-06 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1e23814c-0ae8-3476-9d7d-a1281c0bfa1b | -7.00955 | -42.80561 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4752e2d5-106c-3e44-bac1-f9284f2ddf19 | -8.62129 | -46.29477 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df356fee-2024-3bb6-bcdc-91c8735e06bd | -7.49284 | -45.1697 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f091fd8b-ae46-3549-a93b-658e91c441d1 | -3.81188 | -51.29041 | 2025-10-06 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4158232a-243a-32d7-b15f-e15d15e09a46 | -5.23907 | -45.3791 | 2025-10-06 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95bb8531-c993-3567-bb57-1b35a6aa4be5 | -5.83847 | -45.83412 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4bfa0b72-9403-3693-b8a2-e94de948ea43 | -7.21562 | -45.90563 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2006ea41-4b67-3e15-97f1-912add7d12e3 | -8.56525 | -46.3287 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 427504a6-863b-32a4-8b87-32f46d89568a | -8.55483 | -47.69444 | 2025-10-06 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa8fcc21-26e4-3756-bff9-73e9db454dd8 | -6.70168 | -42.18289 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7df0f4d6-5ff6-3c5d-8e07-eb4f4e765a1c | -8.20046 | -44.15561 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a7557e07-1b2e-32a2-a663-41909421178a | -4.89906 | -45.94653 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9369dcba-c958-33ce-aa8c-a139cbc23bcf | -5.10113 | -42.62913 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0587e6f9-acc7-3ccf-a8fa-f0f34e349641 | -5.2842 | -45.17591 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d705695-8491-3ede-b714-818bf64ddf93 | -4.81361 | -45.79604 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 188cbd43-1ac1-3768-ae59-66bb9f7167cc | -7.46644 | -43.03275 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e505a41e-bcb9-316f-a407-375c8f13571c | -8.61859 | -46.31214 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eb8bdefa-9930-3441-a213-1e47b4275c1b | -5.09446 | -42.62392 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7771d18-a12f-3051-b568-1170d6255998 | -3.67535 | -55.57642 | 2025-10-06 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 514c20b9-59b1-3e30-a5ff-3a59439191a3 | -5.36726 | -45.95394 | 2025-10-06 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2b0bc3b-6060-332b-ab8d-c764fe80ae6d | -8.55398 | -46.24855 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 591e598b-7a1c-3deb-9dda-39504449caf7 | -7.78826 | -42.58955 | 2025-10-06 04:25:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 746bd0cc-effc-3cf4-b914-c07fc947805e | -8.55164 | -46.37286 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04399b5d-e728-34fe-8a7d-52bbb9833669 | -8.61528 | -46.31162 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a7f23bc8-1bd4-38a8-a316-a65387de4cc8 | -5.74581 | -45.51187 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c0d2c6b-4304-3725-a468-a1ef1a37aa38 | -7.32566 | -47.28843 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6521c6c-66a2-34c1-afcd-4a3ea637623b | -5.7427 | -45.4225 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb803116-4c72-3ddf-8161-ac596d853011 | -6.73778 | -44.92528 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 571201c2-2150-308d-b3f2-02f360715655 | -6.29567 | -46.09016 | 2025-10-06 04:25:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e85dfa4-2df5-3198-862a-2fc08f447946 | -4.64696 | -43.19004 | 2025-10-06 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fc6fa66-2857-3c5c-a362-3c3b90476aea | -5.19635 | -46.15543 | 2025-10-06 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 04be7044-b793-3a7c-89ae-e778ef014e0d | -5.7425 | -45.51135 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca11458c-3176-34fb-ad11-e9bf5b9090e9 | -8.19893 | -44.18007 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 314bd429-09fd-3a18-9f52-13520a4cd5d7 | -7.46213 | -43.03657 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 93e5296d-a269-32fc-9dd2-07a9a110ae20 | -5.63037 | -51.09087 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a89a8b12-53a3-396e-b866-2902bdb3217f | -9.20576 | -46.91393 | 2025-10-06 04:25:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8139b533-cb2d-31e2-963e-2e53b6f6ad17 | -7.02845 | -42.30529 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 02a26933-1c91-3af8-b0da-2f6cd7a9e458 | -8.87242 | -46.80032 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3a91fa06-ce41-37a0-bd54-9ff409748dc6 | -5.77151 | -45.78143 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81044fb1-eee4-3ea1-a352-1bb34f2b01e2 | -8.19186 | -44.20303 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1fafa4d3-404e-38ce-ac22-04138517cfb4 | -8.37287 | -48.64764 | 2025-10-06 04:25:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 581f9d21-8477-3222-a17a-02279ab61933 | -2.25114 | -47.86959 | 2025-10-06 04:25:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de710e54-6d59-376d-bf2c-c350458d686c | -5.26783 | -50.98787 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f9d5a75-962e-324e-bf34-94c2ff19486b | -5.22631 | -43.79624 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9b3ce7f-9b3f-32b5-a544-77228aa8de74 | -7.78495 | -42.61264 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9eb35656-ca4f-3369-8773-df373a8eb6db | -6.07273 | -42.53753 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7fa26154-68ec-39cc-a5d4-28dee6422afc | -5.40667 | -45.91782 | 2025-10-06 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c16228f9-8d33-3e38-9116-611dd7c37860 | -7.19189 | -47.61662 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README24.md)
