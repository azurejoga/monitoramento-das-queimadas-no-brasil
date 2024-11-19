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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62403e42-1ccd-3d97-b2df-65cd887cb22c | -3.59707 | -53.99465 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c528a5cd-ac10-37fb-b255-f68bb817f926 | -2.68791 | -51.80553 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b856c503-5825-3ccf-8127-e4c118851868 | -1.59257 | -53.80633 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3ca2f9b-2600-3900-b633-0fa1ba667659 | -3.55428 | -51.53735 | 2024-11-19 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89d11060-2169-3d45-8e68-d1548300ee46 | -1.34706 | -55.73748 | 2024-11-19 05:31:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca921d81-ba02-32f6-8cb1-fb63acfc57eb | -3.20278 | -52.44744 | 2024-11-19 05:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9326d2c8-2a3c-38f2-91d6-e8037cd9398c | -2.76466 | -52.60194 | 2024-11-19 05:31:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0a66c572-eb30-3bf0-858f-c2c67582e459 | -1.43827 | -53.38449 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c09e43e5-be6b-32fc-8128-23a1904d448c | -3.36146 | -54.10672 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb2f0872-6ec5-3ce4-9fd1-50488701e404 | -3.66406 | -50.44245 | 2024-11-19 05:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8d44fec-611e-3025-97fc-9e0aefe939cd | -2.01837 | -52.0785 | 2024-11-19 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 847bc486-efe0-3296-90b0-55724e2c5ddf | -3.18662 | -53.25066 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| beec80a8-83a3-35c9-90e4-b506a7f69b15 | -2.61404 | -54.53829 | 2024-11-19 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a32b0509-6c29-3fbf-a263-dfc5725bc449 | -3.3344 | -53.35702 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ea2c035a-5b0b-3187-b5bd-3f6ce883508f | -0.12137 | -51.43272 | 2024-11-19 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 752e22db-a2b5-3649-ad6b-f5fbf131fcdc | -3.3613 | -54.10542 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1dcc5d73-bb97-3630-8965-94cd0ee1c752 | -2.58864 | -51.71592 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 356d0547-d26c-3148-a39b-865ff00d2166 | -3.97716 | -49.91901 | 2024-11-19 05:31:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcb6bfab-2891-3fcd-b7e7-5b72fb45f097 | -3.34143 | -53.31007 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1f96813-88b2-372c-860a-5ee4957f288d | -1.37669 | -52.07983 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c72803fe-cef9-3fc1-b7e0-f4c569890079 | -2.95968 | -51.41183 | 2024-11-19 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f4fb1ce-e8ac-3d60-bfec-b1af1ddbbfc5 | 0.55125 | -60.36406 | 2024-11-19 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8964f16-0411-348f-a4da-c6c886038eae | -1.64078 | -52.67395 | 2024-11-19 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ca0d276-3bef-3d4a-837b-08aa554b2637 | -0.12204 | -51.42838 | 2024-11-19 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c5466e1-f1af-3e3b-895d-7c44471f7467 | -3.11477 | -53.70362 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f64fc3b8-3a74-3a72-a0ab-6786529e80d6 | -2.66302 | -51.72214 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96d817e7-7ddc-3b18-8ed1-103b62678758 | -0.92909 | -52.50102 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fd7d6a7-9be8-3f35-98f9-d11306713bd1 | -3.17402 | -54.69212 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f2125c5-74ed-3e57-9e7a-a823f823c063 | -2.28895 | -53.63678 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6da9dae1-a9f9-30a8-a3bd-475db9e7f528 | -3.66084 | -50.44124 | 2024-11-19 05:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9519f1a-eb53-362b-be7e-10a3962fda21 | -1.24549 | -52.04439 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff9a4d9e-1c3f-3f8a-bee1-85fba1d2cfbb | -3.50588 | -54.03492 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66cc1666-9392-39ad-aecc-e3a955de270f | -3.3133 | -54.17696 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be033c2c-4ed0-3644-9d0a-418f2e7dc537 | -2.80266 | -54.18753 | 2024-11-19 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76a410ac-397f-364c-99bb-2fdaee882b6e | -1.62031 | -55.14601 | 2024-11-19 05:31:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33db414e-0377-3af7-b0be-a7a8f561d481 | -1.41688 | -52.4369 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 763018e2-046b-337c-ae30-5ce84bda87f7 | -3.04326 | -54.4049 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca5f5ad7-e658-3a04-8f4c-fe8640d15e2f | -0.1834 | -60.6846 | 2024-11-19 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ef7cadc-be1f-3b84-a5ce-8b65582d0341 | -3.36228 | -54.09864 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81084c34-4216-3959-8c2d-4fca817845bd | -2.37241 | -53.68537 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60c1dc25-50a7-3f89-a6be-b9f15b528014 | -3.06378 | -53.28048 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91958e37-5cc7-399a-a0bc-a583b7d559c5 | -2.58186 | -51.71963 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1afb1361-c207-3320-b05e-5f2638bddc62 | -3.18607 | -53.25446 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ceafbd9-c863-30f9-a9a3-012c47bdfb66 | -3.36655 | -54.10625 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88a1cc2a-d55e-3916-9adc-2954e05d3107 | -3.31647 | -54.08411 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69ad858c-dd62-3dee-9910-18c57d34ba64 | -0.15044 | -60.87054 | 2024-11-19 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b31906bf-a87d-3fda-b957-a0db407f8305 | -3.36178 | -54.10211 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 958788c0-14b7-3570-abb4-1ad8cf39bf06 | -0.85717 | -51.86692 | 2024-11-19 05:31:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 59060c8c-35ab-3da0-98bd-8b16f7e2c294 | -1.24613 | -52.04021 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 036d9f84-1273-3ec1-a8a0-c7047eb11b90 | -2.28413 | -53.63246 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8b24c2f-e4ef-37b7-a148-b2bf8ba39e34 | -1.53675 | -60.33234 | 2024-11-19 05:31:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e69fa88-722a-3404-a355-44a379b41cf6 | -2.58118 | -51.72421 | 2024-11-19 05:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c63abeef-6ed3-3e4f-bf06-43e9e196db26 | -0.94044 | -51.72232 | 2024-11-19 05:31:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3e1a897-f8bf-39e1-aadd-3d145603cb28 | -2.86495 | -51.79289 | 2024-11-19 05:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a645d84-d80e-3a25-8ac1-280d5069b299 | -3.12014 | -53.70447 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a7cb6a8-913d-3c8c-a1af-3a923d6d4153 | -3.31121 | -54.08333 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1608784e-eaa3-3b6d-ac03-04e80c0611f1 | -3.05395 | -54.40355 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e1caf23-2302-377b-ad52-3f946021ad85 | -3.99098 | -49.91803 | 2024-11-19 05:31:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5d11d02-dd36-3c86-ac61-82d4886d8f2e | -3.36195 | -54.10354 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56cfc439-8a17-33eb-85ff-3f272809ca68 | -3.19756 | -52.44218 | 2024-11-19 05:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3db51071-6a93-3b4a-ab66-d4cffb6cc0e5 | -2.19878 | -53.6667 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94e90c19-13d8-34e6-96a6-603672bd595d | -3.28468 | -54.11736 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3e2d88d-e3d7-3b12-8f7d-600895feb00a | -3.54879 | -51.53128 | 2024-11-19 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 399f2f8b-df4a-339a-93d3-2a97a6447901 | -3.31375 | -54.17397 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cfa5208d-6149-3605-ae83-cebf49eaf640 | -3.51254 | -53.80121 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c4496e9-d9f8-3118-9bc6-c420d316d652 | -2.95235 | -53.72346 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca77f5ac-594c-3802-a6ca-48dd84252633 | -2.95285 | -53.7201 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e151a6f6-2d04-34aa-a12d-a30d72296c04 | -1.21022 | -51.77472 | 2024-11-19 05:31:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57aee0c1-c7f6-386c-9ced-9fc0ef164a27 | -3.08681 | -54.65887 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69760c8f-b805-3043-a45f-b6a94f3e9f47 | -2.95336 | -53.71672 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d71468b-2675-36db-95ec-285f56041f46 | -3.19973 | -54.32273 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 28cd98a2-8088-3421-beea-465ae00df3fd | -3.06482 | -53.27733 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93c86c01-2965-3a5e-a94e-2d945111acb4 | -2.42771 | -54.61723 | 2024-11-19 05:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ecb3887-381d-3f85-87fd-79ee7f71091b | -3.33493 | -53.35346 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fb670f7-5d77-3b7a-b516-49d34990561f | -3.06373 | -54.40824 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7f6f874-e147-31fe-9096-de52061f1833 | -1.19601 | -51.98178 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6eff83ed-769f-378f-85f9-ab81907d9720 | -1.6995 | -52.14573 | 2024-11-19 05:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c141547c-7cfd-30d0-905e-a4b39e17c965 | -3.08594 | -54.66476 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1eaf94e-242f-3ebb-8f77-863c21624af2 | -2.90576 | -53.05415 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9cf10a36-b2c7-36e0-987b-d9f58f9d109a | -3.20021 | -54.31961 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d9f6554a-9df0-354b-941b-6c4758e5bad3 | -2.28363 | -53.63578 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2a84549d-d948-3d99-8379-0ac02fb1a679 | -1.43775 | -53.38778 | 2024-11-19 05:31:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37fb3802-135f-38cc-8331-ac11b88458b2 | -1.58638 | -53.80735 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1e79148-0f27-3245-b75e-7865c46553d2 | -2.137 | -53.64286 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d610756-cfc8-355f-bb4d-dcfc5aabed79 | -3.36671 | -54.10754 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63fc16f2-0c46-3b1f-bd5d-eb1a6f2b21d6 | -3.18718 | -53.24685 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ded35f4-23fe-3194-b659-2d6a42319064 | -3.36247 | -54.10011 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb1b1fff-c685-3c7a-850f-d44b34f05c19 | -3.05907 | -54.40432 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54d6055f-04ca-32cf-ad1f-f4b3c428e9d7 | -1.92374 | -54.06139 | 2024-11-19 05:31:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 3bf5073d-e7c3-3cc3-9d35-e120aa538808 | -3.05301 | -54.40979 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95eef9d9-8a34-3b83-9c2d-8878977132ce | -0.14707 | -60.87003 | 2024-11-19 05:31:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1f4b98e-a470-335f-bc4a-114590bee12f | -3.05255 | -54.41288 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae9bc748-a883-30f4-8567-b021c9679eee | -3.06323 | -53.28422 | 2024-11-19 05:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d130256-ad1f-3a50-ad51-2ef7f20e2c6c | -3.50983 | -53.80017 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ebfa34de-cd07-3f66-8438-8b45773aee1a | -3.51033 | -53.79688 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e098b659-b633-39b8-8ce8-3dbe36cfbc23 | -3.0586 | -54.40748 | 2024-11-19 05:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d3dfe9d-4d19-3ec7-90e9-20024eeaf78e | -2.1993 | -53.66335 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfc00274-cbfa-3056-a5d2-6e80fdef002b | -3.5495 | -51.52632 | 2024-11-19 05:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ddbaf38-3d22-3df3-ad9a-5c7c9e79bff3 | -3.11426 | -53.70705 | 2024-11-19 05:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eb24d64-4537-3fc3-b424-0e3c6a3c054c | -1.58308 | -53.79832 | 2024-11-19 05:31:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README48.md)
