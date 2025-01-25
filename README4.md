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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70c48dca-d403-38a9-85fe-70d45f668441 | -16.39951 | -49.19446 | 2025-01-25 04:18:00 | NPP-375D | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0cdf911d-1bdf-3f4e-9851-52759667e87e | -19.32623 | -40.06366 | 2025-01-25 04:18:00 | NPP-375D | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1fb79c47-f465-3567-bd0a-250605097687 | -17.48992 | -45.25915 | 2025-01-25 04:18:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 480b7092-1ae0-32ff-9610-7ad02b9060a3 | -18.42652 | -40.03395 | 2025-01-25 04:18:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1761e92b-0c76-3953-9a90-7b7e42876752 | -17.00821 | -49.78046 | 2025-01-25 04:18:00 | NPP-375D | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a4f7a0d-dcea-368b-b2bf-7463653494f4 | -18.14644 | -47.80098 | 2025-01-25 04:18:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15666cad-460c-3cce-bd99-a43f8c7828db | -20.63383 | -55.70514 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5f5bda9d-f876-3e09-892e-9100311bcd75 | -21.07289 | -56.39575 | 2025-01-25 04:18:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c8ccf99-c863-3db4-a48c-c1bd8778f8f5 | -22.6778 | -42.85646 | 2025-01-25 04:18:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9b3023c8-3882-3501-ac21-53818fbaa2a8 | -20.41662 | -43.55344 | 2025-01-25 04:18:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a115675d-421d-3e7e-bb7d-2a754f9fe68b | -21.182 | -48.63512 | 2025-01-25 04:18:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f1f7f683-9075-355e-9e85-9ddef6fea90d | -22.67845 | -42.85147 | 2025-01-25 04:18:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d7914a88-8dee-3bb6-85ad-07f900ba972d | -20.63412 | -55.71199 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 613d0401-a48a-30e5-9b82-8beb113698d3 | -22.28052 | -48.57196 | 2025-01-25 04:18:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| 6a677117-7566-39e2-93fa-9a71fb00c76a | -21.98073 | -42.13419 | 2025-01-25 04:18:00 | NPP-375D | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 43402d1d-8ff4-397b-9e2e-da25cc816288 | -20.63819 | -55.70983 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 19f684d1-c8c0-3893-b844-5d42dc160720 | -20.63342 | -55.71523 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 744d2469-47ea-3a7c-9dca-48116de37d33 | -22.67399 | -42.85589 | 2025-01-25 04:18:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0358dc1c-55e5-3a3f-a49d-2259d12e6745 | -22.7523 | -43.33938 | 2025-01-25 04:18:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4a95d6aa-7217-348c-8209-01f293b8d533 | -19.37789 | -53.55855 | 2025-01-25 04:18:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1911276f-406e-3cbb-bf2a-053b5c5752c5 | -21.18542 | -48.6358 | 2025-01-25 04:18:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e243dd48-08d0-3321-b555-fd1d1177dbb6 | -18.84128 | -52.49081 | 2025-01-25 04:18:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 10c85114-70dc-31c4-a7d6-1db94a2bc0fe | -21.97998 | -42.13555 | 2025-01-25 04:18:00 | NPP-375D | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 98b37548-1c5f-3187-9114-fcf7d07c100e | -20.63751 | -55.71306 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a42647da-bf73-35c9-bd9c-b119d272177b | -20.63552 | -55.70554 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b4a78c5f-0a5a-3c5a-b7c8-414e59fc48fd | -21.07815 | -56.39697 | 2025-01-25 04:18:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0f8e0e60-558d-3a80-9a89-fd99ec00a4e0 | -20.6318 | -55.71489 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7d2ed699-1481-3338-8fe2-13d319a5542d | -18.84046 | -52.49507 | 2025-01-25 04:18:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 13d59e56-af13-3d06-a73e-3134eed1caff | -19.0504 | -52.8581 | 2025-01-25 04:18:00 | NPP-375D | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 957f9ae5-6157-3ed9-89bc-114ccdb0a3b4 | -22.69843 | -43.34549 | 2025-01-25 04:18:00 | NPP-375D | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 62bbae08-8239-3e4c-9e03-582931c9599d | -22.28117 | -48.56807 | 2025-01-25 04:18:00 | NPP-375D | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 932b8855-6921-303c-996a-43cf8d15be20 | -20.63482 | -55.70876 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6e7c4c5d-23c8-399f-a10d-b6efbe68d04d | -21.26794 | -50.65422 | 2025-01-25 04:18:00 | NPP-375D | GUARARAPES | SÃO PAULO | Brasil | 3518206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0df74397-0d0d-3999-b43d-1e7fdad3e6ce | -22.54099 | -48.81321 | 2025-01-25 04:18:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7d8950c-1418-3a83-8916-5c5d8c123de0 | -21.98466 | -42.13475 | 2025-01-25 04:18:00 | NPP-375D | SÃO SEBASTIÃO DO ALTO | RIO DE JANEIRO | Brasil | 3305307 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1b122a6e-2a08-3312-ba37-d2a8555c9473 | -20.63248 | -55.71164 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4aef92de-e060-311c-87cf-d60aa1b6a492 | -19.37336 | -53.55749 | 2025-01-25 04:18:00 | NPP-375D | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06c06313-d112-3868-a717-57feb9be06fb | -20.63316 | -55.70839 | 2025-01-25 04:18:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| eadc9735-0675-382f-9734-d78ade5629fa | -15.253 | -60.2095 | 2025-01-25 04:20:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| fcac15ad-2b67-38ce-bc38-3c76fd9c3bff | -22.69526 | -51.80542 | 2025-01-25 04:21:00 | NPP-375D | SANTO INÁCIO | PARANÁ | Brasil | 4124509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8656cdc1-9be0-386b-a300-e7ce29f3ef07 | -22.69911 | -51.80631 | 2025-01-25 04:21:00 | NPP-375D | SANTO INÁCIO | PARANÁ | Brasil | 4124509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cf9a3ad3-0047-3b34-b1b4-ba90a0d928cf | -3.17828 | -48.03035 | 2025-01-25 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f2102e6-e0bf-3bb8-b7c8-dbabd1d75b59 | -4.41143 | -48.95889 | 2025-01-25 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 886a8591-8031-3269-b297-903ce18b0bf0 | -3.24593 | -48.07638 | 2025-01-25 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a506d57-63b7-3d90-95fa-7a3b42ddf254 | -3.24648 | -48.07291 | 2025-01-25 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ea2609a4-8324-3d14-bb5e-0f4ce2e8bff1 | -2.88236 | -48.27082 | 2025-01-25 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0f5251b5-c714-3dda-83e7-ced5f3a88a2a | -1.87887 | -48.71269 | 2025-01-25 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d185b8f-bce8-37fd-8621-b476b9e8ce71 | -3.34102 | -49.02684 | 2025-01-25 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7f0d086-17f2-35cf-acf6-f5e74b866d7f | -11.05461 | -45.3815 | 2025-01-25 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d35e31c-1a7b-3817-ae67-19c80973670a | -11.05105 | -45.37735 | 2025-01-25 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9e571a0-b30f-38cc-88dd-c301aa434bcc | -9.53001 | -47.78206 | 2025-01-25 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a5ca0f9-266b-38c7-9753-ccf16792eabb | -12.53418 | -48.32296 | 2025-01-25 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b19ea5ae-da68-393e-974d-b79742753071 | -10.9448 | -48.07816 | 2025-01-25 04:38:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 14eac092-81f8-353e-8fa2-038b589ea033 | -12.91123 | -45.09775 | 2025-01-25 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3aa3b5f-d225-31d9-9710-6f52c1870285 | -12.90752 | -45.09313 | 2025-01-25 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca011bdc-7941-3cc0-8a9d-b02628d16d6f | -11.05511 | -45.3779 | 2025-01-25 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 821d4e94-0fbd-3f5a-a64b-461bee61d1a2 | -10.49886 | -42.42671 | 2025-01-25 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 71a08cf6-eefe-3ae5-bc4a-dac3f5478ea1 | -11.28078 | -44.4498 | 2025-01-25 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4fe541c7-29eb-3a13-9863-178507d59f32 | -9.52652 | -47.78152 | 2025-01-25 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdb53ef7-b49f-3946-bddf-8ec2a656f637 | -9.5271 | -47.77762 | 2025-01-25 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a5cb7bf-cfe8-34c4-855d-7a720b012ce0 | -8.11622 | -43.13422 | 2025-01-25 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b1a75083-6237-3e5c-b006-292a5175bad1 | -8.50027 | -43.28897 | 2025-01-25 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ba906589-936c-338c-9f8e-2494ebb90542 | -11.05918 | -45.37843 | 2025-01-25 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ed11791-53fb-3043-8d27-01dad18254f2 | -8.1152 | -43.13182 | 2025-01-25 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d181423a-5d99-3a90-ad3d-3d0c0a64d87c | -12.53478 | -48.31897 | 2025-01-25 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f22bc130-6257-3f08-b73b-8e7dedadc2c5 | -11.05868 | -45.38202 | 2025-01-25 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71f15125-a886-30e6-bc03-84b2240091dd | -10.50378 | -42.42737 | 2025-01-25 04:38:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| ffd69a1a-3659-3940-a7ac-73a7ab370abf | -8.11685 | -43.12961 | 2025-01-25 04:38:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 072ab971-e31a-3a8c-bc3b-777552e70f2b | -12.90486 | -45.08044 | 2025-01-25 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1057f2b9-fdf4-3910-8983-0af6d4cb0913 | -11.27644 | -44.4492 | 2025-01-25 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac8be9a9-c443-3c27-83d5-31141a23d32a | -12.53769 | -48.32351 | 2025-01-25 04:38:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e7fa414-7207-33d9-af81-b1e9e6b1ef7a | -9.59661 | -47.69607 | 2025-01-25 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03f6b9f4-c129-3ba0-a928-c3a79c8df0bf | -9.53059 | -47.77818 | 2025-01-25 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c934e8d-505d-3003-a67c-d1381d31bcab | -12.90699 | -45.09715 | 2025-01-25 04:38:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05b30ea2-af7b-32c7-a342-bcf1885d1fe3 | -11.65047 | -43.91851 | 2025-01-25 04:38:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d243ad0-e075-3c73-969f-1dbdb01dbba5 | -8.46829 | -37.81885 | 2025-01-25 04:38:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0e190f2d-7824-3732-baaf-3af2398c7ada | -18.83792 | -52.49537 | 2025-01-25 04:40:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1893695d-70d1-3f9f-8afa-75f78e2d82ab | -19.16622 | -57.67971 | 2025-01-25 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 3e1be3c9-a19d-37a3-afd5-4d9e599c7acd | -19.05189 | -52.85776 | 2025-01-25 04:40:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 498ec690-e8fe-3e19-810e-c21dafd0cf1e | -16.6828 | -43.88389 | 2025-01-25 04:40:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccec3238-883e-3ee3-b583-e2ad163e5dcc | -19.12311 | -56.22559 | 2025-01-25 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d58826d8-1b68-3a11-98eb-32cce25c3d99 | -16.47882 | -50.5443 | 2025-01-25 04:40:00 | NOAA-20 | CÓRREGO DO OURO | GOIÁS | Brasil | 5205703 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7a2b770c-c303-3f70-9c41-a53f77122fab | -19.05131 | -52.86141 | 2025-01-25 04:40:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2dd1bc41-4d69-36f2-be67-8b857680d356 | -12.50565 | -54.57919 | 2025-01-25 04:40:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 313cd4f0-24d5-3949-ac6f-8dd3c7094078 | -19.51235 | -54.31033 | 2025-01-25 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c80430da-addd-3f28-bcc6-5d3d1decfedf | -12.23555 | -54.3138 | 2025-01-25 04:40:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4d93448-7c00-3def-80ba-42e3de412838 | -15.07877 | -48.94595 | 2025-01-25 04:40:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93a62c4d-d5ec-3c95-a393-a161dabb8bc4 | -19.37387 | -53.55744 | 2025-01-25 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9337955d-0b35-3b66-8527-96e287ad66b7 | -12.28059 | -57.76766 | 2025-01-25 04:40:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07302c63-8b02-31fe-85f6-9e47684abe45 | -16.67796 | -43.88317 | 2025-01-25 04:40:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd120ac6-20bf-3ca4-aaec-600fccac56be | -17.99949 | -52.38584 | 2025-01-25 04:40:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8b9bad1d-7560-31c8-9a01-92191be4f132 | -20.79378 | -41.12984 | 2025-01-25 04:40:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b20b600b-c8ee-338b-92d1-2e95e5497618 | -17.01793 | -51.89014 | 2025-01-25 04:40:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90752279-6adc-33fc-918b-b8162153b527 | -19.02085 | -57.62278 | 2025-01-25 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 8f91732b-db38-3564-abc9-3da5e413e12c | -18.0028 | -52.38641 | 2025-01-25 04:40:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a86f2fe-639a-3b8c-bb6d-a64d40a89506 | -19.3772 | -53.55806 | 2025-01-25 04:40:00 | NOAA-20 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe21c356-1305-3986-aa1b-d86de9dd2eae | -19.04844 | -53.44675 | 2025-01-25 04:40:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fadda71-ff3c-36da-8e52-e55675712cbe | -18.00588 | -52.38662 | 2025-01-25 04:40:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d19d1e7-c843-3fab-8282-67d3a886182e | -18.8418 | -52.49231 | 2025-01-25 04:40:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d9f9333-0e49-3ecd-a7e3-256d6a5953aa | -18.84305 | -53.45612 | 2025-01-25 04:40:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README5.md)
