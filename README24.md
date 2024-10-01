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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e33d7c7d-03f6-3381-82b4-f3385560113f | -12.9998 | -51.2763 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 10ee2f9f-6dc0-365b-8cab-d53390b6dc2f | -12.9988 | -51.3403 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 8cedc7d9-feff-306b-9f8f-ee0d36c9d0ac | -12.9985 | -51.3617 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 35e61652-e6e3-3322-b2db-1ed80051ee63 | -12.9813 | -51.2359 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 47a61362-e32b-3fb4-b166-58aa4ce62b77 | -12.981 | -51.2573 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 859ab561-c142-3b39-82bd-c1a58fbd163e | -12.9807 | -51.2786 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 9240320a-1bce-3d5b-9dc7-3f34cf4e2ce0 | -12.98 | -51.3213 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 15048f3f-33e5-3662-9ced-0704022187c9 | -12.9796 | -51.3427 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 229.6 |
| 23c9ec52-b1cb-342e-a169-35b440820737 | -12.9793 | -51.364 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 180.2 |
| 63f65fd3-7032-32df-add8-5d1dad3da1b6 | -12.9622 | -51.2383 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 36782838-6ffa-3932-b1ad-9df7a8d81cb9 | -12.9618 | -51.2596 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.1 |
| b07e81cc-b692-3c59-94b2-5eb88564244e | -12.9605 | -51.345 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 8c1c1776-fbf6-3dc8-affc-941544f199b1 | -12.9228 | -51.307 | 2024-10-01 01:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 4333a526-8d43-3a71-be7e-2bc6f417d15a | -13.5957 | -51.1796 | 2024-10-01 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.9 |
| e69f9ef0-e83e-3a4f-a5af-c9fef9387605 | -13.5768 | -51.1607 | 2024-10-01 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 4d69192a-8823-3d95-ab72-8c7e95b94d25 | -13.5765 | -51.1821 | 2024-10-01 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 188.9 |
| 5b6f1465-2990-32bb-836f-3f36a7798300 | -13.5761 | -51.2036 | 2024-10-01 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.7 |
| f4f5cfdf-e931-3d5e-a6d4-403b91bc7fef | -13.5583 | -51.1203 | 2024-10-01 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 120.8 |
| bc6ed4a1-11de-3523-9189-799cae9dbf90 | -13.5391 | -51.1228 | 2024-10-01 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 4f3cce83-645c-3f59-bbe4-8fc79f395cb9 | -14.7406 | -48.7498 | 2024-10-01 01:36:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 667222b5-3b85-3bc3-a661-193bc295f0e5 | -14.7211 | -48.7529 | 2024-10-01 01:36:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| cc69da21-3d10-3be7-af76-eb0ab910be8e | -15.6933 | -53.914 | 2024-10-01 01:36:34 | GOES-16 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 48b35d2d-a275-3c9e-935d-4588199636b3 | -16.1859 | -58.4215 | 2024-10-01 01:36:37 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| fd616edc-fdd2-3df1-ab63-b03500d9e14a | -16.6459 | -55.1908 | 2024-10-01 01:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 78.1 |
| 7f9b1c44-bc9e-3dd8-9d74-911ed18afa11 | -16.6263 | -55.1934 | 2024-10-01 01:36:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 84.1 |
| ba8d2242-2a77-3fd7-bd69-4f1c063ace88 | -16.7471 | -57.3651 | 2024-10-01 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.3 |
| 4d8cc6ee-9b6d-36e7-ae7f-389f43c55251 | -16.7467 | -57.3855 | 2024-10-01 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 62.3 |
| 248b9ae1-ac5d-313f-9e54-c19f7310a019 | -16.7275 | -57.3673 | 2024-10-01 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.5 |
| 6973e20d-c425-372e-b841-61c61f72e248 | -16.7079 | -57.3696 | 2024-10-01 01:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.8 |
| 37edb92f-5c7c-30b4-8a94-59f04685d9a7 | -17.8789 | -40.0946 | 2024-10-01 01:36:44 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 82.1 |
| b37c1722-e3d3-3be9-87ca-5951890c81fd | -18.543 | -43.4436 | 2024-10-01 01:36:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.8 |
| 695333c3-50ee-386b-bb35-56999b469878 | -18.5423 | -43.4683 | 2024-10-01 01:36:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| fd1bc5dc-e5bd-3054-888b-403955b5ef8d | -18.6011 | -53.0412 | 2024-10-01 01:36:50 | GOES-16 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 88.2 |
| ea02254c-d60f-3475-a756-a40154247488 | -19.1329 | -57.4628 | 2024-10-01 01:36:53 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.3 |
| b6358f3b-c78b-36b3-9ba4-5c76d246a58d | -20.5259 | -46.3023 | 2024-10-01 01:36:59 | GOES-16 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 05776b3c-7d40-35fe-9d52-feddfc98b617 | -20.6393 | -48.7549 | 2024-10-01 01:37:00 | GOES-16 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 4f317edd-460f-3719-9077-121af548aa2c | -22.3922 | -49.2961 | 2024-10-01 01:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.6 |
| 69cab922-f633-3247-bef4-6436b9908f7d | -22.3916 | -49.3194 | 2024-10-01 01:37:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| 867d6fd8-31ce-3caf-a205-a2abeb46f123 | -22.3713 | -49.3011 | 2024-10-01 01:37:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.9 |
| 2b3220f8-de36-35a5-9829-f4dc5d4205de | -22.3707 | -49.3244 | 2024-10-01 01:37:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 237.0 |
| e0f9728f-2379-37ac-bdf5-d0c437e35788 | -23.0793 | -45.3951 | 2024-10-01 01:37:12 | GOES-16 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.5 |
| f2132591-aa73-32c8-97a9-10085a5f4325 | -26.4142 | -53.216599 | 2024-10-01 01:41:56 | METOP-C | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a086e007-bcd8-3673-8f8d-130ecea3baa3 | -25.014799 | -54.066502 | 2024-10-01 01:42:21 | METOP-C | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6a1139c-444b-3333-9ed2-6db427500705 | -22.373699 | -49.285099 | 2024-10-01 01:42:43 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9fcf1749-32fb-3d0e-a757-44861023eba1 | -22.3801 | -49.307301 | 2024-10-01 01:42:43 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5ab39e25-1bdb-3c0f-b937-7811a2d4f2b3 | -22.364201 | -49.2883 | 2024-10-01 01:42:43 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c495b26d-5426-363f-8c71-8edd591f9fff | -22.3706 | -49.310501 | 2024-10-01 01:42:43 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9c082062-9d8d-3879-a125-0c1c1a783db1 | -22.377001 | -49.3326 | 2024-10-01 01:42:43 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bc37d960-570e-3f9f-9ece-903b2c55894d | -22.354601 | -49.2915 | 2024-10-01 01:42:43 | METOP-C | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6cf7523a-e320-3ffa-b19b-69d357c3d729 | -22.361 | -49.313702 | 2024-10-01 01:42:43 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 524110f7-1b7e-35d0-a552-0c216220823e | -22.367399 | -49.3358 | 2024-10-01 01:42:43 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e45ed51a-0af8-3024-8baa-e35948f450d0 | -22.3515 | -49.316898 | 2024-10-01 01:42:43 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c6789ec-42a6-3c56-9bba-05bf0f9dc491 | -22.357901 | -49.339001 | 2024-10-01 01:42:43 | METOP-C | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2e78ac07-c9b3-3aff-bc06-7cc74ac3447d | -21.5868 | -47.787102 | 2024-10-01 01:42:48 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f3634181-d0b7-3b31-9545-e7a94eb49197 | -21.595301 | -47.815498 | 2024-10-01 01:42:48 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c03feb14-203c-3fae-b742-ed55c65a9989 | -21.5688 | -47.761902 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f7c4c61d-a48d-3b1b-a561-44bd91ba57d5 | -21.5774 | -47.790401 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| dbee0732-db4d-3ecd-8f72-ec0057844311 | -21.585899 | -47.818802 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3b80d9c8-7461-31f7-82d3-bf06b0d48618 | -21.5944 | -47.847 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 07538428-7c73-3cfe-ad45-c95473604343 | -21.559299 | -47.765202 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b3fb1e35-f524-3606-a599-910ab5e71644 | -21.567801 | -47.793701 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 48e21e28-6318-345f-bf7b-3b9eaf8f0770 | -21.576401 | -47.822102 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 52ab4b08-d6e4-3b8f-a399-43031c5e7e6f | -21.584801 | -47.8503 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 637b9960-2bc1-3ac4-b799-ce872fbc430a | -21.558399 | -47.797001 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f6852bba-64b5-350f-bdad-32ede387db52 | -21.5669 | -47.825298 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 460e71af-345b-3f33-94be-52c2c86070c4 | -21.575399 | -47.8536 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 938a5f2c-b643-3999-83f5-62117386ca9c | -21.548901 | -47.800201 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ac89046b-cd90-303a-ab0e-21f220277f8a | -21.5574 | -47.828602 | 2024-10-01 01:42:49 | METOP-C | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 7be2b428-fe71-37c4-aa6f-c2c987d82a46 | -20.626699 | -48.7393 | 2024-10-01 01:43:08 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41e5b92e-88e5-3e9a-ba6e-ba7af05168ad | -20.6343 | -48.765099 | 2024-10-01 01:43:08 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e29d7b08-f7e2-3fc1-bc9d-d922b3809a56 | -20.6173 | -48.742401 | 2024-10-01 01:43:08 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d7fe30ca-e35e-386a-99ac-af7a56e87313 | -20.6248 | -48.7682 | 2024-10-01 01:43:08 | METOP-C | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d76f4e1-6cbc-302e-88e9-8fb865a755bf | -22.188801 | -56.086899 | 2024-10-01 01:43:15 | METOP-C | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8f4ae543-5e53-3a01-a4e6-7733977646b6 | -22.144501 | -56.204201 | 2024-10-01 01:43:16 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ad1b366d-934f-3e14-9aeb-57f95edc9383 | -20.802299 | -53.113899 | 2024-10-01 01:43:25 | METOP-C | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8fc5f6ba-e0bf-325c-98b2-2273be81478e | -20.805901 | -53.127499 | 2024-10-01 01:43:25 | METOP-C | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5a9c94e5-c76d-38ea-adf0-9652499b9e7a | -20.8095 | -53.141102 | 2024-10-01 01:43:25 | METOP-C | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7318d8a6-4dbd-3b46-844f-76b8732e27dd | -21.4174 | -57.237 | 2024-10-01 01:43:32 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2f9bda22-2058-3cdb-a6c6-206a417c61b0 | -21.4077 | -57.239601 | 2024-10-01 01:43:32 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4d3b902a-f481-34ce-b4a6-ca59791db509 | -18.9105 | -49.215302 | 2024-10-01 01:43:38 | METOP-C | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ac3495ea-8ba5-3548-acb2-8f60834269d0 | -18.900999 | -49.2183 | 2024-10-01 01:43:38 | METOP-C | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8b17927a-03cd-3f0f-9a0d-354631fa438d | -21.0369 | -57.510799 | 2024-10-01 01:43:39 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4b9ab583-7707-3d6d-99ef-1bd041f97818 | -21.038799 | -57.518902 | 2024-10-01 01:43:39 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 88a6d19c-d2ac-3c94-b7d9-eecdb27bedb0 | -21.025299 | -57.505299 | 2024-10-01 01:43:39 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 49983ded-fd7c-3879-9d4e-c3ff7291afa2 | -21.027201 | -57.513401 | 2024-10-01 01:43:39 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| e06fc2a8-9476-3348-b295-e59078feb4ee | -21.0077 | -57.518501 | 2024-10-01 01:43:39 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cd224315-0b81-39f9-b9af-15be2bb79058 | -18.513599 | -49.426399 | 2024-10-01 01:43:45 | METOP-C | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7820297a-3590-3f30-b365-74cb894a7e2e | -20.016199 | -55.9827 | 2024-10-01 01:43:49 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8743a09f-fd0e-3b92-824e-98121b35bb85 | -18.5903 | -53.0103 | 2024-10-01 01:44:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d4b09e17-f30d-301f-a952-f021ffe641db | -18.5942 | -53.0252 | 2024-10-01 01:44:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a66ecc79-a83e-3e1a-adfb-b1c17c6d5a21 | -18.5982 | -53.040199 | 2024-10-01 01:44:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 6b1d988a-3076-3d6d-be3a-d0ba8cb60ce2 | -18.6022 | -53.055099 | 2024-10-01 01:44:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f9038865-ae47-3fa8-bf25-7e32aa965efc | -18.5846 | -53.028 | 2024-10-01 01:44:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0c89b5fa-841f-30e8-b920-c7616890d92b | -18.5886 | -53.042999 | 2024-10-01 01:44:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9d9a96f4-5c69-3176-afbc-5179f7020510 | -18.5926 | -53.057899 | 2024-10-01 01:44:00 | METOP-C | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ae301acd-4bfb-367d-bc04-b2e06ba58850 | -19.164801 | -57.472 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| ece99eb6-172d-372e-a570-7a90c4b5be67 | -19.1667 | -57.480301 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 212383e0-3920-33a9-bf3f-5f13479ce528 | -19.153 | -57.466202 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 58e243d5-7abe-3a79-ab76-7b805b8bfdc7 | -19.155001 | -57.474602 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5df53b3c-69f0-33fc-b315-121006620886 | -19.1569 | -57.482899 | 2024-10-01 01:44:09 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README25.md)
