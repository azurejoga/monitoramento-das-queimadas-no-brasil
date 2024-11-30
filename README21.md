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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b07e27f5-09a9-38ef-a33b-a75325528837 | -6.85106 | -38.79115 | 2024-11-30 03:46:00 | NOAA-20 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c2a4465b-4fc7-31ef-9fca-39d38aa41d8e | -2.27192 | -46.42719 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 881c28a3-712c-3d8d-beb1-8a8c22bfb114 | -4.85654 | -41.27379 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 8e016f1b-a234-343b-81a2-2bb6486cc999 | -2.96019 | -48.03658 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c4b2853-0c75-32c0-be8b-250b87fd8cc0 | -2.71635 | -47.55405 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b89b7135-aa1f-34a3-8b1c-bd3f5c1bd13a | -3.94349 | -41.49328 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c093263a-2259-3054-8ded-89066d0d059b | -3.01258 | -45.10435 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6e8f7965-afb2-382e-a32d-03f03cca217f | -4.00877 | -46.94691 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03533cd2-e0e4-3d7c-a337-331151d6007c | -2.3129 | -49.07587 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb3afcce-b1b8-3939-b68c-89005bbfbb89 | -5.38603 | -42.96062 | 2024-11-30 03:46:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a00af5cb-ee54-3623-86cb-f66f71decc2a | -7.19521 | -37.52533 | 2024-11-30 03:46:00 | NOAA-20 | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 04a1d1f7-71bb-32f2-a648-9958590035fc | -3.03456 | -45.12194 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72516b22-7ebb-3f3c-b6b4-fc36d8d942a2 | -3.28135 | -45.57212 | 2024-11-30 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c75eab4-c98c-3f0b-96e0-af3dfda95142 | -5.07687 | -44.98795 | 2024-11-30 03:46:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 125b3ab6-73d2-3b75-87ce-4904f1b4f965 | -4.83245 | -41.28578 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| da754a26-f4ad-3b58-8737-4f21566dc74f | -2.67792 | -46.10266 | 2024-11-30 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b7fe4db-b5c4-3414-9578-e265d532799a | -4.41767 | -46.14703 | 2024-11-30 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7cf7bd5-905a-3dd3-90c4-14ae9bdeb573 | -6.12464 | -44.92459 | 2024-11-30 03:46:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29979d4f-3fc1-33e6-bf92-70d633ac20a9 | -6.94562 | -42.78377 | 2024-11-30 03:46:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cb03745f-1468-35eb-871d-f4713fef65d4 | -3.96807 | -41.52396 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a25be0d0-551f-3179-b3eb-3dd91b9617ac | -4.01542 | -42.52057 | 2024-11-30 03:46:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6e872087-d053-301a-a1a3-e1b4c0cc6eaf | -5.66496 | -39.92271 | 2024-11-30 03:46:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4d6cbcbe-24e2-32a9-a89c-f08b8075d3b9 | -3.47074 | -41.56448 | 2024-11-30 03:46:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| abd80eb9-ffd9-34c1-9aa7-7556aa44f5d6 | -6.68103 | -39.26236 | 2024-11-30 03:46:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 068c77e8-caf6-3cf0-989c-ffd7da500f55 | -4.68512 | -42.37561 | 2024-11-30 03:46:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d8854961-af44-3a4c-b902-2f603c26b5aa | -3.97158 | -41.52838 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| e685953f-297c-3eb2-a273-3c09895f870e | -4.87521 | -41.31023 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 1c3d9b3e-8a71-3b39-b752-78483abdac32 | -3.68095 | -44.70446 | 2024-11-30 03:46:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1816647d-774f-3dee-9a07-ae7b52cc2ca6 | -4.35939 | -43.69516 | 2024-11-30 03:46:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c03055b-3c23-381d-9278-4fcf03677f78 | -2.24388 | -48.25725 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18dc4081-16cf-3909-b103-10461fb1e483 | -5.42101 | -44.85566 | 2024-11-30 03:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa3f392e-0b88-3bc7-ae29-c09cc53a0ed1 | -2.45818 | -46.57411 | 2024-11-30 03:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a6741cb-e7fb-3080-a01d-9311889d4368 | -5.4205 | -44.85854 | 2024-11-30 03:46:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 275345ad-8e6a-381f-9cc8-c0943540028c | -3.13823 | -45.98722 | 2024-11-30 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb8fa22e-c4ad-32c2-b83c-226db636347e | -2.94735 | -47.99569 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afac5edd-f68e-3e89-af58-93e0a3bd8319 | -2.27379 | -46.42831 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b87dc82-1282-33f0-96a9-a3674db4e308 | -7.28418 | -39.1025 | 2024-11-30 03:46:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7a02f50f-ea3e-3b5c-b9fb-e1bd69dc690d | -6.92412 | -45.20644 | 2024-11-30 03:46:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b1463bc0-b1b2-324f-af17-2ece2e36a601 | -4.88028 | -41.30445 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| b9ebcb6e-a889-36e2-9100-5e71705d2402 | -4.86387 | -41.30402 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 51533cbe-2892-302f-b63d-f9b1e793ff2a | -4.58952 | -44.71014 | 2024-11-30 03:46:00 | NOAA-20 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c686fb53-fb14-3bbd-a513-08aaf3b6c4ec | -9.90501 | -38.11146 | 2024-11-30 03:46:00 | NOAA-20 | PEDRO ALEXANDRE | BAHIA | Brasil | 2924207 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e670a52-7978-3cbb-a9b4-91414a31c33f | -4.85592 | -41.30223 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 47de4841-b5a2-3f82-947b-ded5c26e438f | -5.50724 | -46.25853 | 2024-11-30 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5824037d-dd59-320a-a3b8-5f39a32fdfc2 | -4.86949 | -41.27014 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| b55c6679-100d-3bb1-b3c0-6be61ab66cee | -4.86554 | -41.29389 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44ea37e4-3d05-3399-a929-f95f4e0eb005 | -6.79196 | -39.45219 | 2024-11-30 03:46:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 27a82679-a5b8-36cb-ad24-ab0ba61add2d | -6.03082 | -39.36395 | 2024-11-30 03:46:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 60005f97-9d21-3a81-b7b5-309ba90c8c5a | -6.70016 | -47.27061 | 2024-11-30 03:46:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e11013e-ab37-3600-a611-a0cb61826734 | -4.28944 | -44.10865 | 2024-11-30 03:46:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbdcf785-59e8-388d-899b-b9bd0bd27ebb | -3.32979 | -44.00701 | 2024-11-30 03:46:00 | NOAA-20 | PRESIDENTE VARGAS | MARANHÃO | Brasil | 2109304 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d0374298-cf2d-3b3c-a17c-5d736431cdf8 | -5.1245 | -45.15623 | 2024-11-30 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 168ee578-9bce-3fbf-bee1-0f11f961b49f | -7.21767 | -39.06142 | 2024-11-30 03:46:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ed686d58-c4ed-3b6f-bc97-37ef0cb14b09 | -4.84948 | -41.31612 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| f2c01c57-1985-3550-819b-5ee648557feb | -6.25547 | -44.97293 | 2024-11-30 03:46:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f1fd4e15-fe26-355c-9846-81be076afa77 | -4.6778 | -46.37595 | 2024-11-30 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e4820536-b2f3-31d7-bd57-f5f5244a4445 | -7.43173 | -35.12433 | 2024-11-30 03:46:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 270e9d43-92e3-3191-9308-3e1ce53854c1 | -2.37216 | -47.88604 | 2024-11-30 03:46:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a674fa50-62fc-3142-8156-56f448b582f3 | -6.13482 | -43.95389 | 2024-11-30 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ba969293-0f21-387c-a1c2-c9ef9495c5f8 | -5.04026 | -43.62006 | 2024-11-30 03:46:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 506e5c29-d8e6-309b-b4da-fad14ace939c | -5.87699 | -42.32782 | 2024-11-30 03:46:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a42d2330-5953-3490-82b7-93445e70e703 | -4.56486 | -38.4812 | 2024-11-30 03:46:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 8dc1b567-61d7-35de-9800-f438698a6060 | -5.73019 | -43.77632 | 2024-11-30 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6f741ab6-342d-3c84-906a-e7874b076850 | -4.6109 | -47.00832 | 2024-11-30 03:46:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e8e7dfc-3145-3931-b54c-a20164b1b3ae | -2.14442 | -46.49245 | 2024-11-30 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52c7e730-a6d3-3a97-871e-5e7d79154e15 | -1.68958 | -46.78131 | 2024-11-30 03:46:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 59b13317-33f8-3f96-a3ed-7d2cf8e0b111 | -9.14125 | -35.78252 | 2024-11-30 03:46:00 | NOAA-20 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1c6a0f11-3794-396a-a2d9-b296943891b5 | -6.36108 | -39.69627 | 2024-11-30 03:46:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e43f732b-6d68-3aeb-8966-8b9cae7125ee | -3.51257 | -42.17956 | 2024-11-30 03:46:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a3efb047-ddee-3dbc-8808-f66911365757 | -2.45889 | -46.56968 | 2024-11-30 03:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 172f6204-dd09-3c40-a7fc-a999d4279b68 | -6.91665 | -43.54402 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| acb1f45f-3343-397b-852d-be4d35a37fff | -3.94761 | -41.49396 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e330e360-1505-3cd8-8729-d1d3b3185df2 | -3.28196 | -45.56854 | 2024-11-30 03:46:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8052abbd-cb94-3032-b3b5-d6e8e3c27376 | -4.95597 | -37.03483 | 2024-11-30 03:46:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| dcb18232-59cb-3a03-867c-d4b8f4402cb6 | -2.52066 | -48.47054 | 2024-11-30 03:46:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aa854029-874b-3a65-9339-708d6a713b28 | -4.16018 | -38.69551 | 2024-11-30 03:46:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 2b0684a0-3400-30f8-a680-7c370f3f3bd6 | -7.8606 | -45.92466 | 2024-11-30 03:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e9c0fae4-657b-3079-8d7d-db7acfe06cf8 | -4.0788 | -47.02127 | 2024-11-30 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e779cdc9-483c-3251-a7c0-833a3b92be43 | -3.6703 | -47.1339 | 2024-11-30 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| e3846ee5-d88e-3a32-b254-6d7a1a03c86d | -3.96992 | -41.51273 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 24d8598e-4ac3-3e01-ac68-f65337f0a6f1 | -3.98116 | -46.64465 | 2024-11-30 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b934e7b-9570-3630-9080-a45553f879a0 | -6.7913 | -39.45621 | 2024-11-30 03:46:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 076e0294-3378-305e-9c4d-e9e0c3dc910d | -3.99177 | -41.50858 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 48d58373-3e02-384b-9e36-0a4f62d14b14 | -3.03035 | -45.11425 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 7e69e530-f0cb-3c75-bfb7-9ceb1dded7dc | -4.07488 | -42.18954 | 2024-11-30 03:46:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 647f7651-1e19-3571-8486-a38db5735fce | -4.65517 | -46.37179 | 2024-11-30 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 48d3d237-e413-34d6-8413-504e36645f24 | -3.97404 | -41.51339 | 2024-11-30 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| e2ee22b8-0ea2-3a05-99fc-697909229f5e | -3.3564 | -49.76065 | 2024-11-30 03:46:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 238af624-09ef-3298-bf64-1e673f4000e6 | -2.18298 | -47.14341 | 2024-11-30 03:46:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0cbc6a90-03f3-3223-be57-a4c50c889f97 | -3.01486 | -45.10817 | 2024-11-30 03:46:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04689710-d052-36bf-b226-8e5663f19bd2 | -2.84844 | -46.69327 | 2024-11-30 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af92d3f0-71da-340c-a88f-879736cdcbe9 | -1.88144 | -48.65382 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2740989-8139-3d93-926e-a522edec25d1 | -8.31458 | -44.95586 | 2024-11-30 03:46:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58eece1e-3c8c-38cf-ae64-07271ba18a61 | -7.88224 | -37.34967 | 2024-11-30 03:46:00 | NOAA-20 | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0f20477e-f6d4-3b43-aa46-e1c757a34f94 | -2.82394 | -45.29414 | 2024-11-30 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b28f9dfa-5402-39fe-89c2-7f45ceb36773 | -3.94614 | -40.97157 | 2024-11-30 03:46:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c9cd884-839c-36a2-97d3-734740d02b14 | -5.58537 | -45.20897 | 2024-11-30 03:46:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9fa8dbbd-eef5-3556-9593-c93025b18c86 | -6.91056 | -43.55247 | 2024-11-30 03:46:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ceaf66bd-7a82-328a-8cf7-96b22e404ec7 | -2.97979 | -49.59252 | 2024-11-30 03:46:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b111f095-65a9-347c-98a2-252c233fa1cc | -4.87063 | -41.28805 | 2024-11-30 03:46:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |


[Clique aqui para ver as próximas entradas](README22.md)
