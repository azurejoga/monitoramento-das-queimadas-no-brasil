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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e476d916-3f49-39e2-98e8-1d6c297dc702 | -13.90226 | -43.33623 | 2025-09-25 00:33:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 26e014bd-65d8-3fde-aac0-f17ad35aa0f9 | -12.06913 | -47.98803 | 2025-09-25 00:33:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 6e96f942-fff5-30a0-a9f8-ce7154b771cf | -6.43445 | -43.08717 | 2025-09-25 00:33:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 66b4f753-f81a-3c62-90e1-e4ff71a5b72c | -7.38129 | -47.04147 | 2025-09-25 00:33:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 6f34864a-f850-3a22-af4e-7b910100aae0 | -14.05796 | -43.0784 | 2025-09-25 00:33:00 | TERRA_M-M | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 69d2d7bd-d3a3-3475-b6c4-441c2202011d | -9.04712 | -47.01519 | 2025-09-25 00:33:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 15cdb76a-df57-3338-9c23-d95a863d8416 | -7.26409 | -44.91554 | 2025-09-25 00:33:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 74a37050-b494-374e-8051-54095b2c13f3 | -14.50394 | -45.51624 | 2025-09-25 00:33:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 71547f4c-b352-3bbd-bd4c-0b657191ce51 | -2.962 | -48.59644 | 2025-09-25 00:35:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 439e523b-e78a-3d44-bbfd-1c1ce019e061 | -3.73635 | -49.05716 | 2025-09-25 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| c485df27-8f26-341d-8c35-ed17116b3908 | -3.20286 | -54.96283 | 2025-09-25 00:35:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| c75ac063-f02b-3158-9755-6936dfef8c02 | -2.92143 | -48.30312 | 2025-09-25 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 38aeba91-1152-34ac-8f7b-35ae7825f8c6 | -3.61584 | -51.80162 | 2025-09-25 00:35:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 57fcb0e3-7c1b-3f42-9480-1d51443d1c55 | -3.69851 | -49.57906 | 2025-09-25 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| bb13089b-1d2d-3c42-86c7-854b618a5cff | -5.36721 | -46.30073 | 2025-09-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1e8738c8-c800-348b-a153-d207681593d5 | -1.0881 | -54.11586 | 2025-09-25 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 96de084f-be40-3661-8d80-8f1ee8d00f6e | -4.02703 | -47.76951 | 2025-09-25 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 469d937e-fdcc-31d9-bb06-9e38c961f5fe | -6.2612 | -46.10746 | 2025-09-25 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 6a118aea-f905-31ec-b277-dd90e99c92ca | -1.08633 | -54.10296 | 2025-09-25 00:35:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a338825d-b2e5-35c1-bb82-95db8fad9b75 | -5.09209 | -47.47531 | 2025-09-25 00:35:00 | TERRA_M-M | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a350a2d6-50a9-3f75-9d5e-f1cbb6a75c7d | -3.6973 | -49.5703 | 2025-09-25 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 60c62079-2631-35e8-b278-41a1488ffd78 | -3.83574 | -50.97749 | 2025-09-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 75b7b43d-4858-3ce0-ba58-8b416dfcf2fe | -5.59978 | -45.35904 | 2025-09-25 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 407a556e-69b6-361c-867d-0dc568609cfe | -1.87395 | -48.39539 | 2025-09-25 00:35:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| da434cde-ba96-39b6-80bf-11c8407a5d68 | 1.7976 | -50.8527 | 2025-09-25 00:35:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7f7f57a1-5593-3c48-89ce-0e3b6abe2fbc | -4.60701 | -43.90688 | 2025-09-25 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 6492c8b8-29f7-32a1-a68b-529c29e1f672 | -4.79349 | -43.54486 | 2025-09-25 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 07e5834b-6441-33be-a3cf-a1fde0a6026b | -3.81766 | -50.98005 | 2025-09-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| bb6e30de-ddfc-3687-b455-6305849de254 | -4.55072 | -44.01645 | 2025-09-25 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 98e5cad0-97b6-3a31-96aa-c4ccf83ad22e | -3.39833 | -47.50049 | 2025-09-25 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3b100c16-9a8d-3948-906c-9e83b0b43f2d | -5.59125 | -48.66607 | 2025-09-25 00:35:00 | TERRA_M-M | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 66d54203-4f04-3890-b69c-5a54d61b9d1c | -3.79475 | -41.73083 | 2025-09-25 00:35:00 | TERRA_M-M | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| bfcc7c50-89f5-3907-8c8d-7c311d3de349 | -5.01065 | -45.18293 | 2025-09-25 00:35:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 59c4f195-7113-3899-8518-c9b355df84e7 | -4.73918 | -44.43126 | 2025-09-25 00:35:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9f14d509-ac1f-3b0d-a605-6006414c7a09 | -5.36567 | -46.29 | 2025-09-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c4342ecc-53a3-33d9-8d17-23aa93e2989b | -5.35591 | -46.29144 | 2025-09-25 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 86b27d26-6ea7-331d-8499-a614659a490f | -4.58032 | -49.69523 | 2025-09-25 00:35:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 4aa4adc9-ba27-3a28-a01c-a4584245a137 | -4.42687 | -47.26525 | 2025-09-25 00:35:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5de70041-6519-3b02-8662-5ce3c94f6f0c | -5.5589 | -46.28247 | 2025-09-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 61bf5122-6a07-3d07-9917-5478355354c7 | -3.94158 | -49.40129 | 2025-09-25 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ea0dbef3-b542-3d79-8fd4-2a894d869f84 | -3.43654 | -44.49026 | 2025-09-25 00:35:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a1a6f0fe-7fbf-301a-93f1-d905220df297 | -3.94203 | -47.56584 | 2025-09-25 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 9479eba1-d0e1-3449-a522-08f538a2c1f7 | -4.29042 | -48.27012 | 2025-09-25 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4caf7490-92f9-373b-88ee-4633ee885563 | -3.15809 | -49.47732 | 2025-09-25 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 257e2970-f01a-31f5-b978-80d9c6a0a94b | -4.79735 | -47.27822 | 2025-09-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 6fe1180f-3235-3514-8373-44655dbfcf8d | -6.42171 | -47.22912 | 2025-09-25 00:35:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 466acca1-7cff-372f-9bf4-d02d8ae7d3ac | -5.60159 | -45.37149 | 2025-09-25 00:35:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| bcabc424-838e-3fe8-bd2b-a2aa0f74475c | -5.6325 | -45.72668 | 2025-09-25 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 43.4 |
| 970c07b9-bc62-377c-b4af-3059c403bcc5 | -3.83445 | -50.96819 | 2025-09-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 1edd5e29-f502-32dd-b97d-900901c55e34 | -4.55314 | -44.03273 | 2025-09-25 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 339b8b37-4cbc-3fae-a06b-d4fc59ef7e2e | -4.60385 | -43.91784 | 2025-09-25 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 7cf253e7-5751-385a-a329-37121e0654f5 | -2.92271 | -48.31237 | 2025-09-25 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| bcffbd89-2c8a-38c6-b568-00039de6677d | -2.82757 | -46.72782 | 2025-09-25 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 45a91d05-cb6b-3b1c-a345-0a6977c7a66f | -3.8267 | -50.97876 | 2025-09-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 695ac638-619e-3269-bb8d-aff2a8c728bb | -4.76322 | -43.25303 | 2025-09-25 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 40041cc8-f28b-3760-a1ed-9ed5014a286a | -3.76925 | -48.03605 | 2025-09-25 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 22.6 |
| dcb2b0d0-9008-3681-ba77-cdc702efb499 | -5.07977 | -45.51181 | 2025-09-25 00:35:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| edd8d5b5-0913-3d3c-a584-dcc3dfe50c19 | -4.91026 | -46.8379 | 2025-09-25 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 439d92b7-c538-33e1-b4f9-c025e0060bbb | -5.39098 | -42.27966 | 2025-09-25 00:35:00 | TERRA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 39a91415-10e7-3bfa-a643-254d06f14920 | -4.80562 | -43.54286 | 2025-09-25 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 245.0 |
| cf5c1914-03ce-3446-860b-aaba96b4cd3f | -5.00005 | -45.18462 | 2025-09-25 00:35:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 6ef22c1c-838a-33f5-8c0c-bde922e0125c | -6.34637 | -46.33154 | 2025-09-25 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0f800f0b-599c-3b06-b6b9-7f0dcd89b526 | -3.77057 | -48.04542 | 2025-09-25 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 3bd569d7-7c8f-345e-9b87-90448386a415 | -4.16771 | -54.63473 | 2025-09-25 00:35:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| de679671-c702-3ea0-81dc-ecfdc92ca590 | -4.80951 | -43.53659 | 2025-09-25 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 86f8c907-a384-3da2-8204-b291ed2e2330 | -6.2628 | -46.11854 | 2025-09-25 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| bbd892e3-a277-3b69-ba06-8b497752b39b | -5.00873 | -45.16982 | 2025-09-25 00:35:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| c0a15f4d-550e-3691-87c2-c952fa8f12a4 | 1.78703 | -50.84492 | 2025-09-25 00:35:00 | TERRA_M-M | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 42d55a61-cbb5-326d-abed-35a3e67f7961 | -3.81637 | -50.97072 | 2025-09-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 460fa7d0-db9a-3562-b4c4-2a700a365862 | -3.21231 | -54.97165 | 2025-09-25 00:35:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 2d9e2b2e-15d8-3aad-9066-953c8361d564 | -4.09837 | -45.6592 | 2025-09-25 00:35:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 383d8f15-20cd-38ca-bf42-81d232b75a6b | -2.8374 | -46.72641 | 2025-09-25 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 6be267fd-a0c0-3132-9f27-04b807c3dc49 | -2.25386 | -47.88287 | 2025-09-25 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 19dac82e-97be-32f1-8805-46dc557c46b1 | -6.3448 | -46.32087 | 2025-09-25 00:35:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| a5240687-5657-3d59-a17f-8e90c7ad2b60 | -3.82542 | -50.96949 | 2025-09-25 00:35:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 39686cea-ff55-3094-a6a3-83cec9e45544 | -1.53706 | -51.61734 | 2025-09-25 00:35:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8682c039-02c3-34b5-ac48-e655e8adbab2 | -3.09166 | -52.92287 | 2025-09-25 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 1782a145-3c1e-3e1b-916b-741498f37c6a | -3.21016 | -54.95538 | 2025-09-25 00:35:00 | TERRA_M-M | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| d971b5c8-ede8-3037-a253-e6e26d9dd512 | -3.79207 | -41.73687 | 2025-09-25 00:35:00 | TERRA_M-M | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 43.5 |
| b40410ea-5242-3ea2-bb5b-f841b5f979d7 | -5.35746 | -46.30218 | 2025-09-25 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1f607591-efe3-3268-8bd2-44d629188aa5 | -3.43424 | -44.47453 | 2025-09-25 00:35:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e2ff4948-a00f-36e5-b028-cbadbbbb6b92 | -2.2681 | -47.19324 | 2025-09-25 00:35:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 861b7362-4574-3105-9ab8-5707433a242d | -3.3815 | -52.71995 | 2025-09-25 00:35:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ac4ac93c-ac5a-3b9b-be10-3e7f7582a653 | -4.99809 | -45.17127 | 2025-09-25 00:35:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 8d79c690-4cb1-3333-97d0-97a96b0df805 | -3.30731 | -42.17648 | 2025-09-25 00:35:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 28.0 |
| df188feb-d7b1-3c78-946f-dc41e1ed71ca | -4.02837 | -47.77909 | 2025-09-25 00:35:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 07f9c888-86f9-339b-89ee-ce554ad132c8 | -4.79597 | -47.26831 | 2025-09-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 531c0fea-f690-384c-b753-0daf02a7308a | -2.259 | -47.85222 | 2025-09-25 00:35:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| be638df2-eb63-3cf4-b792-1ddab23f9de1 | -5.39388 | -48.84736 | 2025-09-25 00:35:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 36b54cd1-989a-3c96-994d-9164026d7d4a | -4.99279 | -47.3571 | 2025-09-25 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d3424bdd-226f-3de3-8535-05f11df8e538 | -4.60938 | -43.92347 | 2025-09-25 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 570300d3-c97c-38ca-ad0f-462ff647256c | -2.19137 | -54.46622 | 2025-09-25 00:35:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f90d954d-eea2-300b-b048-a022e5b6ff77 | -5.84234 | -42.65422 | 2025-09-25 00:35:00 | TERRA_M-M | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 20d6fc4b-d911-38fe-8658-be694a44039b | -4.8082 | -43.56052 | 2025-09-25 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| b7d44ed7-f3c8-3a01-994c-f7a1fb7769b4 | -4.61567 | -43.91605 | 2025-09-25 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| b6bcc083-06fb-3517-88d5-498ec6cf0b2a | -3.73513 | -49.04834 | 2025-09-25 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| aeaa2c9f-4f35-3933-a935-02744e34ccde | -6.15212 | -44.72747 | 2025-09-25 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8659d826-5006-3a60-b4dc-6924fdda49fb | -3.23646 | -46.80101 | 2025-09-25 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| c6cc633f-e297-3f5c-920e-50aabc7cb319 | -4.28915 | -48.26101 | 2025-09-25 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 1b39f2f3-015b-3438-bb5f-196cef93d6e7 | -20.9931 | -50.0032 | 2025-09-25 00:40:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 277.9 |


[Clique aqui para ver as próximas entradas](README4.md)
