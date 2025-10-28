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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0cface0-cdb3-3310-be81-5149d02cd172 | -14.08198 | -44.16157 | 2025-10-28 03:23:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7b3c453-80fb-33b8-8051-16355b9600cf | -10.6281 | -42.31055 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 86a248cd-d985-3a7b-863a-5faf86eb3fcc | -12.61509 | -45.08502 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7fe724f-3a30-32ec-890d-dc7d9ce3cb01 | -14.4377 | -44.80456 | 2025-10-28 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5c3d88e-3c17-38ef-9e6c-d01abe24ce09 | -10.62832 | -42.32455 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 94fc9c97-e98b-3061-a09b-02fd1e0f9c60 | -10.88054 | -44.39365 | 2025-10-28 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c75a698f-ef3b-39c5-84d5-810172c621c4 | -10.62639 | -42.3195 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f00f61a4-73ca-3395-973c-5782ac5aa0fa | -12.61924 | -44.2575 | 2025-10-28 03:23:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c6d5a77-13d5-3554-9c6c-be677c78de54 | -10.62505 | -42.30995 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bcab21e5-2239-3dcc-ad42-46e9f681626c | -12.62023 | -44.25313 | 2025-10-28 03:23:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 09485aa3-437d-37d0-9069-e6f114f93845 | -12.07989 | -45.6577 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 192fb769-3472-387e-8ed2-9faade79712e | -12.62033 | -44.25212 | 2025-10-28 03:23:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b942872-aed2-3a7c-b5de-966190179442 | -11.28833 | -45.52214 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 70421f4f-e54b-3121-b3c7-0ccb41e3577c | -11.66841 | -41.32053 | 2025-10-28 03:23:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5258d766-2606-33ed-8b8f-68a1bf03b77c | -10.62554 | -42.32397 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 5baf78e5-309c-30af-a9ea-af38774388ba | -13.4465 | -44.10363 | 2025-10-28 03:23:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 32e9b5c8-89ad-3cc1-8123-b6eb01ee9a1d | -8.62582 | -44.80014 | 2025-10-28 03:23:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11ee81ed-617e-3c57-a727-d5def079aa09 | -14.08304 | -44.15655 | 2025-10-28 03:23:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2e6e6cb-1cc9-30a1-80da-d150213c0c94 | -13.62786 | -46.47437 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d6b3eba-032d-3c2c-a8d5-8cab92cc7f59 | -12.0779 | -45.65277 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a53bc25-2097-373c-ba03-7e651ba9fc7d | -12.63011 | -45.08839 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 14894442-4687-31a6-a852-9bcf20ff8a08 | -11.10043 | -44.02463 | 2025-10-28 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dba933c2-40cb-33ef-bd12-d0ec16010993 | -12.62468 | -45.08088 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 237dcdbb-3382-3301-98c1-ccdb513665e5 | -11.66814 | -41.32114 | 2025-10-28 03:23:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a8baf343-53dc-36c5-b806-ed223ec191f1 | -13.78771 | -44.34473 | 2025-10-28 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd7f9365-d3ea-3ddb-aeee-a11cd561b02d | -11.27763 | -41.0705 | 2025-10-28 03:23:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a11278ce-e965-3140-8bc6-b0248c2f9f89 | -12.08539 | -45.66645 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| debc29ca-371e-3b5f-a40a-119293302ea1 | -9.52044 | -40.31395 | 2025-10-28 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6541347a-1117-3c98-823e-b4cd5782fc41 | -11.28415 | -45.50657 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| ef427bce-5893-3b56-a7fd-f5deab20a4c3 | -8.62844 | -44.80442 | 2025-10-28 03:23:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fad00f0c-0234-3728-90b4-2aa595d64966 | -12.6164 | -45.07879 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b115a655-0753-3810-9f18-6d5b2df33eee | -12.62984 | -45.08189 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f1f97f0-b1b8-3d6e-bb1d-fb9251ecdabf | -10.82986 | -44.96394 | 2025-10-28 03:23:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ae2c0f2-54c9-35e9-b7c7-b59ae4872177 | -10.63097 | -42.31116 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7db996ec-4f56-35ba-a966-0854f3659a33 | -12.08391 | -45.67351 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16e076fc-af69-3451-b859-c7afef5ff04f | -9.51449 | -40.3163 | 2025-10-28 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 59e8e7eb-b981-36cd-864f-5d0b2ca3c7e5 | -11.27235 | -45.51037 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ed300717-e1ab-31d0-aed8-6ab37dbd39a2 | -12.0834 | -45.66131 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56659567-f30a-3fec-9944-119c6cf740e7 | -14.05622 | -44.40882 | 2025-10-28 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9a9b8fb-3f71-3bbf-910f-0186e8db09b4 | -10.88315 | -44.39455 | 2025-10-28 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f138842-1cfe-3661-a4b4-e71a20635a49 | -12.5524 | -44.93754 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db0c2898-69f3-3096-87ef-edcca4d66e40 | -9.01284 | -43.97959 | 2025-10-28 03:23:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c83adaf0-f5d3-320e-abd8-e3d813b5b26d | -12.08688 | -45.65935 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68c87ab1-515e-3e4b-9ceb-1cb1b6c62f5a | -11.27386 | -45.50328 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3cc12044-52ed-36c6-ab6a-0fa5315cd6c6 | -12.18902 | -43.5921 | 2025-10-28 03:23:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 71990e83-c66e-374c-a071-d0cb773035e5 | -12.08584 | -45.68405 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bfb23ad4-5495-394b-b4af-8aca294fe208 | -8.63435 | -44.79417 | 2025-10-28 03:23:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da6607de-f483-338b-876b-088cf4b4354d | -12.6138 | -45.09118 | 2025-10-28 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d9525223-7a15-31ae-a20b-f0d37af3992e | -12.6191 | -44.25851 | 2025-10-28 03:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 633c0803-0a4e-3295-b65d-cf238ebbf0e7 | -11.27569 | -45.51189 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 5dfe8090-8870-3f59-a6d3-1231151b07f3 | -13.37687 | -43.45923 | 2025-10-28 03:23:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| faa647e4-772d-36ef-93d8-b925b94dc893 | -10.6292 | -42.3201 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 1f9cf788-b8c5-3d43-bfd6-f78579cf87fb | -14.43849 | -44.8008 | 2025-10-28 03:23:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 984d6407-e75f-3919-8bb0-cb84c1c07c8c | -12.08247 | -45.68041 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1ccc8927-eaee-3736-8723-72109d58c9e5 | -10.62725 | -42.31502 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c254d80c-6fd4-3748-ac23-06f1736f06a3 | -9.00806 | -43.97918 | 2025-10-28 03:23:00 | NOAA-20 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea25b35b-4f96-3b61-85ee-8bab614b35de | -11.33231 | -43.18976 | 2025-10-28 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f3dce82b-d37c-39ef-a1c9-7c9749a6fb49 | -12.08134 | -45.65077 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e047afc8-edf9-3b16-ba91-c2353fe7972b | -11.28496 | -45.5205 | 2025-10-28 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 892dfed9-44b5-3ac4-8d23-d92a193faf9d | -13.55222 | -44.2715 | 2025-10-28 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23d80337-d5f5-3f70-9d55-af1b81e97916 | -9.51513 | -40.31292 | 2025-10-28 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d1f5cd8c-c0a8-30d9-b031-62a5771a42c8 | -13.78658 | -44.35006 | 2025-10-28 03:23:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 931285dc-2673-39b7-89e8-1d256da7669d | -10.63147 | -42.32519 | 2025-10-28 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d50c65f7-171d-3222-ad9a-1dabf5f82531 | -11.10157 | -44.01901 | 2025-10-28 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f7fe3f62-207b-3605-bb61-67918df88995 | -12.08491 | -45.65436 | 2025-10-28 03:23:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 643bb261-7404-3bd9-a22f-04f1f21cc843 | -16.1423 | -45.10259 | 2025-10-28 03:25:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 496404e1-5858-3bd1-8125-3af7874e804e | -19.83546 | -42.88294 | 2025-10-28 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 3ba89f74-4004-31e7-b10c-d8334f6c1ae5 | -18.24592 | -44.19434 | 2025-10-28 03:25:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8702db8c-0a1b-32b3-be06-196d5d8b7f01 | -18.81905 | -43.2277 | 2025-10-28 03:25:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 7ff32e6b-a83f-3b30-b0f7-970411a95e4c | -14.75489 | -44.96043 | 2025-10-28 03:25:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9737e866-a9bd-32f1-a8de-c4a5872f884f | -19.83499 | -42.88639 | 2025-10-28 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1e195a56-1313-3689-b7da-ef05cb91a077 | -20.14718 | -42.40543 | 2025-10-28 03:25:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5fa96273-8ae4-349f-ab1a-9d99070c41b6 | -15.19911 | -43.78448 | 2025-10-28 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cf75c14-6fd4-3950-82d3-631b1f0d93d9 | -20.13476 | -42.41483 | 2025-10-28 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c50a2485-d842-3d37-a31a-a8e165b36208 | -15.57495 | -43.20672 | 2025-10-28 03:25:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 10ef1cc6-c5b5-3778-bd88-9f87a4980125 | -15.14619 | -46.59501 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 858030e0-4f1c-3fae-a8f0-65d86cd016a6 | -20.13987 | -42.41543 | 2025-10-28 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0a36f183-49d4-3047-8232-801c2c7486d0 | -18.04996 | -45.09932 | 2025-10-28 03:25:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f7f9ac05-d529-355e-8412-55c060d89277 | -15.14782 | -46.58781 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 953a97f6-e087-3052-8f8b-e26c7b6f4f60 | -18.14183 | -44.17685 | 2025-10-28 03:25:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4f8fe208-a224-38e8-8b11-eb81a7cab5e3 | -18.14134 | -44.17596 | 2025-10-28 03:25:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fa77c7de-26e8-3709-ad36-432c6fcfad63 | -18.05524 | -45.09946 | 2025-10-28 03:25:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1af91c47-7d5d-3341-938e-dea262a68470 | -20.09923 | -41.44909 | 2025-10-28 03:25:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d79444e8-33cb-3779-bf8f-40a71fc84f4b | -17.68797 | -43.95794 | 2025-10-28 03:25:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d33c4e8a-42b0-321f-8011-92ce899a4b85 | -15.14268 | -46.59155 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f861dd5a-e6d4-3162-bb53-bab82d0a67dc | -19.02964 | -42.03602 | 2025-10-28 03:25:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f05b6f3e-95c3-39fc-bd2c-6e1a204f796e | -14.76655 | -44.96907 | 2025-10-28 03:25:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80610f3a-74f7-31ab-a8b7-016536a4cb8d | -20.14614 | -42.40564 | 2025-10-28 03:25:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e18b7446-b82f-3db7-b692-4246dc44680e | -17.6258 | -43.99615 | 2025-10-28 03:25:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 410dda18-8782-3bcb-8d94-fb88bc9790b8 | -15.1537 | -46.62696 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dfcddbda-f23e-337c-affb-4ef4660d363a | -20.14661 | -42.40821 | 2025-10-28 03:25:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 07a06880-08a7-3e94-a916-da50a14897ee | -20.1314 | -42.40578 | 2025-10-28 03:25:00 | NOAA-20 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 676a91ab-61d6-3a73-9786-83bcb0173b99 | -15.14944 | -46.58068 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 744b7535-0578-35eb-b233-828bacc22d8b | -15.1445 | -46.60244 | 2025-10-28 03:25:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 85fca2d8-6398-37e3-accb-e233c4a20e72 | -19.02028 | -42.03073 | 2025-10-28 03:25:00 | NOAA-20 | ALPERCATA | MINAS GERAIS | Brasil | 3101805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5f68a4be-d2b1-3037-a9b3-1034c5476689 | -19.82478 | -42.88332 | 2025-10-28 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c257bbc3-76ea-3ebb-bcdc-dbfe31249582 | -15.19641 | -43.7876 | 2025-10-28 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f53def8e-d45a-3bc5-86d8-97d28c63c7ea | -16.04646 | -43.54179 | 2025-10-28 03:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb86578a-cf44-34fc-92ef-67b4c54ebf5b | -19.12303 | -45.69685 | 2025-10-28 03:25:00 | NOAA-20 | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3be6e57e-c080-3144-928c-821766327276 | -19.82915 | -42.88824 | 2025-10-28 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |


[Clique aqui para ver as próximas entradas](README12.md)
