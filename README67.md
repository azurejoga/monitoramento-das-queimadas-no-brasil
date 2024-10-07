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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3bc0fcb1-7d11-32b5-be1b-aa8173d0a3e0 | -19.80735 | -43.77956 | 2024-10-07 04:02:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9d3d1be-f893-375c-84f8-1164043311d3 | -19.80658 | -43.84806 | 2024-10-07 04:02:00 | NOAA-20 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3195a686-081c-3ce7-912c-903d687d03ec | -19.79514 | -44.29131 | 2024-10-07 04:02:00 | NOAA-20 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8bb7104-1b2f-3f11-9624-74d17ff33a8f | -14.48562 | -44.96056 | 2024-10-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 516f8747-3fb9-39b7-b8c8-64cc3ece5cdf | -19.94374 | -44.09004 | 2024-10-07 04:02:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| c7764963-1653-3f08-acfe-ce756a270cda | -19.9404 | -44.08942 | 2024-10-07 04:02:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 1a8eaab5-79a9-321a-954b-07fcf7b10411 | -19.9197 | -44.53172 | 2024-10-07 04:02:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e8786121-6af2-3eee-becd-8c10b5fceff8 | -19.91796 | -44.50006 | 2024-10-07 04:02:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cd2ad19f-31ee-318d-b0af-fcd7fc1a2a61 | -19.91735 | -44.50383 | 2024-10-07 04:02:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fee74065-7175-3f67-ab18-dc13e26d7bd3 | -19.91398 | -44.50319 | 2024-10-07 04:02:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6570b26c-9ead-3905-a45d-a2f0e357931c | -19.90671 | -44.10634 | 2024-10-07 04:02:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d555ce12-01e7-3dff-b089-0e3ec25269e2 | -20.20491 | -43.80017 | 2024-10-07 04:02:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d82ee57b-1233-316b-8279-fa84fb1c832b | -20.13704 | -43.86505 | 2024-10-07 04:02:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 469c8464-2044-32e5-959c-0bbc680875e1 | -20.13645 | -43.86876 | 2024-10-07 04:02:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 74a11ad6-f970-3e33-8452-4a5b80dba0c0 | -20.13432 | -43.86076 | 2024-10-07 04:02:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 5c08a910-2d8c-3333-8d44-230e41746e3d | -20.13372 | -43.86449 | 2024-10-07 04:02:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| db6b1de6-a499-315d-b3ad-21af54b46ccd | -20.13312 | -43.8682 | 2024-10-07 04:02:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 2cd18b38-ca7e-3420-a6d8-c9e96daab58a | -20.09865 | -44.22109 | 2024-10-07 04:02:00 | NOAA-20 | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7a2994c9-3189-34ef-a350-2a4357965f7d | -13.47164 | -44.49873 | 2024-10-07 04:02:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7095995-dc5a-3163-b607-2fd9f4538748 | -14.69068 | -45.1446 | 2024-10-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e60d913b-febe-3016-b769-a39853bd12a8 | -14.68779 | -45.1396 | 2024-10-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 85943e3a-ad85-30e4-8813-027db659d9ad | -14.68707 | -45.14387 | 2024-10-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 6df39f0c-d66b-3e26-bdc7-343589d409d9 | -14.4849 | -44.96482 | 2024-10-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 366449e9-930a-325a-884f-8bf9f5c0af54 | -13.87618 | -44.59432 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| befc30d7-17b7-3cd6-8bd6-ca3244a349e7 | -13.87547 | -44.5985 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1069007f-34fb-3582-882f-0c03959f0e89 | -13.87262 | -44.59369 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b22282cc-e89b-3551-8e9a-d6ddf55bc194 | -13.85765 | -44.59536 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58a04e82-2fe7-34dd-8bf0-d88ad88e498e | -13.85408 | -44.59475 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af0535d0-bb7d-3886-8cca-668a34e211de | -13.8498 | -44.59832 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed37f1fe-7411-33ca-b1fa-d278dbc9d3ec | -13.84623 | -44.59771 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d7dab68-9e5d-325e-8ea6-e314d2f1e98c | -13.84407 | -44.63189 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 03d9fbb9-2e06-37df-86d9-0c67359e472e | -13.84335 | -44.63607 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c1667b89-e7b9-3441-adb3-e05d952949ed | -13.8405 | -44.63126 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 866ebfbb-2b1f-33fd-8e02-fe45657bea9f | -13.83978 | -44.63545 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 995c3949-bbed-37ab-ac7d-0c5590fdfeda | -13.83768 | -44.60472 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76695844-812a-3f9d-a691-26197a5b5695 | -13.8362 | -44.63483 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8655fc6b-99c4-3f2b-bc88-5b76be107562 | -13.8334 | -44.60827 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1c0abbd-f856-33db-9ad6-ea06b90f570f | -13.83191 | -44.63839 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52417819-bb5b-3771-8244-de388f8eeb97 | -13.8312 | -44.64256 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c26a082d-05fb-310a-b479-2fdbc0fcbf45 | -13.82911 | -44.61185 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 294206f5-3724-305f-8b50-8f1496fc7f49 | -13.82838 | -44.61607 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 468f1f47-9ee6-35b7-9e7e-c62f655a55f9 | -13.82766 | -44.62028 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 438bd129-d1bd-3680-99b3-163184707766 | -13.82762 | -44.64194 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a98bd6e-cd91-33c9-bfc8-a4c02107dcb7 | -13.82409 | -44.61963 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6961bb9-bd62-3155-8391-dac6aa5c39e3 | -13.82405 | -44.6413 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d61377d-57df-3be7-a64a-429c5e9e4113 | -13.82337 | -44.62384 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6223c2b6-f452-3152-b674-602bddc56320 | -13.82264 | -44.62806 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 666b727a-71e7-38d4-9d02-980e36dc32a1 | -13.8169 | -44.64005 | 2024-10-07 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba1f36f1-969f-3e87-b9ae-4f60a5574155 | -16.84222 | -44.60559 | 2024-10-07 04:02:00 | NOAA-20 | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fd7ff56f-92de-3551-b5c1-85c195a4656c | -19.31055 | -45.02473 | 2024-10-07 04:02:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7787aec-0513-34bf-a4a9-53ef8bea1b99 | -19.19949 | -45.01684 | 2024-10-07 04:02:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cfd05c26-ff8a-33ae-be53-a9b8240c1d27 | -19.19605 | -45.01622 | 2024-10-07 04:02:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a87e8793-71c8-3c11-990c-11a9c6669f9d | -19.01658 | -45.5291 | 2024-10-07 04:02:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 8b383b34-d09f-3e47-b4e2-d6d7a5133731 | -18.74994 | -44.85215 | 2024-10-07 04:02:00 | NOAA-20 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca54f269-2b2c-3920-8f6c-b7f22fd6ad5a | -18.21994 | -45.05154 | 2024-10-07 04:02:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 497c7e8a-03e3-30c7-8d3a-3461c5744e24 | -18.21926 | -45.05554 | 2024-10-07 04:02:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ef23a15-e8cc-3e05-bb59-25163233ba3f | -18.21579 | -45.05489 | 2024-10-07 04:02:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5284904b-c93f-3bbd-9174-b01895714b69 | -18.09968 | -45.62601 | 2024-10-07 04:02:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9adfc583-c2b2-3f32-97f9-5ce5d9f10db9 | -18.09612 | -45.62537 | 2024-10-07 04:02:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f67e8b2-906e-3c75-aa27-857ddaeb24ce | -18.08118 | -45.62675 | 2024-10-07 04:02:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b381e12d-fac6-3c53-87c2-feacc5360fb1 | -19.76298 | -45.32362 | 2024-10-07 04:02:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfd68583-8b5b-3c17-a504-6a2f224785c4 | -19.75743 | -45.31434 | 2024-10-07 04:02:00 | NOAA-20 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0fc9e39-c946-3dba-ae8e-5fd45c39715b | -20.58 | -48.53 | 2024-10-07 04:03:27 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb2ab6d-f3cd-3538-be7f-3a27a460fb37 | -20.44 | -47.71 | 2024-10-07 04:03:27 | MSG-03 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 9f34cbfa-7480-3eca-8030-971a58546a07 | -20.46644 | -47.67392 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 57f3af9d-815f-3fef-ab6e-3f04e7466adf | -20.46642 | -47.65281 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| caa8ca75-62f0-3bd4-93d7-fa4af5b8ebb2 | -20.46569 | -47.66597 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 490adf1e-d8bb-3f78-bd9c-c0503688351c | -20.46549 | -47.67901 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 27.9 |
| a605bd18-65b8-342e-9c13-5b2db245f8f7 | -20.46548 | -47.65786 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 489096d0-7c62-3321-a074-9217279ed1bd | -20.46478 | -47.67105 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 95dec3e9-5d85-36e3-b0a5-8ec4ec7f16c2 | -20.46454 | -47.66289 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 111c230a-a858-353d-924d-df9726e3dcc5 | -20.46386 | -47.67617 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d4ef811b-c52c-3d3f-84d6-083b8832dc9e | -20.46371 | -47.65501 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c5f3c12-f7e6-3f33-81bc-ef910eb719f7 | -20.46359 | -47.66794 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 45.4 |
| bcce120f-12ba-3428-b85e-b0acc17ba630 | -20.46294 | -47.68126 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 42.0 |
| b310f69b-40fa-3975-8f16-aee9b70d0e3f | -20.46264 | -47.67302 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 4d4755e8-2f89-3d69-a638-dbffc740d4f8 | -20.46189 | -47.66511 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a896bd4-dcc1-3fc7-8719-d6e6d403c8be | -20.46169 | -47.67815 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 1aabb357-1e30-39b2-8747-78d7da02fc9b | -20.46097 | -47.6702 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f1f9ad5-f511-3728-ad62-96cf2514b0f6 | -20.46074 | -47.68321 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 7cb06cf3-10cb-3eb3-931f-f23896b5d2c9 | -20.46004 | -47.67532 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 93ee994e-3a88-3a32-9a4a-1d8ffc92cbcb | -20.45912 | -47.68043 | 2024-10-07 04:04:00 | NOAA-20 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5372a7d2-4adf-324b-837e-e5e22d758e58 | -20.45531 | -47.67961 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6e05d048-0426-34a4-90e6-69ad1d427b42 | -20.4544 | -47.68465 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7b38fefe-c1e2-317d-b724-2c2d1e831819 | -20.45257 | -47.69477 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9c91eff5-0f82-3ad2-8372-5ad251bfa345 | -20.45165 | -47.69982 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 729e321c-1c5b-3253-8970-e93b600b9e3a | -20.45148 | -47.67886 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5770b10b-1d54-3384-9091-05fa7aeaadfc | -20.45057 | -47.68391 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3be37b2e-0970-3ff1-be02-568b5bd4dfa8 | -20.44965 | -47.68896 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8a5646a7-d67e-3098-a37c-07cf65b0f663 | -20.44873 | -47.69405 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c578e104-7c00-37cf-a326-22b818f4e4e3 | -20.44781 | -47.69909 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 311f419a-a656-3ac1-a767-b99a23719550 | -20.44765 | -47.67814 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 5f7b17c0-fa01-383b-84a2-795789a44bd5 | -20.44673 | -47.68318 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 696b4ec9-9ce6-32ce-8607-055b65904a46 | -20.44582 | -47.68823 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 35eafd01-5851-3f6b-92f5-742c0df6f109 | -20.44489 | -47.69333 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 25fc039c-c154-314c-ab38-933fd625237e | -20.44398 | -47.69838 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72e5b401-46ee-3b30-9d48-6a0f220cb2ad | -20.44307 | -47.70336 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 23c0a0c8-cf72-3553-9b27-acd8630ce2b4 | -20.44215 | -47.70841 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8251d797-b314-3206-b690-7b23afffad97 | -20.44198 | -47.68749 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 25.9 |
| da728d9d-e973-3c08-a468-e630fad1539a | -20.44106 | -47.6926 | 2024-10-07 04:04:00 | NOAA-20 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 25.9 |


[Clique aqui para ver as próximas entradas](README68.md)
