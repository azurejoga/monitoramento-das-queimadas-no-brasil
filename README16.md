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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| db51e73e-c043-3215-95dc-acc0d5e48760 | -1.37787 | -48.24649 | 2026-09-04 04:38:00 | NOAA-20 | BENEVIDES | PARÁ | Brasil | 1501501 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8b7b4a55-e233-366d-8bd9-56224bfddbb0 | -4.10753 | -51.02977 | 2026-09-04 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45007e0f-8c4f-3428-bb2c-062e031aada1 | -1.81144 | -53.97602 | 2026-09-04 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 04c15685-221e-389d-940d-cf28ce4dd972 | -6.09585 | -44.14639 | 2026-09-04 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 795fb46e-58ca-3274-873f-206c4ba74d88 | -5.84422 | -51.96124 | 2026-09-04 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e61b5e0-0c74-3fe9-a42f-8e23d922ba2f | -3.42788 | -43.2031 | 2026-09-04 04:38:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4cac951-0081-340c-a77c-7c6781c12cde | -6.11124 | -44.67934 | 2026-09-04 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f8735bd-aad1-3c16-b4e8-e8b4f9ca75f2 | -8.1018 | -42.59895 | 2026-09-04 04:38:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b7c2ff10-4fd9-3f18-9e8e-f06ccad01f27 | -3.29069 | -57.88258 | 2026-09-04 04:38:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a64f3e5-8d07-39f7-936d-37849ab4fd8e | -4.39112 | -50.9227 | 2026-09-04 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7ec59094-e375-3470-9afa-8a9e2e8e4fbf | -5.38259 | -54.44765 | 2026-09-04 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10cebd4e-aca9-3086-8a9d-d6ff2ffa4650 | -6.11785 | -44.68474 | 2026-09-04 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 826d542a-daa6-33e5-be9b-ba3979382da4 | -4.90567 | -43.47155 | 2026-09-04 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c8973b2-6661-396d-aba5-43dca20daaeb | -4.15397 | -54.16527 | 2026-09-04 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39d4e984-a253-3327-80ef-870a5b7ee443 | -6.35489 | -46.11444 | 2026-09-04 04:38:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56edf7d3-239f-36a2-9fdc-5ff10bf6803d | -1.69368 | -53.68824 | 2026-09-04 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f254ec97-cccd-3a35-95c2-fda69fa694e0 | -4.49499 | -42.55767 | 2026-09-04 04:38:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 972e7b7b-52ab-32ad-91cc-c7abbbed42c8 | -2.40555 | -57.90223 | 2026-09-04 04:38:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4caa168d-ee56-383b-8c21-a2e69ba4ba72 | -5.80292 | -43.62928 | 2026-09-04 04:38:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 993efda8-5ca0-3b5b-ab59-bf6f5de98b63 | -3.62515 | -54.60546 | 2026-09-04 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 009be2eb-1c06-3946-b509-dfb837e3de7f | -3.20416 | -48.72969 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ffbb8bb3-6dd5-3fc5-83ff-e834818b4ee9 | -4.48437 | -55.07984 | 2026-09-04 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 851210f1-4cb1-3d78-9778-8ae1df9597b2 | -5.82689 | -47.07518 | 2026-09-04 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba10073e-ba89-3f12-9b6b-1e316cb4f0e0 | -7.34869 | -45.47034 | 2026-09-04 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 92974009-691e-3c24-9fe2-6caf5a65237c | -4.66997 | -55.64211 | 2026-09-04 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75a0cddd-49b4-34f2-9be9-20791b7ed9c3 | -5.82628 | -47.03556 | 2026-09-04 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 121c9bdc-89f6-33db-865b-06c74eeff3d6 | -3.24222 | -47.24789 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 420f32d1-a997-3520-85d8-66bba46ad853 | -3.24539 | -47.91207 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f28a9f69-4dc0-3ad5-91ec-6980b5a29e9e | -2.51846 | -49.3601 | 2026-09-04 04:38:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1715cccf-8535-3efa-a2d3-6d05d7a82070 | -3.61174 | -60.56718 | 2026-09-04 04:38:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2b11b4a8-5dd1-3072-a27a-85a512880de7 | -6.67636 | -50.10736 | 2026-09-04 04:38:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fc3ae88-8d38-3819-9645-cd9654087c1d | -5.55215 | -43.42722 | 2026-09-04 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6932eb20-7f9c-3028-a32f-c5a44ca988fd | -5.82906 | -47.03959 | 2026-09-04 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ed4db24-66dd-33fc-b9bd-a9b07edafe32 | -1.47043 | -54.26537 | 2026-09-04 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 722ac848-f3a4-34fc-8f3a-7979694ad372 | -2.82938 | -46.72017 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85adb444-9d5c-3b3c-b4b9-c93af3c8628c | -1.0302 | -53.72204 | 2026-09-04 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc63d57e-f0e1-353d-a6ca-870a440bbfaa | -2.94902 | -51.28759 | 2026-09-04 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 290a540a-3939-3e20-afac-3003b758edee | -1.50407 | -54.97048 | 2026-09-04 04:38:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 764006a1-e583-3906-a442-26e6ed01755e | -6.30925 | -56.044 | 2026-09-04 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d33cf41-a5a3-3d23-8d3f-048017d6c6af | -4.39052 | -50.92379 | 2026-09-04 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f231af3-f719-326e-8418-769b993a843a | -7.45869 | -46.15216 | 2026-09-04 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd2ca84f-db27-31de-aec0-e219c86a1300 | -6.94278 | -45.18962 | 2026-09-04 04:38:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b68a39cc-5637-3c44-8296-d61a54ce422e | -5.3192 | -44.84393 | 2026-09-04 04:38:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f11dd1fb-3fcf-3405-aafc-00051258a46d | -5.38184 | -54.45213 | 2026-09-04 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0be54e83-59b8-33e9-85bb-d1e0f1726a8d | -4.1448 | -51.07447 | 2026-09-04 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5088b25b-5981-3ef0-b697-19c9c65270b6 | -3.06903 | -61.08187 | 2026-09-04 04:38:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b50f6309-9cd2-3abe-b114-c9f9bfb00240 | -2.32574 | -47.19825 | 2026-09-04 04:38:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3147fdea-7cdb-3687-bc53-1f7743dd5ca5 | -5.82573 | -47.03907 | 2026-09-04 04:38:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd59b826-1591-374f-b161-2404d3cf9b16 | -6.11422 | -44.68419 | 2026-09-04 04:38:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f70345ed-7958-30eb-9f52-0682f7a69932 | -4.62418 | -55.73301 | 2026-09-04 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0ee920d-703a-352f-99f7-1d48de61e86a | -3.43097 | -43.2084 | 2026-09-04 04:38:00 | NOAA-20 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e3165f4-f2d4-320e-92d7-c06bb0ee44fc | -3.67605 | -53.75276 | 2026-09-04 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a6343480-07a1-338b-a30c-273161d992be | -3.93499 | -42.99137 | 2026-09-04 04:38:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| eb6a370b-c906-3bda-a230-34f8f6e060bd | -7.34576 | -49.52936 | 2026-09-04 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6cefa87d-7331-3b3d-9e2a-c9e402fccf5c | -3.76916 | -49.12512 | 2026-09-04 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b357fd74-2c92-34d2-a424-5e00c835f7ed | -2.98172 | -49.27011 | 2026-09-04 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83c1c0bc-7435-355d-ac01-47e70e73f3a8 | -2.48179 | -46.85677 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 582faaab-72d1-3bd4-a80a-fa874d34a3af | -5.87972 | -45.5683 | 2026-09-04 04:38:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 30f2b6e2-06a3-3f5d-8635-350acc11b06c | -5.84202 | -52.06674 | 2026-09-04 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3deec221-2035-3d8b-b325-7a8389f18bb7 | -3.18428 | -48.01962 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf612466-95ea-377d-92fd-2bdcbfaaee12 | -3.24829 | -47.25237 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c53eeb36-9b0d-30b8-a6c2-2662e7f2d2ee | -7.34517 | -49.53294 | 2026-09-04 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fcd0d4a8-562d-38c9-8e73-9312bc66c494 | -2.83168 | -48.65273 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c1e22c6-a671-39a4-8a75-f7e30d34c6e3 | -2.03422 | -47.90215 | 2026-09-04 04:38:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 77321bf4-e964-3ef0-9abe-7e8d4beac851 | -7.17619 | -43.74407 | 2026-09-04 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6de6135e-e70b-32ba-b845-013581c6cbd9 | -0.92685 | -47.19289 | 2026-09-04 04:38:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 153296d3-3a26-336d-afc8-4bcca774cecd | -2.47848 | -46.85625 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0ea3082f-c32e-3a00-9687-4051d0a6cc7b | -6.31416 | -56.0449 | 2026-09-04 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e5a6614-034b-3d10-af13-4e5602e16b42 | -2.98858 | -49.27118 | 2026-09-04 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 29b89031-9c4f-3d57-8786-c5262d6ba2e7 | -5.91459 | -52.18805 | 2026-09-04 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cacbff38-2489-3e75-9b44-a3dfa923e021 | -4.10458 | -50.44505 | 2026-09-04 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9d0c8696-e211-3d09-ba0e-9f0b5ce66cf3 | -3.49807 | -49.72837 | 2026-09-04 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00d561fa-e1bc-34f8-9305-d879445f7490 | -4.49958 | -42.55476 | 2026-09-04 04:38:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6a5e6d75-ad26-30db-b3be-17dcf94bf85b | -5.82854 | -55.72718 | 2026-09-04 04:38:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 74c35b6a-2548-3f76-8fda-20f01be69ff6 | -3.19673 | -48.79832 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f595e106-8068-3f73-b061-ee3ed8cddcb2 | -1.79879 | -47.95129 | 2026-09-04 04:38:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 295ea94a-8e53-3637-93d6-438b55285508 | -3.21674 | -48.81268 | 2026-09-04 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ef803ba-c102-3770-9b00-ed2bef16e5c1 | -4.55679 | -47.76279 | 2026-09-04 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 588d473c-0ad8-3170-bfdf-033d32f53b03 | -1.24173 | -54.53267 | 2026-09-04 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c78ade50-4474-33be-ba56-208ad7dc1d8f | -4.97001 | -55.84864 | 2026-09-04 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 021d117d-0eac-38ce-ac2c-e77621b25e0a | -4.47874 | -55.08421 | 2026-09-04 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5800208e-380f-3df0-81dd-d2a9c522e990 | -4.4073 | -47.8483 | 2026-09-04 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c379c58-a99a-3958-9830-86db418e8b77 | -4.36529 | -47.7711 | 2026-09-04 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b2112929-cc43-37b6-bb93-65459a4f480c | -5.16941 | -56.18072 | 2026-09-04 04:38:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 440885c9-0676-3058-a223-1681c77c0c99 | -4.34829 | -55.03901 | 2026-09-04 04:38:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab238c1a-9f51-3a7b-8cfb-3ad1d1209da6 | -3.24552 | -47.24841 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 358dd4f4-ae1d-3074-a52d-0a0f2e9671c1 | -4.5655 | -41.95784 | 2026-09-04 04:38:00 | NOAA-20 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04dc5d6d-bea5-305f-86d6-dcaaeb24293e | -1.39249 | -47.57732 | 2026-09-04 04:38:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4113c162-6660-3a55-b548-42d7918c14de | -3.774 | -51.36372 | 2026-09-04 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13b7d1fe-abd3-37ab-94f2-d82bd3cef64d | -1.5058 | -55.68775 | 2026-09-04 04:38:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a873b19-6c62-3304-98c1-8ae17362597d | -1.47158 | -54.2681 | 2026-09-04 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f4fe10a9-e0ce-34f0-bab5-09f06c4f13f3 | -5.21669 | -49.10573 | 2026-09-04 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e5b395a-e6ce-3728-9a72-5d2cd6dd516f | -2.98515 | -49.27065 | 2026-09-04 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 88869510-3195-327f-b38e-1fcfc7726c87 | -2.26401 | -47.009 | 2026-09-04 04:38:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27f7da56-4e97-3b08-a75a-27d88f43fefa | -3.77509 | -47.55046 | 2026-09-04 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6ff36f9d-993c-3fc9-80e4-8d2b34a439c3 | -0.93071 | -47.18996 | 2026-09-04 04:38:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47a5d4fd-7528-3e27-944d-ec1f83eed68f | -1.5512 | -53.09863 | 2026-09-04 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1de35e4-2341-36df-9760-29a90f3c28d9 | -3.59763 | -49.86152 | 2026-09-04 04:38:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e77734e-ee4d-32fb-bd61-7f546b74e786 | -4.3642 | -47.77798 | 2026-09-04 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b952cbe8-77ff-328b-a456-dfd772d2b539 | -2.82884 | -46.72363 | 2026-09-04 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README17.md)
