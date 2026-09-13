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
| f9999d67-f225-3082-9839-8f3d13ed1be9 | -2.90187 | -51.93478 | 2026-09-13 05:10:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa4af4bb-b138-3392-b2ae-eced883cf99c | -13.61532 | -47.88798 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e9c5258-05f2-3bb7-b7f9-eaf28675d295 | -13.45045 | -48.4915 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4074eb36-49f4-30b2-bb1d-d500fbbcc0ef | -13.78541 | -48.80254 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 685dd9fc-7918-3099-a634-8bf5a14baf54 | -13.61493 | -47.89114 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88bdc057-d3c5-306f-9f52-da2d13d5b88a | -10.35668 | -46.66933 | 2026-09-13 05:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8bba2d21-f741-3935-9dd7-dfaf714b9e29 | -10.96071 | -58.95825 | 2026-09-13 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fae1ff00-2bf2-35ea-8eac-652e8ef5fa30 | -13.46013 | -48.49356 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 605acf84-f82c-34e4-b37d-1ad8c120b807 | -13.61633 | -47.88177 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 41c27e5d-8cf6-31e8-91fc-3fe6b102534b | -8.81996 | -61.40605 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca0a245c-3ff2-35bd-b84f-769a25776358 | -10.69003 | -54.16298 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fe128d97-4386-38ef-a054-ba6b5565ea97 | -13.61524 | -47.89123 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| faf7bed2-a4ae-3d65-aa49-a44466a28ba7 | -9.58123 | -55.151 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ced97e16-e709-32ca-adb6-7279fe287094 | -13.61648 | -47.87844 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 583654fb-cf7e-3c8b-b45b-bfa13f096d73 | -9.70638 | -54.35795 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eeadc567-afe7-31ea-95ec-e3b69b44f1b5 | -10.56639 | -51.34691 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a93c69e0-1fba-32eb-885b-52b3533f03d3 | -10.57415 | -51.35226 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d44ccce4-b6c0-392d-baba-ec810ffde5a6 | -9.70986 | -54.35851 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0dcb284b-675f-39cd-8f88-108dc79a4d25 | -10.94726 | -57.18204 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ff6dad6-564d-3dc9-a0ea-cd59e554774c | -10.48275 | -48.64009 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9106693a-f815-342c-986c-8ab2ace40ef4 | -13.34579 | -51.7844 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af040b02-5416-3665-b7d0-3a96b5dd4ada | -10.72813 | -54.00558 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2dacb998-07b4-32df-8778-33c98e08cba4 | -10.62943 | -46.10648 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 62a8e312-a70f-30f7-9bcc-2306bce3b4af | -8.81598 | -61.40539 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36c6347a-e7ce-3c27-a4fb-d3e63e3baa4d | -10.52091 | -47.90027 | 2026-09-13 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc8adde1-68fd-3c5f-8307-04ab88455364 | -13.40277 | -57.02779 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d02ab287-6f06-3f25-9d90-66e8552641a5 | -10.63596 | -46.1026 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 931d0e1f-bbb7-3112-90ba-d11ce5ff8fd4 | -9.33493 | -60.29085 | 2026-09-13 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c824f746-ec48-313b-a8f5-ed65800ad638 | -15.05161 | -48.54114 | 2026-09-13 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ead0681c-030c-37c3-9d5e-cd5b5b0f21e9 | -13.38856 | -48.01272 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9154a336-3222-3d94-9705-f474f1388183 | -10.25619 | -57.70101 | 2026-09-13 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 99eaee7f-b64f-3413-be0f-869e894f9b43 | -10.68762 | -54.17912 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d9728bdf-9005-327b-a202-238204812827 | -12.15742 | -48.96603 | 2026-09-13 05:12:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8cff48cb-0208-3f40-938f-3b28eebad75e | -13.40221 | -57.03135 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b72a8653-05a5-35b9-8116-88ba5c5afe64 | -10.5055 | -53.57067 | 2026-09-13 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b18c6d23-b814-311b-a01c-f55e42feac3b | -13.45566 | -48.48602 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66b60188-0ac8-3b0c-8f44-b9b4fe80420e | -9.87799 | -47.5876 | 2026-09-13 05:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43d4a68a-238b-3c9a-ac71-47b5629fd967 | -13.44887 | -48.50402 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 180268d1-7e67-3b75-bf8e-a3b1ad06b945 | -10.94244 | -48.35613 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54419ebf-4d71-391d-841b-36b4c1a0870a | -13.45002 | -48.49492 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 005ea304-8f1b-3d7c-8399-bd46bec1481e | -12.85443 | -44.39623 | 2026-09-13 05:12:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ab48bd2-aa64-34d8-85d6-5d06fcdda75c | -13.62135 | -47.88439 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d6d9e97-de80-37f3-86bc-9356c05b670a | -9.71045 | -54.3546 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 349f70f2-c0df-368e-a486-eb105962b182 | -13.78579 | -48.79942 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 664e756d-2b67-3c3a-988f-a4caea14b466 | -9.17396 | -59.42361 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ce10fd1-3944-30de-8c05-8581a1f57a02 | -9.71564 | -54.36731 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76dde560-467a-3a47-85d3-005371e8317e | -13.6156 | -47.88805 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d4a9a987-30b7-3e4b-bd2b-8841c9c0e4f4 | -11.82078 | -46.38106 | 2026-09-13 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 05dbfc82-12c5-36e6-ab32-94c9d2a1d2c9 | -13.45605 | -48.48279 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| cb7e34a3-0ba7-326f-8ebb-421ebc7ba791 | -13.34733 | -51.80261 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2069f473-6b84-3426-9868-c81a7faeeb01 | -13.34789 | -51.79856 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 345ad4e5-161f-35b4-87a7-eb56a1c801a1 | -9.69769 | -54.34472 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b023b6c2-e364-3728-a6d1-ae614b20d04d | -10.2523 | -57.70398 | 2026-09-13 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8d20853-5510-32cd-9488-1e3c1c488508 | -10.51281 | -57.45669 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 555776a5-9fe6-3b9a-afd2-45f16539f4d4 | -11.81858 | -46.39957 | 2026-09-13 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03bfe0b2-d7b5-331e-b3c2-ff0783ef1338 | -8.76951 | -61.40013 | 2026-09-13 05:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ba313da4-778d-3190-91b7-4f5fa80b071b | -9.70176 | -54.34142 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57f17b0d-a543-3063-afce-a4686ecc3c6e | -10.46816 | -48.63452 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d29fd521-943c-32bb-8583-4664618db31b | -10.69237 | -54.17158 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 249db267-34a9-3186-935b-305c2ebeca45 | -11.28046 | -53.933 | 2026-09-13 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aac388b8-8097-38c1-81f7-1d958bfbe69b | -9.38888 | -57.30267 | 2026-09-13 05:12:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5f4906ac-6ea4-3f34-b11e-45d316882cb6 | -10.93579 | -47.91325 | 2026-09-13 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0d836dd-a4bd-338d-8b77-3f3212d76efe | -11.81807 | -46.4038 | 2026-09-13 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a011461f-19e3-354f-b9af-e80b37c95b5d | -10.58095 | -51.36431 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5c3d09c5-c45b-38c2-bff5-67244661ae67 | -10.6422 | -46.00515 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 640aba07-0329-3f95-8190-4ccda1e54842 | -9.71452 | -54.35128 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ec632ad-bc70-3a8e-96c6-6d59ecd1748b | -12.1339 | -57.19538 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9ecad46-d8f0-3491-a1f1-163ac9ec8cae | -10.68709 | -54.15839 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 94d6a2a9-8f19-3e4c-a98e-aea2b6884929 | -13.98479 | -54.07034 | 2026-09-13 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6aed5d1e-038f-3c73-8ea1-64f550745684 | -14.10255 | -46.35926 | 2026-09-13 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d86b6e5-88cc-350a-8871-6349b7d3b295 | -9.58294 | -55.16236 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27dc26cb-cd9c-3cb1-91b4-366dca6ae100 | -13.45484 | -48.49294 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b42d21e8-7172-313e-be10-bc6ee62b65d3 | -14.10304 | -46.35466 | 2026-09-13 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8e58652-b7f5-3c4f-b41b-3201bca23bed | -10.95668 | -58.96142 | 2026-09-13 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f4c7025-6a6c-372d-90ba-a48a57d4b242 | -13.48743 | -48.48954 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9b815dc7-937a-34ed-bc32-b2564905b04d | -7.45268 | -63.80209 | 2026-09-13 05:12:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5d1f5a7-298f-3e7d-a52b-f4dda674f5a4 | -11.62269 | -49.8197 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9f799e49-b721-310f-8bb7-3862349ad82c | -10.51613 | -57.45724 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4dd7e4a-5c60-39f0-a92b-79883a1b120c | -9.24255 | -60.3966 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 454883fe-f72a-3943-aff8-c06b76334738 | -13.31499 | -51.72464 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebb6b930-3d14-3f06-aaa7-c0f87077138e | -11.57533 | -46.99041 | 2026-09-13 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 673c9f61-b7c3-3836-b007-25df969ef8a6 | -10.95057 | -57.18258 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f92feaab-c6f8-3700-b0c9-c03b76e19509 | -10.5304 | -51.36078 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5d48ea1-00a3-3c75-b7cc-c98340017b63 | -10.46776 | -48.63751 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23a1f52c-e393-3d8d-9e1b-c73c385573ab | -10.25173 | -57.70753 | 2026-09-13 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a11016f0-98e2-3c04-a2e9-b5159c061b39 | -13.61053 | -47.88139 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ccfc3438-5e49-37b7-a112-0c2931f067cc | -9.38945 | -57.29915 | 2026-09-13 05:12:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9ffe6c8f-bcb4-3c51-a3ee-b73b5cce6c63 | -9.5835 | -55.15873 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83b6a758-3000-3638-ae41-4b1c549fcf66 | -11.04727 | -47.17212 | 2026-09-13 05:12:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adf70b42-09b3-35e3-a130-687b26c18c27 | -10.25563 | -57.70454 | 2026-09-13 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 36e0b4ef-f726-3318-83fa-1c3425feb1e7 | -12.15674 | -48.9713 | 2026-09-13 05:12:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d6a924c-8d66-301b-a1ea-26182ea3ddba | -9.89355 | -47.5933 | 2026-09-13 05:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 94421a95-3a24-3c89-9c34-93a16d4e0a13 | -13.34534 | -51.78596 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0c179c85-1cf6-3668-9fc6-fbeaab5a5d95 | -10.25506 | -57.70807 | 2026-09-13 05:12:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5762efba-b1e5-3bbe-abb1-a70d7f970a77 | -13.34645 | -51.77796 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35cc3ae5-96c7-3962-bbaf-7273915361d5 | -13.34685 | -51.77638 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| daca7c8a-96f0-39dc-a2ac-08e04ee99dbf | -13.31131 | -51.71992 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ee6a032d-5eb1-367c-9875-f7b8a12535df | -13.62171 | -47.88148 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc993c32-1ef3-3d57-93cd-071a36a56356 | -8.82116 | -61.40928 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a32ee21f-c953-3b07-89d5-3de2af5a8467 | -14.95668 | -47.52875 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README52.md)
