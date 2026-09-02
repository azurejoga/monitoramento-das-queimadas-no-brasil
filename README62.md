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
| 232f456b-1ee5-33f1-a242-e1af58b4c311 | -8.93024 | -69.45436 | 2026-09-02 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9ca24cf-a1cd-3368-8ed4-bb21f2781ba8 | -6.69366 | -59.94807 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e40f46f5-f0b4-3099-b8b0-ad68ef1db841 | -7.21415 | -60.68524 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b605082-df1b-3902-a8a1-bb02b3b313ca | -9.44224 | -67.45244 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5a1162f-5199-3ec0-afbd-557199ff2e90 | -8.65859 | -70.68616 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 613b585d-7549-3d91-a68e-5c0a30563197 | -7.44426 | -61.4137 | 2026-09-02 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1a75047-a834-318b-8170-9123f96190b9 | -6.76642 | -59.44422 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93eb37c7-63ff-3cf7-8a85-5d386e763ca9 | -8.93081 | -62.36551 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f525e0ba-748f-342a-8d29-1c96c3c82efd | -6.64917 | -59.43486 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0fc21596-a72a-3faf-bbf7-61234975b87e | -9.47235 | -67.08705 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7461022-427d-31c2-b611-87f7ab5d8337 | -9.00504 | -65.41852 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4c1f4c5-51f7-33d2-a09f-ad4af028cf0b | -7.68787 | -67.12603 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c063e0f1-ee89-3b6d-9887-807f20f41ea4 | -7.68422 | -67.12548 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7967aa1d-8060-3be5-91ab-d41968e20d2f | -8.64659 | -69.77576 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db30711f-a7e5-3f97-bc1a-9870b1f6cd64 | -6.64533 | -59.43795 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b93a31af-e45c-3bee-b0e5-e578ca2e6d50 | -9.035 | -65.40659 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 042580c4-5f1a-3e18-9040-0e0a8fb24ffa | -7.50461 | -63.76184 | 2026-09-02 06:01:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b38836c2-1c70-3ec1-9b58-25030bbbd4d4 | -7.20195 | -60.68921 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e7e7361-9e45-3eea-911f-c56a81ff1fc5 | -7.20262 | -60.68704 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f14212da-a4eb-30b2-b109-1b741fa8998d | -7.30662 | -60.62495 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9367563-de9f-38d6-b84e-7b1d41adaa8e | -7.69216 | -67.1223 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbfe654e-d754-36c4-be42-3f7e0a0c013f | -8.49462 | -71.47094 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71401c18-4aa8-3ab1-94d3-917c169a62e4 | -7.19834 | -60.6736 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5eebcb2-5f6c-3f67-8586-298a184bd53b | -9.03652 | -65.40417 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c279410b-623e-3fe6-be80-3aaa18e1c357 | -10.49015 | -64.32698 | 2026-09-02 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 91418600-b531-35b1-a1f8-ccfd98e81875 | -9.0208 | -65.4549 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f8f94f8-85fd-3edf-a58e-5cada6f9991c | -7.75787 | -61.19836 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 079161a3-4f9a-3578-905e-c360017c67b6 | -8.74973 | -62.57586 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 322f4a8c-66a5-3d8d-9481-2ee1d4782d5c | -7.20481 | -60.66725 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8fa1cc2-6370-319b-b19a-82bde04f519e | -7.25639 | -61.11127 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aaec1f0f-55f2-3b24-a0d0-470fb3e1b669 | -6.18287 | -57.73284 | 2026-09-02 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 83fc26b4-0c7c-3e70-8929-1941c15db28f | -10.09594 | -69.23171 | 2026-09-02 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| efe38ce3-f291-3084-abae-1ac33ef0eff7 | -8.00562 | -70.62146 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85c7fb22-d0ff-351f-ab2d-61dd5f61c294 | -7.34151 | -60.57777 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| efa2a0c6-d3dd-313f-94ce-c5551690d3ba | -8.91562 | -62.3633 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ddd360e-9f09-364e-a22e-397262dc2fe3 | -6.92451 | -59.64552 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 067467d0-1736-39e4-9029-1198c48c8fa5 | -7.20561 | -60.66536 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66a40616-5e1d-3a06-aa0b-0dfba5fe8ad0 | -8.76453 | -70.79179 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e69813f0-aaec-3e9f-ac18-803b400f3e14 | -8.89121 | -71.39425 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d0f4482-c4d1-3b41-af8b-3e6892a0a4ca | -10.48561 | -64.32648 | 2026-09-02 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 26.3 |
| bdea276c-7af4-3b06-9a75-3c0f1cc0fa4b | -6.14692 | -57.75121 | 2026-09-02 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88297cde-eb30-3664-bd51-c2a128d42645 | -6.15353 | -57.75185 | 2026-09-02 06:01:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 082c4e2f-f660-3e6e-b3fd-04d52ff96e75 | -9.03008 | -65.44871 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 548e58c4-7e68-3331-b4fd-d88a35fd9ecd | -9.01432 | -65.41236 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ed2b9fd-99f6-3ec6-8866-44b0b6e69f27 | -8.91685 | -62.36345 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 672217ed-2554-3804-ad00-2708e967913b | -7.20464 | -60.67243 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed5051c0-0b7b-3747-b6a1-32f22b62c9ef | -8.9055 | -62.36183 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1d139a42-89b0-3636-9822-4925f47b8e1a | -9.0897 | -65.37639 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 84fe5be8-52f3-3323-9900-06204716680c | -8.81297 | -71.24219 | 2026-09-02 06:01:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e0df8a5-5527-3806-a610-7b2057f95bc3 | -7.21538 | -60.67274 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2c8dcf81-d34d-3dd6-806f-0607bd63d706 | -8.78585 | -69.01965 | 2026-09-02 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 302a2260-74a6-3858-9827-2a24ea3343c5 | -9.02939 | -65.44752 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4b9efcb-e4f3-33f5-938b-7f00e8266e41 | -9.00556 | -65.41483 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e95b0f1-ba97-3973-a9fd-175d04bc47c8 | -10.10376 | -69.08776 | 2026-09-02 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f41aefea-8e07-3a4f-95c7-e060f63c0501 | -6.77356 | -59.43613 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8351e8a0-a090-3296-b572-2e301669287d | -8.71866 | -70.54256 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65cb5431-97bd-3738-8b51-e3ba0b845328 | -8.58513 | -66.97856 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e96d5460-5e32-3fdd-b58b-8c82a3c3d444 | -7.19911 | -60.67152 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ca9c472-2f36-362d-8a1f-fd54f17bcdaa | -5.57577 | -60.19293 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3dc845c-7bb1-3e74-bcb2-08cb121d8576 | -7.21515 | -60.67806 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b664dc06-1cc9-31f7-b692-c3dd3c20a5fa | -5.32959 | -60.14881 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d88aa1fd-d8c7-34a8-9f13-41bc610ad587 | -8.91138 | -62.3657 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fba5aea-df95-3bf2-8caa-f1acc9f1d69d | -7.19962 | -60.66784 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b6136edd-5c76-390b-95d4-76a34f34a62a | -7.21566 | -60.67435 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 669764c6-eb79-387a-accd-659716557e3d | -7.35615 | -60.58743 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed75b578-2896-31d4-83a5-503b557b3cd1 | -7.25687 | -61.1078 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1118be13-4cc4-3fae-bdb1-a0b128c44e54 | -6.87877 | -59.40017 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ce7a1488-ce42-30ea-8a8f-bf17168b75b1 | -9.02027 | -65.4586 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbd2b2f6-3d8e-3d72-b6e5-c28fc983983d | -8.65198 | -70.68512 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d97070b-73cc-3cb9-b86c-9015fb45aaa4 | -8.64932 | -70.72384 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3023b1a8-b432-3af8-ab6a-a603456468db | -7.6958 | -67.12285 | 2026-09-02 06:01:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12b47194-d94e-3b20-9fb6-147135cae6f4 | -8.77691 | -62.83634 | 2026-09-02 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8eb2d213-da50-3dca-9fbb-4de19829f5ee | -9.00292 | -65.43338 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79524a4f-d371-3aa1-a9b9-8f4bd46802f8 | -9.44715 | -67.44439 | 2026-09-02 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2957ce9f-ab1b-3878-bc15-26df6aff3f26 | -9.19019 | -65.90747 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 176c8056-826f-32f4-8049-18a73cf24c77 | -8.76508 | -70.78831 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6dc852e4-1c84-39dd-bb21-79708f9ab400 | -9.0249 | -65.4555 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9838067-a58f-3c30-924e-6001044226ce | -9.05199 | -65.4357 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea79338b-ff5f-39f6-881f-cc3d7c08cc04 | -9.02544 | -65.45181 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358b1954-3b3c-3435-9f22-f29a5257d98e | -8.75051 | -62.57012 | 2026-09-02 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 215b00e8-d9be-38f5-a273-61f31149b933 | -7.44382 | -61.41701 | 2026-09-02 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d2c804c-e621-36a3-a303-e4d9f1e2151d | -9.1296 | -65.4727 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f79831e9-a362-3428-be06-a32f6b8e049e | -5.33012 | -60.14508 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1102aad9-e5d6-3346-9cd5-09efcc01e135 | -8.7864 | -69.01596 | 2026-09-02 06:01:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 985c3b72-7cec-3ac8-aeca-6b98631e215a | -9.65 | -68.6125 | 2026-09-02 06:01:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 464d1f3e-8c92-3a95-9478-8f7b3e070651 | -7.19638 | -60.68867 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67760533-e1ea-3612-9355-38d0481e0f0c | -8.79945 | -71.0472 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3e90828-2c3c-38b3-8119-78dedbbb45cb | -8.8679 | -66.82475 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36611eb8-9f5a-32c6-8f06-6275fdd6906c | -8.63668 | -69.7959 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0097bacf-6c39-3f64-a023-076cb56b256a | -9.07304 | -71.96333 | 2026-09-02 06:01:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6b1e0a81-3107-3c72-a86e-693861e70394 | -9.0102 | -65.41174 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b60d0f02-7744-307c-b4f6-ec7000fb4721 | -7.26176 | -61.11209 | 2026-09-02 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8bbd0e33-43e1-36f5-8afb-6f69a2f74aac | -9.03143 | -65.43266 | 2026-09-02 06:01:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9be9fca4-6139-311f-a37b-d847f0fc7efc | -6.93685 | -59.64324 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 84dddbd3-e169-3ced-af14-7f0bcd42b1aa | -8.56283 | -63.19278 | 2026-09-02 06:01:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7c8c74bd-5f5c-33bf-a35f-9f1158ff72e5 | -9.10458 | -63.97741 | 2026-09-02 06:01:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b73ec21-bc0c-34a9-8d4b-445b41bfa0e0 | -6.92903 | -59.64341 | 2026-09-02 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c4e037a-0a93-3380-b2c4-649f085ee54b | -9.50907 | -68.59192 | 2026-09-02 06:01:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 636e20cc-3be3-3aa5-879f-7d3390483411 | -8.61043 | -70.34047 | 2026-09-02 06:01:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92753f4f-853a-3dd1-a7e2-31b37f482891 | -10.48357 | -64.32964 | 2026-09-02 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |


[Clique aqui para ver as próximas entradas](README63.md)
