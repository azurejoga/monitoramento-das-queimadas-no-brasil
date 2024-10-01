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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ba5176f-ed77-3c15-b921-b549fe061c60 | -12.99571 | -51.35348 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f4ab36b4-152a-373a-a727-22b2ea02c7b3 | -12.99549 | -51.3219 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 62cad93a-73d7-35a0-85cd-26df4cac312a | -12.99536 | -51.27854 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 48cdc192-10e0-3e14-bbd1-5df7fcae4d7c | -12.99502 | -51.25917 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 078268da-9ddd-31f9-9b84-5d5796f8efe5 | -12.99493 | -51.24721 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b3ef6d0b-0aac-37b8-a56c-0e720e31cbb1 | -12.99478 | -51.22798 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 924ef39d-5f90-39a4-b340-293636ded01f | -12.99454 | -51.31603 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 1b63f595-94b8-32fb-84df-74dbb4fb095a | -12.99421 | -51.32789 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| f46c364b-24d3-3aa8-9c4c-b70743f9c32f | -12.99412 | -51.28452 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 773846c1-0c28-35cc-8f9e-9ef038d6da25 | -12.99374 | -51.26513 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d271e0aa-506e-3b48-9856-060cfb7f91dd | -12.99369 | -51.35374 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c3229099-3330-3155-9d65-dede51d16c93 | -12.99369 | -51.25316 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8b566457-c570-3d80-a9ef-01986d8761b6 | -12.9935 | -51.23391 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 80935677-4e52-3478-be75-561b60afe5eb | -12.99328 | -51.32206 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 4e040e03-bd54-3a73-9690-96b0d626bf2c | -12.99326 | -51.22194 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 7744d66b-ffad-36eb-83ce-8991b789f093 | -12.99246 | -51.27108 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5164058c-5f79-3f77-9c76-d95a271ee6f8 | -12.99245 | -51.25912 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4575218e-9944-3c62-b9eb-1607113fa533 | -12.99243 | -51.3598 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f77ed1bb-3bcf-3b33-ae45-84e74d105354 | -12.99222 | -51.23986 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0dd54ce5-9b78-3797-9d07-fc0da966bd52 | -12.99203 | -51.32806 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 1ec3a3f4-ccbb-3c0e-90bf-4212b406839a | -12.99202 | -51.22787 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 60a742a2-64c1-3698-8c74-58441c0baf3c | -12.99121 | -51.26508 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 932927d6-91c9-37d1-840b-5811da3168b0 | -12.99118 | -51.27703 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7606a498-f21a-3e29-b4b3-80af6de9fd1f | -12.99078 | -51.3341 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 0ce9d8f2-fb94-37fc-86cf-e506732b09bd | -12.99078 | -51.23381 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7f723337-9f83-336e-b5ec-31717088abee | -12.98997 | -51.27103 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 1e6ff644-1a86-3994-a0bb-af92fc5f620f | -12.98989 | -51.283 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a35adec0-a725-35c2-962f-b16000825c94 | -12.98954 | -51.23976 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 47a3a4f7-922f-3215-a2fa-a667ada24fe7 | -12.98942 | -51.22061 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 391a54d6-9dbc-3a9d-a0c4-880a9d3a40ba | -12.98883 | -51.3204 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 22.4 |
| df14c5dd-3a7e-306a-8e5d-ec79d084f70a | -12.98872 | -51.27701 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e1a09444-78f6-3093-a5f5-fd2f5fa0eece | -12.98838 | -51.25768 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1b1d4ba6-280d-383c-81bd-ec9dcdcfe80f | -12.98814 | -51.22654 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 4a9e5899-0297-3b48-920d-6cddc62668c0 | -12.98774 | -51.35801 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 76fd5604-c0c9-3788-b3fe-b36c52f09405 | -12.98754 | -51.32639 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 73b04b07-941d-39ca-ab11-c21104bd196a | -12.98747 | -51.283 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b36acff7-5adc-36d0-96dd-b8ab8b7d9293 | -12.9871 | -51.26364 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 916840c0-800d-38bd-9b1f-f93df0350c23 | -12.98687 | -51.23246 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| b28bddaf-b3e9-32ec-8c3d-2d871e97a86a | -12.98625 | -51.3324 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 3bd7c1f4-9217-3c1a-b89b-ad080702244c | -12.98582 | -51.26958 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3563113e-3df9-3ae7-80a8-8fe1877e2538 | -12.98581 | -51.2576 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b33d14a0-2020-35d3-89c5-da09bdc48107 | -12.98575 | -51.35826 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bcf26898-2180-32dc-bfac-25be0b908873 | -12.98559 | -51.23838 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 14d5fc20-9340-3766-8d95-18ea6616714c | -12.98538 | -51.22638 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.8 |
| e843a327-9bde-3480-ab2b-b6f8614ceb0f | -12.98537 | -51.32653 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f6f6afb4-11d4-3cd4-9c39-59b3edd88dd4 | -12.98457 | -51.26356 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e429138d-9173-3d9c-97f2-cc1241447d11 | -12.98453 | -51.27555 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| dc9ea6ba-c949-3ef0-8031-29106e619e52 | -12.98414 | -51.23233 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 5367d3b2-60bd-3f6e-95d7-159d00fb20ac | -12.98412 | -51.33256 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3dcf1c8c-3a08-3b26-845c-05d6bc6cb0d1 | -12.98366 | -51.34444 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c73e88ad-932f-3503-8b63-09c1582782c2 | -12.98332 | -51.26953 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 20fa1de1-526f-36f3-a7c3-71399a3cfa3c | -12.98302 | -51.25026 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5602f357-cb52-37d3-97b8-8ab8a2f2e2e0 | -12.9829 | -51.23826 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 7b971c16-78df-3600-968d-ffc6a421a0b8 | -12.98174 | -51.25619 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 273f82d2-a5ff-327c-af86-d8691b7284ca | -12.98164 | -48.54062 | 2024-10-01 03:49:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd3eaf27-8db8-3510-b45f-bff0a6487174 | -12.9816 | -51.34465 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| addb7ebf-cec7-3d72-8ddb-b9b41673eb3a | -12.98152 | -51.22504 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 898f8ce2-a81f-3469-a3d8-2dab968d4f52 | -12.98045 | -51.26215 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2cf796f1-e1ea-3ec5-a4f8-03608c690ca7 | -12.98041 | -51.25015 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ca1eedc7-3770-3b86-b39a-11dfb90efa30 | -12.98034 | -51.35069 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f49b0693-b7e5-36ac-a55e-42ce03f8a0e2 | -12.98023 | -51.23098 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.1 |
| a3d7bf8a-3d1c-3faa-9f55-87f5dbcba288 | -12.97958 | -51.3309 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02e7f580-b1de-3261-af4e-50e91ec42417 | -12.97917 | -51.26811 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9ede1de2-f4fe-3197-99dc-94303eac1b03 | -12.97917 | -51.25608 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 27a3f520-2810-3179-935b-bf888cf5ef8a | -12.97895 | -51.23691 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 046bbc2c-7d00-3605-a6f3-91fe28fb6d0b | -12.97828 | -51.33692 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 594e1390-e88a-3b10-92d2-4d4003e71df9 | -12.97793 | -51.26204 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e6358080-6189-38f2-9c5c-c78729cafc98 | -12.97752 | -51.23081 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| f46a994a-9bd3-350b-ae69-1ba2296a2273 | -12.97698 | -51.34295 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b3f83f5-7e39-3d29-a5b1-eec732e23eb9 | -12.97627 | -51.23675 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4cb97390-b4ca-396e-9c31-298ea541e385 | -12.97619 | -51.33707 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ad91f37f-190e-3d8d-ae9b-f7822b25570b | -12.97594 | -48.53966 | 2024-10-01 03:49:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b57cffa1-1c04-3724-8f91-60376c85dbf1 | -12.97568 | -51.34898 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bc1243a4-8eb5-33fa-a127-934159938e73 | -12.9751 | -51.25471 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eee9d1dd-62b1-3398-aaf8-30f298c28ab1 | -12.97502 | -51.2427 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2fb68bbc-7eaa-3d2a-aa82-64bbb24b2058 | -12.97493 | -51.34311 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc7f419d-1a25-3fef-a0c4-37af643ad3d7 | -12.97456 | -51.31147 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a48a335-6264-300b-8bce-48b6c0dad5c7 | -12.97381 | -51.26065 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03501ff2-420b-3d20-8936-9454e7be96a0 | -12.97339 | -51.4248 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 5f3d0e7c-e154-363e-b162-f41c849beb60 | -12.97311 | -51.41901 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 7320184a-e032-3307-abf1-bab87f433062 | -12.97253 | -51.25458 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7995f638-a39a-35e3-bdc7-3822fb0d83e0 | -12.97207 | -51.43093 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| ac6d2464-0c30-34cd-a731-ff30557dfd4c | -12.97183 | -51.42516 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1ed88d6e-7af8-3425-976a-513d7547d4e9 | -12.97128 | -51.26052 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d1dfd82-d16e-3bdf-b359-3ab602eb3754 | -12.97076 | -51.43704 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b5babc4d-0a21-3874-93ba-dd37c3d71961 | -12.97055 | -51.4313 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| a65b369b-e3f0-3df1-a213-79243aaea40a | -12.97031 | -51.34144 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cff41154-da1d-3143-a37d-fea0a3fa83bb | -12.97013 | -51.30991 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b2444a1-b36c-3742-b159-0ce3d50ab238 | -12.96987 | -51.36731 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5c162715-8c44-3ed1-8730-7c9e99ad1a02 | -12.96928 | -51.43742 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 5e53f046-a626-3d09-a09d-d8e50e267be7 | -12.96883 | -51.31591 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69fad9ed-83e2-3157-bbb6-716f850535c9 | -12.96839 | -51.24117 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5deb7ae1-6142-3a7a-9b89-139fcf3720d8 | -12.96789 | -51.30994 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffd30a2d-d29d-3269-a765-0c3d68c0a3e8 | -12.96714 | -51.24714 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b8051b43-9419-33ef-b76c-fa5f9e55ce66 | -12.96675 | -51.2159 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d6e2edbf-ee6c-3fe4-b6cb-4d28f9f6d17b | -12.96669 | -51.4233 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 6f2380a5-e10e-3f03-8da7-36ef5a18d6fb | -12.96663 | -51.31596 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 29e54b7f-e8f4-3203-93c9-dd8c32d43f0c | -12.9664 | -51.35953 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ed621635-7be9-3c2d-8d2a-0823f092d3c3 | -12.9655 | -51.22186 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 3c782848-fd99-3a6c-837a-b18ea5d76660 | -12.96537 | -51.42942 | 2024-10-01 03:49:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |


[Clique aqui para ver as próximas entradas](README52.md)
