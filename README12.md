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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dabb71e0-650a-3f33-8730-8518ae2efa54 | -3.02995 | -53.26717 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| f64f2e4b-6571-35bf-ad29-9fbb4247811e | -4.95556 | -47.59756 | 2024-11-07 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7b4c492c-428f-33ec-90fd-8b77aedd98d2 | -2.93332 | -52.55271 | 2024-11-07 00:56:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e382085e-5d7a-3e0b-b4d4-36bffffa91cf | -4.29214 | -48.64924 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7325d16d-0c89-3b30-b772-9236e4589ce4 | -3.59033 | -50.22594 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 86f92f3e-5716-3141-8ed7-bcc41c92c5b2 | -1.86497 | -47.82852 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 8eb9c2d9-45a4-3f9b-968a-3361f3671724 | -4.08616 | -51.01856 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 69f5bffa-1531-3cc5-80ff-78e08252fa1f | -5.38156 | -46.26685 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 21090075-dfe2-3e5f-b99d-319e754ae71b | -2.18059 | -48.37375 | 2024-11-07 00:56:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f881f48-d7ab-382d-afb5-959e570ebd4b | -2.80806 | -51.49461 | 2024-11-07 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fd6479ff-7db6-3947-963a-7fb97857088e | -3.11206 | -53.71434 | 2024-11-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fd0eadf6-685f-3e99-8eb1-da79984f8b2d | -2.05059 | -52.08118 | 2024-11-07 00:56:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 07c43603-c0af-319d-92e9-febe50aac7b4 | -1.80968 | -46.98509 | 2024-11-07 00:56:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3f8c55c0-c3a6-36b1-9da0-aa91e3922f62 | -4.02085 | -48.28802 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ca6a0ba3-90e0-3036-9713-2dfdf027f87a | -5.11117 | -43.97518 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d7d913e5-b2c4-3faa-8428-946f9b7c926b | -3.04034 | -53.26577 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8e747e49-44a5-31ba-a34d-c5cc15341dc6 | -3.95055 | -49.44003 | 2024-11-07 00:56:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f715caf2-4034-3de0-9ad4-b29d0a846ac6 | -3.7221 | -52.26596 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c8f0556c-3f75-3c31-a5d2-8586feca693b | -3.34637 | -50.25412 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8408d11-fcdf-3a28-964a-c9c9842643f3 | -5.59465 | -45.20638 | 2024-11-07 00:56:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 99d7a573-3933-3c25-b061-5a5e2ad13e3f | -5.61419 | -43.94731 | 2024-11-07 00:56:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9d22fa28-7b79-3f6d-9f51-4751df6816c4 | -4.37227 | -47.24801 | 2024-11-07 00:56:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ca955501-f964-3a21-a5ca-467ac4c07710 | -5.1465 | -47.71012 | 2024-11-07 00:56:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 41b38a91-2559-315b-bb7c-53562fe84d4f | -3.22429 | -50.37492 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| b9413b4b-df2a-347b-b6c7-e9c0764040a5 | -2.3138 | -48.1431 | 2024-11-07 00:56:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d74bcad1-67bb-33d9-bf2b-550548c7cfdd | -3.25352 | -53.40392 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| dd097298-8b28-3bfb-8f91-3f7a2a64c8ce | -5.46616 | -47.04951 | 2024-11-07 00:56:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1c72ac09-9d8d-3f8c-bd00-c623dafaf204 | -2.74211 | -51.89478 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 51c2c318-d718-3b69-99e7-4312abc26f5d | -7.84344 | -48.20421 | 2024-11-07 00:56:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2c834051-5908-3a79-95e8-56997949ac4c | -2.76047 | -53.23566 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 22f8dee3-e58e-3e43-a67f-513b1f5c0343 | -6.04108 | -46.60295 | 2024-11-07 00:56:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6500a127-89ea-30ff-9d89-f67764420c4f | -2.24737 | -53.67536 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b61e2300-afb5-31d5-8091-f22a74c3335f | -3.01461 | -53.23165 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 5a0b4a88-a3b5-3a14-b508-10f1fc5bfc6d | -3.33089 | -49.02515 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| e3840487-c04f-3b34-838d-39b80c08be0d | -5.44177 | -43.57098 | 2024-11-07 00:56:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ada6c229-ed87-3d81-aa1a-fb00a04e4209 | -1.48423 | -47.21938 | 2024-11-07 00:56:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 70694251-e18d-3a35-8c00-cb9e125531e0 | -4.24161 | -48.54727 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 55b839a0-a3fe-3522-9e4d-5dbcd783bcc9 | -5.9657 | -45.36516 | 2024-11-07 00:56:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d8948058-1f47-3c53-a065-16eb3c5f1848 | -2.23304 | -48.02635 | 2024-11-07 00:56:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ea1c0e24-0489-3d3e-bc9d-8219801d0bc3 | -2.78275 | -52.87434 | 2024-11-07 00:56:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 80614418-59a2-3f5f-aef8-c6a941e3317a | -6.2916 | -47.20503 | 2024-11-07 00:56:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 32920928-4ea2-3f23-aa6e-0296ac859685 | -2.82411 | -52.95182 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| cf6bb7e5-45bc-328d-b257-2a91827f0189 | -6.45851 | -44.67529 | 2024-11-07 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4ffc1e8d-672e-3df9-b7b9-124478f488e9 | -7.43758 | -42.54455 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 84ce3495-b4e1-31ab-b04a-35b7173fa857 | -2.22627 | -46.53397 | 2024-11-07 00:56:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 4b07c199-94e0-3317-9d9c-c9578821db80 | -4.46664 | -46.51674 | 2024-11-07 00:56:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 1d8afad8-642b-32b4-9b9a-25e766a7c738 | -3.34761 | -50.26307 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 69fd7a92-857a-344c-bc88-e0b400f4c7da | -3.36959 | -49.75632 | 2024-11-07 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3bd893fc-4a52-327b-bd2e-96db7cdb3fc0 | -2.08281 | -52.03522 | 2024-11-07 00:56:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9d9baa0b-d762-3e0f-80f6-cc5327e3e212 | -5.77464 | -46.16219 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5ca00300-9174-36be-8c9b-b99fab7999d3 | -4.22371 | -48.61352 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 93aaa119-46c8-3427-a6bb-15735b7b8d6b | -2.60853 | -48.2069 | 2024-11-07 00:56:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3a4babfc-1ef5-3722-9380-203046a00ba5 | -3.43835 | -50.2536 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0764d38f-a03a-33f7-a405-6e028f97419e | -5.98794 | -45.37435 | 2024-11-07 00:56:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 43e4a693-6b1f-3246-97aa-d3aa691aa358 | -2.84813 | -48.66364 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 79164874-65d9-3585-90d0-b0f23dc6bd37 | -5.61941 | -45.93338 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7ec88d05-a481-3c74-886d-44908780cddf | -2.38817 | -49.39064 | 2024-11-07 00:56:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 78be2113-239f-33f2-b6f5-3cc80d0065d6 | -5.22732 | -44.91821 | 2024-11-07 00:56:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| e6a410ad-821a-3500-af0c-a97d87486a75 | -2.8391 | -49.464 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 079d9e5a-745a-3af4-a4ef-ac7ae92b5b3c | -2.66848 | -51.81826 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| aa3d1fe9-fd1a-3862-a4e5-fc4b7ac58f7f | -5.44322 | -45.1382 | 2024-11-07 00:56:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d0a7bc9b-4296-331a-a919-badc00a785d3 | -5.84227 | -46.26694 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 91965247-a242-3c4a-8643-fde167426af0 | -4.35248 | -48.6166 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2a5a260e-87e9-30d7-b4ad-855a1181fa96 | -5.95004 | -39.67794 | 2024-11-07 00:56:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 58.4 |
| 25c14711-366a-30d1-9fe7-aa6fbbd394b5 | -4.35498 | -48.63446 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c99d78da-01a5-30b4-b833-e9670b512890 | -2.97164 | -53.86992 | 2024-11-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 963226d1-3bf9-333a-a814-5ea8577a53e3 | -6.86106 | -47.9761 | 2024-11-07 00:56:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aaa75945-6ae6-38b4-8c11-2c7999c74272 | -4.38508 | -50.84264 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4c8714fc-d3d6-32fe-8b97-4f4fcf2df263 | -4.07072 | -48.3179 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0121bf81-ced9-31eb-b98a-18e5d9a98aa0 | -5.84995 | -46.6222 | 2024-11-07 00:56:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d84d6a0d-cd70-3334-8207-996434fd3b3c | -6.24897 | -43.56752 | 2024-11-07 00:56:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 8015e466-0cff-3cdf-b88c-3ee2ce74347f | -3.51293 | -50.46365 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fb491be4-2082-36c0-bccf-774b67a715ff | -3.00464 | -53.44368 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4ba2c0fd-21b2-3392-ae6a-c34060c0c298 | -4.1113 | -48.86826 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| c85284bd-b50f-311e-a452-9e802e115aa9 | -6.55624 | -39.66797 | 2024-11-07 00:56:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 75.4 |
| 38083fa2-1bee-36f6-b9ec-04b4d30b38ed | -9.34685 | -48.95313 | 2024-11-07 00:56:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc3bc15f-cd7f-3c55-8ab1-64bf97e759c9 | -6.96195 | -39.81033 | 2024-11-07 00:56:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 2834d09c-8876-318f-a988-76a64c67d984 | -3.95451 | -48.14579 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 06dc96cb-eed8-3d90-84d7-ea80a6fb9577 | -3.30321 | -50.08458 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 03a65fd0-98de-3a76-a369-d6ef60a633d3 | -4.46271 | -46.51263 | 2024-11-07 00:56:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 147a5976-449c-3479-89f8-5a31caba7363 | -3.22473 | -53.11561 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 23dc50f1-3c0f-370b-9ee4-2ca5c833eef1 | -3.24896 | -50.01981 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1d43101d-0f35-325d-89b4-a85abae0ad0c | -2.18314 | -48.32622 | 2024-11-07 00:56:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0e4914bb-a37c-391e-be70-fc0d9ad7aad4 | -4.24036 | -48.53834 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 78b35af1-84a5-39d7-b618-465b9a33d371 | -3.09612 | -53.92455 | 2024-11-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 23dcd1ea-cb5f-3b73-b2ce-e4cf6596bd9c | -3.29433 | -50.08582 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 0b94ec6a-6363-311a-b450-4db2485aa532 | -2.8064 | -51.80337 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 67b2fbd1-781c-392b-8b7c-8fc6acc57eb8 | -2.885 | -48.73169 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1e35c98f-f801-3016-8fcb-75c4ad7e0b91 | -5.04139 | -44.75141 | 2024-11-07 00:56:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1fda3838-3efc-38ce-a8d1-0f209449b971 | -2.49632 | -49.11689 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 0c4c0eff-5b62-304c-af34-d992f10c7e68 | -2.44193 | -53.67567 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ad9751d2-333c-3a93-a568-cd53024a650e | -2.83789 | -52.90237 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| d52153ce-987b-362c-a08d-157cfd788f2f | -5.59648 | -45.21873 | 2024-11-07 00:56:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ee979c7f-dd07-391a-9a0b-736abaa97536 | -8.693 | -47.96276 | 2024-11-07 00:56:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0135920-3fd3-3c97-9901-cf8257e7bd8a | -2.39839 | -53.63494 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 36545c7b-d759-3711-b0c5-c22ae4f975b9 | -7.85354 | -48.21183 | 2024-11-07 00:56:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| e0408475-769d-3e0a-a49f-9fd2904d22a0 | -4.74095 | -44.41703 | 2024-11-07 00:56:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 27.0 |
| e3fab444-f83b-3278-85be-cb3b2fcf9ae3 | -3.37082 | -49.76514 | 2024-11-07 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2e11cf3e-5376-3eee-97b9-19c595656a98 | -2.72958 | -51.73247 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 356992a1-ce6b-3a61-a562-0729cb8b3223 | -8.03008 | -49.62758 | 2024-11-07 00:56:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README13.md)
