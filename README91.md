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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2b83afb-e902-3024-a7bb-9dc44ced049c | -4.06835 | -50.01361 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aca6044f-a62e-3071-9bc7-ae0a19cb5b8d | -4.60848 | -47.98024 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0a8bdfbd-bdbf-3d97-b2d9-31e92f4b47ef | -2.81627 | -46.65078 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bcd8723-2065-3d82-bdaf-bf5557dcfe64 | -4.77571 | -48.91757 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0860528b-69bf-33ec-baae-9270675170e7 | -5.46752 | -47.69285 | 2024-11-10 04:38:00 | NPP-375D | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fa392d6-7d1f-3c98-981d-83adbdec9e79 | -2.88345 | -49.3876 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02d99c72-4c09-3e84-8cf4-b68f9890260d | -2.46169 | -53.68642 | 2024-11-10 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e25392b0-22d1-36e8-8faa-d695198496be | -2.15411 | -50.74139 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f71eb9ef-edc1-36bd-a30a-f8d00b4535c0 | -3.22372 | -50.27654 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f273e25d-e4f8-3ca4-a2c3-300a1e4d6ae6 | -2.57248 | -48.18729 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1511b690-b684-3a1e-b41d-a073c4f7fd8e | -8.38621 | -44.12616 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab46a3dc-5e72-3982-987d-00cea10d569d | -3.94853 | -49.40083 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bed68829-04f1-3565-9492-ea18f3b4cbe7 | -3.1112 | -50.15132 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae792dfe-fed8-38d0-9294-b4f37cc052ec | -2.83532 | -49.05217 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 11a45a05-e4af-393b-8e44-de3fcaf7766a | -3.23591 | -46.484 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88a14949-163b-3fb3-b9a1-4cfbc18f6123 | -2.94222 | -46.78248 | 2024-11-10 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd006faf-bca3-3fed-889a-70149f45c6db | -3.08214 | -49.56552 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5198cc54-67d4-3db4-9832-89991e62fa78 | -4.97041 | -49.35546 | 2024-11-10 04:38:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3759378-d05a-3ead-9cf9-2f5345c608c8 | -2.17898 | -50.51888 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32b0137c-f457-31e5-b9c0-a8a1b3262ab4 | -7.17382 | -45.38918 | 2024-11-10 04:38:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f78d356-7790-3869-9f9d-9fe6a9d962c3 | -3.12791 | -50.44254 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 185faa1f-aa4c-38d8-a7eb-d40fcf8477fc | -2.84691 | -48.44163 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c1549bd-92aa-31af-9df5-a1fb1108d4bf | -5.31438 | -47.69094 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4f0efb25-6b9a-3953-a59a-3ca8fc7a725f | -4.2464 | -48.02077 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45bbd062-17ea-351c-bdc6-17a19c9b51bc | -3.11043 | -48.61741 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5589fe04-7755-3600-92dd-238f3aa239a9 | -2.41883 | -50.41691 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7ec79510-1298-3c03-ac30-ecfa2355b05a | -4.17385 | -46.78068 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b91e9850-ca6f-3eac-abd8-ba5c722f6f67 | -2.38348 | -49.82778 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6fc73e71-ff0c-3c97-aead-edb670b2939c | -2.31609 | -50.67154 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a878192-8d64-3a82-8399-b3478897d5cf | -3.95372 | -48.15765 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43c53c63-7cc6-354c-9425-97aa83a3659d | -2.58569 | -48.16813 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b38e5654-2f7a-34af-935c-50e3bb99e306 | -5.32132 | -45.06047 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2d1ba49d-acc6-3cb5-a6a8-63d0550d8f00 | -2.90678 | -50.40455 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c3c0f0a-27ca-33b5-90c7-b53c4fb04fd4 | -3.1751 | -49.10839 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79e0e648-0771-3b95-9443-121772ee6d44 | -3.43338 | -50.2975 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| f3f1f0fe-d3f7-3ffd-a9d2-92df49f6eae7 | -4.10537 | -49.09148 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa681f92-dc08-3443-bdb6-8f2d8ed27c96 | -2.08119 | -52.03747 | 2024-11-10 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52e1494f-b2bd-3a4d-b4de-d68f7d7e46d7 | -2.72965 | -51.73701 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 987c4390-ca53-3c68-bb93-a60b4eddbe59 | -3.17051 | -50.2165 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9954302e-09e0-33cd-9814-20a714c4e5ca | -2.83237 | -49.77338 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0d055aa-3b48-3568-84f2-33501c3ecf28 | -4.0768 | -50.01156 | 2024-11-10 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ae74bc4-d679-308b-9998-088ff52462cd | -3.22889 | -50.44272 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 754a8c25-8fdf-38dc-ad13-6a492e4c3dea | -4.43816 | -43.64647 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac3da961-bc9f-39d9-b2db-de9075762b53 | -4.11877 | -43.5969 | 2024-11-10 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| de64195e-c410-3b0a-8606-c06786864d4b | -2.26518 | -51.89452 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df02db66-83e1-3bd4-9cac-bf4cbdbdb377 | -3.59139 | -50.27054 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c25b445-b2b3-3f51-8d4a-5fb93490903a | -4.2045 | -48.54468 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdc6ceb5-4e18-38b2-8b70-f797fa1c2d1e | -3.99574 | -46.41571 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afe24343-f08e-312c-9fef-35cf7dcaa160 | -3.60696 | -42.8128 | 2024-11-10 04:38:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d3205824-d6da-3215-8852-1dd9fdf50026 | -2.58061 | -48.13551 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 776298ab-4631-3f16-b602-265771c8c3d3 | -2.39133 | -49.84371 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1bcef9d7-9442-3081-a4aa-fac779a87833 | -5.32963 | -47.70429 | 2024-11-10 04:38:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b92e9c27-a6b8-32d3-9492-1c87f8b7d70f | -2.90692 | -49.54223 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 723c1fd1-2cf8-393b-ae99-89f46a6461cd | -3.09829 | -49.42081 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| bb70993b-c415-3f69-95a5-ae7982ade327 | -4.23306 | -48.01863 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57a7803d-c56e-3b5e-a1d8-184e6d5ae056 | -3.57446 | -45.82723 | 2024-11-10 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca366074-953f-3a6b-8656-baac7de43fa7 | -4.70667 | -43.79424 | 2024-11-10 04:38:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 726d6f4e-8ed9-3256-a171-27a0d756459a | -2.92028 | -49.50111 | 2024-11-10 04:38:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6b0a4828-bd92-3c8b-9f07-32042b51f83d | -3.18124 | -46.5256 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d983f07-6c29-3988-af08-ce248ed0daa7 | -3.30915 | -50.13718 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e7b9663-ea59-3b8a-bbf7-19213b06b8e1 | -3.61928 | -55.47742 | 2024-11-10 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1179586c-a10a-39e2-9690-ce5868bb8207 | -3.41547 | -51.40847 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5154621-e73c-3cdf-97b2-4d71a5899d08 | -4.30914 | -48.65344 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6e5ee76d-c41d-3619-bddc-1b7961e03abc | -4.28257 | -48.1981 | 2024-11-10 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8b29666b-fc11-3a52-9d4d-2f0e3d5b1f52 | -2.87455 | -51.46727 | 2024-11-10 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7eaef766-bbc2-37fd-9c5c-94fb46b4ab1f | -2.74115 | -49.39366 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cea0a20-64b3-33ce-985f-7f2f915da891 | -3.1047 | -46.60957 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 24073543-ea1d-3102-b166-e4ed5f4d924f | -2.38875 | -50.45047 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 27c5deb8-1dc1-3677-a604-6d1f9227799b | -5.265 | -44.87693 | 2024-11-10 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0381c61-ae1e-37a2-9783-27fd4715a068 | -3.94814 | -48.14966 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 71bc8c64-5a15-3635-a3f8-514b8c462c03 | -2.86295 | -48.44765 | 2024-11-10 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c6fe0a0f-e4b9-3b40-bcdf-067988008902 | -3.9543 | -48.99715 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 208a1f8a-28d5-355d-9080-3226d9d564ed | -2.15472 | -50.73755 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e9e522c1-25c7-38c6-9165-76477604298d | -2.56871 | -50.67878 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 10fd0a88-0016-30cd-9b8c-26239bf5f7da | -2.84255 | -49.4388 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 39130e7b-d263-30c3-b6d3-80751ab9e517 | -3.58395 | -49.98917 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2aef02dc-ae3b-3e3b-85a4-86b7c0fc7453 | -4.04592 | -51.07521 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82c59463-aca4-3dcc-bf24-ccf79f3c54d3 | -8.40953 | -44.11376 | 2024-11-10 04:38:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 229f210f-a7df-3e71-9ec7-98932060d27d | -3.25324 | -46.46351 | 2024-11-10 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f1545167-562e-3591-aa9f-87e3e618dcb2 | -3.03774 | -50.32631 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6ee214fd-cf89-34b4-97a9-e5cdc31c6540 | -1.49042 | -55.43489 | 2024-11-10 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ba108ae6-c492-3e78-af70-b1fe0326ca5e | -4.08769 | -45.97808 | 2024-11-10 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94dd2d32-57e7-3973-b3dc-08f4f5f81a92 | -2.21038 | -50.47752 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c127d2c6-9634-3164-a69b-3c7b1d18f9ef | -2.67538 | -51.82135 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a27e23f4-4e5f-3be2-87de-13335e3cc4b0 | -3.10711 | -48.6169 | 2024-11-10 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8687de18-ae1b-37cc-8af1-a588d56c50eb | -2.99383 | -49.50535 | 2024-11-10 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf7d5e57-f691-3dd6-a83d-35b5e422dcbc | -3.41496 | -51.2058 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61a6bfd6-bba9-3021-9069-6cc13926251b | -3.27011 | -50.02809 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bfa2a56-ff94-359c-8e99-e21e2dd0722f | -3.53296 | -49.26777 | 2024-11-10 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5e440e29-5605-3724-b4cc-65cd29538e4f | -3.13075 | -50.44678 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 772fbdd2-22ed-3cdc-868d-db8ba2b4d025 | -3.01755 | -47.95893 | 2024-11-10 04:38:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 649d4ba2-50db-3c5d-a5af-4a5a105aacd8 | -5.61618 | -43.74553 | 2024-11-10 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0f84afb-7a73-3bdd-85aa-38f7ae66621b | -3.59596 | -50.24157 | 2024-11-10 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3f7574e8-217b-3e31-949e-b5396abf2ed4 | -3.83369 | -48.87918 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b943d4a2-d49d-3b19-b7f4-b395e0a4259f | -2.69002 | -49.87169 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 81eb10b4-e320-37a5-b1f5-bb414c40b483 | -3.97043 | -48.18163 | 2024-11-10 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1aa17877-3a5b-36f8-a7b5-4f8d0b429138 | -3.84475 | -44.12545 | 2024-11-10 04:38:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 93e7647a-eded-3d2e-b409-07c3bd268536 | -2.6472 | -49.90171 | 2024-11-10 04:38:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa06875f-9ea6-3a88-9c32-c7d266931d1f | -3.96535 | -48.9918 | 2024-11-10 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| af08d1b2-9086-3811-8cfd-afca9f9852a7 | -3.09351 | -51.11692 | 2024-11-10 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README92.md)
