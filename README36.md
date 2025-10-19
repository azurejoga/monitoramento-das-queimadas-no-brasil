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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef3fa0aa-537f-3e89-a48c-6d36ed4c1519 | -16.76022 | -42.7765 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 35.8 |
| efe1e894-51b5-38b0-8118-73f8bcb502de | -15.90632 | -41.57178 | 2025-10-19 04:14:00 | NPP-375D | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5985555b-10c6-34e0-9ac2-c215ec74bf6e | -15.51197 | -41.68093 | 2025-10-19 04:14:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 31b510a9-1ba7-36a5-ad12-520d0f117f3a | -14.91048 | -46.72152 | 2025-10-19 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb9d7958-ae6e-3d61-b710-fc1e00ccd17d | -16.80847 | -42.82236 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7be7da74-9256-3d6d-9ff5-7200eae348ec | -14.19054 | -44.79705 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| e18ef676-e7fb-32f9-ac67-2239d34cf333 | -15.01615 | -41.99686 | 2025-10-19 04:14:00 | NPP-375D | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| af76243a-f8f5-3398-a29b-14ca291dcbd7 | -14.46262 | -45.57738 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 644cb170-4b0b-37fd-9012-be73427ca108 | -14.45767 | -45.56454 | 2025-10-19 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5e45dbc-bbaf-32b4-9d9c-943ec8a24e28 | -16.77987 | -42.76078 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4189f600-e57c-39c1-a7b8-65bf5b3ffe41 | -16.14709 | -41.15695 | 2025-10-19 04:14:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 42100f0f-cb07-345e-b5b5-65262ce67335 | -15.79118 | -43.64928 | 2025-10-19 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f85d3b48-f6bb-3c69-84d0-ef69a1543086 | -16.74114 | -42.76564 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 8f2a11e5-b885-37f6-b9e4-6452a56b1e79 | -16.78996 | -42.80797 | 2025-10-19 04:14:00 | NPP-375D | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18669ed6-9800-381c-9164-bab441ed3c0f | -15.26193 | -43.58556 | 2025-10-19 04:14:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 412205f8-0c9e-33aa-9760-0037b6463dde | -16.14474 | -41.14825 | 2025-10-19 04:14:00 | NPP-375D | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 583b969a-3141-3db7-b0fe-606e2087ece6 | -15.52697 | -45.34903 | 2025-10-19 04:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 42b1052f-3b55-3fa0-ae3a-131ac081cf2b | -22.30237 | -51.50846 | 2025-10-19 04:17:00 | NPP-375D | PIRAPOZINHO | SÃO PAULO | Brasil | 3539202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4de7f417-d967-3ab8-a8d1-c385f24f6766 | -16.7834 | -42.7668 | 2025-10-19 04:20:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5050fc1e-6403-316c-b92b-54c0171dedc1 | -4.8409 | -42.7465 | 2025-10-19 04:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 50.6 |
| fa22f24a-6c5c-3ab5-8299-457024ccfd5e | -16.7635 | -42.7714 | 2025-10-19 04:20:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 160.7 |
| 47a9b011-eb05-3ea5-889b-328928a150a1 | -8.6032 | -40.1834 | 2025-10-19 04:20:00 | GOES-19 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 71.7 |
| dc5e27cd-8682-32c1-a6f4-b0c14b68d727 | -16.7435 | -42.7761 | 2025-10-19 04:20:00 | GOES-19 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| bf12d188-560d-3400-9cf8-b5606cdf07c5 | -13.5405 | -43.0077 | 2025-10-19 04:20:00 | GOES-19 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 63.9 |
| 509316a5-7697-388b-8338-9717fc224f23 | -3.52322 | -49.93599 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 139b515b-c192-3972-af9a-1579433c1c5d | -4.77246 | -45.88892 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa7be835-1b1b-3e29-97af-d40bb9ddf1e2 | -4.1212 | -49.10033 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 888674d3-e7a0-3570-b0d5-909cbd694b75 | -4.98653 | -43.84951 | 2025-10-19 04:29:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d725a1d8-d7f3-3df7-8aab-0e3bfdc322d8 | -3.81724 | -48.65154 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6cbeae32-d316-3392-848d-59754f861647 | -3.89002 | -52.40693 | 2025-10-19 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7a9dec5-2de5-38c9-a7f9-c8b83e1d4903 | -2.80991 | -54.38609 | 2025-10-19 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c746594-d68c-3c08-a7ff-c8ae0533017f | -4.92469 | -45.67547 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 976ae8a2-c9f7-3437-819d-d14d175243ee | -4.28576 | -45.48138 | 2025-10-19 04:29:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9573f38-8624-3529-abbd-97904a0e3fe8 | -3.44251 | -52.82877 | 2025-10-19 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42e8b542-4057-3cbd-80a6-d020371d36e9 | -3.8037 | -51.94107 | 2025-10-19 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef29915a-ffa6-33f5-9fa4-c3db60d77e9e | -0.03702 | -51.11591 | 2025-10-19 04:29:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 869cd8d1-940d-368f-93be-a5f2e85fdae5 | -3.14025 | -50.25118 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26909b7f-97e0-3483-811f-76d920a00c72 | -5.05662 | -45.4365 | 2025-10-19 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c86bbfd0-3fdd-3fe7-8933-6a447641d2e1 | -4.12155 | -50.71833 | 2025-10-19 04:29:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7588eac0-3a00-39c2-8809-e48592b5951c | -0.73392 | -50.59469 | 2025-10-19 04:29:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d080a09-85e5-3236-b90c-02071a3fc342 | -4.24853 | -40.34949 | 2025-10-19 04:29:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ef29be4d-1acc-301c-b20f-bf7635d29b4c | -3.52029 | -49.93136 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a7c52a1c-19a9-329f-a017-84f83989a222 | -2.94428 | -48.07223 | 2025-10-19 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb1127d5-3b6e-3674-a38a-41a0d4f296ea | -1.42899 | -49.09793 | 2025-10-19 04:29:00 | NOAA-20 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 628684d8-f07e-3861-8387-f042b897912b | -4.91955 | -45.70839 | 2025-10-19 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88355d4f-a353-377a-b419-b9693113bbb8 | -2.90813 | -52.73051 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36238219-f1f3-39fd-a925-dd05d62e3c31 | 0.31798 | -50.96834 | 2025-10-19 04:29:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 005cefa1-11b7-381e-9157-7869cf2773b7 | -3.39512 | -54.06419 | 2025-10-19 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7cf0a6db-6cdd-37e2-b423-267f258af047 | -2.90386 | -52.7299 | 2025-10-19 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 626d0df1-8a4b-344c-b493-21fa318f2bc5 | -4.23963 | -44.6869 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b63d1ae2-0e92-36aa-9530-16df1b40ea08 | -5.26749 | -44.82033 | 2025-10-19 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f886a5b6-fe07-3a02-a95d-9795067a0dd5 | -3.51937 | -51.66215 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aa04ec8-1cac-37d8-b22f-5d63cf4a87b3 | -4.23546 | -44.68272 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0caf3571-caa5-3db7-a209-37d84caab813 | -5.47871 | -43.12859 | 2025-10-19 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3160e4c5-264c-311f-b70d-59744f07ac11 | -4.59241 | -46.5184 | 2025-10-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80973e45-6998-3b99-bfb0-15253a3cbb9b | -4.97054 | -44.61171 | 2025-10-19 04:29:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2929e7bc-38b9-3ee1-864b-1c8a62cc6376 | -2.73696 | -49.39366 | 2025-10-19 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28bdbfc5-ab89-3e2b-8d1d-1481fc9d22fb | -5.47621 | -43.03152 | 2025-10-19 04:29:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30a39c08-2805-33a1-89ab-6349be9c0411 | -3.14819 | -50.2481 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f6efe4c-a318-33f1-94e4-2feddf555bc8 | -4.24124 | -44.69157 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f9fd2b-f89c-397d-aeee-88e480973500 | -4.1925 | -45.79229 | 2025-10-19 04:29:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9b7fc48-50bc-3526-829b-a7ab62001a11 | -2.44148 | -48.61708 | 2025-10-19 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 479a2471-a7aa-3594-84d6-5e77b1d9aa3b | -3.13887 | -50.26278 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae02b54d-e3ae-3dce-9031-1cc8193f967c | -4.30327 | -48.06992 | 2025-10-19 04:29:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abf84819-88f7-334f-b3f3-46f7aef46b42 | -4.2449 | -44.67578 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5015efd7-c992-32e1-80c8-3f42054ea018 | -3.04276 | -40.10908 | 2025-10-19 04:29:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f8749220-13a7-361a-9f34-82d7c49b0355 | -2.59666 | -49.49767 | 2025-10-19 04:29:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60758b0e-f207-32fe-9627-38d3d3d2fdca | -2.59251 | -49.50107 | 2025-10-19 04:29:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5620cff-d12d-3a0d-920a-bf8f4f4528d2 | -4.06205 | -48.96635 | 2025-10-19 04:29:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fab04be-14b8-335f-9d61-22968a8d9578 | -4.16219 | -51.09286 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a8aafc9-2bc8-3818-817d-88f17e80a426 | -2.70469 | -49.86322 | 2025-10-19 04:29:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d7f2a1e-bea3-34b0-86e3-3e6f208478f4 | -0.98758 | -47.07824 | 2025-10-19 04:29:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 559906c6-2067-39a3-9196-6277feabfc12 | -2.86967 | -50.74238 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0309f8a9-26c6-3b46-ab03-246fd119621f | -4.23607 | -44.67883 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15edabd2-db4f-3d4a-a759-96266ae3a5de | -4.23486 | -44.68661 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 724589db-de71-3b4d-9593-c808b15064af | -4.58535 | -46.30274 | 2025-10-19 04:29:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49b1c1a5-78f8-30cf-89ea-dd48e541d37b | -2.69302 | -49.55294 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 1a2cfcd8-306a-3d6c-b027-48f8b0c1c0d2 | -4.41646 | -43.95848 | 2025-10-19 04:29:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b9cb511-0d1f-3eb1-955d-f8cafd47ee39 | -3.51253 | -49.93422 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 511f00f0-9863-3c94-9df5-f5a44d9a6408 | -4.23774 | -44.69103 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aad5c0f5-993c-3584-91af-cce6dc91cfcd | -2.65092 | -49.52187 | 2025-10-19 04:29:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53292596-6cc7-3846-a512-042c8994e1b7 | -1.18651 | -47.66702 | 2025-10-19 04:29:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de51767b-cfc6-3af3-bf41-a4c925865622 | -3.527 | -55.47325 | 2025-10-19 04:29:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e8074df-37f2-39ab-a1bc-7b61647b7964 | -4.24885 | -40.35238 | 2025-10-19 04:29:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d65a5498-b0fe-3f3c-8b14-3032bf8361d7 | -3.57497 | -41.61445 | 2025-10-19 04:29:00 | NOAA-20 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 88c2c410-0793-3d81-b195-bcb943081342 | -3.52504 | -50.32833 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f34e102-b9d4-3701-8785-9eba1ade1717 | -5.37107 | -42.80143 | 2025-10-19 04:29:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2900d6e0-fe1c-35ab-b580-1ac8699bdae6 | -4.24431 | -44.67967 | 2025-10-19 04:29:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e2d9bf9-5ef7-3092-acda-65fd338ce4ec | -3.52478 | -50.30669 | 2025-10-19 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16313e3a-9215-378f-b0d4-75220e9e7ca8 | -2.47794 | -44.16658 | 2025-10-19 04:29:00 | NOAA-20 | PAÇO DO LUMIAR | MARANHÃO | Brasil | 2107506 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e04ce080-aaa4-3954-88db-14fb2ff92d7c | -3.14164 | -50.2459 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b7847ae-f7f3-36bc-97ee-02164cc760f5 | -3.14094 | -50.25013 | 2025-10-19 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbeba862-3691-3bc1-bc2c-a59be462e1fc | -2.68596 | -49.55181 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ac25d060-fe60-37b5-befa-7d076ba523ba | -2.43807 | -48.61654 | 2025-10-19 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e0fabaee-e9fe-3d32-a290-f0f634be5a35 | -2.69012 | -49.5484 | 2025-10-19 04:29:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| cac33abe-926f-3399-96e6-b904fb71e5ca | -4.83733 | -42.75229 | 2025-10-19 04:29:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e04e1df9-834b-33be-9c30-f75a40666f98 | -4.24802 | -48.56825 | 2025-10-19 04:29:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2fce046c-d611-3da3-913d-a576c8fb59a5 | -3.03774 | -51.21261 | 2025-10-19 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f3803acf-dd3e-3da5-b827-9e2bfce21bda | -4.90896 | -37.41523 | 2025-10-19 04:29:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 65e3810f-65b4-3a75-abfc-6c55d75c135f | -4.63391 | -46.53533 | 2025-10-19 04:29:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README37.md)
