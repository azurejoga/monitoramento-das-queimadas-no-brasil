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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36af9a97-46fb-3aba-a2ef-df86f59310fd | -6.71251 | -58.57018 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 019ed5fc-dc84-34b0-835d-b10fbc5427ce | -6.24827 | -60.02162 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0584a729-dfca-396b-a50c-5bfe820b6265 | -6.7861 | -59.67412 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fafc2e84-42e9-3ce8-ae66-9bf63965c19d | -6.77268 | -59.64952 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85e175ae-16c5-33eb-857e-12f79e703aa6 | -5.31613 | -60.19287 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88e790e1-8276-39eb-ac9a-d9f02b6245b3 | -6.79302 | -59.66681 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6be64384-cede-3ba1-afce-fe2333eabdfe | -6.68539 | -58.53663 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82c63da6-1cc0-371c-b1fd-8bbba2e68d20 | -6.71076 | -58.56369 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf7b8891-3eae-33e8-a348-13bd40af0ad3 | -6.91271 | -59.36347 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11a636ef-1eb8-3e5a-a03a-f482438f2d61 | -6.24984 | -60.0104 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cee0848f-df8a-3c52-bac1-47376d35d6e4 | -6.69094 | -58.54251 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b2246fd-ff17-31e0-afcd-0bef0b30bd05 | -5.30858 | -60.20376 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7526f649-88f3-33ad-bb48-329da1733c3e | -5.3036 | -60.19944 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 561ff37a-43fa-3c3d-aa80-d12a0df9f58a | -6.23853 | -60.00898 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| bfe6b8df-0620-3fdc-821c-ad416d2084db | -5.31563 | -60.19644 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2bc951f-f5ce-3b1b-9dcd-3848e461579a | -6.70203 | -58.55418 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 61c32769-e0d7-3fd7-8dfd-8b14f9a1344d | -5.30315 | -60.2055 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53ea0784-d9ff-3566-9cdb-c6c6ec9cc666 | -6.26058 | -60.01587 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2922d737-dadf-3bf5-99b8-ac242ac21ac0 | -6.24523 | -60.00225 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7dfaaf56-6ed5-3832-8fb9-e06e2959a8fe | -5.30257 | -60.20649 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad6e428b-8ad1-3467-a0b2-fc1d588f2da6 | -6.77973 | -59.67738 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63a1dc38-531d-322f-999e-75d56b5a758c | -5.52688 | -60.2086 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b9fb1ade-a721-3a1b-ab4c-e36e4bb76f44 | -5.30964 | -60.19919 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6fb4970e-b84f-3c4a-987f-3afe69843192 | -6.78302 | -59.65299 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58a05024-6a99-38bd-b893-90059abef1ee | -6.25549 | -60.01118 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 830f43d1-471d-3c0b-8155-0e55325e5329 | -5.4032 | -60.16783 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa8495b0-b5eb-31a7-bdc6-c10f848da977 | -6.68282 | -58.5345 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6eba0568-8228-39fd-b104-038dcd8da2de | -5.45037 | -60.15278 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49083ef1-4352-34b6-8185-54ebcf8234c0 | -6.77033 | -59.66615 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a3ee3b1a-b0cd-3837-a1de-b5d8aadac31d | -6.91643 | -59.36177 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04138084-d59d-3808-8559-df522d3dc1bd | -5.40822 | -60.17225 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4312f032-77cc-3839-b363-489c1d6d76b9 | -5.31464 | -60.20351 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d21040c8-fdc0-32ce-876c-1bd8e0a20178 | -6.77151 | -59.65778 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f9e417f8-f631-35df-9ab2-3a8aabcd2812 | -3.39494 | -59.45502 | 2025-08-26 06:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 94fb631d-734e-3509-b4c7-66e8c1bd95fe | -5.31564 | -60.19392 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0275fe6f-05f4-31cc-ad53-ca9987261fd7 | -4.95943 | -55.81411 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 804fe1b7-3cc8-308f-bda0-c7b41ec24a85 | -5.5275 | -60.20412 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f91d2f6-6c62-3d36-8b41-3bf6173cb7fe | -5.3146 | -60.201 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efcc6e2a-d2ba-33c7-bd0a-ce015c9c2f30 | -6.70072 | -58.56362 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7c91e225-38f6-307f-ab6a-fef391365a10 | -4.96567 | -55.82205 | 2025-08-26 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8d2c8ed-9105-3c80-8faf-bac6e361d024 | -5.44484 | -60.15197 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a5ee650-bf18-3616-8eb7-fbc2324cddd2 | -6.70455 | -58.56262 | 2025-08-26 06:01:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a27d605e-5c0b-33e1-9513-cf0507ff3207 | -5.29766 | -60.2047 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa49b378-2d42-35b3-b458-e4611175cf2e | -3.39224 | -59.45341 | 2025-08-26 06:01:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6240af9a-be36-3ae3-a507-838ab6810ecf | -6.24262 | -60.02085 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 80aa2f56-dea4-381e-8f54-f8444c8c9cc4 | -6.76974 | -59.66362 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cdc0d3ba-9ea6-33ec-a107-f3eabd09978d | -6.7703 | -59.65943 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e979030-f99b-397a-9615-e599827bccdb | -6.79246 | -59.67088 | 2025-08-26 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4dd427a1-d6dc-328a-afea-ba3231f9ecdc | -6.24209 | -60.02465 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 11ccc5cf-0aa0-3995-ad0b-4c385751c7f1 | -5.29864 | -60.19758 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6804a6fa-ea98-3224-8f91-7d6eee978671 | -5.3091 | -60.20024 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb938ab1-d977-3c2e-a969-406eaccf9c90 | -5.30464 | -60.19482 | 2025-08-26 06:01:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49767852-7e1f-38e1-af16-f444f1be2c98 | -8.55758 | -62.65068 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eda2177c-7171-3724-b567-e32ec63e736b | -7.39293 | -64.34573 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 229c2abf-a865-3789-9159-12a00ca71407 | -8.5422 | -62.654 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6498b7d-8cc0-3c8a-8e59-6eae80698f8f | -8.10165 | -62.88572 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e93dced7-15c7-3a3f-b797-f6777f531801 | -9.02109 | -65.70983 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0231b4d2-df7f-3831-a47c-12e72d4f31ac | -9.19789 | -59.5175 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 095fda93-9211-37cf-b765-5ce254f658ba | -9.02908 | -65.72389 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e10872ee-b93a-3818-815b-f2093d81a096 | -9.03706 | -65.72509 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 15d98786-b19c-351f-a6c5-ef891ec9d06a | -9.01463 | -65.69834 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 943d476a-6de2-3868-ba19-8fb951177934 | -8.99534 | -65.40614 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2f8ecccf-9a46-37f1-a9b4-3d3c4f8eba58 | -10.14834 | -67.67125 | 2025-08-26 06:03:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f84a84f5-ebf9-3b15-97d5-3fec6fdb0e51 | -10.01791 | -62.39001 | 2025-08-26 06:03:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bdccefb8-5ea6-3e22-aeef-6b63ef05b0f2 | -8.8632 | -62.43124 | 2025-08-26 06:03:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d0a9a6d1-5a74-32e5-a27b-3cdd07c6a009 | -8.99431 | -65.41335 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3cde8671-7c7b-37fd-9b54-671b35ebced6 | -8.97955 | -65.42948 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0693c9ca-bf9b-390d-a0ce-31fc3f18dcb8 | -8.97853 | -65.43665 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 44f228dd-fdb5-3a3d-8784-2aaf3f855e29 | -7.4009 | -64.35098 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8201114-bf2d-3f1d-9a16-85ad075f6c00 | -8.34156 | -62.94347 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7be61f98-1fb7-3614-9264-3af3144e28e4 | -8.53882 | -62.64248 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d9144c9-01a0-3c3e-aa7f-453c4ccee972 | -8.81411 | -69.29645 | 2025-08-26 06:03:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b282d37-09eb-3022-8c4a-e6ef76efee05 | -7.38328 | -64.35246 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2f7f21fa-9d03-35ac-9fa7-8490854bd2a8 | -8.98007 | -65.42589 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4901ae8-8db7-39ee-bdf5-2c1f4b10328d | -9.79681 | -64.25116 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5d3e05d2-2f60-3ef1-b729-0cd0d8bd679e | -8.57111 | -62.62511 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a0d89abd-337a-301f-a156-06d45b3a5225 | -9.15634 | -59.45602 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a39fc00-0b25-3ae4-ad59-95cfd43b7f69 | -7.88632 | -63.00708 | 2025-08-26 06:03:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6e614a70-5a62-31c0-8843-593b8aa58457 | -9.18338 | -59.53425 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 718f6e41-597b-3855-a398-ccb9f0299c4e | -8.57525 | -62.63116 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5366c9f0-8357-3f1e-b3c8-5454f3b54b3e | -8.56547 | -62.62982 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e89e2ca5-3bac-3fd4-ab64-f344c21dcd82 | -9.64437 | -59.63401 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32cf0a87-a954-3f54-85ed-065cb64006f5 | -7.5284 | -63.37973 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 328c57d6-ecab-346b-86ac-414a07f6b94a | -9.19167 | -60.78775 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72a11235-6a65-3fce-ab45-bc41ce44002f | -9.05375 | -65.72235 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c5deb12-4230-385e-857f-3229e5e36e00 | -7.40517 | -64.3516 | 2025-08-26 06:03:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0bf4632-6d5e-337e-9877-48ff598d03d9 | -8.99889 | -65.41034 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8e273f06-ebfc-3210-b923-4827c8457dcf | -7.29357 | -59.66943 | 2025-08-26 06:03:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ccacc14b-3f9d-319f-82f0-a95f6a013640 | -9.23296 | -60.81956 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40ba007c-5c6a-3b35-877c-63b328b068a2 | -7.62334 | -61.04525 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c894d239-7aa4-3b0d-b1d1-11820250ff59 | -9.23637 | -60.92128 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60baa757-584d-3b24-b7a6-faef742e2676 | -8.12217 | -62.87828 | 2025-08-26 06:03:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94b7c800-afeb-3d77-af22-5ff86b9f0ff5 | -9.09444 | -65.7229 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81de911b-5191-3ad9-8e41-c44dcc2f121d | -7.62593 | -61.04162 | 2025-08-26 06:03:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26537c8a-7a02-38f0-adf4-7891b3d5aa06 | -9.23714 | -60.91082 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef83a2ac-9643-3c4f-bae7-541d8213f424 | -12.33652 | -64.22967 | 2025-08-26 06:03:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c4e01cf5-7ec1-30a6-946f-817e30aab4d9 | -9.27487 | -59.7891 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b2adae5-50fe-31ff-9939-fb67d81c8d73 | -9.0154 | -65.69312 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6d71a98-af4a-3ec3-9d8e-9631ba1d58dc | -9.0117 | -65.37903 | 2025-08-26 06:03:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 476466d8-8877-3d81-840f-288d4896c2a2 | -9.19123 | -59.52127 | 2025-08-26 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README91.md)
