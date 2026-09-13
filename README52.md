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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f71ecd50-36a9-37e1-817a-e52beabfa178 | -9.17696 | -59.62515 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4c3e4702-072b-3974-bbf5-bc2402fb3222 | -11.24702 | -54.15768 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd8d2bb0-1b03-3fc0-8d0e-39681b8f4d6c | -10.65806 | -58.77093 | 2026-09-13 05:12:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8a0be29-a1fd-3d1b-b8a6-5e9c2cce281b | -10.68407 | -54.17859 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5e80cbde-dbde-39a0-a610-c6b812ad2ca6 | -10.68233 | -54.16593 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| cd99850e-f38a-3f76-a51e-686aee5e0731 | -13.59833 | -47.88977 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5b11560-5b68-3eb0-85cb-08c734d08aad | -13.61609 | -47.88168 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e215e303-12dc-332a-ae83-9cb3adfd5b8c | -8.86633 | -62.52701 | 2026-09-13 05:12:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ba97e542-ab58-301a-9cab-9004fe903e9d | -13.61139 | -47.87432 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9431a6e8-4dd2-3372-9664-cb2d3e196f18 | -9.69652 | -54.35242 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f89c2a7d-188f-3f20-8a05-b68ebadd4ad4 | -10.75344 | -46.25164 | 2026-09-13 05:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11477296-62d9-3333-b509-4ea0c0a698a0 | -13.62194 | -47.88158 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 50e10c1e-51d8-396c-a634-b4aaaae82397 | -13.29563 | -51.64354 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71f4cecd-7f5a-35f2-9d49-41d23be0e7c9 | -13.45563 | -48.49294 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8fe7f42c-9f54-3189-b100-bf3b29797698 | -10.50137 | -53.57132 | 2026-09-13 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58b3922e-8b40-32f9-9b74-ad124a90d59d | -11.83092 | -46.39701 | 2026-09-13 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5fb344f-daf4-3a0e-ab24-224264769459 | -12.15708 | -48.96864 | 2026-09-13 05:12:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87726601-9887-3a38-9994-37238d1c3b82 | -8.7726 | -61.40605 | 2026-09-13 05:12:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 5114265e-e91b-3ba6-b0ef-257d88ad1070 | -10.96413 | -58.95884 | 2026-09-13 05:12:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0101fcc8-087d-3ea3-b967-db059d1a879e | -10.63906 | -46.10626 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a348f71-09f4-3952-8f69-c596c3edfdda | -15.04659 | -48.53733 | 2026-09-13 05:12:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f4026593-01f7-3b04-98fd-5f1eafe51fc6 | -10.47146 | -48.64834 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e514e6e4-66e8-3ebd-bafe-8e15f6898e49 | -9.58067 | -55.15461 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cdd3ad79-e7cd-3a35-ac47-38f2da9656df | -10.69177 | -54.17562 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4d006908-a180-314f-8304-5fdece7e8698 | -11.83035 | -46.40169 | 2026-09-13 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80a24939-9f13-3726-818d-5604267e2425 | -9.69711 | -54.34857 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 478d6fbc-c1ce-3071-a933-1a9297038b7f | -10.35618 | -46.67321 | 2026-09-13 05:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4e0729c-7af8-37a4-ba56-d5864a076c01 | -9.70867 | -54.3663 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea8e3390-37a0-3dbe-a4d7-3c582976d898 | -10.68822 | -54.17509 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2cb8ee0e-dd80-37b8-8cd5-086fcda6457c | -10.68882 | -54.17106 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 68d54bcd-2e8c-3419-b566-675a832489b8 | -10.35771 | -46.67705 | 2026-09-13 05:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05843b65-8247-39f4-a72d-dbba534b6fb0 | -13.39469 | -48.00759 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0cb4f00-dbee-327b-97f3-b32fc224ad62 | -9.89936 | -47.59052 | 2026-09-13 05:12:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 410c4e86-d5a3-32d0-ae07-5068c3c06089 | -10.90033 | -47.81042 | 2026-09-13 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7159dcb8-f980-3cfb-9b7e-bf22087da181 | -9.38138 | -56.98932 | 2026-09-13 05:12:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a12f40b-b44f-34f5-b4e1-97a116c5618a | -10.415 | -54.36025 | 2026-09-13 05:12:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8578be18-6abb-3d89-a4cb-56797f514371 | -10.68173 | -54.16997 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| bdc91f0b-52d7-36ec-a25b-708217c20305 | -10.69297 | -54.16755 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d8d37e79-5cd9-3dd3-9027-49c564e3d279 | -13.40609 | -57.02833 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44509b94-9a07-3b75-aa80-88fc09f1b65a | -13.38162 | -48.01191 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 898796a3-eb76-3430-b026-f786382da81f | -8.86277 | -62.52221 | 2026-09-13 05:12:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e4dede8-c761-3437-affc-1acbec88cdf8 | -13.45268 | -48.51112 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bdae77d6-5e27-3af4-a09d-64e43c204adc | -14.10253 | -46.35744 | 2026-09-13 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b2f5c87-565c-3ba1-bf08-96b1e368c55d | -13.31075 | -51.72404 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f153417d-a6dd-3143-9d0f-b857c72481d5 | -10.63565 | -46.00886 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2945d6fa-befe-3f46-a2d8-89a5fcd61137 | -9.24627 | -60.39723 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b10811ca-b948-3b5f-ae61-c674699403e3 | -10.68942 | -54.16702 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9f16c431-b69c-3bd7-934f-e05d448d05e0 | -9.70703 | -54.33023 | 2026-09-13 05:12:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f24d46f9-c479-3eed-b9b9-dc518cb27934 | -9.17041 | -59.42302 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5760ce03-6ef9-3bea-9a68-3c507d2c323c | -10.75398 | -46.24742 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3b774f9-b46f-3399-afa8-13b0c754292c | -11.25784 | -54.13411 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6b3bff8-7da6-30f2-8084-b4f27a429e2f | -9.59479 | -55.15299 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51f7fab0-3ecf-386f-acd9-aa7b4457f960 | -10.45529 | -48.65496 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 947dfd4d-1f34-31bd-9e99-a6431c981c2c | -13.46545 | -48.49389 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4eebe889-cbf1-32a1-8521-955a33ef731e | -9.18477 | -59.44614 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a957cb71-53b8-342d-8233-7808f0ecc369 | -10.68294 | -54.16188 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f4c4467d-a3d8-3784-90c6-9397f3478972 | -14.10865 | -46.36018 | 2026-09-13 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24462bcd-04f8-3d2f-8090-cc535c567b27 | -13.38712 | -48.01216 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe55993e-955e-3f4f-bea4-13e1b79e2dce | -10.94615 | -57.18904 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1667f6b9-9b1e-3b6e-b3aa-63892cd562fc | -13.45302 | -48.50824 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9a96f04-cc7b-3f50-ac75-95566f3dedc8 | -13.34158 | -51.78376 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3e045a0-a760-35c0-980a-a44e99c8e729 | -10.45608 | -48.64883 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15295db7-1892-3dd7-b5b4-194a00196d54 | -8.88486 | -62.57219 | 2026-09-13 05:12:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c90d74b1-2e8e-31c0-be3b-6e05a883281b | -13.31555 | -51.72051 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97193d72-0cf3-3b6d-9ccb-141fd583a0c1 | -10.58516 | -51.36466 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb62b4c7-bd33-3c1a-992f-07314cb16f36 | -13.38925 | -48.00684 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32d768f2-f81c-3cd1-b849-38dfb0ace04f | -10.5518 | -51.32944 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9b5428f4-3b90-3e19-88e1-c4fc265883bf | -10.68648 | -54.16244 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| acaae40c-9079-34bb-99c7-aeb3cfa2a5c4 | -10.62348 | -46.10573 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| a0df330c-ac04-3ad0-8666-eb8dc7d65df9 | -13.79148 | -48.79606 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bce3ab1b-49bd-30a0-bcf2-814988d8c214 | -8.88557 | -62.56813 | 2026-09-13 05:12:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1bc03426-78d9-3d5a-bf4e-8b7ff9514692 | -13.45334 | -48.51109 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2edf3577-b0f2-3e7f-bc6a-d4c21772a659 | -13.34843 | -51.79701 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c04a8f2-e34e-35a7-be35-edc6fe146509 | -12.13059 | -57.19484 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f8a913dc-98d8-3361-96bc-04113725062e | -10.69358 | -54.16351 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29e67e7c-e142-3435-8813-ee4f55995ffd | -13.36804 | -51.71357 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea245d75-e3bb-3ae0-8433-7577c3c75cdd | -11.04329 | -57.21953 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ab784136-29a2-314d-9d4c-c04881fcbd84 | -13.30709 | -51.71925 | 2026-09-13 05:12:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d82d2325-ef9d-3e24-85d6-cdf004a3c2b7 | -10.56223 | -51.34616 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5e3456e-e38a-330a-a2df-4c30b64c80aa | -13.59878 | -47.88605 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99a55f1a-0b3a-33f0-bc65-759cee1078ca | -10.47275 | -48.63846 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a711850-0a60-3fa0-b210-0397c88ac336 | -10.94339 | -57.18501 | 2026-09-13 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05da9329-4fd4-3eec-9b95-d7c555640818 | -13.40166 | -57.03491 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ea4cf6b5-2ad3-35c5-9615-b1b48269be7f | -10.56582 | -51.3509 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3de5c6a2-60d0-3bdc-abe2-e6a8e67c9f08 | -10.48774 | -48.64097 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f435821-ccde-3249-a43c-28e65b0009cc | -11.56964 | -46.98975 | 2026-09-13 05:12:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1b8a76df-0122-31ed-85ce-c25dbd6d02c4 | -9.5914 | -55.15248 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3af71c9e-ca36-3c35-adea-0e1a3bad9096 | -14.10862 | -46.35835 | 2026-09-13 05:12:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c49613f0-472f-38bb-bf64-df33f81101de | -14.95803 | -47.53061 | 2026-09-13 05:12:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 84ea5755-bd16-325c-9459-720f453172bb | -10.55601 | -51.32982 | 2026-09-13 05:12:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ee86bfb-74bc-3808-aa74-fbc4a4d453d4 | -11.82446 | -46.40068 | 2026-09-13 05:12:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4dbc9f51-476e-391e-9704-009883492bb9 | -10.89549 | -47.80576 | 2026-09-13 05:12:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c00f5ea-10ff-327f-a4a7-ddea5e3d8f39 | -13.45526 | -48.48942 | 2026-09-13 05:12:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 15efa434-361d-3705-8834-d4cdebf5196f | -8.81907 | -61.4112 | 2026-09-13 05:12:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9c30eb1-3b6e-3a7e-b754-5a4fa700ccda | -10.68527 | -54.17052 | 2026-09-13 05:12:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ec16d364-ce52-3e6d-a1f6-fc87583e294c | -10.94281 | -48.3533 | 2026-09-13 05:12:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fba96d54-5be8-3c73-9725-a0501c34539d | -13.60896 | -47.89428 | 2026-09-13 05:12:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6dc49722-30a4-3cd6-8c17-79ced231eda2 | -12.13446 | -57.19186 | 2026-09-13 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf1e7348-dacd-3914-967a-b144da9a5a97 | -9.59196 | -55.14888 | 2026-09-13 05:12:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00a84d44-6228-3c1d-bcc5-1ebae85fc08d | -10.35818 | -46.67316 | 2026-09-13 05:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README53.md)
