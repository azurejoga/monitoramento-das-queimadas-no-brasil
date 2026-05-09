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
| ba283850-f7bd-3290-aa0f-da349c406345 | -14.90595 | -43.55877 | 2026-05-09 04:29:00 | NPP-375D | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 882b13fc-8078-3fcf-b228-c728f8ac76d4 | -11.77351 | -43.6524 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5c9f2c14-d913-3691-8c79-b641e2a19097 | -12.88414 | -49.33438 | 2026-05-09 04:29:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e84805e6-ccf9-345a-9860-d099b6417af8 | -13.18471 | -52.6846 | 2026-05-09 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d20ec1c8-8256-3b11-ae26-7e324c1ca7e6 | -8.70327 | -49.08982 | 2026-05-09 04:29:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| deb34a11-99f2-39ca-9e64-deb642d2cd89 | -10.72993 | -43.98596 | 2026-05-09 04:29:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df6efc18-7e50-334c-9652-beef82a3f2da | -11.60401 | -54.18389 | 2026-05-09 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2139fcf0-9261-3226-885b-14ba232df852 | -12.86157 | -43.76137 | 2026-05-09 04:29:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dee58fe-6a70-3e97-bc80-5c5b8f0dae56 | -12.49838 | -45.43761 | 2026-05-09 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ebff123-6fd9-3bf3-a9ef-274046be8319 | -10.67151 | -49.70715 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8fd349d4-222a-3a57-83d7-f0a57b5edc62 | -13.88836 | -43.76598 | 2026-05-09 04:29:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca0b8f4e-94be-3c69-9760-22c7961e3c51 | -11.60108 | -47.10538 | 2026-05-09 04:29:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 974b3025-d714-39dd-84d8-c895c51ebc0d | -11.77413 | -44.09573 | 2026-05-09 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d78d4043-72a8-3407-bbc0-920db4ad68cd | -11.98251 | -47.14966 | 2026-05-09 04:29:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad502cb3-b166-3c3b-86ed-4883eff52455 | -10.55187 | -56.3423 | 2026-05-09 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 174e7e10-c3c0-3841-9399-51045190a903 | -11.77068 | -44.0952 | 2026-05-09 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0686dd7-943d-300d-993b-353712ce0df6 | -8.72321 | -48.33403 | 2026-05-09 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2407bed-048f-358a-bc85-da3d4e3955c0 | -11.42299 | -47.09058 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3b60652-2977-3cfe-a292-2228eb33e34f | -11.93923 | -43.38272 | 2026-05-09 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5fd9b601-11ea-3f14-b392-3e90c7243b9c | -11.29407 | -54.76002 | 2026-05-09 04:29:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4db87e64-9ea0-37f0-b93b-6c9ea4da9c29 | -11.93505 | -46.75314 | 2026-05-09 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd464bcb-c3f9-3455-8318-b9d91003c640 | -11.78284 | -43.66199 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2597673b-8b6c-3326-9c63-d23666024266 | -9.45612 | -47.79473 | 2026-05-09 04:29:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61f66f53-3e4a-3aa9-97e3-6f048019b4d7 | -11.98054 | -46.78986 | 2026-05-09 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 431f1719-9dd3-3098-a030-32bb8e38c47a | -11.77702 | -43.65296 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0911188c-7602-3743-80b8-b228897f7224 | -10.09612 | -52.19226 | 2026-05-09 04:29:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49b57e86-6c36-3a42-994c-2d986941770b | -12.13999 | -40.8955 | 2026-05-09 04:29:00 | NPP-375D | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 99126298-f29d-3c81-8377-9ff4a64c7679 | -10.25673 | -47.40147 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56adedf7-3917-391c-9b3e-da2384153f9b | -10.09689 | -52.18786 | 2026-05-09 04:29:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c812c0b-0885-38fc-ae65-5583bed266ac | -14.14713 | -45.39841 | 2026-05-09 04:29:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 716e0fab-2137-3374-a8d5-44aad074314c | -11.79164 | -47.09642 | 2026-05-09 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4587d05-5b51-34f0-a1e9-6d48fd295d05 | -12.85804 | -43.76082 | 2026-05-09 04:29:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0978d66a-c229-34aa-8f49-bedcac7ef41b | -11.94278 | -43.38329 | 2026-05-09 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2127ae7a-e4a1-3c36-aab9-e8b3511924b7 | -11.7794 | -44.0964 | 2026-05-09 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 796b15b5-5980-354d-a860-4178c0b2ef91 | -11.94338 | -43.37926 | 2026-05-09 04:29:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1115ee47-ec78-36c3-bd5c-85d289feb7cd | -12.06416 | -45.29255 | 2026-05-09 04:29:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb1e5303-9226-3e0e-8971-7eff22e617e1 | -11.8233 | -47.33527 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ead04831-2d13-3186-8f6f-da819047fae1 | -11.60893 | -54.18491 | 2026-05-09 04:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4c332d0-8d8b-3ef6-9c8b-137ebc7a1e54 | -11.76723 | -44.09466 | 2026-05-09 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0fc2adc-ee34-33e8-8168-f6c6c7121c25 | -11.77758 | -44.09626 | 2026-05-09 04:29:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ae0e68c9-689d-3ae0-93fa-4f6a141ab9db | -13.08605 | -44.20866 | 2026-05-09 04:29:00 | NPP-375D | CANÁPOLIS | BAHIA | Brasil | 2906105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21427586-9ec0-3ed1-9562-929a19ac8842 | -11.78274 | -47.08754 | 2026-05-09 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bc03b33-72b4-3685-9613-517238b5acce | -11.82548 | -47.34311 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dadb4969-7d91-3ba1-8767-54b514132def | -10.54687 | -56.33718 | 2026-05-09 04:29:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad97a9a7-0036-3cc1-b30e-cfd01e8757e1 | -11.82211 | -47.34255 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d242e88-4249-300c-8b2d-212a2e3fea7d | -14.90105 | -45.18481 | 2026-05-09 04:29:00 | NPP-375D | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 753caac2-2587-3f98-8e2f-c29bcf93fc1d | -10.23738 | -52.22736 | 2026-05-09 04:29:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ec8791d-4c24-38cf-ac2b-2be74aa30c34 | -13.68495 | -44.29007 | 2026-05-09 04:29:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19eb6185-e917-3a03-aaf0-1cca91df2684 | -11.06769 | -52.47145 | 2026-05-09 04:29:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b303f41-4344-36e6-b0d8-02bdd12e6623 | -10.66775 | -49.70648 | 2026-05-09 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 737122f1-b6a6-3748-9794-895ab3a854bb | -11.77643 | -43.65691 | 2026-05-09 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2da39976-9b80-344d-b59c-6347ea6c235d | -11.8239 | -47.33164 | 2026-05-09 04:29:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cbf06ea0-3c89-3b7d-ace7-15a7b2d4746a | -12.49559 | -45.43349 | 2026-05-09 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eabcebeb-b554-39ab-b1e2-3f945bb0579c | -8.72751 | -48.3229 | 2026-05-09 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f3fce2c-2c0f-3d3d-9310-a35c443bb743 | -10.7605 | -44.49755 | 2026-05-09 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 38609b06-a52f-3391-beb4-05ea2223ae36 | -13.66902 | -52.19838 | 2026-05-09 04:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c27d687e-1289-3b12-86ce-bb4e536dc662 | -8.72855 | -47.98298 | 2026-05-09 04:29:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3f6359eb-1a2e-3f58-8c01-1fcafaff0aea | -15.41886 | -43.10918 | 2026-05-09 04:32:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ce9680c6-aee0-30b2-b7ed-8bcbfa393122 | -20.7947 | -41.12942 | 2026-05-09 04:32:00 | NPP-375D | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 951f946f-40d6-3909-855d-13f9381521db | -22.90064 | -43.4884 | 2026-05-09 04:32:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 02e5dd13-012b-380b-a7e6-d9071a2f50a5 | -20.2354 | -46.82412 | 2026-05-09 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 91c02a33-6de6-3230-bf74-7353ec3dc827 | -16.39562 | -48.90026 | 2026-05-09 04:32:00 | NPP-375D | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51ed563e-7aa5-3afe-b115-98de9c894588 | -19.21029 | -44.89333 | 2026-05-09 04:32:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e48ea1a4-1e3a-3c46-af0e-9a37b023f45e | -16.41729 | -54.91703 | 2026-05-09 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 156db208-fe83-3f6a-9189-8a8ab1b4fc7b | -15.22137 | -50.859 | 2026-05-09 04:32:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf1fafde-61f0-3d3d-a59c-007001ce4972 | -19.20877 | -44.89426 | 2026-05-09 04:32:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77562e8b-94ca-355a-a35c-db5c1391ca98 | -18.48428 | -51.68625 | 2026-05-09 04:32:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac1ca7fb-035b-3548-a42a-bad7d299f593 | -21.33266 | -47.0304 | 2026-05-09 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3cd50c47-8a28-3223-a574-10557c68a3fd | -14.00469 | -56.63499 | 2026-05-09 04:32:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c01e31b-2de2-33f6-9136-71096dab192d | -16.35664 | -43.87952 | 2026-05-09 04:32:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| caae1d84-aa5d-3116-8af2-f4eb5b41ed83 | -20.25254 | -46.09805 | 2026-05-09 04:32:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b1977b8a-85d6-3cbe-a48d-f1e4c922b7b2 | -16.41362 | -54.91052 | 2026-05-09 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19e2639c-1193-35f7-9020-efd1791249a6 | -14.007 | -56.62342 | 2026-05-09 04:32:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 229ecae6-9d76-3291-8e74-0a36d8994d03 | -21.33323 | -47.02655 | 2026-05-09 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e44930bc-70a7-35a5-83e9-77b1c578aa50 | -13.99768 | -56.64124 | 2026-05-09 04:32:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd9c26a9-4f51-36c8-9277-27a05b984501 | -15.22138 | -50.85623 | 2026-05-09 04:32:00 | NPP-375D | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| addbf440-90c6-37a0-b420-dcdaf5eaf8fd | -16.41307 | -54.91163 | 2026-05-09 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6ed1a22-9af3-3d54-abae-bcd7e4d67aa9 | -16.41195 | -54.91721 | 2026-05-09 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d064a44e-cce9-30ad-a593-d2e80b031489 | -19.8696 | -48.96686 | 2026-05-09 04:32:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e7806d0-6c3f-3f4a-a698-4d06d61bbcac | -14.00316 | -56.64265 | 2026-05-09 04:32:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcf75b03-c30c-370a-99cf-16bdcbf082c5 | -16.41669 | -54.91815 | 2026-05-09 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f36c530a-4274-32e8-ac68-5485d2b3acc4 | -16.41837 | -54.91144 | 2026-05-09 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86498935-91c3-3f17-a683-e18da5d26b90 | -16.41782 | -54.91255 | 2026-05-09 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8f3eed6-4f06-375b-9219-6712114d4798 | -21.53581 | -47.13851 | 2026-05-09 04:32:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6ce94fcc-3c09-35f8-88c8-d56c1f8eb89b | -18.01276 | -51.80538 | 2026-05-09 04:32:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ddec92d2-2399-313d-9fa8-d51442d83a07 | -20.22575 | -46.81615 | 2026-05-09 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71a218f3-4399-3b74-90e9-7bae3782ad22 | -21.33662 | -47.02712 | 2026-05-09 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 5bde0aae-1bed-3b9b-b9a6-b84caeef9b8d | -18.92392 | -53.22254 | 2026-05-09 04:32:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d41905ad-58e8-32e6-b087-21d58c819a4b | -20.22632 | -46.81238 | 2026-05-09 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 89ce8dfc-c5d0-3ec5-9814-d06c86a80ec2 | -19.86899 | -48.97061 | 2026-05-09 04:32:00 | NPP-375D | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24511e13-ba85-3d44-8d8c-ecedd0d3760e | -18.0773 | -46.37064 | 2026-05-09 04:32:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f8d8ea26-a573-3fb4-8d99-fd57abd60f4d | -20.22974 | -46.81578 | 2026-05-09 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8880f549-3ca3-3b19-b558-69ec6e46421c | -14.00547 | -56.6311 | 2026-05-09 04:32:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 26e6d466-c294-3f4b-85d3-afd7cc8a3527 | -20.22636 | -46.81526 | 2026-05-09 04:32:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 358b2d93-11ac-3a19-a86c-54fbeb886b22 | -21.53243 | -47.13792 | 2026-05-09 04:32:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de277add-7fc5-3c70-99a6-a97f89a4f0db | -22.41114 | -46.61959 | 2026-05-09 04:32:00 | NPP-375D | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b8eb5d97-f280-311f-9393-a0fcdb2bf76f | -21.12174 | -48.63097 | 2026-05-09 04:32:00 | NPP-375D | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6503886f-7f6b-3589-bbb9-3df63d337ffe | -21.33604 | -47.03097 | 2026-05-09 04:32:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 443cae03-ef3a-3bdd-8b29-13a532b0c6ad | -22.4077 | -46.61898 | 2026-05-09 04:32:00 | NPP-375D | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7eac2d39-53c9-3de0-8a65-38e4344aba9d | -16.41254 | -54.91609 | 2026-05-09 04:32:00 | NPP-375D | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
