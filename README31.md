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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f025265-7b7b-36c6-b880-dd0ef8a93c0d | -5.43739 | -50.62362 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d3b96f0-1795-3984-a38b-d3682eaaef88 | -5.4338 | -50.62303 | 2024-09-30 04:29:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82317043-feb9-358a-b041-c3db35777624 | -5.29603 | -50.07023 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9c329954-4ddc-3672-813d-903718a84f95 | -5.29572 | -50.06739 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c265e93f-6cf0-36df-9935-65a2ebfebf21 | -5.2951 | -50.07132 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4ab446a-f4d9-3c7b-bf40-0571770898d2 | -5.26464 | -49.90264 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 299b3add-f3ef-36ae-8395-010412465f12 | -5.26115 | -49.90206 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90272e81-e860-3d41-9648-aff8413e156a | -5.26053 | -49.90591 | 2024-09-30 04:29:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe4095f9-1e7c-37d2-b447-a0318c8416d0 | -6.84009 | -50.48954 | 2024-09-30 04:29:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fe8720f0-764a-3589-b602-c6459a63cecb | -3.55866 | -51.64876 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87f6d78f-3305-39aa-beb0-08bfc355c583 | -3.30292 | -50.66392 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4721928d-c64c-332c-861d-b5229c582076 | -3.30222 | -50.66829 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 61dfafe7-3d2c-377c-a3f4-292a399f971a | -3.29923 | -50.66332 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d5e2fd12-b15b-3615-a856-513c97dd5af6 | -3.29852 | -50.66769 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 537cad58-a927-3bd5-8528-164cbfd66919 | -3.21212 | -51.01285 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| b35090d8-caa0-3d62-afa7-c8717ee5cffe | -3.20835 | -51.0122 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fe7a4930-cbc3-3e4f-926d-d8d59cd7c2dd | -3.20023 | -51.15812 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0dba9042-2348-3488-b13b-3418ab108537 | -3.09418 | -51.28842 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d1e44b21-05a8-3777-b250-5d43e4439ab2 | -3.07419 | -51.217 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f4e5751-aa56-3ec3-a20e-7cdf712e97c8 | -3.07342 | -51.22176 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7f1821c9-0036-3f45-a7cd-12552dca1840 | -3.07114 | -51.21161 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6cae6bb1-348c-39b0-add2-31049538fd67 | -3.07036 | -51.21639 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5144e1cb-53f5-3702-a5c7-73fbc7c7040c | -3.06958 | -51.22118 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 40749c38-5b75-3015-8c90-03c4d87cba46 | -3.06653 | -51.21576 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e8026ce-bb96-3d08-b83b-2070469b2f9c | -3.0367 | -51.44771 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 9693e911-a5c1-3ade-89b5-df1210d104e2 | -3.03589 | -51.45269 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 318be920-e300-3a3f-b50a-249e0c81967e | -3.03279 | -51.44717 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fa11d543-96f8-3052-ab4c-15713fbda9a6 | -3.01516 | -51.35268 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be42a806-5747-300c-89d7-3ac0c118ca1b | -3.01213 | -51.05111 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 19b18128-c520-3561-836d-2be1c51dc3f3 | -3.01017 | -51.46341 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e1ccc8f-4617-3545-b35d-58da7a8728aa | -3.00908 | -51.04587 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5404c3a5-a090-33ce-ad84-340ff0a7aff1 | -3.00833 | -51.05051 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2278460-848b-3d7f-8ba2-ccd6f196c4fb | -3.00758 | -51.05515 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8aaa851-d4a5-38f4-8f85-be66b5a7291a | -3.00453 | -51.04991 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d109c37-9dc3-32ca-b68b-c2bcb2934650 | -2.96058 | -51.64711 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9eb202b6-4e10-30f6-8c41-b6fe3d67ca52 | -2.95979 | -51.65213 | 2024-09-30 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2e4e7e5b-3a60-3fc0-a007-9b0c31861d26 | -2.88071 | -51.66536 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0381ab2a-8cb1-346e-9270-5d4a3bc94e8c | -2.87676 | -51.66472 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ead1120d-a98a-3ce0-96b3-2251df6b68c6 | -2.87594 | -51.66975 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f3daed3c-caa3-3e82-9749-c4bd972f3863 | -2.87314 | -51.66783 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a480f7a4-86a9-370c-a4ce-b72edc184d69 | -2.87235 | -51.6729 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68ff90bc-be94-3eeb-8007-cecbe82be1a9 | -2.87198 | -51.66912 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95ab90c1-de5b-3d05-ae6f-8eeaffac2b11 | -2.87156 | -51.67797 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d732737-92d6-3680-8e99-573a8e9744ab | -2.87115 | -51.67418 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c801a20-35c1-30ee-8186-6cb746852f7f | -2.82441 | -51.34497 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a09c6937-ad1f-33ff-bc5d-49fbf70d816e | -2.80954 | -51.94202 | 2024-09-30 04:29:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8fde436c-93b2-372e-965f-d8d28c36711a | -2.70674 | -51.34645 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 710088f5-4a57-32bc-8464-e8b2727a2b01 | -2.70598 | -51.35129 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3e8d3efe-6c3a-3f87-83f7-50d8bcfd55bf | -2.70423 | -51.34364 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e9023e16-7c4b-3960-af4d-23f3abb8d252 | -2.70344 | -51.34848 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 6b4e54b3-45c6-3d95-b065-15e4a468c80e | -2.70285 | -51.34586 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 55742a90-2ae5-31d4-bcea-d2fda7866a1b | -2.70265 | -51.35329 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6028441a-e234-31d2-8a7e-3f5121f4b27c | -2.7021 | -51.35069 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 34a6f8a6-ed96-3f0a-84f5-0399736b8a23 | -2.70035 | -51.34303 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 86e118ab-f7bd-377a-85e4-960ebed32723 | -2.69955 | -51.34789 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| b042741e-e844-3958-94f1-90dad770116d | -2.69897 | -51.34524 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f3d20d3b-eb1c-3ac3-9258-0c626f48a883 | -2.69876 | -51.3527 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b89d1b4f-ba59-368c-8116-cfe492a5a84b | -2.69821 | -51.35007 | 2024-09-30 04:29:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7db08fc9-5658-3433-9118-2e028b974baa | -4.61548 | -50.97205 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 764d7fa1-7fc9-38ed-8a29-4a1849bfbaac | -4.61178 | -50.97142 | 2024-09-30 04:29:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c8ae7f5-452c-3cca-a381-4c69d49bedaf | -4.13093 | -50.82254 | 2024-09-30 04:29:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54f7ea03-18ac-3a23-bd96-574f28fa1e53 | -0.79216 | -52.48512 | 2024-09-30 04:29:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a84a5542-2a43-3900-9e45-3a98cbb0e0e9 | -2.20064 | -52.05053 | 2024-09-30 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 56ac6f54-1e27-3704-9805-97f0a7840787 | -2.20005 | -52.0542 | 2024-09-30 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 667b6d2d-8a41-30a4-8206-c4ee4f7daafd | -1.87716 | -52.0931 | 2024-09-30 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f18f3aa3-a9d1-3847-beff-02d45b086d61 | -1.87657 | -52.09679 | 2024-09-30 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69cb8b35-5caa-3b89-b879-75c93afa788f | -3.27011 | -52.59491 | 2024-09-30 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32bcc3b9-3770-3d8e-a13c-bf1bd140ae19 | -3.24106 | -52.79682 | 2024-09-30 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34b90326-ae0a-3ef4-8bf9-51a8ea16f140 | -3.0796 | -53.06504 | 2024-09-30 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 117327ef-7b83-37c9-a0c0-efa5a7b7833a | -3.07767 | -53.06551 | 2024-09-30 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3969a53d-b89b-35ea-b928-e2be97f53ab0 | -2.85543 | -53.32945 | 2024-09-30 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 543da90b-5fe1-3a9f-99b9-f205e62bec14 | -2.85102 | -53.32871 | 2024-09-30 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b09c9333-bd05-372a-8c99-0cc8bbf8e6a0 | -2.7585 | -53.23204 | 2024-09-30 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1f364c21-5582-3178-920a-3fa6b17f6803 | -2.75411 | -53.23134 | 2024-09-30 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab824807-19e8-3a3c-8d93-19479f3a394d | -2.68404 | -52.43816 | 2024-09-30 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00f84989-6d97-3981-ab57-2580d7b05bd6 | -2.67989 | -52.43736 | 2024-09-30 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd375843-1a69-378d-9642-0d7db26f5d8e | -3.73625 | -52.42456 | 2024-09-30 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae69f9ea-ae3b-398f-bc11-f1a8432dfac5 | -11.91452 | -55.91473 | 2024-09-30 04:32:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9ae62fa0-277f-3426-9c28-cc361e52601a | -11.91366 | -55.91938 | 2024-09-30 04:32:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e3a3eeff-f901-3514-9c1a-5071d8e42add | -11.91309 | -55.91636 | 2024-09-30 04:32:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 694d9b66-e3f8-3046-b815-5cf13d56be12 | -11.48692 | -56.78135 | 2024-09-30 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1588fc9-15e5-30f3-b44e-804e2fa55c87 | -11.48592 | -56.78677 | 2024-09-30 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 574518db-22f8-3f41-ad62-465e7d9c1b7a | -11.48209 | -56.78043 | 2024-09-30 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5f4e0587-5d29-3cdf-a5cc-a2f8dbd9d916 | -11.48109 | -56.78585 | 2024-09-30 04:32:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| ff604e9d-b8d7-3735-9d68-4f02cd4c9124 | -10.51743 | -57.77916 | 2024-09-30 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27b358d6-0163-3a98-b132-fd5c8d2afe18 | -10.51681 | -57.78247 | 2024-09-30 04:32:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d279c3d9-0512-3ed6-9e04-b62fa7bb63b1 | -10.13235 | -56.76631 | 2024-09-30 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e2d7a6d4-b3db-36b7-867e-b85c5a6337e2 | -10.12916 | -56.761 | 2024-09-30 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0a151db7-166b-375a-a48c-228dd63969eb | -10.12843 | -56.75966 | 2024-09-30 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 26879e28-d12b-3de4-8026-34e9fe29175a | -10.1281 | -56.76671 | 2024-09-30 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 5b5e04ae-0b4a-3209-b5de-03faca7c3d4b | -10.12741 | -56.76538 | 2024-09-30 04:32:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a719b9f1-1edf-3bc1-933b-413fd87e9b8b | -9.89805 | -57.06302 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be554281-56ce-3500-82b1-118fac12b8b2 | -9.89749 | -57.06607 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cc4932d8-7f6a-3944-89d9-9ca15325f8c0 | -9.89302 | -57.06191 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4148d0e2-4e86-36c9-a366-02524403faa9 | -9.66931 | -56.95919 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0543ed72-a3cd-3561-8843-350242446916 | -9.66875 | -56.96219 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c898dbc5-63be-3c7a-a281-df0e58ccf914 | -9.66819 | -56.96521 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee1ade39-7d89-343a-9e4e-65a9553ec15d | -9.66536 | -56.95235 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e341c16-389c-3fc0-b9eb-2bb397acd6dc | -9.66481 | -56.9553 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fdfefbc-c87c-3639-b51b-145f2096d999 | -9.66425 | -56.95831 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README32.md)
