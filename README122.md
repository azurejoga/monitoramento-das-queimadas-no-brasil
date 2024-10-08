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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b65df55-39c1-31d0-b256-20fbd30945cb | -9.90951 | -60.17716 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2dfa0b4a-37a0-3559-9f25-798b69a2a08a | -9.90671 | -60.17307 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 753b90ab-09c4-335b-9908-c6f5ffce1e74 | -9.90616 | -60.17664 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58ddd2e5-5a33-3c3d-8f77-9be01649cc2e | -9.90336 | -60.17254 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad855648-61dc-3079-a913-f26c5370c6f1 | -9.89599 | -60.31001 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5235c74b-5ed4-3d9e-a1b1-4b7565846224 | -9.8932 | -60.30593 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f9697a9-f312-33a4-8bc9-a5cb9a53f190 | -9.88599 | -60.30842 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7db766e0-7b4e-3fa4-bac2-5bf0dd40ad1e | -9.88476 | -60.27186 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7321fe9b-4734-3cdc-bc6b-c1ac9a110127 | -9.88265 | -60.3079 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3aa7c1a6-9004-335a-b0c7-6e9074e91bbd | -9.87932 | -60.30737 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d3b74e5-e738-36dd-bc52-e274ae481cb6 | -9.87598 | -60.30685 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eda578d7-d08e-3cfe-9f69-f905dee340ff | -9.87544 | -60.3104 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c2441a4-bd8a-3b1e-88bd-caa8acb71414 | -9.87362 | -60.15039 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67593f6e-4ed7-32c0-b02c-62138882cb7b | -9.8733 | -60.30718 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c7a467f-15c4-317a-9e46-02978812c241 | -9.87275 | -60.31072 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6835dcfc-c339-3be1-86f8-541457f4b7ad | -9.87027 | -60.14986 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66c69069-0147-3e7c-9150-5078dce99793 | -9.86996 | -60.30666 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63f2e9e4-dd7f-3f8e-9d2e-4499e74c356b | -9.86941 | -60.3102 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd14c8f2-183a-3831-ba12-60aed9c82b7b | -9.86693 | -60.14934 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e38c79d-4e04-3c99-b007-877fa31d70b5 | -9.85607 | -60.30811 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2afcac62-b063-301e-b3ea-fc051224e70e | -9.85552 | -60.31166 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d447dcaf-7a83-3cf6-8023-0793c49bc86d | -9.85274 | -60.30759 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf6184c8-91b0-3e3f-80af-0ec733dde73b | -9.84438 | -60.29539 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 234237da-40ce-371d-90db-36e51c884417 | -9.84383 | -60.29893 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86602896-44a4-3799-9fca-f375cc2a4fc6 | -10.45334 | -60.10349 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2746fda-2147-3fca-b649-74dc9047d844 | -10.34749 | -60.19787 | 2024-10-08 05:23:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71a41a11-fd8b-3bdb-a9e1-7db38d7d6be2 | -11.43116 | -60.45765 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5d019c1-eb5a-30f4-82ae-0e7c95e56dbc | -11.41943 | -60.44468 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9011bef-0448-3321-963a-6b990fd68a6a | -11.39029 | -60.41069 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 891a1239-07ea-3b27-a766-24947004f565 | -11.35901 | -60.5712 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9dbb9601-8ba2-3b30-8b51-83fe99dd0777 | -11.35567 | -60.57069 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| df153722-4e58-3c5a-8c21-3a49a944eee1 | -11.33651 | -60.54588 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42413a9c-007e-365d-a173-e0f8b0a0ffc3 | -11.33038 | -60.54128 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ce21919-329a-3a7e-8536-1109c9b986cf | -11.32704 | -60.54075 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbce8ac0-32ab-3b83-af85-8a7820094983 | -11.32649 | -60.54433 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91d71865-25a6-3a65-b338-3b16077fb28b | -11.3187 | -60.55043 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 125aa7f5-b84e-359c-8ea3-bb9b88cf78b1 | -11.3176 | -60.55759 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eeb294a7-ae25-3ee5-9d60-9957928c4f54 | -11.30313 | -60.5627 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b75588c-909a-356f-ae18-c876722ba431 | -11.30258 | -60.56627 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08ec8567-7126-32fb-99b6-01aa7f033acb | -11.28156 | -60.61412 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff4b1684-077d-3228-9a02-b036ff8a0073 | -11.28101 | -60.61769 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f1ea2061-6ec1-3080-9226-21307743c910 | -11.28047 | -60.62125 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14460643-3199-3a58-89a1-7b422218efb3 | -11.27927 | -60.58451 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3e915290-e92c-3680-8020-7168f4155e5f | -11.27877 | -60.61005 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5438c638-257f-372e-b070-9e8dbe07eeda | -11.27756 | -60.57331 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37f41711-e4ab-3443-8cf3-bd306db3f9aa | -11.27702 | -60.57688 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 838ce4b6-a78f-3214-ba40-78a9bde7e704 | -11.27647 | -60.58044 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99539b1a-5edf-3012-a21f-f716bc6808cf | -11.27592 | -60.58402 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 59ef874e-6e0e-33ef-8723-3620f6edc2f7 | -11.27543 | -60.60956 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8136fd77-8914-3513-ac91-e7a63606ac2d | -11.27477 | -60.56922 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19f9b8b6-0472-3ea8-b2e9-6227901b042c | -11.27422 | -60.5728 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b80fae6-2348-3fa6-b4e1-16a2200cc1f2 | -11.27143 | -60.5687 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50acaa92-ae31-383e-86a2-b36cfd1244f6 | -11.26809 | -60.56817 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c87b892b-1bd2-3e34-929c-8258df00fc3a | -11.26644 | -60.3842 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 077eb0c5-ca97-3928-ae83-a0e0e9845613 | -11.26589 | -60.3878 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c14cd956-4c16-3401-a1ef-8b731358490e | -11.26534 | -60.39137 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 33df37cc-e231-3a55-bd7e-af3084d2c9ca | -11.26199 | -60.39085 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3ad6b352-57c4-3ac0-aaeb-b024521f91df | -11.26142 | -60.56712 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2490e4ab-76a7-34ae-93b4-7601aea2d3c4 | -11.25937 | -60.62516 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81dccd76-48a7-3b41-91cb-095f6f1d93ce | -11.25919 | -60.38673 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f14c1171-ff76-346c-a875-719dc4eefad9 | -11.2582 | -60.48213 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 94a583dd-9f65-3aab-ad11-e8311034950d | -11.25764 | -60.48575 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4a4ca379-ac48-3bc7-83cd-fb54c177db8e | -11.25708 | -60.48936 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 759cc077-a3b0-32c1-b47a-cf47c7ffcab3 | -11.25698 | -60.57375 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed99c932-b604-3bed-88cd-d683eea6a76c | -11.25476 | -60.39328 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d01cf4da-16ec-30be-9832-2aba997459f1 | -11.25469 | -60.37133 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 40937131-034a-323b-ae6a-25b773ff46cb | -11.25359 | -60.3785 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fcdd517d-707d-3d31-998b-368c29b84b00 | -11.25141 | -60.39272 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1eb5d283-bbca-3aaf-b7fc-18d388c128a2 | -11.2508 | -60.37436 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 50012bd9-94a6-3c8d-88f5-2c62e2eda584 | -11.24698 | -60.57205 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ada4f62c-a33d-39c3-a1b0-72f33d64497c | -11.2415 | -60.50161 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 881d0c20-f766-3eeb-895b-bdf14bc4b0d0 | -11.23772 | -61.18316 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41c401f6-4bc7-3f65-a624-ead30bc18cf6 | -11.23772 | -60.57044 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2971d080-20e3-3deb-b310-d4106b912f1a | -11.23442 | -60.59182 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35b2cabd-4011-3b6c-b1f3-c1022ea7d4fa | -11.23387 | -60.59538 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68cc7a87-aaeb-3385-bc57-d241b93ac1a7 | -11.23277 | -60.6025 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84773701-6fa4-3ae6-a331-d207c11f81b6 | -11.23219 | -60.58417 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4de9f758-3537-3326-919d-87d7f2b69473 | -11.23109 | -61.1821 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7487a57f-5215-31f6-a3e5-828c918df2b5 | -11.23105 | -60.56939 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 503fc0fe-f4f6-372f-bdd4-a71ec2ff50f4 | -11.2305 | -60.57297 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cee5fb3c-0f58-3b16-9ca5-4425fafd5da3 | -11.22611 | -61.17052 | 2024-10-08 05:23:00 | NOAA-20 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39d76efe-662e-3ba2-8fa2-3ade16efcc2c | -11.21145 | -60.49669 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa3e60be-9a7a-33e6-82b8-4b0ed3028b80 | -11.21035 | -60.50383 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cb1ed99-0efc-33cb-a81a-cac12934f5d0 | -11.288 | -60.32483 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3377c526-d319-3b21-9c28-6b620b71f496 | -11.28464 | -60.32433 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d04eeebb-76d9-3d75-b876-a88955567ee4 | -11.28409 | -60.32795 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92600331-5069-341c-899c-89fce2e83554 | -11.28315 | -60.32034 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afe93840-85f6-3aa1-937c-5c5057e1523c | -11.43171 | -60.45407 | 2024-10-08 05:23:00 | NOAA-20 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f156ec92-1457-35ea-ae12-2dbd6bf91a9c | -11.26309 | -60.38372 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d9815ea-6723-3e0c-910b-7176b4d8b19f | -11.26253 | -60.3873 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 00bae881-bafc-3f0e-ba78-c335c51fc408 | -11.26145 | -60.39439 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dc58c4b8-7dac-3d5e-bf9a-d8a7b8b45456 | -11.26061 | -60.48262 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 57e67de8-5020-3401-82a5-37badd87b86e | -11.26006 | -60.48624 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1ebbbf3-0f64-3d3c-89e7-d09f2890b3ff | -11.25974 | -60.38317 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8b8a3efc-aae1-3c64-b3f4-a7c72d56ecb1 | -11.25951 | -60.48985 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf38c62c-102e-34ea-9267-acc33c8e66d1 | -11.25865 | -60.39029 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b3fb040d-c0cd-3b87-9210-7f90404f5feb | -11.2581 | -60.39384 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 871b2998-bbee-3392-b2ed-0810d856f9a1 | -11.25756 | -60.3974 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b525f485-e54f-3003-ab5e-e4ed7ff40511 | -11.25639 | -60.38261 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c98166b3-ac03-3d2f-a894-e8633cb1968a | -11.25531 | -60.38971 | 2024-10-08 05:23:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README123.md)
