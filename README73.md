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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88224dea-afd5-31f1-9046-8ad74a5bb2a5 | -10.49048 | -48.18806 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6b40804c-24ec-392a-9242-d69172fce18a | -10.48842 | -48.17493 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3be87904-4206-33c1-8f64-8eb6fe5e0b10 | -10.48771 | -48.17907 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e2570074-a0a9-3d8a-8e06-95e25b93ffd6 | -10.4863 | -48.18724 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eea22bb9-1a8d-30d3-b4e9-265bbf3e5b3d | -10.48432 | -48.17367 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b74c4081-0d5f-3738-a792-a8afc1f7ddb7 | -10.48362 | -48.17777 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3b81fcfc-1fe2-3af0-9ce7-f1733faddff7 | -10.48023 | -48.17241 | 2024-10-04 04:10:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d5392652-a604-3567-ba8c-4ea922444d17 | -10.41585 | -48.17043 | 2024-10-04 04:10:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 284012db-9b75-395f-8926-42bcfaf6c2fb | -10.41164 | -48.16978 | 2024-10-04 04:10:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cedb9970-66ab-354c-a3a1-6fd1c7b62746 | -10.40913 | -48.15969 | 2024-10-04 04:10:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92399034-6015-3558-9b17-c35cea5089b4 | -10.40832 | -48.16425 | 2024-10-04 04:10:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99c1b888-1984-378c-a195-fbb52233f95b | -10.28261 | -47.69116 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b24fd910-59f2-3065-bcb7-3de68c45474e | -10.2806 | -47.70263 | 2024-10-04 04:10:00 | NOAA-21 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| af59cade-b3a4-3323-b14e-962fbd9b5bf9 | -10.12153 | -48.82885 | 2024-10-04 04:10:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c72b8f85-7511-3baf-ab6e-367d682916e9 | -10.11709 | -48.8283 | 2024-10-04 04:10:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c5607d5-1c1b-39f8-b0dc-dbf0da8ad776 | -10.11266 | -48.82773 | 2024-10-04 04:10:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ca907e6a-65c2-3037-9f39-85353daae699 | -10.10749 | -48.83127 | 2024-10-04 04:10:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d76f0b07-9605-390f-8f61-9dd9ed2f58f8 | -11.90257 | -48.31462 | 2024-10-04 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 99cbaacf-1a78-37ac-9180-fdaf496c8fb6 | -11.89846 | -48.31383 | 2024-10-04 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc6bd3cd-46a7-3ac1-8f77-2efa3a01d7d7 | -11.67416 | -47.81009 | 2024-10-04 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c45ab22-304e-37bc-8dc8-4cf64958939f | -11.66889 | -47.81645 | 2024-10-04 04:10:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01b73185-0530-37be-b91e-7f656ba7010a | -11.32318 | -49.00335 | 2024-10-04 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a2bb0d2-b045-3d9e-bc8d-6317819714ec | -11.31883 | -49.00252 | 2024-10-04 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e804e6cb-39d6-3048-b5c9-7c4c8f741f94 | -11.2586 | -48.83876 | 2024-10-04 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6ce40a18-5ef4-3059-a74d-0f63d1b189f9 | -11.25784 | -48.84297 | 2024-10-04 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bf68f57e-19e1-3e3a-9d25-fb0259a61433 | -11.25666 | -48.83877 | 2024-10-04 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff5e35f8-05e6-3be4-8caa-62380f781b9a | -11.25593 | -48.84298 | 2024-10-04 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf3125aa-ecf5-3535-9aa9-706e046803cb | -11.25352 | -48.84221 | 2024-10-04 04:10:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c144408-a289-3ecc-9f43-b92244a1e1a6 | -10.87342 | -48.38962 | 2024-10-04 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 01a9958b-beca-35d4-8edb-0f267d8de1a3 | -10.87272 | -48.39365 | 2024-10-04 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| bb4c18e9-711a-3d21-856f-860a973a7bd7 | -10.8692 | -48.38887 | 2024-10-04 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 50351e13-4921-33da-9ee5-275bb14b8d50 | -10.8685 | -48.39291 | 2024-10-04 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6cc967c4-6d83-33b1-9b8f-7422270e44e8 | -13.51826 | -48.61098 | 2024-10-04 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 80a345c4-7d61-3b2c-b09c-32ad88f1bfac | -13.51482 | -48.60659 | 2024-10-04 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1d678259-b6bf-3294-b8a1-827e6ac83b56 | -13.51346 | -48.61413 | 2024-10-04 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23eb5e17-af8b-3ada-8755-ae80ca205f9e | -13.5107 | -48.606 | 2024-10-04 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af887767-d313-3314-afa9-3da58e800b62 | -13.50658 | -48.60539 | 2024-10-04 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29e94041-6c51-3ddb-bf0b-ae286e010f57 | -13.50112 | -48.63563 | 2024-10-04 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f4d3403-4962-32d9-8f0a-25fd03eb6b43 | -13.5004 | -48.63959 | 2024-10-04 04:10:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a2a18984-cfe6-3c4b-8f51-d7bf2e0dfbdc | -13.32971 | -49.31976 | 2024-10-04 04:10:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8910eec3-392d-3117-98ef-17f259b6017a | -13.23246 | -48.64187 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63daa4c5-763f-31e1-90fd-11d2b99951a1 | -13.23178 | -48.64569 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34064faf-6c5a-37a0-9de4-7ba0bf09e8b6 | -13.22902 | -48.63722 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 990df659-b6d3-31c2-af15-d17febdb3f33 | -13.22766 | -48.64491 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 311326c9-a858-3aa6-98f6-c2608cb27cf5 | -13.22355 | -48.6441 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 409d844f-d0a5-3d8a-bb5a-794d345f9941 | -13.21874 | -48.64724 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3447f0a3-54e1-3ae4-96fa-313aad6488d7 | -13.21804 | -48.65116 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b1c39f2-464d-3c8a-bdac-4c7d9fee3637 | -13.21323 | -48.6543 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1475e76f-4f9e-3795-a868-b35192a83022 | -13.19675 | -48.67498 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 451ea7ec-e025-39f5-af8d-2b11720625d2 | -13.19265 | -48.67405 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f97da80a-89af-3f04-aeac-c8586cc89fc3 | -13.19196 | -48.67789 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 725a664a-81b9-31af-87d1-f86f679991cd | -13.19128 | -48.68171 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c3c94fb-a096-3288-ad7d-1f39c2b319ea | -13.18855 | -48.67313 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50843f6c-07fc-3dc6-9691-92f3f019f876 | -13.18787 | -48.67693 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9f2bdd9-d54b-3838-b697-5906b07b3a15 | -13.18719 | -48.68073 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00beea01-3a53-395f-a131-0f0d77c91089 | -13.18447 | -48.67211 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1090d30c-6e2b-3c7c-99c7-20054fb9dd86 | -13.18385 | -48.62812 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 56565955-d8ee-334a-a50e-6d5d3490da1e | -13.18379 | -48.67588 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 929c3a03-d36c-3bcc-a905-faa5ae555db5 | -13.1824 | -48.68361 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 037c68b5-85c3-3958-b4de-fac39c4ba07d | -13.1817 | -48.68752 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df855f71-88f8-377a-b58d-a9b8fceced3a | -13.18102 | -48.66754 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b11279e-9858-3cb9-878e-870a772b96b5 | -13.18038 | -48.67108 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e6997a55-63c4-3e92-8ff0-bbd69bc30d83 | -13.17971 | -48.67484 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a8b4913d-70e6-3f86-b1a5-9dd1e74ed0fa | -13.17908 | -48.63099 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 81cedbc8-9b63-37d0-8170-88ce9cacd04a | -13.17757 | -48.6867 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e5dcb06-e1eb-3d5c-8768-e16c9f5b739d | -13.1769 | -48.66671 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 72de5dba-d743-3b49-be17-48e2b0cd7f83 | -13.17628 | -48.67021 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 95c4d067-46cc-3ad5-8479-b5fc196f700f | -13.1756 | -48.67395 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 751692ed-0284-307c-9a49-a28756e16a71 | -13.17493 | -48.63039 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6190f8e3-53b1-357b-81e2-1e102687ca04 | -13.17344 | -48.68591 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3efd07c9-151a-39b1-85f7-605876fbad41 | -13.17144 | -48.62612 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 622359c6-2d29-32f7-a420-be58608a5d6d | -13.17078 | -48.67703 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1e98df27-8ee8-3c03-820c-98d9a9fa6ca0 | -13.17078 | -48.62982 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86567cf0-5bc5-3641-a2a8-f765c89a10a3 | -13.17009 | -48.63364 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 772e5bf0-18fe-3bbd-868f-406372b664e7 | -13.16939 | -48.63751 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1945d125-d017-3112-b66d-0f959cddfb89 | -13.16867 | -48.64146 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ba99fd99-887f-34e0-a3b0-1843e18241a4 | -13.16864 | -48.61808 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a7871ad3-ca54-31ff-9806-53e5ffbd196d | -13.16662 | -48.67641 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5915ca69-5156-320b-847b-cbc1a46689e4 | -13.16662 | -48.62927 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a35ba5cd-b8c1-3876-93ea-e5fe453c05d2 | -13.16592 | -48.63311 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9ee80c7b-18a1-308c-936e-3e488e802fdb | -13.16522 | -48.63698 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5283e4a4-3fa0-3392-80cc-9cb262e99570 | -13.16517 | -48.66079 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| db500829-c312-3a20-8e04-8371c6209b8b | -13.16384 | -48.66815 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4ac52db-851f-3eb1-aac8-046b6d061b2b | -13.16383 | -48.62115 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db689a94-7a6c-367a-ae0b-0da6c2c4f35d | -13.16316 | -48.67191 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7ae6caab-dcc1-360a-b591-039f0ed1ffca | -13.16315 | -48.62491 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54711923-43ce-33ca-9cfa-ee40540ded6a | -13.16247 | -48.62868 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8facb3ea-2de5-3cbe-8593-6ca22b55044a | -13.16246 | -48.6758 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6ddd5487-3bb9-34f6-b7e6-717bcfefec19 | -13.16104 | -48.66006 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da500e51-3f3b-390a-878e-9518fe86858a | -13.16036 | -48.66383 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e71ff107-f08f-3876-9f2d-569ee419ad78 | -13.1583 | -48.67517 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a7971ae1-1c06-3f1b-bb8d-b85957bad66a | -13.1576 | -48.67902 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f2960f4-b446-322a-aefa-2c9b1e6a7a6e | -13.15483 | -48.67077 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 33d4d708-0c65-3b5a-9f96-1706dc795b12 | -13.15414 | -48.67455 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 72e775ea-7cb7-3cda-8476-0a82d2295648 | -13.15345 | -48.67833 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| acd49ff5-8cf4-3a42-a5fd-00553b07e862 | -13.15273 | -48.6823 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 994250fd-ff15-3070-b0a5-0908fd383cb7 | -13.1493 | -48.67768 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 117fc005-3701-3fa3-8487-016de749a617 | -13.14859 | -48.6816 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c2d93b61-772a-3d9f-ac65-d207ec0d845b | -13.14444 | -48.68091 | 2024-10-04 04:10:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| feb3b138-8800-3d7a-b388-f1f479442ea6 | -12.48833 | -48.0189 | 2024-10-04 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README74.md)
