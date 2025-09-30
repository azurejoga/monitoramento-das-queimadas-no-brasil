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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 703af521-4c27-382c-a2b3-f82708370be3 | -10.85129 | -47.95787 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5afabd44-7823-3758-802a-cd4b58cfd318 | -13.22288 | -47.32354 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 352b5bc9-abb2-3361-b7d3-1f5508c8624d | -14.49595 | -44.85538 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c94f854-295a-3c0a-875c-d9188a0a1d9b | -6.78719 | -47.16285 | 2025-09-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 92ff58c2-d3c9-300b-a897-d58e5b4b9158 | -10.83964 | -47.96421 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45264c37-09dc-360f-9bce-20dcb9345bdd | -11.75987 | -44.74032 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.9 |
| b70bcef2-36c7-3789-9fe6-04a709f75495 | -10.07403 | -50.21773 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7a8a6eef-461d-3386-b839-d1654db4149c | -9.30378 | -54.50465 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c7b74cf-cf5a-3566-b3a9-21f2469e7473 | -13.37067 | -48.16862 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 29c92ba7-3894-3140-9c43-92de5489a8ba | -13.59952 | -48.03618 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df261b33-f2f0-3826-bdc1-08947f05a497 | -10.31227 | -54.17691 | 2025-09-30 04:40:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c129c4bc-eeff-39d2-80ba-84322e35e858 | -13.22812 | -50.93552 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 5bb19be4-8cb4-3065-aa5c-2db71c6d4a8b | -8.61657 | -54.98828 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa8c2787-a83a-3532-b76f-b740192bdec3 | -11.78861 | -47.60624 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16a7959e-9dea-3c22-af53-1f589c227e34 | -8.50512 | -47.25292 | 2025-09-30 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 283af63a-6b52-3268-95ab-9d29c175d8b0 | -11.44496 | -43.5124 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 77c9d147-007f-3551-9aa8-a388d10390d0 | -10.40286 | -47.80371 | 2025-09-30 04:40:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7744144-6daa-3070-bbff-dbc73cb6e906 | -12.58711 | -41.29124 | 2025-09-30 04:40:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 087d2cdc-50ce-3508-a898-310300cdceea | -11.19141 | -47.23671 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e49f9e7b-e631-3e95-a738-938151852440 | -7.01788 | -45.20959 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b700067e-14ce-31bd-a80d-1e75792252a0 | -10.83615 | -47.96361 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a3837ed-efc3-33b6-8269-06dd02f1fd95 | -13.04016 | -47.08175 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5b1c48a-9f44-3fc2-8807-2566ef025fc3 | -9.3984 | -54.70728 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3ea2312a-b783-3e6f-b762-d7a23dd315bc | -8.63056 | -44.02073 | 2025-09-30 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7c836e9-0edf-34a1-806c-3d4217e5b2b6 | -10.18729 | -44.88265 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 05b1730d-e471-3368-96ba-35becea16991 | -12.97304 | -48.41522 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9a9b842-0d2c-3669-97b6-a94ce0eabe5b | -12.95741 | -46.402 | 2025-09-30 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e4430e1-ec05-375a-ac7f-7cc48f415602 | -11.75382 | -46.85349 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2abe8956-0373-3724-aa64-98504cba7237 | -11.4529 | -45.03727 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 726d816d-26cd-3d9d-b9bf-02c9278064ce | -13.59467 | -48.04438 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3080de7d-0eb9-358c-b43c-e2730e2a6429 | -13.57268 | -48.09533 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cba6c8d5-0105-3ddc-9edd-7cff5db4ab43 | -8.85914 | -46.58542 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b68dfe14-3fba-3a09-9816-2d2e9120e6c5 | -10.66106 | -53.70762 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0f7fdf6-b90f-3b13-b585-88b36bcb94dc | -8.09303 | -48.00529 | 2025-09-30 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47c541a5-3bf0-3456-8a89-fa5c0ccfe1f7 | -8.85852 | -46.58971 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26834e2b-2428-398a-bd3d-2886b7a140e2 | -9.96498 | -48.8028 | 2025-09-30 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a12fcfb6-54e5-36f1-a18d-11ba1d735512 | -7.8878 | -55.44895 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce45a11e-5a38-33e4-bd62-698ea73b373d | -12.76387 | -47.76508 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca97a8b1-412d-3c2f-b40a-8d1b95a6370d | -7.9119 | -44.60258 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1a85df33-228e-310b-84af-6ded9a2172f0 | -11.83731 | -46.61556 | 2025-09-30 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e43904a4-4861-35d0-850a-f5ab48e5a591 | -7.63193 | -45.45769 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81efab51-c6d8-3458-b885-7c9002b2b62b | -12.88492 | -44.68471 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0facd71c-e6fa-3f37-a6b5-3ec978516b96 | -7.78479 | -54.92831 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 550467b5-061f-3b0e-9185-3bf5121c1945 | -11.41879 | -44.90171 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7b2c6b0b-90d6-3266-9f89-e42583592b99 | -11.42245 | -44.90627 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e22e133-f008-38c2-9e2c-cee71158440b | -12.41402 | -50.19674 | 2025-09-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d64ed17-0a81-3aff-841e-099bb001291f | -7.77205 | -45.7462 | 2025-09-30 04:40:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a347ff2-e173-3770-a05b-215b81c7c63c | -13.78547 | -47.9439 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 17884fbf-0a31-31fe-ae8e-617c94235316 | -11.15866 | -54.12828 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 9f1e86cd-4803-3ceb-88c5-6a159b3507c8 | -11.88278 | -48.05149 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f5ac5f6-c05a-37ae-8330-35ec42f557a1 | -13.67253 | -44.21787 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62a18b14-e443-3571-b1aa-dce348698c31 | -7.86379 | -47.25433 | 2025-09-30 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7f18f0d4-c04a-35cc-83f2-f837051cfa16 | -13.80131 | -47.88413 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1cfe09e1-1545-3adb-8748-bc07ceeb6e9f | -12.84819 | -47.01583 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 19042476-cd30-31de-9e8b-60387c04d0c4 | -13.62228 | -48.03089 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd898445-3403-3923-a4cc-6718f411e6c1 | -11.64575 | -47.48788 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8a1e598a-de40-3c9f-8e70-695ad31a073f | -12.14209 | -54.27138 | 2025-09-30 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a6ec80e-45c9-35b7-b760-b8c63ab96384 | -8.06819 | -42.94653 | 2025-09-30 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 84a6ad1f-7cef-3944-abd0-f2aee85a4ff1 | -10.07349 | -50.22121 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| d007ccf5-83fc-3003-a675-d1f424fd64a7 | -8.3179 | -49.03851 | 2025-09-30 04:40:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a13fe8c4-2e3b-3ba3-8c9a-8ef04cb90d73 | -8.78091 | -51.65341 | 2025-09-30 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 957e0b4f-22d2-36b9-9234-a7ef56ad764e | -11.20115 | -47.22071 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a43b2b96-2e56-3f4d-bff0-e0fda94e5a02 | -13.09239 | -47.03738 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91f5e5eb-b302-3653-8a71-a92d4a32c2c9 | -7.50208 | -46.12523 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f0b6b976-848d-3c45-a9fb-9703dbe716e0 | -13.80193 | -47.87974 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 727e7de6-90e2-3aae-88dd-3b261a0a8dbb | -13.28214 | -48.45485 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 748ac811-2561-3e33-bd32-10b90ee7b364 | -11.46187 | -44.99208 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0250e358-790d-392b-a4df-d6066384212d | -8.72352 | -47.98848 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8b9ab9a-f504-38e0-b7ee-d03df7f813f0 | -10.25676 | -44.9586 | 2025-09-30 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9843143-dba0-36c9-a751-cb8d73bb746e | -11.68013 | -44.29689 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1605d22-c05f-3b75-9605-efefa85d1f0d | -11.6215 | -52.24013 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65b3aee2-02b7-35df-b98f-292fcad44fb5 | -9.80481 | -49.07372 | 2025-09-30 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 409a3a81-b792-34d3-85f8-aa36d2271174 | -10.10907 | -47.78893 | 2025-09-30 04:40:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 127f6ffe-7772-39a6-898b-0314768b6b7e | -12.6919 | -45.28249 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3011998-09fc-3492-bb81-efd15a0b438c | -11.43499 | -45.03219 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9cc2f7ff-30ee-3318-a34f-254ff515563f | -8.26636 | -45.50943 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d38cf288-1cbd-3668-89be-b63d118b7c54 | -11.46078 | -44.99987 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eea476a7-29a7-3b6b-9676-27361bed0a76 | -13.66964 | -44.31188 | 2025-09-30 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 00cf744a-df93-38db-83b7-79f819b69f0c | -14.39928 | -47.1465 | 2025-09-30 04:40:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f20746c-5784-32da-85b8-005b0bbc73db | -10.62805 | -48.54414 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6eda434b-e27a-3ff7-aa0f-64bbf3d4d2f8 | -9.42944 | -54.72061 | 2025-09-30 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 371122c7-88f1-3fb5-a2c4-8cb2c448538b | -10.38789 | -51.1635 | 2025-09-30 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a1362cd8-2440-3be5-a315-22d3e0b31c03 | -12.93159 | -47.13797 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0af2c537-5cf9-3070-ad12-c1a81b85932c | -11.44749 | -45.03397 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 020c7b57-18b5-30c0-9e90-14c7cb5a3a7a | -11.06623 | -47.82433 | 2025-09-30 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 417b0935-f99a-3108-aafb-24084b0a2fd1 | -11.14111 | -54.12166 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f89bdf7f-d808-372a-8f16-cce29f2f7a96 | -8.24976 | -45.52974 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 404901f7-5b21-324d-9e82-6b83c010271d | -10.8507 | -47.96191 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe0facd0-4c2e-3933-92ec-25f6082124b4 | -11.43512 | -55.03899 | 2025-09-30 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dde9be55-099e-3360-aa01-94da919e6b2a | -11.45601 | -44.98158 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b1948cd-ef04-3119-864d-4e52eef0f303 | -13.22372 | -50.94203 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 509ff00c-2501-3929-93c6-2de5d5157435 | -11.44097 | -43.50681 | 2025-09-30 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 279bded8-97b5-3b07-89ea-dc30dc69f901 | -12.78152 | -46.85632 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 85e0a48c-f19f-3621-842f-83a408f65fc6 | -7.82431 | -46.98795 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22886764-bb91-34b1-b852-20727604554e | -7.56216 | -42.4094 | 2025-09-30 04:40:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9b19b37-44c7-379e-8c89-ba7ca0424358 | -11.16306 | -54.12457 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8c5bc14d-c4fa-32b1-bcd3-7854c2b8efcb | -13.64758 | -47.32877 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9835db93-8250-35a7-87bc-497811d943cc | -7.53803 | -45.30192 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 11151abe-c3ff-34a6-8bbc-410a09a1ce8f | -12.06686 | -47.98177 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b07ae1c2-8980-3626-a512-75bdff97d786 | -10.0404 | -50.19094 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README63.md)
