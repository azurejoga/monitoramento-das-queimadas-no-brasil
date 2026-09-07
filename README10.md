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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a63ca82-aa9a-3d56-9dbc-8feca5178e1f | -9.73638 | -43.41687 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a01686bb-6110-36f6-8339-2cb39bdc4312 | -13.46264 | -48.51549 | 2026-09-07 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 457c0970-4180-3271-a8f6-49102135b287 | -9.72885 | -43.42264 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f1e53b8c-47c7-38ce-a595-016392a4f884 | -9.74212 | -43.41486 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a033de05-66d5-30dd-8083-c66e6a23a81d | -9.93178 | -48.05284 | 2026-09-07 03:45:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| faea853d-e633-3408-8385-c33235b295c0 | -9.72733 | -43.40806 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| eacd35a7-04bd-3cf2-9b7d-d08d2fa5ba4b | -13.45062 | -41.89346 | 2026-09-07 03:45:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 95e0e3eb-8d9b-3d05-b7b4-a70026c4160c | -11.03904 | -44.34411 | 2026-09-07 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| deeda0be-6233-3d2f-b926-fe1e2bb42352 | -9.72602 | -43.415 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9eebad1b-49af-38e1-832c-18d320e74f8f | -11.94188 | -44.86209 | 2026-09-07 03:45:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 572595cc-604d-3dc1-a140-52932977954e | -9.73395 | -43.4298 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 6b01f6c2-a250-37cb-ac6c-6c72310c66e2 | -11.33375 | -45.09708 | 2026-09-07 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b3c9eda-7be8-3ec4-bc93-37ce215e4fc7 | -9.72799 | -43.40453 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4f5910f8-f660-360e-8b9e-1a32babd7b08 | -9.74622 | -43.39299 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9a635ebc-dca1-3f7d-be7e-7d2e3526842d | -11.32204 | -45.06717 | 2026-09-07 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0dae6523-1589-3bb0-be11-fedbac03f088 | -9.74053 | -43.39481 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0b16676f-d443-3c19-90f8-70213bfd9754 | -9.7354 | -43.39362 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d9a5943a-d661-3108-9402-92510be36dbd | -11.03368 | -44.34295 | 2026-09-07 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f398f8ca-ec8e-3dbb-acd6-a6039d21860e | -15.93563 | -41.98346 | 2026-09-07 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 44ed52a3-2f65-3414-8c7f-f602aabcb156 | -14.53835 | -40.32244 | 2026-09-07 03:45:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e453c007-a205-308a-bf18-6b1554cae7ee | -11.94216 | -44.8615 | 2026-09-07 03:45:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b16f16f7-18b9-341b-9c43-999b075c3ee2 | -11.32875 | -45.09282 | 2026-09-07 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de9cb7d8-21d4-3e71-b6d2-642a22bda73f | -9.73249 | -43.40242 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3817e959-068a-3aa5-9f18-e867a3792ed2 | -9.73651 | -43.38775 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5ec8238e-a2bc-3c5d-af78-452159df36d3 | -10.89891 | -40.41136 | 2026-09-07 03:45:00 | NOAA-20 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0bc004cc-90ec-3c12-8d0c-839370facda1 | -9.72427 | -43.41836 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d7d79cb1-bd40-3322-8d66-3a33050353e8 | -13.44697 | -41.8886 | 2026-09-07 03:45:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 60311e01-3c56-3546-88ab-7e2ca64786e7 | -9.73304 | -43.3994 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d78daaef-c466-38e5-ae3a-4d833ce3c4ed | -9.73129 | -43.40908 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 126e9364-ba0e-3ac1-969a-1dfb3489c6f2 | -15.9314 | -41.98269 | 2026-09-07 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1bd81a9-25f8-3a9e-8f8b-f3b971674609 | -10.73843 | -45.08116 | 2026-09-07 03:45:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6c11f640-e265-329b-84e2-245ba9e39936 | -9.72995 | -43.42258 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6d2d26d4-1874-3d52-b210-5df9f4121682 | -14.86604 | -40.91569 | 2026-09-07 03:45:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cf0f1c9a-32c2-3619-95fc-fc6b6255f2cc | -13.84801 | -43.65321 | 2026-09-07 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| db3d6c07-ee1d-3e81-9dea-93e30cdafcd2 | -9.72487 | -43.41503 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c038122f-176c-3795-b3e7-c55096c503f2 | -9.73699 | -43.41362 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a889dc20-3aa9-3ed1-b2d5-c88f50375c1e | -9.74783 | -43.41293 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 83e157ad-4c7f-3b42-b923-e2d73662d30a | -13.30913 | -45.23992 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| bc2b94fb-0edf-3bb2-a6eb-806c09052978 | -9.73761 | -43.41035 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 28388c08-7840-3868-b2f1-4db0c29a2dab | -13.30987 | -45.23619 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| a16223d8-6486-3c3d-80e8-308bf6d7fc65 | -9.73577 | -43.42011 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 0dccd7f6-da85-3434-80c8-89c1dc14f72a | -11.3315 | -45.1088 | 2026-09-07 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 210f5ae6-627d-309f-a641-ad665bf2fbe2 | -9.73183 | -43.41257 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c0314c3-df1e-3b7f-b4bb-8ae9ffcc081a | -9.74271 | -43.41171 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| ab99f8fc-aaad-3310-a2e8-325f35b40e3f | -13.3066 | -45.2241 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d59bb3d5-0bb3-349d-9721-8f7c6c3185fe | -9.74389 | -43.40541 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 24b0938a-9d13-35dd-8268-50ec39d2d769 | -13.30368 | -45.23871 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| d381d2b9-2a33-3c66-8f32-bc3b61fa5570 | -10.7335 | -45.0763 | 2026-09-07 03:45:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 564ad594-8d8e-3472-bebd-279359620f87 | -10.73919 | -45.07726 | 2026-09-07 03:45:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 92a4f2c1-f7ae-3008-adbe-e60fdecbde2a | -9.73996 | -43.39783 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 64b7c82b-a437-3410-b017-3f594f7d7078 | -9.72611 | -43.40814 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 067e1b5d-f502-3bd9-82b6-35fc2384946c | -15.66935 | -42.10316 | 2026-09-07 03:45:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 553bebd4-28d5-3ae8-b6a8-2c85a3e889f5 | -14.86538 | -40.91932 | 2026-09-07 03:45:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d9969fe7-bd7a-3723-84b9-56a786b80f7f | -9.73192 | -43.40561 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7ec276d-4699-3b8e-9830-88e875cfb9da | -9.73456 | -43.42656 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 2b4e994d-62ea-3ee1-bc7e-a61fff9d09f1 | -9.74109 | -43.39182 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c9d2f2bf-1eaf-3371-80a0-461d0290f48b | -9.73248 | -43.40914 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5d0b341-8521-3228-8564-8b53f8f253fd | -9.73005 | -43.41597 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8d5ee5e-9ee3-3c51-bd69-7eb3fcec8276 | -9.72826 | -43.42588 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7f54246c-87d4-3bde-8436-6a8ec840f537 | -11.33079 | -45.11254 | 2026-09-07 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b3a080e-8fbb-3840-8e6b-b207250edfc3 | -10.73275 | -45.08015 | 2026-09-07 03:45:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 183b85ef-c32d-3bcc-9a5b-67e59767dac7 | -11.32228 | -45.09619 | 2026-09-07 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b3ef18e6-b7e8-377b-bd82-3f65de3ecabc | -11.33299 | -45.10106 | 2026-09-07 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 195e0447-2edb-3462-8790-e2c78c7597dc | -9.74447 | -43.4023 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d2f7bee-db3f-36a9-88a0-b9e3c4ad1f24 | -13.30442 | -45.23502 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 62719465-7572-3ecd-8d37-dad1d958ccb9 | -9.73066 | -43.41257 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac5f376b-a7f3-3d2f-83bf-b980cac6b1e5 | -9.74564 | -43.39609 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e9accbe5-7e14-376c-95bd-016327b79346 | -13.31133 | -45.22887 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 39675667-103a-34e3-a823-e52a79de7fe8 | -13.46576 | -48.51847 | 2026-09-07 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a221674b-a023-3c47-aac8-c7dc32deb518 | -9.73939 | -43.40084 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6af7ca5a-f5df-3b7b-b4fc-7fa4726fa8a8 | -9.73372 | -43.40253 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a66ae5f3-ab0d-30e6-8911-4073a206d394 | -11.32796 | -45.09694 | 2026-09-07 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35f14729-7bbf-383b-808d-46577a64f5a1 | -13.3106 | -45.23252 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 6fa1e066-2592-3c0a-bc52-2d23399e157b | -13.30515 | -45.23138 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 69bce041-9179-3072-afac-7f206c60f3ab | -9.73313 | -43.40572 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5110fff8-e402-3afc-b25e-3a9c13904276 | -9.73057 | -43.41929 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f7eae79a-082f-3ac6-b105-eeb4b92509e1 | -10.73766 | -45.08514 | 2026-09-07 03:45:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 47b72d8d-17be-37c6-93d0-de38239568ac | -9.72666 | -43.4116 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f2a47e22-2c87-366e-82c8-9bcf32f5f25a | -9.74166 | -43.38881 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f14ec8e1-796d-3c80-909a-cf77a4a01442 | -15.93215 | -41.97859 | 2026-09-07 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e139cf51-6b68-3f7e-9f49-66e6b0ffaa5d | -13.30838 | -45.24368 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e555f66b-fccb-3b38-a2ca-6ddce7995f41 | -9.72674 | -43.40466 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5f74ff94-7ad6-36b0-92bc-f64599ac6cb4 | -9.7433 | -43.40855 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e044d73b-7259-3047-b37e-518c2912dbe4 | -15.93638 | -41.97935 | 2026-09-07 03:45:00 | NOAA-20 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 51.5 |
| bf14fe8e-6a58-32f8-aaaf-5f0396aba052 | -10.89957 | -40.40757 | 2026-09-07 03:45:00 | NOAA-20 | SAÚDE | BAHIA | Brasil | 2929800 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c358209f-2327-3d15-a1cd-057a3f4e141f | -9.73517 | -43.42334 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| b9330fc4-959f-3d66-a968-0b89bf594e41 | -13.46948 | -48.51595 | 2026-09-07 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3663efb3-23db-3e58-b8b2-e00f4e303ca9 | -9.73429 | -43.39952 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bb6c82a-e368-3d44-8e8d-6b1396e4d8cd | -9.7312 | -43.41594 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfc18955-31d7-3d6d-a593-822dd122b2a1 | -9.73822 | -43.40709 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5d8d174f-22e6-30e3-b03b-4beddeaf6155 | -15.47005 | -43.87431 | 2026-09-07 03:45:00 | NOAA-20 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0aafb864-332f-32cd-bf25-06729e8874c5 | -13.84909 | -43.64762 | 2026-09-07 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2b301d53-a20b-3901-99d3-0841be8a1f93 | -10.37199 | -45.0166 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29219d77-c425-3202-9b34-9ca5d6d2db6a | -9.74842 | -43.40979 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| f52b2520-37b3-3abb-94c7-4af4ca3e80dd | -9.73411 | -43.3935 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 02f8e506-22dc-3fda-b931-c17feeeb38cc | -13.46723 | -48.51171 | 2026-09-07 03:45:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 970e136d-695d-314b-819a-fe2690ee3bb0 | -9.73358 | -43.39643 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fcfec91-3642-39a8-bde2-bb0f53a111ca | -9.73882 | -43.4039 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0f003040-95da-30e8-9c40-5ffc973adcf5 | -13.30587 | -45.22774 | 2026-09-07 03:45:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| a76703f1-1426-34a1-81dd-14c5f8dfb660 | -9.73516 | -43.38765 | 2026-09-07 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README11.md)
