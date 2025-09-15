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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b460ec51-bff8-30b6-9e53-3f5f0ceec1dd | -20.93504 | -47.01913 | 2025-09-15 03:32:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c07b5fad-eaa9-3681-9bac-700b94af30c0 | -17.27604 | -46.10679 | 2025-09-15 03:32:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 780bef95-8cc0-3f78-b2e8-6c1043cd8d75 | -21.25869 | -45.63181 | 2025-09-15 03:32:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1da37b6b-9122-3a8c-9355-37e4db4c67c3 | -19.14642 | -42.08698 | 2025-09-15 03:32:00 | NOAA-20 | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7f4b0ba3-d758-3912-be56-aca4d4631477 | -17.61051 | -44.17502 | 2025-09-15 03:32:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cd94b05-dc3a-3c97-9342-2d137cc669fa | -14.93665 | -46.55241 | 2025-09-15 03:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54ff0f70-52e3-3819-9ff7-49455c7dd13f | -14.27858 | -46.13304 | 2025-09-15 03:32:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63795ce5-18a4-3aca-a788-73ce5ac0f765 | -18.57935 | -48.15181 | 2025-09-15 03:32:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ee8a7b3-b960-38b6-8912-784b0c8a37d5 | -18.61309 | -43.90395 | 2025-09-15 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c862450c-52e2-3369-abbe-686dd7b84d0d | -20.52245 | -47.47396 | 2025-09-15 03:32:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41be5505-518d-3cc4-af73-458128712134 | -19.71491 | -45.4518 | 2025-09-15 03:32:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92c5fe3a-393d-3452-add9-1ddc20c503c4 | -17.33992 | -42.64819 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 96dfb7e1-68f3-3dba-8a4a-7543b3a46af2 | -17.33597 | -42.6518 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 800ad52d-8107-3191-9008-288b61764b50 | -17.34104 | -42.6427 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c88b3244-eae1-3dca-b79a-541e2360e6ef | -13.92937 | -44.79869 | 2025-09-15 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aad5d0fe-0bf5-3c1b-ac13-5a208dedbea3 | -19.71437 | -45.4519 | 2025-09-15 03:32:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf06a9b5-0ed1-330f-8c85-19d52de00e19 | -17.31544 | -46.10651 | 2025-09-15 03:32:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b728505d-3399-3225-9955-dfb21171df7a | -13.93526 | -44.79985 | 2025-09-15 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 220122fd-603b-3bc9-9845-0bf69ef9d7cf | -14.50754 | -47.35687 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 126c529f-3d98-3c34-b780-580c90720e4d | -19.62082 | -43.74139 | 2025-09-15 03:32:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29aff1a0-7b64-373e-8c1e-d29951fb869b | -14.5088 | -47.35872 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b9c7add-b654-3156-9857-06d525a45c01 | -17.33859 | -42.66401 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf954594-3e10-3945-8f2a-835b242c4682 | -14.50405 | -47.34046 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3812f7b-be0f-3134-8402-bd5b831db09c | -17.34476 | -42.64913 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1ebb5942-effe-3057-9881-48e9a09c2471 | -18.61929 | -43.91035 | 2025-09-15 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcec5769-2e8a-34d6-955b-d96b522699ab | -20.86118 | -46.21585 | 2025-09-15 03:32:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b75abc5e-37fb-364e-89aa-70af5b55e2fd | -17.33881 | -42.65363 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2d5ada7-ebc8-3160-998c-37324c4103de | -20.19287 | -46.28915 | 2025-09-15 03:32:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6d23788-d468-3b66-b420-de8d4f9c4f99 | -14.50873 | -47.35144 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ccb4726f-b7d6-3d1c-bde1-2f70595814dc | -17.33704 | -42.64635 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3c3e6e94-9668-3214-97bc-ca0825f594c6 | -20.23077 | -46.17434 | 2025-09-15 03:32:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 20d129f7-d853-33ec-912e-5c2721e03e4b | -17.34188 | -42.6473 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1f93dcdd-3e5a-356c-abf6-241e1d5fadaa | -14.83476 | -45.48923 | 2025-09-15 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99a03ebb-48b9-31b5-b75a-2440f8f7cffe | -20.5274 | -46.86913 | 2025-09-15 03:32:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| db8dc88a-901a-3111-9bda-b50f68de4ddb | -17.14031 | -48.53349 | 2025-09-15 03:32:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ff678d72-e698-395b-ae88-fec9a6f1492e | -14.94441 | -46.58182 | 2025-09-15 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2448ddd6-d11e-3b31-9744-864c2ed3b443 | -17.13966 | -48.53313 | 2025-09-15 03:32:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f062af8a-a055-326a-a9e1-1d21682e98da | -13.93437 | -44.8042 | 2025-09-15 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 118bb1aa-900e-38e2-9b12-171c3b796937 | -16.78439 | -49.10501 | 2025-09-15 03:32:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0926b72c-e092-3a32-b030-1ea32379964f | -17.34587 | -42.64367 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f3e993ee-f9d1-3224-a05e-481eec8782ec | -19.65814 | -43.71375 | 2025-09-15 03:32:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 577d5eba-673c-3b94-ad1c-6ebbce9e68e3 | -18.71076 | -44.27563 | 2025-09-15 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db2137f7-5dd8-33db-b7b9-60d9dbdbcbc2 | -18.61807 | -43.90567 | 2025-09-15 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a22c3ea4-5bad-31c0-a9e2-0565ff5de047 | -19.7161 | -45.44409 | 2025-09-15 03:32:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8316d27b-b5b4-3ce6-818f-842664d81952 | -15.11488 | -41.87223 | 2025-09-15 03:32:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a818e524-57f0-3072-9349-c76e9f5de3ab | -14.25679 | -43.20654 | 2025-09-15 03:32:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 7a16f720-246f-3c94-ac43-5d1779ec5712 | -20.32493 | -43.68113 | 2025-09-15 03:32:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0104703a-189d-3739-8efe-711b9d15068c | -16.27884 | -45.68612 | 2025-09-15 03:32:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4a3ab3a-30c1-3ff1-8abf-f19e498fce73 | -14.25611 | -43.20993 | 2025-09-15 03:32:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f69caede-b6f3-32ec-b5b1-6822ec04900b | -17.34295 | -42.64181 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 146cf21e-1207-3711-8542-7575e0c6f94f | -20.22981 | -46.17861 | 2025-09-15 03:32:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| db6951ff-0139-37b7-8ea0-a7de442dbd7c | -14.27976 | -46.12753 | 2025-09-15 03:32:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0eb47da-91b9-382b-ae35-16e44380e50e | -18.78477 | -48.54025 | 2025-09-15 03:32:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcb1afe1-03f3-3f14-a9e6-1686d93b5ac0 | -14.59039 | -46.5976 | 2025-09-15 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dff0516-e47e-348f-869e-0e06ed19b757 | -14.59679 | -46.5993 | 2025-09-15 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17746d12-3996-3a44-8f68-1af801de87a6 | -20.86026 | -46.22004 | 2025-09-15 03:32:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b8aaf21-43de-340c-b549-18cde7880e64 | -17.34363 | -42.65464 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8f0a8f93-ffcd-3e7c-bce1-73dad995ecb2 | -16.28239 | -45.68728 | 2025-09-15 03:32:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8bc1429-2396-32db-9ac4-a2a9d23bf2b6 | -14.58967 | -46.5985 | 2025-09-15 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2d14355-ffae-308d-8dc5-946ead2de835 | -18.58837 | -47.20618 | 2025-09-15 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e6c2180-fb4e-36f5-b13b-32afee74ab31 | -17.61582 | -44.17603 | 2025-09-15 03:32:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ac092ca-d57c-3f16-8acc-51d02b3128a8 | -18.62003 | -43.90686 | 2025-09-15 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bdf088c1-0663-30d3-8284-fdb37998ffc9 | -17.14125 | -48.52645 | 2025-09-15 03:32:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c512757-fe61-3944-86e3-eba6b4bd09e1 | -17.76225 | -44.51375 | 2025-09-15 03:32:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57f6f523-9d2d-3e9f-98ee-4c221b3fd69d | -17.33768 | -42.65919 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05ec555e-e0d0-39ac-9e94-fd83f075ce67 | -19.71658 | -45.44396 | 2025-09-15 03:32:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a29727f0-2116-3bda-9481-2a75e90ccc4a | -14.94202 | -46.5928 | 2025-09-15 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 0aa135b8-5be2-3a9a-a288-42e45150bcd2 | -20.23534 | -46.18059 | 2025-09-15 03:32:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9eaa46b9-68cd-3343-a7e6-f4378be6ca43 | -20.08048 | -46.89119 | 2025-09-15 03:32:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f4d9bc6f-c80f-3bca-ae8f-1b1a3637e371 | -15.75114 | -45.0929 | 2025-09-15 03:32:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 875014b8-1e69-326f-a773-e37a337c3308 | -19.87297 | -42.48706 | 2025-09-15 03:32:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 26bdddcd-fe89-3d53-8a74-dc6ad23b0149 | -19.74496 | -45.12512 | 2025-09-15 03:32:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1600bf29-dc10-370f-95e4-a41aa799317e | -18.62635 | -47.3282 | 2025-09-15 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| cabdeb83-c43c-34ab-8270-d04de5b356f1 | -17.34562 | -42.65381 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3e8390b9-628f-3292-982c-13bb641b2474 | -17.3467 | -42.64827 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 86a61a9a-adb9-36b8-9cd2-c1ab5c551dbc | -15.41683 | -47.34688 | 2025-09-15 03:32:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| edee3c1f-737b-35ad-82b1-e81d59b8f66b | -17.31424 | -46.11195 | 2025-09-15 03:32:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b031e88-370a-3b3e-a801-5012975846be | -13.92846 | -44.80312 | 2025-09-15 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfe017b0-7468-36dd-9150-a2eada793494 | -20.52838 | -46.86484 | 2025-09-15 03:32:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c45190e2-40fc-34b8-8537-c23883386e8f | -17.3408 | -42.6528 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7ccdb605-35b0-377d-b34a-f83e9423b4fe | -14.50426 | -47.34741 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 718cf89d-d9a0-3c14-b96f-5ead16c65e10 | -14.13216 | -45.41599 | 2025-09-15 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a3e3c82-d697-367a-a6cb-78b630186524 | -18.63138 | -47.33512 | 2025-09-15 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| eef7c5c1-ac45-3ab4-97b8-f82b5105b033 | -13.92755 | -44.80751 | 2025-09-15 03:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 09a993d2-fbae-3b64-8f88-f67991345f6f | -18.62811 | -47.33452 | 2025-09-15 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a7b3cee3-3e13-3891-a2df-ebb8b103526f | -21.2579 | -45.63537 | 2025-09-15 03:32:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ca675337-b3c3-3ae2-847d-e6d3b0eb314e | -14.50175 | -47.351 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7c0c9db8-041f-3473-b72c-76ded60a9194 | -18.62934 | -47.32923 | 2025-09-15 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e71e87a7-e9d6-37cf-8dd5-b796ca122bf6 | -14.50295 | -47.34549 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c4e99132-b5c7-3851-a807-ebddba34b445 | -14.9432 | -46.58736 | 2025-09-15 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bf96ccad-493a-3e5b-966b-5bd1542195c0 | -18.61508 | -43.90505 | 2025-09-15 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cd633df2-742c-3b5d-b18b-f6feeea20542 | -19.62201 | -43.73561 | 2025-09-15 03:32:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b35ef0d8-cb05-3c56-a7af-7dd55140e622 | -14.12609 | -45.41463 | 2025-09-15 03:32:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06126c0e-2074-38c7-9516-ef09d9d28d90 | -20.08157 | -46.88643 | 2025-09-15 03:32:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb816d5e-de28-3c63-8e7a-ad381643e9d6 | -14.51445 | -47.35767 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4257d2b3-21a1-300f-9938-c4dcd7fa8c3c | -17.34249 | -42.66027 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c99b0c0b-5042-3113-b604-acef66bdc250 | -20.23437 | -46.18492 | 2025-09-15 03:32:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ab3ba5b2-e495-34cf-8600-aaffb8b1ba31 | -20.85464 | -46.21872 | 2025-09-15 03:32:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 19860d6e-d78e-37f2-9467-3721bf6a36c9 | -20.08763 | -46.88725 | 2025-09-15 03:32:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6976b5b-2909-340c-a66d-401ef655dede | -19.65776 | -43.71215 | 2025-09-15 03:32:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README15.md)
