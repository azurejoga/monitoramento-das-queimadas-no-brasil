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
| 533f74bc-101e-37ad-8928-109b6743dffa | -20.23347 | -41.25325 | 2025-09-12 03:40:00 | NOAA-21 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| f42b9037-d9a6-3671-876f-f3379e32c25d | -20.66707 | -44.25619 | 2025-09-12 03:40:00 | NOAA-21 | DESTERRO DE ENTRE RIOS | MINAS GERAIS | Brasil | 3121407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 66c7429d-cd77-3bf2-9eba-6ada90045bec | -20.01197 | -46.92098 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 562887f9-4e5b-3c2f-b7df-af62e0bc7a0b | -18.67817 | -47.67006 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7bacd82-3ec5-3b7a-8d9c-737fb3950508 | -20.20654 | -44.55506 | 2025-09-12 03:40:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 766bfa54-92e0-3b52-b898-9c9e471d9759 | -20.35415 | -49.95505 | 2025-09-12 03:40:00 | NOAA-21 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07ed97b8-6975-332d-b97f-99e432613748 | -18.6597 | -47.67158 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 912cd981-589a-3526-b041-d6e7cff49fa3 | -18.65795 | -47.65226 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 536afa32-c899-342f-89a4-61d338c60c0b | -21.94586 | -47.55743 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4845e80c-5ee4-3e54-8b88-82ae9fc8b864 | -20.0027 | -46.92324 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 94b0cc68-5d2f-3966-977a-86a3ecb3c7d2 | -17.50238 | -44.32508 | 2025-09-12 03:40:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 104e40cb-5ab8-3388-a2da-5f2b906fd954 | -19.74204 | -45.94734 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22a73326-50c3-3fc2-82ac-36a396aa33f2 | -18.77116 | -48.54516 | 2025-09-12 03:40:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d4401ed9-7b70-3b13-8145-4b0da5a14449 | -18.77195 | -48.53817 | 2025-09-12 03:40:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c2577839-ef9a-3c84-99b7-fe21505a3bf1 | -19.93346 | -43.87471 | 2025-09-12 03:40:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 8490fdc1-80ab-3038-8668-2d29296c2f75 | -21.32326 | -45.00298 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 7802240b-1ae0-31ac-89b1-2ffe3f61e189 | -21.94133 | -47.55249 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8e187e9-d3e7-35a4-ae71-203afcad71ea | -21.96887 | -47.55548 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| edd60fd2-7e62-31c4-91ed-71fe88d766c2 | -20.57322 | -44.36498 | 2025-09-12 03:40:00 | NOAA-21 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4653b66e-cfe2-383a-b552-372f560307f6 | -20.00325 | -47.64973 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2330931e-9371-3fa8-9ff9-72f660ceac5e | -18.59629 | -47.18303 | 2025-09-12 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea94db0d-016d-356e-9ac6-5a16ed91bbf6 | -21.19083 | -47.52933 | 2025-09-12 03:40:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 91f826b3-7fcd-3fc3-9e93-ce5b6bb96920 | -21.96967 | -47.5519 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d12a3069-2d44-30b6-983d-ffca79c24b37 | -20.00783 | -47.65563 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5d0c5410-b0fd-319a-b7eb-5ab8e3ce8659 | -22.15102 | -45.83067 | 2025-09-12 03:40:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 943f66f9-d20e-374c-aa61-416b8f98041f | -20.01073 | -47.64251 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1bc116e8-ec4a-3d2e-a1a7-28a368d7e99f | -16.43413 | -45.68552 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2b3af45-16f5-3310-8d71-84f6f3878f4e | -19.15034 | -47.69631 | 2025-09-12 03:40:00 | NOAA-21 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7346e018-d81d-3fec-b7d7-1a71f861ba9e | -23.11936 | -47.50638 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 3bb495bf-572b-35d5-849a-fe76193cf1f2 | -22.18416 | -49.73721 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| f14382f4-28ae-34e6-b3fd-431dbe87ecad | -18.05342 | -45.44022 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2198ef01-668c-3931-b767-55c93523f323 | -21.84398 | -46.51159 | 2025-09-12 03:40:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 83bb07f7-422c-3dc7-a12b-0534bdf7a840 | -23.12014 | -47.50289 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 59086afe-f4a3-3746-963f-5d5cb9e17641 | -17.352 | -46.69985 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74cef0e1-7b03-3a81-bdb2-8982fd4c81d2 | -16.28602 | -45.68689 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 24688969-6619-306c-9a27-1d59d9a23162 | -21.33753 | -45.02797 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1ca7414c-cb81-3a92-878e-eba59a8462cf | -22.17689 | -49.74084 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| d6bae6ef-91f6-3c03-9607-fc7e556abea1 | -19.99743 | -47.6494 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91e227fe-f545-3d3e-b9b6-c76ea02195cb | -17.35286 | -46.69583 | 2025-09-12 03:40:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23425d93-690d-36d8-8983-24011df0e7ff | -18.61689 | -48.25558 | 2025-09-12 03:40:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6ecda1b2-ccae-3eac-a914-78b3b091995e | -23.43402 | -47.02263 | 2025-09-12 03:40:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 8d627870-6d7a-39ba-a2bc-6b503e2c230b | -18.05477 | -45.43372 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86609819-25fe-3ae2-a491-47c71b6d8547 | -21.33853 | -45.02306 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a8d32e8a-449b-3708-9d0e-f8590ec4009d | -17.72286 | -46.13743 | 2025-09-12 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f145ef3-b133-3ebd-ba56-c80ed9619ad1 | -21.95533 | -47.55598 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4812c759-4b95-3f50-8ea8-ab2539f2325a | -18.0541 | -45.43698 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9934f91d-b69d-3c46-81ba-612a7b3b5eb4 | -22.22322 | -49.60427 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| c83f50f0-99ad-3025-8bb0-18fcae8dfd24 | -22.81652 | -46.42793 | 2025-09-12 03:40:00 | NOAA-21 | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 872b73b2-7c6d-3226-bc7c-6c03e6a4f738 | -20.35606 | -48.40148 | 2025-09-12 03:40:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c13d640-0528-3c59-be71-a75cb860881b | -19.98404 | -44.86415 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO PARÁ | MINAS GERAIS | Brasil | 3161809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5171d87-1222-34db-bf49-95eb640fc95a | -20.70288 | -46.07892 | 2025-09-12 03:40:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| da375541-13ab-38ed-865e-0110d4b41191 | -21.42998 | -45.47252 | 2025-09-12 03:40:00 | NOAA-21 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| c7e91a9a-5906-3d12-9a7e-0e040effe555 | -23.1477 | -48.25546 | 2025-09-12 03:40:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5e87fca8-3420-3353-a484-91ea37085172 | -21.84558 | -46.51126 | 2025-09-12 03:40:00 | NOAA-21 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0433dcd2-af9d-3722-8bd1-f72b69c325c3 | -16.42058 | -45.6976 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee9459d5-7143-3c18-a433-5bdbae486efa | -21.95229 | -47.54408 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ab8ba849-f1c5-327b-bc75-f163c1533462 | -16.42277 | -45.68681 | 2025-09-12 03:40:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c380286e-7869-3e43-a9e4-e07f2f6b124c | -16.44253 | -49.04398 | 2025-09-12 03:40:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 924d9698-4ca5-37b5-a905-0223605b6f65 | -23.11135 | -47.49296 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| fee94085-5ff4-3472-af4b-46a39713f76c | -21.62797 | -46.79401 | 2025-09-12 03:40:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1e3164ec-ef79-384b-98dc-2d7e3da99cf8 | -21.32353 | -45.02524 | 2025-09-12 03:40:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 8ec8eccb-948e-3b50-8ac2-e9dc44ecdf9c | -20.57353 | -43.74749 | 2025-09-12 03:40:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9922db9e-cfa1-3101-920f-4caf6f69b4e4 | -18.66175 | -47.66238 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 78425996-d6d6-3a9f-bde4-59554790597c | -20.36137 | -46.66087 | 2025-09-12 03:40:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94245924-fde0-30f9-88aa-958672b66066 | -22.52015 | -44.70945 | 2025-09-12 03:40:00 | NOAA-21 | QUELUZ | SÃO PAULO | Brasil | 3541901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d5542466-54ca-3606-b041-7c27e7551726 | -20.39765 | -42.1954 | 2025-09-12 03:40:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a1dc8d7d-51b5-3470-9dd0-040a6e612c38 | -17.13292 | -48.49529 | 2025-09-12 03:40:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 434713db-e0af-34d3-a4fd-b69954807b57 | -21.6486 | -46.409 | 2025-09-12 03:40:00 | NOAA-21 | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 0c555a01-d36a-34e8-bcac-e103dddd843c | -20.01541 | -47.64798 | 2025-09-12 03:40:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f1df23ba-fd68-3f5c-ba3e-d3ccba757c33 | -22.60961 | -47.28556 | 2025-09-12 03:40:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be636f33-4bdc-36cc-8a2f-360594d00194 | -23.14847 | -48.25206 | 2025-09-12 03:40:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f3d73ecb-f4d7-35a6-882b-46f7f69435c7 | -18.65759 | -47.65307 | 2025-09-12 03:40:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2d6660e3-5b02-377e-b6f5-148453aa2311 | -23.12849 | -47.48991 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 82963cb2-82c2-3a96-affe-8126cece47a1 | -21.2931 | -45.94914 | 2025-09-12 03:40:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| ec8820b2-d963-398f-83fa-9acaabaca3dc | -22.69914 | -48.70075 | 2025-09-12 03:40:00 | NOAA-21 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| b9994076-683e-35dc-932a-944a2317c75b | -21.9574 | -47.55632 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de378347-f3e0-3da7-9a20-70a3ad6a80ba | -20.69777 | -46.07824 | 2025-09-12 03:40:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bba4b5de-2abb-30f4-b557-0aae922526ad | -22.52208 | -45.09928 | 2025-09-12 03:40:00 | NOAA-21 | CRUZEIRO | SÃO PAULO | Brasil | 3513405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e1e2d2cb-a983-3e9b-a1a5-f54ecc05c5d2 | -21.94998 | -47.55468 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 65f055b2-d17b-37bc-8feb-ec5a19103077 | -22.78788 | -47.80955 | 2025-09-12 03:40:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ac448866-d293-3a18-8d3f-6bdedcefa210 | -22.23046 | -49.60062 | 2025-09-12 03:40:00 | NOAA-21 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4ccbdd27-5c06-3030-bbf2-f3d3d9a877a0 | -18.05275 | -45.44345 | 2025-09-12 03:40:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99ad0f55-53e3-3fb6-8841-238845d72301 | -23.09741 | -46.67469 | 2025-09-12 03:40:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 43e3c4f5-de58-35dd-ac97-ff39312c4f69 | -18.44838 | -47.1732 | 2025-09-12 03:40:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a516ae02-cedb-3bb1-8eb5-d4abc3f92428 | -21.94836 | -47.5621 | 2025-09-12 03:40:00 | NOAA-21 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 58ad8375-086e-3183-8003-5d0ce56ba067 | -22.70115 | -48.6921 | 2025-09-12 03:40:00 | NOAA-21 | LENÇÓIS PAULISTA | SÃO PAULO | Brasil | 3526803 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| da0fc745-e54b-3488-893d-db19d9054194 | -18.62573 | -44.26481 | 2025-09-12 03:40:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fbdd56e7-a7a1-3820-897e-66d67fe1e133 | -18.76309 | -48.1989 | 2025-09-12 03:40:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 142a4044-9e37-37dc-8a38-2243e8e8ab32 | -17.27472 | -46.08936 | 2025-09-12 03:40:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71276def-abe7-31c3-a379-eda9ec0fd524 | -19.74979 | -46.08979 | 2025-09-12 03:40:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef063922-3f70-3f53-8585-3afda4db559e | -22.68791 | -45.52136 | 2025-09-12 03:40:00 | NOAA-21 | CAMPOS DO JORDÃO | SÃO PAULO | Brasil | 3509700 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ddf78ed5-c45b-32d4-99b1-d79c93dd3b6e | -23.32415 | -47.32576 | 2025-09-12 03:40:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6c02507c-86c9-30a2-a542-23a77147065b | -20.01122 | -46.92456 | 2025-09-12 03:40:00 | NOAA-21 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f54bbb79-7101-325f-a09d-550bcac36357 | -20.98433 | -46.98522 | 2025-09-12 03:40:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd23fa53-1cce-3375-ab31-fd7520b12a40 | -22.39815 | -46.74899 | 2025-09-12 03:40:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 4858e82a-58a2-3e97-b41a-8d3e9947b028 | -23.14689 | -48.259 | 2025-09-12 03:40:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 52e3b877-8a9d-35c2-9fb9-a65489bf93e4 | -23.42827 | -47.02469 | 2025-09-12 03:40:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 30ad74f7-4986-3f1c-ad3e-b0bcf511e31a | -16.65776 | -47.62671 | 2025-09-12 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecd96b0b-f3bb-35a0-ab27-424b5888568e | -23.14927 | -47.47025 | 2025-09-12 03:40:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6225ff03-c755-384b-8b74-9b6c3a62f30e | -17.54675 | -44.54323 | 2025-09-12 03:40:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README25.md)
