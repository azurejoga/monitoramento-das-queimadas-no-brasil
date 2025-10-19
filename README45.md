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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06682088-10f7-3999-913a-57c3693e8722 | -9.21986 | -46.05343 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fb4793a-3a8e-3816-9bc6-5dc790891562 | -5.59874 | -46.36227 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1d653b5-9c15-3fa4-a60b-61be6e18dca5 | -11.19833 | -43.99108 | 2025-10-19 04:32:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 471e57db-0f16-3d54-87dd-8485307c5914 | -6.23234 | -44.13737 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f38ac929-a6e5-35f9-afe6-44058bb51dc5 | -5.86289 | -42.35628 | 2025-10-19 04:32:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2bbd0461-e5a5-3c6e-b2eb-9ab46157d823 | -9.21811 | -46.06488 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4ed6b53-9c8f-3934-9edf-34154126fcdb | -7.00426 | -47.42655 | 2025-10-19 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffaf7586-61c2-3642-b5c2-7e27d4ca65db | -5.09809 | -46.13268 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c6871b7-6adf-35a9-ad9e-b8f9871061c6 | -7.81611 | -44.91412 | 2025-10-19 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7413236-1a4b-3fef-ad31-dbde40f5dacf | -8.34732 | -46.21796 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 694d9984-94e5-30a2-898c-bc710a458556 | -11.60538 | -44.05196 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4cdccc60-c711-340a-bb8b-cad16975cfb5 | -8.43056 | -49.59019 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ab8c0f0-1dc8-397f-b260-09e427300814 | -11.65326 | -47.31817 | 2025-10-19 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ff73698-5e92-3633-975b-d3a1ff721a65 | -5.78385 | -47.60534 | 2025-10-19 04:32:00 | NOAA-20 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6bb1f020-645f-387d-b16a-8922feee4ad5 | -8.39718 | -46.23644 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 994dd890-6329-3fec-aa33-04c0c3ae79c2 | -7.16777 | -42.35849 | 2025-10-19 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9bddb567-5d43-3656-80b9-52a0b12c4055 | -11.60791 | -44.06284 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 95daa3ba-c088-349f-a117-5af1ef241056 | -6.14587 | -44.28782 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81f407fb-577b-360f-b1aa-2a6897f566b9 | -10.16401 | -42.21309 | 2025-10-19 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 6c999fd0-871b-3e3d-87ba-4745d2e815af | -5.84883 | -45.7286 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8ff099a-0b35-3c38-8941-0a3aec8d2f6e | -6.5926 | -45.8788 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96f94237-dae4-3f28-b940-4eedcfabce73 | -11.36626 | -49.25413 | 2025-10-19 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ef786302-d156-3dd3-bfcb-a1d2a2f12c5a | -8.07305 | -46.79838 | 2025-10-19 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 01ee2a03-a239-397f-bd86-21a9cf668811 | -9.6813 | -47.45984 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97ddee5c-2ad9-3f9b-af7a-f1dc6a55a384 | -9.24523 | -44.34452 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a9f0503-8e30-345f-91df-9bc094d8be9a | -4.96624 | -56.26924 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f4078db-ec9e-3f96-91d4-22f0fdb4e6f6 | -10.9781 | -42.29436 | 2025-10-19 04:32:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 77fd5904-8974-3856-ad2f-520df1248caa | -7.19371 | -42.18279 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1991fab2-ce2d-3a10-a5e4-7740dec819d2 | -10.6922 | -44.54179 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b20ac72b-e229-3c0e-9d54-8711cda8062e | -10.95278 | -45.47032 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d817b866-8381-3be6-8887-c319eb581256 | -5.49342 | -43.54649 | 2025-10-19 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cb2fcc74-d3a5-3bf3-893e-b6b2536f3dc6 | -5.96185 | -44.19596 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1f6f2e3d-e4c0-304c-ac74-623da4b63ae9 | -5.92663 | -45.45107 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dacb719b-31a4-3820-b96f-4a3a5fb3d104 | -9.91321 | -47.65177 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a52ade78-9fca-34f5-98c8-3e8014397335 | -11.18311 | -47.71315 | 2025-10-19 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 01b8998e-6ad4-3d63-adf6-65e66ba50dda | -5.30178 | -45.32439 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93edac0f-8774-37cd-83e9-38f7788b85fd | -7.62294 | -60.93245 | 2025-10-19 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| ae9e4172-39bc-3488-841b-4556cd98249a | -9.18214 | -61.38684 | 2025-10-19 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 10984ae9-4157-3b56-92bd-ec5092a1d27b | -5.78471 | -45.98771 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ccb1619-3966-32d6-b765-ce92827d95dc | -8.44068 | -44.16776 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 808cef5d-c22e-3c5a-9234-e2af908adc46 | -10.98649 | -47.93327 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 940e1aba-8fe7-3bb2-9709-aa99de0e7144 | -8.34789 | -46.21429 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 09b5dc14-d275-3545-96f1-6d6bd24f5acc | -10.62083 | -48.01302 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a482c1ef-1164-3a53-b8c0-05f29d305714 | -10.56209 | -45.1578 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd9f26c6-4a1f-39c4-9918-c92c1980333d | -5.99335 | -42.79328 | 2025-10-19 04:32:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 43659bc1-3854-3eee-9217-955942c8be8b | -5.54223 | -46.52666 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 34ac22ef-d3ab-38c0-9698-35eec9ccc4e7 | -10.18047 | -44.52943 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b145da-cf17-38eb-848b-b671ad74ab50 | -7.1324 | -44.26101 | 2025-10-19 04:32:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 90b5cfb3-9875-36e1-9304-59c4ecec3655 | -5.59803 | -50.05384 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f70b1e4f-f88a-3d54-8fb4-7e113d9d55e0 | -11.34998 | -44.27941 | 2025-10-19 04:32:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bdeb9e34-48fb-3795-a34c-c1912bdd8537 | -9.26098 | -44.34222 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc5629d1-5679-301f-a72e-4c339dcd5105 | -9.32653 | -46.11242 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cc0083f0-05dc-3126-af33-08511b127ec4 | -8.57867 | -44.58531 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5fb6fd7-912d-3d7d-a45f-dc3d744ce428 | -6.53262 | -47.57484 | 2025-10-19 04:32:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6673f8d-1c57-3f66-9cbd-239a881e1292 | -10.15963 | -42.21247 | 2025-10-19 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 38cfb50e-c80f-30a0-898c-9dea66e0a0a0 | -5.68058 | -47.20338 | 2025-10-19 04:32:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b601fe2c-5769-3b25-b8fb-89c0b335991d | -6.37869 | -45.76688 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3796d8f7-e3eb-3bc3-9485-ff32bc64ce4f | -7.19735 | -42.18724 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 2c5593a8-97db-3678-be89-dc968be60bd6 | -5.17335 | -49.88063 | 2025-10-19 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72781678-fc20-38fd-999a-523b74b161a0 | -11.6514 | -47.32169 | 2025-10-19 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5f45a42-c8ac-3bee-8da6-98673d4123c2 | -4.96485 | -56.27707 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0761a58d-e341-3498-b245-29b5864af0bf | -5.645 | -46.58565 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5857830f-ca13-32f9-a024-468d82dc1ffb | -10.78076 | -40.31624 | 2025-10-19 04:32:00 | NOAA-20 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cb04509c-dc00-3eca-a3af-9fe57527ea1e | -9.18887 | -61.38818 | 2025-10-19 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 884d347c-64e5-36ab-846f-c2c94e32800c | -6.21191 | -44.67327 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a555bd0f-8c37-3dc5-b8bd-d4f1d398684f | -11.61187 | -44.06342 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 392689a5-1e04-37db-9545-ecebe8cfe6c9 | -5.40642 | -46.41541 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5391de77-3d5c-37bc-b1d0-98431d418b4e | -7.19392 | -42.21041 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 86dcb1c3-0518-3409-a984-c8f830eb0544 | -9.22098 | -46.06927 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1c5dabf4-68dc-35b4-a464-988a1864cd7d | -11.65323 | -44.08521 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c9148c59-3e23-3463-a7cd-fdeb06d78619 | -5.64134 | -44.81338 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4d994ade-9b3a-340f-bdf3-f01e3e4faf32 | -8.24295 | -43.9881 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d1970d6-5105-3701-94f4-ccdcedd48041 | -10.88316 | -47.89857 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3594a049-b85c-346b-a6be-3ac1a3a7c470 | -12.56686 | -45.43767 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6794e26d-eba5-3c67-bf81-a77e88548f00 | -5.92722 | -45.44731 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1be837de-6d7e-3dbe-af83-9fe7fcd2e2bb | -5.36783 | -45.27925 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a930e14e-002d-340d-8fb1-f460a4861ac9 | -8.24535 | -43.998 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6f2d0dbd-fb91-3616-90a4-d228aa53b695 | -7.59618 | -46.07062 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 400817e7-b013-36be-9a60-d778d65f38d2 | -10.68326 | -44.55009 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b55732a-cd01-33d1-843c-1508033ae692 | -5.17628 | -46.10867 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f52cf5d0-df20-3964-b007-e38ed2890811 | -5.49437 | -43.54484 | 2025-10-19 04:32:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09896e67-40de-3586-bc8b-f10de3a9800f | -10.41617 | -47.73421 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f53bbf5-7dfb-3586-81c4-26646580ffef | -10.03934 | -59.36516 | 2025-10-19 04:32:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42f221c1-5f73-332e-8199-f0d870fd238a | -9.67796 | -47.45932 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2aa4295-0522-3d19-8ff9-834e6e06ed52 | -11.64064 | -44.08864 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03e64226-3f8c-32dd-a342-a422ad411a29 | -10.15525 | -42.21186 | 2025-10-19 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2c3dddd7-48ab-3536-b49e-2bfb61ffaff5 | -5.16956 | -46.10764 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3ad2ffc5-5806-3974-b9b3-67fd284571fc | -6.74007 | -44.28939 | 2025-10-19 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 289d2a6c-b3e0-36dc-ba6c-426706516d8d | -7.44963 | -46.52635 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7031549f-07cb-3ca1-be83-55171f62f130 | -5.9478 | -42.23112 | 2025-10-19 04:32:00 | NOAA-20 | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0a1643aa-765a-377e-aa88-90b8e8fad146 | -7.184 | -39.67254 | 2025-10-19 04:32:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e465caf9-46f6-368f-a599-c44bae4a5ee2 | -8.56382 | -48.1362 | 2025-10-19 04:32:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93b52099-e4b3-32c0-b315-929a935025a8 | -5.89251 | -46.69598 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 672cb835-4ddc-3578-9516-eccb3b700076 | -8.4489 | -44.1642 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 271b748f-0eeb-3b43-9cb8-af4c41d91f97 | -12.45644 | -45.42762 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 671b78d3-b241-3baf-a106-5faad69439bb | -10.13131 | -44.52281 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35ba85a7-18b3-3b9d-aa1c-ed070cffcaab | -9.90434 | -45.95835 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5d2e768f-f609-398f-b4b5-cfbd48db9c51 | -6.10611 | -44.84768 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8f464846-7d0d-3bac-9ac9-bd23344185ae | -11.77777 | -49.57114 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a6b6724-82ec-3d61-b507-ce5c3c5733d5 | -7.18803 | -42.2213 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |


[Clique aqui para ver as próximas entradas](README46.md)
