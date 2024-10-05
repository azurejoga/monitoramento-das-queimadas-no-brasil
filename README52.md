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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce2048d9-3e70-3551-8a34-3a1a85e80768 | -18.86241 | -43.60382 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| c6b7921e-d160-3512-878d-90a2f9a9b95e | -18.86211 | -43.58423 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 871709f7-5c83-3785-bdb0-f6050df2504a | -18.85876 | -43.60283 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5512861e-bbe0-3ccc-b789-c308b1a3dc17 | -18.85838 | -43.58369 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 23d42c43-85bf-3268-a5bb-d05e39a60f9f | -18.8501 | -43.58706 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 86e22a9c-3258-389f-93db-bf3ab883fec1 | -18.84931 | -43.59146 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2251e12b-7857-372f-9bed-48aba2075887 | -18.84556 | -43.59094 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 69b7f900-9841-345f-8b82-47302463f100 | -18.84346 | -43.59261 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 2aaef05a-19ae-36f3-8f36-2efe52030507 | -18.8431 | -43.60455 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c565fce5-3e68-361d-9dd5-fad15a61ce91 | -18.84184 | -43.5903 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e6de8b81-c8e0-3e5b-8782-2f0d541a2654 | -18.84105 | -43.60636 | 2024-10-05 03:51:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 40a2db9d-fcc6-37ea-9f6a-82f7cf78871d | -20.51536 | -44.89654 | 2024-10-05 03:51:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 769ed409-3d9c-30ac-b147-b0c95673f5c9 | -20.51443 | -44.90157 | 2024-10-05 03:51:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c5f8915e-5611-3449-b19a-7d83f0d639e1 | -20.51054 | -44.90081 | 2024-10-05 03:51:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 04cc2ee2-cb94-3850-8a7e-46bc11549f04 | -20.00944 | -44.4827 | 2024-10-05 03:51:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 391c9059-f1a1-3764-8180-f656fa818561 | -21.0433 | -44.80405 | 2024-10-05 03:51:00 | NOAA-21 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| d1befe1e-1233-39fc-9b8d-d47865176e0a | -14.86647 | -45.13689 | 2024-10-05 03:51:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a314f6c-5e56-3614-84ba-f6c4ae6211bc | -14.86566 | -45.1412 | 2024-10-05 03:51:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 59b342b1-a18e-3d35-a882-f74ab9af64e3 | -14.48528 | -44.96242 | 2024-10-05 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db9afe74-977d-3773-97a7-0aaf6c5750ba | -14.48095 | -44.96162 | 2024-10-05 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1850a32d-7e5f-3b2a-9510-eeeafdf4d85d | -14.47663 | -44.96081 | 2024-10-05 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e1a8c0b-00bf-3102-8d97-cc4f85551bb3 | -14.47583 | -44.96509 | 2024-10-05 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 515ba28b-a815-3c7b-99a5-99c07a43717d | -14.32766 | -44.70784 | 2024-10-05 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aced764f-60ae-34fb-9e61-ba0b046ba57b | -14.32415 | -44.70291 | 2024-10-05 03:51:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b04f90f-a667-30ff-b7dd-4ecbbee7142d | -14.07049 | -43.95521 | 2024-10-05 03:51:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ffe716b-8b08-3801-bbea-cc5b5a21f8b8 | -14.04751 | -45.14413 | 2024-10-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b21e7fdd-7cc5-3930-874d-a5dd71886507 | -13.87377 | -43.78773 | 2024-10-05 03:51:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 456d40b4-ad1c-37ce-a28c-7bf34ac4556e | -16.35091 | -45.67504 | 2024-10-05 03:51:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4143da29-9075-316f-9133-61c352f67e16 | -15.85955 | -45.26732 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b8dbf60-38ee-3521-a5ce-aaa5250b316d | -15.85876 | -45.27152 | 2024-10-05 03:51:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63348cd9-3347-3517-a3c8-27832a606789 | -15.72651 | -44.83284 | 2024-10-05 03:51:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3043bc8c-1c89-398a-bec8-904762f8b90f | -16.96884 | -44.76505 | 2024-10-05 03:51:00 | NOAA-21 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66dec95f-27ce-3486-af77-868cfa50f57d | -19.2967 | -46.20784 | 2024-10-05 03:51:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96922f50-61f1-34fb-89c4-daeb615774f7 | -19.29587 | -46.21218 | 2024-10-05 03:51:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 87f19e44-9bd2-3302-b555-7d4ab4a0f00c | -19.29503 | -46.21654 | 2024-10-05 03:51:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ee24beb1-9b5f-3a10-bd22-04a36bbc7e30 | -19.29242 | -46.20687 | 2024-10-05 03:51:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71df1012-fa29-3752-be28-60647de01ee0 | -19.06714 | -46.3359 | 2024-10-05 03:51:00 | NOAA-21 | CARMO DO PARANAÍBA | MINAS GERAIS | Brasil | 3114303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9ba41a5-f3c2-37e9-8a00-598f1a591f7a | -18.10629 | -45.60014 | 2024-10-05 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7b66eeb-fa3c-3fb1-9fc6-3db49e2b1f19 | -18.10287 | -45.59502 | 2024-10-05 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3232e57-cfd9-3271-8562-d930f428a35b | -18.10209 | -45.59917 | 2024-10-05 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c54a88b8-1dc9-34f8-96df-300e7efcb401 | -18.10131 | -45.60332 | 2024-10-05 03:51:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9530ab68-442d-3adb-82b0-9b07f101e7cc | -20.07792 | -45.78647 | 2024-10-05 03:51:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce99e7fa-95ac-3e1f-a860-69ee77334cef | -20.07638 | -45.78288 | 2024-10-05 03:51:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d1d28e34-e77c-3658-8a6d-67219d65c20c | -20.07562 | -45.78692 | 2024-10-05 03:51:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 795db039-baa2-34a5-afb1-3acab5c5ff4b | -20.0746 | -45.78148 | 2024-10-05 03:51:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9d36d19-6871-3d06-9e04-0aa9584c1aab | -20.07382 | -45.78552 | 2024-10-05 03:51:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2871b52c-66ba-3493-b6f3-cdca7e1e88d0 | -20.07304 | -45.78951 | 2024-10-05 03:51:00 | NOAA-21 | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c6af165f-47a1-3994-ba85-fd9129aab60f | -20.79952 | -45.42809 | 2024-10-05 03:51:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a80508e1-8b5f-3902-b6c1-cfc08345eb95 | -20.79774 | -45.42812 | 2024-10-05 03:51:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5246dccd-0663-3fd7-be9a-b0dc981e2144 | -20.79481 | -45.43105 | 2024-10-05 03:51:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b26e14f8-ae83-382e-8e39-bafca8dbaebd | -20.79305 | -45.43108 | 2024-10-05 03:51:00 | NOAA-21 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1142188d-14bc-3a21-aa9f-2755a5229a22 | -19.6045 | -46.26548 | 2024-10-05 03:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| efef030b-e224-3535-bf36-0064cffd4dd1 | -19.6002 | -46.26468 | 2024-10-05 03:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0bd8a19-0a06-339d-b16b-ec8130e5b660 | -21.07873 | -45.72602 | 2024-10-05 03:51:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3af00203-69ce-3b9a-9ec4-07de40cc94d8 | -21.078 | -45.72983 | 2024-10-05 03:51:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 319d2810-0fe3-37cb-b01e-6df1d0ecfa80 | -20.79355 | -47.74828 | 2024-10-05 03:53:00 | NOAA-21 | NUPORANGA | SÃO PAULO | Brasil | 3533601 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 93326e98-79e2-3c48-ba51-51b2b9fa20db | -20.79144 | -47.75854 | 2024-10-05 03:53:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| efd4233a-4638-31be-ab6e-7b33598c0de0 | -20.78858 | -47.7545 | 2024-10-05 03:53:00 | NOAA-21 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6feb799-c31b-3a7f-ad24-0e59cd6b412b | -22.37257 | -47.93948 | 2024-10-05 03:53:00 | NOAA-21 | ITIRAPINA | SÃO PAULO | Brasil | 3523602 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa906290-4ae0-345d-93a1-3d490624b9e4 | -21.92678 | -47.56305 | 2024-10-05 03:53:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d22d8ac-b2b7-3880-8aa5-5e7a8e3cfebf | -21.89625 | -48.47408 | 2024-10-05 03:53:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9079c2c6-4fb1-37e4-b040-915cade6d30d | -21.85076 | -48.42738 | 2024-10-05 03:53:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba159ac7-a9fb-3e8e-8b61-7b9b9625cb8d | -21.84662 | -48.42854 | 2024-10-05 03:53:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1e785616-f7a2-3bf7-9ed3-815efe5e1237 | -21.84607 | -48.42628 | 2024-10-05 03:53:00 | NOAA-21 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85d68e2e-9fbc-3c40-ad45-f70bf73eaa65 | -21.78015 | -47.04391 | 2024-10-05 03:53:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c65fcea-c643-3496-93a2-e1ffe4f7e5a3 | -21.77926 | -47.04844 | 2024-10-05 03:53:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| abd7dee7-91c6-377d-baf2-00d04f3fbe14 | -21.77585 | -47.04285 | 2024-10-05 03:53:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8ef46c0e-fe10-3135-86ac-229ed148fbb8 | -21.77496 | -47.04738 | 2024-10-05 03:53:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9f05a17b-1f40-37fa-8f4a-2e0c81897aea | -21.77154 | -47.04187 | 2024-10-05 03:53:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 9.3 |
| ec76e3fe-c5c6-3c35-a4e8-9a9df54aa3e1 | -21.28704 | -47.39708 | 2024-10-05 03:53:00 | NOAA-21 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cff44c10-dd48-3c41-b9ef-032ea44c5381 | -21.27903 | -47.40258 | 2024-10-05 03:53:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7b2ffa6-8853-3489-91fc-7c2de255e7f5 | -21.27802 | -47.40752 | 2024-10-05 03:53:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 510bf4a4-b342-3582-adc9-14ca808cee62 | -21.27626 | -47.40455 | 2024-10-05 03:53:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 71fbd4ae-6b42-33f2-a251-954926c4af13 | -22.83668 | -48.41288 | 2024-10-05 03:53:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b734bab-38e6-39ec-9442-9ac7ce7384e0 | -20.93325 | -49.01826 | 2024-10-05 03:53:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 49f32675-ec94-352f-b9e3-149eb1c80444 | -20.9326 | -49.02136 | 2024-10-05 03:53:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 96cab4b4-4bf3-3ae0-8c64-c4c060dfb562 | -20.9296 | -49.01087 | 2024-10-05 03:53:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8da9dc5a-a77c-30c6-945c-8a0818c69515 | -20.92895 | -49.01395 | 2024-10-05 03:53:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e7e1ba39-4b66-3989-889d-ea56d7f47f7b | -20.9283 | -49.01706 | 2024-10-05 03:53:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| d7cc1cb0-02de-3dea-b513-932456318c4a | -20.92765 | -49.02017 | 2024-10-05 03:53:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 942ad3f9-ea9a-3a17-b9e9-b755b36471e3 | -20.924 | -49.01271 | 2024-10-05 03:53:00 | NOAA-21 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0007f2ff-f6ae-315f-a6c3-60af373fe5f6 | -22.38668 | -49.26619 | 2024-10-05 03:53:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1dad3c50-f9a0-3628-8356-775bc82c0cfa | -22.38546 | -49.27189 | 2024-10-05 03:53:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 60eb3802-3929-39fc-94a7-7b1fa738d784 | -21.8096 | -48.74502 | 2024-10-05 03:53:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6ac43658-ee93-33dd-9b9c-ffcccb9eb27b | -21.80841 | -48.75066 | 2024-10-05 03:53:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 16a3659d-8756-3e68-b582-676923b89474 | -21.80482 | -48.74382 | 2024-10-05 03:53:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 450de9bd-8c3b-321f-bea1-5b226b2150bb | -21.49782 | -49.73823 | 2024-10-05 03:53:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5f2678e8-bb0d-3f9b-9efa-83f61629aaaa | -21.49712 | -49.74142 | 2024-10-05 03:53:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c90e83e1-349c-3747-b96f-46610d3a5784 | -21.33106 | -48.88845 | 2024-10-05 03:53:00 | NOAA-21 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb873c44-e1f3-3687-8c02-b22b6a87af49 | -21.13995 | -48.45197 | 2024-10-05 03:53:00 | NOAA-21 | TAIÚVA | SÃO PAULO | Brasil | 3553203 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9d4fd640-59c1-34b3-9bb6-48621d8dd001 | -20.94548 | -49.53812 | 2024-10-05 03:53:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 611c3b37-eca9-30fa-9b42-d39ef2297a8b | -22.54182 | -48.81483 | 2024-10-05 03:53:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5ba4cdd-2623-30d8-a812-097dd5d65f51 | -21.9036 | -50.72064 | 2024-10-05 03:53:00 | NOAA-21 | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fd250d7c-c030-3765-b3a5-99748e22aad4 | -21.89827 | -50.71905 | 2024-10-05 03:53:00 | NOAA-21 | BASTOS | SÃO PAULO | Brasil | 3505807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a540937f-947d-31f6-8123-e4d78d5ccb41 | -20.57621 | -51.39546 | 2024-10-05 03:53:00 | NOAA-21 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f11deebc-dd80-3f30-8f5b-2015f2d3d2a4 | -20.57521 | -51.39983 | 2024-10-05 03:53:00 | NOAA-21 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| d705e7e4-6bba-389b-bba4-6d4ae9a1554c | -22.77356 | -53.37009 | 2024-10-05 03:53:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2aa08dfc-6f82-30b5-94ba-304a7a63006d | -22.76868 | -53.36311 | 2024-10-05 03:53:00 | NOAA-21 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bae2a127-e16a-3576-9094-fd5ce00413af | -21.65765 | -54.82667 | 2024-10-05 03:53:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5257a5f0-3fbf-3e90-aa3a-a97ef887bfc5 | -21.65752 | -54.82718 | 2024-10-05 03:53:00 | NOAA-21 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README53.md)
