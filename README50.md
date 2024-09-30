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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 178a8cde-898a-3c97-8967-3f7c6f017221 | -16.10968 | -57.53134 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| a17b3552-e84a-31f8-91d2-924171bc1975 | -16.10508 | -57.53001 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a77d76c7-bd1d-304a-9ce5-8754475987dd | -15.9184 | -57.44492 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c794b72-7525-33c9-9701-2fbad484779d | -15.91468 | -57.43917 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2921944c-0240-32c9-b96b-f22caec5fce5 | -15.91001 | -57.43831 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7eb4884c-b696-3583-befb-ec6f336cfb5c | -15.83081 | -57.38523 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10511803-5c35-33cf-bc08-c27852403185 | -15.82615 | -57.38435 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8c834c0b-f00f-33bd-85a1-ecfb5b25afbc | -15.82506 | -57.39009 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12f59e70-615f-35a1-bd42-79bfcea907d0 | -15.82146 | -57.3837 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| eebff33f-9532-331e-b856-73a7bb7090e6 | -15.82026 | -57.38993 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2fcf4b36-4f78-3633-b9be-ee5d83eaf2d1 | -15.81907 | -57.39619 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cae17dcb-fb7b-3c1e-914b-f4059a38b788 | -15.81547 | -57.38976 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 724135ed-c53f-3f63-af31-45c5e0dae22a | -15.81188 | -57.38336 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e649058b-57c7-34fc-b153-187b72e3e876 | -15.80929 | -57.34673 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0938c7f0-180d-357e-8f66-0c8edb8326e0 | -15.8085 | -57.3508 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae97a4de-71d2-3e40-9d8f-55f9223e3ced | -15.80833 | -57.37672 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46aa8863-2391-3ddc-8b84-32b0176d6f49 | -15.8077 | -57.35495 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 95c6febc-79c0-3294-8188-db399a336764 | -15.80684 | -57.35943 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62794492-57a9-3aed-9641-e19c2f19de77 | -15.8048 | -57.37 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 39bfd643-99e8-342c-8b90-ebe99e381184 | -15.80119 | -57.36373 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a0858c46-c67b-3197-91f3-ffd543a65f1d | -15.77796 | -57.78993 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 203486b2-1ee4-34e4-9d80-261ff2e50bf9 | -15.77719 | -57.79125 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4d3b23d0-3b9a-3d6c-a150-8633c6e587ea | -15.77694 | -57.7953 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8fa25ec0-9156-3fba-9998-d6549a30047f | -15.77612 | -57.7966 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ad990542-133f-388c-8dd4-26ce610b2218 | -15.7759 | -57.8007 | 2024-09-30 04:34:00 | NOAA-20 | CURVELÂNDIA | MATO GROSSO | Brasil | 5103437 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b4680e5c-ec3e-3320-9f1f-7508b8d8c38c | -15.77505 | -57.80199 | 2024-09-30 04:34:00 | NOAA-20 | CURVELÂNDIA | MATO GROSSO | Brasil | 5103437 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d4732e22-284b-3bc0-9ad5-23a59a4b048d | -15.7732 | -57.78891 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c56ba035-ff5f-36cc-85f5-614df1fb3647 | -15.77216 | -57.79429 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b94aaa6-678b-3ed0-b880-ec6bc8d1f77d | -15.77113 | -57.79967 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc06eba6-da0d-3458-80f3-a48eb5c10523 | -15.7701 | -57.80507 | 2024-09-30 04:34:00 | NOAA-20 | CURVELÂNDIA | MATO GROSSO | Brasil | 5103437 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b65d27cb-b54f-305e-ac7a-18a8a6a0f6db | -16.60564 | -57.34026 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3fd3698b-0e18-3b46-abf6-956971d4bcb3 | -16.60378 | -57.35001 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 4e60e89b-e321-35b5-94c7-a7d8e70940e3 | -16.60201 | -57.33443 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| deb05ea3-45de-3bcf-b03f-e437cf641b6a | -16.59746 | -57.33347 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1afa786d-eafe-3bde-943c-e1dbbc42c819 | -16.5641 | -57.40788 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 01940c70-cd10-3061-9ca9-0e60624ec8cc | -17.1967 | -57.39334 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| cc9e512b-de84-3805-a50b-6e17ab50d0b5 | -17.19218 | -57.39237 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 489c0560-6f97-3767-aba2-484938c585bd | -16.99069 | -57.98671 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| cef45923-31c1-35f6-925f-e9ee3023b9e6 | -16.98965 | -57.992 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 356d41d5-6833-31a9-b4b9-1ff920643ab9 | -16.98861 | -57.99729 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| c546071d-6de3-3443-881f-9927b818a58d | -16.98493 | -57.99098 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a5402505-fdcc-3cea-845d-aecbaa2b0d42 | -16.98388 | -57.99626 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| d7306bbf-8e90-30a9-beb9-1c55fe7313e2 | -16.98284 | -58.00154 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.5 |
| c026618f-b5e1-3995-8f39-fc2263994331 | -16.98179 | -58.00684 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 2e6b6b8d-9440-3110-b31e-2b059aae7366 | -16.97916 | -57.99523 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 76bc11be-b374-3642-8f4a-7f004fa3249a | -16.97812 | -58.00052 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 92c9d0e4-6c4d-3327-bbf1-67335d11ede4 | -16.97707 | -58.00582 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 728d34cc-9e28-38f2-84b3-e15087d51061 | -16.97602 | -58.01113 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a9b1748a-6d6b-3add-94db-1745730cb157 | -16.97234 | -58.0048 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 91075e6f-d1c0-3815-a570-92f70245b490 | -16.97129 | -58.0101 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| e02eaa02-4509-3ab5-a5f9-888383fb2a41 | -16.96867 | -57.94896 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b1f9b50e-5770-3a39-aa46-8563b65c57ac | -16.9682 | -57.94657 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9ce5e767-dc78-3d6c-ad87-41dd85d79569 | -16.965 | -57.94271 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1baa4fa6-9fcd-3c3e-85b9-d8fbad928b5c | -16.95925 | -57.94693 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6d1145ce-01d3-3ccf-a57f-d9c990789f97 | -16.95878 | -57.94451 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 6e75e640-4617-3791-8520-dbf849222e09 | -16.95715 | -57.95744 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 10fe2cc2-e4c6-3836-8801-2c1b43431ea6 | -16.95711 | -58.00702 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 60d55ed8-eddc-3873-8ed1-4247f86046d5 | -16.9561 | -57.96272 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8ba2d185-e1f2-359c-8684-a6bb5e1f75f2 | -16.95605 | -58.01231 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0d1ef22e-acad-3605-9f7f-d1e894ef11ed | -16.95603 | -58.01012 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 807fb3ac-60a0-3cb5-bb68-ed2cf774a42b | -16.95575 | -57.96032 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 57528099-78be-352b-bbe7-d23eba23bd33 | -16.95558 | -57.9407 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 78edaae9-b78f-3e4d-99db-409ac8489f4d | -16.95473 | -57.96562 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ff5ca3e3-1bd0-3465-a0e0-dac3ee21be39 | -16.95454 | -57.94592 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 011b0d07-c6cf-3cc3-9931-8e1914d7e5bd | -16.95407 | -57.94349 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| dea21ae3-8bff-3064-a7e9-ee8474c28934 | -16.95243 | -57.95644 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 34101e22-449f-3c69-b78b-d866873f2339 | -16.95138 | -57.9617 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 42357ae8-7367-3895-9f89-41f87a5733c3 | -16.95103 | -57.95932 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c9f33e24-b7f1-3f43-8dca-2ea2b2dda48d | -16.95001 | -57.96461 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 07ad93ef-228e-3f7b-836b-612bd1af1296 | -16.94721 | -57.93345 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 0c5f1e57-e476-30d0-a697-6301d7a439fc | -16.94667 | -57.93097 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 3caef2ff-4e18-354f-9dba-d6b669e668f2 | -16.88693 | -57.7136 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| d0506965-9648-3b0f-81ab-8431a46884db | -16.88592 | -57.71868 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 198e067d-26b4-36ef-b53a-d6ff4b927faa | -16.8841 | -57.71647 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f1c65a35-06f1-373d-9bf3-cfb0f73be1e1 | -16.88329 | -57.70754 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8cc33c6d-a332-35c8-98e0-4497421890fa | -16.88127 | -57.71767 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e72267d1-7332-3995-bf6d-a8ba86af3ac6 | -16.88043 | -57.7104 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a992ed7f-27e4-3931-b790-9f088fb4d4ea | -16.86845 | -57.69723 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| cab36d27-9028-3eaa-83a1-fb6ce0af150c | -16.86747 | -57.70231 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e38f37a0-d7d8-3115-b904-906af53d3a64 | -16.86722 | -57.72875 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 5d4f5715-532a-3d06-923f-723d04cb0950 | -16.86283 | -57.70132 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0086bfb5-9075-3062-a47b-632c5cae4cc7 | -16.85917 | -57.69524 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 55927e46-b674-35af-86c9-81600175ba7b | -16.85818 | -57.70032 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 24f3af16-9f6a-3469-ae96-3773fc9b073a | -16.85354 | -57.69932 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 794518c6-f091-3099-a18f-f5c5417afd90 | -16.84889 | -57.69832 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f539003d-f22f-3532-ba21-a7feee4f75a4 | -16.8479 | -57.70341 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| e41e8380-d5bc-3f8e-a3d4-b834a1830499 | -16.82361 | -57.55659 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b81c2377-400c-3f85-b7f6-9ecf5ce23a05 | -16.82263 | -57.56157 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 59f49417-5353-35da-b21b-b436716298ba | -16.82148 | -57.54964 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8113fab1-c80e-35e6-a61d-57d7ce584144 | -16.82097 | -57.54565 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 2ec4c120-1089-3693-891f-c1ad8c63fbbe | -16.82053 | -57.55464 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 8e6b394c-f41e-309a-9156-df49c4e042c9 | -16.81999 | -57.55063 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| dcecfc95-aed9-3591-a194-612ac4a9b7d8 | -16.81959 | -57.55962 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 91ae496b-38ba-3200-928b-bcb517cfbc7c | -16.81901 | -57.55561 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fff7087d-d6df-3983-a989-ba07de45d75f | -16.81687 | -57.54868 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 444f1212-fadb-3449-b6fa-70020d1c7380 | -16.80577 | -57.55668 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| aacc7592-09fe-3a71-921d-281b792b314a | -16.80481 | -57.56168 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| b4969a01-5f70-31a7-85a0-1c1e92d4788b | -16.8042 | -57.55767 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6c535d3e-2a81-3419-b363-4b4d60419929 | -16.80322 | -57.56265 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 9d73dc6b-0999-3d01-91cb-081afccce6c3 | -16.78585 | -57.79695 | 2024-09-30 04:34:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README51.md)
