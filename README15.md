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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6ce7d89-7eb6-375c-9ee9-2fa9dcd3b258 | -15.74403 | -46.2721 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b70e672-c978-3fd5-9453-c1facecb4135 | -11.86316 | -44.96526 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7e97fbe9-2f16-3c8d-a2e4-46c9535cab62 | -15.52786 | -46.81949 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3b62317c-d511-3512-bc1d-f1f5c23a2fc2 | -17.08506 | -46.24433 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 89dd91ec-6f71-37ac-82cf-1d6d3bd91cbb | -12.83153 | -43.80721 | 2025-10-04 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63de569f-9acc-3540-a691-c164b273d17a | -14.92424 | -46.87893 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f461fda-31fe-3f44-872e-a73bac2aefa2 | -11.85777 | -44.95752 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4641571-5a55-36ac-be20-5e5b29092d7e | -17.08644 | -46.23827 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0b3514e8-01e4-3796-b2b1-10acf432aa9a | -15.96071 | -43.33267 | 2025-10-04 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c2a0da56-e7de-3643-aa76-9565cfdd1a1f | -11.88593 | -44.9907 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dddac5a2-0f31-34ae-b7a2-f53613031534 | -12.02225 | -45.20014 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7f423f1-ac51-3208-9ec8-282a7cbbb393 | -11.45319 | -45.14234 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a4544b97-de92-3538-b2c1-63c5548dc297 | -12.11088 | -43.44557 | 2025-10-04 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d4eb6e7f-cd93-3d56-9840-f33c776afaea | -15.00114 | -41.42904 | 2025-10-04 03:25:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 307d60d0-08e3-3e9c-8416-aaa61e26e8bd | -18.58599 | -43.46663 | 2025-10-04 03:25:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e2df5a94-bada-32e7-8833-247bcdce4100 | -11.82519 | -45.04627 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6a531feb-c461-3657-9e96-30c405495f83 | -16.35418 | -47.07115 | 2025-10-04 03:25:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 64894b6f-6288-334a-b162-dcd60e3c212a | -11.88784 | -45.02596 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c67f7ac-ff22-35e7-8a31-1427745b4f1a | -12.1104 | -43.44741 | 2025-10-04 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bf290b42-606f-3642-a793-dbfe94e62437 | -11.7957 | -45.01908 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3e68277-7236-3f1d-8a6d-5be33d643a5d | -11.50268 | -45.01042 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a5a89af3-507a-38e3-899b-4db74a810a58 | -13.8834 | -46.51703 | 2025-10-04 03:25:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5d2dd546-dd74-35d6-b32e-4b6f8834375a | -17.08228 | -46.25651 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93ba3e3a-49e6-3897-b9b5-a6b82edd161f | -14.30593 | -45.86961 | 2025-10-04 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78189ceb-1f8b-36bf-834f-380c79ce6ecf | -17.15701 | -47.02943 | 2025-10-04 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dc2832a2-75d8-3aca-9362-ea992b7032f4 | -14.93137 | -46.89614 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f6e8c54f-bde1-3933-87d7-f7837d03ebba | -14.92229 | -46.87096 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 45c3df16-932d-32fb-8832-b3faa7f58479 | -12.52635 | -45.96926 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5f11d476-9a94-39b6-88a0-5be7fefc974f | -12.8377 | -43.80851 | 2025-10-04 03:25:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89d6c457-76c1-3d05-bf93-7b14bc330a01 | -15.82955 | -42.61663 | 2025-10-04 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b64b3c63-6a46-383a-aecf-713dc50c06d5 | -12.03322 | -45.21544 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 65c5f705-6a0e-3a90-807a-b345ccbbe556 | -15.53761 | -46.83122 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abd21409-636a-360e-8865-b8d558628057 | -14.20333 | -46.07815 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 65e397f7-ff15-36c4-9865-17b68eb114cb | -14.91865 | -46.88673 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| fea3a787-d607-3381-ad12-37838db37e48 | -11.84144 | -45.03587 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71b82ca5-05d6-375e-818d-1de54dbb6ba2 | -14.92785 | -46.89602 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5fc3a1cd-719c-3eab-b697-0a223df205f3 | -15.5291 | -46.8363 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e3c8c5bb-682b-3679-a756-99ea352fc120 | -11.47594 | -45.03681 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 4d5cb644-79cb-3ab4-90c7-77f10aa36459 | -13.56053 | -44.09772 | 2025-10-04 03:25:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3106bc0c-78de-342f-acf2-b124ca074b6b | -17.55986 | -46.7618 | 2025-10-04 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9e562592-7942-3813-acc6-5531fa8870e8 | -17.63172 | -44.4471 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2bb40506-4987-37ca-a533-4a2a57c5dab0 | -17.96131 | -44.26251 | 2025-10-04 03:25:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 68c079af-df3e-393a-a22a-d57462d4b240 | -14.24002 | -46.10634 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 0c5f5246-b443-39d0-a12b-95e4638a2a70 | -11.47718 | -45.0309 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0974e50b-2f04-3c1e-aa8c-6e0535e3522b | -12.03716 | -45.19658 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 5bda1120-f869-313a-9f0c-2bfa11b44f8c | -11.50917 | -45.0132 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8c2454ed-42b9-3ad9-9387-8a3ff110cb08 | -11.80042 | -45.01913 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4cae3b61-ff42-3abd-9e44-a8896e87a525 | -15.52474 | -46.82325 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e13da3d-9b7d-30a4-bc0b-293af3c6b93d | -14.9402 | -46.85778 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 009cbc32-2b52-3d39-b542-4a2c6396fd2a | -11.45361 | -45.14296 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f0c6e6ba-4388-30f4-97d7-284bdaa9f49a | -18.18065 | -43.5639 | 2025-10-04 03:25:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5abcf6e5-8d18-3642-b8c3-2b5eeefdbc0c | -12.93089 | -45.07637 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5293a963-9837-3ea8-8107-e5c267ff0ba8 | -11.799 | -45.02611 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c8f4065c-01c1-301c-b6eb-76e0ae6347ea | -17.15555 | -47.03648 | 2025-10-04 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d1cc5b5e-49f5-33d7-bd66-8eeead083a30 | -14.91693 | -46.89416 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1ddfc2db-530b-3140-b729-91013f89759f | -15.61067 | -46.93132 | 2025-10-04 03:25:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5628697-354a-3fd3-ab9c-5762d8b427e4 | -11.48278 | -45.0317 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 44297166-6d46-3ede-aaf2-cff604402f60 | -12.41777 | -45.15519 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 17b3f647-30a4-361c-bdc2-302e9aa297a1 | -11.45181 | -45.14911 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3e6a37fc-433d-3113-be98-4b7df5fa4e31 | -14.32262 | -45.86419 | 2025-10-04 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99d25371-58df-3132-9838-126c2902c81c | -17.96318 | -44.39402 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24ae4f07-061c-349e-86d3-67546c681726 | -17.08781 | -46.23226 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2a4e3568-675d-3fd9-b9e5-18d944f4928b | -11.72231 | -44.43896 | 2025-10-04 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b21543b2-3da9-3f96-95c3-e2a28574c2ac | -14.2309 | -46.08279 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 3e206804-0c7f-3e08-91a8-b44994a14072 | -12.07339 | -45.16586 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e71e260f-8b7b-31ab-a6db-5aceb4b94439 | -14.21 | -46.08054 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| fd6cde70-a3f0-3dcc-90ad-0e14f9646ef2 | -11.81179 | -45.04298 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 72420468-227c-3abe-8375-73f870ba7b15 | -14.94882 | -46.86866 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ca0364ac-1303-3920-900c-eb2cded663a9 | -12.95604 | -42.42213 | 2025-10-04 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 476158b0-959e-331b-9007-12c985084173 | -12.30283 | -45.36664 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| acdd39ba-25e7-3d7c-9065-3bf7ce9a90ec | -11.88201 | -44.9874 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 23e62c80-457b-3318-b412-0cd22c61cb76 | -14.19687 | -46.07482 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 71c80c0e-61fa-3098-a87c-0cd2a084953f | -14.29927 | -45.87337 | 2025-10-04 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96cc8cfb-1769-3d4f-8977-d322c8f763bc | -12.11119 | -43.44356 | 2025-10-04 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 452de985-f3c0-3485-b988-d11687ec7d80 | -18.18794 | -43.55692 | 2025-10-04 03:25:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e487ba4-09c9-3d1a-9b2a-4ba0dd25076a | -15.71889 | -46.28242 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 26584d30-18bf-3235-bdf2-ed4b1ef145e9 | -12.92677 | -45.06301 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 902ecf3c-be01-3aee-890b-fefef501f2e5 | -11.87928 | -44.98895 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 51eef768-fe70-3926-b415-bead6116d026 | -14.32946 | -45.86532 | 2025-10-04 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d697f9ff-cfcf-3eca-bb21-72b37e8ddbb0 | -12.52905 | -45.97789 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 19564f13-523d-3900-9c1e-e79803fe4f73 | -15.6186 | -46.9487 | 2025-10-04 03:25:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b693dc8c-0771-3965-8fd2-bde651197fb0 | -12.53042 | -45.98463 | 2025-10-04 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b3329ffc-0d48-34f4-84ef-6340aff584b8 | -13.29892 | -40.56393 | 2025-10-04 03:25:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d245dfd5-c318-3156-a17c-7cce40437f69 | -11.87515 | -44.97504 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 27584c33-2653-3211-b909-fcc3cfdb18c9 | -11.50267 | -45.00327 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 041ee5df-ea70-33ad-9bad-6088dc6b4cee | -14.24161 | -46.10052 | 2025-10-04 03:25:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 5817cc76-29b4-3c97-ad67-202232abd682 | -17.47723 | -44.04148 | 2025-10-04 03:25:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b88ad75-a5e7-3052-b854-fb85d159fb3c | -15.53356 | -46.81678 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 58138a65-2b7f-36fe-b73f-b351b4cfa607 | -17.98916 | -45.00997 | 2025-10-04 03:25:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 618f7c2f-2eef-34be-b870-7101d8a3d89a | -11.71657 | -44.43993 | 2025-10-04 03:25:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 05c9e403-a308-3aca-a4d1-bd354b537a63 | -15.52477 | -46.8334 | 2025-10-04 03:25:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 08160fd3-7047-36c5-84c0-8df0e51c170a | -17.15727 | -47.02903 | 2025-10-04 03:25:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7c2d038a-a7db-3e57-8d72-3f6ecb5eb993 | -12.04266 | -45.20418 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 86da3092-bc9c-3ec9-ad8f-10dc8a761990 | -17.08125 | -46.23067 | 2025-10-04 03:25:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ea253e4-d2ed-3e14-b5f1-ad200b6ef058 | -12.03455 | -45.20911 | 2025-10-04 03:25:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 27ff5a44-a22e-3fb1-ba9f-ff5f94b6d004 | -14.91356 | -46.89338 | 2025-10-04 03:25:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 11f808db-cec2-3635-b848-cc280c5cd2f4 | -15.83425 | -42.62142 | 2025-10-04 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 91f9c837-d3d3-3e4b-a4d9-e9695f3c6011 | -11.46576 | -45.15295 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46aee198-0489-330b-add0-eeecf7702863 | -18.59456 | -46.49323 | 2025-10-04 03:25:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db274780-1045-3276-931a-a0d58706fc31 | -11.48081 | -44.98001 | 2025-10-04 03:25:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README16.md)
