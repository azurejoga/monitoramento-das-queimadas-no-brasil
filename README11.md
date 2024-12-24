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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4dd1fced-d24b-3a55-8fa7-0a5bf4d99c99 | -3.03351 | -50.4954 | 2024-12-24 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fc309457-1257-37e3-a7fe-64f1d36dc9eb | -2.50454 | -54.65603 | 2024-12-24 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a66d0ad2-af78-3e92-88bf-c643ff001c5c | -12.25141 | -63.46574 | 2024-12-24 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 055a286e-1486-3fa1-b959-1db5eec638c0 | -9.22532 | -60.33547 | 2024-12-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43444f82-b994-3df6-95fb-c316e773f498 | -3.10278 | -54.54992 | 2024-12-24 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b682af58-fff6-3014-ba95-953010b82efd | -1.98904 | -54.21588 | 2024-12-24 05:31:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c5251bcb-de1e-31db-a256-5ed09fd59920 | -7.98652 | -61.60344 | 2024-12-24 05:31:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90c9ed5f-44e9-3715-a894-fe880e64d5fe | -1.52135 | -54.95569 | 2024-12-24 05:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34ca7e2c-f7c2-3b77-a89f-9a9631e55e24 | -2.41562 | -54.21845 | 2024-12-24 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d1c92a2f-ab52-3994-afc4-f7bee0768a83 | -2.37924 | -54.61615 | 2024-12-24 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d13264e-d932-3ef0-8f9c-b499c5e437e1 | -3.58427 | -54.30543 | 2024-12-24 05:31:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bbdcedb1-5cc8-36a9-8d8c-8e37c8c184d1 | -3.14913 | -53.18579 | 2024-12-24 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17295015-1ce3-3996-a3e2-3e05e6c91ac4 | -2.97302 | -54.13013 | 2024-12-24 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7a1b032b-cb1b-3679-95b4-f8315890a59b | -3.02756 | -53.89563 | 2024-12-24 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f252ef-7480-3d3d-88b8-f13617061444 | -1.7134 | -54.48685 | 2024-12-24 05:31:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dee7076c-fc0a-3ef4-ab6a-8d74ab397776 | -1.95155 | -56.49551 | 2024-12-24 05:31:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7ff212d-0e43-3125-a11f-f0d74e62d532 | -12.25196 | -63.46222 | 2024-12-24 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fb6eb8b5-d84b-3d9c-8ba8-232fcd98f9ec | -2.40526 | -54.19169 | 2024-12-24 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e3a3e84c-3a66-3856-a3d0-4efd5f4f06eb | -3.13283 | -52.12847 | 2024-12-24 05:31:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbcc5c46-09f6-3925-9372-154eb3bdc631 | -2.5884 | -54.2504 | 2024-12-24 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe15d61a-1fd8-3f93-a8e3-0fe1bd7fbd44 | -3.02835 | -53.89033 | 2024-12-24 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cad7271b-77df-3151-b483-50e0d8fb4d9f | -2.86813 | -51.65865 | 2024-12-24 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35833ce0-e88e-3cfa-b27f-f03965d9e340 | -3.03239 | -53.89634 | 2024-12-24 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 17a00ab4-a6a9-3e08-9f36-9311196df29b | -3.07053 | -54.64023 | 2024-12-24 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bbef606-fa66-3b5d-8516-caab300b2722 | -3.13334 | -52.12497 | 2024-12-24 05:31:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65a479d8-ebad-33e7-96c6-d1dcc581ae44 | -3.14869 | -53.18874 | 2024-12-24 05:31:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9802324-99cc-3fb8-9b5e-580dc9e5a7e2 | -3.06983 | -54.64475 | 2024-12-24 05:31:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65202767-b2bd-33e0-866a-d60afd6c6027 | -2.3747 | -54.61544 | 2024-12-24 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 43d19a3b-a826-3745-ab59-59af837b677f | -3.80625 | -51.03335 | 2024-12-24 05:31:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e6a8f4b-1dbf-3fed-9d4e-ee6df6267869 | -2.97226 | -54.13518 | 2024-12-24 05:31:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1332d92d-ca6b-301a-9978-5ea1c3061449 | -9.22591 | -60.33152 | 2024-12-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1143699f-6300-3437-a64c-4bb5289b0271 | -2.41095 | -54.21771 | 2024-12-24 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6b5331b4-1b56-351a-adbe-748626fb0fcb | -3.03318 | -53.89105 | 2024-12-24 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 93f87d80-75e1-39fa-af37-a9e266146f17 | -3.58871 | -53.71019 | 2024-12-24 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 62f00368-50e7-3d91-bc4e-c9f6ac72120f | -9.22884 | -60.336 | 2024-12-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da8a78ef-7406-311e-9117-4ec19438ef1b | -2.86868 | -51.65482 | 2024-12-24 05:31:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c027e679-596c-3861-b50b-54dda6bf271f | -3.0623 | -53.79633 | 2024-12-24 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b61079bb-84b0-3c01-91b8-652b18593fd3 | -9.92923 | -59.90478 | 2024-12-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 94f5a915-ac62-3c7f-bd6f-88635998a816 | -9.66627 | -66.57462 | 2024-12-24 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7d069698-f503-3732-a44a-967e36f1b6a6 | -7.91797 | -61.54216 | 2024-12-24 05:31:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d33be9a5-b794-33e8-886d-d451d1448f19 | -2.76797 | -52.64573 | 2024-12-24 05:31:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fa150d3-504a-338c-b2f2-5d3f12ca0404 | -3.06309 | -53.79108 | 2024-12-24 05:31:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da1a6f15-72e1-33f9-ad14-615859152788 | -2.79578 | -51.77114 | 2024-12-24 05:31:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca54d916-f096-38f4-9acb-ec311e02f685 | -9.22181 | -60.33495 | 2024-12-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64e5a5be-2b4c-30cc-a22c-7ddd87bf14d8 | -9.22122 | -60.33892 | 2024-12-24 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b70923bd-d6c0-3ab1-b220-7e3d0b90fb29 | -12.25527 | -63.46275 | 2024-12-24 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2110a97e-23cd-372e-9a07-e2caaae2c9eb | -9.92623 | -59.90005 | 2024-12-24 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38b7676e-6b84-3cd8-b051-77d89e966a41 | -2.41168 | -54.21281 | 2024-12-24 05:31:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2ae396e0-91cb-3a7d-b56d-f5c0a3b2dc25 | -19.83496 | -57.48824 | 2024-12-24 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2ed939a8-3eca-39a8-8e83-2d0e19be6241 | -19.83915 | -57.49435 | 2024-12-24 05:33:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e08e2069-ba6b-3358-9b47-058e1a1ba530 | -2.3649 | -45.5912 | 2024-12-24 05:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 00537118-1a28-36d5-ac2a-439256ef76bb | -2.3463 | -45.5917 | 2024-12-24 05:50:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 7fcfbe25-33f5-36e8-9f21-c9640efe5fa3 | -2.7654 | -52.64373 | 2024-12-24 05:52:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2e48ec68-6dcf-309f-b1e9-44f96da7f5c3 | -2.08407 | -45.36224 | 2024-12-24 05:52:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 19.8 |
| d35a649e-b15c-3767-9fc7-ddcb06e10379 | -3.02883 | -53.89013 | 2024-12-24 05:52:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6862f9e2-e3e3-303d-87b7-ed8c813a1963 | -2.34148 | -45.57941 | 2024-12-24 05:52:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 68a7b4c0-bd57-3e8c-8df3-37eb99b6478a | -1.70898 | -54.48353 | 2024-12-24 05:52:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1410a828-f112-3f55-8542-0279dd071491 | -2.35429 | -45.58119 | 2024-12-24 05:52:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b77730d4-3695-3fd8-83f0-926d262387a3 | -2.54617 | -54.76139 | 2024-12-24 05:52:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 94cd43e1-373b-350e-96a6-8d69cdb55b6a | -2.76512 | -45.09085 | 2024-12-24 05:52:00 | AQUA_M-M | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| a56e7bfa-ade6-3c92-8ee0-70d3a14b4549 | 1.00705 | -59.50474 | 2024-12-24 05:52:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 339272eb-db25-3ee3-b324-80d810e27eed | 1.01182 | -59.50404 | 2024-12-24 05:52:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc49bbaa-9c71-389a-a003-3113b2a9574d | 0.557 | -59.80565 | 2024-12-24 05:52:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25680b95-336f-3a31-bff3-74cf996415f9 | -6.22984 | -55.62593 | 2024-12-24 05:54:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 7979b203-b4b6-32fc-97aa-f795fc0b13cf | -6.2315 | -55.61508 | 2024-12-24 05:54:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| a7826c45-0a3e-3bcf-98cf-a5a87314fe97 | -6.23062 | -55.62933 | 2024-12-24 05:54:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 93c2374a-4e09-375e-9ef1-46bc72dd59d3 | -2.35904 | -54.61922 | 2024-12-24 05:54:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 89271a5f-efd0-3606-a7ab-fa26c4a0384e | -3.58461 | -59.61158 | 2024-12-24 05:54:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 211d2cf5-24d2-3c96-92ea-5163ffae3af7 | -2.35998 | -54.61291 | 2024-12-24 05:54:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 290dc657-2a73-302b-a632-63a424470757 | -2.55517 | -54.76497 | 2024-12-24 05:54:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 55e61da6-3e31-3b91-9544-1079c6909b26 | -6.23144 | -55.62323 | 2024-12-24 05:54:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a80e5c2c-3345-3798-80bc-82635a073206 | -3.58416 | -59.61456 | 2024-12-24 05:54:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f73bf816-03cd-335d-9ac7-33fe0fdcc148 | -12.25371 | -63.46568 | 2024-12-24 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42832303-6dfe-3a0e-a524-0d71e84e26a4 | -9.66718 | -66.57515 | 2024-12-24 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c6533ef-3ae0-3af3-b8a2-7062df728aba | -9.93172 | -59.90619 | 2024-12-24 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20b2540b-bdaf-3799-a4e5-a5a855b25870 | -9.66503 | -66.57201 | 2024-12-24 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3386f39-1096-338c-a02b-c0c9406b1e12 | -12.25063 | -63.46307 | 2024-12-24 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 78816107-3684-3b63-b0ed-bee2cd11e4b1 | -9.22513 | -60.33726 | 2024-12-24 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 297b51c6-39be-37e4-ae6b-a044c661010e | -7.91943 | -61.54041 | 2024-12-24 05:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c8a1a4f6-4b49-3480-9994-ea9dc26e631e | -9.21943 | -60.33982 | 2024-12-24 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c8eb654-55ff-32d5-aac8-2cd514a43c14 | -9.23083 | -60.33478 | 2024-12-24 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f3d721e-afc2-3d8e-b453-7b6600e94f4e | -7.91906 | -61.54311 | 2024-12-24 05:57:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| da465eca-4a30-3fa4-b730-f4816c683857 | -9.92625 | -59.90543 | 2024-12-24 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 660d8dee-1ca1-3c09-92cf-8a84dd33231b | -9.66859 | -66.57255 | 2024-12-24 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4de6b480-7005-3b93-b8f1-b488fa022a4e | -9.22556 | -60.33405 | 2024-12-24 05:57:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a553a98f-f09d-3473-8ad6-28869aa74311 | -9.66777 | -66.57111 | 2024-12-24 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cb6a6ba-6de8-3408-bf96-c710d89cee9c | -19.83525 | -57.48783 | 2024-12-24 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 78fc9036-2992-3c6a-aa93-04588d290c7c | -19.83468 | -57.49498 | 2024-12-24 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d82ed231-e3f2-3527-8568-979cca46b945 | -2.3463 | -45.5917 | 2024-12-24 06:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 86.0 |
| cc0d2ba8-ff72-3247-918a-f091fa005cb1 | -2.3649 | -45.5912 | 2024-12-24 06:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 41056637-54b0-37a9-a687-3920d72808f3 | -2.3464 | -45.5693 | 2024-12-24 06:00:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 5cab63f6-b169-330e-800d-f49f3303a32c | -2.3464 | -45.5693 | 2024-12-24 06:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 59.8 |
| cb979e79-470b-3c29-bf3b-ba11f85aaa55 | -6.2339 | -55.6308 | 2024-12-24 06:10:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| c5a84354-3a8b-396e-b8ce-7d8a24b29715 | -2.3463 | -45.5917 | 2024-12-24 06:10:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 83.9 |
| fcb514c3-e93d-349c-9bc1-2d3f8c0f9c56 | -7.91583 | -61.54275 | 2024-12-24 06:18:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24dd9b9d-30b2-38c9-9dc9-529249942f8e | -6.2341 | -55.6109 | 2024-12-24 06:20:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 5f5ec292-dd98-3574-bb1f-8c2d6adad80b | -6.2339 | -55.6308 | 2024-12-24 06:20:00 | GOES-16 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| b6a35c33-6f68-3d5b-b589-acb41ac02887 | -2.3463 | -45.5917 | 2024-12-24 06:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 8033dac5-5cdc-3f21-925e-a88f164f721e | -2.3464 | -45.5693 | 2024-12-24 06:20:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 8dbc4509-50f0-3223-9f20-eb54e0a16b2f | -2.3464 | -45.5693 | 2024-12-24 06:30:00 | GOES-16 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 49.4 |


[Clique aqui para ver as próximas entradas](README12.md)
