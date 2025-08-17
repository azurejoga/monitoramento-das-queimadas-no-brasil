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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51ec124f-79ff-32a4-8451-e370eac23f02 | -13.43846 | -45.88091 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a598687f-3497-33eb-9c1c-ffb02e5e54b2 | -10.8508 | -45.3403 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 62ec07bc-188f-3501-81c6-25e1b96f6bea | -14.93686 | -47.05896 | 2025-08-17 03:25:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cb1e32d3-148d-3577-8464-72fb2f7681d5 | -10.85278 | -45.33651 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.7 |
| a0f8daed-b103-3e2d-a0f2-fa2cdb13a05c | -12.82116 | -38.41896 | 2025-08-17 03:25:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| df6f1efd-2918-3ad0-abed-e8692c0e8ba3 | -13.8762 | -45.55193 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 875eca1c-5ed4-37b9-9191-06cfff607b0e | -15.53265 | -42.35141 | 2025-08-17 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df3230e2-82a9-345e-802d-3dfd949f2092 | -10.83484 | -45.35366 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| fd19cbc0-d205-3cf6-aa3a-07e9116f551a | -11.09676 | -44.81282 | 2025-08-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ce6d468-f902-3269-995b-8383f2725981 | -13.01852 | -42.326 | 2025-08-17 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 9e7dba7c-b0f1-3e6e-9ce3-99e748480f3e | -13.43436 | -45.9002 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 88336487-16d0-3044-bf35-1fe4c7c3637a | -10.85357 | -45.32708 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c849fdea-6809-36b2-8c6a-b35d3ccaa7bd | -10.84107 | -45.35219 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 0b3bf77b-5904-3bfe-94c4-fe9e9fb1798f | -10.85499 | -45.32031 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a47e67b4-2706-3209-8473-ce5088ea4d36 | -10.84033 | -45.32674 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9f24463-cb51-37cc-9eda-866f20272172 | -13.87746 | -45.54609 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49367c36-66c3-3c6c-b47a-c99f3744ed5c | -13.01775 | -42.32985 | 2025-08-17 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 7ad8a411-fb00-3432-9ce6-e2d8d173f2f1 | -11.89927 | -43.43197 | 2025-08-17 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5bb8aa7e-f3ef-3f6e-8d11-aeb44d527ee4 | -14.93522 | -47.0662 | 2025-08-17 03:25:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4b4e6e0e-26fb-3761-b2a7-9be671c8b7b1 | -17.62504 | -39.92807 | 2025-08-17 03:25:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ed24582-4feb-36c7-9e3c-78b8e1e026c2 | -10.83966 | -45.35888 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| cfdcd160-2c53-3f63-a0a1-fb5cd4b08289 | -13.43709 | -45.88734 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b7021d97-1da6-372b-94d9-5a76efa8d4d3 | -10.8327 | -45.35757 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23053565-0a70-3957-8068-daaee598278f | -15.52348 | -42.34169 | 2025-08-17 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c1bbc61-b010-341d-9e6a-262a2f854205 | -14.18414 | -45.31496 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e2c9caa-bbd7-31d2-98a8-e8f66fa492f0 | -10.83818 | -45.36594 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 9d8da697-378d-3afc-be22-cc8d0fde07fa | -13.42918 | -45.8926 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 0e5ed455-5c0b-3582-bc13-43881df11fe8 | -10.82367 | -45.33761 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d39c82f-ece0-307c-bcce-f6eaf4f1d0e5 | -13.44393 | -45.88882 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f0214fe4-b94b-3d7f-9c25-73a42fc16e89 | -10.85218 | -45.33372 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 57ee9b6c-544b-3778-acc3-f03f68b5b6d6 | -13.43462 | -45.90049 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 6da8c849-9f03-3b7a-b290-4a5a883ecdca | -14.19297 | -45.33049 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a4e2113f-ab51-3266-8fdb-5b19c2073147 | -10.84389 | -45.33879 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 965e6ab7-57bd-3ff8-9ca8-a93e3a14b919 | -12.89145 | -46.12284 | 2025-08-17 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| b1722478-14c4-3cec-ad80-dd0bce04df06 | -10.84042 | -45.36175 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 37779616-da60-3ce3-aa46-d95eb883c0ed | -15.52277 | -42.34518 | 2025-08-17 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d79add4-ec80-3331-9d2a-1e94a7a3452a | -10.83347 | -45.36039 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.3 |
| 9d4cf5df-d506-3737-9d2d-a8495c2b22bd | -10.8355 | -45.34431 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 04390e5d-0a41-3275-a77f-1b96bbe82670 | -11.094 | -44.81186 | 2025-08-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f82a66e0-8b65-35d5-acb5-225144c9ef35 | -14.18769 | -45.3233 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 66fa9912-67b6-371d-8dc6-c1257ff74f5f | -10.86045 | -45.32872 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 9fe0e3a7-f4b3-3dcf-933c-4881e59b7a72 | -10.83145 | -45.32922 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eca97cd3-c0c9-3990-87a5-103b821804a0 | -10.8555 | -45.32312 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 68650f12-36c1-3319-a75b-63e9ca2b2d0e | -14.18945 | -45.32218 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5394d619-d585-3edd-87e7-7ce57478a38e | -10.84453 | -45.34159 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a7ff8552-0950-3f72-be0d-4ad3183e2d53 | -10.84316 | -45.3483 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 6e9cb20c-16af-31dc-9636-c09525321e8a | -15.53338 | -42.3478 | 2025-08-17 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 347ec042-ab8c-3a65-86c3-26a98467407f | -13.43573 | -45.89377 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2b60fa19-1fb5-30cd-99d7-e41a1db0c148 | -10.8418 | -45.35499 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 97440ff2-43d7-378d-8503-92b9b1090ca0 | -15.52807 | -42.3465 | 2025-08-17 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23fee0c9-48ea-3095-bf49-9767c463d354 | -13.43883 | -45.88124 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1fe9d0fe-06f7-316c-b87c-95b13480b18e | -13.01296 | -42.32474 | 2025-08-17 03:25:00 | NOAA-21 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 83ad6c8b-ea5a-3383-9eee-0eea98830526 | -15.52878 | -42.34301 | 2025-08-17 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4da6547e-85ef-360b-abac-bff1d5342f4e | -10.83897 | -45.33343 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5575217f-a821-3ad8-b698-10ef342c25a8 | -14.18642 | -45.32912 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4498a1a4-8ebd-3bf6-95cc-12a028b4ed38 | -10.84247 | -45.34552 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 01c1ad48-d86d-399c-bee1-85560722e142 | -10.83425 | -45.31596 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f5d3c0be-ef13-332c-a652-0c413cd859c7 | -14.18823 | -45.32794 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c88b14d0-6af5-31c6-816a-1779f3b5e107 | -12.89001 | -46.12949 | 2025-08-17 03:25:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| db0c89a7-77fb-3181-ac9c-044a4b3b6f66 | -14.18894 | -45.31762 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d7badb7-289c-362a-ab55-e14ee1cb7a46 | -10.83837 | -45.33067 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4aaf5259-6aad-328e-831f-38393a444570 | -10.82511 | -45.33057 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8948359b-02a4-3269-bb9f-f9b220d6761d | -10.83619 | -45.34707 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 917e6c69-1807-3a7c-bff7-27bf154caebb | -11.0901 | -44.81123 | 2025-08-17 03:25:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35a5813a-eb89-3f4c-9aa8-0bd514a859ae | -14.18698 | -45.33381 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 104c17d5-1731-32c2-a5d3-b2e5a77604e2 | -13.42889 | -45.89227 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3bf94355-4ea0-3cb1-b416-83a62f21dfc8 | -10.83285 | -45.32257 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00f16a99-dcfd-306a-9e54-2a0c98323236 | -13.47554 | -44.07993 | 2025-08-17 03:25:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05ffd3ed-f01e-3592-9aa7-015cbd37e3a8 | -14.18241 | -45.31616 | 2025-08-17 03:25:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f92adbad-4f2f-341c-b3aa-af6fa2281dc8 | -10.8341 | -45.35095 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19b8a9ee-4105-38ae-8525-9e063495c218 | -13.4453 | -45.88238 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 99f4af00-ca41-3be1-a5cd-565ebdb7b4c8 | -15.52947 | -42.33957 | 2025-08-17 03:25:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 02534bdd-6099-3028-b827-cd3e69f77788 | -10.85412 | -45.32992 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 87fdd4bd-099a-3c8f-9775-1e640e6bee4c | -13.43743 | -45.88766 | 2025-08-17 03:25:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 42a24841-19e0-302d-871b-9a5ead8e401d | -11.90022 | -43.42717 | 2025-08-17 03:25:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b79e1a9-ec7f-3dc9-bb8d-ddded735446e | -10.83342 | -45.32525 | 2025-08-17 03:25:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7e36d0d0-5578-3a10-b248-661fe37b6b8b | -18.06503 | -46.35621 | 2025-08-17 03:28:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61735abd-6d3b-313d-b118-3d82d34e13bc | -19.77748 | -46.04508 | 2025-08-17 03:28:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e542d49f-1c8e-3561-8066-c5304a935272 | -20.29369 | -42.20604 | 2025-08-17 03:28:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 8faeed12-d865-387e-be4e-e2b1957012ed | -17.96927 | -42.9866 | 2025-08-17 03:28:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| cb847bd0-885a-3684-a012-30384253297b | -18.96038 | -43.74403 | 2025-08-17 03:28:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fc4d441-c9e4-36a5-89d9-f7e2b38df281 | -19.16788 | -46.5794 | 2025-08-17 03:28:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ce9de265-8479-34d7-9861-dc23658f36b4 | -20.29251 | -42.21189 | 2025-08-17 03:28:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| f72ab486-91fa-364b-b3d2-4e1360c1820c | -17.92983 | -44.37613 | 2025-08-17 03:28:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5a53503-1dce-3a19-8ee0-43c9d67f7b17 | -18.62378 | -40.00798 | 2025-08-17 03:28:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6bfef5c9-246f-370b-9fa0-086940dcdc69 | -19.06588 | -42.72178 | 2025-08-17 03:28:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 536a9a0f-103b-3ca5-99ca-c45e15d7c438 | -19.7837 | -46.04626 | 2025-08-17 03:28:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3934ff6c-65b7-3380-b2e5-e38eee99df70 | -19.77935 | -46.04325 | 2025-08-17 03:28:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1584fa48-bc35-3ed7-8ecb-78517660c8cc | -18.95942 | -43.74855 | 2025-08-17 03:28:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72d25720-2bd9-3447-b256-2179293ec7e1 | -19.77829 | -46.04795 | 2025-08-17 03:28:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2d3a8fae-0b51-3888-9555-5a6ebc7426e9 | -19.67878 | -41.98405 | 2025-08-17 03:28:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a6111a64-3ae8-3bb2-9591-7a9118441f79 | -20.29035 | -42.21283 | 2025-08-17 03:28:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f039500d-d781-3e45-a940-53299c1dba93 | -21.35636 | -43.76515 | 2025-08-17 03:28:00 | NOAA-21 | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a53ecd11-9d50-3c00-b761-36dadde2841f | -18.96563 | -43.74623 | 2025-08-17 03:28:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 323a78c4-adde-33ce-b4c7-b97677f38141 | -18.06441 | -46.36043 | 2025-08-17 03:28:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e97bb847-eb31-335a-819e-62df425d0488 | -18.88928 | -44.77486 | 2025-08-17 03:28:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 997eba2e-8c16-3005-b823-c2ca1b2214bf | -19.78449 | -46.04917 | 2025-08-17 03:28:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fea43e97-01f1-3ea7-9b2f-1a19c626285b | -19.16034 | -46.5827 | 2025-08-17 03:28:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba9cb7cb-3968-34b2-af42-6e899a7fa52f | -19.06074 | -42.72075 | 2025-08-17 03:28:00 | NOAA-21 | BRAÚNAS | MINAS GERAIS | Brasil | 3108800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8de00196-8b54-376a-92fd-870baf624865 | -18.88819 | -44.77515 | 2025-08-17 03:28:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README10.md)
