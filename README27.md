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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c9b78ef-5c13-3409-b294-938e907d5f85 | -3.1061 | -50.2686 | 2026-10-01 04:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| b2506c71-0a57-35d0-aba6-ebe8909f9a27 | -14.3834 | -51.2892 | 2026-10-01 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 29e5544f-9e69-3f67-9506-2f553c488de4 | -14.3838 | -51.2677 | 2026-10-01 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 5f2cc50d-eafe-34e9-a6b1-f809d8ccb18c | -3.2766 | -53.8602 | 2026-10-01 04:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 31384166-2b2d-3e10-922f-da2cb7c48d6c | -3.18578 | -48.02151 | 2026-10-01 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 506faa84-4662-350f-8dac-7532976088a6 | -3.10013 | -50.30154 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0ad1fc9d-d044-3fcc-9807-8354ccba9378 | -3.6944 | -47.12435 | 2026-10-01 04:12:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9167a171-9277-3a05-8c05-5ce895935e99 | -3.80974 | -51.02961 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 09f16611-dd63-387b-b6ca-a38670989fb1 | -2.36419 | -50.35068 | 2026-10-01 04:12:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb287555-fc1c-3b8d-a9af-19af71237714 | -3.38022 | -50.94878 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e14bdce2-f21e-3d3a-91e2-719a00ed8b0e | -2.96741 | -51.02201 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90a9e1ee-8397-3541-9df6-c3627a23e54d | -3.0996 | -50.30001 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d91ff373-c53a-3861-8401-7fc48c5c26e8 | -3.01335 | -51.46029 | 2026-10-01 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 770c9b9f-f197-3f70-9c23-d0ccded56d9d | -3.09826 | -50.27143 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cedd763e-f046-38aa-9cf8-39c24fd3946f | -3.54937 | -41.56843 | 2026-10-01 04:12:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 75b1d6e5-d5a3-377d-b426-7bdc1ce11b65 | -3.16201 | -51.3577 | 2026-10-01 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9cec3536-175c-3195-860a-8c385954e897 | -3.79934 | -50.60585 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c6c0b964-587b-3bb1-b1a8-5cc846739f75 | -3.79381 | -50.60766 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77d1c512-d0db-32b6-8d4c-6bef7d4bf554 | -2.97651 | -51.04807 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 244a44fb-e885-30ab-98b8-0dd016b884db | -3.54526 | -41.57172 | 2026-10-01 04:12:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44a84f8d-ae7d-3999-be18-0dd7ecc58cdd | -2.48362 | -49.25578 | 2026-10-01 04:12:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbd89b5f-cf1f-3fae-afc7-99bd898c0735 | -3.11657 | -50.27453 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 362d2862-6486-30c3-8930-6fb21ac59869 | -2.417 | -49.29826 | 2026-10-01 04:12:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46633cc3-3da7-3e84-b55d-c53fd617f864 | -3.95182 | -49.04959 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e010894-402b-39c7-b39b-63dcb7cb4bcd | -4.16501 | -48.89684 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22b9504a-b092-3963-a572-13b267f70887 | -2.96641 | -51.03022 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5959b7a4-5e5b-3b36-a609-4de64d5c454d | -2.84657 | -45.13183 | 2026-10-01 04:12:00 | NPP-375D | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e8d19a7e-10a3-3fdd-a317-f324ba58e6fb | -3.37689 | -50.95821 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d603c74-4cf7-31c6-9fe9-6d705082e3e6 | 1.96598 | -50.85564 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0124130e-0579-3fbd-a493-38d5c5a97e17 | -1.90344 | -45.81774 | 2026-10-01 04:12:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9366b8a-1c08-3811-94cb-5a0a1223c4b1 | -3.09937 | -50.2682 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 471a4b25-5870-3033-a197-df5acd8a16da | -3.11498 | -50.28375 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| fa644260-d236-3fed-8e4b-1164a5f605cb | -3.09297 | -50.26571 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dc1458b-e0aa-396d-960f-e6ee81689231 | -3.19102 | -48.02255 | 2026-10-01 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bc4de1ef-5748-345f-bb27-9336ae8255d4 | 1.96701 | -50.85431 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bcbc5a6-d95d-3c18-8953-dcb308e2ef44 | 1.97202 | -50.8411 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3d421a7-4958-3f7b-9907-62a9b1dc3fbc | 1.97092 | -50.84248 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3574129-ef1c-30d8-a9f4-58b0298a7939 | -2.91709 | -51.31324 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 777f937e-115e-3d91-907d-8d05bc6b0d00 | -3.42032 | -48.33958 | 2026-10-01 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd2d8a93-7e5c-363a-b076-ba44e9f3ecd4 | -3.79846 | -50.61089 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 124c8750-9ff4-3c2c-b3fc-00ccc50e0d83 | -1.32444 | -49.13214 | 2026-10-01 04:12:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 758b5456-fccd-330a-afcb-fc32cbae0ce0 | -1.90419 | -45.81298 | 2026-10-01 04:12:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c383cae-c6e6-3b26-94b8-8903d10ce6bb | -2.41769 | -49.29422 | 2026-10-01 04:12:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d269d419-a6ac-3c33-9436-9f08f81e8c1b | -2.9756 | -51.05331 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e6ee488-ae22-3101-aed9-5f2c0dea19d1 | -2.97192 | -51.03648 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 72767b6b-de0f-310a-8287-0f65a82383d9 | -2.44795 | -49.22065 | 2026-10-01 04:12:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b65a0d84-e54d-357b-bb3d-08476a71bbee | -3.12111 | -50.28469 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 738b8d3d-7d93-3cca-9cc6-1770bb5a5bb3 | -3.10516 | -50.26785 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9d22326b-7a3f-3865-a0e3-9fd70d0ad6ad | -3.35804 | -39.13173 | 2026-10-01 04:12:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1bc59396-fed2-3c8c-ab6a-896217278a05 | -3.03338 | -48.41935 | 2026-10-01 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f855465-b005-3788-a3d2-d44e3c27dbfe | -3.55016 | -48.17814 | 2026-10-01 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f3ef67b-1f27-33c8-8b89-51df9837efcc | -2.99205 | -51.03459 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 37f1c44d-0936-367b-a868-c74d8fea609c | -3.95874 | -49.44928 | 2026-10-01 04:12:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a52a370d-a08d-370c-a6c2-945411f9b156 | -3.11126 | -50.26891 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dcc556f-b1a2-3d8d-927d-03c6fd4a9fbd | -2.97381 | -51.02315 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 649c7458-03ed-3cae-987a-bb70883c45ee | -2.90868 | -51.32292 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7c7c552-8277-32b9-84df-0130667d2455 | -2.44284 | -49.21576 | 2026-10-01 04:12:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1edaa898-3007-3d99-823b-972d1dfde99d | -3.93638 | -45.41703 | 2026-10-01 04:12:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc5c8957-c799-3458-ad75-b0b795bb9ff0 | -2.97675 | -51.04515 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 228f67d7-b37f-31db-b86c-cc144441727a | -3.09405 | -50.26243 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3fa1f868-59ca-3446-a27d-ff0cb8f30096 | -4.14549 | -48.91191 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53b93578-c780-3a16-b6f9-cc8cefa69e3e | -3.00589 | -51.06934 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f239d932-b088-30f0-877a-f248d2dbd710 | -3.1012 | -50.29072 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dcee1b23-e750-31c1-af0b-6634c6354890 | -3.10888 | -50.2827 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 405d491d-33d7-3ac1-9334-dddfcec9e58b | -3.93202 | -45.41631 | 2026-10-01 04:12:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df90dc42-7012-3958-9c61-a4b4521d5085 | -3.10809 | -50.28727 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5c0522fa-f058-36ce-aaf9-0f15eb922fa9 | 1.97793 | -50.83393 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d40dafd-e97f-347f-bfed-090a4574b85f | -3.27513 | -50.70128 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aeb9fa31-64c8-3e06-ab79-dce457ded8d8 | -3.22035 | -48.81371 | 2026-10-01 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 722147f6-50b7-36e2-bdfd-a0e952ace610 | -2.99845 | -51.0357 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7cee1409-cd4e-393e-99c6-1421cbe7f761 | -3.11286 | -50.25961 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95431dd6-b4dd-3b91-b17d-213ecb808232 | -0.93779 | -47.55337 | 2026-10-01 04:12:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bf2de63-2cbc-3fa1-94f6-c8f3e44e1b9e | -3.10651 | -50.2964 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1af3caa2-e0ad-34a8-a5bd-6408aaad512f | -2.27212 | -48.75469 | 2026-10-01 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46cb76eb-2bdc-3c6d-8850-aa924d63e6ae | -2.97935 | -51.02945 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d84bdd9b-c53a-31e0-ac88-99dd2442caca | -3.1057 | -50.30111 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 447b150b-7a04-3981-a4d9-5cfb308c1a26 | -4.15462 | -48.8914 | 2026-10-01 04:12:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42628701-7c3f-319f-bdea-2b455b38af25 | -3.2555 | -48.77506 | 2026-10-01 04:12:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3d958f8-569f-34de-8d4f-52f24b866aff | -3.1134 | -50.29294 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a58858f7-37f8-3d45-9c12-03225c1db21a | -2.98013 | -51.02719 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 628ace87-f674-38f7-ad83-5581030ba258 | -3.5726 | -51.48061 | 2026-10-01 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23e83920-f94e-3ce5-a388-9d2e35a06a74 | -2.96653 | -51.02725 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc76ef6b-24ee-3820-ba5a-8c7c3cd752e9 | -3.00678 | -51.06413 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c5773d87-ecec-3ef4-ab8e-265240f14761 | -2.91262 | -51.30966 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43aee5e2-4e82-3454-8091-16a91800673f | -2.90963 | -51.31748 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4ab237f5-0c8d-3055-b2aa-351b750a6083 | -2.99115 | -51.03979 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a4aa2d96-d664-3ed1-bd7a-a3c368ee4a0f | 1.96791 | -50.86041 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a692f1da-0b9d-317d-ad77-40e2ffb9880e | -3.37952 | -50.94275 | 2026-10-01 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a1a204b-fa50-36d5-8425-62210078bc57 | -3.41841 | -48.3381 | 2026-10-01 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ae2d581-1975-39f6-a26f-bb58fe752c37 | 1.96522 | -50.84217 | 2026-10-01 04:12:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a07d37dd-992b-3069-b173-b91f7f7ebed2 | -4.4907 | -46.40925 | 2026-10-01 04:12:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8cf670a-a9b2-3b51-8936-b32fa89b23ca | -3.11736 | -50.26993 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3e7c12d0-a439-3e54-b2e7-18593b0b3e1b | -3.54876 | -41.57229 | 2026-10-01 04:12:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d39db930-c059-3067-86ba-fb7b804887e5 | -3.10547 | -50.26929 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 81cbf80c-8e3b-30b4-a5ab-70eb9f6e759e | -2.97833 | -51.03757 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb2ee6b3-38e3-35b3-96b2-3057cb5ddce2 | -2.27771 | -48.75573 | 2026-10-01 04:12:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af89a3d4-799a-37ee-a581-1ae315da7592 | -3.09328 | -50.2671 | 2026-10-01 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 523c3994-fb4e-3656-b341-ba8c260daa2f | -3.55159 | -48.17775 | 2026-10-01 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02e8cdda-39f4-3e08-9afa-200f77b540be | -3.9559 | -48.12907 | 2026-10-01 04:12:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f51ae265-2811-3032-a3fc-3e03fa4c38a6 | -1.90657 | -45.81627 | 2026-10-01 04:12:00 | NPP-375D | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README28.md)
