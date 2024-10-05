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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2d65674-0062-33ff-aff4-3c68ed6f05f1 | -14.04091 | -45.18 | 2024-10-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 7c7dc8ef-5955-330b-80e0-1450afc08079 | -14.04009 | -45.18444 | 2024-10-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| fbde38e1-62af-3563-b23e-0f0a54cce59a | -14.03926 | -45.18893 | 2024-10-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3a3c0998-b429-393f-bf6c-71346839bd00 | -13.99359 | -44.03029 | 2024-10-05 03:51:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b18ae8a8-1028-3ee4-bf1e-63eaebfe81d7 | -13.9929 | -44.03408 | 2024-10-05 03:51:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d93ce5c-3c1c-3f83-9f5d-b1ad8b4a4d71 | -13.39694 | -48.08721 | 2024-10-05 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 75931984-d51f-34d6-becd-1e033af18000 | -13.52983 | -48.60427 | 2024-10-05 03:51:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cfa60127-4e98-38f5-91ec-3d343a133230 | -14.0477 | -46.36423 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e8cec41-50d1-3013-a60d-7b74e1597152 | -14.04671 | -46.36948 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4deb5a63-b807-3c50-a10d-5a330d760269 | -14.04567 | -46.375 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7edc0bba-9a87-3079-bace-1ec4d6823b9e | -14.04294 | -46.3632 | 2024-10-05 03:51:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14e50a09-8995-3126-b32c-785d5e157695 | -17.62754 | -46.98239 | 2024-10-05 03:51:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b86f420-2939-3cf8-970a-a9467b3e9145 | -17.62297 | -46.98102 | 2024-10-05 03:51:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2dfde0f1-17a2-3dec-9d10-e219e953a7e4 | -17.57787 | -46.93979 | 2024-10-05 03:51:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1f7e1307-51e5-3de7-abf5-566108d5b1df | -17.57681 | -46.94513 | 2024-10-05 03:51:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7c1ba345-aa1f-3756-b8eb-47eb2a5c725a | -17.41476 | -46.31902 | 2024-10-05 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1120515e-07a2-3e05-877f-f910097e8e21 | -16.95073 | -47.12377 | 2024-10-05 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b8df9ecd-b8d4-3bbd-8698-ef20e22fcbe3 | -16.94599 | -47.12271 | 2024-10-05 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8dcfd8bc-fd0d-306f-b3e2-53acac88a4b8 | -16.94124 | -47.12168 | 2024-10-05 03:51:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5694f2b4-99c9-3b0e-9deb-d30212e049ae | -16.9238 | -47.18533 | 2024-10-05 03:51:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 54dcc97a-0b67-36fa-a8b5-7d5ba2da5ec5 | -19.47174 | -46.85106 | 2024-10-05 03:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4b4fdef8-875d-3dd0-a57b-907a76736611 | -19.15121 | -46.62698 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f385e172-55e8-3d19-9cbe-f3ad5d1e8dcd | -19.15104 | -46.6343 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ac4bba62-0265-35bd-a12f-6bacc0f1e501 | -19.15025 | -46.63176 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52873007-64c0-3267-b39d-b6fab81b9349 | -19.1493 | -46.63657 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2312c315-4eee-3e87-bad3-82a7add7d1e4 | -19.14856 | -46.62327 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4a75e0b-91a9-3328-80bc-d4d7b0a13e75 | -19.14767 | -46.6279 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 200cb255-f047-3abe-ba4d-af886ae95162 | -19.14689 | -46.62553 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 814c608d-ac38-3793-a38a-43cddbd04593 | -19.14675 | -46.63269 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e226c509-e21a-3a97-bfcf-b401b05d0979 | -19.14597 | -46.63016 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cdf8642-c773-3d8f-88a7-83843a9128c0 | -19.14582 | -46.63754 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 17549e43-e137-31ef-96a2-5f938edea755 | -19.14499 | -46.63508 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fc714e34-a963-3194-a155-39b72192fff1 | -19.14405 | -46.63977 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b792c482-8f67-3115-a860-d7db2e59d6a0 | -19.1424 | -46.63135 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4c571b7f-3a58-3b64-9895-2b9e22c38e3a | -19.14146 | -46.63628 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 37cbe7c5-2cc2-3b7a-9f8a-f7d5814285f2 | -19.14064 | -46.6338 | 2024-10-05 03:51:00 | NOAA-21 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b58530af-0cfe-3135-b26d-c3fd4986a324 | -17.18211 | -39.29245 | 2024-10-05 03:51:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fed8308f-1d35-397c-9a98-606b3a843394 | -18.50826 | -39.92313 | 2024-10-05 03:51:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ea124473-6bec-3348-aeee-fa08fa30b3fc | -15.27233 | -40.32604 | 2024-10-05 03:51:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| e4fdfb54-78fc-319e-90ac-292c20a889aa | -15.26896 | -40.32547 | 2024-10-05 03:51:00 | NOAA-21 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1e516e99-c0a8-31c7-aa1c-9e376dbb769a | -17.93597 | -40.54066 | 2024-10-05 03:51:00 | NOAA-21 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b0e1f32a-9fc7-35a2-becd-5398b245b0ed | -17.93538 | -40.54435 | 2024-10-05 03:51:00 | NOAA-21 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7c7571f5-155c-3e5a-a73d-82406e1949af | -17.93204 | -40.54376 | 2024-10-05 03:51:00 | NOAA-21 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 014c480d-4c72-330a-a0be-c3ba6861e18b | -17.9287 | -40.54316 | 2024-10-05 03:51:00 | NOAA-21 | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| e3b4f013-3ad1-3b17-a4c4-26135e5b986b | -20.31069 | -45.58474 | 2024-10-05 03:51:00 | NOAA-21 | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28af8810-0a9c-3792-a02c-b657e67ed8a0 | -14.06234 | -45.13784 | 2024-10-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13a347b8-db9c-3d30-9c0b-93a03ef35a0f | -14.06153 | -45.14227 | 2024-10-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 709fe62d-2374-3964-bf40-4c5071acc63e | -18.5538 | -42.23743 | 2024-10-05 03:51:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| b8dff03d-dfc8-3c00-9d4e-5d8c593aac70 | -19.87346 | -44.39909 | 2024-10-05 03:51:00 | NOAA-21 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ec66efb-d8df-3dad-9dba-00c651bca5b5 | -19.81507 | -43.77465 | 2024-10-05 03:51:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7395465-275a-3e7d-9e7d-b34509198279 | -19.81049 | -43.84228 | 2024-10-05 03:51:00 | NOAA-21 | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 209bfe61-98e3-325a-b9b8-2fb62b13f130 | -19.76953 | -44.2615 | 2024-10-05 03:51:00 | NOAA-21 | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 01b57fe0-357a-3cd4-b4ec-7a41a0cc6fcc | -19.76467 | -43.63737 | 2024-10-05 03:51:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1f059a0-aa0c-34ff-850f-87b8b738ba03 | -19.761 | -43.63668 | 2024-10-05 03:51:00 | NOAA-21 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cdec2f1d-4bab-3b34-9470-e70d69784bda | -19.83863 | -45.89155 | 2024-10-05 03:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88eaf1b4-83b7-3a13-b7b9-fdc87070f755 | -19.83768 | -45.89124 | 2024-10-05 03:51:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e32276f9-7ec1-3518-aaa3-f024e88ab53f | -19.80591 | -46.4467 | 2024-10-05 03:51:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 85564ff0-664a-3f72-825e-010c3b838d18 | -19.60966 | -46.26187 | 2024-10-05 03:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a0c99625-32af-34f9-b62c-661c43c765d0 | -14.05713 | -45.1414 | 2024-10-05 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2029df67-6163-3d6a-8988-3d73beaa6a50 | -17.86178 | -41.42352 | 2024-10-05 03:51:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| daba68ad-2640-366d-8fa8-6e7cebeedf83 | -17.86114 | -41.42732 | 2024-10-05 03:51:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 40d38c7b-2f21-3db0-b9a3-5df2cf64742a | -17.85838 | -41.42282 | 2024-10-05 03:51:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d958566b-3fa4-3cbb-bd31-bae2d688b06c | -17.85498 | -41.42211 | 2024-10-05 03:51:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 71e42eda-4968-3f55-80fa-587a33e9b7cf | -17.48763 | -41.15582 | 2024-10-05 03:51:00 | NOAA-21 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2d8c23fa-b73b-3f10-8a19-9c3e3715ad23 | -17.1008 | -41.19789 | 2024-10-05 03:51:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7019c83b-052b-353b-8dd5-10ced16f6f19 | -17.0716 | -40.94951 | 2024-10-05 03:51:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd4666a1-d4b1-3b64-b6ad-dde6c2d2716d | -17.06822 | -40.94891 | 2024-10-05 03:51:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7b21f37c-373f-3b61-9772-62eba87f5aad | -16.90897 | -40.6124 | 2024-10-05 03:51:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 059c3421-4022-3b7a-8171-65a6e0a2d5a2 | -18.56861 | -41.23317 | 2024-10-05 03:51:00 | NOAA-21 | ITABIRINHA | MINAS GERAIS | Brasil | 3131802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1539ce7e-a302-36ac-93e3-29942056986f | -18.09773 | -41.48536 | 2024-10-05 03:51:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 170b0aca-e814-31c4-910f-8321b8782254 | -18.09367 | -41.48864 | 2024-10-05 03:51:00 | NOAA-21 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 3f9dd1dc-d79b-3d08-86b1-d298e964a8f3 | -19.02906 | -41.04257 | 2024-10-05 03:51:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 588c51c9-849d-38b2-b7e2-20c04940e8fa | -18.87798 | -41.21378 | 2024-10-05 03:51:00 | NOAA-21 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 758a652c-1b2e-34ef-8780-e289bd9c65a8 | -14.13431 | -41.69216 | 2024-10-05 03:51:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5994d2d0-dad7-3578-8fa5-e93b86d4ec08 | -16.26482 | -42.28094 | 2024-10-05 03:51:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| eead10e8-f481-396a-ae5a-29cada13c8b0 | -15.76847 | -42.16805 | 2024-10-05 03:51:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c222339b-bc29-3d59-b41b-f31df611378f | -15.52287 | -42.24088 | 2024-10-05 03:51:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 516ec73f-db82-3b9e-abd7-176e88384dd1 | -17.9441 | -41.47782 | 2024-10-05 03:51:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d2090217-1827-3483-8831-1dce3374b769 | -17.94001 | -41.48117 | 2024-10-05 03:51:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 05edae1c-4883-37df-97cf-da3be182280e | -17.87368 | -42.25684 | 2024-10-05 03:51:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6962b227-0552-3c13-aa1d-1b584e022849 | -17.87335 | -42.25737 | 2024-10-05 03:51:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e16e33f5-cd2b-3e1c-8da1-757bc320c017 | -17.79818 | -42.22978 | 2024-10-05 03:51:00 | NOAA-21 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ce6c077a-a6aa-369b-ae44-18de1f09d3f8 | -17.62435 | -42.01352 | 2024-10-05 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 7784cd71-32c7-3112-b390-62670e7ca314 | -17.62365 | -42.0176 | 2024-10-05 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8f161970-0945-31f6-a629-e0e9e4e65121 | -17.62086 | -42.01289 | 2024-10-05 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| e8dd228d-0ea5-383b-8996-631c6c1c99af | -17.62016 | -42.01696 | 2024-10-05 03:51:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 6c148825-80ca-3f9d-a95b-d0f635976a31 | -17.33331 | -42.37153 | 2024-10-05 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 884d65ba-a6c5-3e05-afcf-eefd32e61e25 | -17.31834 | -42.37313 | 2024-10-05 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbdef600-8700-3c61-947b-94fbcdb93c82 | -17.3176 | -42.37736 | 2024-10-05 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4183c19b-072b-3cde-92d7-8ce07ad44ed2 | -16.99059 | -41.54249 | 2024-10-05 03:51:00 | NOAA-21 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d45f4974-02f3-3d28-a1b4-0db868718434 | -17.74943 | -42.89552 | 2024-10-05 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e09a7fc-a0d6-35aa-bd62-2c688ea421fc | -18.55798 | -42.23409 | 2024-10-05 03:51:00 | NOAA-21 | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 50c73e19-9306-3a90-b24a-51772331165e | -18.53132 | -42.26307 | 2024-10-05 03:51:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 613d070b-787e-3188-be5e-39eec7687651 | -18.53059 | -42.26725 | 2024-10-05 03:51:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a542fb61-5a19-304b-babe-968291b51dbd | -18.52465 | -42.25423 | 2024-10-05 03:51:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b0dbea91-6b2b-3255-bcd9-d7bd0c04c3b2 | -18.52115 | -42.25363 | 2024-10-05 03:51:00 | NOAA-21 | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4e39da89-11fd-327d-ab4a-2342912667cb | -18.49941 | -42.19074 | 2024-10-05 03:51:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c1104d4d-ca2d-3b5d-b018-4494362e062f | -18.46698 | -42.4229 | 2024-10-05 03:51:00 | NOAA-21 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| eadebe5f-c8fb-39eb-9237-56e03ff83550 | -18.27516 | -42.62645 | 2024-10-05 03:51:00 | NOAA-21 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 93d4e662-b081-3479-bd81-9fd7618cb750 | -18.18715 | -42.58914 | 2024-10-05 03:51:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |


[Clique aqui para ver as próximas entradas](README51.md)
