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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 81030c6c-3497-3179-9297-98ee39912941 | -2.01466 | -51.19614 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 76959a90-5298-38b9-abe0-d88724b70c8d | -3.94383 | -46.6887 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6ec67a6-a071-3cd8-9ce0-ee80c5b969c9 | -3.02339 | -49.52359 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e45275d1-005d-3d65-a67d-4babf23713d2 | -3.4626 | -50.53667 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fa9cdb9-53b7-3ce8-8476-75e952183ca7 | -2.71812 | -49.80028 | 2024-11-30 04:40:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99c987f7-c1c8-3bec-8f3b-522dba41787a | -2.25556 | -48.47387 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb144742-d16f-3d80-81d3-34a84b9c68d6 | -3.29285 | -53.8279 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e52bf9a-03f0-366d-ac8c-f22e3fc2c653 | -2.43159 | -50.39174 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be2e1638-5240-36d2-892c-fc1a1b1c7d0a | -3.71308 | -47.14513 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26d0e8db-2662-36b3-9eca-426357dd736f | -2.18754 | -47.13986 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3b37dec2-900d-3638-ae42-eddcbb6dd20f | -1.4085 | -48.14414 | 2024-11-30 04:40:00 | NOAA-21 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92f8ab36-1363-3557-ae4c-655078d40e3b | -3.60121 | -54.42552 | 2024-11-30 04:40:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1fd44ead-c474-37d0-a2f3-10a5131a1d11 | -2.72704 | -46.28117 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07233dc3-cf9d-3694-af42-970e0c64ea15 | -5.46626 | -43.26947 | 2024-11-30 04:40:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74de5adc-0f2d-36dd-8b2f-8a16a8447e51 | -4.66577 | -45.67176 | 2024-11-30 04:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d4cb1438-2e99-3f87-8703-89711ecf344a | -2.88603 | -51.72129 | 2024-11-30 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| caec261e-6677-37cc-9098-b9cd2ec6b532 | -3.97251 | -49.91442 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0bfe2e91-fb7d-3268-9b73-b1baba67c23a | -1.99085 | -53.29278 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 847f7864-bc0c-3928-83a7-c8ffb90c5c45 | -2.02396 | -51.16917 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33a72b00-f42a-31c0-9d7c-ac1f3eb14f82 | -1.05522 | -53.21149 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c05a6b30-2b26-3e70-a002-3ffc796a0cf5 | -3.64684 | -50.23303 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73c7c276-06c9-3807-81d4-4904ffeb38fc | -3.20331 | -48.59037 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b8b4bbf-c5d4-3ff5-9e9d-59e8e30343c4 | -2.08533 | -48.5383 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24ea14de-4b66-3e82-b40a-a35857d3dc52 | -2.92242 | -54.26513 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| cbdad70f-9fa5-3b1e-8bc4-8465456f0018 | -2.59604 | -53.98172 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dff3bb6f-ac30-3bd9-aaac-ab4bda271c55 | -3.40584 | -50.31561 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a38f14e9-a82e-3908-9d69-1a8adb0069be | -3.83363 | -46.54985 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e742289c-e8c1-30ae-8741-b6e8f51f14fa | -1.96865 | -51.10204 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b1d22d0-6d06-3f5d-9d9f-c8b0d7fddb25 | -3.46655 | -50.53359 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fcd6b57c-a3d9-3e03-a4b5-152a951feeb1 | -2.82501 | -46.85294 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cda9b31e-a5d3-3c58-9e01-e9e75d1a67a7 | -2.53411 | -47.33238 | 2024-11-30 04:40:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b3ee5f5a-d682-3ac8-9d4b-b1bc3642bab9 | -2.09337 | -48.61683 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 633915ce-12b3-35a1-be4a-fa0d1d3d8bb2 | -2.32923 | -54.50498 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4aedf117-c407-3d5b-a62b-6962fe2753c6 | -3.93973 | -46.7158 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fd8c517-4f41-3a34-b274-16639d4c7b33 | -1.45282 | -51.49698 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2bc6053-d5f1-3611-a3e9-15c9a89325fe | -4.07294 | -46.69554 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4b8eece-f511-3dc3-8f9c-57b1d08e2b09 | -2.85076 | -46.68413 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 859f18de-9895-3fa0-a811-42be631b40ca | -2.61805 | -49.24448 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ef6be9d-4ca8-3785-afb0-2bf0dad9e366 | -3.25923 | -53.63737 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 627828bb-d929-324d-bee8-436dcb1b86da | -3.94593 | -46.88494 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad113c8c-4ae1-3402-a64a-aac9440afb74 | -3.83182 | -49.13894 | 2024-11-30 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49e414a5-49e6-352a-8f55-2d319ada1236 | -2.70983 | -48.67826 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b7ec553-338c-3153-aa63-164fe6639159 | -3.87134 | -47.07347 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb3db3a1-88c5-3459-b2c3-15a7826e4a35 | -2.4355 | -46.50988 | 2024-11-30 04:40:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cb879e1-c0eb-3258-8768-0be14ff237d7 | -3.93186 | -48.14514 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67b22338-76f3-302a-bbe4-9f84172bdca5 | -3.49246 | -53.81097 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a700984-f68d-331b-a24b-6ea07d046d68 | -2.5821 | -49.99451 | 2024-11-30 04:40:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be3704d4-78fa-3724-a54b-8e07899bf315 | -1.50057 | -54.95009 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8597e301-8daa-3ca6-a9a4-43173184b323 | -2.58479 | -47.02481 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d91c169c-3e64-3311-a7b6-44ab25b32c8d | -3.93799 | -46.72722 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0eb79587-1a82-3332-9e86-eb2b9fa5090a | -2.44637 | -53.97757 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f5696f04-9de5-3d0a-b24e-f3175ceb98d4 | -4.87094 | -41.3202 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 84d7eb05-e0b3-315a-b7c0-c5f5a054c7cb | -1.87141 | -46.46545 | 2024-11-30 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7391ba5-1c84-3823-9db8-bcc0b95b2cee | -3.59096 | -50.36962 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 85e568f7-4f7b-3be5-8000-a498e8a27d41 | -1.31973 | -51.67347 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dfcb876a-4a53-39ae-a3a0-4700285db49e | -2.8338 | -48.47214 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6fce2685-f35c-31d5-a7ab-5552460a1bb5 | -1.49086 | -52.32426 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c742e726-f0a2-3629-a1e2-2ead8f7db059 | -3.69257 | -47.14189 | 2024-11-30 04:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cd98280-2645-3939-ba98-76540b286f6a | -3.33807 | -53.2111 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| afc6bde4-917e-3e2c-b378-dc908f837244 | -3.9974 | -46.50109 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5f37f236-b311-3b23-b42b-d43df5cbd2e1 | -2.54024 | -47.97635 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e086071f-3e24-3d2e-97f8-017bd8ebbeec | -2.58917 | -48.29677 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4967beef-20ff-3c94-9fd8-6a85770a18bf | -4.07978 | -47.02042 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 618065ae-00ec-3c4a-948d-3dc9e9d1c682 | -2.71585 | -46.30736 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 40ce22a6-558b-32e3-903a-2545415c455b | -1.2689 | -51.63305 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ac51fc1-9cb7-38e8-93e3-8c1fbcff53fc | -3.33662 | -46.69761 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05f7a263-4572-332f-993a-f1d98aa2aa21 | -3.59489 | -50.00168 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bbc25f8-50a0-3115-818b-30be810bbfed | -1.21852 | -47.61833 | 2024-11-30 04:40:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bd6bbe2-5e4b-3ef6-8835-7c5a28c03f7d | -2.18536 | -48.39913 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35ad6527-2e15-36c0-914b-5629711f3f08 | -2.77997 | -54.21324 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 61968d88-87dd-3dde-b214-ae106575f8dc | -2.0064 | -47.8441 | 2024-11-30 04:40:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 071c2a39-6ba8-3dc9-8b2b-632585047ff3 | -2.61489 | -54.20531 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44459555-b78c-3459-81d4-821a109d3827 | -1.62705 | -52.37896 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 07aa8470-f75b-3e6d-b24a-8bfb29e930e0 | -2.92539 | -48.01458 | 2024-11-30 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 65cdad74-2512-3af8-a9c4-b4e9be4248f1 | -3.02143 | -52.38488 | 2024-11-30 04:40:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c0e88e0-82d0-373f-9340-d6f9acd3a5ef | -2.83322 | -54.0382 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5de2261a-a85c-351f-a2f7-eafd08498f33 | -2.33853 | -48.83464 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4ca81e1-05ae-3c50-a3f6-0c70484b73e5 | -2.36783 | -56.11719 | 2024-11-30 04:40:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16868b2e-d2fa-393e-b658-05cc1bed6346 | -3.98971 | -49.9349 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79730821-4e21-3999-958e-53e2be390400 | -3.03789 | -50.97741 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e7ca5d93-78ce-3ad6-9854-8171077a664a | -2.83512 | -54.1049 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a22e0c7c-f330-3d28-b0f9-d49df7b8d551 | -1.53787 | -55.86964 | 2024-11-30 04:40:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4dd0f29-203c-39c7-95f9-0501ce5cee86 | -4.05545 | -48.3363 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9400dcd7-1755-374e-bd34-d8e849d93c9e | -2.4406 | -50.42276 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 04a14787-476e-3ea2-b9ed-9f2e174c9819 | -4.04722 | -48.08052 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36fdcae0-49c0-3670-8e7a-5351110ca6f8 | -3.34378 | -46.60495 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba1e5c3c-8b81-3c78-b986-cf88beacaa4f | -2.82884 | -52.94534 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a8df774-7b0e-399f-986f-9cb21092f0cd | -3.131 | -50.39333 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29b2275f-0b6f-3f5c-b46d-8844802c80c5 | -2.59223 | -46.00333 | 2024-11-30 04:40:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c27468c1-282b-324c-8d60-b31bc6dd488b | -1.62152 | -53.88988 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 01dfa663-e40f-37a1-90ff-7d4433960e5e | -2.30013 | -48.47017 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98bbc399-0324-32bb-92e4-c3bfaf8689d2 | -1.5943 | -51.26881 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 881da03f-2175-3906-b151-5844a36933e4 | -3.42599 | -50.42836 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f74e1893-bc90-3a1f-9d1f-9831441a4c51 | -2.98884 | -49.11242 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7885a3a-dfa5-356a-9886-e6b1490aed74 | -2.5622 | -48.20709 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e306717b-42cb-3785-b3e5-5073ac471f44 | -3.73614 | -53.36744 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ec68f7a-479d-34c0-8a1f-5a2ca2591ed0 | -3.0375 | -48.51828 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a31d3174-1d92-3c67-90bf-4de0fc509f22 | -3.51722 | -50.25643 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 154d6433-2654-3967-bdfe-6833e6770cc2 | -3.52392 | -50.47633 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33309945-43f4-33fb-9dbd-5c3991726ff9 | -2.80015 | -54.03664 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README60.md)
