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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba7e2fce-a4a4-35c7-b8fc-71b8c5f9b40a | -15.49561 | -47.96278 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d01a06b6-5465-34d3-bd23-959678e9ddf8 | -14.98171 | -46.28726 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00cf7779-42fe-32c9-83f4-de625cb54eb5 | -10.85324 | -49.91656 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1883e16-3e61-30c8-aa66-8c04ff1ef351 | -15.56182 | -45.31794 | 2025-10-09 05:12:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d345b30-f0c6-3ba7-a2cf-e50579c63016 | -15.22014 | -46.38206 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c79ecf3e-82e4-3dcf-a409-70931f2cc185 | -15.49622 | -46.86893 | 2025-10-09 05:12:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f05737a-f649-3474-85eb-333523e1141a | -15.23577 | -46.36022 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1da6b835-977f-3820-bfc2-6931a687ab9d | -13.58934 | -48.66654 | 2025-10-09 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5be9c2d9-6a82-341f-a95a-13b708265ec1 | -13.78945 | -45.87339 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1d3aff35-ea12-39c3-aed1-92926bb431b3 | -12.25619 | -47.88557 | 2025-10-09 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93087110-0144-34a0-ac35-82f68024ef05 | -15.46977 | -47.96719 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4de018b7-2ba0-3ac1-84dd-f6844ff0e0e6 | -15.4838 | -46.8679 | 2025-10-09 05:12:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b3993422-80ce-3bb4-9795-581972dd4e8b | -15.75403 | -48.72386 | 2025-10-09 05:12:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c163cdf2-14b4-3812-a35b-50894571354f | -15.22376 | -46.37916 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba597686-c937-322a-81d5-6938f2689616 | -14.84587 | -48.36153 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 37dd4659-6e5c-3fb8-b1e6-a8baa1801d2e | -12.0876 | -64.2252 | 2025-10-09 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c066b2a-759d-3be8-965d-b53498350cb0 | -13.81402 | -45.83619 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 028c7de7-f5bf-3ab8-bd88-b11338f1cdfa | -15.00359 | -47.53533 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58eb08e9-6930-3e5b-bdfc-5ef63a5a9f4c | -14.97503 | -46.28588 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2cf5a29f-228e-381d-963e-500c4f31c417 | -14.84671 | -48.44979 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f218cff4-73b6-3091-9a3d-1528749dba89 | -12.25678 | -47.8804 | 2025-10-09 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e96771f3-7801-3c30-a71c-d4775c346e91 | -12.40009 | -63.88056 | 2025-10-09 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4c44fdda-0670-3da0-bd9b-457acedd0459 | -11.99137 | -45.18547 | 2025-10-09 05:12:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 71e0c4d9-299f-31d2-93d4-6cfe475f243b | -13.78878 | -45.87978 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 40b5ca2b-d230-3a38-90fc-d31fbf30e92c | -9.62446 | -67.51994 | 2025-10-09 05:12:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 172e7196-fe94-30a8-bcf6-16987a1231e0 | -14.73392 | -46.09259 | 2025-10-09 05:12:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e758342a-8c1d-3628-b7c8-07e0eeb41ca5 | -12.08282 | -64.22826 | 2025-10-09 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0ea96d01-f773-3572-a66b-3f29df6ab326 | -10.89647 | -50.64196 | 2025-10-09 05:12:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76e85e02-5361-3a8d-a6a9-8441a39ea7c7 | -14.97446 | -46.29171 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| d850a526-53b4-3e00-860f-8c79d3d7418d | -15.28868 | -46.16207 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c264e597-cd98-3de6-aba2-bf76f5df6c14 | -15.4968 | -46.87009 | 2025-10-09 05:12:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b8867a2-ad40-3043-83b6-54b123cbfab6 | -15.06733 | -48.07645 | 2025-10-09 05:12:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65bd0508-ac74-33f4-86fa-e63e514f9430 | -9.81716 | -65.01881 | 2025-10-09 05:12:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db2fc0a8-dbc6-3ca6-a622-fa378235652b | -15.28647 | -46.16379 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eeba3b0b-ce81-3a1b-85f8-910f05ee1a9f | -13.83024 | -45.81335 | 2025-10-09 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51b44e9a-27e7-389a-80cb-9a3c0389c234 | -15.48949 | -47.96199 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08dffcde-ae12-3f64-8ea7-a89b7c34c25f | -11.71555 | -59.27964 | 2025-10-09 05:12:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0e540c3-8124-3e16-a8aa-64123fca8917 | -11.34336 | -49.38138 | 2025-10-09 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f49ccdb-ede5-3483-bea4-476e9bd9b5d7 | -14.6353 | -49.2585 | 2025-10-09 05:12:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 942ad5c2-c067-3b3f-bc66-6cc4c50d321f | -10.85869 | -49.91426 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87130381-2e02-3a77-b7ef-19665cf54f3c | -15.47077 | -47.95771 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a2ce4507-1527-35ef-9d0a-5526e5cc71fa | -10.86294 | -44.62424 | 2025-10-09 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 015e2341-22bd-3e0e-a092-c6189933268b | -15.28922 | -46.15636 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1254aba9-ae74-3137-bc90-deee00680649 | -15.74906 | -48.99612 | 2025-10-09 05:12:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 521bae76-47c1-381b-ab2b-b75144990734 | -14.07524 | -50.1579 | 2025-10-09 05:12:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3014410d-3eb6-33e6-86a6-409aa2a156f2 | -14.97389 | -46.29752 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cf97442a-47ff-3e16-b559-aededa1f0498 | -12.39609 | -63.87982 | 2025-10-09 05:12:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c5f1eb24-92e8-3051-8947-29a684968fad | -11.00216 | -52.32358 | 2025-10-09 05:12:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9cac85ac-929e-3939-946a-d55200da05aa | -15.47026 | -47.96249 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52353bc6-b1b2-323b-a1ca-15bd3ec5cee7 | -13.92768 | -58.38287 | 2025-10-09 05:12:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d55b86f7-fb45-3c86-af7a-6562a27952b4 | -12.26764 | -47.89033 | 2025-10-09 05:12:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3855228f-82c9-3689-b775-132894974e2e | -10.52381 | -50.01749 | 2025-10-09 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f2ca7720-052a-33fa-9e31-89452ae3fdd1 | -11.78448 | -45.1551 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e82d7391-658e-3469-8a8a-c5ae3bcc7c1c | -15.38633 | -48.05823 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f49dd44-a0d5-3a2b-b090-7e357c02d894 | -13.79558 | -45.88061 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 36e53e07-76d2-325c-931a-5a192c2c628c | -15.23169 | -46.36777 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fb78079d-8acd-3cbb-b118-87e685d29af3 | -10.85584 | -44.62347 | 2025-10-09 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 75a9608c-da80-343f-9360-e9e11e09f631 | -15.39288 | -48.04466 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0a571fd-2ee7-3b96-8495-f5f78b7112f3 | -13.28799 | -48.46206 | 2025-10-09 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6f20f33-aa56-39a0-b3c1-6b9ebafd7475 | -14.78215 | -46.11056 | 2025-10-09 05:12:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 50d4f5a1-15a2-3036-82fa-52c3b9dcd4fc | -15.49036 | -46.86845 | 2025-10-09 05:12:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0676d757-4e8b-3793-9150-ba6d581176aa | -15.39238 | -48.04927 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a46d7b06-f7e5-37aa-9929-9afcf761e0cd | -13.5889 | -48.67038 | 2025-10-09 05:12:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b091238d-c985-35bc-ac68-015a20296611 | -14.63574 | -49.25451 | 2025-10-09 05:12:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46205ac7-694e-335e-aa5f-2a9209642ee4 | -11.78523 | -45.15156 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae069968-76f2-3692-b328-14bca643ab4e | -14.98591 | -49.93887 | 2025-10-09 05:12:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f13b522-33de-3072-9a12-20a12a4f86e5 | -15.47635 | -47.96349 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6607e88d-0667-3cf5-a77a-a7eebb34e2ef | -13.82386 | -45.82263 | 2025-10-09 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4755d3fb-76b3-3f2d-b2da-c95d47e820ce | -13.8309 | -45.80707 | 2025-10-09 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f7d62eb-62be-3901-a264-6a595395c951 | -15.48905 | -47.96643 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55b81c24-326b-38b9-8d8d-c7f92dbcf27d | -11.34377 | -49.37812 | 2025-10-09 05:12:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68b763b2-96e9-33f8-bc73-a3e8e3d03496 | -15.74535 | -49.03104 | 2025-10-09 05:12:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fde1461e-3885-3d82-9ff6-88ce614e860c | -11.34769 | -61.61715 | 2025-10-09 05:12:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd351743-29f4-3fa2-a245-431ece2c3bc0 | -10.84979 | -49.94359 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc486cd8-9d75-3bbd-b19a-cae0334bd1fb | -15.39188 | -48.05384 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89358b62-8978-301c-9deb-fc182a981ca9 | -15.29645 | -46.15276 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c7caea2-8578-3750-90ac-c29c612e5768 | -11.78513 | -45.14897 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7fd5669d-3aee-3f83-a5f1-65b72cec37ea | -15.29378 | -46.15957 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8eaefa05-e672-376b-a189-12fe78566d63 | -15.00982 | -47.53622 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2821329-0329-3f21-a1fb-9fbec7f2c1a5 | -10.85505 | -44.63054 | 2025-10-09 05:12:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d052d194-fc5e-30bb-9cf5-a691edce024c | -13.82571 | -45.80394 | 2025-10-09 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8097e65f-4bdc-36a9-a3c9-40e7abe43f4e | -13.78528 | -45.84705 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74c65cc1-7a69-350e-91e0-6dece92477f3 | -10.55659 | -50.03993 | 2025-10-09 05:12:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c78fc04-1472-352e-8237-3d9036447ffa | -13.29322 | -48.46746 | 2025-10-09 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c944d68-64a2-381e-851c-ff359aed8b9d | -15.38578 | -48.05335 | 2025-10-09 05:12:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fe782da-1204-3747-8616-96acee60cff3 | -13.79145 | -45.85408 | 2025-10-09 05:12:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ebd9148-ac36-376b-8f5d-59790c4de049 | -13.82448 | -45.81637 | 2025-10-09 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68bbc1ed-20ec-3edf-acc2-9b7385ef792c | -14.6364 | -49.25892 | 2025-10-09 05:12:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 577b3ac0-e4c0-3da3-b9f4-dfe9e3b6708b | -15.47128 | -47.95287 | 2025-10-09 05:12:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 47a375d0-64b8-3bba-8ffe-6ee19cb717f1 | -11.77816 | -45.14842 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 36183f0d-af56-34ab-881f-baee4f59b1f0 | -13.8296 | -45.81946 | 2025-10-09 05:12:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 40d91bab-8826-3475-9b64-b3d646447fd7 | -15.22792 | -46.3715 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ffa70236-fdbd-300e-8ba4-1d737ca175de | -10.74272 | -50.06164 | 2025-10-09 05:12:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab360c1e-e5b1-37bc-bf7b-0901785669f2 | -10.73432 | -49.33623 | 2025-10-09 05:12:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 68ab42d1-ccfe-3dee-8ba8-5ca359b500e5 | -14.72686 | -48.37015 | 2025-10-09 05:12:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4054fe32-de53-3080-8409-163809ee4e9b | -15.00553 | -47.53581 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f814a2f7-1855-3dbd-9388-efa5356c71ba | -13.28849 | -48.45768 | 2025-10-09 05:12:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87fcd693-9dc3-3d0f-ab97-0511ed3e2abf | -11.77758 | -45.15714 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| c6db302f-626f-3f7f-9882-25d2e2ed225f | -11.79291 | -45.14588 | 2025-10-09 05:12:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cade226c-1e98-358c-bdea-1a901e22e375 | -15.01035 | -47.53093 | 2025-10-09 05:12:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README55.md)
