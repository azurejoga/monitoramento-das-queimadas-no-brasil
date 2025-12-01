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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61194a57-cd27-3526-8e21-6a3a0c381642 | -4.38333 | -43.16192 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3574d09-1b94-34fb-a2be-712505ba92e7 | -4.37205 | -43.15993 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 466b66d4-d485-340d-a0be-53602aa29039 | -4.39644 | -43.3397 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8de74ae5-4bf2-3777-a307-60119f296727 | -4.38463 | -43.15414 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0aa8f328-a300-3b64-bf2b-45c20d0c2ebb | -6.31279 | -43.80963 | 2025-12-01 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 34f0545e-b0fb-3b19-9ceb-3e78d1105b82 | -4.38336 | -43.14566 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 017484f3-278c-310c-bd4d-deb59770ba6e | -4.36705 | -43.15511 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2845e421-7c0e-3e52-b053-669101bb5ae3 | -6.31141 | -43.81724 | 2025-12-01 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8f83ebb2-36f1-390b-a8df-44913849df33 | -4.39276 | -43.32695 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 82057aef-8730-3ad5-8e35-4fc1e0e480c4 | -4.38067 | -43.16105 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16b6eb57-f70a-3bc8-8cae-a544b064dcd4 | -4.37364 | -43.168 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12873487-96b6-31d8-9051-0840e94bb205 | -6.31644 | -43.81119 | 2025-12-01 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0c87bddb-ca74-39db-b096-273a12befb51 | -6.31577 | -43.81501 | 2025-12-01 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0dfdc3e3-5836-3aaf-9135-cdff595a4415 | -5.33103 | -43.57 | 2025-12-01 03:36:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 33e8f482-4e19-30ab-b540-daf94a92a322 | -6.53722 | -37.7873 | 2025-12-01 03:36:00 | NOAA-21 | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a1ad0240-2c8c-3c0f-8cc2-9b7665310644 | -6.31209 | -43.81349 | 2025-12-01 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dc22041a-461a-3fee-a7ca-15f1eaf4db88 | -6.67147 | -39.89348 | 2025-12-01 03:36:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c07427d4-b1b0-31cb-a515-640934f50b76 | -4.37399 | -43.14839 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1367258-b7a1-354d-a760-11308587e3a8 | -4.36373 | -43.15821 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a78d70cb-5c0c-33bb-b82a-6e220a0f691e | -4.39344 | -43.32299 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 25ca446f-99b6-3427-a73f-007cce8b413e | -6.67655 | -39.89004 | 2025-12-01 03:36:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f37b44cd-f699-3df2-ad78-77c2ab662dcc | -6.31072 | -43.81022 | 2025-12-01 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d303592-db69-3ac0-88f8-a83d9d44652b | -7.09332 | -39.33843 | 2025-12-01 03:36:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d96bafe6-b640-3425-8974-2497bb846c2f | -4.37271 | -43.15602 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba6de0af-4b31-301c-9b1c-ad11efa9707e | -4.37925 | -43.33712 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5864f972-ab89-36d3-831b-0fb73a99c391 | -3.93945 | -45.85229 | 2025-12-01 03:36:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d55baf65-e177-38e8-8ccd-fc317ae8e8f9 | -4.37502 | -43.16008 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 99d8a464-545e-3218-9d57-39c29e24a9a5 | -4.31072 | -45.37688 | 2025-12-01 03:36:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c2fa445-97ca-3276-bb9f-6e7db0451392 | -8.54379 | -40.21035 | 2025-12-01 03:36:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 58011528-6b7b-3dfc-9568-9a58870dba7a | -4.39208 | -43.33088 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| f1fffe04-f323-3a70-b609-feb626020bbd | -4.37006 | -43.15524 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| a0d805cd-492c-35b2-8582-2bc23db4c1dd | -5.52658 | -42.60258 | 2025-12-01 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f9d9182f-24c6-3302-85b7-52f3c510a162 | -3.70859 | -45.91114 | 2025-12-01 03:36:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 368d53f4-eb23-3576-8fa6-3ebd4debb96a | -4.3777 | -43.1609 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 72558798-07c1-3dce-adba-bdbccd415429 | -6.66626 | -39.89247 | 2025-12-01 03:36:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 292a51c8-8fa5-3196-8b2e-23e855eaf4a0 | -4.39005 | -43.34264 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 59f91344-264a-376f-9b25-bb3093ebc0d7 | -4.38202 | -43.15329 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e8dfae7c-e4ba-317d-9b84-359ff2c7c207 | -4.36441 | -43.15437 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3626116-de88-38c7-934a-81ba72b32002 | -6.96161 | -39.13527 | 2025-12-01 03:36:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 63e8b2cf-c705-3403-9516-5e85d97556e8 | -6.31512 | -43.81878 | 2025-12-01 03:36:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9894433f-96df-3b69-8740-837dfd9014f2 | -4.38568 | -43.33393 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 4375542d-46a8-36b9-906d-1d3353277ae3 | -6.10837 | -35.16414 | 2025-12-01 03:36:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 79a34d84-444c-331d-b791-d97679bcd0c2 | -5.52296 | -42.59167 | 2025-12-01 03:36:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ebf8d991-c546-3550-bd8a-a2422269db9e | -4.37073 | -43.15144 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 486bb0c8-c048-303f-81d7-c7a4b0804017 | -6.67224 | -39.88904 | 2025-12-01 03:36:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f26941d4-2c39-3f8a-a87c-e23df40e1fba | -10.21779 | -36.64828 | 2025-12-01 03:36:00 | NOAA-21 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f294d1e7-4ece-32ad-b1b1-04a6eac0dc6d | -9.41374 | -35.55654 | 2025-12-01 03:36:00 | NOAA-21 | PARIPUEIRA | ALAGOAS | Brasil | 2706448 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e0f603b4-289c-3f7a-9a5d-01ac8e2b4d4b | -4.37705 | -43.14854 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 72781685-d24b-3ef5-8f04-b6c476b251a6 | -4.38269 | -43.14948 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 310f96c9-c9eb-363b-adb6-9cc6679413c1 | -4.70354 | -44.4091 | 2025-12-01 03:36:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fa0c4f78-9a0e-3d97-b3c8-786f0ac0d809 | -4.38398 | -43.15802 | 2025-12-01 03:36:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ca79e5d0-a50e-36d7-bfd6-a695fb459d0a | -3.85111 | -40.97503 | 2025-12-01 03:36:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e8d03d65-704e-3aa1-aa49-8d39a7fa1e69 | -4.3914 | -43.3348 | 2025-12-01 03:36:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 47.0 |
| be97639a-492e-3b87-a1d6-34acf4f57d22 | -6.99417 | -38.69463 | 2025-12-01 03:36:00 | NOAA-21 | CACHOEIRA DOS ÍNDIOS | PARAÍBA | Brasil | 2503308 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02792cda-d453-377c-ba9b-ca8ba11f297c | -17.00452 | -39.77499 | 2025-12-01 03:38:00 | NOAA-21 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e2ca9aab-f541-34e3-9d79-f7a2468273c7 | -12.92019 | -41.14238 | 2025-12-01 03:38:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9ea5e559-c692-3319-ae0c-5528e587f6ae | -11.58141 | -40.84089 | 2025-12-01 03:38:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2d28273d-d7ba-3656-a7d7-77d98e904cde | -13.9395 | -44.35485 | 2025-12-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 321f4ac7-a45f-35fd-ba26-b24f5e808e06 | -16.46651 | -46.42147 | 2025-12-01 03:38:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36097a2b-d520-3fc0-bf0b-3ec556568b0f | -16.46569 | -46.42542 | 2025-12-01 03:38:00 | NOAA-21 | NATALÂNDIA | MINAS GERAIS | Brasil | 3144375 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e892fb10-d1ec-36ba-bf63-ea0154bfbd18 | -13.03731 | -40.05442 | 2025-12-01 03:38:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7b805fd5-5214-3761-8d61-e16fc0fb679e | -13.03823 | -40.04911 | 2025-12-01 03:38:00 | NOAA-21 | NOVA ITARANA | BAHIA | Brasil | 2922805 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d53a95e0-e4a8-37c5-a039-7ca4ea6b7164 | -15.57187 | -40.0595 | 2025-12-01 03:38:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0c2af947-a8f0-36d4-9af3-0b0e182022c5 | -13.47247 | -44.55006 | 2025-12-01 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31e9f5a3-324c-3668-8ab6-e48ff9827127 | -16.14307 | -41.09626 | 2025-12-01 03:38:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 136feb79-8a01-3ff5-8531-a48c66ffbdeb | -15.57275 | -40.05461 | 2025-12-01 03:38:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bc26b324-1ae2-349d-babd-3562d77fe800 | -12.92372 | -41.14725 | 2025-12-01 03:38:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2841fa65-f79f-335e-963d-c90b0ee295fd | -15.5757 | -40.06015 | 2025-12-01 03:38:00 | NOAA-21 | ITARANTIM | BAHIA | Brasil | 2916807 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7806dd1f-82ef-3948-8179-39bd0d966424 | -13.94012 | -44.35164 | 2025-12-01 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9b67ecd-b2e7-34cb-a9c5-b1b678fb69bc | -4.4064 | -43.3351 | 2025-12-01 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| bc121375-af86-32e4-b190-e439dd36a126 | -4.3702 | -43.1741 | 2025-12-01 03:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 30a9fcb2-0bd1-3355-8ddc-7edddf8c7218 | -4.3879 | -43.3129 | 2025-12-01 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 99319e2e-c203-3b71-950d-7e9e7f3b7330 | -3.7009 | -45.9 | 2025-12-01 03:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c3844f8e-fb4c-3505-8f54-b7a51ce354f8 | -4.3877 | -43.3362 | 2025-12-01 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 908a0fa1-1881-3312-8537-07cdc622abbc | -4.3703 | -43.1508 | 2025-12-01 03:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 503a3ced-6d23-31aa-b83e-044143cb9fcb | -3.7195 | -45.8992 | 2025-12-01 03:40:00 | GOES-19 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 2fe9a88c-8c14-31f5-9b98-115f51e2dc50 | -4.3876 | -43.3595 | 2025-12-01 03:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a90344b4-36fc-3be8-b62c-9287f6796639 | -4.389 | -43.1497 | 2025-12-01 03:40:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 9e44dc5d-2e49-32ee-80ea-3aff7bdb3339 | -3.2174 | -50.139 | 2025-12-01 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| d692bfec-7103-37d8-81ca-bae6b73424ff | -23.12241 | -45.28659 | 2025-12-01 03:40:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 483839a2-4344-39a4-ae74-22350713455d | -23.13047 | -45.29419 | 2025-12-01 03:40:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9b5ce845-d0a4-3ff7-81f5-21c2cf26a993 | -21.53415 | -49.52748 | 2025-12-01 03:40:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a4028e41-d1a1-32d4-b6d9-1870b0c5ff2e | -21.53293 | -49.53264 | 2025-12-01 03:40:00 | NOAA-21 | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 28c9636e-fe8b-323f-a53e-11bfe191ea01 | -23.13157 | -45.28892 | 2025-12-01 03:40:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9a33d0b8-be2d-3a8f-b67f-f473b10722b0 | -19.82789 | -42.45336 | 2025-12-01 03:40:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0d891fcc-2149-313e-b73c-51dc96bd364f | -18.88584 | -45.75723 | 2025-12-01 03:40:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f93e9378-eb3b-3d38-a4dd-36ee77c92ea8 | -19.83199 | -42.45423 | 2025-12-01 03:40:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 935da997-6a24-349f-b4ad-3b4a6fea65e7 | -23.11782 | -45.28551 | 2025-12-01 03:40:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ccd82273-2cb9-37de-b4b8-f92e4f34dba2 | -21.98066 | -44.51913 | 2025-12-01 03:40:00 | NOAA-21 | CARVALHOS | MINAS GERAIS | Brasil | 3114808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b5e7b384-8734-376b-8b68-cd6494a0fccf | -23.12699 | -45.28775 | 2025-12-01 03:40:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| a3f740be-98bf-3ecd-908f-ad6475ccedf9 | -22.72582 | -47.35872 | 2025-12-01 03:40:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 18e79c94-f443-30ae-a723-8487de43557d | -19.80139 | -47.8059 | 2025-12-01 03:40:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67161058-3ffd-3092-8402-29d0692a1d16 | -23.12589 | -45.29301 | 2025-12-01 03:40:00 | NOAA-21 | SÃO LUIZ DO PARAITINGA | SÃO PAULO | Brasil | 3550001 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3600fde7-edb9-385b-af45-86c2e20e5329 | -19.80202 | -47.80677 | 2025-12-01 03:40:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e82dce96-9625-32be-b616-03fec30ea8a9 | -22.52579 | -46.92492 | 2025-12-01 03:40:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5929b0c-7def-34a4-b2b9-d972365f4f1f | -21.84196 | -44.59421 | 2025-12-01 03:40:00 | NOAA-21 | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7b1af567-a4eb-3ee7-ada4-1c9bfe0b94a0 | -18.89157 | -45.75554 | 2025-12-01 03:40:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d30631a9-9cde-3e40-ab0f-b6999f3e4f40 | -20.91959 | -46.79061 | 2025-12-01 03:40:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 90b87949-1680-315c-8761-755a6647e7c0 | -20.9189 | -46.79374 | 2025-12-01 03:40:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69da48b7-0a0e-3e70-961c-441050699ed8 | -20.92405 | -46.79551 | 2025-12-01 03:40:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README9.md)
