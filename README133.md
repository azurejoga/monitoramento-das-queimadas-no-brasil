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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4348ed10-5c36-35be-afb9-cb440749cc3f | -14.44094 | -46.11176 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b31fbea-e95e-31eb-be3c-617cda0d4134 | -15.1155 | -46.68567 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79153b12-720d-3280-9b16-3f401e85bb3a | -12.30287 | -46.87705 | 2025-10-03 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45467a49-ea64-3fa2-8afb-92c456eff330 | -14.91263 | -48.33276 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 62a7e212-a000-311f-93a4-cf0e025f31f3 | -14.28916 | -45.9695 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5cf330a-7a6c-3826-9692-6f9f367b0630 | -12.84208 | -50.49854 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04cd1094-41c3-3559-aa5d-8f3ddf464539 | -14.87115 | -48.31094 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ce927eda-d8a9-3755-b8c1-e37940e70b6a | -13.12478 | -47.86988 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c68e87b-d506-3570-81e6-6d69e6838afa | -13.32863 | -47.59118 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 39abd94e-383a-3a6c-a58c-ed1f0b230b40 | -14.68215 | -48.08049 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c516c52-bc95-3c86-b48b-5a69a570eca4 | -15.21553 | -48.00095 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0907f951-6285-36ee-8ce0-6e820cb5326d | -14.21332 | -46.0865 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e936fc3f-2d1c-3012-beb0-79d6f3a0892f | -14.23213 | -46.11136 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b3e20034-6b0f-3937-91ab-45cb9265ee32 | -15.34567 | -47.83033 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09490086-0048-3bd5-a407-a63c2f16e675 | -14.01462 | -44.96883 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36787803-6631-31e6-adbf-75fcbbc4de31 | -13.1465 | -47.89569 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba0f3d75-ad2c-3818-b325-43caca651e64 | -17.24993 | -47.01722 | 2025-10-03 04:34:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d730562-f0e8-366d-9a08-9990a4245ee6 | -14.64851 | -48.11996 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 875fa8a5-260c-337a-b7ea-d65fad5b173e | -20.43921 | -49.97815 | 2025-10-03 04:36:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ccf2adb-822b-3240-8755-2a03482a30dd | -20.85259 | -49.48068 | 2025-10-03 04:36:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| ae86e205-cc78-3210-8690-49d827fa8195 | -21.34798 | -45.00949 | 2025-10-03 04:36:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3e811f12-839c-3a32-b49b-656162e9e96a | -21.284 | -44.97626 | 2025-10-03 04:36:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d49a4638-300c-38d5-b519-452412a5fadb | -21.34321 | -45.01307 | 2025-10-03 04:36:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bb3f3b4d-07e3-3dd9-89e2-d0cdbd6e26f2 | -20.99952 | -49.2164 | 2025-10-03 04:36:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 3fc85942-b839-3dcc-bd21-186897fa535e | -21.66071 | -45.83408 | 2025-10-03 04:36:00 | NOAA-20 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f73c2918-78ff-318d-aa92-61708ce30e94 | -21.28453 | -44.97194 | 2025-10-03 04:36:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3b709db2-0ba2-3f65-b1a5-e2faedf8943f | -20.8498 | -49.42869 | 2025-10-03 04:36:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e9ae7043-3f6b-3732-9bc5-1b31ebb943c0 | -21.34848 | -45.00533 | 2025-10-03 04:36:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2358bb76-2840-35e1-9b0a-30c0a0c67ef3 | -21.16914 | -45.24553 | 2025-10-03 04:36:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fc5039c7-d5d8-3e8b-84ed-2505e098a536 | -21.3475 | -45.01355 | 2025-10-03 04:36:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9d4944d9-1f85-312b-9e4b-348ab5898140 | -21.06834 | -45.61348 | 2025-10-03 04:36:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de493f3c-bfa3-35db-8f0f-208fb0533902 | -21.40471 | -45.83408 | 2025-10-03 04:36:00 | NOAA-20 | FAMA | MINAS GERAIS | Brasil | 3125200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 195a55c0-9db9-342d-b52e-0e43550598f3 | -20.86276 | -49.48234 | 2025-10-03 04:36:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 88c71916-f2a5-30ed-b900-8d7e3fa18f55 | -20.91194 | -46.22424 | 2025-10-03 04:36:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ab50b4e1-a44d-33d8-a789-2bbe14644286 | -21.26985 | -45.61991 | 2025-10-03 04:36:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8a28922c-d444-3db6-b12a-d09d0ac8c6dc | -21.34369 | -45.00905 | 2025-10-03 04:36:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 64a29db9-39b5-3f84-8ade-d3d0fc2edc44 | -21.52348 | -46.07679 | 2025-10-03 04:36:00 | NOAA-20 | SERRANIA | MINAS GERAIS | Brasil | 3166907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0ca15d1d-24bd-3ff4-ac8c-5bf5aba4725f | -20.99838 | -49.22421 | 2025-10-03 04:36:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b4e6231e-7a58-32b3-be7c-e4b87e1c443e | -20.99553 | -49.21973 | 2025-10-03 04:36:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 1d7645ae-6d0b-3efc-8f39-1b4d241b74db | -22.37692 | -49.01667 | 2025-10-03 04:36:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f45e51fa-65cc-3d79-9bb0-83eb4ec3a05e | -20.87407 | -44.74735 | 2025-10-03 04:36:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9e5b00cf-469a-3aa6-87bf-370140fe4aca | -21.00237 | -49.22086 | 2025-10-03 04:36:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f9009986-5c43-3a95-afaf-0396c4f028ce | -21.34418 | -45.00494 | 2025-10-03 04:36:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9a9989b2-6968-368e-a9ad-5a91ecd229c7 | -20.99895 | -49.22029 | 2025-10-03 04:36:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 34a31972-fffe-3287-802e-100b25357edb | -21.33942 | -45.00839 | 2025-10-03 04:36:00 | NOAA-20 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 246bc816-38ee-39a6-bb4a-486df025b8ce | -20.9961 | -49.21585 | 2025-10-03 04:36:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b545a7fe-0759-30aa-989d-afab5b488851 | -20.87354 | -44.75177 | 2025-10-03 04:36:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ba3ae5eb-3c6b-3443-bf82-e016dde59be0 | -21.24467 | -45.014 | 2025-10-03 04:36:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8b7d745e-c5b5-3880-8f22-e61c00b9cc35 | 4.53278 | -60.2925 | 2025-10-03 05:21:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0db51459-9690-33db-9ea8-1fe0b0c2e80f | 1.52166 | -55.82579 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| d0b5e507-402c-3757-9609-9500d5330532 | 1.73014 | -55.88201 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ecc327e1-e4f9-3d4b-97e0-7dfc80fc87ce | 1.71949 | -55.88361 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad630876-6994-3205-a581-a9dbf7b2a081 | 1.52002 | -55.83847 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d8cf636-893c-3a09-8b55-cebdde361ba9 | 4.38678 | -60.11925 | 2025-10-03 05:21:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6baf455-76f9-3cd2-928d-03723295c73d | 2.71443 | -60.18698 | 2025-10-03 05:21:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2e06196-be10-3222-8f63-6edebfb0b259 | 1.52358 | -55.83791 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 117e12e3-6fc1-3c8b-a506-a52503330fdb | 1.78868 | -55.81482 | 2025-10-03 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ea376ec5-2704-3b2e-b4ae-f6b0aef488b5 | 1.71885 | -55.87963 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f259f93e-9400-3098-8338-1a79f0e0d696 | 1.74885 | -55.86246 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 294b9d17-6e67-333c-ad2a-fc0c70ecc6b0 | 1.51418 | -55.84766 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36d56341-02da-3b9b-a630-e3c837173534 | 4.54971 | -60.70579 | 2025-10-03 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0646922-272e-3316-a299-a1bc618b5d52 | 1.52102 | -55.82175 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 28e9e241-01a4-3b86-b314-7e11be9992f0 | 1.78576 | -55.81943 | 2025-10-03 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2cdb08ba-cc48-3ef9-a98c-90683fb0939b | 1.52038 | -55.81772 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1bfc2336-0ecb-3533-beb2-dbae977835b2 | 1.72177 | -55.8751 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aef8e6e3-aef5-3fae-b75b-e19fe9473966 | 1.51225 | -55.83553 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc93fbc0-24c0-3367-9ab6-35ced50359d8 | 4.5532 | -60.70526 | 2025-10-03 05:21:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20a14953-e040-3aaa-9317-450e61d9203d | 1.52066 | -55.84251 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9e342024-60ba-3ca0-825a-d0e17226bda3 | 2.4251 | -61.34795 | 2025-10-03 05:21:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d658d1f6-67b6-323e-9893-4b089efc4b67 | 1.78346 | -55.82803 | 2025-10-03 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6068594-bed4-38d9-8b59-521f5f410dc6 | 1.51938 | -55.83442 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c75987e8-2aff-34d8-b2a3-90713fc6b71a | 1.51354 | -55.84362 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 225aa82b-1438-33b1-9f96-26438ebc0207 | 1.51974 | -55.8137 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af2c0aa9-cd66-38c8-808f-872668a60ddc | 1.51289 | -55.83958 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df8cfa71-1ca1-3bfb-8a61-fcd760ef48a9 | 1.5213 | -55.84655 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 9b24ef99-e1d8-363c-b03e-fa8a976a0554 | 2.27684 | -50.73164 | 2025-10-03 05:21:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b74305bb-42c7-36a6-8e6d-1480cadb3d92 | 1.5223 | -55.82983 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 31017905-da3b-3530-8ed7-410f523f1d6a | 1.52294 | -55.83387 | 2025-10-03 05:21:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4352aeeb-61a5-3803-b32f-4b88664aa3cf | 4.45699 | -60.02608 | 2025-10-03 05:21:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd30aa71-8980-3001-97c3-9d600c7f9a3b | 2.11955 | -55.81974 | 2025-10-03 05:21:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d82497af-1885-3e01-b750-469e93294e44 | -10.34666 | -48.18023 | 2025-10-03 05:23:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c130b9e3-b96a-3e36-9af0-7b5b3de41a37 | -2.92583 | -48.30693 | 2025-10-03 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 45f4726c-76a3-373a-90f8-ea028949f73e | -5.61588 | -51.93676 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 233908b0-713d-35c5-ab51-4cd36a1c95b8 | -9.99471 | -50.23269 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 812b4244-58cf-3192-b369-bb2d02a246b5 | -10.00558 | -50.25786 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e710d23-12e1-3013-b206-6ff71cd8ea13 | -10.89873 | -56.19868 | 2025-10-03 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cae9296-432f-3144-bbef-54ccd3076637 | -6.03887 | -52.42284 | 2025-10-03 05:23:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26906c1d-2257-3a8e-9c4c-3df862dd5fc9 | -11.53675 | -49.8259 | 2025-10-03 05:23:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71a7a898-26d8-3d3d-a2ef-483d3e806a75 | -9.99845 | -50.2145 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62c3bf03-2104-37c6-a80f-66ab5cfd73d5 | -10.28695 | -50.29914 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fbe9e230-35f0-3612-9776-b186ae50b6bf | -10.12156 | -52.34702 | 2025-10-03 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42150b71-c872-359d-b0bc-c2314c08fb4f | -3.33575 | -52.0551 | 2025-10-03 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 769bd19e-a744-3c53-b203-7093aefc8cd9 | -9.99016 | -50.23222 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7b82448-bc60-3b07-8ec0-675498dff524 | -12.93922 | -48.43433 | 2025-10-03 05:23:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39422f95-4068-3edb-9134-e3c163bfeef6 | -10.88076 | -53.76995 | 2025-10-03 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80f8e987-75fa-3beb-9d9a-73919f8fd923 | -7.93899 | -61.5104 | 2025-10-03 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f218eeb2-d11d-3440-847b-f5ba4b2d84d7 | -3.33656 | -52.04951 | 2025-10-03 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7395802e-716d-3b6c-a141-ea4f9053ecc9 | -9.99354 | -50.24194 | 2025-10-03 05:23:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e20db486-245b-3cb6-81a4-3fd4098cad1b | -5.00108 | -56.06894 | 2025-10-03 05:23:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dad0bda8-9e0a-39a3-aa43-de2b8b5d3daf | -11.63045 | -47.99618 | 2025-10-03 05:23:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README134.md)
