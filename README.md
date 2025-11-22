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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bbc35be-c76e-3218-a552-c55931a3fc94 | -23.486799 | -51.479401 | 2025-11-22 00:28:00 | METOP-B | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3843da12-376f-307e-a870-edc643baf12f | -27.849899 | -49.499599 | 2025-11-22 00:28:00 | METOP-B | BOM RETIRO | SANTA CATARINA | Brasil | 4202602 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0fb4922e-6342-32c6-a1f5-64b25970b667 | 3.1101 | -60.749001 | 2025-11-22 00:28:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0ba1a484-77d0-3fae-aaab-2ba5f035b0e8 | -4.1211 | -50.081299 | 2025-11-22 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2e64a48-bf94-3d4b-9757-8b6968f2e439 | -4.0202 | -42.521 | 2025-11-22 00:28:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c85b9fb-cca2-30fd-b60b-c3b68ab3b18a | -0.9922 | -53.737598 | 2025-11-22 00:28:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4586a9d4-0804-3c86-86c0-5b0a27f867c5 | -0.9938 | -53.744499 | 2025-11-22 00:28:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1619a2-c8a7-3795-b008-2cafd1b5ba14 | -4.1191 | -50.072601 | 2025-11-22 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 113cabed-954e-34dd-b03f-a31d39c92475 | -3.7457 | -52.074501 | 2025-11-22 00:28:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32d8aa69-1aa6-3034-828d-6526a774256d | -4.1093 | -50.074799 | 2025-11-22 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0ef9ff6-85f5-3132-8d52-f41f289a1d02 | -23.4884 | -51.487499 | 2025-11-22 00:28:00 | METOP-B | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 78dbf30d-faee-3b74-bf12-2830805e3d4b | 2.5369 | -60.560398 | 2025-11-22 00:28:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3c08f7f0-868f-370e-b9d7-e16d5f98b34a | -4.0884 | -48.835701 | 2025-11-22 00:28:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee0393a8-4a2f-33ba-bccf-4e240a980a9b | -27.848301 | -49.4916 | 2025-11-22 00:28:00 | METOP-B | BOM RETIRO | SANTA CATARINA | Brasil | 4202602 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0e43e688-f3d1-36ff-8bba-55939abd011a | -4.1113 | -50.0835 | 2025-11-22 00:28:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3d4262d-7910-32ad-b545-a3664c31e40e | -3.6073 | -42.000198 | 2025-11-22 00:28:00 | METOP-B | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e6b27d33-e073-3cd6-ba4f-73167bf408ab | 3.1075 | -60.760101 | 2025-11-22 00:28:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7a5979a6-6e35-3720-988f-d60f4789ec3b | -3.5978 | -42.002499 | 2025-11-22 00:28:00 | METOP-B | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5e078613-6f6b-3572-b409-9303b76a8b70 | -3.8211 | -45.364101 | 2025-11-22 00:28:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fdb2c606-a0da-343d-beb3-f34121de1e6a | -0.9568 | -47.561901 | 2025-11-22 00:28:00 | METOP-B | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6bb2d6-e303-332f-8da1-da81a54619d4 | -4.0835 | -48.814899 | 2025-11-22 00:28:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b74b0adc-dfb2-3898-ba19-0602f4940759 | -3.1735 | -48.618801 | 2025-11-22 00:28:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f89293f5-a313-3b14-87bf-0f9494b451a3 | -3.8168 | -45.3461 | 2025-11-22 00:28:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca21d08-2855-3588-8566-0d8c693a6413 | -3.3401 | -53.277901 | 2025-11-22 00:28:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75abc4e1-b736-3934-b5d7-61895ffdc448 | -4.027 | -42.548901 | 2025-11-22 00:28:00 | METOP-B | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 85de066f-dd68-3991-b3e5-a83a69021329 | -0.96 | -47.575901 | 2025-11-22 00:28:00 | METOP-B | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40ce399b-9e6d-34c3-9644-434d0e269265 | -3.6148 | -42.030899 | 2025-11-22 00:28:00 | METOP-B | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 28a85698-0479-343d-b5d8-0567c2308525 | -4.0298 | -42.5187 | 2025-11-22 00:28:00 | METOP-B | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a3bff68b-63da-3871-a5aa-bfefe725a258 | -3.8308 | -45.361801 | 2025-11-22 00:28:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a990b6cf-88d8-37d5-a1bc-2f6ac660eaf1 | -3.8265 | -45.3438 | 2025-11-22 00:28:00 | METOP-B | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 329139f9-7ea9-3d12-9123-80e760fc9411 | -1.5897 | -47.0215 | 2025-11-22 00:28:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 191d9705-7c1c-35af-93eb-00b7ad7f4073 | -4.086 | -48.825298 | 2025-11-22 00:28:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48cad50b-d7cf-380c-9334-5f923f2aa6cb | -3.1709 | -48.6078 | 2025-11-22 00:28:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7b4f3d1-dbac-3ace-abc4-b303f485c532 | -1.0198 | -47.2145 | 2025-11-22 00:28:00 | METOP-B | PEIXE-BOI | PARÁ | Brasil | 1505601 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f40f1316-7fb2-3dc7-b27c-6d04c095dc7c | -27.84465 | -49.49986 | 2025-11-22 00:47:00 | TERRA_M-M | BOM RETIRO | SANTA CATARINA | Brasil | 4202602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| b5f1c57c-ae2c-3697-9beb-18c91492e19b | -21.04439 | -48.55281 | 2025-11-22 00:49:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| ffc9c16e-27f1-31d3-aeff-0cc2fda0075d | -20.8794 | -52.33637 | 2025-11-22 00:49:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 68196f8a-6063-336a-b950-8250a16117ff | -21.3124 | -48.56005 | 2025-11-22 00:49:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 84bfbd16-a646-3089-bf62-b86468983633 | -21.30243 | -48.56198 | 2025-11-22 00:49:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1ed676f5-ce2d-3da8-a0e7-d7c3c9565f2b | -23.48616 | -51.48567 | 2025-11-22 00:49:00 | TERRA_M-M | ARAPONGAS | PARANÁ | Brasil | 4101507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| bfbf9619-01c8-34ff-b44e-df94d71352ac | -21.31043 | -48.54787 | 2025-11-22 00:49:00 | TERRA_M-M | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d4cf4828-246e-3b63-b868-c208defe37e1 | -21.08807 | -48.63287 | 2025-11-22 00:49:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| bd2efe61-cb3d-3caf-a2e0-5e778dc45450 | -20.88827 | -52.33497 | 2025-11-22 00:49:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 7c315c56-a0bd-31a9-a88b-0b4849d83053 | -20.8807 | -52.34583 | 2025-11-22 00:49:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5400b7a1-3ffd-3c7b-9e46-a2998087c64d | -20.88957 | -52.34443 | 2025-11-22 00:49:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 42a04548-15f2-38b0-b028-490fc51d6d32 | -22.00434 | -49.90946 | 2025-11-22 00:49:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 215f1166-dd16-3d81-aeea-d0b443117ce2 | -22.0059 | -49.91976 | 2025-11-22 00:49:00 | TERRA_M-M | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| 75369f51-5a91-3167-9e02-09629cbca7b2 | -22.11512 | -47.00353 | 2025-11-22 00:49:00 | TERRA_M-M | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 46c8d5e0-bd6c-3edd-8071-ac8d538a7fe0 | -16.77727 | -51.3432 | 2025-11-22 00:49:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 1b3e5bfe-0532-3508-b414-635189c82a65 | -16.77872 | -51.35311 | 2025-11-22 00:49:00 | TERRA_M-M | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d44bf678-264d-31a7-8692-415b4772407f | -16.37294 | -52.6279 | 2025-11-22 00:49:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 24e6319e-b96b-3e41-a40b-d99eaa060c46 | -16.26497 | -52.45243 | 2025-11-22 00:49:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fe2c4744-f76a-3cbd-b784-d0999282127d | -16.37424 | -52.63713 | 2025-11-22 00:49:00 | TERRA_M-M | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c1f14820-f9f2-3d1d-b267-e5ee815684e9 | -4.11411 | -50.0746 | 2025-11-22 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 97e7688f-371d-3483-8912-9b83e67dbd71 | -4.12619 | -50.07291 | 2025-11-22 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| a77d8bac-cbea-38a8-b5e0-bb039be06e2c | 2.54494 | -60.57143 | 2025-11-22 00:54:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f532aa5f-9131-3dc2-85a8-3d9df982de9f | -4.12173 | -50.07925 | 2025-11-22 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| b9afe71a-e8d3-3ba7-bc4a-07312bf8420d | -4.11671 | -50.09187 | 2025-11-22 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| e172194c-fe43-3dcc-b5a9-e4a2edf66b9c | -4.09363 | -48.82206 | 2025-11-22 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 369ff4e2-9771-3ecf-939a-d22d660f2ce9 | -0.99827 | -53.74778 | 2025-11-22 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a51632d1-b536-37d4-b2f3-7309449e61c3 | -3.74923 | -52.0742 | 2025-11-22 00:54:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c9e99dd9-524d-324e-b752-475065c5e0cc | -4.12876 | -50.09007 | 2025-11-22 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0b7bf945-d373-3faf-b769-6d691e2584a9 | -4.11926 | -50.06194 | 2025-11-22 00:54:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 190c1296-7598-3158-ae25-16d8a3fc0e3d | -4.09839 | -48.82722 | 2025-11-22 00:54:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| ad98cb80-7fdd-3072-9d9a-6816234a9e18 | 3.11176 | -60.76189 | 2025-11-22 00:56:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 25.5 |
| a8379174-431e-3df3-b46a-462f79a7daac | 3.11007 | -60.77388 | 2025-11-22 00:56:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c77e069a-020c-33a6-8b52-b3cce5160b33 | -21.3013 | -48.5546 | 2025-11-22 01:09:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 79efdce2-0df9-3868-83dc-0ad52b75a9fb | -16.7749 | -51.352001 | 2025-11-22 01:09:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9fd94f4e-bf08-30da-a023-cb64f5826d9c | -22.004801 | -49.919399 | 2025-11-22 01:09:00 | METOP-C | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a2ad99d4-be49-357f-a141-5a13a86979fd | -20.889299 | -52.347698 | 2025-11-22 01:09:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bef4f2be-7597-3ed5-92e5-c7be8adda3c1 | -20.886 | -52.333 | 2025-11-22 01:09:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 792d8474-35e3-342a-9266-a7359c7c8063 | -20.8876 | -52.340401 | 2025-11-22 01:09:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c952a405-d72f-3767-8688-df8b1dab3708 | -13.2424 | -61.6478 | 2025-11-22 01:09:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 885209de-f7bf-3b21-9243-7a18b31b624a | -16.773001 | -51.344002 | 2025-11-22 01:09:00 | METOP-C | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| cd4c4f96-5d3d-33a9-9b32-507e73071bd6 | -13.2396 | -61.633801 | 2025-11-22 01:09:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 465e43db-96d1-3a88-99ee-d72f50e1832c | -21.311001 | -48.551899 | 2025-11-22 01:09:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 518ebfb8-6dec-3bde-97f5-9a0f4452c18e | -13.2298 | -61.635799 | 2025-11-22 01:09:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3cf495fa-b91e-345d-9545-50116e19f907 | -21.3134 | -48.5616 | 2025-11-22 01:09:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9314b77-3d0a-33a7-878b-de0288214de9 | -21.303699 | -48.564301 | 2025-11-22 01:09:00 | METOP-C | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| e0120a77-42b6-32cc-b129-3aeba4da67e4 | -4.1256 | -50.0802 | 2025-11-22 01:11:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba083bf6-0bc1-355e-8f61-8ca61bde9ffb | -2.9192 | -48.2188 | 2025-11-22 01:11:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 882af759-5c4e-3b1d-aae2-1059a472b3fd | -2.9335 | -48.235699 | 2025-11-22 01:11:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8eda1bb-41a9-315e-ae52-0a97b9166029 | 3.1184 | -60.7565 | 2025-11-22 01:11:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 15fbd457-d255-3061-a8f5-18c46625f256 | -4.1223 | -50.066601 | 2025-11-22 01:11:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dde51d4a-6d99-324f-8a82-459f03f18972 | 2.5422 | -60.571499 | 2025-11-22 01:11:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7cca2265-a5bf-34e8-9770-4fe56d592547 | 3.1167 | -60.764 | 2025-11-22 01:11:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 15ba5bfa-b957-34c1-a425-266800b06c79 | -2.9289 | -48.216499 | 2025-11-22 01:11:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6aa8eb3-b2d4-33e3-b758-f30e73af88f4 | -4.1126 | -50.068901 | 2025-11-22 01:11:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 892ada7a-2afd-343c-b739-1ed15283f568 | -2.9238 | -48.237999 | 2025-11-22 01:11:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64252590-c8ae-39c4-8a7d-45d862b443bd | -4.1192 | -50.096199 | 2025-11-22 01:11:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68430999-740e-374e-afac-c4c94e15b282 | -4.1159 | -50.0825 | 2025-11-22 01:11:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 329d8fd7-701a-3f73-9d1e-df490aa9f94c | 3.115 | -60.771599 | 2025-11-22 01:11:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0baeff45-c225-3c20-814d-59f7274137fe | -3.2756 | -45.4702 | 2025-11-22 01:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| ef562099-cedd-3973-85ad-f0e8b3818e9f | -20.6358 | -47.4322 | 2025-11-22 01:40:00 | GOES-19 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 96.4 |
| ddeea94e-06c7-3421-9f22-dc2ff28b9f33 | -4.038 | -42.5365 | 2025-11-22 01:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 80a6e32d-1df6-39f1-bda1-4f3655dbce26 | -3.2754 | -45.4927 | 2025-11-22 01:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 0ebeec45-7b12-37dd-9cd8-4d58697ac092 | -4.1047 | -50.0857 | 2025-11-22 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| a1736e88-c8bd-3959-8eae-6bcdd0d25868 | -3.257 | -45.4709 | 2025-11-22 01:40:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 798a5236-1384-301c-864d-63860a146526 | -4.1232 | -50.085 | 2025-11-22 01:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| fb5ae071-c36c-3d87-8ac1-0e52aaa05ff7 | -4.1612 | -43.697 | 2025-11-22 01:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 54.7 |


[Clique aqui para ver as próximas entradas](README2.md)
