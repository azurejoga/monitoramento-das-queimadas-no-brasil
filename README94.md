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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a18b01b-d01d-3ab7-b59a-f32102170020 | -5.69539 | -45.32681 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb63910b-ea24-38e2-849b-3565632c16e8 | -5.43106 | -45.88066 | 2025-09-11 04:44:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd1c3525-772b-3a14-9762-c19d3b1dd09b | -6.20682 | -43.49783 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 949386f9-e121-39b2-8318-4f97ccae1fa3 | -6.17089 | -42.67257 | 2025-09-11 04:44:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bede4ab3-af1f-3cc2-9666-818cea1c926f | -7.49122 | -54.94752 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 52ec488c-152e-354f-9355-42b5551468b1 | -7.49492 | -54.94812 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a25f269-059f-3507-a5e7-c1fac2e9c158 | -6.90033 | -47.90371 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82a24f64-f77f-3cf0-b62b-f53a139c0982 | -4.86884 | -42.76265 | 2025-09-11 04:44:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7efbdf96-7d40-37e3-816c-c73010cff109 | -7.66335 | -50.27278 | 2025-09-11 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb33d69e-66d2-3d29-a9bf-1dd249e0cdfb | -8.9669 | -46.07173 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a029694-cdf5-3418-ae0a-a938f75baed2 | -5.13294 | -49.86933 | 2025-09-11 04:44:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ee8cb503-0489-36f0-a694-47fe8fb45239 | -5.72889 | -45.41711 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92618236-b260-3daf-aadd-fb99d1da33d4 | -5.89492 | -45.8085 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96a65aad-b2ae-3598-94cd-02c9b0d163e4 | -5.65344 | -43.89884 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71420cc8-2318-37a8-82ae-f8a8f708cbbc | -3.24381 | -50.80224 | 2025-09-11 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d5921ee3-8a5f-3c05-a136-179c36da311a | -8.09035 | -52.34735 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 644e1ed8-2b61-335c-b4ed-41562b5e7dae | -6.44935 | -44.05706 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f8c3dc9f-412a-3c40-9754-7d43e601ddca | -5.2289 | -43.69704 | 2025-09-11 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee38b577-d21d-359c-9566-8e665ab781e7 | -3.31537 | -54.91196 | 2025-09-11 04:44:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b9c60db-ecee-3d4c-b21f-19b304863a68 | -5.50095 | -49.21134 | 2025-09-11 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 20517f3d-a377-3ae3-adb6-46fdac7ab560 | -6.18046 | -53.26474 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b13bed35-0a0f-3712-95e6-79c9ee7dad0a | -7.40914 | -45.85421 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5ef5958d-21ec-3d8f-880f-7484723062e4 | -9.09272 | -46.95122 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb7b87be-9fd6-36ed-a849-717fb16d7199 | -5.72674 | -53.59883 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0e2a5da-8493-3dff-8ca0-6b6f6afb8628 | -5.72321 | -53.59827 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9598c1d-a4f7-3e4c-a348-4463ae75c2e7 | -3.67647 | -47.49478 | 2025-09-11 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 284bd779-0ba0-32f2-a782-a5bc9e234f4d | -8.02047 | -48.66174 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c503bc68-3a63-3020-94d5-f9a03c2706c3 | -5.65105 | -42.62867 | 2025-09-11 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7fe41f2f-c2b9-3bc9-94c5-c80abdfd256f | -5.85095 | -44.17571 | 2025-09-11 04:44:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7597e21b-3f79-3256-aa2a-b5a1a6a8ec0f | -8.0567 | -52.32755 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4acb8d8d-efb6-3b8d-a5fb-5fe38a56bf86 | -8.81064 | -48.09511 | 2025-09-11 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3df64e16-1453-365a-967c-4b88effbe415 | -7.14802 | -46.04658 | 2025-09-11 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f6d4672-7a8b-3958-90ba-0f7b81a38d7d | -4.19881 | -55.13765 | 2025-09-11 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64c6d8d6-cc37-3a2f-b69d-3ad340d39e45 | -7.09551 | -50.75817 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9eaeb493-a20c-33a3-b39f-46b39a5a5e6d | -7.77901 | -50.99084 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4d9fbf6-25f0-3cad-94d1-5e21e906887f | -6.74537 | -51.963 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bfdcebc-aeee-3431-9b9d-697cbb0d1abb | -8.08589 | -52.35382 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5295cafc-fac6-3ca5-a72d-a7579c0fb5d5 | -7.07982 | -44.85146 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 08c19715-c473-3df0-81f5-eebc94f3dc85 | -6.13995 | -45.47242 | 2025-09-11 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ff22461-e6e2-332c-aea5-8f088e30af56 | -5.57871 | -42.92786 | 2025-09-11 04:44:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a3f9f48d-7069-33aa-a084-ce941bd1a417 | -5.0846 | -44.24984 | 2025-09-11 04:44:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd0e4377-bddc-33e7-989e-9e973f1424ec | -8.03704 | -48.67185 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d2f6b16-eb7e-36e7-a6ae-c8022ae785ce | -4.58513 | -45.6159 | 2025-09-11 04:44:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0939f0e-e1f0-3c3d-a480-89a2a96e3531 | -5.76845 | -42.44609 | 2025-09-11 04:44:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0d9b3570-5425-364f-b5f2-f83a9ff1148d | -6.82189 | -52.7959 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f78cf89a-b640-3e97-a805-eee3b4e021e9 | -5.66403 | -43.89084 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07df0d8f-6b4a-3997-a2dc-331485f272a7 | -7.18474 | -44.96568 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c70c587-4825-32a3-81d2-f62de3f0393a | -7.89831 | -46.25658 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb3a0f64-532c-3b6a-ac4f-575e2672dcff | -3.68719 | -47.49631 | 2025-09-11 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a94d42be-3789-3eb6-aa3b-982fb194aeae | -5.59858 | -48.11651 | 2025-09-11 04:44:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6e881ff-a541-367d-896a-7aa8042d54d0 | -6.81036 | -51.87636 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdbad058-ddbf-3fdd-86ea-0de59bdf41c0 | -5.65185 | -42.62295 | 2025-09-11 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fd1d28a0-3f90-368d-b179-2fa2fd8dc646 | -6.85338 | -47.8707 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c3e71e2-b4da-3905-89eb-d32fcd94c35f | -3.34273 | -50.82071 | 2025-09-11 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67e83a09-2e24-3cc5-84ac-b17b3044ef1e | -7.78181 | -50.77729 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5069ccfb-2cf1-3a11-869b-2d4cff0db51b | -7.16197 | -48.88612 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fdf38b9-fa4b-3615-b857-3a6123cbd542 | -8.03585 | -48.67976 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 789f32c5-64eb-38e9-8071-cb320afda7b9 | -9.09889 | -46.95906 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b60e810-d152-3868-8c1c-7d5e2a2104b3 | -7.57159 | -48.23742 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2327bb2-3356-3983-b56a-c89b06bef7d4 | -6.22002 | -43.37131 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98fa0778-7059-373d-95c4-ef32053d19df | -8.43652 | -49.11093 | 2025-09-11 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 1c3eaab2-0fa8-3857-b823-73c2f097aabc | -5.82434 | -45.27149 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8793eb21-86dc-358c-ab52-526240ad0dcc | -9.04877 | -46.97686 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 79c3cebe-87a4-3526-b123-bca1e99e459b | -6.40467 | -42.60679 | 2025-09-11 04:44:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 841eec40-1521-33de-9e8b-eb2b66983e2f | -7.26557 | -44.90211 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cc9d36b-9f4d-386a-8f7d-b5258eb8e104 | -5.65516 | -46.22993 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbc9d7c8-2bf6-33df-b35e-f1ffdda8a6e8 | -5.54444 | -45.37572 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 056b3e1c-deda-37e1-83bb-7a8798431e7b | -4.92704 | -55.78656 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7841e812-903e-3df6-818f-405b24650008 | -8.42324 | -49.08099 | 2025-09-11 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 97158d3b-420a-3946-a19c-e451f3221382 | -8.07359 | -49.90276 | 2025-09-11 04:44:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c21c5570-ac76-3c07-ac80-501b899a0148 | -3.08116 | -48.8175 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96f73b1f-2f95-3709-8292-ca6a867777d6 | -1.97949 | -47.98066 | 2025-09-11 04:44:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f0409e3-4660-32d7-b54d-bbad551753bb | -3.34722 | -39.28034 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1ab8d456-76b2-327c-8e2c-599d28ff3934 | -6.39461 | -43.51725 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edccefd7-b986-337a-8cec-e97c6e7ba666 | -8.20175 | -50.11142 | 2025-09-11 04:44:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6d98607f-3e68-36d9-b614-1abdd56bc26f | -3.82522 | -51.03506 | 2025-09-11 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61e8f98b-2ad7-3276-bff7-2c3ee63c7891 | -5.48068 | -44.11737 | 2025-09-11 04:44:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dc3d7fa-2a47-30ea-ab28-32d2da9ba853 | -7.86047 | -44.88691 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4ffc412-1465-3d7a-8cbf-2a93e181038d | -9.14555 | -46.21337 | 2025-09-11 04:44:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed27f282-19c7-3f90-890d-2e9f569bf1c1 | -6.20254 | -43.52772 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 547fced4-8b99-3454-8dad-2ded7635eaff | -8.74767 | -47.11759 | 2025-09-11 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9ef73694-3a5f-365a-ac77-40a4a837c092 | -8.6607 | -45.7367 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e41af3c4-a1e1-3646-b6f2-56f85b4c8f82 | -8.02757 | -48.66263 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05322a3c-5300-3238-8c2c-511d88cddc0b | -7.46625 | -45.2859 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb1b16d5-a8f6-3e84-af1d-f799026477ae | -9.0825 | -46.96601 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7a5d8d19-465e-39f4-9ae1-9c2f71c8a707 | -5.88781 | -52.10119 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a767917c-7496-3b16-b221-5f09a86492da | -8.04364 | -48.15318 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8042e15e-c6fe-3974-90b7-dafc39bf766f | -7.49419 | -54.95253 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d7ca1f5f-d64d-3cc6-ab6f-ef9d7173fca1 | -5.65049 | -51.86091 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c328db63-bab6-3f1e-8bc6-ed22315b9035 | -9.05284 | -47.05915 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 9b7f8c9f-a7a1-3128-a302-325ecf109cb6 | -5.3341 | -49.00224 | 2025-09-11 04:44:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc5df083-36f3-3fbc-93f6-164127a58200 | -7.38457 | -50.886 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 391789f0-184e-39b7-ae88-db9bfff5e6d1 | -6.74865 | -51.98523 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c960bf3-e660-3b26-97b9-8d589c9d338d | -6.24666 | -43.49191 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1c1b0a59-9a1f-37ba-9d96-01d0320ae453 | -9.06207 | -47.05069 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a168e87-11e5-3c3b-a43b-c32760d70205 | -8.10696 | -44.84692 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4e9e1b0-f875-358c-b99c-f4f7ea0968a7 | -9.05816 | -47.0501 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7d664732-5d33-308a-bf41-9b8a04509822 | -7.3901 | -50.89402 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e96af5a6-5b9a-3eac-8ef0-572d77fea38b | -3.30433 | -48.71452 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f354cfcf-a804-3190-b1fb-2e56baa08ab9 | -7.88663 | -46.05141 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README95.md)
