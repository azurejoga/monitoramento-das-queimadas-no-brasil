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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb5157a0-636d-3037-a852-200e68ff7857 | -11.71458 | -47.62363 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e50aee26-c733-3cbf-9f39-11f4ada4691b | -9.96707 | -46.77756 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1796a89e-bdc6-3f8b-ac1a-7b3eb946fe12 | -14.56738 | -53.58959 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| b8302d93-2255-39ab-8abf-d01e2e153a0e | -10.10018 | -50.27991 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fb9ecd4b-eb45-389f-b41e-1debdbf2413c | -12.09448 | -47.14025 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c038cc4c-c914-3b51-b077-b22a9106713a | -11.91667 | -45.04407 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6ae8dc30-d6ad-3a58-be49-efdb2e5806c7 | -10.15092 | -45.76989 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d0ad5546-1aa6-3da9-8bfa-57625875f16e | -14.44209 | -52.51219 | 2026-08-31 16:30:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f0d59b4a-3577-3141-b449-501c5cc58a7c | -11.73954 | -47.63815 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0182a40f-1ad2-34c2-9075-502035375683 | -12.16951 | -50.53541 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c5a4eeb9-dd26-3c25-80b2-046e01d5fcb8 | -9.89814 | -46.63327 | 2026-08-31 16:30:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 75e4142a-e793-370e-aa5c-078c4bf927e6 | -12.09503 | -47.14427 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| de9f58ea-5626-3ef7-a823-81fb327590b2 | -11.91535 | -45.04306 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| fc881c9f-01f3-368a-926f-8a462433ef10 | -10.56281 | -50.36195 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7340054d-051f-3d15-9a81-c5d3295e850e | -13.79903 | -40.11086 | 2026-08-31 16:30:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 885ae201-6296-3176-a6fa-26a4f353cf99 | -10.05719 | -36.53037 | 2026-08-31 16:30:00 | NPP-375 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 3192b6e3-197c-34a2-9d89-e3ecfb373106 | -11.49239 | -50.34556 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e97a3f73-ae3a-3d6a-b702-9124f6c51ae8 | -9.65141 | -46.06601 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e02ca865-de5f-3118-87b3-a0f659e602b6 | -11.08609 | -51.53857 | 2026-08-31 16:30:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| cca92fc8-02a5-3ba9-a693-2b30d56774ac | -15.24331 | -52.72993 | 2026-08-31 16:30:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 9b9ee3cb-25f6-389b-8a1d-ba8228516985 | -7.15436 | -37.66035 | 2026-08-31 16:30:00 | NPP-375 | CATINGUEIRA | PARAÍBA | Brasil | 2504207 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| a70769f4-db80-3466-8312-bb646a507142 | -11.15888 | -45.04844 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 840e680c-827f-3f5e-a98d-768e4a741304 | -9.19743 | -47.99882 | 2026-08-31 16:30:00 | NPP-375 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| d9be299b-892a-3ebb-abc4-56c4e1e659e5 | -9.15956 | -49.95586 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c78360cb-1a84-3a20-870a-4553118d6872 | -9.58377 | -47.60194 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 616061e0-ef42-3d7e-9821-48cf22aa28cf | -10.99023 | -48.38843 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 52556b30-3247-32db-813b-a7c0ae5513ed | -14.79577 | -48.2627 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 06483016-d013-389b-957e-b494f8baefc3 | -10.82413 | -45.36269 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| ea5ce4be-d2c8-3003-9d8d-0d4580831647 | -10.54871 | -43.92585 | 2026-08-31 16:30:00 | NPP-375 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bd831d46-7634-36c9-b8d3-0fe1c5da7f04 | -11.67779 | -44.87292 | 2026-08-31 16:30:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1fc64fca-921f-3943-8079-931dfb6036fc | -10.56321 | -50.36505 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf37814c-1b60-331d-b68f-283f4f47f950 | -14.23048 | -43.8225 | 2026-08-31 16:30:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| f1a57d35-a318-399d-9fda-c4ae27d19d46 | -10.96427 | -48.40891 | 2026-08-31 16:30:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cbf437e2-ead6-3e35-80f2-d86dec8f6932 | -10.01818 | -46.15552 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3fa8219a-7a73-3a46-8e04-5b4344ad0184 | -11.21928 | -45.11201 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 54c79135-6cc0-39c4-9822-669338e353ca | -13.0538 | -40.46111 | 2026-08-31 16:30:00 | NPP-375 | MARCIONÍLIO SOUZA | BAHIA | Brasil | 2920809 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ed8fa5ef-440e-3f73-bf65-c97352135aff | -10.84818 | -45.31791 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 547a063a-3832-394c-90a7-b1aa6d062638 | -11.24221 | -45.14053 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| aae8dce2-b750-3c07-b04b-46299ecbc522 | -9.65892 | -50.85472 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| ddb726ff-260e-3586-8f78-2452cfc85a6f | -11.25321 | -45.11172 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 25b49419-0102-3342-9805-3843a09d371e | -8.4976 | -45.5341 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 37eae500-e967-3bfb-9313-448c2cce067d | -14.95413 | -54.57082 | 2026-08-31 16:30:00 | NPP-375 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 51b14306-8699-3b83-b8fb-efd0f4fb0508 | -13.38949 | -51.78634 | 2026-08-31 16:30:00 | NPP-375 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 57d6c8e0-d989-3d92-8586-72403149a2be | -8.86333 | -47.07346 | 2026-08-31 16:30:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| c1543e4e-ab6f-36bd-8866-72bc8ea5f3f4 | -8.72751 | -45.37674 | 2026-08-31 16:30:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1cff9e57-6acc-3dd0-a9d4-932c7d48cf32 | -12.07771 | -47.20764 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 3e167936-d15d-3b72-b6be-da7f45eea104 | -11.17917 | -50.56583 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 717404a4-9376-3c6e-b860-32e8930a0412 | -9.60237 | -47.61146 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 658682ab-2653-3726-b2c2-17b4473e5ca3 | -12.89428 | -45.84513 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 71ebc001-53c3-3fa0-abb1-be4a23eb288f | -10.74207 | -47.95613 | 2026-08-31 16:30:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b67aabfe-5850-3573-9b96-aebb5aeeca57 | -12.17485 | -50.53475 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 089f07d7-5e89-375b-bfee-7f076686d56d | -9.67614 | -48.32167 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 808b5a9d-97c1-3898-aebb-c6b2ead56417 | -11.20033 | -46.11415 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 406d294f-3f2d-3a02-ba8d-3a02f87040ff | -10.74215 | -54.03733 | 2026-08-31 16:30:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 43.9 |
| de11a17e-7afe-3a71-85ba-b88fa4a4fed8 | -11.24731 | -51.25888 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| eabe6ae3-f2e4-356a-8b85-8b672f43fb4c | -8.76596 | -46.45596 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| a6001957-6a54-3987-b93a-894caa5a870a | -10.45419 | -46.74504 | 2026-08-31 16:30:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ab2645fd-2bce-395b-b42f-f1c3697d64a5 | -11.94246 | -40.62266 | 2026-08-31 16:30:00 | NPP-375 | MUNDO NOVO | BAHIA | Brasil | 2922102 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 6a8d6d26-19d3-3bf9-95d6-32b162e6136c | -13.46262 | -51.40979 | 2026-08-31 16:30:00 | NPP-375 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ba0c2897-746b-32ff-a47a-096b0405aeae | -11.63253 | -49.41267 | 2026-08-31 16:30:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e6e06d96-70b4-34cd-838a-1e599e901f06 | -10.13046 | -45.84412 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 77e77c92-1805-38f1-a650-c9b335d57861 | -10.92637 | -50.61994 | 2026-08-31 16:30:00 | NPP-375 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 681f2b89-d3e9-38dd-a17e-7a080764fa7f | -11.24701 | -45.0948 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3312a6d-a91e-3d98-8f01-4489de37eaaf | -10.12573 | -50.31643 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dee06f10-34d6-3ff9-bb33-ff3ab8fa87e5 | -12.09316 | -44.99178 | 2026-08-31 16:30:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0e5de4b5-685b-3931-ba37-5eae605190d9 | -11.20823 | -45.11395 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6d3f017-f305-3e01-9e1a-94f5068434a4 | -11.68086 | -46.74459 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 36b36ae9-2f1b-3d45-b107-0abd8b3b0bb7 | -9.40854 | -51.6887 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| df281a45-d1eb-356a-a1c1-f6aff9b9d52e | -12.89585 | -45.83725 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5b7b6516-b128-3ba8-b199-2e8e50088d33 | -9.68973 | -48.12812 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 2f9e2cf3-4bb6-3127-8898-1f5adcdfae23 | -14.79146 | -48.26139 | 2026-08-31 16:30:00 | NPP-375 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| a15732a2-d127-3e5a-ac92-3fa8ac45721f | -12.16867 | -50.52868 | 2026-08-31 16:30:00 | NPP-375 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 268a3074-52fc-3a16-8867-806320cc2438 | -8.73505 | -46.46081 | 2026-08-31 16:30:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ccc117df-f22d-3d6f-8b40-2cf36184bf6c | -15.40462 | -52.70957 | 2026-08-31 16:30:00 | NPP-375 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b12ac64e-b7dc-3da6-afd3-8bc8120b038d | -12.37792 | -48.16524 | 2026-08-31 16:30:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e731203c-64cc-35f5-8fc2-8d3f57c3a721 | -9.64557 | -46.05243 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9a88f8c5-498c-39ee-960a-1a57f572e7ae | -10.84702 | -45.33634 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 38756c77-ff6f-359f-bc0d-475515acc644 | -9.66992 | -47.94914 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| b544604c-56af-3ce5-8357-44967e75f34b | -11.96291 | -47.74842 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 2d944f2e-95ce-3291-9ff9-d3c3028174a4 | -14.51919 | -52.29298 | 2026-08-31 16:30:00 | NPP-375 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8f1c11fa-1720-35dc-a97e-f24e4422bfee | -14.61882 | -53.59256 | 2026-08-31 16:30:00 | NPP-375 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| bd7c36e8-1f88-3c5f-ac2a-39bbb0f1d194 | -10.12415 | -50.30434 | 2026-08-31 16:30:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 18aba0fc-668c-3935-bc18-f743436c0461 | -11.2008 | -45.06118 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 61e8f075-cfad-37af-ab93-aa265d2d660f | -10.83681 | -45.99704 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f2e23f04-1c64-33c2-8821-1bb17065e1ad | -13.84796 | -54.08965 | 2026-08-31 16:30:00 | NPP-375 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7ead7fdf-16fd-30cc-99f1-b1a862995c84 | -12.10133 | -47.25358 | 2026-08-31 16:30:00 | NPP-375 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| cf081fe4-1352-34c1-a9a1-fcc36f1a7249 | -11.25258 | -45.10733 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 7ddbd8b0-f293-3f81-b8f8-7acb14dc5b10 | -9.6577 | -46.05541 | 2026-08-31 16:30:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| ee381cd3-dba4-31c2-8f34-1a5a3652172a | -11.68057 | -47.60133 | 2026-08-31 16:30:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6019a923-dd7a-3560-ad68-4a6910a12d4f | -11.24958 | -45.38151 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 764272b0-9654-3ba4-b3a5-b385389845a6 | -9.42403 | -45.6842 | 2026-08-31 16:30:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 2a7c8e9b-5fe6-39d1-92f2-b679233209b7 | -9.66177 | -48.28319 | 2026-08-31 16:30:00 | NPP-375 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9ca9b66c-4ade-38a3-8091-5cb15ca2744c | -11.2411 | -51.24535 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 86063bac-a869-3eff-966f-74c3c68e97f5 | -9.16802 | -49.98937 | 2026-08-31 16:30:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4dd84761-d2b9-3613-a978-1ead54414cf4 | -11.64752 | -46.74546 | 2026-08-31 16:30:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 51f7dc5d-203d-3d6f-9ae5-9bd09eebe00f | -9.61189 | -47.61822 | 2026-08-31 16:30:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 17659242-3120-3a16-be18-a5ac84e84204 | -11.24342 | -51.26354 | 2026-08-31 16:30:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 28.4 |
| aefbd837-4b69-3249-8b8f-5f10f9e3005e | -12.88073 | -45.84436 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| b81134dc-86c7-3842-87a3-d3a1034b3fcc | -12.96035 | -45.92725 | 2026-08-31 16:30:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 689b6c4d-173b-3aa6-9f70-fe26bbe35d56 | -11.19729 | -46.09638 | 2026-08-31 16:30:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |


[Clique aqui para ver as próximas entradas](README117.md)
