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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 04b4009c-9a68-3d16-ac54-d2a43ad073b7 | -18.7445 | -49.20004 | 2025-08-18 12:36:00 | TERRA_M-T | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ae86f0ae-75a8-324f-9dbe-9a53bdb94158 | -15.60566 | -54.29818 | 2025-08-18 12:36:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7d79e56e-4663-3a57-94c5-82c0edb94b82 | -16.32628 | -48.89838 | 2025-08-18 12:36:00 | TERRA_M-T | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7388b36e-edcf-3a79-98d7-43b67bbf89e4 | -17.76086 | -45.58339 | 2025-08-18 12:36:00 | TERRA_M-T | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 4db468c7-9ab5-3699-9845-67d7c659de4f | -16.83222 | -48.92928 | 2025-08-18 12:36:00 | TERRA_M-T | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e5e4b43d-2155-34bb-96b3-5104b3d55214 | -16.79137 | -50.09567 | 2025-08-18 12:36:00 | TERRA_M-T | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fc0b418f-d85e-386e-8726-b94ab11576aa | -20.87692 | -54.97473 | 2025-08-18 12:36:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 24.0 |
| c372c970-1e29-36ca-b3bd-7b460a276242 | -15.70871 | -48.62714 | 2025-08-18 12:36:00 | TERRA_M-T | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2fb4bb6c-c153-30e5-bcb3-182725567651 | -20.87848 | -54.96455 | 2025-08-18 12:36:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eb19c4fe-2651-3bb7-a788-46e412b89f40 | -18.74606 | -49.18768 | 2025-08-18 12:36:00 | TERRA_M-T | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 623a1db0-519d-34ef-ace9-77db23ac5082 | -20.22912 | -47.05958 | 2025-08-18 12:36:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 5c810339-fcfa-37eb-9670-6d6f7b805ea3 | -20.21881 | -47.04076 | 2025-08-18 12:36:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 7dc94382-c4d7-36cb-bd66-a679df8a8c7f | -15.77133 | -47.79868 | 2025-08-18 12:36:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 237938bb-e524-3d66-8a27-615f43dd9d3d | -15.61341 | -54.31015 | 2025-08-18 12:36:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ddd3d90a-a6a4-3018-ab5c-7b525b64ec69 | -15.02317 | -54.79965 | 2025-08-18 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 314c05de-564d-3979-bdb4-0451588926a5 | -17.44242 | -45.15852 | 2025-08-18 12:36:00 | TERRA_M-T | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 479a198b-4791-3c8d-a1c9-ff3ff5fe40a2 | -14.96662 | -54.78016 | 2025-08-18 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 37.4 |
| bacfdddd-4491-3781-bd4f-ff1b46b12db5 | -16.32715 | -48.89298 | 2025-08-18 12:36:00 | TERRA_M-T | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d28af90c-53ab-3d60-9be6-40599e0dd5fb | -16.84233 | -48.93016 | 2025-08-18 12:36:00 | TERRA_M-T | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| ed755e8a-1e58-39c7-93c9-09355f4662b3 | -18.51782 | -46.27507 | 2025-08-18 12:36:00 | TERRA_M-T | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 4bb3071c-fa9c-314b-83fe-f4fcadc449e8 | -15.86483 | -50.21536 | 2025-08-18 12:36:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 200674e6-2725-3b4b-ba6f-23ef071472c5 | -15.01519 | -54.78699 | 2025-08-18 12:36:00 | TERRA_M-T | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f023c3a0-6633-31fa-b59a-f548f9626cda | -14.98778 | -54.77182 | 2025-08-18 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 769bee8f-2865-353a-bc26-008aec0e92c1 | -23.23097 | -49.51492 | 2025-08-18 12:36:00 | TERRA_M-T | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 5551a89b-4990-3478-9777-8954d1b6af22 | -20.40324 | -54.68786 | 2025-08-18 12:36:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 56bc6071-8b6e-3dfd-9601-c64465539586 | -15.80324 | -48.27969 | 2025-08-18 12:36:00 | TERRA_M-T | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8c3fc135-655d-399b-935d-19d00d9d3f12 | -16.43215 | -49.41449 | 2025-08-18 12:36:00 | TERRA_M-T | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a1bf3048-22f9-360a-b69c-08fb6a208a74 | -19.17538 | -46.55357 | 2025-08-18 12:36:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 53c355d3-99b0-3f5d-ab25-46488c9e92a0 | -19.15149 | -47.02694 | 2025-08-18 12:36:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 6ad5194c-045a-3d7e-8fdf-32f0ae011d6e | -20.86775 | -54.97336 | 2025-08-18 12:36:00 | TERRA_M-T | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5b508682-7274-37c2-b43c-585229fe3f00 | -16.84385 | -48.91829 | 2025-08-18 12:36:00 | TERRA_M-T | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 28096225-cdcc-323f-b1e0-c99d041e2266 | -14.98605 | -54.7829 | 2025-08-18 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 46da4264-1f0e-38f1-bbe2-23a1baf1682a | -19.17938 | -46.54138 | 2025-08-18 12:36:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 15.2 |
| e96637e9-ebde-33a5-a883-2e684cef7632 | -15.01341 | -54.79853 | 2025-08-18 12:36:00 | TERRA_M-T | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 48d02968-1676-3008-be4f-a3ab8dd0803a | -19.17737 | -46.5603 | 2025-08-18 12:36:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| d8b0763f-f5d8-3720-a499-38242cf9d11f | -16.83375 | -48.91728 | 2025-08-18 12:36:00 | TERRA_M-T | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7941cd5b-6494-339c-9bac-7d772df59aac | -23.55004 | -50.77356 | 2025-08-18 12:38:00 | TERRA_M-T | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 830e9958-f26c-321d-a8c8-8bcceb7cbc95 | -23.54859 | -50.78539 | 2025-08-18 12:38:00 | TERRA_M-T | SANTA CECÍLIA DO PAVÃO | PARANÁ | Brasil | 4123204 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| a684477f-f794-3277-8d6d-b3d2a5864184 | -24.74587 | -51.93337 | 2025-08-18 12:38:00 | TERRA_M-T | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| b8277cc9-2a9b-335c-9475-979551645483 | -24.74728 | -51.92256 | 2025-08-18 12:38:00 | TERRA_M-T | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 766dd0b8-fc60-398a-acbb-587926891588 | -24.86003 | -52.0291 | 2025-08-18 12:38:00 | TERRA_M-T | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 1ce9bbf5-c32b-34a4-90cc-ff8fa48ba5c5 | -24.75233 | -51.92962 | 2025-08-18 12:38:00 | TERRA_M-T | PITANGA | PARANÁ | Brasil | 4119608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 2464965b-e2cc-3023-9e5a-f4951ee9515e | -27.2121 | -50.66459 | 2025-08-18 12:38:00 | TERRA_M-T | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ec70b2d7-99d0-3ae9-8e6d-33ee5a72b61c | -24.86936 | -52.03037 | 2025-08-18 12:38:00 | TERRA_M-T | SANTA MARIA DO OESTE | PARANÁ | Brasil | 4123857 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| d6c5a434-0fa5-3b8f-b4a4-3bbdbb87b06b | -14.1897 | -45.3241 | 2025-08-18 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 16ce2001-ea6f-37b9-a96d-da8475d2cb6f | -13.1555 | -54.9357 | 2025-08-18 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 234.9 |
| e343e583-cc5f-3c02-9132-bf8113d6f398 | -9.3989 | -48.2994 | 2025-08-18 12:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| eb7d07d8-6389-396c-8064-203efe677e38 | -13.1558 | -54.9151 | 2025-08-18 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 8c0fedf2-2cde-39a8-9831-c8b7f10d94a5 | -12.6435 | -45.3269 | 2025-08-18 12:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| c0979b03-b5cb-39b2-8a3f-93e6294d9c1f | -13.8752 | -45.5179 | 2025-08-18 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 83.8 |
| c7534d3e-8409-345a-a886-2209e324ad63 | -14.1702 | -45.3276 | 2025-08-18 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 1f6b4f2e-c83f-3670-9019-32718c7f7bbd | -13.8748 | -45.5411 | 2025-08-18 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 7c616c5c-92de-3936-8b25-8f1cf719b71d | -13.1746 | -54.9337 | 2025-08-18 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 245.8 |
| 74c1aa53-967d-357c-b356-72dbd98a4349 | -13.1749 | -54.9132 | 2025-08-18 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 30a80402-e014-38cc-9a64-be2f92117455 | -9.3989 | -48.2994 | 2025-08-18 12:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 94767b37-b112-33f5-93b2-3bdb36e40c0a | -13.8748 | -45.5411 | 2025-08-18 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 23c77695-1777-36e2-826b-2629f318a612 | -8.3349 | -47.6145 | 2025-08-18 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 2ca79202-0101-394a-9e2c-97591e8c5ff1 | -14.1702 | -45.3276 | 2025-08-18 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| c7e1f076-e688-3fc0-ab43-e6f327b2f3f6 | -14.1897 | -45.3241 | 2025-08-18 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| f7a28ee7-8669-3fbc-952a-10ad65733c84 | -13.1749 | -54.9132 | 2025-08-18 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.8 |
| f2ebfa77-9400-32aa-a572-c16b0be567ff | -13.1746 | -54.9337 | 2025-08-18 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 312.0 |
| 6a174aff-f557-3b21-b106-3adfc35cd399 | -13.1558 | -54.9151 | 2025-08-18 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.0 |
| fc5c8a03-4244-323c-985c-8e35d531502b | -13.1555 | -54.9357 | 2025-08-18 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 260.4 |
| 6213a271-f345-3bb3-889d-8947fc60523d | -12.6435 | -45.3269 | 2025-08-18 12:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 20661512-1b86-32a4-b88c-cf5ca9d51424 | -14.1902 | -45.3008 | 2025-08-18 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| a3fa7976-45a9-36e3-8c77-af1398604f07 | -13.8752 | -45.5179 | 2025-08-18 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 4dd8c60d-913f-3669-950c-abedcbe4fcf9 | -14.1902 | -45.3008 | 2025-08-18 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 9bf29094-d38c-3474-afa6-00a3be97ead0 | -13.1555 | -54.9357 | 2025-08-18 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 245.4 |
| f2411f14-7d15-3c04-9b21-90c4a45e18b9 | -14.1707 | -45.3042 | 2025-08-18 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 7a7674ab-6dbe-35d4-8294-711e8a79b9ae | -14.1702 | -45.3276 | 2025-08-18 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| b4ae5a65-d7a3-3a3e-afb0-a8d04e8d281c | -14.9622 | -54.7766 | 2025-08-18 13:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 6a4a8569-62a1-31a9-970e-87d5ca002ccf | -14.1897 | -45.3241 | 2025-08-18 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 06f937b8-e253-30d1-9ad3-cb9c8fc9c53e | -13.8748 | -45.5411 | 2025-08-18 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 992db891-e5dc-399b-b82c-4e9d2564f647 | -12.2938 | -50.0121 | 2025-08-18 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| d350425b-2ef5-35ea-b26e-87c447f431e3 | -12.6435 | -45.3269 | 2025-08-18 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| c840eba1-54c7-3a3d-a9e7-d4370306d853 | -8.76 | -46.6878 | 2025-08-18 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 71a3b151-17dd-3894-8f98-f5377b420c3a | -13.1749 | -54.9132 | 2025-08-18 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 0ca5b330-5185-362e-8eff-568aca55a458 | -8.3349 | -47.6145 | 2025-08-18 13:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| d1070162-33cd-3f76-84c2-da21f0f4e701 | -13.2375 | -50.7972 | 2025-08-18 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 193.4 |
| fd3459e3-0929-3c30-a2b4-b169666d7c9d | -13.8752 | -45.5179 | 2025-08-18 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| d14cd0d7-0ec0-3fb1-907a-b761a5d3aec2 | -8.7602 | -46.6655 | 2025-08-18 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 23829f70-9e6d-38be-8093-7675bd5f4e65 | -13.1558 | -54.9151 | 2025-08-18 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| cf3ad307-6411-3b52-a315-778523e55bbd | -13.2567 | -50.7947 | 2025-08-18 13:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 79ed2abc-c8b7-38a8-b622-c77dbf8bd330 | -6.5203 | -45.4787 | 2025-08-18 13:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 6170e675-2c50-349c-82b7-c977bfa2b79b | -13.1746 | -54.9337 | 2025-08-18 13:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 236.6 |
| 0c4a732a-1404-3c8b-b4a4-1baaca383a55 | -8.7602 | -46.6655 | 2025-08-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 6af72f45-d510-3a47-b1aa-beeaeb0df0e2 | -14.1897 | -45.3241 | 2025-08-18 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 25775b60-1178-3379-a565-2009dd982941 | -8.76 | -46.6878 | 2025-08-18 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| e3cc767e-821f-3fd4-9fb5-6f14364382f3 | -14.1702 | -45.3276 | 2025-08-18 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 6fb3a87c-40e8-3f6d-a3b4-4fb665052f04 | -13.2183 | -50.7996 | 2025-08-18 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 876af7bc-1e01-3646-8861-266b156b5b85 | -13.8752 | -45.5179 | 2025-08-18 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| bf2b35fe-4147-3677-ac14-35841af504d0 | -13.1746 | -54.9337 | 2025-08-18 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 249.5 |
| c6432ae3-7a05-37e0-b103-4e6c764823fb | -12.2938 | -50.0121 | 2025-08-18 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 949972af-7c3a-3c41-b254-de35dd97683b | -13.2375 | -50.7972 | 2025-08-18 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 50055d7e-3051-39e6-9278-bffe115ea670 | -13.1749 | -54.9132 | 2025-08-18 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 35e19656-1dc8-30d6-a638-5b36c95c5999 | -9.3989 | -48.2994 | 2025-08-18 13:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 7dcadd7d-4691-3408-919f-8f6ff15135e7 | -12.6435 | -45.3269 | 2025-08-18 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 0d8c9f3e-72bb-38fa-8b9a-8e959c21e30f | -13.1558 | -54.9151 | 2025-08-18 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 125.4 |
| cb9d81c7-d374-34c7-9cce-63f2c2132272 | -13.1555 | -54.9357 | 2025-08-18 13:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 226.9 |
| ffc77a43-8a01-3c35-aa49-c95ade13d898 | -13.1994 | -50.7806 | 2025-08-18 13:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |


[Clique aqui para ver as próximas entradas](README37.md)
