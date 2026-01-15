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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| af522501-980e-3d65-bbcc-a74ddbe8f48d | -7.2411 | -43.0428 | 2026-01-15 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| eb31bda1-f904-3a92-85b8-98ecc59ab337 | 4.0578 | -61.4661 | 2026-01-15 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 55.1 |
| f35a9906-65ae-3201-b9fc-44395b3e025c | -4.372 | -37.8918 | 2026-01-15 00:00:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 78.1 |
| 957a9751-a706-3dc7-8c45-8f3a7672326a | -19.37386 | -40.86124 | 2026-01-15 00:07:00 | TERRA_M-M | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| cdbec4fd-b65b-36ed-9616-a44430c9f934 | -19.37539 | -40.87134 | 2026-01-15 00:07:00 | TERRA_M-M | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| f707fb9b-b92c-3b1a-a6af-4053fd9576a0 | -22.17926 | -43.1384 | 2026-01-15 00:07:00 | TERRA_M-M | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 13b2a4a2-f8ef-3638-b127-f2fc518c9ef5 | -12.08448 | -43.76684 | 2026-01-15 00:09:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f2233ad7-7830-3207-852c-c446dc939373 | -14.41038 | -44.58569 | 2026-01-15 00:09:00 | TERRA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ffe0bf2e-701a-3775-830b-edf89b23f054 | -7.23209 | -43.05087 | 2026-01-15 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.8 |
| a45049b8-87f5-3e55-9b73-115b805ca226 | -7.60929 | -47.06639 | 2026-01-15 00:09:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 441a1a13-5b5e-35b7-9aa6-32348157721b | -10.76533 | -45.01387 | 2026-01-15 00:09:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 852d476a-727f-3228-8e72-6fd80e19afd8 | -13.74006 | -43.66278 | 2026-01-15 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9e5258fa-1107-3a0b-9aca-81a89b878b72 | -11.6615 | -43.77023 | 2026-01-15 00:09:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a7105c24-208d-389e-ac2b-efbd7eb23ca4 | -7.86012 | -39.0923 | 2026-01-15 00:09:00 | TERRA_M-M | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 389bdbef-751b-316a-8a24-8ecb198a58cb | -7.25285 | -43.05866 | 2026-01-15 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 2a921ee7-27be-3706-89b6-049e80e6b15a | -7.24324 | -43.06009 | 2026-01-15 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 560b7110-9570-3b8a-9271-3af4c56fd2c5 | -7.98982 | -43.38643 | 2026-01-15 00:09:00 | TERRA_M-M | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 78eed1d0-aa7c-3a3f-855b-f6b49b19b7fe | -9.96382 | -36.36515 | 2026-01-15 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.7 |
| 64c549fa-96d4-33b6-9ec1-7fa96cdd94b9 | -8.43272 | -44.02438 | 2026-01-15 00:09:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| c2f38b98-ba5c-3ec5-a5b8-4247b4d0e949 | -8.42368 | -44.02576 | 2026-01-15 00:09:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 55b9ec6f-1d8a-3d72-ad56-d8134c02058d | -8.15437 | -43.18389 | 2026-01-15 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 2d4d6064-15c1-36e8-83db-fd3dafe457cc | -8.42235 | -44.0163 | 2026-01-15 00:09:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ae6263c-0589-34f4-9b6d-5bc31301026d | -13.60385 | -43.55538 | 2026-01-15 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 639131eb-5917-34c3-b4c3-4a1addb36843 | -10.76656 | -45.02277 | 2026-01-15 00:09:00 | TERRA_M-M | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 7446e769-752a-38d8-960d-651004f8d8ce | -7.86319 | -39.11224 | 2026-01-15 00:09:00 | TERRA_M-M | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 3bcdeb38-43da-380d-a490-2f1d29b97fa3 | -12.50621 | -43.68229 | 2026-01-15 00:09:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 2efba296-53a2-34df-aea7-1e9b50423457 | -15.37339 | -43.68319 | 2026-01-15 00:09:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 3fdb5dac-03d4-360a-bd39-e2ca5dc126f2 | -12.08778 | -45.58128 | 2026-01-15 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 017e63c8-6a2f-3fed-8ecc-fdfa452085c9 | -7.23364 | -43.06153 | 2026-01-15 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.5 |
| fbc280dd-5df1-3cff-a03e-3e60838e2d24 | -12.51511 | -43.68094 | 2026-01-15 00:09:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 71da72c2-0244-3943-991a-b210c51bb4d6 | -10.4858 | -44.92768 | 2026-01-15 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d889f0e4-8665-3890-895e-313ad9a461cf | -14.76599 | -45.92582 | 2026-01-15 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| e698470c-5cce-3572-be64-4fad2e3b0b83 | -12.08655 | -45.57215 | 2026-01-15 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 339ef53a-a84b-3c39-b537-4cc24bb7a5e3 | -7.25132 | -43.04803 | 2026-01-15 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 23e214a9-8921-3763-b420-7ececf78cc47 | -12.61994 | -46.12106 | 2026-01-15 00:09:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 89376482-a52d-3bf3-91ba-dc53fd484cdd | -7.68908 | -43.72729 | 2026-01-15 00:09:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 7f8e3be9-a4d5-306c-b574-f7176cdedc89 | -7.60803 | -47.05705 | 2026-01-15 00:09:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 97d17c76-daa7-304b-83ad-5d5b1cfa8c81 | -10.59279 | -44.9694 | 2026-01-15 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 18bf9e40-07c4-3d72-a8cc-9f9ab0561e0b | -6.88247 | -42.83902 | 2026-01-15 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| e5a2bbdd-d168-3071-a632-e4406cb2aa5b | -10.49902 | -44.74675 | 2026-01-15 00:09:00 | TERRA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bec4d7bf-ba15-32e9-a435-9a48df110441 | -10.34379 | -44.82703 | 2026-01-15 00:09:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| beaf3858-aaf5-3778-947b-de1dcbdf566c | -14.40156 | -44.587 | 2026-01-15 00:09:00 | TERRA_M-M | MONTALVÂNIA | MINAS GERAIS | Brasil | 3142700 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2906abd0-eef5-381d-806a-7342cbfd5c6f | -8.40055 | -44.05795 | 2026-01-15 00:09:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2d22dadf-041b-389d-9750-59e7e27c005f | -14.17144 | -43.72204 | 2026-01-15 00:09:00 | TERRA_M-M | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0b4a981f-b22e-31ac-b6a4-4215375cdc96 | -10.48703 | -44.93658 | 2026-01-15 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 528a2869-2643-3719-b9f0-d9002c282b76 | -12.12333 | -45.57621 | 2026-01-15 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a85080c3-3a37-3c0b-8e76-0afea5b7e0a2 | -12.0863 | -45.30389 | 2026-01-15 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 9eaca89e-01b7-3953-b61d-f8a010650f3f | -6.88404 | -42.85007 | 2026-01-15 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 5ae68728-6eb7-3f4f-8637-2529bfd405b2 | -14.58031 | -42.26558 | 2026-01-15 00:09:00 | TERRA_M-M | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| fd1bffed-76e2-39f1-babe-2cf7a6eda893 | -12.09514 | -45.3026 | 2026-01-15 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f79f8a29-b560-38db-b294-e21c3403723f | -13.60514 | -43.56456 | 2026-01-15 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2fb7f86c-b1a1-379d-a86a-c66c4232c5b4 | -14.76729 | -45.93565 | 2026-01-15 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e7663ce5-cdfd-3ee9-b59b-d1f792eca8b5 | -12.5164 | -43.69013 | 2026-01-15 00:09:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 15a027a8-8b13-3497-a894-d73a6a8deded | -12.5049 | -43.6731 | 2026-01-15 00:09:00 | TERRA_M-M | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2261042e-a01c-3db7-bb3b-971cb55d5216 | -12.09391 | -45.29359 | 2026-01-15 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 1a48ad82-89da-32db-82f3-551af28dc9ef | -7.67985 | -43.72865 | 2026-01-15 00:09:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 8aa50c9a-f34f-3c3e-b85c-774ba9741732 | -12.09268 | -45.28457 | 2026-01-15 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 45ccaf1e-b95f-3606-b802-48a176eddfaf | -7.24171 | -43.04946 | 2026-01-15 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 1e2db6cb-240a-3cb8-94c8-d2b8c2ed68bb | -12.65941 | -46.76309 | 2026-01-15 00:09:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 7b4d8b29-a253-3554-afa4-022d14a78f8f | -12.13222 | -45.57495 | 2026-01-15 00:09:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cf3e6eed-7745-3f68-816c-a868194dff55 | -7.04774 | -43.9535 | 2026-01-15 00:09:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ddb41722-40ad-34bc-8555-c85d449b0136 | -10.59402 | -44.9783 | 2026-01-15 00:09:00 | TERRA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| e856426f-e07e-3fec-99a6-8c5a6e9caf3c | -8.91523 | -45.96102 | 2026-01-15 00:09:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38610fa9-47ce-31d5-bf9d-21dc430610b9 | -6.88542 | -42.84359 | 2026-01-15 00:09:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| cfc8098f-237d-3abc-be2e-c0a0c4b4841a | -4.372 | -37.8918 | 2026-01-15 00:10:00 | GOES-19 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 77.3 |
| 9d131a12-f3c0-336e-a698-cb98ff0eff2f | -7.2411 | -43.0428 | 2026-01-15 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| 76bed683-13e6-3c66-aa7b-e50b16c01709 | -4.37928 | -37.92288 | 2026-01-15 00:11:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 29.7 |
| ec3fc738-456f-3ce1-9647-daefc4af48eb | -4.39689 | -43.85472 | 2026-01-15 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b27b92ae-f8d8-3ddb-b836-982ff334f34c | -4.73243 | -46.65546 | 2026-01-15 00:11:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7e5f35b1-1c3b-3edd-8ed0-f68ccf555d2c | -3.66455 | -43.52402 | 2026-01-15 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 81c22e83-227d-39a5-b7f1-6d3414ef8b63 | -4.92718 | -43.41753 | 2026-01-15 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 54c658eb-1f6a-3efc-9341-9c32ae3307a3 | -4.37288 | -37.88863 | 2026-01-15 00:11:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 73.1 |
| dae2aa2d-32ce-3c9b-972b-08262390fa37 | -3.23946 | -41.80757 | 2026-01-15 00:11:00 | TERRA_M-M | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 1325568f-12bb-38b7-a505-a78f4c12e3ea | -6.56775 | -44.46634 | 2026-01-15 00:11:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2e9a2221-877f-35e2-911d-da38ff3a0c77 | -4.37743 | -37.91737 | 2026-01-15 00:11:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 71.7 |
| a050a1da-a5b6-3e91-b146-b26abaad6675 | -4.37494 | -37.89408 | 2026-01-15 00:11:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 67.1 |
| 16f99691-8853-344e-bb34-dfad818dc784 | -5.53824 | -45.15081 | 2026-01-15 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 69b84b0d-e232-3afe-9b23-ed0bd863ff4a | -5.90013 | -42.55466 | 2026-01-15 00:11:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| e91caafe-901a-318c-a12b-822ffa72f9f3 | -4.91393 | -43.46358 | 2026-01-15 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ff94b0ff-3d4d-3bb3-9a97-1fcb02a3fbcf | -3.66162 | -43.51966 | 2026-01-15 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 31958ab8-f9f3-3b40-9b22-a15cccfd1fb3 | -4.39836 | -43.86504 | 2026-01-15 00:11:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 946b0747-51df-3993-afaa-27abc89f10ee | -4.92871 | -43.42845 | 2026-01-15 00:11:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 305dc83a-e6c8-3899-8053-a5224b2c5aaf | -8.4279 | -44.010502 | 2026-01-15 00:16:00 | METOP-B | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6a5c7402-d62c-3036-95dd-b34fd42987a5 | -14.7712 | -45.922501 | 2026-01-15 00:16:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e796258b-dcb1-3d46-ace9-7772f9ac5ed8 | -10.4832 | -44.916199 | 2026-01-15 00:16:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2fbe566a-86b5-3991-912d-999cdab31ed3 | -7.8572 | -39.070801 | 2026-01-15 00:16:00 | METOP-B | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 8e009d19-d715-32c8-a017-23a3797230b3 | -7.2243 | -43.042301 | 2026-01-15 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f50168fd-d6c0-3594-9f9c-9d4644457213 | -6.8827 | -42.822899 | 2026-01-15 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 31439cbe-b8d0-3a19-9c27-4a724cb000f4 | -13.6038 | -43.543701 | 2026-01-15 00:16:00 | METOP-B | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f194c9ec-c5d4-328b-9a36-5e86505e20cf | -7.2437 | -43.037498 | 2026-01-15 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b09e7820-b886-3a31-b9b3-34aa6f2457c0 | -12.088 | -45.277401 | 2026-01-15 00:16:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 422bbec3-bd31-33b5-b2f3-42d966dcf1ff | -10.4855 | -44.9258 | 2026-01-15 00:16:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 62cb66c2-7923-30c9-afd4-f3cb51477ab7 | -12.1164 | -45.615501 | 2026-01-15 00:16:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 55b00b78-c109-343b-867c-f4e3a5eadf6c | -10.5967 | -44.959 | 2026-01-15 00:16:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 373ea099-82fc-36ac-8d25-203dd51875ba | -8.4251 | -43.998901 | 2026-01-15 00:16:00 | METOP-B | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0cac8bc6-479f-3d3e-a780-3a959d047419 | -10.5869 | -44.961399 | 2026-01-15 00:16:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b0ffb1dc-03d8-31a2-9f27-9d87dd7eafef | -7.2306 | -43.025902 | 2026-01-15 00:16:00 | METOP-B | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f5116c42-4e37-333f-bfc0-ec0193ea4c2d | -10.7731 | -45.005501 | 2026-01-15 00:16:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 486af8b7-0671-37bd-887a-cf8cda8c4bfc | -10.3459 | -44.817299 | 2026-01-15 00:16:00 | METOP-B | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f50c843a-d51e-3597-9de1-91c5e2f2ace9 | -12.0901 | -45.286098 | 2026-01-15 00:16:00 | METOP-B | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
