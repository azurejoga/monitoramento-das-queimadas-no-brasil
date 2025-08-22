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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 270f61b7-aecc-3c55-8148-8dc1c6dfa6a1 | -8.8872 | -62.42829 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a3bbd40-6f42-34d6-a99a-4bfe6ed4319b | -7.55655 | -63.8435 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aa9ba92-c81f-39ac-9d65-63f29a24de6f | -6.63271 | -58.41235 | 2025-08-22 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db2f737b-0111-3b5b-9a1d-dae81806c1fe | -9.47354 | -57.8267 | 2025-08-22 05:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 160baac9-3b51-3752-992e-4a7f77d64dbd | -8.86592 | -62.41055 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06f68fa9-cd56-37d0-8a14-326cea997453 | -9.15758 | -59.60011 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bbbc3e7c-978f-3d4f-b8e4-03adc9f02894 | -8.88015 | -62.40897 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b27263ed-1170-33de-a295-1ddec16788aa | -7.6247 | -69.94435 | 2025-08-22 05:38:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 606c378c-4b29-350b-8400-f29382b8adbc | -5.44021 | -60.16141 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd2b491f-5246-3e7b-8d15-48841348fc71 | -8.60025 | -62.61753 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d01baa67-a412-387b-820d-626432173021 | -7.54549 | -63.84887 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e0aac71-3c9f-37a7-b9da-b89f2f798589 | -10.86501 | -50.83978 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 14eb5618-f514-349b-914f-33cf7f0482da | -6.4374 | -53.38385 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 496847f1-7525-3274-8aa4-8b11bb2e7a39 | -9.65824 | -59.63699 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb151fba-5b60-3a51-b7d0-4bf15cd55ff4 | -7.72657 | -66.92395 | 2025-08-22 05:38:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5c9ff85-57f0-31ed-a21a-026943f4a533 | -9.18463 | -59.63153 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 019b621e-5322-34b7-86aa-63a7ce762959 | -7.29493 | -59.62695 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d311ebcb-edaf-30b2-91f4-25742045c2e0 | -5.79959 | -59.21721 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 313414d8-4322-3b7f-b3bf-f757788e5c30 | -5.80526 | -59.21987 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a36ceccf-94e1-30c9-9b39-b47a4d4e5ba8 | -7.50395 | -63.83159 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a973ab5-3d26-3111-a450-ba320158b7c7 | -8.86136 | -62.39473 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8942fee8-431a-3b1d-8ffe-d5566026559b | -7.55158 | -63.8534 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6359b0ef-d32e-3176-a6c5-0dbe0fe69f47 | -8.66657 | -70.03961 | 2025-08-22 05:38:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f7b3aac-3961-3fe4-94f1-18371e93d52f | -8.88378 | -62.42775 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 26e9378c-9354-387c-8d8b-57fd9be25017 | -9.21152 | -59.45255 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 915ab89a-c757-372d-98cc-12524464cae3 | -9.2736 | -60.77963 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 382a4de4-66e7-3e6e-9e64-63ca6bbe51b7 | -6.44946 | -53.38144 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d22f9d82-b0b3-3c09-86b9-424192b6e4b8 | -5.24084 | -62.86575 | 2025-08-22 05:38:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 54f09548-5b2e-35ea-8665-93eb473da67f | -5.87782 | -57.75549 | 2025-08-22 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f511170c-c8c6-3d17-915b-5dabd942e52f | -7.55823 | -63.85445 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ada5dce-2192-31bc-8aca-a15bc89bcbfb | -6.26947 | -53.70906 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e84ebc06-451a-30ed-872b-d3edf032d6c2 | -9.17945 | -59.58805 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1f16450-08c3-3390-8105-f6cac6f52b07 | -6.63031 | -58.54106 | 2025-08-22 05:38:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b37b0cdf-f1d5-3e8c-a720-440b8eb5eb5a | -9.21883 | -59.78359 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bbca9d2-dae7-36e7-b895-b17d5bce9022 | -9.23404 | -61.02308 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f3424e9e-3cc3-373b-934b-742cfcde4608 | -10.13585 | -65.28632 | 2025-08-22 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| dbc120e4-5223-3771-927f-a190ae6e89c8 | -6.90018 | -59.89984 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 706215f6-2a61-3f0f-b890-d73b781020a6 | -6.44891 | -53.38545 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94b7976d-9be1-3272-b6ea-650bc4046658 | -6.16608 | -53.77533 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cc0ff00-03d1-3e76-873c-a3585b667ab4 | -6.89656 | -59.89705 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44913301-a14e-31ff-8226-348ba4a43308 | -7.58856 | -63.44548 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98ac768e-f30a-3328-94a1-ce437f6d2d55 | -9.19243 | -59.6362 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c02b01f-3b33-397b-be55-fe8388e222ac | -6.56116 | -60.05834 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d841b67-5e8f-3019-8d8b-c72adef78361 | -6.26996 | -53.70544 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5694f473-4b96-34eb-b5e6-5c489ce59c52 | -7.78113 | -66.95689 | 2025-08-22 05:38:00 | NPP-375D | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dd9ffd6-d117-3727-a38f-1ba894027835 | -8.61098 | -62.61549 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36362acc-0d5b-3943-94b3-7f32a9199aec | -5.88868 | -53.63636 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7067611-cc57-3d02-a7c4-62f5cd7ae93a | -6.89725 | -59.89256 | 2025-08-22 05:38:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5e693443-975c-30c2-b0b9-71e15ca698a0 | -10.46407 | -59.13714 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 216859a7-bb8d-33eb-aece-b65b9055137c | -5.14727 | -60.37306 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 189d037b-f204-34c7-86f2-50151196bcd8 | -8.5515 | -66.95027 | 2025-08-22 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32356be8-9328-30fb-a4b1-26acb6c3aef8 | -6.44757 | -53.38713 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b46dee5-7f5d-3c55-8743-2e13b565d7df | -7.63336 | -69.94588 | 2025-08-22 05:38:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68d9db6c-c581-3af3-a134-f397120b4317 | -9.23466 | -61.01886 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2be60ce9-f9f4-3fc2-8bb5-69cbace2cd9d | -7.5034 | -63.83507 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3785298-8977-38d1-8b5a-817adf484a82 | -9.75189 | -62.77051 | 2025-08-22 05:38:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5e7d4069-8054-372d-8254-a12e3158ddf2 | -5.88055 | -53.6327 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 743b9015-096b-3b1f-a4c7-aafbbe01eb9f | -8.4402 | -63.86204 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 393bd07d-0d75-322b-b53c-52e9f80d70e3 | -6.61791 | -60.00859 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f9c5c61d-9459-3e05-ad36-d2e82816f1dc | -8.87502 | -62.41954 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d476e00d-92bc-3e30-b01f-c2a1332b0eaa | -5.23806 | -62.86176 | 2025-08-22 05:38:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 385af018-826d-3f16-9613-21683bdf5d69 | -5.88261 | -57.75236 | 2025-08-22 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec5ddfef-ae57-348c-ac26-57a7df5d9211 | -9.88342 | -60.28868 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b5e7f346-6979-3fab-ad44-fcbe67dcb248 | -7.54494 | -63.85235 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cd4b092-1ed1-3538-9565-723bdf1ecaef | -5.87547 | -53.62818 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1bf45c65-a770-3b3d-8cee-9899b6bd2170 | -6.16282 | -53.7686 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36f1462d-fa10-3294-8b15-c4ca890e6f87 | -11.9036 | -55.89238 | 2025-08-22 05:38:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f733296-dd7f-3366-bdcb-868fa0166e39 | -5.80454 | -59.22456 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3096fad8-5f98-34f0-a7f4-f496ea567e17 | -8.60759 | -62.61496 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f6994bd0-d29e-30d2-b632-b4f8ae0449da | -5.88563 | -53.61693 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 691cb474-9bfd-3514-854c-fb3ac62397b4 | -8.42771 | -70.70837 | 2025-08-22 05:38:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a30b7307-1936-39a8-9b51-ba0da0bd98e7 | -5.87235 | -53.63013 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d03520ea-9458-3443-912d-d8d64a51cd68 | -5.87953 | -53.61963 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e22c783c-09e8-3f5b-9710-dd2999dfb926 | -8.87218 | -62.41531 | 2025-08-22 05:38:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ed0dc30-0966-3156-8c9a-737543952b7b | -7.62833 | -69.94928 | 2025-08-22 05:38:00 | NPP-375D | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e19616c-0248-372c-87fd-59601a2a04a2 | -9.90315 | -60.28682 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9bcd89c3-c79b-3f8d-8787-138a1f94e8bd | -9.21212 | -59.46475 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba4887d0-63ce-3248-8017-a93e6676bc92 | -9.10136 | -61.43403 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e7f6d78a-7548-35f2-b6c4-bdb240e8ab48 | -8.59969 | -62.62117 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9b8856b-4b74-3285-b0de-32ec4afd014e | -10.02133 | -64.83964 | 2025-08-22 05:38:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a1538b9-f492-3c3c-b982-c57eb1b34637 | -8.6155 | -62.60874 | 2025-08-22 05:38:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2ab233e-9808-3f35-ab4c-f121daf6b09d | -7.08682 | -63.0837 | 2025-08-22 05:38:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1146e4d5-9039-30d2-b2f3-c02a9a8c7eac | -5.87901 | -53.62336 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2abcf1a2-b2ea-3361-b0f2-26c8f024b9f5 | -7.50285 | -63.83855 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b981306e-551c-35e1-906e-ac6a310bdeaa | -9.31514 | -57.01455 | 2025-08-22 05:38:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 206d8d5d-6d48-3074-83a1-7b1658ce2002 | -9.19455 | -65.66476 | 2025-08-22 05:38:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ca681a0-a325-3f57-a738-4a0ba4bbedcc | -9.2114 | -59.46986 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 424e6bb0-3175-30a7-aa26-ce27ea1f8bc3 | -9.20982 | -60.78516 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| edb097c0-6462-37c8-b4ba-f72cb4d32058 | -6.62862 | -58.41168 | 2025-08-22 05:38:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d5c721c-27a1-315e-8e9c-353aa593fc0c | -6.62161 | -60.00921 | 2025-08-22 05:38:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a72e9242-e016-3f17-bd26-663e59727d2d | -9.75529 | -62.77104 | 2025-08-22 05:38:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ecf2c7b0-dfda-3aba-bf96-1dbabb637121 | -9.18851 | -59.63556 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4449ff79-37ce-38bd-b449-a60b649559cc | -10.86098 | -50.81102 | 2025-08-22 05:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 904fab36-2a33-3aac-b25b-339e9c965a5f | -7.561 | -63.85846 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8833809d-d2c9-3901-88ff-18955d2f18bf | -9.16865 | -59.60689 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20cc2abc-af03-3e1b-856d-87e14db75cdd | -9.2383 | -61.01941 | 2025-08-22 05:38:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 052aa741-684d-3ca6-8785-c06a2e3394d4 | -6.57605 | -59.87318 | 2025-08-22 05:38:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3545faa1-6b66-3a02-b26b-4ebeb6b0e732 | -5.88324 | -53.61418 | 2025-08-22 05:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af261df5-a028-3b7d-abdd-aa893ac051dd | -9.52748 | -60.54324 | 2025-08-22 05:38:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3c4cfee7-db28-3aac-af3e-ef7fad0127ed | -7.54826 | -63.85288 | 2025-08-22 05:38:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README57.md)
