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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7433f674-7a00-34cb-aa90-0821de5f6873 | -12.79645 | -45.00378 | 2025-02-21 04:31:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8854f530-4271-3d2a-9359-39ffd820c1e8 | -14.42518 | -45.63496 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34ba63af-c539-3af6-8925-681bacd82f1f | -12.35129 | -47.98999 | 2025-02-21 04:31:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbcf6796-e3d5-371b-99df-f1fc4549a91d | -14.42583 | -45.63023 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 732ebee8-f55c-3734-bd34-354692899efa | -14.45591 | -45.66362 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13b48e57-4abf-3709-a693-68f7ad2633bf | -11.97237 | -45.15606 | 2025-02-21 04:31:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afe9ae66-c571-395f-bdc6-a94abcd27778 | -12.80346 | -45.00972 | 2025-02-21 04:31:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11fc844d-23a2-3582-aae0-63b1a420846a | -14.42831 | -45.64025 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da14dde3-64c7-3c13-85f2-93466b27d452 | -12.80029 | -45.00432 | 2025-02-21 04:31:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d04c53a3-f921-31ff-b671-b20634583700 | -14.11202 | -45.66842 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fedc9e4a-149b-3893-8eaa-7481917d0128 | -14.42961 | -45.6308 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d9981a3-5f08-3a6b-b6fb-ddee7134f7fa | -14.43209 | -45.64081 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d7cd078-8759-3254-afbf-2df519d1a9c8 | -12.75581 | -48.34167 | 2025-02-21 04:31:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ddc7696-b3de-3eb5-9b38-dddc227ea77a | -14.43965 | -45.64193 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1cde2cb-3ff1-3084-ac5d-723763e90bb8 | -14.43339 | -45.63136 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f71912c7-6868-35d0-9f48-9762a70b6584 | -12.35464 | -47.99052 | 2025-02-21 04:31:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2730a454-7b08-398f-a44f-7cadcf7923ae | -11.57184 | -47.63198 | 2025-02-21 04:31:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3e5cd5f6-8e1f-3264-b3c6-86ba434e3a99 | -14.42896 | -45.63552 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 969705c8-a2ad-3cbf-9316-e6234d840d9d | -12.0993 | -51.22903 | 2025-02-21 04:31:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dfe2aca2-8797-3174-84d3-e4df0fd6e71c | -11.57126 | -47.6132 | 2025-02-21 04:31:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b062bf8-952b-31d8-a905-51f65572e8b6 | -14.45214 | -45.66306 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cc8cf68f-d39c-3eff-b8ca-0f12360c6ef2 | -12.33024 | -52.47918 | 2025-02-21 04:31:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57b44cb7-fa9e-3fc7-ad9d-4b0d6c8fb36c | -12.78036 | -47.11656 | 2025-02-21 04:31:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53b32be2-8a30-3581-b3b5-1f48c800cc38 | -12.07127 | -48.46705 | 2025-02-21 04:31:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b2201e9-98b9-3b65-9043-f3256de7598e | -14.4403 | -45.63721 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 426da335-fdbf-336b-8a00-6342987cbfdf | -12.07623 | -48.45694 | 2025-02-21 04:31:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a2387a1f-e093-3cb3-90fb-c7c5ea0dc70c | -14.43718 | -45.63192 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99730ac3-9236-3fe7-a892-7d8c8cd5c04a | -11.86184 | -46.93798 | 2025-02-21 04:31:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3474418b-9646-3049-bfc8-27015f8b537e | -14.43522 | -45.6461 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f737fbf3-28be-36c7-92f8-bb6a527fc9ec | -12.07569 | -48.46049 | 2025-02-21 04:31:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8360ae6a-a25b-3dff-83b2-8c09489da17b | -12.79961 | -45.00918 | 2025-02-21 04:31:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3547b579-cbf4-3a45-99cd-bc0cf89bc5fb | -13.52932 | -46.50469 | 2025-02-21 04:31:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f72f75e4-657e-32cb-9c81-b33f36228cf6 | -11.85437 | -46.94074 | 2025-02-21 04:31:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5034ac14-dcbe-3fb2-ad9f-30731098260b | -11.85494 | -46.9369 | 2025-02-21 04:31:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a8156a9-0b09-30ad-a39a-f6021178ddef | -9.29908 | -43.17689 | 2025-02-21 04:31:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 55c22a73-ea43-3618-b272-e2da0672e8b4 | -12.32125 | -46.66499 | 2025-02-21 04:31:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f61417b2-7e1f-37bb-886d-90f5c25e07bc | -13.96276 | -48.50581 | 2025-02-21 04:31:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00a59932-a42b-32c3-bc36-dae6d48445a4 | -12.07182 | -48.4635 | 2025-02-21 04:31:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58667456-7957-317f-8fb6-f7c31ca24a99 | -11.80642 | -46.65281 | 2025-02-21 04:31:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5c7b139-53af-367f-9699-f1ef7fb050d9 | -14.43652 | -45.63665 | 2025-02-21 04:31:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 733eb2a5-8f73-35bc-a176-df4d52093ab5 | -11.85839 | -46.93745 | 2025-02-21 04:31:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 310e284b-f620-3152-bdf2-7b0adfac21e2 | -19.43874 | -49.30869 | 2025-02-21 04:33:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a4135e47-7dc1-35eb-9703-b9e1d2b18a0f | -22.59068 | -43.16382 | 2025-02-21 04:33:00 | NOAA-20 | MAGÉ | RIO DE JANEIRO | Brasil | 3302502 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e4ac6e13-b019-3397-bf9b-932b4b107bf4 | -15.56955 | -47.85479 | 2025-02-21 04:33:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5af359d-c865-32d9-a988-277e963e9b13 | -17.04962 | -45.04139 | 2025-02-21 04:33:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8cd61db1-415b-39a9-8232-8db221cd22d5 | -17.46113 | -47.01132 | 2025-02-21 04:33:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6b2f653c-b902-38c9-99b3-1a9766151682 | -20.30461 | -46.4964 | 2025-02-21 04:33:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6599f9aa-72e6-3d9f-8205-07caa32d02ae | -17.45768 | -47.00829 | 2025-02-21 04:33:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 647aed5f-7f3a-3ed9-a56b-363be43c4d4d | -17.46174 | -47.00693 | 2025-02-21 04:33:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c740fc3-221f-37b5-90e0-c09c1a22a190 | -16.73706 | -48.11655 | 2025-02-21 04:33:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd10eda8-91d6-350b-ac71-d25e80c2ccbd | -20.95794 | -48.81164 | 2025-02-21 04:33:00 | NOAA-20 | EMBAÚBA | SÃO PAULO | Brasil | 3514957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 45de4dd0-975e-3ea5-b576-15d6b0ef8fb9 | -16.58677 | -50.46997 | 2025-02-21 04:33:00 | NOAA-20 | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e81fc9e5-a475-3ec5-98b3-d58491264478 | -15.74331 | -49.54789 | 2025-02-21 04:33:00 | NOAA-20 | ITAGUARU | GOIÁS | Brasil | 5210604 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b258e353-f3eb-309a-81d2-0d88c980deb6 | -20.19799 | -43.28861 | 2025-02-21 04:33:00 | NOAA-20 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d14bc4b2-287c-3660-abc5-f4a626a8cc1a | -18.76369 | -50.70957 | 2025-02-21 04:33:00 | NOAA-20 | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77c2642c-46f9-34bb-8b9a-85f8ecb87514 | -20.3108 | -45.58386 | 2025-02-21 04:33:00 | NOAA-20 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 886b7a0f-3855-3c65-adb2-5198cb915aa6 | -15.39199 | -43.7383 | 2025-02-21 04:33:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25ee0a22-3728-34d4-8c56-a4b608ce5bd4 | -16.3469 | -43.69535 | 2025-02-21 04:33:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31f40980-a1db-30d0-ba8e-1d26174ee0a9 | -17.87078 | -45.54681 | 2025-02-21 04:33:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7334e2d3-da65-3470-8362-cd32f9f1cfe2 | -16.68137 | -43.88528 | 2025-02-21 04:33:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7fe540c8-6d98-3438-b178-a0c08daaa373 | -19.96492 | -44.18431 | 2025-02-21 04:33:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 42c68091-7d89-3559-8eb0-e7e22da23ded | -21.26172 | -49.00783 | 2025-02-21 04:33:00 | NOAA-20 | PINDORAMA | SÃO PAULO | Brasil | 3538105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 771301ce-1f9e-3544-8804-216e659ebde2 | -15.01178 | -52.43671 | 2025-02-21 04:33:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f573660-2aec-318f-822c-beee4376d385 | -17.86877 | -45.54499 | 2025-02-21 04:33:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a35fd164-566a-3c4b-b514-0f719b9b7de8 | -20.16545 | -47.27941 | 2025-02-21 04:33:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63f2e9ff-3301-39bc-8c2f-7b06e6745ffd | -17.4607 | -47.01324 | 2025-02-21 04:33:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6901ef92-afbe-3f2f-a566-75b512a9b637 | -16.78444 | -49.6184 | 2025-02-21 04:33:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d57b7a96-ad90-3b25-9e4b-f47f920a05a8 | -14.45557 | -47.9132 | 2025-02-21 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c71d711d-cf65-3509-acb1-7c27fd09982e | -17.46132 | -47.00884 | 2025-02-21 04:33:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d733dac9-7db1-3481-bfe3-ee38c352a214 | -20.30073 | -46.49584 | 2025-02-21 04:33:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b7683ee-66e2-3511-8055-1dbb6c542f53 | -15.73068 | -43.14971 | 2025-02-21 04:33:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1daa6c65-e1b0-34f3-8569-882954d61b2d | -18.0613 | -48.90472 | 2025-02-21 04:33:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dd1ce172-3a66-3ae5-a479-63bcbd3a256a | -17.00724 | -49.78062 | 2025-02-21 04:33:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d1ecb20-4780-39be-9f4f-07fa94052169 | -16.68007 | -43.88647 | 2025-02-21 04:33:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdb08b4d-14d5-36f8-bf27-023f1f24001e | -19.4393 | -49.30487 | 2025-02-21 04:33:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccdae5a7-ec7a-35c5-9ee2-32c4c69e1dbc | -14.45613 | -47.90944 | 2025-02-21 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c03879d7-e9f1-3e76-a0e7-8df8b3fdfe93 | -18.63252 | -43.1726 | 2025-02-21 04:33:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5ea88508-0667-39f4-a616-7e0412679c58 | -17.05367 | -45.04203 | 2025-02-21 04:33:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6dd4d533-916f-3ee9-aaac-12c399cea190 | -21.18029 | -44.27141 | 2025-02-21 04:33:00 | NOAA-20 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2f9dd768-b6fe-32ff-9efe-f52a08c640b2 | -17.08476 | -49.38757 | 2025-02-21 04:33:00 | NOAA-20 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ad63ff0f-6614-3eb2-b066-2ea17a02d174 | -15.55529 | -46.27529 | 2025-02-21 04:33:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 512e5790-80e0-3245-9584-348a850e17a8 | -14.45273 | -47.90888 | 2025-02-21 04:33:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54b268ad-4df4-3471-9481-8d77679e7635 | -18.63723 | -43.17305 | 2025-02-21 04:33:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 87d15db6-d0e1-3f9d-82a4-fc1b331ffe56 | -20.76459 | -46.76714 | 2025-02-21 04:33:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 96ba0cd7-1c31-312d-862f-5c1923081d26 | -20.19743 | -43.2863 | 2025-02-21 04:33:00 | NOAA-20 | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 0bdfdb11-beeb-3649-b543-3e024cc2adc4 | -17.45749 | -47.01077 | 2025-02-21 04:33:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e2392eb-5def-303a-b2a5-b420bdfa98c7 | -15.07926 | -48.94614 | 2025-02-21 04:33:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| add779fb-9934-358c-8150-bd9091ef2549 | -20.16482 | -47.28408 | 2025-02-21 04:33:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71c24978-b76e-37ea-92e1-1b8bb35bcdc1 | -15.91525 | -48.06945 | 2025-02-21 04:33:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 151200ee-87a0-3809-b969-20246135f96a | -23.59396 | -47.43974 | 2025-02-21 04:36:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b3594356-e538-32d9-9b49-7be6e05fcc9a | -22.9021 | -43.7519 | 2025-02-21 04:36:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| e5e536d3-2f02-38a5-a903-0e76d90315ac | -22.54074 | -48.81443 | 2025-02-21 04:36:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0787d49b-1c5d-30d3-9278-66055eb353cb | -21.4783 | -52.62235 | 2025-02-21 04:36:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 191aba0d-be16-3dc8-a6ec-109768d062ba | -23.33873 | -46.77095 | 2025-02-21 04:36:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b653b063-4c34-3afa-bff2-d9c6c2b0518c | -23.77625 | -46.70771 | 2025-02-21 04:36:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9c55b433-8865-32e5-8f71-0b2a565301a5 | -22.82394 | -51.36474 | 2025-02-21 04:36:00 | NOAA-20 | FLORESTÓPOLIS | PARANÁ | Brasil | 4108007 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f61fd670-fec0-3799-bedc-9bb3146bbb0d | -28.58646 | -49.44236 | 2025-02-21 04:38:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3fe7e3fc-0175-3dec-987c-cdca70f37da7 | -29.77856 | -51.17394 | 2025-02-21 04:38:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 2.1 |
| 9e324715-dba5-358f-8df7-b1a3011b912e | 2.51095 | -60.9847 | 2025-02-21 05:20:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5605bf69-3a28-3a85-915f-97839803ec4c | 2.66958 | -61.40741 | 2025-02-21 05:20:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README6.md)
