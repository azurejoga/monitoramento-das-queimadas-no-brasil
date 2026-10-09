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

## Dados Diários - Página 293

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7583780-8d27-34b7-a949-5123f6a235a8 | -7.4883 | -42.8532 | 2026-10-09 18:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 122.9 |
| 304bce2f-ea8d-339f-ac5d-3b03dec5f8f0 | -3.2533 | -50.3899 | 2026-10-09 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 311602fd-ad3f-3b40-926b-893c897ecb8a | -13.3671 | -43.8742 | 2026-10-09 18:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 325.2 |
| 641d464a-13f7-3785-9701-b419b175e058 | -3.4463 | -57.9618 | 2026-10-09 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 3756b868-e01c-3159-ac4d-64c012132dec | -15.3825 | -41.9277 | 2026-10-09 18:40:00 | GOES-19 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 545.8 |
| 3710d7f8-12c3-38d0-8978-6eb169635aba | -11.7768 | -45.5035 | 2026-10-09 18:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 607e4b5a-1b05-3def-b51d-3b3bc83b6fda | -2.9451 | -54.0497 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| fb1c01ed-d7db-3102-b585-6a455b06de8f | -6.4956 | -38.9535 | 2026-10-09 18:40:00 | GOES-19 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 160.3 |
| 89551ba9-0504-3e0b-96e1-4033902876b2 | -2.7244 | -54.1351 | 2026-10-09 18:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 155.9 |
| fcd78d9c-1cd7-33dc-bbf5-ec364f0f63a9 | -3.0191 | -53.9071 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3b6756ab-6e62-3def-8034-af435ce2488f | -6.8098 | -52.7744 | 2026-10-09 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| b65f88be-3ac7-3455-a504-e5705a655b20 | -4.937 | -56.8675 | 2026-10-09 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| a76ccb36-572e-3ce4-950a-783b04a88bf8 | -12.1243 | -43.3023 | 2026-10-09 18:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 35782bbc-cbda-3b85-bed6-220ce814883f | -6.4021 | -52.7159 | 2026-10-09 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 87064e8f-6660-393b-8378-22913709a73f | -3.2136 | -42.9764 | 2026-10-09 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a9429736-b76c-3681-b6bf-07786e40ce32 | -10.5104 | -47.2288 | 2026-10-09 18:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 821c4ef0-9a0c-3df5-b9d5-44f5bdadfa36 | -3.5893 | -59.0773 | 2026-10-09 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a8e203ac-e246-3ccd-acfb-c2218dd4976a | -2.4806 | -56.0875 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 5977ddbf-8e6c-31d9-bc2f-10d53c75af52 | -11.8787 | -47.3668 | 2026-10-09 18:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| ab2368a6-a24c-3994-8d73-0610825c442b | -12.3712 | -46.5562 | 2026-10-09 18:40:00 | GOES-19 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 270.5 |
| 8c8536a0-452c-3094-8007-d04ef7d30d63 | -7.0036 | -47.7062 | 2026-10-09 18:40:00 | GOES-19 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| bf38403e-4534-3ee3-9711-3f536c091a1e | -10.8909 | -44.8001 | 2026-10-09 18:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.7 |
| e2b4c7a9-4cc4-37fa-b215-72ddcfd50380 | -10.9384 | -45.3916 | 2026-10-09 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 1d3e9a2c-86c1-3b1e-93d5-d62ec1d122b9 | -11.2471 | -46.3284 | 2026-10-09 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.7 |
| d6ee1701-e929-3f6e-97fd-bc22e41f9dfa | -4.4079 | -43.1252 | 2026-10-09 18:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 32367e4d-31de-3066-a0c2-7619f0c20231 | -15.4269 | -43.3102 | 2026-10-09 18:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 2acefc16-d9b3-3344-a205-9fc970e6321a | -3.2945 | -54.0006 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 2861cde9-3c47-3dfa-9004-4f4bd455413c | -8.9311 | -45.1355 | 2026-10-09 18:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 295.3 |
| 851675df-1528-371b-af10-c64ada542593 | -2.572 | -56.1646 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 7eab6db4-6977-3bd6-a6fe-f27c41b81d4d | -3.1697 | -58.6437 | 2026-10-09 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 97da892f-0c03-38c1-bbde-3fa8293099d7 | -2.4442 | -55.97 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 224.0 |
| 0b614e7b-f753-39f4-9f7a-48872a457002 | -10.472 | -47.2556 | 2026-10-09 18:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 3e387ae8-6f8e-3795-9db3-0248158cbb56 | -5.561 | -43.9544 | 2026-10-09 18:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 108.7 |
| c27dcc6c-5077-31ed-a8a1-442e96bc5c90 | -1.7296 | -56.0597 | 2026-10-09 18:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 07035d5d-d937-3dab-ae81-2f92ce9bc24c | -7.5162 | -45.3024 | 2026-10-09 18:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| dce62512-5f99-3304-8e05-29e3ea7bbb97 | -2.4988 | -56.1462 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 92f8600f-e9fe-3adc-a42e-ecc67f4c0163 | -3.6439 | -59.1721 | 2026-10-09 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| cc4e73d4-68c9-3076-8770-96030d0b5f65 | -12.8303 | -44.6239 | 2026-10-09 18:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 33fdb9cd-0de9-383c-84dd-48920d0f704d | -3.6623 | -59.1525 | 2026-10-09 18:40:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 38fe5b2d-4620-3754-b5de-9debde3e0707 | -13.3865 | -43.8708 | 2026-10-09 18:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 287.8 |
| f993c9e0-7e1d-304d-b048-149ba4c0b6b4 | -3.9311 | -55.7179 | 2026-10-09 18:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 14392767-d654-32be-9921-f3b250fde5e1 | -2.4259 | -55.9901 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 32d15c36-4303-3f75-b523-442704e5b6b9 | -7.1827 | -52.6078 | 2026-10-09 18:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 1fd7d149-f88a-39aa-91d0-a42ab7a63655 | -3.1697 | -58.6244 | 2026-10-09 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 6c087cf1-d330-3e9a-af81-4a84bf382c97 | -9.0362 | -44.3654 | 2026-10-09 18:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 126.1 |
| dd801b9b-dbd8-3418-a296-0e99ed18adbb | -2.4623 | -56.0682 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 65cd1209-d204-37ad-b139-8cd53cc87366 | -3.1972 | -50.5592 | 2026-10-09 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a69f4a80-a91a-37e2-944b-c5df5c5c0b48 | -2.9266 | -54.0903 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 467a85b7-3a31-32bb-8227-0f00d2ae6b28 | -18.3327 | -42.3849 | 2026-10-09 18:40:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 235.8 |
| 99bc6230-4e6d-39ab-bb01-a51479617643 | -12.5446 | -47.5875 | 2026-10-09 18:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 000866ba-cbbd-3e3d-b07a-d0ce944716c4 | -7.3361 | -50.0286 | 2026-10-09 18:40:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 4c55cdc6-3cd6-3632-9ee6-c60c861f03f9 | -2.5492 | -58.0179 | 2026-10-09 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1c8bf001-ee31-3e59-9646-4dc03f726a57 | -9.9004 | -44.8839 | 2026-10-09 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 145.2 |
| fd6c2830-ea6a-36aa-a0cd-1714774003fc | -3.0559 | -53.886 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| cfa23c85-2b01-37aa-8d71-023f48d0bd22 | -7.5908 | -47.0423 | 2026-10-09 18:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| a0e9482e-5740-3158-a325-b95f452ab74b | -3.2577 | -54.0217 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| eaa142e1-c2ed-3b99-a9d4-92dd5cd87a41 | -12.2504 | -44.7631 | 2026-10-09 18:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 67909fa8-bc89-3127-84bb-b8e5d327a08b | -3.0375 | -53.8865 | 2026-10-09 18:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| b60aef4d-ea6e-3dc1-ab98-85e420314a65 | -3.1787 | -50.5807 | 2026-10-09 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 443ad416-8848-379d-969f-3c5ec42e2314 | -18.3132 | -42.365 | 2026-10-09 18:40:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 146.0 |
| b90b4dc0-0bf9-34f5-9bed-9ead2fccf668 | -14.0467 | -43.846 | 2026-10-09 18:40:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| b8d58efd-5239-3bf4-ab79-eec8fbf7d9cf | -1.8416 | -54.9503 | 2026-10-09 18:40:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 30074bfb-4da6-344b-9e4a-39ec8c79e508 | -11.5874 | -45.3931 | 2026-10-09 18:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 31807427-9eb7-3b38-9c39-430993f44a75 | -10.9388 | -45.3687 | 2026-10-09 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 307.2 |
| e1bdac45-0388-3272-a90e-605f10335a7b | -3.3455 | -50.4078 | 2026-10-09 18:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 4f88584b-9cdf-3dcd-9cdb-8b33bb150e9f | -4.7219 | -55.6727 | 2026-10-09 18:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ab0e15c8-bca3-3ca2-8b06-64224036b34b | -6.5826 | -43.034 | 2026-10-09 18:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3a78df8d-adaa-3a8f-8efc-66c1e6d6fcc0 | -9.9977 | -45.9893 | 2026-10-09 18:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 687525d5-4f45-348f-ab60-78d90cb4dbce | -10.4917 | -47.2087 | 2026-10-09 18:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 1338adb8-f516-345d-b698-3498735b65cd | -3.1879 | -58.6433 | 2026-10-09 18:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 325a3541-9ece-3796-881e-8c3f1144fa02 | -3.5193 | -58.0183 | 2026-10-09 18:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 9c7d0122-5c6a-389b-93c7-ff08ad45a643 | -14.4339 | -43.9396 | 2026-10-09 18:40:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 214.8 |
| 74d6fd8e-0462-363f-8f38-c807cbf74127 | -10.2486 | -49.6851 | 2026-10-09 18:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| c3f208de-2928-3bf3-bddb-154d5e23b135 | -16.9672 | -41.154 | 2026-10-09 18:40:00 | GOES-19 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 144.3 |
| 739dfad0-c324-37d7-91bf-d1e47cb0d3e4 | -15.2732 | -42.3699 | 2026-10-09 18:40:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 228.1 |
| 974ef4d5-6fc4-3b1a-94a3-17c1000bb11b | -2.8997 | -56.9423 | 2026-10-09 18:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5e107cfe-5976-3e08-84e9-cd4a523ffe9d | -10.4724 | -47.2333 | 2026-10-09 18:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 7574ef32-ee25-3208-add5-76c1cff7f036 | -10.9575 | -45.389 | 2026-10-09 18:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| de336d64-4c42-383a-a7a4-dae646604ec2 | -2.4623 | -56.0879 | 2026-10-09 18:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 05eb06f5-5074-3200-8244-d88e787e0496 | -11.6194 | -43.5959 | 2026-10-09 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9ff1811f-bd5e-3f88-9d40-4cceb3952b8d | -3.2137 | -42.953 | 2026-10-09 18:40:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 02e919ad-d27e-3ae4-8cd6-38c8d62c606a | -2.7428 | -54.1146 | 2026-10-09 18:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.2 |
| aa6103d6-af1b-3545-991f-2574af27e1a5 | -11.47 | -43.3824 | 2026-10-09 18:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 293db85d-e1a4-3822-bb8e-8a0868d7b42b | -10.5087 | -47.3401 | 2026-10-09 18:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 2af87d3c-6e45-3225-be98-207564d205f5 | -2.2113 | -53.7029 | 2026-10-09 18:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 522e24a9-fd1e-37c7-a577-c53a2a6c7780 | -12.0453 | -43.4102 | 2026-10-09 18:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 2d19c095-84f7-3239-82de-2b9f6aa84ca6 | -0.7398 | -57.9598 | 2026-10-09 18:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| f06e2590-d594-3b89-82f3-23779efc73bb | -4.6113 | -55.7162 | 2026-10-09 18:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 2ba16917-c7eb-35b1-baf9-c8ab7ee234dd | -9.8795 | -50.5131 | 2026-10-09 18:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| f886fcd9-1883-34a4-a6b2-692b9603597a | -7.4697 | -42.8315 | 2026-10-09 18:40:00 | GOES-19 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 4d79da10-eeec-3ec5-9635-31836dc787dd | -14.3611 | -55.0114 | 2026-10-09 18:40:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 163.7 |
| bb29e48a-b54e-314e-b80f-c1a3453650ad | -9.9398 | -44.7869 | 2026-10-09 18:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 1de30c95-f7c7-361b-9346-06b2aa517b13 | -9.9788 | -45.9916 | 2026-10-09 18:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 72e65ddf-c9db-380d-b646-63f7e22830fc | -9.0173 | -44.3676 | 2026-10-09 18:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 183.4 |
| d39c7663-8dd3-3dbc-bd53-eae2a0c67bbe | -5.8715 | -38.9898 | 2026-10-09 18:40:00 | GOES-19 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 15082742-3958-33f0-bf07-3a3c9d06ad25 | -7.2283 | -44.1622 | 2026-10-09 18:40:00 | GOES-19 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 9c8b9f42-dbe4-3b0e-b174-a2fb9051c0d3 | -15.8531 | -42.0202 | 2026-10-09 18:40:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.7 |
| dac25b51-800e-364e-a6a2-8a13d6c0e459 | -6.4909 | -46.6 | 2026-10-09 18:40:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 229d13f0-6268-303a-a1f0-8687d2b9d5fa | -2.5125 | -58.0765 | 2026-10-09 18:40:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| a5751f5b-c5de-3de6-ba92-0359654fbe2b | -12.208 | -43.9512 | 2026-10-09 18:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 86.6 |


[Clique aqui para ver as próximas entradas](README294.md)
