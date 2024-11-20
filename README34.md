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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9b9edd8-7a93-3972-a605-ef565f9d57bb | -5.61329 | -35.35615 | 2024-11-20 04:27:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0fc217cd-d87f-31b4-96db-b751e5d0c191 | -11.05958 | -45.19148 | 2024-11-20 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| caaae6c9-b2fd-3901-8e03-7bd55ca46037 | -4.93849 | -50.64709 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 561b5871-e557-3d21-8499-03fba90984db | -7.38856 | -42.77313 | 2024-11-20 04:27:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| beeab309-d27d-35ee-8da2-20ce3442bb73 | -5.20701 | -40.63849 | 2024-11-20 04:27:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a35e664e-e094-383b-b31e-d15407bda0dd | -3.85572 | -50.13283 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8006ba6-0974-3d26-a59c-aa6b81da3227 | -5.7598 | -47.0288 | 2024-11-20 04:27:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 66bf32eb-e3bf-36a2-b158-81660962a33e | -3.78193 | -44.06794 | 2024-11-20 04:27:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0739b625-3541-39b9-9bd3-7328084e6060 | -10.84719 | -44.90892 | 2024-11-20 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84f38612-9174-3868-8fd0-c5f9d073a345 | -4.20422 | -42.20038 | 2024-11-20 04:27:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1c26ab53-9f27-392b-bfca-be0827e15a7a | -3.7537 | -51.33991 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bc08411-8d2a-3931-bae5-d6ea17cb8e1c | -4.16661 | -45.51242 | 2024-11-20 04:27:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d52b573-d844-3d99-98da-212386884875 | -4.38404 | -50.42085 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6ee3a2e-e9a2-3a03-a73e-d3ddc05b56bc | -8.00153 | -44.39194 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03a44a77-3e0b-36fe-b5e4-015eed011bdd | -2.68931 | -51.80488 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fbdf6877-746b-32a4-a2c6-4211651ced58 | -5.05972 | -49.86343 | 2024-11-20 04:27:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56b664e5-820d-3cbe-bec5-367f210c4e34 | -6.01656 | -46.45263 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f436f45a-aefc-389f-9d1f-b9c861f8be0c | -2.95034 | -48.32935 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ea2dbc2-4f91-3fc6-9209-313b1b0068ad | -3.19679 | -54.32523 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c93edf32-ea16-3590-ba9a-438676217a13 | -5.48765 | -46.20309 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 64117162-8565-38c0-93cf-bde4da0a618a | -3.48738 | -48.23939 | 2024-11-20 04:27:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a219e80-06b5-321a-b45d-0684904232d3 | -3.02822 | -51.52392 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17b33d0d-c480-3aef-809d-49ec1ffc7d3f | -4.09669 | -47.81394 | 2024-11-20 04:27:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac14f831-d2cc-32d9-a8ab-8d4575fbedba | -3.27265 | -51.62336 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2d237dc-dd46-3ce8-8418-4920aedd3c23 | -4.64248 | -49.30969 | 2024-11-20 04:27:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57e49a41-21ee-3d40-9d98-0e95155853a8 | -4.10624 | -51.0485 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 013cc808-854d-3996-b3ba-0c2252a961e7 | -3.82829 | -47.4704 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e59e9115-2256-3b37-a0f3-ac8b5d732466 | -3.21982 | -53.841 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 083a79dd-027f-3781-a2f3-a5cd11345217 | -8.92922 | -44.25628 | 2024-11-20 04:27:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2372e34a-1f49-357e-903e-7fe4b5c56efd | -7.2243 | -45.17641 | 2024-11-20 04:27:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee2ded7b-4d65-3812-9e8d-c67fde3b352b | -5.26068 | -43.84028 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a74b3c68-e343-3c64-a656-9abf91c830ba | -2.93033 | -53.07405 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5cb2f99-2e97-36be-84f8-a53e8698bafa | -3.70926 | -53.75062 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fc9a0bd8-2fc1-3a5a-9d2b-0bd2485709e4 | -9.67222 | -46.25219 | 2024-11-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 98d0347f-c8ad-30ad-bcb9-c56758595166 | -11.24915 | -44.44418 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5abd406-180b-3e20-a6ba-98304690bb15 | -2.74896 | -51.83049 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 127275b5-3a06-3a5a-86a6-de7aaed113d4 | -3.88431 | -52.23672 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 48b8ee60-f617-3636-9efc-466eb0fb8360 | -3.67351 | -54.27411 | 2024-11-20 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f503292-61b2-30f5-b8ed-7c0209e35afc | -3.27243 | -51.62258 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72947f5e-aa50-3ec5-8207-54c5129c5382 | -3.9745 | -51.24609 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6b0e080-27c0-39b8-9409-b346e5f2fd18 | -3.88845 | -46.66204 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d18701ec-c440-37f8-8fec-af8681c0f1e2 | -5.82876 | -46.54685 | 2024-11-20 04:27:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1ce9b76-c49c-31b3-a351-e3e35b9ade03 | -4.73812 | -46.66772 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e65e25a-bd47-34e1-969e-a913e544bee1 | -3.81463 | -47.79682 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0c1962f5-c58c-37f2-a543-3bd4ca8b9d02 | -2.59505 | -54.01526 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c43e0b1-8ca2-3925-9aeb-1619e0a74f24 | -5.70189 | -43.26077 | 2024-11-20 04:27:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6906bd5-1050-3170-9294-c5feedccf9d4 | -6.36198 | -55.3679 | 2024-11-20 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e98dce60-9d84-399a-92c4-a91fccbd5dd8 | -3.88513 | -46.66153 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d1fbb16-bd07-3516-bd4e-ad9dc07ff46e | -5.60179 | -46.16854 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d8a9ba0-b9a3-3645-b2d0-78f35ec48718 | -5.45577 | -44.82302 | 2024-11-20 04:27:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1c62222-ab03-3e5d-8aaf-8437abf0a9d0 | -3.72564 | -47.37671 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75068809-f299-33d8-a354-55bf93103b07 | -3.80291 | -51.14399 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4897d555-9527-3a77-aa02-ecad5d64b45f | -6.38211 | -44.74762 | 2024-11-20 04:27:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 570305ab-b1aa-33e0-b718-93a66c128051 | -6.47616 | -46.07913 | 2024-11-20 04:27:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 23e2e36c-0953-3472-84bd-2c12ac115c2e | -5.2572 | -43.83974 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5d6a73d-b190-3dc9-92c2-a23b64d25eea | -3.87137 | -47.07535 | 2024-11-20 04:27:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 009db631-1c35-3538-b1ed-39c5d86c2b3a | -7.53105 | -46.2272 | 2024-11-20 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9ffc8ff-af48-3f15-998f-f039931977c2 | -5.75828 | -46.05861 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39e9e0e6-4fb1-36c9-af34-de8aea85e1ba | -9.16125 | -44.30201 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f2b493e-5d37-373d-95a1-9175e74d00dc | -5.18391 | -45.44353 | 2024-11-20 04:27:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0d98a02e-1a76-3c5a-9092-b6ac8769c9fb | -5.94975 | -48.06275 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b60c1ad-9cdb-3cdd-a587-22ac499a464a | -5.39441 | -45.13478 | 2024-11-20 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2db9c557-0047-3a1c-85d3-c5fcb715a957 | -2.93215 | -48.33054 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| baa078e3-5a3b-3484-9a5d-53a60c7ad5f8 | -2.92872 | -49.42562 | 2024-11-20 04:27:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40eb315f-2ff6-3d65-bc87-f39a21a3cd7a | -4.74298 | -45.41435 | 2024-11-20 04:27:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 967f8cae-dea1-3e47-8f7b-1adf82f91778 | -3.64985 | -45.20545 | 2024-11-20 04:27:00 | NOAA-21 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d1d7c840-5ef8-38c3-a1a8-d0227d768a25 | -5.37686 | -50.47672 | 2024-11-20 04:27:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 854d8414-214e-3049-91e0-1de7f95724f3 | -5.7025 | -43.25669 | 2024-11-20 04:27:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c612a148-1966-358e-b3c5-44b919c58143 | -5.06283 | -44.79593 | 2024-11-20 04:27:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de9b7eb4-1946-3ebd-b20d-65a1512b8cd2 | -3.88011 | -46.06298 | 2024-11-20 04:27:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8240239-b79d-309d-8435-1d71bb2a5f62 | -2.9131 | -53.06076 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| aa10e182-c029-3a4f-9a39-ab0b5ba2ec48 | -5.09567 | -45.98994 | 2024-11-20 04:27:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2d4a43e-7035-3855-a7b8-5f10f8993d02 | -3.41864 | -50.71207 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ead89ea-d929-36c9-94ba-0d798e9f2d38 | -3.8618 | -44.44451 | 2024-11-20 04:27:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d48e301b-a824-3330-8e2a-c35cf14b7d2b | -4.31396 | -43.70611 | 2024-11-20 04:27:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a30c5ab8-f12a-3a13-8fd3-9807d33aaeab | -3.24138 | -48.4375 | 2024-11-20 04:27:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d87e49d-8d00-3728-9bd4-248fefa111d8 | -5.3836 | -44.96563 | 2024-11-20 04:27:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 659739a6-5b8c-35e5-8a7b-1b96ed5cde01 | -2.27656 | -53.6419 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e67396c9-5cd1-3299-b7d9-512e6a7a1e3a | -2.80961 | -54.0235 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dbbede9a-5f51-36ff-9b43-3cbd0a6d8f8f | -3.78932 | -44.06531 | 2024-11-20 04:27:00 | NOAA-21 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6986fafb-3533-3b76-b976-0657b6cceaf1 | -3.76546 | -53.85062 | 2024-11-20 04:27:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 53056f99-bf2b-3928-9c85-abab75142a18 | -6.0101 | -38.65507 | 2024-11-20 04:27:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3a398afc-c257-3354-91b7-a661391771d6 | -2.91909 | -53.06408 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 27882521-4bf6-3d4a-8632-5c9f2f714d71 | -2.84921 | -48.67003 | 2024-11-20 04:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 758a5aa7-bc98-3e28-ad55-0118e9975480 | -2.85729 | -51.58733 | 2024-11-20 04:27:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea69959e-0e7e-3ffc-8347-b5f1e2bdc0eb | -2.34492 | -54.78038 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bfbf3ddd-e0d5-39f7-a83d-9117ba8bd6dc | -3.01122 | -51.00609 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae944468-8c71-3c3e-b8c5-222b811f8086 | -6.41176 | -47.51236 | 2024-11-20 04:27:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c69b49b0-ff25-3364-86e1-6bfd60ff4647 | -11.24676 | -44.44642 | 2024-11-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37327aa1-f335-3fc4-94bc-41333524eeb1 | -3.84796 | -50.69635 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6509c874-0807-36c9-bd5b-ef7e0234e07b | -4.44795 | -46.58655 | 2024-11-20 04:27:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 35.3 |
| e8b954c1-6f18-3765-94f1-fcd6d4f8ab6d | -5.69912 | -45.84774 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc3dba34-5fcb-3c31-a2fe-4b80faff553c | -3.81063 | -47.79999 | 2024-11-20 04:27:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d036f3a5-b3ec-34ee-a480-23ecd34d1cc8 | -2.92575 | -48.32555 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a3c68ff8-2b5b-3fed-8019-c4238f1bb4d8 | -2.73975 | -51.72309 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 628a8891-322a-3fe2-af30-9e8dcf24b130 | -5.85121 | -44.38877 | 2024-11-20 04:27:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11079fe5-7e85-360b-8d16-7cc07b1b6f18 | -4.53443 | -38.57743 | 2024-11-20 04:27:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d4049055-40f3-36d9-8f5a-f706eaed7cf7 | -11.01118 | -45.26397 | 2024-11-20 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4b04251d-b6fa-3785-a738-27508a80e0e0 | -2.61851 | -51.80225 | 2024-11-20 04:27:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3758a0a9-2eec-37d4-9edc-5d350c429ee4 | -8.00001 | -44.39272 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |


[Clique aqui para ver as próximas entradas](README35.md)
