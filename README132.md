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

## Dados Diários - Página 132

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8650978c-9625-38f1-8a67-7235bfb2de23 | -13.2624 | -47.81509 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3918971f-c3df-322d-b000-c2f9ec8b79a8 | -15.58617 | -52.49734 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd239b8a-f34e-3ec0-a207-69d2026e684b | -16.34625 | -51.46668 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cb1c3644-d010-3033-8786-db5dd763d982 | -12.12564 | -49.42881 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0d4a00f-d6cb-3693-9f65-ea1b2b7a3c1c | -13.30802 | -47.62546 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6db643c8-c5b1-3a14-9b20-3ce9dd8f7e48 | -17.96524 | -57.58224 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4c69537b-6223-360a-b66a-e2351f761016 | -11.51497 | -54.47434 | 2025-10-05 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b07ff03-5ab0-37bd-b301-28b7a491ebeb | -18.22497 | -53.36626 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26a1b1f2-2516-31c0-963c-1569f9dd63d5 | -16.15773 | -57.57249 | 2025-10-05 05:16:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ec5e3e08-d72a-36bf-a160-0f0f6845726b | -12.60988 | -48.12088 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1482f5a2-bb48-3795-bc47-07d7af5335c1 | -12.38616 | -51.0929 | 2025-10-05 05:16:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ae107c4-4156-3c7d-968f-1e0ffdda6582 | -13.45636 | -47.29369 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a7e2a8c1-7007-34cb-a1da-a94f76ea5cdd | -17.95639 | -57.56885 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2eaebc14-a7dc-359d-a10f-5d0dce9589ed | -15.12297 | -45.73839 | 2025-10-05 05:16:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e05ea5cc-11dd-3daf-9493-fa0226071f71 | -14.6841 | -48.35691 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1bae8c1d-10cc-3f60-acbb-83b428fdd33a | -13.74615 | -47.97059 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7435f345-ba9b-321f-9dac-3d86df284342 | -13.31775 | -48.08146 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf26f344-f6e5-38fb-b1b6-217f1dc12476 | -13.32713 | -48.10484 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ebdd9ff-43df-39a7-a73b-1dfd63cf003b | -14.6129 | -52.52096 | 2025-10-05 05:16:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04debf20-8524-3a9e-9d1f-ac2ed36acb01 | -18.25731 | -53.36341 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0bddf9ac-c1bb-315a-8d07-d1562ea3fc09 | -13.12899 | -50.87685 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 454540d5-f352-35eb-8915-04f81f8645bd | -17.87858 | -57.63285 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 06b415c9-46ac-3986-b077-21a7cb617b35 | -11.92337 | -55.9089 | 2025-10-05 05:16:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d950b1b5-9598-356a-87d6-710bc3e20f13 | -16.35155 | -51.46069 | 2025-10-05 05:16:00 | NPP-375D | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 206e60aa-e7df-334b-9f22-791205af964c | -14.68365 | -48.36112 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 09c2706d-eb13-3f07-ab13-fc64e101f809 | -10.83046 | -57.19751 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f98f1a20-5c27-3b76-b42e-f29ff8a9d089 | -15.42386 | -50.20899 | 2025-10-05 05:16:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 832d2c89-22ef-3a5f-a035-a7c2c0e9b82f | -15.7776 | -49.08995 | 2025-10-05 05:16:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b532f133-ed76-3496-8d7f-c0c9a867e288 | -13.13741 | -50.88947 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 4b84d49a-7ffb-38d6-bf29-e107bbbd1b25 | -17.97816 | -51.14137 | 2025-10-05 05:16:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ecbe596-b8af-3f8d-9d82-7409de8b4955 | -15.21269 | -46.38628 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf83a99b-f2b4-3e0d-a174-9e15fd5c1e6a | -12.46024 | -45.51815 | 2025-10-05 05:16:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be852c38-3d8a-316c-a718-e3c913cde030 | -14.74373 | -54.65234 | 2025-10-05 05:16:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8406ee19-3804-3d94-86e1-7b775c2470a2 | -15.30243 | -46.31939 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48474816-f2b8-38bb-9407-e47d23c58943 | -18.24898 | -53.35699 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6a14655-1c0a-3d46-b838-8fe65f8d92b2 | -19.01385 | -50.60752 | 2025-10-05 05:16:00 | NPP-375D | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 12.0 |
| 309cffd4-8ed8-37c6-b96f-fd36074119b9 | -12.9459 | -54.73108 | 2025-10-05 05:16:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 566c5dcd-1fdb-3997-96f0-b93413a3d7c8 | -13.35582 | -47.58863 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d12db8a-f2da-3322-8936-6c813de61ae0 | -13.26596 | -47.62039 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4b6f44ce-20f7-3160-90b1-72a0c3a5d368 | -13.35626 | -47.58472 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2a491f30-9878-34ac-8a5a-c1680b0facf5 | -18.14485 | -53.34895 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14038359-8b3a-3fbc-8b53-c397e1fe676c | -12.8976 | -47.32198 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9934be53-ed3b-30d6-8914-24047ab37994 | -15.24889 | -56.76302 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b98d8a11-0e72-324d-a1c8-a0fcd17cbe1e | -18.25636 | -53.33458 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2bdd40cf-955d-3c76-97df-ae308baea4b9 | -15.14264 | -45.75461 | 2025-10-05 05:16:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fd290143-55f4-3d24-8363-1301779d17e4 | -17.88799 | -57.6421 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 67bcb11a-82e2-3738-bbca-813b5edbad24 | -18.24843 | -53.36138 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e2d64e64-e243-3f60-83e8-9f4931c9d6ac | -12.30956 | -55.15059 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8efc0b0c-0a21-38ad-90a0-27b79f78b98c | -13.43538 | -47.27765 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| df40fb55-ced4-31e9-8282-d71e52480cdf | -13.30324 | -47.78008 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e29ed255-397a-31d8-924e-71055d3989c5 | -15.35552 | -47.98205 | 2025-10-05 05:16:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44619cfb-b417-3d0e-b596-f2aaab0cd293 | -15.22237 | -56.79637 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f6ce875-9538-364e-acaf-7eea98a30ca8 | -12.30844 | -55.13228 | 2025-10-05 05:16:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebaef59f-2d7f-34b3-9f18-ab79716a91b3 | -13.29068 | -47.62215 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b545f512-b442-3040-b1d1-04d7fdd6d4ad | -12.61302 | -48.12239 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 588aaeed-bb03-324c-9948-940c4db9a5a3 | -17.88506 | -57.63759 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 4014be50-5cd1-342f-b19e-31e7ee46595c | -18.17483 | -53.36553 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 913e2bc7-7365-3ddc-aa1c-f836d5cfcb3e | -14.98881 | -49.97959 | 2025-10-05 05:16:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58e7849f-1653-3c0c-9c91-47b4a919f275 | -14.33502 | -47.69764 | 2025-10-05 05:16:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b550df6d-8166-3486-a3c0-e42a6b32b3c4 | -15.58292 | -52.48635 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d2a8b2a7-8fe8-3df8-9377-39fd52626915 | -11.50173 | -54.45783 | 2025-10-05 05:16:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5383b5b8-3266-30d7-83d3-822fdcff344b | -15.21767 | -56.80392 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed914bf9-357d-32a4-948f-3095aefd092f | -18.20141 | -53.37214 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a7c8df4-eac6-3ce2-930f-e589986d639c | -14.69379 | -48.35868 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 62dd8d9e-a580-3461-a887-8651563ad236 | -13.13889 | -50.87817 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.3 |
| a2daff83-8fca-3710-acca-408ffffbbb29 | -10.83438 | -57.17215 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9343647f-542f-3981-a09c-c9cf94044925 | -16.05573 | -50.92841 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 738cfceb-6998-3e3c-a72d-daeabcc33fbf | -16.07093 | -51.08452 | 2025-10-05 05:16:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efa8cef3-e69b-3470-b171-dfe01e7e4a58 | -17.95935 | -57.57323 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b5ebc2ae-9750-3240-89fc-cc4fd1fb7e49 | -12.41445 | -51.10219 | 2025-10-05 05:16:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 65fe63e6-c564-30f9-8382-5d31feb0ca16 | -15.25537 | -56.76837 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| beeb7d8c-7fc3-3428-87cf-bf31fc290676 | -13.36262 | -48.06086 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 480d5c8a-aa50-32b5-b97c-be74adab0efe | -13.09818 | -47.83717 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8272cf4-9f4e-3573-aecd-740541f62b7d | -12.97153 | -50.99562 | 2025-10-05 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 809a3bd2-5094-3037-b5d8-5a842c1c5551 | -13.32166 | -47.78088 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24d1027f-f85b-3326-a3e8-12f0e526c9b3 | -14.69466 | -48.3511 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92711257-7943-30c1-bcf0-43b55b7a7473 | -17.89912 | -57.6425 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| dee47e17-b42a-3aaa-a33d-471621ee676a | -15.60005 | -52.45737 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c97eb8-0c2f-3e62-9b13-5399509fef08 | -18.2534 | -53.33587 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2372cb7b-7d7a-30f0-bd39-36da7feae689 | -10.83101 | -57.17163 | 2025-10-05 05:16:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccc3d718-0432-3ccb-8cda-3abfa4e0857a | -18.25672 | -53.36808 | 2025-10-05 05:16:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5d379d12-6461-3056-9d2e-412ed0249fcb | -12.40962 | -51.10154 | 2025-10-05 05:16:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6df1fc83-6f8b-3378-9525-4dcd04123394 | -10.03056 | -62.4633 | 2025-10-05 05:16:00 | NPP-375D | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e43c2418-7aa8-3ab0-a315-d5a444984e00 | -16.94471 | -52.68056 | 2025-10-05 05:16:00 | NPP-375D | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 622a30e9-e136-32ff-bf93-7b9decddea6a | -14.68132 | -48.36197 | 2025-10-05 05:16:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 66d4b2a8-15b3-3c15-baff-3b9b2b98e00c | -13.09926 | -47.82766 | 2025-10-05 05:16:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e06ba31c-63a4-3a7f-80ee-9129d206dafe | -18.20085 | -53.37672 | 2025-10-05 05:16:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ba571c05-b7ad-3bcf-86cb-fd7a158695d7 | -15.3092 | -56.9404 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c24e70a4-fb19-3212-b2f7-ef85f74f2359 | -11.76282 | -64.92595 | 2025-10-05 05:16:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e62876b1-53a4-3688-b2ad-8320979596ee | -17.94588 | -57.59184 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| fc7202a7-9b3d-341b-b458-20c20f476cca | -12.92196 | -47.30771 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e03b99cd-9f57-31b5-a9a9-97f7ae89750f | -13.26096 | -47.6096 | 2025-10-05 05:16:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| b2194760-2ea6-3088-ba55-33f469af65ea | -17.96106 | -57.56142 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 8a7f376b-c16f-31b8-b8e0-272613538805 | -15.21294 | -56.81171 | 2025-10-05 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5f76e76-64b9-377d-9646-ddeab274a710 | -17.92595 | -57.6055 | 2025-10-05 05:16:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e7e2a483-92f2-3a2f-8a0c-5abee9456aea | -15.59916 | -52.50286 | 2025-10-05 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da232ccc-aa84-31ff-811d-9a5d4c0d8adf | -12.82026 | -46.85257 | 2025-10-05 05:16:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b24ac32e-186f-39f2-9d33-14717deae6e7 | -11.83113 | -60.48392 | 2025-10-05 05:16:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 486c599d-794c-34c6-8642-2b21e231c832 | -11.87034 | -56.87304 | 2025-10-05 05:16:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5cc0c785-1887-3426-b6cb-9c1964332c7d | -15.97784 | -50.90667 | 2025-10-05 05:16:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README133.md)
