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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1790ef0-4597-3b1f-b3cb-b1d178bc52cf | -9.76325 | -48.58117 | 2025-07-23 03:42:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6929140c-4220-3780-817c-4edf48883e93 | -7.9399 | -44.8553 | 2025-07-23 03:42:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df27eab2-966e-3fee-80a0-32453c07bc63 | -6.60735 | -42.40035 | 2025-07-23 03:42:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d50cf011-1b0e-3575-b700-9482cc837bb6 | -7.21973 | -49.59436 | 2025-07-23 03:42:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b580dd95-ac8b-36a3-a577-538424487e8a | -5.83337 | -44.10355 | 2025-07-23 03:42:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f76abe1-8f64-3b0a-b687-f178f70eabc5 | -10.63904 | -45.22845 | 2025-07-23 03:42:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9d1fe26-0e35-3ab8-938b-c905000ace23 | -6.92644 | -44.30281 | 2025-07-23 03:42:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 965ee585-97e6-3e61-a41d-13983ee482e1 | -4.29726 | -48.10514 | 2025-07-23 03:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d0497a16-eb1c-3a45-85e5-677ca50cc5a2 | -7.88579 | -45.55971 | 2025-07-23 03:42:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26c90956-048a-34c3-9e22-555d48dc3b21 | -9.05669 | -45.06761 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f6ac6a0f-54a8-3a20-b76e-511dc73ef3dd | -5.59458 | -45.05496 | 2025-07-23 03:42:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 425ff38d-1245-3634-8901-83abd0e1102b | -9.05841 | -45.05829 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d513c562-0d15-33f0-9354-dd17166d3b7c | -7.52692 | -42.42095 | 2025-07-23 03:42:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 553bff46-ce9b-3798-adcf-d797a28a6fb5 | -10.88531 | -44.36087 | 2025-07-23 03:42:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44c78941-0590-364b-bc2a-8d780d41c777 | -8.91004 | -47.35835 | 2025-07-23 03:42:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 62f7c739-baac-3615-b796-f0782936bdca | -9.2571 | -48.56224 | 2025-07-23 03:42:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fbe4dcaa-fe41-32b0-935b-c88e1c7cccc5 | -9.67238 | -43.72569 | 2025-07-23 03:42:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 16d45b4c-5e20-3a01-a701-4d2507885def | -9.05729 | -45.06435 | 2025-07-23 03:42:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1e71398e-d49d-3741-852b-01aa38b58af1 | -7.1393 | -46.10313 | 2025-07-23 03:42:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 82b6fc42-1e7e-355c-8523-a3565e51bd79 | -4.77849 | -45.34109 | 2025-07-23 03:42:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7e7da6f-19fc-32cd-a7d4-765bc47b9466 | -5.67542 | -43.67321 | 2025-07-23 03:42:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a79a3d20-5cc7-3e2d-9ef4-26e30f309c91 | -17.51128 | -39.94378 | 2025-07-23 03:45:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c0c6ca04-10b3-3be8-a4d7-8871169ce507 | -13.71524 | -45.69368 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86fd34ea-966e-3739-a812-05aa42f1c401 | -13.6932 | -45.69869 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6688c2ed-f6c6-35ea-b27a-775617cc93a9 | -17.44418 | -43.6387 | 2025-07-23 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7d9d85a-9606-36da-a490-5f123440611b | -13.71405 | -45.69979 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d34e3f9f-17f9-3c08-8a63-92914fc67a1f | -13.71465 | -45.69673 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7e0bf410-f19f-3ddb-b0f5-0e830a4e9b67 | -16.40208 | -46.87536 | 2025-07-23 03:45:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ead1c17-0b1f-3d9c-b24e-415e5c59c4ea | -13.7203 | -45.69472 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f79bf1c-3c36-31af-85b5-46d22f03a6c3 | -17.5606 | -47.50417 | 2025-07-23 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f64e7c3d-a4f9-37fe-b77a-fbaabfa8927b | -17.56514 | -47.50891 | 2025-07-23 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 72eb7322-0c05-3e67-8fa7-bbfe44f3f71c | -15.53679 | -45.37128 | 2025-07-23 03:45:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6c9b116-80e2-3af8-91a4-9e12cae0cbae | -13.71971 | -45.69777 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a13380d9-5ad5-3815-aea8-6358b55e0148 | -16.0413 | -43.72361 | 2025-07-23 03:45:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7391a53-436f-37f0-adb9-26e3b8265e9f | -13.69886 | -45.69669 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 411415ca-40b7-3b1a-bbc4-498026ebbb19 | -17.72714 | -42.07331 | 2025-07-23 03:45:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 82b23236-f52d-340c-b305-9ebed8466639 | -17.57044 | -47.51002 | 2025-07-23 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 843d1787-9da3-3f85-91df-e98539f3dad4 | -13.54057 | -43.70856 | 2025-07-23 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 22bc6ddc-436e-31cb-a412-2292d55048e1 | -15.6044 | -46.52085 | 2025-07-23 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dca3e81b-e232-3e5c-b263-a97ade0baa38 | -16.04933 | -43.79906 | 2025-07-23 03:45:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 85c70e3e-741c-38a2-8502-83eb76cbdb3c | -13.71077 | -45.68961 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d0a70bd-4950-3dca-a86a-bfce05566349 | -13.09701 | -46.83496 | 2025-07-23 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5d1ac8c9-440a-3536-a131-01c291c992c7 | -14.18749 | -45.34161 | 2025-07-23 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aea032c2-5991-3758-878a-424229562d64 | -13.70899 | -45.69877 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 045c1947-045d-3205-a95c-18f604315c78 | -15.55698 | -44.75161 | 2025-07-23 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 927bcae2-27f6-3732-a1b0-5c991f8bca3b | -13.68488 | -45.6875 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f10e8dba-8578-3610-bf60-af51f15e4720 | -16.03704 | -43.72272 | 2025-07-23 03:45:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33c00f91-2032-30e8-bbe1-5c3407926195 | -12.65021 | -45.05201 | 2025-07-23 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 00bfebb2-414b-3474-9a68-a4ce6a2b9638 | -16.09816 | -42.27895 | 2025-07-23 03:45:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f77ffd67-9273-3fe4-bfb1-9217f17b5b56 | -14.3898 | -47.74274 | 2025-07-23 03:45:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95b561c0-535e-37be-9f59-d10ef832e7c1 | -17.72703 | -42.07522 | 2025-07-23 03:45:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b78f3d80-8e0c-3f34-a918-8e9951fc722c | -11.81071 | -44.26944 | 2025-07-23 03:45:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12ede4a2-4ea7-356a-b046-766747a85d35 | -15.56159 | -44.75252 | 2025-07-23 03:45:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8ea14356-d36d-3509-85c8-06c50b0e234f | -14.64394 | -46.83552 | 2025-07-23 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46e65a1f-b717-3c2c-9099-dc3fe12c221d | -13.71583 | -45.69063 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9a166b39-1097-39aa-a95c-8d88cddc1873 | -13.64956 | -45.71802 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c98128a6-c51f-3bf6-b107-119e3e4f26a2 | -14.6551 | -42.20162 | 2025-07-23 03:45:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d9e9dd35-c75c-31a9-a41a-b91845b30e0a | -13.74503 | -43.46131 | 2025-07-23 03:45:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d6ad981-e3cc-3823-ae16-5a5344e6bf0f | -15.93097 | -43.52383 | 2025-07-23 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3040434-b4b8-35ee-8d32-7bc721ca537d | -11.52148 | -43.24555 | 2025-07-23 03:45:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 81c2069d-2e2f-325a-af4a-554d6aaa5bff | -14.64466 | -46.83199 | 2025-07-23 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7b475d9-cfec-3d78-b2e6-33c5729c7eea | -15.59927 | -46.51962 | 2025-07-23 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 714a98b6-fbf3-3e4f-8dc7-a3263df29eb4 | -13.30469 | -44.18213 | 2025-07-23 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01e6ae11-7dc4-3c20-9923-f01716783559 | -17.50785 | -39.94315 | 2025-07-23 03:45:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 71b3b9cd-93e5-3001-a50c-6477835c07d2 | -16.61605 | -43.3592 | 2025-07-23 03:45:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d03e959-4dae-3234-837a-1dee2b61dae7 | -14.74148 | -46.30198 | 2025-07-23 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e46a55bc-422f-3f5e-8022-12f1fdb4a332 | -14.39058 | -47.73899 | 2025-07-23 03:45:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a5794af-8699-3b83-aa6f-0fa200c60ae3 | -13.30186 | -44.17966 | 2025-07-23 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b42dfeaf-6f3d-31a3-a3be-a5761b9468b2 | -17.57119 | -47.50644 | 2025-07-23 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c422b994-02fe-38f4-8d10-1810dce8fc0d | -14.65631 | -42.20514 | 2025-07-23 03:45:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fa3e658a-68d7-396d-9847-df89cb9afdf8 | -13.64838 | -45.72423 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 95ce038e-8d3d-354f-b958-9d6c019964ab | -14.74551 | -46.30327 | 2025-07-23 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8cc1638c-ab3e-356a-86be-0c595d26ba77 | -15.59863 | -46.5228 | 2025-07-23 03:45:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 46e92192-9a9a-341d-9b13-697c61231d1f | -14.17926 | -45.35755 | 2025-07-23 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a765476b-1c46-3ad1-9016-984655bbc896 | -15.77968 | -46.05988 | 2025-07-23 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a453a9e-9e79-36ab-85c0-f90b25768146 | -13.70333 | -45.70078 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1a47bae7-592e-3656-a980-db18df1a4ab0 | -13.09762 | -46.83188 | 2025-07-23 03:45:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdf63f7e-9a1b-38bb-99c4-bf15f1a404d4 | -15.57371 | -41.06642 | 2025-07-23 03:45:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 66164544-e90c-3a4e-b25d-3dc8ccd480d6 | -14.50076 | -43.80939 | 2025-07-23 03:45:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7001b36b-8943-3c54-9d14-ed001567b292 | -17.84439 | -42.64228 | 2025-07-23 03:45:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3c104d54-412b-3a42-a8bb-2c53f5ba4314 | -13.69946 | -45.69365 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 787a4555-bba8-350a-ab09-93b8bd222228 | -17.5659 | -47.50531 | 2025-07-23 03:45:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9a93381-2c5d-34fa-887d-992de4d81b68 | -13.07695 | -44.06599 | 2025-07-23 03:45:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dfa9db93-b6a2-314b-be77-0371b3d716aa | -16.61398 | -43.35909 | 2025-07-23 03:45:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d1d1f043-4318-3fc2-9865-673ad50063c5 | -13.69827 | -45.69973 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cd82f0b-bfd7-316a-bffb-8d677a139d86 | -13.64897 | -45.72112 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7a92b74-a6ba-33e5-a45a-a70532d3bf27 | -13.70452 | -45.69469 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 74e56877-6094-3c67-8173-6f39af212053 | -17.84566 | -42.63957 | 2025-07-23 03:45:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d0c2062b-507e-3452-8aef-5aa99319b05e | -14.64733 | -46.83378 | 2025-07-23 03:45:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abd741de-f4a9-3d9f-9edc-4788da93080c | -15.57294 | -41.07089 | 2025-07-23 03:45:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2d50bd82-b9d5-32d8-8114-ff23ab6e5b2b | -12.66335 | -45.03687 | 2025-07-23 03:45:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bf171ff7-7bd7-3541-bc5c-9205b803aedb | -15.93069 | -43.52311 | 2025-07-23 03:45:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c32b3ed-b4a7-354e-ae1e-5dbfaeb12679 | -17.44231 | -43.63977 | 2025-07-23 03:45:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20f39656-f185-371d-a992-a5d0bf8b44bd | -17.8453 | -42.63713 | 2025-07-23 03:45:00 | NOAA-20 | ARICANDUVA | MINAS GERAIS | Brasil | 3104452 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be510122-9823-32e3-b591-5cc2ef476cb5 | -14.74612 | -46.30013 | 2025-07-23 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c085daf4-681a-3512-b332-d6128ad5e2ad | -13.70392 | -45.69774 | 2025-07-23 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 858a07fb-8a6f-375c-8f9b-eb8e937e60df | -14.18625 | -45.34026 | 2025-07-23 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 245c5dca-41ae-3d09-be21-e26d8963a545 | -15.77976 | -46.06224 | 2025-07-23 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 686b8d99-0fab-3aaf-a153-851345542809 | -14.77168 | -48.25607 | 2025-07-23 03:45:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f8fc1d7-3beb-3448-9d8d-312ff160ec3a | -14.74212 | -46.29883 | 2025-07-23 03:45:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README7.md)
