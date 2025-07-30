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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a635521-64f4-326e-ab60-ed858ed8df08 | -6.52244 | -56.20236 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e055aa0a-ddc4-36f9-8900-2cc86e8c7ddb | -6.49856 | -56.19807 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d67f5edd-6eba-33b9-8bdc-d55e98e4691b | -6.62411 | -59.98356 | 2025-07-30 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3ead007d-a66d-37bb-adf9-0f9d6cad4f13 | -6.56305 | -56.18707 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e44ea0f4-65d9-37e5-96b5-39aa1798dff3 | -6.54638 | -56.18821 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e621adb8-aa67-36e6-8f5f-2259f31f0356 | -6.50628 | -56.19997 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a05a6f3-8626-3d6f-8821-75d5e3e05ea4 | -6.45548 | -53.35777 | 2025-07-30 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74b0154e-3801-36d7-9508-e2d29ff74aac | -6.53183 | -56.21415 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d2b6845-d1eb-37b2-9bf8-61aa13b9ee4e | -6.50347 | -56.20222 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e4ff66cc-915b-3fdb-ba9c-9e0e7cd56f56 | -6.50444 | -56.1954 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e39da9ed-ac56-3555-ac86-e05b6029fa9f | -6.49808 | -56.20147 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f1d8d6a7-d763-34c9-a15b-ecf6b82e0576 | -6.49365 | -56.21218 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fc299928-9bd8-3f9e-bfc5-e444ed9b0490 | -6.56354 | -56.18358 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca8b81bc-7572-3bb1-af97-74cc11a12059 | -6.50134 | -56.19582 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8c5b365f-7d5f-34f2-a35f-816c5ab4b688 | -6.5297 | -56.18944 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4c63a3d8-ec3c-34b7-bd94-458bf8111125 | -6.49146 | -56.0122 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b47afcbe-4772-34b7-b886-2eb177757bd7 | -6.50042 | -56.20264 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1e9d8049-82f6-3dae-992f-193e6513e200 | -6.52197 | -56.20582 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a8d2f664-85c2-30a4-a108-cf7b980cc143 | -6.50395 | -56.19882 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 729d60ba-b0a2-348c-ad68-5fbec6e40363 | -6.50249 | -56.20911 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 177ff824-0681-3a69-a954-aa2a1704586f | -6.56894 | -56.18432 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d865d0e-352b-34ba-819d-c5620dc30473 | -6.52923 | -56.19286 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| cbd03713-9acd-3bcc-abe1-f2051b1fe12d | -6.56799 | -56.1912 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ddb0e66-b8bf-3adf-9adc-9fa2b61af843 | -6.62775 | -59.98788 | 2025-07-30 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06a8c2d9-56c4-3eb3-8c4a-53058bd415f4 | -6.50151 | -56.216 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66f7d2bd-c5b4-3a29-903c-11b1350c8bd9 | -6.5269 | -56.21002 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9630bce1-9d78-3497-a2f8-530971c308a8 | -6.49811 | -56.21989 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17684e33-95c3-35f5-8d00-285f3bfea0a7 | -6.50674 | -56.19654 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 8bd9852f-b0bb-3b86-8034-58d25660388a | -6.52783 | -56.20318 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 239f5539-69ef-39d0-8042-59909980aecb | -6.62047 | -59.97923 | 2025-07-30 05:42:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8d30aa01-a5f8-3b98-85a0-2455be264924 | -6.50088 | -56.19923 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 625bcdb4-86b2-38dd-a8fe-38bdae69b692 | -6.50442 | -56.21379 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eab3c1c7-ab46-3ce2-9daa-d7450c69fda7 | -6.5283 | -56.19974 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c728170-abf5-318f-a3b0-3a03ec0efe56 | -6.50299 | -56.20564 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc68b50d-6db8-301b-892a-a802f35aadcb | -6.64957 | -58.82512 | 2025-07-30 05:42:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7e9f0b81-9994-353f-ae26-39367a9fb272 | -6.49075 | -56.2144 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6aa0b9d2-5d58-3bf8-b507-aff94a603abf | -6.49613 | -56.21523 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 85314c29-05d8-3271-a62d-523dc8306071 | -6.51028 | -56.21103 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 443dadf2-ea85-37c6-a916-bf0f1a858e6c | -6.56258 | -56.19051 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f3bcfb1b-6601-3f15-a4a6-68484726d60b | -6.49319 | -56.21563 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c31e61f3-722e-37ab-9737-66fd2f4b93ed | -6.55766 | -56.18626 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d0c3268-60df-3632-9c20-8d193bf3ded1 | -6.49027 | -56.21783 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b5999df8-f640-3bbd-85b5-60d3b20772cb | -6.55623 | -56.19664 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30d914f7-da16-3953-b6d3-fba58aea0087 | -6.5072 | -56.19307 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 13e9632c-5787-3103-a7ee-8d58337dd5f7 | -6.49905 | -56.19464 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9ac9b096-39e8-336d-bac2-facf8bb7a662 | -6.50395 | -56.21721 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b1b665cf-5d15-3cfc-916d-3382fe687be6 | -6.49996 | -56.20607 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a351122e-8b87-3daf-bc9c-1e49c7832c42 | -6.49857 | -56.21645 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 65c76d8d-4c8a-3cb2-b4c2-97b2b85abff6 | -6.50488 | -56.21032 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0aa6093-3ac4-351b-94d5-c27af426c6f2 | -6.45421 | -53.3633 | 2025-07-30 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 43b7832f-4772-3fb7-ba3f-acc8bf8f62c5 | -6.52643 | -56.21345 | 2025-07-30 05:42:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9fc4962-7fbe-3a8b-983f-ff7dcb7113df | -9.4556 | -57.84978 | 2025-07-30 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd36ab0f-e45d-355e-927b-a19625af7538 | -14.41373 | -59.33939 | 2025-07-30 05:44:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f483925-35ef-39f8-bfc0-556b6b6edeb8 | -7.10603 | -63.04828 | 2025-07-30 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7438153e-93cb-3a61-89c1-425a36d55425 | -9.31372 | -62.6515 | 2025-07-30 05:44:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9c1d4d0-3974-3a48-9d7b-be2902d0bc7c | -9.45582 | -63.20884 | 2025-07-30 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba9a8da9-7818-374d-9090-0055ef85feca | -7.10252 | -63.04774 | 2025-07-30 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45d93a06-78ea-3b5d-95d8-4e624c1355db | -11.93854 | -63.85478 | 2025-07-30 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f07cabc1-28b1-349c-a601-2c99b4264913 | -9.67113 | -63.17068 | 2025-07-30 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d68038c-a610-33fe-a283-59e64656f906 | -8.32426 | -54.75553 | 2025-07-30 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc89f305-e2fb-3d12-baef-dfafb54c1a2f | -14.41305 | -59.34491 | 2025-07-30 05:44:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5fb5c922-28ad-3fcf-8edd-1af647c7d811 | -14.50923 | -58.8019 | 2025-07-30 05:44:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9ceb631-6e2e-3447-95fb-10b33c41e091 | -9.45599 | -57.84688 | 2025-07-30 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b33c15d-8ff8-3d8d-a987-030075190e76 | -9.46063 | -57.85052 | 2025-07-30 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a49ee59c-9670-3856-a4c7-d978be4bd357 | -8.33703 | -54.75234 | 2025-07-30 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07606d01-9ba6-34e5-b7aa-0e2c87556155 | -8.31534 | -55.10956 | 2025-07-30 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11f8b232-b74a-3c39-8881-f8ac3dfd87df | -8.33642 | -54.75707 | 2025-07-30 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b58f0013-9b88-3381-9191-8bf55ed801ff | -8.33093 | -54.75164 | 2025-07-30 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f648ee22-f164-3909-b636-a3ea56ff8a63 | -9.46101 | -57.84764 | 2025-07-30 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53f41e48-4149-3e44-8759-476e7f041b61 | -12.25507 | -63.81436 | 2025-07-30 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a1f64d7-9fcb-3b1f-ae37-ea64be2bd4d0 | -9.66754 | -63.17013 | 2025-07-30 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 102c3326-a6dc-3b94-9447-3f51379d1f28 | -8.33034 | -54.75631 | 2025-07-30 05:44:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e59f8e5-b5ce-3919-b0cc-db0d7a419a02 | -7.10312 | -63.04381 | 2025-07-30 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f16f1f06-935b-3139-847d-3abc4c3a61f2 | -7.89901 | -61.52233 | 2025-07-30 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9ea9ca12-38e2-35e4-87a3-e2fb7a2e5fdd | -7.90101 | -61.52071 | 2025-07-30 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ac42f22-1933-3b05-9d32-f72a09995422 | -10.15325 | -67.22977 | 2025-07-30 05:44:00 | NOAA-21 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 942f053f-5df5-3762-8d5f-95929cacc40c | -8.61448 | -60.60294 | 2025-07-30 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af9b3b49-c589-335d-9df2-1d0b909e86da | -18.44722 | -54.6684 | 2025-07-30 05:46:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26614f78-bccb-341b-a892-339993a6cc40 | -10.6169 | -45.2512 | 2025-07-30 05:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 5abd75ad-7ffd-3dd4-b006-6d71303062cd | -10.6169 | -45.2512 | 2025-07-30 06:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 6aaf51eb-515d-34b9-81ef-2274486ff876 | -10.6169 | -45.2512 | 2025-07-30 06:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 1ac967ad-0c89-36d9-868a-b93aaac6cf7d | -13.0873 | -47.3074 | 2025-07-30 06:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 1a83ef64-145e-30ad-a391-d90251df6d3a | -7.10508 | -63.04803 | 2025-07-30 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5074c351-c201-31bf-9458-a7be5f155051 | -7.10552 | -63.0449 | 2025-07-30 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff019207-a9a7-3f77-9095-a1cc0c196676 | -11.93572 | -63.85477 | 2025-07-30 06:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffacbeab-19b1-3b53-8c96-186e95327b7a | -11.94099 | -63.85548 | 2025-07-30 06:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0e6cb75-2b57-38ae-9921-76477c0f988c | -12.25528 | -63.81356 | 2025-07-30 06:10:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 477a385a-fb36-33ff-9d99-ff0d4bed0b5d | -7.09988 | -63.04729 | 2025-07-30 06:10:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8048b4c-54a8-3264-bfd0-33d298973ca6 | -11.94058 | -63.85495 | 2025-07-30 06:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13148ab0-702c-3b48-863d-b530537b7566 | -11.93531 | -63.85422 | 2025-07-30 06:10:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5d89f2c8-194c-3603-9927-db1ae4ffe7ce | -13.0873 | -47.3074 | 2025-07-30 06:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| cb8b6a03-6a8b-3a0f-b475-8eb3996ce80f | -13.0873 | -47.3074 | 2025-07-30 06:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| fc1aa720-1777-37c0-82e9-0159dd725715 | -13.0869 | -47.3299 | 2025-07-30 07:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 6c385e3f-ef33-31f2-b92c-f1a2ac3c61d3 | -13.0873 | -47.3074 | 2025-07-30 07:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b5a0ee5f-8b89-3cfb-808c-4b5ecca76c60 | -12.6129 | -48.0673 | 2025-07-30 08:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 5001ed72-ccfe-35bf-ab10-cddaaf7402fe | -6.1366 | -42.5544 | 2025-07-30 10:10:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| 3caa994a-e7ba-3da4-a697-274601e90449 | -8.0425 | -46.9132 | 2025-07-30 10:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| dadb264b-d643-3e99-9669-9c9dd95603ef | -8.0425 | -46.9132 | 2025-07-30 10:40:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| b5cc5253-9809-3d46-87c9-61728505c31a | -8.0425 | -46.9132 | 2025-07-30 11:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 530d01ce-e5cf-3f97-8d7f-699afd9f1c85 | -7.70088 | -37.51313 | 2025-07-30 11:32:00 | TERRA_M-M | TABIRA | PERNAMBUCO | Brasil | 2614600 | 26 | 33 | nan | nan | nan | Caatinga | 13.4 |


[Clique aqui para ver as próximas entradas](README34.md)
