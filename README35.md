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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6ff9d07b-ac1c-3fdf-adcc-6186f72b0e94 | -15.96912 | -43.33081 | 2025-10-05 03:36:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c36f47e-1828-3c38-ab15-5c1ef5c835ba | -15.55232 | -46.85164 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 598a371a-9e49-3ab2-a4e4-afcbc947f770 | -15.12818 | -45.74337 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6374abfc-e480-39ac-85d7-634bdbd6aa17 | -15.39739 | -47.96433 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dbff6bd-4f8c-37b2-87e4-e9d207326373 | -15.7363 | -46.26581 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8177da89-4c33-3894-8703-c3f45e8882c9 | -14.91938 | -46.85731 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1d78c841-d7d1-3924-966c-ed366f64cbb7 | -16.35466 | -47.05851 | 2025-10-05 03:36:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 460c5b0b-6be9-335b-ac72-71dc53a7581e | -15.20881 | -46.38512 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a85e816-b1dd-3642-891e-5227a1fae9a0 | -14.95434 | -46.85371 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6daddf9-b44c-3d90-8122-13e382540e1e | -14.33625 | -47.68759 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 28936648-13b1-3dff-9df6-b16ee3774007 | -14.68859 | -48.29885 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| edd10b32-1146-3360-b86d-6c637d9ee8ac | -20.7353 | -44.33068 | 2025-10-05 03:36:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 048eeba4-9955-303a-aa37-fe44e943922b | -19.86662 | -45.69698 | 2025-10-05 03:36:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a3ff35b-24f9-3b73-b20d-ac38167efdc9 | -14.67315 | -48.3689 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4bdb642c-95a6-3929-99b7-fb2932409f21 | -15.35182 | -47.97412 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7084fb5e-ceda-3f06-8e28-e3c66e0cacf1 | -15.13741 | -45.73013 | 2025-10-05 03:36:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1447835-8a4e-308e-8084-1f121d781048 | -14.6627 | -48.28122 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5e8cfa1-873f-3db4-b7b7-dc821a1d1765 | -18.7885 | -41.38353 | 2025-10-05 03:36:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2aa31f1f-cc35-335c-8b61-580a87ee7707 | -19.58874 | -44.6334 | 2025-10-05 03:36:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96f0192b-34b6-3c35-afd8-796aeb73dd62 | -14.6633 | -48.35448 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 08c0188e-7165-33dc-b2bb-67c91dd692a4 | -15.30348 | -47.96365 | 2025-10-05 03:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 6feeb3bb-74a0-3bb2-aaf0-357ff54bdf01 | -14.46121 | -46.33581 | 2025-10-05 03:36:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c2107614-c841-3d55-8225-dcb5c2792e93 | -15.74584 | -46.26712 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 353a1d18-0a0c-36be-8915-5fb2cc815c87 | -15.73963 | -46.26569 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15b26257-e859-3ee7-9502-2de5d4dccfcf | -15.54258 | -46.8345 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 93bb2318-3d91-3d11-bc66-351f8aa27afe | -15.76541 | -46.26692 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a8c05f00-1055-39f9-89dd-782d3cce1857 | -15.12921 | -45.73861 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a88ad1b-f172-3366-ab81-c67c9a59892b | -18.33442 | -45.88427 | 2025-10-05 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 3b99360a-834d-3a22-a60e-275689757cd2 | -15.75187 | -46.26937 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 445d71f9-8175-373c-a671-2616064644cf | -17.97171 | -45.00819 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c99fad31-b8d2-3a3f-a751-70792c5ed99a | -15.13836 | -45.75541 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ce90f75f-b113-33a3-bb0e-ce2c71de02dc | -18.33196 | -45.8905 | 2025-10-05 03:36:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 67.7 |
| efa42bee-c3a9-32a1-b48f-bafb11e45c23 | -15.32576 | -46.37313 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3008e7e1-9485-36e3-b484-facc03299cf6 | -17.02051 | -43.46011 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 241e2b03-c8ad-3b97-93a3-1cfca2b55b1d | -14.6806 | -48.30131 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6d6dd0b-ce62-3276-8848-a342c24c5971 | -14.65329 | -48.33285 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c067a07c-15f9-3d0e-90b4-67be0ba82167 | -14.87617 | -48.26384 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 747dc181-f5d8-32f4-9a96-dd894669cf23 | -15.53944 | -46.81816 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e897f788-a261-350a-aaf5-12d2a73daf9a | -15.13843 | -45.72537 | 2025-10-05 03:36:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 98766ce6-6bac-3918-8f0f-636d2d00cf10 | -14.94801 | -46.85138 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9174d1d-f3e4-3a3d-af4f-5ad506d05050 | -14.66181 | -48.35258 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 586702cb-d334-34c9-8b78-6783bd09f4d2 | -18.55155 | -41.58267 | 2025-10-05 03:36:00 | NPP-375D | NOVA MÓDICA | MINAS GERAIS | Brasil | 3144904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 13a260ec-d541-3188-abaa-68f3823c5825 | -15.14035 | -45.74616 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 51d89c73-dc68-31c1-8d5b-2381255acda1 | -17.97414 | -45.00639 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 743cd08d-8377-341f-a5a5-05935fbf3412 | -19.8611 | -45.6955 | 2025-10-05 03:36:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12883c9a-6471-3fb9-8b6c-610214439fcb | -18.00053 | -45.00894 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bff6760b-f61f-326c-bdb3-0442ddbcb0b1 | -14.88121 | -48.16118 | 2025-10-05 03:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d7357cda-f715-3ce7-b073-03e092bf22ea | -15.74252 | -46.26713 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40b6ba6d-7f57-3c77-9685-feca2cffb7ce | -14.00699 | -48.20869 | 2025-10-05 03:36:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8ffe918b-4bdc-3363-a69f-8a9db50323fb | -14.68089 | -48.34287 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0083615c-c44f-3f88-80de-b80f6a10af4f | -14.68196 | -48.29513 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 236d2c78-8e88-37bf-9341-8c77c3c16c99 | -15.54777 | -46.8432 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eab33341-06d2-36fa-a10a-4cc381e722f7 | -15.51321 | -46.84666 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66951354-d3a3-3731-b48e-cef3f4d241ef | -14.33348 | -47.66731 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d626bbfe-8867-3691-8e8b-f148bc5aa8d1 | -15.53497 | -46.80853 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b765c474-aaf1-3362-9662-7de9c892d91c | -15.37986 | -47.94559 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| aa30bd64-dffa-3a87-9855-2e9e1da1fbd4 | -17.20161 | -44.45021 | 2025-10-05 03:36:00 | NPP-375D | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3ee2c5c-9155-3f44-94a7-48b8b1f98887 | -14.41462 | -46.17739 | 2025-10-05 03:36:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0f1e5be-382d-38aa-9089-ccdad8c12af8 | -17.94616 | -47.02205 | 2025-10-05 03:36:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec8a0a1e-eff8-3299-98fc-90979ca6f10a | -17.02884 | -43.44553 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 217e4b14-d358-34fc-ac37-7ad670946c06 | -20.73962 | -44.33511 | 2025-10-05 03:36:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 45765e9f-6ceb-35e6-81c6-84b537b66536 | -15.12889 | -45.74201 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cca15fae-3220-36b5-b3fd-d6724e3ba320 | -17.98036 | -45.00435 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7314cc1-6f93-3b21-8bed-09a2dfede636 | -14.68666 | -48.27396 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3d98750e-2559-36d5-a16b-e96dc0c00f5f | -15.29658 | -47.96213 | 2025-10-05 03:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 75a69bbc-dc07-3197-9cb0-57cf850ceff1 | -17.01714 | -43.45058 | 2025-10-05 03:36:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1d0c3f0d-0e51-3cfa-80c7-3ddd7c019011 | -14.79967 | -44.89521 | 2025-10-05 03:36:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 797d4a19-b77f-3fc0-bc55-d224aa121dfe | -15.90752 | -48.83344 | 2025-10-05 03:36:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7d224af9-3f55-3aaf-b443-e2e11c085ac7 | -16.45033 | -42.68473 | 2025-10-05 03:36:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 553becab-584a-3101-a093-789b1cb03fb9 | -15.53609 | -46.83324 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7ce20c70-5450-34fe-a7c8-39a77f1be2a8 | -14.88977 | -48.26923 | 2025-10-05 03:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f37afc2e-1c5f-30b4-8757-1e6eae191365 | -15.38012 | -47.93839 | 2025-10-05 03:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a50316d2-4db2-3140-bb1e-83c68fddf171 | -17.5875 | -44.4603 | 2025-10-05 03:36:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1fe95a10-1e06-39ea-a3c3-1cbf4deaa937 | -16.29092 | -45.24297 | 2025-10-05 03:36:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 084fcd9b-64e6-353f-b793-b046d8a90bb5 | -14.66936 | -48.35221 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3fade1dc-7a85-34a0-8541-49e1543e7c24 | -14.33483 | -47.69404 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8c5165fe-f728-3d4f-8a77-8b479ac09528 | -15.54147 | -46.80904 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 41d7d64c-db2e-357b-a12c-8d01b4fc02ec | -14.46098 | -46.33516 | 2025-10-05 03:36:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 24580704-5d6d-3e42-9f15-9a752d949ba6 | -15.53709 | -46.83 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d0a5301-1d25-376a-88d3-54f5d0623daf | -15.29974 | -46.31912 | 2025-10-05 03:36:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d303f772-611e-3361-a081-595f7ee0e374 | -15.1238 | -45.73584 | 2025-10-05 03:36:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 540996ca-5f7c-367e-85a9-c236a0904ae6 | -14.92973 | -46.84118 | 2025-10-05 03:36:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92692e38-35cb-3e8a-8b32-e68bf208102d | -15.16805 | -43.6298 | 2025-10-05 03:36:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6da005ca-5e64-3858-90b9-4ff4ff2a8726 | -15.31467 | -46.37128 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6afd4a8-84e2-3ee9-8601-dd8be4854eae | -15.30107 | -47.32925 | 2025-10-05 03:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a8ae201-bc90-3ac3-bb83-efb4a5bed031 | -14.68989 | -48.27044 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2ccddb36-72c0-3dbe-b728-178f1d6533a7 | -18.0015 | -45.00444 | 2025-10-05 03:36:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4a691649-5e42-30b2-ae53-933713d5b2bc | -15.30953 | -47.32245 | 2025-10-05 03:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58ba7e77-aeea-3b27-aaeb-f2de172b432d | -14.45992 | -46.3402 | 2025-10-05 03:36:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2719d0f-3781-33de-b3bd-c59e0bb18727 | -18.78768 | -41.38781 | 2025-10-05 03:36:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8e4330f5-e4ec-391b-a91c-0ac4f687e89b | -15.29838 | -47.95869 | 2025-10-05 03:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 8dde1090-dd07-3b63-9280-36a29f46c901 | -14.66343 | -48.37909 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5a0d26e4-635a-3bd2-97d9-c4b0cb46d780 | -14.32003 | -47.69548 | 2025-10-05 03:36:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6a986abe-7fc8-30e7-a7ed-0956af476edb | -15.13701 | -45.73359 | 2025-10-05 03:36:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 994b842b-6d75-33f2-8578-0e423b3e9b8c | -14.87837 | -48.15764 | 2025-10-05 03:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 16960f6b-35b5-360c-98ac-7f5c63b1ad81 | -16.36094 | -47.06069 | 2025-10-05 03:36:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d71ad2ca-b30d-335f-ba20-b8c71904e4a2 | -16.26154 | -47.11234 | 2025-10-05 03:36:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ea00ab9-c5d4-33c5-a9bf-66c2b40c08a1 | -14.6514 | -48.34114 | 2025-10-05 03:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ec87590-b99a-33b7-88d1-04ba6c64c4ce | -15.5426 | -46.83575 | 2025-10-05 03:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9191e3a-b318-3751-a010-fe6248c023b5 | -16.26927 | -47.10812 | 2025-10-05 03:36:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README36.md)
