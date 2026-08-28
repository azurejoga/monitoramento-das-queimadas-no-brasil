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

## Dados Diários - Página 154

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a944d78-8103-30a0-80f4-d0434908579f | -7.73651 | -72.66419 | 2026-08-28 17:47:00 | NOAA-20 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e337a4c8-aa4b-3513-aa19-b16ff7a4134a | -8.26974 | -71.14781 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 15.5 |
| c163e3cb-4457-3c57-82e7-16d8ce2dbd96 | -3.66641 | -59.3217 | 2026-08-28 17:47:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8bbea0d6-f5b5-3f6e-9cff-2059b141d794 | -7.9233 | -61.36998 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2b5e01f1-b2ce-34aa-833e-cecf45b2d60c | -8.67665 | -62.94889 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d9b9e1a7-6821-3341-8e40-61fdfd1f4e8c | -3.90617 | -60.94403 | 2026-08-28 17:47:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 6552eb1f-107c-3dbb-9367-ebaaddec9c3a | -8.63597 | -66.54211 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| bb378a9e-2a94-3524-9718-faaaf84fa074 | -7.60923 | -61.35598 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| a559f7b0-1599-3581-82e0-6353404c2c1d | -6.27873 | -53.14076 | 2026-08-28 17:47:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 11cabd89-a040-3aa9-b22c-63e99aab36ce | -8.99406 | -72.66312 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 15.7 |
| f6388ac8-3a6b-3a44-91f5-536076b23e4c | -8.87499 | -66.89822 | 2026-08-28 17:47:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 922cb122-f6d4-3a96-8da6-ab70f5d8ba72 | -6.66193 | -59.43958 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 9f673de5-b82e-3b2f-ae7c-e71133020ec0 | -8.65514 | -70.75305 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 572feb18-aafe-3850-9feb-55736b57b162 | -6.80337 | -59.40074 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 72d6dd09-00c2-30d4-94b3-6b84fa30f4d0 | -4.30116 | -59.46926 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 88b02806-6925-3394-84f3-7fd4a9fc0ab6 | -8.8794 | -71.46545 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 8b8fc63d-849b-38c8-b277-8f2437dd9b8e | -7.58807 | -61.31007 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7c3f0520-9d60-3b2f-86bf-3772ed24f025 | -6.86031 | -59.44301 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 787351cc-355b-34e1-863d-37fc19d26018 | -8.88216 | -70.80867 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f6f44c3f-88b2-3800-9006-97278fa85aca | -8.64132 | -70.50874 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 61.8 |
| bad472e4-4f80-39ff-b0ba-0bfabe8f8fe0 | -6.16112 | -57.78722 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 1d2de1ae-41b4-3033-b1a1-9e2512861b8d | -7.91593 | -61.36737 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.8 |
| b10d3fc4-db04-32e2-806c-1f5c31ea6495 | -6.78514 | -56.63214 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9fae51c2-489f-317c-a734-f61261bb7ff4 | -2.61222 | -56.57764 | 2026-08-28 17:47:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6ff01853-1a0c-3230-a885-e3b5c38b05a8 | -9.73195 | -71.34754 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec96b39a-d15a-3bf1-b169-99f3c5565d07 | -7.59265 | -61.31694 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 90851056-8444-30dc-83aa-60b9632bec26 | -7.10213 | -55.48215 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 1196816f-4074-3767-a4f3-cc7079e30d2d | -7.06554 | -59.22511 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| eb40c253-0618-3fde-b1f3-54b1e9857d01 | -6.84825 | -59.46348 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| 21b957a8-452b-3292-977d-2b4d872f9883 | -5.76805 | -57.56115 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 005fbf38-a020-330b-9ee3-135d00b0fb30 | -7.58641 | -61.32172 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f4a946a-ca39-3b4a-9f19-4933ecdc35a3 | -7.94266 | -71.62681 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e69b768-0f54-301f-8076-8eb4a8492824 | -9.46056 | -70.43606 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0810bb74-3dd2-3d95-b3ab-8569e06c508c | -4.00608 | -55.33679 | 2026-08-28 17:47:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d6f1e9ea-8b05-37a5-99e5-f4f7bf5af6a7 | -8.80709 | -70.78703 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 336cb4be-d489-31a7-aa48-8cee28b150f6 | -7.2155 | -60.62242 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4f7e9f33-5e8f-34f7-8d1e-f5d856d7f80e | -6.33118 | -57.73948 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 625f78e9-49f2-3075-8fab-fcc776190f19 | -6.23879 | -55.46661 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5afe71c7-fbdb-3aee-b562-8a22271a624d | -7.91581 | -61.32218 | 2026-08-28 17:47:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6dd73683-a341-3f15-8217-a636d223d31d | -6.72189 | -59.44936 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b92342b-d3f5-39c5-b540-c4f20a642b3c | -7.48118 | -61.41074 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 252038cb-1637-31bf-a62e-4a69b088def4 | -8.22651 | -69.84251 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 9481fc23-f8e9-35a8-a459-105dec960b28 | -7.48741 | -61.40599 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 906f2bbe-f0d8-34a1-ada7-0412e12cebec | -6.69034 | -59.44493 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ed570745-8ae6-37bb-b934-b74a21442b57 | -3.11062 | -60.84044 | 2026-08-28 17:47:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fae7447d-f26d-3e2e-9660-319c340b686a | -5.93566 | -61.43397 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| df3d5b7a-bad7-3605-a569-57947918bcb3 | -6.99976 | -59.56436 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fe2c6741-fab0-33d4-b832-b5bc55d0747e | -6.84406 | -59.94888 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| f8e8c2e0-fc48-3b8b-8770-df9b7db54906 | -9.07881 | -72.2391 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd1446cc-4853-3af5-b29d-c4879f389580 | -3.40864 | -61.34517 | 2026-08-28 17:47:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 40b44fd4-dec2-310a-9ef1-6fdcdc7a7e33 | -4.33177 | -54.90268 | 2026-08-28 17:47:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| d2b218f2-5c88-3c2f-b730-aa60ba4da779 | -3.09476 | -57.21671 | 2026-08-28 17:47:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 903e7fda-1ee2-3fd0-a971-19294de515cd | -6.59159 | -55.42619 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5e087065-802a-3d3d-8193-f13524fb2bfb | -6.1575 | -53.5038 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8879e2c-6202-3735-8653-b9710eb0ed6c | -6.69636 | -59.43464 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e93e7e6c-7cc7-30c1-9753-20c58fb9e5c8 | -8.94765 | -72.73302 | 2026-08-28 17:47:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f02cfe34-0c06-394f-b906-adb9ce47e506 | -5.98603 | -57.75103 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e5af7fcd-fa31-3d04-8387-9e499e7360e1 | -8.65756 | -62.82375 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4519b03b-d26d-3ae7-a1d8-d801767afab0 | -7.33701 | -55.69945 | 2026-08-28 17:47:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8ea767b4-6748-3fa0-a579-9c8fc67d2edb | -6.1765 | -55.46768 | 2026-08-28 17:47:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b0cbd279-46c2-3614-9b71-9175bbd3c623 | -8.67718 | -62.95237 | 2026-08-28 17:47:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6a0cd7e0-5407-3c76-bb0d-0709a3b6f25c | -8.9498 | -69.46577 | 2026-08-28 17:47:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c5b3efab-5793-34d5-bba3-3cf4fd2c5d0f | -6.85068 | -59.94345 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 4ff51449-f297-3557-ade3-23311c9eb8c2 | -5.99594 | -57.68044 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0ad63f35-be7b-3b64-8f26-34730d5351cb | -6.84338 | -59.94463 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| bb686834-3db4-35d8-9781-5e622cff40c6 | -4.30504 | -59.46867 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 546d97da-7f34-3b00-9b53-3fb49083fff0 | -8.45836 | -70.41595 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 0bbc0ee4-1fc6-3148-8e5a-ce7f4c6d4171 | -5.76873 | -57.56524 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 5db3ea2b-9106-37e9-bd3b-68583ddd646b | -5.99316 | -61.46354 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 08630192-3f97-3c56-bee1-95543591caef | -8.36125 | -70.75235 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 552eb0ee-2bcf-30db-ae3d-1625278b6914 | -5.14425 | -56.27597 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 49f177e6-d5e3-3ce4-9240-bde2f64d2c17 | -8.3105 | -70.72987 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 94ebaf30-bdcd-3b31-bc50-f2713d4ba45e | -7.00383 | -59.51819 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 4425eb11-480d-3850-bb8a-9c3644eec332 | -8.99394 | -71.26447 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb1e8e05-57da-3f1b-adc2-0300007ed6fe | -9.74522 | -68.38169 | 2026-08-28 17:47:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bfe00aa-f6ca-333c-a350-b78c6292eba2 | -8.55115 | -70.60297 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 21871a2a-bb6d-32fc-955f-94f567b20ebb | -4.30453 | -59.47192 | 2026-08-28 17:47:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 15b24646-e95c-3415-826f-89167977736a | -6.17373 | -57.78516 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 120.5 |
| 41c03a55-dac8-3677-9cf7-582b1e7e9003 | -7.96532 | -71.3864 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 2774ff52-3d81-3614-b2aa-82af8bcb9a45 | -6.02658 | -58.05586 | 2026-08-28 17:47:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2cd0794d-e2f1-3cd2-9723-9f124777bcd0 | -7.18277 | -60.64723 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| def41f5b-f3a9-3d62-be8f-5dbbd21b6549 | -7.44356 | -73.20924 | 2026-08-28 17:47:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 11.2 |
| bcb6cbe0-57c5-3277-91d6-c2530ad14c52 | -6.37748 | -54.95665 | 2026-08-28 17:47:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6f09a1ca-1fc8-3a51-b5ae-515001543d85 | -4.96625 | -56.27048 | 2026-08-28 17:47:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ebd3a2ea-97ca-33ef-bf38-54ac9b0c9ed3 | -8.06211 | -61.27271 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 27386ebf-642b-3c25-ba5d-74204aa64c56 | -4.14729 | -60.7686 | 2026-08-28 17:47:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 158.6 |
| f667ff70-3484-34ab-b9ff-3c128748ac5f | -7.58358 | -61.32594 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6250c2db-32dd-3982-b7c5-71eb0efea3d1 | -6.93442 | -58.95028 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 29abc3bf-f556-3cf1-af95-58081e855629 | -7.47894 | -61.41864 | 2026-08-28 17:47:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 0cb452e9-4132-3495-9c69-3b10d036f5de | -8.56581 | -64.17105 | 2026-08-28 17:47:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 607e7a59-991d-31b8-9a4a-efe8149a617c | -3.01753 | -57.5172 | 2026-08-28 17:47:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7caa1d11-14af-3fb1-9e69-aea1b9a70a69 | -8.93699 | -70.71478 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6e1b01fa-7ca6-3b62-b2c1-40fdd1b1294d | -8.96731 | -70.64452 | 2026-08-28 17:47:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 2828c1a9-56fc-3da3-bb13-2e42b9e95aa4 | -7.71979 | -71.42109 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d39452f3-6735-38d1-b834-9ea70d372bcd | -8.47081 | -70.80791 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 66b67b1e-d0b3-3cf4-9086-6c74f0bbb07c | -6.83313 | -59.73803 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3af5ea57-1e5d-37e4-9d71-d4748a5c4e3a | -9.36088 | -70.49146 | 2026-08-28 17:47:00 | NOAA-20 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 13.3 |
| a52f2d21-29aa-3754-accf-1c390ba6759b | -7.06859 | -59.21987 | 2026-08-28 17:47:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ce63fb7c-8754-376c-9ecc-fe6928c4fe67 | -7.64874 | -70.22295 | 2026-08-28 17:47:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 30a72d92-ee58-3cf5-891b-52769da6029e | -8.27017 | -70.85753 | 2026-08-28 17:47:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 16.6 |


[Clique aqui para ver as próximas entradas](README155.md)
