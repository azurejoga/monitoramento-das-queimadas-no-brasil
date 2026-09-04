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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dfa088a3-de5a-3ea9-abf9-f348ad94501a | -17.09574 | -56.86718 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| eb7eeb25-603f-3048-b567-cf6558313e41 | -17.09627 | -56.86151 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cabd2d97-bf59-32a3-b4ba-07bcfca4c848 | -17.10551 | -56.85115 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| cf924daa-ef69-3963-9d8c-44cea80dfdcd | -17.10494 | -56.8568 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 05e23302-dba9-3d16-a0da-97e5d1966ab7 | -17.09897 | -56.85044 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5389774e-bff0-3d7c-92bd-13fb468c076c | -17.10282 | -56.86221 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1a325471-bd60-36da-9d60-46c080e45277 | -17.10335 | -56.85655 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 19ca7ece-6058-3bc5-b40f-9abc9c264d25 | -17.09725 | -56.86741 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 68302b03-813c-3c5f-b6c9-acc55ba0de7a | -17.09735 | -56.85015 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9a424a1e-4bbe-31fb-aafa-3843ca44127d | -17.09681 | -56.85583 | 2026-09-04 06:03:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f72a8693-f49c-35c4-84fe-366c9150b63b | -5.5983 | -43.98764 | 2026-09-04 06:05:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b7294a54-8b0f-3ac9-8aef-b351b577e7ea | -7.12572 | -42.24178 | 2026-09-04 06:05:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 9656e069-6d3d-3e41-8427-553054b65a91 | -7.11258 | -42.25426 | 2026-09-04 06:05:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| b7cb82ac-33c6-33b8-a57f-910844a7c820 | -5.58542 | -43.98546 | 2026-09-04 06:05:00 | AQUA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 4f794da4-0846-3b1a-ab7f-935eba5f2113 | -7.11483 | -42.24007 | 2026-09-04 06:05:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 24.0 |
| bd128ce7-9534-348e-9987-8d0930f1f9b5 | -12.98925 | -44.11324 | 2026-09-04 06:08:00 | AQUA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6dcb60ff-2ebe-3fe2-a3b5-50cb42ca67e4 | -13.40107 | -41.88272 | 2026-09-04 06:08:00 | AQUA_M-M | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 40501d0f-f157-3dba-9c46-65b606fb7dc8 | -14.90514 | -44.67633 | 2026-09-04 06:08:00 | AQUA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 1258b7b7-d765-30e0-b5a7-9aad2fa76310 | -7.59244 | -44.73992 | 2026-09-04 06:08:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| fc36f959-211c-35e9-817f-ed0bd6b922f1 | -9.00942 | -40.99606 | 2026-09-04 06:08:00 | AQUA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| ed77bae6-9d74-3c3a-a3c6-d7e1b768c3cc | -6.6881 | -59.982 | 2026-09-04 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 141.1 |
| c4634756-2a51-3b2c-96c6-1d317ef992d0 | -8.6101 | -67.1969 | 2026-09-04 06:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 5ad4e7cc-86b8-35d8-9230-52c2ca3c753c | -6.6697 | -59.9635 | 2026-09-04 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2ca00508-437d-3622-9fd4-cef2d1406add | -8.5916 | -67.1788 | 2026-09-04 06:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 2c8c9d9f-cfe0-3580-8693-80324ed2d10a | -6.6882 | -59.9628 | 2026-09-04 06:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 207aa28a-1a3a-3051-a4fe-a4c703f0e675 | -8.6101 | -67.1783 | 2026-09-04 06:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 3aafa836-344d-3bd5-bb5a-a6faaf18b050 | -18.51984 | -48.18433 | 2026-09-04 06:10:00 | AQUA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 37.9 |
| a83c24c6-b220-36e8-bc7b-ccf50eef8df6 | -16.65894 | -43.63408 | 2026-09-04 06:10:00 | AQUA_M-M | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 820bb5a6-812e-378e-8516-010ba09b9d9a | -3.01994 | -61.48372 | 2026-09-04 06:18:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 412de3f0-f5de-33c2-9580-a7c24d8e4db2 | -3.07966 | -61.09032 | 2026-09-04 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47e35241-d07e-3934-8952-26aaef775abe | -3.61607 | -60.57335 | 2026-09-04 06:18:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 605b613f-2267-3853-b5dc-4e2315f05c5f | -3.01974 | -61.48582 | 2026-09-04 06:18:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44327aee-1b38-3f4e-b360-3dec02b81c32 | -3.21568 | -61.17613 | 2026-09-04 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0ca1d710-f3ab-3143-a703-c2030aa35c12 | -3.07179 | -61.08109 | 2026-09-04 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| af662ef4-44d9-37f5-b297-3702dde4a684 | -3.01852 | -61.49307 | 2026-09-04 06:18:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22c9b57c-bc86-32d0-82e8-90ae5e632f4f | -3.61038 | -60.56691 | 2026-09-04 06:18:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e65803db-34c6-31ad-9ac3-6bd08136a179 | -3.07108 | -61.08602 | 2026-09-04 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7e94294-f551-3e41-bbbd-ff41b01d5417 | -3.07867 | -61.18093 | 2026-09-04 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8b16300-f790-3981-af6c-46b27d1d6555 | -3.02464 | -61.49393 | 2026-09-04 06:18:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 937df90d-5909-31fd-8597-02f2e7148752 | -3.07411 | -61.08461 | 2026-09-04 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 599ecfc5-9e05-3619-b54e-5a1d042ce4a6 | -3.61603 | -60.56896 | 2026-09-04 06:18:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e16fe6f-55f5-3613-9cf1-70fded30e4cb | -3.6169 | -60.56784 | 2026-09-04 06:18:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 578551bb-d554-3895-a7b1-efa4fcdefa79 | -3.01923 | -61.4884 | 2026-09-04 06:18:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02367e8a-9a06-3501-a3b6-0783c82a5ff1 | -3.07792 | -61.18583 | 2026-09-04 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13a5dec9-2ed6-3ebd-80e4-f4aab2fefbd3 | -3.01906 | -61.49051 | 2026-09-04 06:18:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0450b4e-4037-3efc-bb48-278d3cb3ebfa | -3.07486 | -61.07969 | 2026-09-04 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81037ad1-97a3-3606-ae7f-bd61d99bd43c | -3.07737 | -61.08684 | 2026-09-04 06:18:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0017ecfb-38dd-3655-9a8e-a613512c55a7 | -3.60951 | -60.56799 | 2026-09-04 06:18:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a633887d-a12c-3fe8-9133-5809cd0f7d02 | -8.5916 | -67.1788 | 2026-09-04 06:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 23cf2b8e-7960-3624-a3fd-54ec6204c8e8 | -6.6881 | -59.982 | 2026-09-04 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 119.3 |
| 949a5edf-ee74-3d40-9fcd-2729ca49d47c | -6.6882 | -59.9628 | 2026-09-04 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 2a482805-ac12-36be-8e20-2a8a8cfacad1 | -6.6697 | -59.9635 | 2026-09-04 06:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| cb84fa3c-dbbb-305e-81f4-d95e2cdf201f | -8.6101 | -67.1969 | 2026-09-04 06:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.0 |
| b3566a1d-c248-3d6b-a7ff-a807279a7e88 | -8.6101 | -67.1783 | 2026-09-04 06:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 87f90bee-1e2e-366f-83b5-fc13d8271ceb | -8.87412 | -68.61177 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2de4e71b-6b23-3c91-a221-f5fcb7ed9946 | -9.53469 | -63.5646 | 2026-09-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 14a03447-fd47-35b4-a5db-adbc103eb212 | -6.70741 | -62.86385 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1551fb9c-1458-32bb-978a-1f8570724d5f | -7.79228 | -66.96007 | 2026-09-04 06:20:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5470f09a-eda9-3876-a1db-0cc7d6bdb106 | -9.04499 | -65.73637 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b077a9c9-063e-37bd-a8b6-33c17b527b77 | -9.11178 | -65.49876 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e70904b0-00f1-3f43-94a9-36162fd46a35 | -3.77589 | -61.75578 | 2026-09-04 06:20:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3faa7e34-3713-36a5-9cff-b297f45bb9bf | -6.97518 | -71.65993 | 2026-09-04 06:20:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f0626140-92a9-367c-97e3-e5ff403608b5 | -8.98995 | -67.02553 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b56bde13-1f76-3313-adc6-0044b528016a | -7.01669 | -62.98315 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 356cb0aa-c5fc-3ab4-91df-523bcd204da7 | -3.75623 | -61.75433 | 2026-09-04 06:20:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 928ef758-27ec-3337-94bf-ac5e5945f655 | -9.03997 | -65.73559 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c616f8a2-de8f-3d01-ab70-17ecfa1dd5a1 | -7.74517 | -70.54618 | 2026-09-04 06:20:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e824975f-0866-3e46-af39-b84a5db3a381 | -6.67441 | -59.94796 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48fcf1fb-7453-33b7-9eb6-e09d82341863 | -10.28923 | -68.84762 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c2b85927-bbd6-302f-b47e-6066fd0329f5 | -7.83561 | -73.08579 | 2026-09-04 06:20:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cd4018c-3197-3b29-966c-d8a236d98256 | -8.16925 | -62.7761 | 2026-09-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7354442f-3533-3653-90fe-237ea0d60e00 | -10.28402 | -68.85459 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b6697f1-e372-3b03-99de-3ba92a60c36b | -10.28254 | -68.8351 | 2026-09-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52ff759b-9800-3e9e-9219-b69844792209 | -3.75634 | -61.76226 | 2026-09-04 06:20:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eef3fdde-90df-3641-a862-ea52fc94072b | -6.68328 | -59.98924 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 6b524344-7232-35fd-acb8-3aa4f54c279b | -8.8736 | -68.61552 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7d9f1ab0-d127-3c3d-bc0f-3dfa56f274ee | -6.66971 | -59.94744 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f06fc622-8472-3c64-b3c8-cf49bb046214 | -8.52163 | -67.1597 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a49a3441-734b-39fe-97ae-6873b1dffb10 | -7.01555 | -62.99158 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecca47e0-290c-3918-90ea-b053b9a8fa4c | -9.16019 | -68.53308 | 2026-09-04 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 050f2e81-2cb2-3c3d-89f5-4652f40452d4 | -6.70151 | -62.86301 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4221d7fe-0997-3df7-a7c9-c745525e5068 | -8.52097 | -67.16428 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d8202f53-2e35-32c2-8740-506e2536a5b4 | -6.70682 | -62.86813 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88f1fe8d-b2de-32fc-b756-2d9a045decb2 | -6.68063 | -59.95517 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 072b5318-6f1c-34b6-acdb-de0cb7c841d2 | -8.86999 | -68.61121 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 215774e6-0641-3928-9e4e-954b4b4ee48c | -8.87147 | -68.49728 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b53cef3-bcac-3fad-b10b-e93e35db30eb | -6.68414 | -59.98274 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| bf436cf3-9de4-37ff-abbb-8dd9df566b20 | -9.03535 | -65.73187 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a3c976e-cb67-3a9c-b83a-1efa8b543b41 | -9.04963 | -65.73989 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2c23349-1c85-3195-aa61-13a22f6b8729 | -9.10666 | -65.49799 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3255b723-2526-39f1-a9df-ca075de3cabf | -8.70992 | -62.95034 | 2026-09-04 06:20:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 642a2d07-5545-3319-b094-99dc314f4813 | -8.89784 | -68.88412 | 2026-09-04 06:20:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bf6edf7-99c8-3ff2-95fd-2d4c2fa9c81d | -6.99148 | -62.99257 | 2026-09-04 06:20:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7da4890-e662-3aae-8b09-13e2c2d99dce | -3.75554 | -61.75889 | 2026-09-04 06:20:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2cfbc0f0-7c3e-3baa-9e59-20606fe0fe14 | -8.87203 | -68.49348 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9831832-9873-363f-a46e-df0c5867e637 | -3.78196 | -61.75667 | 2026-09-04 06:20:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ef5348f-befd-3543-8899-899f88a2181f | -6.67886 | -59.96858 | 2026-09-04 06:20:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| df5502cb-df71-324e-ac3c-868fb26f4039 | -9.04459 | -65.73928 | 2026-09-04 06:20:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc9c7ce6-cd99-3c4c-b65d-56ae1698fe81 | -7.74486 | -67.06533 | 2026-09-04 06:20:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5461cb8f-5447-3316-9d7e-4d4dd543229e | -8.60421 | -67.17422 | 2026-09-04 06:20:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |


[Clique aqui para ver as próximas entradas](README38.md)
