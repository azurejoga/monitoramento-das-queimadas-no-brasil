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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a97c1566-6b9e-3d76-9260-f59304e8229b | -22.58792 | -46.77813 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 20b6fac2-2f74-39a2-a16d-b4fa21f93f7e | -18.49702 | -44.03792 | 2025-10-01 04:23:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ff0c9ee-c748-3359-9483-16b3e661d3be | -20.61086 | -46.06968 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d41811b6-1000-3c35-83ec-4af814a360d2 | -17.96946 | -45.01652 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 26dc4ca4-7f62-3a7c-a696-400033c78c84 | -22.11221 | -44.68942 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 102728b7-8959-32a3-89c5-af07d48c7055 | -22.26591 | -46.73055 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7f6368d7-4bc7-3f9e-8e05-88f9ee2605ae | -19.88593 | -42.62803 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 36913a14-79e7-326a-97f6-7dcd6e56edfa | -23.40175 | -47.05154 | 2025-10-01 04:23:00 | NOAA-21 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| eda122fd-6c38-3890-ac28-361b8bb075de | -21.0199 | -45.18133 | 2025-10-01 04:23:00 | NOAA-21 | CANA VERDE | MINAS GERAIS | Brasil | 3111903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| ad546b1e-a831-34e0-b9bb-3e0ed495c6a1 | -20.13046 | -46.33582 | 2025-10-01 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4b86fc0e-945e-37c6-b832-36ce884ffe7d | -20.48389 | -43.95009 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 00a5f1d8-417d-3ca3-a037-91d559b3baf2 | -23.04891 | -46.66145 | 2025-10-01 04:23:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7f9ccdd1-16fc-3d03-b1f7-008854f4f1ff | -18.49278 | -44.0416 | 2025-10-01 04:23:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a2ea9ec-1fd9-34c7-8c70-311f1336b724 | -18.31193 | -44.02948 | 2025-10-01 04:23:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1bb15591-9fcd-3cdc-9c7f-0985421c7bdf | -20.48824 | -43.94605 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4f83ff94-0ed2-3b33-a517-983ecad299c1 | -21.34768 | -44.88956 | 2025-10-01 04:23:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e732e0d4-4459-3b95-bbfd-a096da732cfd | -18.86113 | -41.98629 | 2025-10-01 04:23:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da08fbff-baed-3976-ac29-7e7dbbf099e3 | -19.463 | -44.28633 | 2025-10-01 04:23:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee34f6c2-fefd-3b46-a86e-349d4960f36d | -22.57971 | -46.78182 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| e68dfc84-a202-399d-8f6d-6dfed412eb7f | -17.8553 | -46.15376 | 2025-10-01 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b0ee25f-4cfe-308e-a76c-13399ce07572 | -20.2343 | -43.87789 | 2025-10-01 04:23:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 60bfb5e9-cf97-3073-a681-4f87a08d5f99 | -20.63348 | -46.18097 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79c8f111-83f1-312b-afcd-86be32ac9c07 | -21.04477 | -45.67595 | 2025-10-01 04:23:00 | NOAA-21 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 169a9577-6990-3a2f-87cb-864500af461f | -22.40765 | -43.16875 | 2025-10-01 04:23:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 997f4395-76e5-3bf7-9242-35ee1579dce3 | -22.27151 | -46.71583 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f2e74e0f-265a-380e-a230-db5cc4f1ef61 | -19.96564 | -43.72133 | 2025-10-01 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aabd55b5-45a4-3776-9d2a-d7b274a2ccbf | -20.00506 | -47.0358 | 2025-10-01 04:23:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1b10fe7-53d6-32f6-8199-ce094f63ef5d | -18.48608 | -44.03625 | 2025-10-01 04:23:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e0e6087-f37b-393c-a7be-6d5322acce45 | -20.17007 | -47.53498 | 2025-10-01 04:23:00 | NOAA-21 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 843f7030-9523-3a97-95f5-5193afd63c62 | -19.86961 | -42.59534 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 90ce6d93-e942-3ff3-b27b-4c6cb7d69805 | -18.33865 | -44.18625 | 2025-10-01 04:23:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a028c52-5064-33ea-af06-989909e948f5 | -21.48807 | -46.92537 | 2025-10-01 04:23:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0cacd5f0-6760-3acf-8784-63583262301a | -20.98458 | -45.46066 | 2025-10-01 04:23:00 | NOAA-21 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d295d82-6b49-3f31-bfaa-e566eaa651d1 | -17.84638 | -46.16747 | 2025-10-01 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7e305a2f-ab36-3565-8ae1-7cbd838c614b | -23.55546 | -48.46841 | 2025-10-01 04:23:00 | NOAA-21 | CAMPINA DO MONTE ALEGRE | SÃO PAULO | Brasil | 3509452 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ff724aec-0a7a-3e96-a835-a153d9d26c9b | -22.27719 | -46.72458 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a3c83a5a-3e20-32d1-9705-33445d2fb26a | -20.62213 | -46.18725 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2caedff6-c506-3cc1-8728-370a65cb1cf0 | -22.26227 | -43.43374 | 2025-10-01 04:23:00 | NOAA-21 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| da16a740-5afc-3f42-ac53-81abc3e0d820 | -21.42652 | -44.16752 | 2025-10-01 04:23:00 | NOAA-21 | PIEDADE DO RIO GRANDE | MINAS GERAIS | Brasil | 3150307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 77e4f8f8-3aec-3220-b126-cb1e203d7710 | -20.62556 | -46.21181 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 13c5454e-20c0-3ea6-8460-6763cc611116 | -17.7344 | -46.63747 | 2025-10-01 04:23:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71ae3635-abf5-3928-b2f4-e78b2f0a0c21 | -19.81263 | -44.06969 | 2025-10-01 04:23:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d1ee8e84-b3ee-3a9b-820d-da7e33f03b52 | -20.12312 | -46.33863 | 2025-10-01 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f058e64e-5d98-319b-94d3-9eccb9cbf654 | -20.81513 | -43.073 | 2025-10-01 04:23:00 | NOAA-21 | PAULA CÂNDIDO | MINAS GERAIS | Brasil | 3148301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4dfb172a-73d1-3416-944d-bed52e1c84b1 | -22.44397 | -48.3106 | 2025-10-01 04:23:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e58cb0a9-f45c-3da0-9ba2-3e2da34e6e26 | -22.9271 | -45.5088 | 2025-10-01 04:23:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 533f0f1a-8eea-3f68-92fd-bd6e0d19af59 | -22.07526 | -48.45104 | 2025-10-01 04:23:00 | NOAA-21 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37495c38-9317-334d-a51a-85ef559ab90b | -22.76621 | -45.78675 | 2025-10-01 04:23:00 | NOAA-21 | SAPUCAÍ-MIRIM | MINAS GERAIS | Brasil | 3165404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 13ce8c2e-c2df-3401-b3df-0325875538c0 | -18.80709 | -47.55298 | 2025-10-01 04:23:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ae3cbd0-4adb-314e-ae0e-967cf1ea9e95 | -22.10377 | -47.80423 | 2025-10-01 04:23:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04cec6dd-fdf4-3be0-8144-128366abe3b5 | -18.96049 | -43.70386 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fd8a7331-078e-381a-81d4-f99386cf7e77 | -22.10235 | -45.31495 | 2025-10-01 04:23:00 | NOAA-21 | OLÍMPIO NORONHA | MINAS GERAIS | Brasil | 3145505 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a32a5136-de72-3ba6-ac93-2abf3edb879d | -21.19456 | -49.29839 | 2025-10-01 04:23:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0ee2fb12-8aba-3dbe-94e3-f50ed0bcc54d | -20.61708 | -46.22231 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3d9e5ef-abf0-3956-a073-0d22e94ad3ff | -19.86248 | -42.58678 | 2025-10-01 04:23:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 6e3bf780-dd3c-3745-85a7-47246ecd5cc8 | -18.96822 | -47.8709 | 2025-10-01 04:23:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63cc886c-e922-3886-b5e1-ca5aa07973e4 | -20.79728 | -43.5236 | 2025-10-01 04:23:00 | NOAA-21 | RIO ESPERA | MINAS GERAIS | Brasil | 3155207 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5dcb6301-f9dc-3eda-a8a2-e82befce6544 | -22.77873 | -47.61139 | 2025-10-01 04:23:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b3dbd898-3b35-3f29-972d-fb8fd8bc6a44 | -20.1114 | -44.37543 | 2025-10-01 04:23:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| cb225f06-31b8-37ef-83e7-ea7219abc442 | -21.34489 | -45.87915 | 2025-10-01 04:23:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a40990e0-ef42-3cf1-9761-9bb7f368f6c3 | -19.71107 | -44.05826 | 2025-10-01 04:23:00 | NOAA-21 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 545e6f2f-5acb-3fa6-ab73-bd8019697688 | -22.40813 | -43.16492 | 2025-10-01 04:23:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 03840ce8-4590-31f8-8f17-d2acbd2f2ba0 | -17.21651 | -49.61768 | 2025-10-01 04:23:00 | NOAA-21 | VARJÃO | GOIÁS | Brasil | 5221908 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32545018-139c-39ef-9a9b-b31c259b980e | -20.12901 | -44.02785 | 2025-10-01 04:23:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 184a8bf2-503f-35a4-bbbd-2247aea90751 | -19.93173 | -43.88736 | 2025-10-01 04:23:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| da2002af-1ea1-3b54-9536-af3dcfad5031 | -21.88772 | -48.14853 | 2025-10-01 04:23:00 | NOAA-21 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e91fa538-894e-3ed3-bdc2-e178db930227 | -19.21748 | -50.68777 | 2025-10-01 04:23:00 | NOAA-21 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e04c9dac-3ecd-38a8-b32f-75d955e9b79f | -23.6874 | -46.86974 | 2025-10-01 04:23:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c60fc154-76ec-3f79-966a-77b3b60df126 | -20.23804 | -43.87861 | 2025-10-01 04:23:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a89672b8-9cc1-3a03-b950-c07f5a1a5bb7 | -17.9718 | -45.02497 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d87d128f-d4cc-3ccd-ad04-7063859833e4 | -22.11239 | -44.69229 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c8309fc4-c9ba-327c-bd5a-cd41152e4b51 | -22.27379 | -46.72403 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 1f312db2-5087-34ed-950b-7cf678cfd822 | -22.65292 | -46.76138 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 8f88838a-b6c5-39d9-a168-259995844abe | -23.20207 | -45.10128 | 2025-10-01 04:23:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 89a6e441-d4c8-3f37-b847-efb1d4026793 | -18.70232 | -44.33032 | 2025-10-01 04:23:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65c2fe0e-9336-319e-b312-89cd05738de3 | -20.48886 | -43.94125 | 2025-10-01 04:23:00 | NOAA-21 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b2e5a406-1091-33fe-b78b-d00ddccd9dbc | -17.87108 | -47.14251 | 2025-10-01 04:23:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 517ad52c-ef79-388f-91c4-b76c4ed9b398 | -20.44118 | -43.59288 | 2025-10-01 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c2fda0f9-ffb7-33f1-8812-434dfe3cd826 | -20.62103 | -46.21907 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd567caa-32ae-3c7d-b429-c158774e39d3 | -22.64333 | -46.75557 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c418beb8-cfb3-3732-89fb-01174962fc61 | -20.0337 | -44.53484 | 2025-10-01 04:23:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 22ad44f8-f15b-372b-a717-3050ceda4ced | -20.22458 | -43.44553 | 2025-10-01 04:23:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 50340982-e9c4-3ae9-a946-0d3f9a71fd7a | -20.84785 | -49.44075 | 2025-10-01 04:23:00 | NOAA-21 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b2841b04-7e47-35ab-a118-9baa7ffda2ce | -20.42468 | -46.17231 | 2025-10-01 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d3220cf-dc2f-31f7-9277-9bf685a3b1fe | -20.33161 | -43.04018 | 2025-10-01 04:23:00 | NOAA-21 | BARRA LONGA | MINAS GERAIS | Brasil | 3105707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 4ba8bd3c-aa40-3f01-848b-460278b8f5ae | -19.86515 | -43.8135 | 2025-10-01 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 6cc2707d-a207-3889-8f3f-ffd193760a24 | -20.60687 | -46.07301 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 3263ad5d-ce5d-3415-b62c-eb3110151cda | -22.28114 | -46.72125 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ee18ad71-fd74-3998-b62f-9860479937d6 | -23.36482 | -47.16172 | 2025-10-01 04:23:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 19df1822-ee5b-3c97-acbf-facc9b218564 | -19.86395 | -43.8226 | 2025-10-01 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 103899d5-c651-3db6-8b50-2ddde8b11503 | -17.96309 | -45.01142 | 2025-10-01 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6f89051-c30e-3f68-b44f-e180523d0ea5 | -23.36202 | -47.15719 | 2025-10-01 04:23:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7784f3d8-c2a9-3682-9552-f5e40fa58183 | -23.3279 | -46.86497 | 2025-10-01 04:23:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 3291ee5f-7049-3f89-90d9-0c34a7fdeef5 | -22.58114 | -46.777 | 2025-10-01 04:23:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| 680b7000-874f-3cc4-ac24-d09137488588 | -20.63861 | -46.21782 | 2025-10-01 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d67540a8-232d-3bcb-988f-d67d1d1af141 | -22.33833 | -48.98269 | 2025-10-01 04:23:00 | NOAA-21 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a130464c-bf4d-39ef-b35b-63c714583bb6 | -19.9342 | -43.8973 | 2025-10-01 04:23:00 | NOAA-21 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 6e724704-5c3e-3778-9206-a7020c7effd7 | -22.27774 | -46.72074 | 2025-10-01 04:23:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4477ced8-1b3d-3ef3-bfa5-44786aa17e18 | -20.11812 | -51.8088 | 2025-10-01 04:23:00 | NOAA-21 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba7348e2-c8eb-3b0e-8e77-a2bd4cbeada1 | -22.11587 | -44.69012 | 2025-10-01 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |


[Clique aqui para ver as próximas entradas](README77.md)
