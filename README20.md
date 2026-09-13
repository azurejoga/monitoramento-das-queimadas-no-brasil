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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f88cf14-62af-3981-a04e-25f9b059ecfe | -3.04756 | -51.25818 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44a45038-9c31-38ea-b5ee-c9e8a350fb96 | -7.15646 | -42.10221 | 2026-09-13 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f22392ed-253b-3f01-8354-6007b4a664da | -5.20177 | -49.33126 | 2026-09-13 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ecdfb48-1c83-3f9d-a690-23f89fe3520c | -7.46728 | -42.11284 | 2026-09-13 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 588bcc49-2374-3724-8492-2feff77fa410 | -6.05449 | -44.90509 | 2026-09-13 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ecd2481-575b-3d69-9843-9bde4061cebc | -6.23275 | -43.52189 | 2026-09-13 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0d63baf6-46ef-324c-976c-fb937f3e4a4c | -5.17642 | -49.34621 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 112ab118-cdfe-36de-a6fa-b1dbd129ba64 | -6.8792 | -52.84691 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6779c8d-bb88-3e5b-ab87-ece61645b9ff | -4.92513 | -45.83188 | 2026-09-13 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 99e28f0f-1522-30e0-ac50-6b26a28d6036 | -2.83111 | -49.22956 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8374272e-961d-33a3-821e-4557d8c0a8e4 | -5.90576 | -52.10423 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db86d4cc-9de2-3acb-9c4d-acdb9a3eec79 | -5.81751 | -53.7976 | 2026-09-13 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e119a3a5-bf19-3e20-9ccc-5d1c38efb79e | -6.08326 | -51.75713 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a322d20-494e-321d-9ff3-5488a6ace5c5 | -4.41297 | -54.86188 | 2026-09-13 04:14:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| cffbb1c4-0165-3933-bf3b-b2be5158c4fe | -5.1205 | -55.96969 | 2026-09-13 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3f726ce1-d39b-3519-b337-3ffe234afde2 | -6.54388 | -47.29108 | 2026-09-13 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 886e2111-f25c-334e-a43d-f5b7999a1752 | -7.38151 | -45.34827 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 01adf90d-90f9-30d5-95d0-1dac150df969 | -2.72259 | -49.79205 | 2026-09-13 04:14:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9edda39-021e-35a8-936b-5ac1dbf1b50c | -6.06797 | -53.49471 | 2026-09-13 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eab1208e-b9e1-399e-8fb2-6ffafcdfcee0 | -1.79436 | -47.83904 | 2026-09-13 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bf1f785-dfd3-305e-a648-6909e493a6a3 | -7.13867 | -43.75455 | 2026-09-13 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82fd83cc-ae02-3062-82ea-3b2befc2b1e8 | -7.75585 | -49.44181 | 2026-09-13 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb11e599-7e9c-3c48-af8f-c854def22fae | -2.83038 | -49.23415 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7167e699-ec00-3176-bd09-b59d5431c0d5 | -7.37108 | -45.36943 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7906601-1093-37da-89b9-db8e01988180 | -7.96152 | -43.99549 | 2026-09-13 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1450c4cd-d156-3f47-aacf-9a5e7928235d | -2.61264 | -54.76282 | 2026-09-13 04:14:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e095090b-777c-3253-9ea8-93dbfd144c1c | -7.02011 | -44.6366 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ee1aa794-51ee-39d4-ba00-958a9665f0e4 | -5.93601 | -46.35494 | 2026-09-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae005aa7-3f3d-3a35-9b9c-2c3c06e0cdb6 | -4.45217 | -50.16583 | 2026-09-13 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3ab594b-f5d8-3fb8-8ec2-1d2eb5886623 | -7.13591 | -43.75056 | 2026-09-13 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85b26ea2-2650-3f73-8b46-6bece36d736e | -7.37057 | -45.36973 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| d8aa9ee5-ee6b-34e9-94ec-5b927b981aff | -5.86236 | -46.22897 | 2026-09-13 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0752d817-c2c0-3ac8-995e-0375c62c0400 | -7.3769 | -45.35516 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e946a72-5a6b-3d7a-a65b-1073588ec406 | -3.95384 | -47.61818 | 2026-09-13 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cb29ef7-42e8-39d0-8d9a-9f374d1a10f3 | -5.77451 | -45.09563 | 2026-09-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c702bbcd-60da-3151-94de-74449ade4110 | -5.61359 | -44.85124 | 2026-09-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb7ad388-8fce-38c4-a6b2-3aed98d67a26 | -3.3323 | -42.29679 | 2026-09-13 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4d27a0f0-03ce-342c-baf0-3ecb9f3176ea | -6.87859 | -52.85048 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6f1ffe3d-7763-37b2-853d-c9092cc88908 | -7.53094 | -47.33849 | 2026-09-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 79fada5b-22fd-3917-b764-b5c284da1946 | -3.87383 | -51.19073 | 2026-09-13 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c55cfde-8897-3af0-bbdb-336f42ac198d | -2.79882 | -49.40429 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1f08e6fb-0b32-3e1c-9aff-c10d8d9d8f76 | -3.5497 | -48.17749 | 2026-09-13 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 822082e2-4e8d-3832-8d1e-ec409f2a1010 | -2.95203 | -50.39737 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e8dea29-871b-38d6-aca1-f9308585e7c1 | -8.74762 | -46.42989 | 2026-09-13 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df9c1811-9d92-3dac-acf3-7bc710d96ebf | -7.52795 | -47.33339 | 2026-09-13 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2db695be-a8c5-37e0-bcc6-51ec0f4f6cb7 | -2.9534 | -50.40548 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6bae1f3e-5199-3bd3-8fab-c62558281870 | -7.25605 | -45.55843 | 2026-09-13 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a08732ca-7fb1-31e9-8d8c-eac53b1e9e77 | -5.18082 | -49.34694 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95c02747-75ab-3087-96fb-e1f937c64f17 | -6.72392 | -45.41687 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 06b1b026-68b2-3b51-b5db-340d02b2e9d3 | -7.96097 | -43.99897 | 2026-09-13 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dab2433a-a92f-3685-987c-7b2271676e83 | -6.69449 | -45.90735 | 2026-09-13 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74d9ef60-0ba5-39fa-8477-ded64496f2eb | -2.84768 | -49.53845 | 2026-09-13 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd621cba-f597-3adb-aaef-90233cc67ea1 | -7.32134 | -45.56908 | 2026-09-13 04:14:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1997160f-6740-3513-95f4-a800391a617b | -6.76376 | -45.45398 | 2026-09-13 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6436bbc9-46be-3099-840d-158822b1f91e | -2.96675 | -50.39961 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 207bd12c-bb33-3989-8bfe-f389dbbf89e3 | -7.24848 | -46.70288 | 2026-09-13 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7b0d38b-c9cf-3f17-8199-2aa431b39928 | -7.98429 | -39.86919 | 2026-09-13 04:14:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0a0d7ad5-bf7e-3abd-ad44-6c1011aa85aa | -6.26953 | -41.95178 | 2026-09-13 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 81d39cb7-295f-3ce6-abf1-4ad7fdaa6b30 | -5.54438 | -44.46146 | 2026-09-13 04:14:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1460666-7580-3037-aae9-d575175ab1ff | -6.23111 | -51.69801 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76077f68-bea0-39d6-9300-1d7f0e318aea | -5.76707 | -45.09832 | 2026-09-13 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1df6afde-2876-3eab-a597-8d6a63eeed91 | -5.55247 | -43.43567 | 2026-09-13 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 715723b5-cb4b-37a6-80ca-b8c43c9051f6 | -5.61757 | -44.84813 | 2026-09-13 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea7e80df-a942-327c-b3fd-a6db3a89cb07 | -6.72387 | -50.46876 | 2026-09-13 04:14:00 | NOAA-21 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3197691f-8ec5-3450-9f85-a29cc01d74b8 | -7.15927 | -42.10631 | 2026-09-13 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e9a106a-fd12-3a51-892b-61bfd20542ec | -7.01789 | -44.62896 | 2026-09-13 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8cf92af4-5561-3081-9092-365ad9179c02 | -5.82262 | -53.80295 | 2026-09-13 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 57b554a8-affa-32f4-b929-f6b1b6e19248 | -8.05182 | -46.8434 | 2026-09-13 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f70a5b8-6ce5-33ae-a1ce-29f15128668e | -2.93958 | -50.39759 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0bd31e6-d792-332f-abf3-3876155297b6 | -7.28233 | -50.7821 | 2026-09-13 04:14:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d356c891-8a9b-3331-82e5-eee2f518c8a3 | -2.11408 | -47.12224 | 2026-09-13 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 704d10b9-1e97-3057-b9f7-1350568dc27d | -4.60608 | -46.31733 | 2026-09-13 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| af3f9172-c784-31a6-9e11-34253d67dd5d | -8.98048 | -44.39478 | 2026-09-13 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a49c9615-229e-33c7-8ee4-fc6f4550b35e | -7.97308 | -43.98664 | 2026-09-13 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d50cee1f-3e5a-3db6-86a2-713103a2ec45 | -5.02272 | -49.99318 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 34.4 |
| dd1fae8b-4a1f-3c4e-b6fe-e3cb7de1c4d9 | -5.48059 | -45.60104 | 2026-09-13 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27bacac8-f6ff-34b5-a65d-64f695db3151 | -7.19708 | -45.92151 | 2026-09-13 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e8c3b7c-0225-392f-813d-e6fd96be3e74 | -7.28688 | -46.23872 | 2026-09-13 04:14:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b74b8ba-b70b-3c49-84a6-a4c7c47ac135 | -8.28257 | -39.975 | 2026-09-13 04:14:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 29c01a82-fef5-31c0-a642-f9aeef7af3ff | -3.33176 | -42.30023 | 2026-09-13 04:14:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| e379f029-1347-35fa-a7bb-2868c33356d3 | -2.82965 | -49.23873 | 2026-09-13 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3b7881a1-7f8b-3efe-9d9c-b788320d0b49 | -8.97717 | -44.39426 | 2026-09-13 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb0c8cf9-baeb-34b9-983b-fb7030081bbc | -6.23216 | -51.69206 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d25c9133-1cf5-3573-b4a7-d699e825e027 | -3.45445 | -47.46369 | 2026-09-13 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95e5f0a0-bca0-3bcd-92a9-c28930f7340a | -2.94849 | -50.40476 | 2026-09-13 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0cc28b17-1336-398a-a84f-006350f98086 | -4.45688 | -50.16658 | 2026-09-13 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 196a993e-eb34-3e95-a39e-7c7dcc56d4e8 | -5.12084 | -41.07738 | 2026-09-13 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0bfada8b-604b-3a6a-83c6-fc9e55d2f052 | -3.57007 | -53.00841 | 2026-09-13 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aee96242-127b-3e05-9515-a5b5b0681efe | -5.12729 | -55.97073 | 2026-09-13 04:14:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8cd900f9-0dba-3e40-9a00-0ac9ceee0eb9 | -7.37971 | -45.35939 | 2026-09-13 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a22d3bc1-0f74-3982-ba22-dd0ec9d56047 | -4.92449 | -45.83585 | 2026-09-13 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 1308bba7-ae53-31bc-b2be-3fd22c73ed71 | -5.02653 | -49.99868 | 2026-09-13 04:14:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6dec4eb3-e7ae-36ea-9a69-8a6935b09465 | -5.49377 | -49.50508 | 2026-09-13 04:14:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bc6ffb3-51b2-3063-afc2-0d042e12ddf4 | -6.51751 | -42.23704 | 2026-09-13 04:14:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ff1c91e4-36b1-3d73-9d93-45d014114687 | -8.28323 | -39.97053 | 2026-09-13 04:14:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6b0a0b4e-c37f-36ac-8fe6-679057ab8a33 | -6.23618 | -51.69891 | 2026-09-13 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e8ebd5ef-3b5c-3197-aa8c-925598551d16 | -4.15353 | -50.21318 | 2026-09-13 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33c5e0ce-9ad0-35d0-ab1c-3dba9caa4629 | -3.05214 | -51.26971 | 2026-09-13 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b2d1877-9d98-3726-ac6c-27b0ee6812e6 | -7.09163 | -43.94614 | 2026-09-13 04:14:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 197b11d7-2d4d-3fe6-b440-35bccf7d89e4 | -5.12425 | -41.07793 | 2026-09-13 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |


[Clique aqui para ver as próximas entradas](README21.md)
