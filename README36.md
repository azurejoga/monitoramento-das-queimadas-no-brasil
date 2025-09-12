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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1019700a-abf7-35a9-8fc4-6b3f2abf183a | -8.54768 | -48.95397 | 2025-09-12 04:04:00 | NPP-375D | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22bef53b-bcd4-3c8f-a4c0-99e3961b664c | -10.17106 | -46.1769 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51ffe488-f398-3007-9f68-064f265a0fe2 | -10.89757 | -47.2442 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b48af6a-7912-3635-956f-fb06f7407667 | -11.24422 | -49.41232 | 2025-09-12 04:04:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc9153a5-48db-3630-86fe-3525293b4882 | -9.04681 | -47.06579 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| c107dc59-e41a-31e9-935c-812824672cbd | -9.02143 | -46.12109 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bcab4ab7-7991-33c2-b354-c529f9d6f4a8 | -11.13932 | -45.23867 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6906f1e6-fa72-3b48-9450-d2a1349a5bf8 | -8.88252 | -49.9311 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 36f90f4f-ba30-3c13-8298-65e2c3c03e96 | -11.41239 | -43.70768 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 599f4f8e-4b77-3b38-8aea-06a9fd2a35fd | -7.55607 | -44.38735 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a08203b5-1f35-36fc-983f-5f8152b8fae4 | -5.598 | -42.91521 | 2025-09-12 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bb2f07de-a0b5-3513-aa21-d969d1f1ab01 | -9.72402 | -48.33617 | 2025-09-12 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7a32de6-600c-3278-8835-8ad97cc22320 | -10.35014 | -50.53279 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46127245-8690-3794-ad73-09436c3e466a | -11.4336 | -48.56495 | 2025-09-12 04:04:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef284e2a-54e2-3f64-96d8-4d3e83518de2 | -6.81565 | -45.64798 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce952c06-1c44-3cb3-ba03-2c2ceffdce86 | -10.7818 | -45.99492 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c60f07bd-218d-3050-95cf-5efbfc0979bf | -6.05213 | -43.10537 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93c07886-6cd7-3e91-b0e6-2d36e6da1c71 | -3.69348 | -49.10274 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e27b2a0e-b28e-3352-aad1-28b4f4470995 | -6.15411 | -42.61337 | 2025-09-12 04:04:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fc5e5995-ef04-3736-a1ec-54424b632000 | -6.8236 | -52.79824 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 96c7af09-3811-3ef2-9ee9-850ae81de765 | -8.08185 | -42.56271 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8c97493c-e3fb-303d-9105-6ae9afbc2dab | -10.58283 | -47.21848 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b0d89b8c-c7b8-36ce-b675-672ea53cc744 | -9.10848 | -47.11814 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc9172f8-00ea-3aa0-91bb-aac80f49d3a6 | -3.83402 | -48.94923 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 860e99e7-9471-30cd-802f-923fda3a9116 | -10.67578 | -48.60015 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 50e2088d-b18a-3ffe-94fb-e6b016e648b4 | -10.5553 | -51.48598 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e829c3f-1554-3730-9ce3-e553ac4d6024 | -3.68931 | -49.5724 | 2025-09-12 04:04:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c20315b-b4ad-37b3-a6fc-ad89f6831b9d | -9.11317 | -46.96396 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf707a7f-8a95-312d-8538-678fe0399baf | -6.30337 | -44.23406 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e7244d3-ae16-3dbb-94c6-fa1fcc168a88 | -7.32663 | -44.41814 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4abeddd4-0460-3fd9-ba61-173f9c76528b | -11.67363 | -46.56367 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7df47bc0-da7e-3ccf-a3f8-f1697cbd5968 | -6.82701 | -45.65768 | 2025-09-12 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cffe9dba-0dc0-31b5-903c-f121d3b8e142 | -6.31363 | -43.32754 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 75b48c8c-ea45-3a86-8a5f-a4c57a02a695 | -3.68786 | -49.10186 | 2025-09-12 04:04:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fe52358-6b16-30d7-ad93-3a1a3ae1de37 | -6.44736 | -44.03955 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 978db5a2-3587-356f-9943-d400a9b5d8c3 | -11.68726 | -46.52219 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fa8646e-e522-3a7f-aa20-945ecb7102b0 | -6.32162 | -43.44033 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efd1a25e-ed80-3131-9790-bd935c6c747d | -8.89942 | -49.93771 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 341f2807-87ec-3f92-9651-820b40f03523 | -6.252 | -43.42432 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db87dfa7-e761-3c58-94cb-52f4edeae90f | -6.81574 | -52.80319 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7155f516-7bc3-3691-90b7-a97b104729b9 | -9.35017 | -46.59374 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2b8b2d8e-e44f-34f7-9252-53ef6743494f | -10.77714 | -45.99778 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 067eb135-3823-38b7-a85e-b49120f30faa | -11.15053 | -45.31771 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 328245c9-21a3-3eb1-89ff-4bf2a26dc7ab | -10.22008 | -46.24773 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e967cfe-affb-3823-b500-62d403cb2b2b | -6.70808 | -42.04761 | 2025-09-12 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8487962e-52f2-3991-a2cc-8a3cdc6b5785 | -7.2489 | -44.47288 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df45682f-8af4-3bbc-88c7-bbecaee20833 | -6.32943 | -53.46471 | 2025-09-12 04:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22f1451a-bcac-3a4b-b751-c756b5bf9ff3 | -5.92277 | -45.74097 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0cabe50-64e3-3a09-af74-2e802e85e6e7 | -8.0843 | -50.18927 | 2025-09-12 04:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 31926886-00e6-3803-b1b0-7d535d8b6af4 | -12.10398 | -44.86461 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 427983ca-4e2e-3753-b2c7-490cbd66fed0 | -8.43819 | -46.89415 | 2025-09-12 04:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7c46f24-edb7-355a-8007-54acad40655a | -8.87397 | -49.53773 | 2025-09-12 04:04:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 58d2e207-3213-33ee-a724-3bc3ca089d5c | -5.86444 | -48.15729 | 2025-09-12 04:04:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b58b385-13a7-382e-ab20-0abd648e4482 | -6.22043 | -43.37616 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65ca1a69-9a8a-3b72-830f-39393ab85fd1 | -6.30266 | -42.2279 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| de2cf059-468e-3643-bd38-fb5b0d030dbc | -10.4285 | -50.62502 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2ab188e-ba67-3c5c-bf64-4ac238dfae11 | -6.67997 | -44.14412 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b1ecc9cb-40d1-389b-8fc3-0ebc0e58a6a2 | -6.19888 | -42.66481 | 2025-09-12 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f659aa05-ff6f-3785-be61-42c4c257dbde | -11.08766 | -48.44281 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2f97ba82-e604-300f-8f9f-0d8618f5881d | -9.0148 | -45.7408 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d648aab3-8ade-329e-b118-3613e051bcbb | -10.78925 | -46.00006 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca230aad-12a8-392a-af76-2328a6fa41cd | -11.67154 | -46.58569 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8660a206-7015-390b-a55c-665df4102e87 | -6.60976 | -42.27142 | 2025-09-12 04:04:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 66447c9e-86cd-3dbd-8048-1cbd8ae6eb5d | -10.85366 | -48.15963 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d6941c5-6ea7-3508-9170-28c30ab89d2e | -5.65454 | -45.94524 | 2025-09-12 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 59e181bc-4dca-33de-bcb6-0373aa3df059 | -7.44284 | -44.44007 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c7555070-3e22-3e1c-b15a-bd528c2ddd69 | -7.39939 | -44.36174 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eaa137db-e79e-3685-9eb7-4ede3ca00cbf | -11.70357 | -46.50236 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e501e867-fd6b-3bb3-9b36-866ab7c81dd5 | -10.21662 | -46.24316 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a612755d-c8a9-35f7-a64b-4a60e1e3f1a6 | -11.14109 | -45.23594 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6bcc9c2d-7660-337a-84de-b3d0f974c708 | -7.23957 | -44.48095 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c0fa84d-26de-32f3-b10f-67b4279ed11f | -8.94535 | -46.72062 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f6fa7251-195a-3802-ae88-a7ed1c86ea89 | -11.6732 | -46.59076 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 69f803ad-5dad-3633-a61a-a42383a459e7 | -8.48468 | -47.27235 | 2025-09-12 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4666e293-63e6-3665-ae9f-26e29c8c15d5 | -5.2784 | -49.29506 | 2025-09-12 04:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a2a37d6e-3355-3c56-9d73-b282d87f9249 | -9.05093 | -47.0423 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 84a09d89-4ff6-3e16-b6e2-157096ae59e9 | -6.96189 | -44.82633 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0fceb2cc-d95d-30e1-bfe8-4f9ce5a17ea3 | -9.06888 | -46.57568 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec429e92-e7f7-3d7e-b2d0-380b3cb44378 | -8.18936 | -46.10357 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c311b86c-cfb1-3d9e-a50a-21158718514b | -7.41603 | -50.65277 | 2025-09-12 04:04:00 | NPP-375D | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 949ae4cf-da64-3de4-9b72-f68c16cb08f3 | -6.2949 | -44.23708 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fe658c0e-7af4-3b32-a571-387765fd05d7 | -8.88794 | -49.93213 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c74fd6a9-36b8-302d-b7db-78dab158edbe | -8.89464 | -49.93327 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bded842f-aa40-3511-9ad2-a0086b2be8ef | -8.18063 | -46.11168 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5785206e-7bcc-3923-8af4-5f0482e86566 | -11.36671 | -43.50864 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfcabe88-9a9e-3140-ad4b-7f941e137547 | -9.95966 | -51.68756 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c9649019-020e-3836-a83a-536d69a0d78c | -10.70277 | -48.6157 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 85d1064f-0605-396a-b4a2-529b26dc684c | -7.56216 | -44.3982 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3eb9bce9-823c-3828-bd5c-3725c3dad44b | -6.44582 | -44.0728 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0cbdc441-44e7-355f-a506-9082875d332a | -11.44873 | -43.57822 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 824755e9-5188-3a4d-9cab-6ffc8ee1fa3d | -7.54373 | -44.39021 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92151077-ec63-333a-bcd2-24ea8e574981 | -6.30203 | -42.23175 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| d6b2b83d-cdff-312a-8107-b1d77913f3f8 | -8.17947 | -46.11004 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8db7d1f6-37f0-3dde-b538-6f16f896c21a | -9.34173 | -48.94933 | 2025-09-12 04:04:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 731024b0-68b6-3dcd-8c48-4cd265860f6b | -11.66989 | -46.60992 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d285a13c-9c67-3618-9daf-20f6e30963b9 | -12.02034 | -43.79087 | 2025-09-12 04:04:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b0aee2b-a33f-3fc0-92d8-d06f4c32bcb7 | -7.05524 | -44.69715 | 2025-09-12 04:04:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd438993-61ed-3a34-8acb-755a469d4b77 | -10.41005 | -50.0116 | 2025-09-12 04:04:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0df0be78-54cc-32b3-84bf-1dc6bc19e97e | -10.74851 | -48.18122 | 2025-09-12 04:04:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 44518582-3431-3715-bc75-d4fc1c26fa36 | -6.68772 | -44.12164 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README37.md)
