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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4511947-755f-3b8b-8e72-d2d31a02e131 | -17.8029 | -53.76226 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 7554f8ad-0b65-3ab5-a046-2b343b909c7a | -17.80211 | -53.76589 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8a7b3495-cde3-32c4-9a63-282dbde6d83c | -17.79645 | -53.76372 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2652bbf4-633b-3c18-9c2f-c43aa6dfd5bd | -17.79295 | -53.77994 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 59852239-2618-38fa-aa1b-f6f4c102a2ab | -17.78432 | -53.76312 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0465fd3f-b9bd-39a3-b7f8-6d889a030dab | -17.78333 | -53.76768 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e578efce-1686-3e54-a668-69ea2fa4cdc2 | -17.78232 | -53.77232 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69ee1369-e93b-3343-9c56-2979909f669b | -17.77638 | -53.77141 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f5253ce-268d-3639-bdf4-c1d6926a8227 | -17.77537 | -53.77609 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9da3bbe1-90c1-3572-bfc1-4123ca058edc | -17.84028 | -53.7881 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 03c4c359-e38e-3f0a-af9e-7cd9c55e013d | -17.83797 | -53.78949 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| c1e57b76-bc09-346f-b1af-dc0db94e03ed | -17.8336 | -53.79066 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f484531f-6655-3231-8507-67ef0b1ac195 | -14.8112 | -53.89737 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f9fe5eb1-b676-3579-917b-c15cce6a23f5 | -14.8101 | -53.90253 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 4f26d2b5-9b8e-3b55-91ba-ebcb4e54c3dd | -16.49205 | -53.95575 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d14bbf4-ab8a-3106-bcb7-f948c7cb24c4 | -16.492 | -53.95726 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03989a93-8b84-3fd0-aec5-30db03eccdbd | -16.49109 | -53.96022 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de34ff33-9e00-318d-8fda-cce951c48e87 | -16.49101 | -53.96176 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de2e8995-12c1-3ee7-9329-5f8b501ee223 | -16.49008 | -53.96498 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c9b0449-2b49-3406-bf59-84eef244edda | -16.48993 | -53.96665 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cad820ee-d836-385d-9024-e771892fe145 | -16.48603 | -53.9555 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e5d1086-2210-36a2-9833-547928583ea8 | -16.48512 | -53.95847 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5224c8ec-b034-324d-bf7b-671201b23edd | -16.48504 | -53.96 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62b2cf7b-4e6b-313f-b254-784ac783bf64 | -16.48413 | -53.96309 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eba72f1a-71ad-3a8e-9359-4499a02ed6ce | -16.484 | -53.96473 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b6270e56-5e44-3a33-8877-1ad6e055b81f | -16.48309 | -53.96802 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b00babc7-0686-3b87-99b3-e4fe10b6119b | -16.48291 | -53.96965 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 35cfddcd-dd2e-326f-be30-080e52a3e98b | -16.47906 | -53.95827 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac2259ed-5f2f-3653-a43f-42e1ca7d2b7d | -16.47812 | -53.96148 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 827e0af1-12b8-398a-8694-4d950643e20f | -16.47799 | -53.96316 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1cbe2862-8669-3f84-b349-72ab2358f77f | -16.47706 | -53.96649 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cfeea41a-1d1f-3f5b-9ec2-e2ec5d6f7052 | -16.46485 | -53.96504 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2228e7c-1960-3fee-8f1f-0302ebdbb435 | -16.46391 | -53.96857 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a1ce89b1-7943-34f3-9334-3319bd3d1545 | -16.46366 | -53.9704 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 09bb84b5-8a72-3f52-b52a-670b6d56fa22 | -16.45931 | -53.93075 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8aa8f6a2-62d3-3333-891d-4be6450ad27a | -16.4578 | -53.96742 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5cac9ee-8e94-360d-94b8-25516e947b4f | -16.45668 | -53.97264 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 57315cf9-6fad-3d41-9575-b49496f0510c | -16.45321 | -53.92964 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e76400d7-5e12-34a6-91ec-c3b43d9a1f8a | -16.45168 | -53.9663 | 2024-10-07 04:02:00 | NOAA-20 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2faf9db7-271a-390d-b4da-0a7cefcb99a7 | -17.32687 | -55.04391 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5b436eba-aa41-373c-b495-b7e2d273b256 | -17.32585 | -55.04244 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1fbd08bc-f034-33c2-88ba-7a3c58031d7c | -17.32464 | -55.0479 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 041235c6-7252-3ea8-b662-bd59f61908d3 | -17.32054 | -55.04235 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| fecc8c3c-88cc-3065-975d-6b7273f688c4 | -17.31953 | -55.04086 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b6b14d74-a4d1-3306-9e9d-ab915875aa5b | -18.07791 | -54.3195 | 2024-10-07 04:02:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35cdf67f-6106-3c1a-be42-91662a5ddd15 | -18.07205 | -54.31744 | 2024-10-07 04:02:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e15fbe0-dedf-3125-97ff-0f2be504aa05 | -18.07088 | -54.3227 | 2024-10-07 04:02:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66fe0aad-0699-309a-a80d-13b81b402e29 | -17.83908 | -53.79379 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 90df9f7e-ea09-3c2d-bd52-088ab868d7f7 | -17.83802 | -53.79878 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c466dc4d-0d7d-3b0d-bc6f-9df3ea4185e1 | -17.83708 | -53.80319 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c9e15835-05b1-31b8-afb3-6369203db628 | -17.83662 | -53.79563 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6b2d87c0-004f-3da7-aef4-5ab2ed28d03e | -17.83557 | -53.8004 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c92f8fc1-33a3-35d5-8773-adc05f740ecc | -17.83457 | -53.80493 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bff406f9-2cc0-3428-ac4c-fe5f06662c58 | -17.83224 | -53.79712 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 693ea1c7-f66e-3de8-b5a1-0f0a5570b158 | -17.83123 | -53.80185 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b29403da-8841-398c-8596-2d8ca6a2ddaf | -17.83101 | -53.79323 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e1c88cc6-9bd4-3007-ac6c-711d3fd53913 | -17.82976 | -53.79888 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b5e0f1ea-00b1-316b-8af1-bcea6eedc382 | -17.82871 | -53.80363 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2a8dc12b-bf67-3ef1-b228-ab57ea73d676 | -17.82653 | -53.79508 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7c90ab5-57f1-3019-a2ae-0090db72836a | -17.82401 | -53.79709 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed4d9f16-6e78-313a-8c46-7fa06b3558f4 | -17.7944 | -53.8017 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c4c3509-6d93-3f54-bc40-3c3981409dc6 | -17.79339 | -53.80641 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4e8ea7d6-9ddf-3b15-888d-2e634fe66035 | -17.79239 | -53.81103 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a369cc1c-e962-39c7-85bc-04667876e867 | -17.79141 | -53.81557 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a15a7636-6205-3695-aa9c-fae76c8ff596 | -17.79092 | -53.78936 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 23.5 |
| b39f588f-5884-376a-88d6-f20ed5d755bb | -17.78985 | -53.79432 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1e9b4b0a-69e7-33d9-806d-594f5558da35 | -17.78872 | -53.79954 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0c4492a0-89e1-36ff-9bad-81b591c835f8 | -17.7876 | -53.80474 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| fe6aca8b-19da-3342-943d-191265aa7ab8 | -17.78658 | -53.80944 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7136cbd7-0203-312f-8d0c-8d27720e181e | -17.78558 | -53.81406 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4598007d-ebb8-3960-897e-e27db4e6c306 | -17.7846 | -53.8186 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1056065c-fa3b-3495-9ed2-1a2ee5100bf1 | -17.78363 | -53.82307 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 21e60b20-6acc-32c5-abb2-79af7d764265 | -17.783 | -53.79754 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 9610fd3b-e689-3921-9834-103753c02689 | -17.7819 | -53.80263 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 55fb008b-49f3-3aca-bfb5-cff29eef5913 | -17.78084 | -53.80754 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 2791e7b0-740c-36b1-a12a-4586176fc76b | -17.77978 | -53.81244 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 604d95fd-0998-3463-b0c9-f13248e2a64e | -17.77878 | -53.81706 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d7bcab88-3a70-37da-8a93-ca9692b57bfb | -17.77827 | -53.791 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 61cdb355-1013-3002-957d-b55103204805 | -17.77781 | -53.82154 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c11e01e4-a0ac-3077-a7c2-0786cebdec55 | -17.77718 | -53.79605 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 90a4962a-01d7-35ce-a529-6756fa1887b3 | -17.77686 | -53.82593 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ac8e9c35-1ad0-346e-a6be-00d7d0019949 | -17.7761 | -53.80105 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 31bb0d42-3544-3440-bcba-7e88bfcc3162 | -17.77501 | -53.80608 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ec59bc22-959a-37ee-a405-bfbca6b99e10 | -17.77395 | -53.81097 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1d6075bf-8c3a-3c14-b27c-c83d9aad1857 | -17.77232 | -53.79014 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7009d841-016c-351a-aa57-1018facaffbd | -17.77133 | -53.79467 | 2024-10-07 04:02:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53c38011-39ab-3679-a481-c5fc4b719ef1 | -17.181 | -53.92714 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0219c07a-b22b-31b3-bf19-f7954b6072da | -17.17995 | -53.93196 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d117a6a-e0e2-371e-ae58-9195734322d4 | -17.175 | -53.92597 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df261f16-637c-3179-9305-dc90eb4fe90c | -17.17394 | -53.93079 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58217254-a6f6-354c-a839-5c0b70e3525e | -17.16792 | -53.92966 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2330df39-f882-3981-97fb-03c73332d51b | -17.16479 | -53.94395 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 166b3f0a-1c38-38fb-8875-357de421af69 | -17.15985 | -53.93789 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 459aba72-195d-35d2-b3fe-0934994d898d | -17.15881 | -53.94262 | 2024-10-07 04:02:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c942bc4-4e13-39b8-90fd-2ef2a518ae68 | -17.0286 | -55.07386 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8e972f64-4fa4-3bbc-ac88-2ca0c7fd4909 | -17.02223 | -55.07225 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0b34088b-d168-3230-b2ee-b6cec43b61a1 | -17.02209 | -55.06948 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 91447211-b4aa-33e8-bad1-9ed013139902 | -17.02098 | -55.07779 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 107e014d-e6bd-3db4-a2ac-ab8cc0be9065 | -17.02087 | -55.07503 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1cda03a4-17a0-3500-86bb-5636b24dc128 | -17.01974 | -55.08331 | 2024-10-07 04:02:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |


[Clique aqui para ver as próximas entradas](README61.md)
