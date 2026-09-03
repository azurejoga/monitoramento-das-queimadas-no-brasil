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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25a404b5-0677-36c0-b617-8d76ecd9b1d9 | -11.0155 | -45.091202 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7f5c47e7-2a00-3785-812f-18a541868346 | -8.448 | -54.693901 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d94a748-7c37-31a9-8581-558ef8d72bd7 | -16.7864 | -49.630699 | 2026-09-03 01:12:00 | METOP-C | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 10aa3442-6825-3d9c-9651-c3dd2922deb2 | -3.6115 | -55.374802 | 2026-09-03 01:12:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4cfe659-1205-3f03-bcd0-e482347cd6b8 | -8.1512 | -54.926899 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4dee69d0-f4b9-3b1f-aa43-6dbfe926fb4c | -6.3349 | -56.040401 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98c5b183-23ac-3e2c-9609-135b34335f40 | -5.2137 | -60.036499 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e5dfc47-90ad-3438-8459-7fd14f180972 | -10.2073 | -50.275398 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d4fdc3a9-581c-36fa-bce2-4b0c0f3c46e4 | -4.9893 | -55.844002 | 2026-09-03 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb11a2ee-57d6-364a-b931-45810c61e987 | -5.9462 | -52.191601 | 2026-09-03 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a11c294-5601-3986-98fc-094aa7ee4e9d | -7.3301 | -55.124401 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 659b4776-7819-3708-ac1b-c9a45b07847b | 4.4108 | -59.782902 | 2026-09-03 01:12:00 | METOP-C | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 47d3ab30-f2d2-3e12-82b3-07e76d2d10bc | -5.5999 | -60.1992 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c91fb801-464c-3cd4-ab14-eac63d1eb993 | -8.4818 | -54.662399 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50d8d790-14d0-315d-97de-e06274c0dd49 | -7.5784 | -57.689999 | 2026-09-03 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 041b7829-dade-3d51-a755-ea6298aed745 | -8.4578 | -54.691601 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dba7cb0c-00a3-363c-98ea-6aebf5ae1f5e | -3.1569 | -60.6366 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d6fff71-0b02-3804-b04f-d079a8fcd0e0 | -6.4297 | -58.305199 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 86fd0d17-4b83-3e6e-a5d7-4c8263ade6c4 | -5.2783 | -60.1866 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d61dec07-d4db-31fe-b55e-b450c9e6b0ad | -3.661 | -58.774399 | 2026-09-03 01:12:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 39f2a434-d02f-39b9-a245-50fdfb604052 | -10.3853 | -49.952 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f40d2792-a612-3084-bfdb-51f1c467ec9f | -7.5144 | -60.771301 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 38e88e3a-a6f8-3a57-b7cc-983588c4e85f | -12.4332 | -44.8078 | 2026-09-03 01:12:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bdeedc77-4047-383a-adb4-fa95237b054a | -5.591 | -55.813301 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b13902fd-96f1-3e04-836e-740d21ca425c | -6.634 | -55.237999 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a4c8dd7-541b-3fee-b0c5-e0cd3fe2ae84 | -10.5435 | -50.006302 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91546c5d-8b81-3a74-8390-2ab223d1a072 | -5.5643 | -60.223801 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a6fcbd8-79d4-388d-b735-42a49886e05d | -8.4801 | -54.6549 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6d6b069-fc88-3df9-97bd-b8185db95d52 | -3.1483 | -61.1898 | 2026-09-03 01:12:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e36fd96e-e7a9-3ce3-b2f2-86c0d2491ce3 | -4.9876 | -55.8367 | 2026-09-03 01:12:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9e4cd5-18c4-3596-a870-75ad5af71f58 | -4.1305 | -51.0182 | 2026-09-03 01:12:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d4a68fe-d360-3877-b979-31a66044e346 | -6.5818 | -58.568401 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 66715dc2-59b6-34ce-a83a-4d8e10bed47f | -6.6536 | -55.233601 | 2026-09-03 01:12:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13b2e310-a748-3b95-bda7-c75d75e6cd99 | -18.774799 | -48.9128 | 2026-09-03 01:12:00 | METOP-C | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 10cb9d1d-f3fd-3552-8581-5822cd3d1f7e | -6.7907 | -58.672401 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e60b21ab-f0fc-3b90-b4b1-85208d28809e | -11.3314 | -45.116501 | 2026-09-03 01:12:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81f2a952-bb9d-3aef-bf50-e288d2f43765 | -7.6232 | -57.614399 | 2026-09-03 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d68e154-adeb-331f-a089-ed6c0a6f1b32 | -7.0934 | -56.5121 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0cb1517-c96f-3652-8510-81fb837ff0cd | -9.1027 | -65.3647 | 2026-09-03 01:12:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 44c4246d-c304-3c77-b923-0ce167681475 | -6.6652 | -59.4436 | 2026-09-03 01:12:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9f474e7-8bde-3ae1-af11-c5cb1f62c5b4 | -3.4034 | -59.362801 | 2026-09-03 01:12:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ec7dfc6b-75f9-3024-a09b-bf1228105af5 | -10.2941 | -50.0424 | 2026-09-03 01:12:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 18579818-1957-3e77-9da1-443466f52bab | -18.183701 | -51.791599 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b3a6cddc-afe8-39fc-a842-479468c5aac6 | -6.5068 | -53.594398 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 745b463a-1100-3cb1-8b20-40129c88025b | -9.0891 | -65.347801 | 2026-09-03 01:12:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 526ff8e6-ab48-3f60-9fc5-960b653ac690 | -5.2218 | -60.0266 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7c9dc66c-b91d-3bc8-943e-df5975ec8a60 | -12.4261 | -44.781601 | 2026-09-03 01:12:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 395b68c7-f8c4-36f9-9215-212524629052 | -5.2154 | -60.0443 | 2026-09-03 01:12:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 74eed881-e4e7-35b6-a311-137325e85e09 | -18.173901 | -51.794102 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1481da2a-68af-34d5-913d-8a4a1579b035 | -9.6317 | -48.555599 | 2026-09-03 01:12:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06bc4618-f80a-3b4e-b652-3972d2006b6f | -4.4243 | -55.765701 | 2026-09-03 01:12:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b47abfeb-9140-306b-8dad-b9632c165aa3 | -7.6345 | -57.619099 | 2026-09-03 01:12:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa368231-082b-37d8-80e1-029654746e8f | -18.156401 | -51.807201 | 2026-09-03 01:12:00 | METOP-C | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e025f85e-ff91-312d-86c9-5e7011e98611 | -6.6559 | -52.960602 | 2026-09-03 01:12:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9773a579-07c0-3245-968d-341582a1eda3 | -6.4313 | -58.312302 | 2026-09-03 01:12:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fcad3ff6-6ba5-31bd-9c52-3df1150b1922 | -6.403 | -55.2211 | 2026-09-03 01:12:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 796a19da-a8b2-3123-b477-4cf1261f24f9 | -10.99 | -45.08 | 2026-09-03 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c570e3e-269b-3258-bebf-c9b5ca9bd830 | -6.4208 | -58.3137 | 2026-09-03 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 66b7d2ff-6a03-39cf-a766-047832247acd | -6.6698 | -59.9443 | 2026-09-03 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| b46e3f2a-b828-3182-89f7-33b0e6ba4cf4 | -9.0415 | -65.7349 | 2026-09-03 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| ca95c2ef-8300-3a0f-a1f0-199b8031609d | -8.0737 | -50.9656 | 2026-09-03 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| adf65744-4801-3d20-b23a-ac0f55949060 | -6.6248 | -55.2331 | 2026-09-03 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| f6031e63-dba2-32dc-9c27-e47a53474d43 | -6.3236 | -56.0632 | 2026-09-03 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| adcda591-4146-30f3-9b9a-c223f5ce3c3f | -10.8822 | -45.3305 | 2026-09-03 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.4 |
| f1b99873-e061-343f-94b8-20907bfb4602 | -6.6542 | -59.426 | 2026-09-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 503b21f5-5f84-38c1-a28f-e25c1b7972e7 | -6.7463 | -59.4416 | 2026-09-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| b2069348-5c88-38c7-9db3-977128671da1 | -6.3052 | -56.0442 | 2026-09-03 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 24667d89-d711-3c43-8f95-83519f684100 | -6.6358 | -59.4267 | 2026-09-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 41aaa3a5-1538-3c33-a730-5e3da92e7d50 | -13.4157 | -42.4999 | 2026-09-03 01:20:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 94.7 |
| a52ca705-a645-3410-9e19-3d71597fbd1f | -10.9013 | -45.3279 | 2026-09-03 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 1f78b504-efc7-3d2f-8e04-576d1d36946c | -6.6541 | -59.4452 | 2026-09-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 0cc91950-1d2f-3f55-ae14-61d94b01e4e5 | -8.4487 | -54.6846 | 2026-09-03 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| a3410270-6c0c-365b-a854-a5a432cb4915 | -10.8826 | -45.3075 | 2026-09-03 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 2406f0fa-ea09-39da-8eff-859609d84499 | -12.4037 | -44.7856 | 2026-09-03 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| e253c6bc-9100-3d95-9849-77d3b4a677f6 | -8.0924 | -50.9642 | 2026-09-03 01:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 113.9 |
| e502bdef-9f89-31d5-87c1-d55f7c172d79 | -6.7648 | -59.4408 | 2026-09-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 3cf3c490-1613-3542-9de5-89a157010f1d | -6.6764 | -58.7686 | 2026-09-03 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| aced00be-fe47-3e31-b3ac-b7e97e777f4a | -6.6883 | -59.9436 | 2026-09-03 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 151.2 |
| 66e5b961-0005-3a25-97f3-648f71db739f | -6.4209 | -58.2943 | 2026-09-03 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 1909620b-318f-35d5-91ff-4c8f298897d2 | -6.6697 | -59.9635 | 2026-09-03 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| ba4b7a58-ed29-3d74-8d82-6ebc0de6a13a | -11.0003 | -45.1078 | 2026-09-03 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 8f530c5e-ebdc-3bcd-835d-6d57777cb5c6 | -12.4033 | -44.8089 | 2026-09-03 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 135.6 |
| f7636d92-b23d-3b63-bdab-791aaa7ca285 | -10.9017 | -45.3049 | 2026-09-03 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 9194847a-5642-3f39-94f1-26faa1708353 | -13.4162 | -42.4755 | 2026-09-03 01:20:00 | GOES-19 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 8773ae42-72ba-3831-88c5-1da32fe555b5 | -3.2486 | -47.2438 | 2026-09-03 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 2a300510-d94d-33bf-91b7-b387ec2eac45 | -6.3237 | -56.0434 | 2026-09-03 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| be63ce8e-f99f-3ee6-a5e2-1a16c5acbd82 | -18.1704 | -51.7904 | 2026-09-03 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 9e987711-1e7e-3804-98c7-ea90b4454e8b | -6.6357 | -59.4459 | 2026-09-03 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b0193bbc-5468-32dc-8dae-9765e817740d | -6.3051 | -56.064 | 2026-09-03 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 85e5fb0d-3ae4-39c1-a485-81832996d6e3 | -11.0006 | -45.0847 | 2026-09-03 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 23be13ce-4957-3624-9274-f10341b578fe | -10.2028 | -50.2895 | 2026-09-03 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| d708a3bb-0d07-38da-be32-632f1b88ff10 | -18.1699 | -51.8122 | 2026-09-03 01:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 54.4 |
| e759de2f-8483-3b18-b1cf-676c26ca73da | -11.001 | -45.0617 | 2026-09-03 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b4a3dbd9-2a74-36d7-9d3a-83c7d089f2e8 | -10.9815 | -45.0874 | 2026-09-03 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 05c41270-df03-353e-9d30-f29d37ba3bb6 | -6.6882 | -59.9628 | 2026-09-03 01:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d94540dc-cbfd-335c-b443-6b464005345d | -6.6541 | -59.4452 | 2026-09-03 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 2c2d22b3-31ec-3f24-8546-36609720fb5c | -8.4487 | -54.6846 | 2026-09-03 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 108bb066-2249-3d6e-90f8-becf9902f263 | -10.2028 | -50.2895 | 2026-09-03 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 131.7 |
| a49baac2-d0ea-382c-9340-e3a09c672afd | -10.9815 | -45.0874 | 2026-09-03 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 135.8 |
| f7d4c6f2-e690-3ba8-afc3-112c728580c7 | -10.9013 | -45.3279 | 2026-09-03 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |


[Clique aqui para ver as próximas entradas](README12.md)
