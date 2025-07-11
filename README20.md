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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab85e0c7-6dd9-3ed0-bce0-90a2f64fe5f0 | -11.33364 | -45.21848 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70e0aa63-54b3-356a-839c-bb8401993e3b | -9.96575 | -64.9498 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 77d32bed-7697-3930-aa24-f740e12c579e | -9.25819 | -57.79989 | 2025-07-11 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d7005b0-d439-384a-9e2b-1af640508f38 | -13.15328 | -47.29353 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 94656ce0-3654-3195-8bbf-5ba5f73f7ac3 | -9.9644 | -64.95712 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 93fa59ca-aed2-3af1-9c95-810913c56a3e | -10.80566 | -62.00196 | 2025-07-11 04:59:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29460333-b072-3f39-a861-705685f313b8 | -11.43997 | -45.12007 | 2025-07-11 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a10dae6-25f0-3891-909e-254802c61468 | -10.74557 | -49.84699 | 2025-07-11 04:59:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31b0f6bb-9d45-38e3-91bf-5a22ccb8db53 | -11.87652 | -58.71497 | 2025-07-11 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8672bd5-b54f-37ef-ab73-43e4711dc974 | -13.14484 | -47.278 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea360589-0319-3bec-9179-08b56a555881 | -14.39283 | -43.77062 | 2025-07-11 04:59:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58188060-4b7c-36b8-bb72-ad3a073eaaea | -11.57467 | -47.43137 | 2025-07-11 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f2021678-88e6-36d1-be66-81d97ee855f7 | -10.3544 | -49.91608 | 2025-07-11 04:59:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab24ce74-2558-3cee-bb14-57f2888f1695 | -12.02836 | -49.52063 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db7c87d8-3ff5-35f2-9f71-dd101d3a42a6 | -11.78777 | -57.24039 | 2025-07-11 04:59:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ee1acdc-1564-31a1-8bfe-432da3dc0158 | -13.13926 | -47.28122 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18fb727c-534a-3d8d-8dca-92d8f9aa6a52 | -12.0919 | -64.24579 | 2025-07-11 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2523f2ed-98af-3b9c-a47a-5fb5df0855ae | -9.92557 | -59.90252 | 2025-07-11 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8001c821-6f13-3d41-bbc1-b8ebf6441cbf | -16.0412 | -43.72741 | 2025-07-11 04:59:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c0bfc8cb-938b-3209-b9b8-5e650087508d | -14.39226 | -43.77612 | 2025-07-11 04:59:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f88bf3f-bfbc-316c-80b3-7867bcb7db2e | -13.17418 | -47.29203 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f45312e-e56c-386d-adf7-7d1b5d269afd | -9.96989 | -64.95815 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24d1b58e-09cc-3823-a766-ed0da83a8d98 | -9.86158 | -60.29411 | 2025-07-11 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cd0ed9c-5d4c-35ad-8d14-5db0b63af3dd | -13.14224 | -47.29918 | 2025-07-11 04:59:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ea3a552-58dc-3cca-9032-c9a6b0931c29 | -11.86647 | -58.70902 | 2025-07-11 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47e4c9ed-f82f-37ef-af1c-f316b06f5af9 | -12.0958 | -64.25276 | 2025-07-11 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79b42338-b1ad-324a-93ae-53736f46bf0f | -13.00062 | -46.28018 | 2025-07-11 04:59:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ae2455f-e98e-368d-b594-a72f880e715a | -11.32444 | -55.21291 | 2025-07-11 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d6f4db0d-dee6-388f-a56e-9d51d1782c04 | -10.84482 | -49.11486 | 2025-07-11 04:59:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 03c8b81e-67d6-3d0d-ae46-8e63a9d46489 | -11.33316 | -45.22248 | 2025-07-11 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8762e84-60ef-34ef-956a-eb37f1bb8985 | -9.47465 | -57.32679 | 2025-07-11 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19d64530-66b1-3009-ae93-86d9b1a75024 | -13.00484 | -44.85988 | 2025-07-11 04:59:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dcf5d862-9af1-3562-affc-2ec0e3a6eb27 | -12.09133 | -64.24879 | 2025-07-11 04:59:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0c9b89a-37d0-312c-a6c2-2c36242e4f6a | -11.3303 | -51.44297 | 2025-07-11 04:59:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0198c8ce-3fa6-3ce8-90f6-a5466e340710 | -11.82883 | -48.21094 | 2025-07-11 04:59:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 25e80d02-492b-37a0-ac04-0d945322957b | -13.86801 | -45.87302 | 2025-07-11 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf10f23c-1c2b-3e8d-acc6-bc4ec9099a19 | -9.96373 | -64.96075 | 2025-07-11 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8c08dde-064f-3f7e-83b1-912322bb415f | -10.58283 | -49.13231 | 2025-07-11 04:59:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 92bac376-4b42-3ba5-bc6e-1a8399f77dde | -11.87581 | -58.71916 | 2025-07-11 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d71ef567-6cf1-3d3f-8ec4-20aa197ad01c | -12.05671 | -48.54612 | 2025-07-11 04:59:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0084b745-c650-32f6-b1fc-67bc536ca326 | -14.73475 | -48.4024 | 2025-07-11 04:59:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 684c7a45-907d-31e7-ba51-9358472dfef9 | -5.5614 | -43.9082 | 2025-07-11 05:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| f3c0f723-8c21-3f6a-b89b-7c8dada01b73 | -9.9148 | -47.8282 | 2025-07-11 05:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 2bd56a99-e509-3503-be8e-a89c21a89dbf | -5.5429 | -43.8864 | 2025-07-11 05:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| e563ec08-cf36-3f2a-8c0e-d3981ae9d3c3 | -10.6672 | -49.4895 | 2025-07-11 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 4cf9f449-a144-32ec-a5ca-b55b3c63c5dc | -10.6862 | -49.4874 | 2025-07-11 05:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 44c8c1e0-cab8-347b-8a2d-e6e72f262f63 | -5.5427 | -43.9096 | 2025-07-11 05:00:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6e920f13-932e-3d0c-9778-4583945831c6 | -19.44766 | -48.53922 | 2025-07-11 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a3e6e016-67c5-38a0-bc10-b8a901f82cb0 | -21.19283 | -55.69456 | 2025-07-11 05:01:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4aaacb0-235b-3f90-939f-17f3ef0e7ec1 | -21.69034 | -49.4982 | 2025-07-11 05:01:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| a04e052a-4636-3550-9e41-3aad7c12be8f | -21.68542 | -49.49754 | 2025-07-11 05:01:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| cb876030-e097-319b-ab01-6216188ee398 | -18.42455 | -54.55932 | 2025-07-11 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bce06e9a-05d6-3130-a2d9-2f8b73625989 | -19.44799 | -48.53625 | 2025-07-11 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 55b434b7-59d7-3ffe-960a-1d4169dfab58 | -17.68378 | -52.9004 | 2025-07-11 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b12c8c9-567a-3863-a5db-ea3c2df8a0f3 | -21.53597 | -49.52555 | 2025-07-11 05:01:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ae739428-de3d-338e-bf59-d525a584b17c | -18.97277 | -54.38459 | 2025-07-11 05:01:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77829c02-a34d-3a90-aa32-898b3a17f716 | -18.65532 | -55.72213 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b4c5b422-6623-305e-bd05-5926d43c80f5 | -18.66207 | -55.72323 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 59d0729f-de04-3c36-8cb1-c22c4e903a4c | -19.08994 | -56.04567 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3a9ba4b6-b478-3757-b29f-dce19edd4668 | -22.3112 | -49.1388 | 2025-07-11 05:01:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ae2193d-8c66-3b89-8ae7-8298f2ef3fa6 | -21.89874 | -56.73582 | 2025-07-11 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cf1948cb-56d2-3ab9-8062-2b02f8a1caab | -19.08658 | -56.04511 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fcbd854d-605e-3237-8454-e6b16bc52455 | -18.66151 | -55.72701 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 7175862a-385d-31b9-81f2-40d32f7a799b | -22.54007 | -48.81257 | 2025-07-11 05:01:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01a4a2ec-797b-3ffd-990d-d3882fcb341c | -19.45107 | -48.53879 | 2025-07-11 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbdb2d6b-d493-3b33-890d-fe857e2b0a81 | -21.68719 | -49.49905 | 2025-07-11 05:01:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| a891ad54-9539-3e30-8aed-d4230d825533 | -20.32603 | -55.00513 | 2025-07-11 05:01:00 | NOAA-21 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9e77560-f177-304f-bbb0-3fda70430c51 | -21.89538 | -56.73525 | 2025-07-11 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5cd26142-dc34-3ea6-a5d5-1bd6d158899d | -18.97219 | -54.38876 | 2025-07-11 05:01:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 866da7f2-14a5-32ab-aba2-bdb41a9691ce | -18.66544 | -55.72379 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| da72eddd-a242-3ceb-a72e-b7da36cf70f7 | -18.9698 | -54.37986 | 2025-07-11 05:01:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1deb5f6c-ae72-3d13-aa90-941f9e6f093a | -18.97039 | -54.37566 | 2025-07-11 05:01:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 820a7ccc-a8a5-348b-81cd-34264aecca31 | -19.08937 | -56.04941 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e8a60210-4a70-31ae-8534-684577895607 | -18.42804 | -54.5599 | 2025-07-11 05:01:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f37716b5-fab4-39ff-9be1-b2bafa9a9f61 | -19.44626 | -48.53534 | 2025-07-11 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1cbf43d-9b6d-300c-90b8-43385b32ccef | -18.66488 | -55.72756 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9f129027-93af-3c13-9f63-139b2c5dbc10 | -22.27534 | -54.9486 | 2025-07-11 05:01:00 | NOAA-21 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50210764-039f-3a0d-8250-0de45e8db33c | -19.08602 | -56.04886 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 5c5190fd-a647-3dde-a12e-c53648dcec8e | -19.09329 | -56.04622 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 996cf2d2-4759-3aa0-9cd5-0397f05b98cd | -18.30765 | -52.41663 | 2025-07-11 05:01:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7b762602-7f5b-3a3d-a66a-371186e9d2e5 | -18.6525 | -55.71779 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 33d6b8d3-1b87-3ec0-b14b-cc742f0ab628 | -18.65083 | -55.72912 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d197acc9-af7e-3d0b-ba3c-c924cc1fee66 | -19.44595 | -48.53835 | 2025-07-11 05:01:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd1feea9-75b7-354f-896e-d5149dd2da8b | -17.59802 | -52.49873 | 2025-07-11 05:01:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 39f2c9b2-7da4-356d-bd9f-febbe0b91f97 | -18.88357 | -49.05276 | 2025-07-11 05:01:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f92e875-58d4-3ad1-b727-4cfdb2b65631 | -21.83119 | -56.26639 | 2025-07-11 05:01:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d23a1d25-85ef-38be-80f7-158a13165f48 | -20.47793 | -53.6756 | 2025-07-11 05:01:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1caa89e1-930d-30a7-9875-b8c328c835b9 | -19.02419 | -57.62172 | 2025-07-11 05:01:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9087b280-dd30-3b55-8d2a-8be8566fd47d | -20.70803 | -56.66302 | 2025-07-11 05:01:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 807666cb-6595-34b3-85d9-514edf974927 | -18.65028 | -55.7329 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8eae49d3-a174-33f5-aa13-cd3ac082cf8e | -21.32287 | -44.23382 | 2025-07-11 05:01:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f05a5fa0-61c7-3b7d-b048-945c0d316510 | -18.65195 | -55.72157 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 8c017b61-b3ef-3fb6-a1a5-7d81ef40b2ec | -18.64857 | -55.72102 | 2025-07-11 05:01:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 638de12c-1a82-3fc3-b8ca-46efd05183b4 | -15.50283 | -56.30926 | 2025-07-11 05:01:00 | NOAA-21 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 71ab329b-c014-318f-b0ad-6c0a14ca6e0a | -19.97491 | -54.33955 | 2025-07-11 05:01:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0124a92b-9eb2-384b-9433-ddcf5c62c193 | -22.31629 | -49.13941 | 2025-07-11 05:01:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ff5aea9-55f4-37e5-99fd-a4c2b59073ac | -21.68777 | -49.49323 | 2025-07-11 05:01:00 | NOAA-21 | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| e260856c-3283-39b6-b3ae-db1d4fd19ada | -21.32039 | -44.2364 | 2025-07-11 05:01:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d2958eb2-974d-3b74-b114-ef3d9a4ec006 | -24.31703 | -50.84885 | 2025-07-11 05:04:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c5a3363f-470c-3836-aa8e-fe9d9f4180f2 | -24.31917 | -50.85494 | 2025-07-11 05:04:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README21.md)
