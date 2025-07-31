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
| 4b43c808-ff04-38ca-be83-cc3ed970385f | -6.4765 | -56.2132 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d9464b-c918-38a6-8e74-98dc2a82bf86 | -11.0866 | -48.637199 | 2025-07-31 00:31:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e137ba87-eb69-3a8c-842c-bb35cd8dad77 | -7.7035 | -51.0895 | 2025-07-31 00:31:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 136c8291-8257-30a8-91c4-db903e6b1852 | -9.1924 | -48.6022 | 2025-07-31 00:31:00 | METOP-C | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af65a603-956b-3a4d-a154-27975fa7cdf3 | -7.0845 | -44.901402 | 2025-07-31 00:31:00 | METOP-C | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8d921826-9046-3571-8f60-faf7b92d8c10 | -10.5665 | -43.308998 | 2025-07-31 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c740a129-38cf-3264-b97a-0ce48940046a | -8.9155 | -46.745098 | 2025-07-31 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74aa42e8-ca11-32d4-90bc-daf1d9a27c8d | -13.4757 | -45.6866 | 2025-07-31 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 369f8c1f-bcc9-3bda-922d-f69d341406e6 | -12.669 | -47.794701 | 2025-07-31 00:31:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2711718b-6842-3a12-b3b8-06419502f338 | -6.4851 | -43.341301 | 2025-07-31 00:31:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2969e6af-df98-36e3-83b1-9388be4f4295 | -4.2696 | -48.109501 | 2025-07-31 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1deb3841-9ef8-3484-af7f-7dd0332675e1 | -8.9172 | -46.7523 | 2025-07-31 00:31:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f83bd97f-e4c4-34f2-b12b-f46ea9d9e556 | -13.4774 | -45.6478 | 2025-07-31 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a2c9136-1da0-3050-93d6-e6fb77c433cd | -19.1483 | -43.497501 | 2025-07-31 00:31:00 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 60a75bfb-37b3-3cc3-988d-ec996e2bae50 | -8.8849 | -47.346001 | 2025-07-31 00:31:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3d51212-7eb7-31e2-9644-1cd8669ec2dd | -5.4514 | -44.398899 | 2025-07-31 00:31:00 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8ff8ca7e-25f5-3f61-b79f-ed04771d4568 | -11.8856 | -44.560398 | 2025-07-31 00:31:00 | METOP-C | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94cd40c1-476d-3585-906f-c4dc68bf4bc4 | -8.5559 | -45.515999 | 2025-07-31 00:31:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b5281e15-d96c-33ee-880a-89bd3d57d1f6 | -10.6657 | -48.871799 | 2025-07-31 00:31:00 | METOP-C | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 61f95957-7ca1-39bc-9433-9e22e76a2ef5 | -10.5681 | -43.316299 | 2025-07-31 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b268c4f9-b1cc-3098-a457-8a74bd6e435c | -16.093201 | -46.8876 | 2025-07-31 00:31:00 | METOP-C | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 305cadb9-fbc5-3c0d-a891-b6f57aba7729 | -9.3551 | -45.494701 | 2025-07-31 00:31:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4bbb405-1c7c-36ce-bb25-6d5fcc3c0650 | -6.4758 | -56.161999 | 2025-07-31 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9ac5134-76a6-3ffc-aa5f-94a4eedaf423 | -8.1345 | -45.0257 | 2025-07-31 00:31:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1fc11d0c-fe24-3bd0-8729-1fa627bebe36 | -8.1247 | -45.027901 | 2025-07-31 00:31:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fc9ac266-163a-34f8-94ad-71785fc0d081 | -10.4941 | -42.557098 | 2025-07-31 00:31:00 | METOP-C | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b6198405-9004-3de9-a390-1459b31d0673 | -8.5574 | -45.5229 | 2025-07-31 00:31:00 | METOP-C | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3c0acd09-ef93-32bc-bdd7-7aebcd3e3cc9 | -13.4725 | -45.672001 | 2025-07-31 00:31:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7808b6d3-2df9-306b-b2f6-e70914d84de6 | -11.4965 | -44.254902 | 2025-07-31 00:31:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 108395fd-c45f-3b3f-b925-683c03f7463f | -11.7052 | -48.176399 | 2025-07-31 00:31:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2763907c-60ea-3120-821b-6d4a8fce5099 | -18.507799 | -46.693901 | 2025-07-31 00:31:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dcf313fe-c025-36bf-9f85-d05ad691825d | -10.0137 | -46.546101 | 2025-07-31 00:31:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 977d7a5c-2700-31bc-a82f-b1b49a43896b | -6.683 | -43.8801 | 2025-07-31 00:31:00 | METOP-C | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a127d65-9ca7-33b7-b198-92d7ef464883 | -10.605 | -45.233002 | 2025-07-31 00:31:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c93007c0-35d1-377e-8c14-be2f3621f7e4 | -14.6685 | -47.858398 | 2025-07-31 00:31:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d7632e5-58fa-3b9d-aa4a-464a0ed3dd68 | -11.0905 | -48.655399 | 2025-07-31 00:31:00 | METOP-C | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5c0a7676-ee20-3197-a74b-6b84552158b1 | -9.5997 | -43.859402 | 2025-07-31 00:31:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0189ef74-79df-36b7-85a3-907e37d880df | -10.8947 | -44.510799 | 2025-07-31 00:31:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b610aae1-9ead-3369-8aba-fd1160deacbe | -8.1215 | -45.014198 | 2025-07-31 00:31:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3dbdbeb9-a069-3510-bc6f-9f2069d2bf6c | -14.8166 | -49.279499 | 2025-07-31 00:31:00 | METOP-C | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bc49152e-a536-3fe2-a141-046b71fc3ea1 | -6.5862 | -47.285099 | 2025-07-31 00:31:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3345c55e-24a7-3698-bff7-895a74b4f68a | -13.1746 | -47.234402 | 2025-07-31 00:31:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ad03a56e-1ba7-396f-8c38-e2e10a236610 | -16.326099 | -52.6633 | 2025-07-31 00:31:00 | METOP-C | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eb3067d0-2257-3288-8f7e-03506e531e2e | -10.0338 | -53.863098 | 2025-07-31 00:31:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f862bfa-5636-31e6-98f6-ae71bc4446ab | -10.5698 | -43.323502 | 2025-07-31 00:31:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b9a8825-6db7-3dd8-8616-1eae62333235 | -10.0153 | -46.553299 | 2025-07-31 00:31:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 07f443bc-1791-390f-b717-848c5fe275f1 | -12.5119 | -44.731602 | 2025-07-31 00:31:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 689f806b-1f81-3525-ae3c-cff07000200c | -11.9482 | -41.408298 | 2025-07-31 00:31:00 | METOP-C | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4a471b7a-1c50-34b4-8150-e0b588495313 | -3.7937 | -48.963699 | 2025-07-31 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fe0289a-d470-3f17-8b13-8de3a1a1d374 | -6.5879 | -47.292301 | 2025-07-31 00:31:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 11e79ef2-4b65-395a-9698-835e2c1fbcaf | -18.509701 | -46.702999 | 2025-07-31 00:31:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e6ab4b99-af04-3a10-bfcb-3681e836334d | -6.4833 | -43.333698 | 2025-07-31 00:31:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f37761fd-7515-3565-802c-352785f0d2ac | -7.8428 | -45.554298 | 2025-07-31 00:31:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 67d9fd00-04c1-3f80-9224-b0ee0799199b | -18.499901 | -46.705101 | 2025-07-31 00:31:00 | METOP-C | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2868838c-5223-3432-a1f1-c49324dfd65a | -10.5787 | -45.253601 | 2025-07-31 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 33abe14d-d78a-3450-a799-1607e4d79112 | -14.6704 | -47.867699 | 2025-07-31 00:31:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c61cf18-ba64-3895-b960-a6e21c74bf39 | -5.4595 | -44.3895 | 2025-07-31 00:31:00 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc23c908-bf9b-33bd-a48d-4209dd820008 | -18.5718 | -43.779499 | 2025-07-31 00:31:00 | METOP-C | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 59c54dd4-94c4-3b1c-8b6a-de5c59b6b3c2 | -11.7109 | -48.202801 | 2025-07-31 00:31:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 60757bfb-ea9c-3e42-9b1f-215c38c96934 | -3.7919 | -48.955898 | 2025-07-31 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d2735b4-67ac-3b66-b190-5dfeb033349f | -5.453 | -44.406101 | 2025-07-31 00:31:00 | METOP-C | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cc416287-aa1b-396f-9612-c9f0caf9e016 | -10.5689 | -45.255901 | 2025-07-31 00:31:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aac96169-0eb2-37f6-9412-3724b172fba3 | -11.7071 | -48.1852 | 2025-07-31 00:31:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a9d6e2fb-8b0c-3bdc-abca-a9008766b5b4 | -13.6371 | -44.2365 | 2025-07-31 00:31:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 443d4f33-de0c-3946-9159-222ae7d6e11e | -10.1781 | -47.991901 | 2025-07-31 00:31:00 | METOP-C | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b36efacf-7262-3035-bce4-94a36283a0d7 | -13.5044 | -45.6726 | 2025-07-31 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 132.5 |
| b5081eb2-2fda-3b57-914b-b06dab12e113 | -6.526 | -56.1923 | 2025-07-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| fbaf67d2-2fbe-3a20-acb1-ea837fa3190e | -6.6726 | -56.3831 | 2025-07-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 86685e7d-bab4-3c4f-a8e1-849204f1b051 | -10.0843 | -53.8712 | 2025-07-31 00:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 82cda16e-0e8f-33bd-a370-024a7e299546 | -11.7508 | -48.1825 | 2025-07-31 00:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 473b549f-b800-32dc-a86f-255917e9a77c | -6.5258 | -56.2121 | 2025-07-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| e4e8c711-656a-3820-a0ad-5c0cca8bc3fb | -6.654 | -56.4038 | 2025-07-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| c5748b6c-8490-318e-b4fe-8d89588506b5 | -6.5629 | -56.1906 | 2025-07-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 2da5a191-49c4-31ab-86ab-bb1cb3b3bbc2 | -5.5011 | -44.3956 | 2025-07-31 00:40:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| c8126dee-5e30-3d92-9131-bcc97392cc78 | -6.6725 | -56.4029 | 2025-07-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| cf4d112f-bcea-3ec2-8d18-85a3a2a5756d | -6.5445 | -56.1915 | 2025-07-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 080b04fd-a820-380a-b5af-f671839bc6ab | -10.0655 | -53.8727 | 2025-07-31 00:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| bac2fdb7-d4ac-3a36-b2b5-2b5711e5170e | -13.5238 | -45.6693 | 2025-07-31 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 921e18b0-9f9d-345a-816f-bfbb62ffecc7 | -18.5328 | -46.6973 | 2025-07-31 00:40:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 43.3 |
| b847eaa4-de6d-3bb5-b53f-1ff941c467c7 | -6.5075 | -56.1932 | 2025-07-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 8683c7a7-d8b1-3949-91b8-142d773feb4a | -13.5049 | -45.6494 | 2025-07-31 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0199369b-602e-346d-970f-6b9953cbb4e2 | -13.5243 | -45.6462 | 2025-07-31 00:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| dc4aa240-2c70-3c22-bb69-e2c0c8fdc2aa | -6.5074 | -56.213 | 2025-07-31 00:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 10cf2130-ddea-3159-9113-896ccd92849c | -14.866 | -49.2832 | 2025-07-31 00:50:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 84eff511-dd0d-37fb-8cc0-96963b7f7e3b | -6.5258 | -56.2121 | 2025-07-31 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| bd2ae4e4-b270-3fa4-9e3d-2ea8317298a6 | -18.5432 | -52.032 | 2025-07-31 00:50:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 41.8 |
| e215881a-7364-37f8-8fcc-2c1b1eddd34a | -13.5049 | -45.6494 | 2025-07-31 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 071f3909-3fa5-3c4e-ac1d-ff3492eac161 | -6.526 | -56.1923 | 2025-07-31 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| ae901d18-8662-343a-ab17-1bef3c2d35a4 | -10.6169 | -45.2512 | 2025-07-31 00:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 7672b58e-e1a1-34ab-986b-8c28c8821c4b | -10.0843 | -53.8712 | 2025-07-31 00:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 74699f9e-2a82-34f5-a3af-8024168393ab | -7.5969 | -44.8165 | 2025-07-31 00:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3ffd5130-aa32-3802-a11e-0d66e20e948e | -6.6725 | -56.4029 | 2025-07-31 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 133.5 |
| e6cb22e1-25d6-38a2-8bee-33954b7c26b3 | -6.5629 | -56.1906 | 2025-07-31 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 18722d68-fc4b-3a35-bf99-213bed0a5923 | -10.0655 | -53.8727 | 2025-07-31 00:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 51a1b31c-9582-36ba-b2dd-59704810204f | -13.5238 | -45.6693 | 2025-07-31 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 669db5f9-a7d9-34ee-bc4e-f66502fec942 | -14.8465 | -49.2863 | 2025-07-31 00:50:00 | GOES-19 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 1a1f369a-7714-34b3-bc23-b1e86a70aed5 | -13.5243 | -45.6462 | 2025-07-31 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 33ddfdfc-6a5b-3b21-a92e-f7ce7ac736ad | -6.654 | -56.4038 | 2025-07-31 00:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 3540725c-762e-3549-81cd-4a02113f0d15 | -5.5011 | -44.3956 | 2025-07-31 00:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| db589662-1dd3-3533-a864-683c8e539c0c | -11.7508 | -48.1825 | 2025-07-31 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 93.2 |


[Clique aqui para ver as próximas entradas](README4.md)
