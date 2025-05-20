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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d31fe8ac-704b-38a3-b08f-2fd57a55c4e6 | -6.23084 | -43.35917 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d6d3086e-9d70-312d-b889-e175c73f2672 | -6.22681 | -43.35259 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b83b979a-3fed-37fe-b85e-54afbd61c731 | -5.78353 | -43.6186 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1a67026-3b8d-3f04-801a-792ceaf43c3f | -6.31729 | -43.74403 | 2025-05-20 03:40:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bdb6573-6857-307a-9046-c3e769903206 | -5.57741 | -43.59281 | 2025-05-20 03:40:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4977158-1e3d-33d8-a3d3-97d3a68bbe33 | -6.22937 | -43.36779 | 2025-05-20 03:40:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63d74239-c16a-37d6-a044-11e0a3c15d69 | -11.23275 | -49.49917 | 2025-05-20 03:42:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3aae8a6c-d806-386c-a016-637137fbbd05 | -9.04079 | -47.75986 | 2025-05-20 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3004c348-0e78-3bd8-9aa0-5a66027fe505 | -10.58577 | -46.97537 | 2025-05-20 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5519f4c2-a30b-3135-97b4-51b659d4890f | -9.43826 | -40.37587 | 2025-05-20 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| f4e0daad-a8f7-3117-a0d4-0153e9269b4d | -11.4172 | -44.70369 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| da08b946-eb28-36a5-bf3e-da5db0f32ba8 | -11.41164 | -44.70564 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1346ebe7-bb7b-3846-96d6-35a3e0a43969 | -8.74817 | -49.75729 | 2025-05-20 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd6d2e34-bcee-3776-a4eb-74aed84d9e8f | -13.02015 | -45.07389 | 2025-05-20 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4011418b-76bf-3d47-b5de-beabe3a72df9 | -11.5117 | -48.58323 | 2025-05-20 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 944604ef-59a8-3683-b7d8-c1243416c667 | -12.43353 | -43.72757 | 2025-05-20 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8392d419-b06c-3622-9050-49dbd506ba93 | -13.02596 | -45.07052 | 2025-05-20 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d0e409d6-a257-3273-b4ca-655de9b44bc5 | -12.27352 | -44.59574 | 2025-05-20 03:42:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07ebf8a0-27a9-321d-9d29-0271c7f74176 | -11.41664 | -44.7066 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0daa556b-8e88-3d67-8a1e-5d5136d8b147 | -12.83548 | -47.3998 | 2025-05-20 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec6c66a5-76b9-331a-980a-b8b7196aa918 | -11.51659 | -48.58581 | 2025-05-20 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04ac4717-2b26-3f78-a2ec-77c042818c5d | -11.41799 | -44.70292 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c31ec94c-75f4-34a8-901d-afbe2905661e | -10.35923 | -47.97897 | 2025-05-20 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c70471ac-fc64-33ae-a0ac-75d90339d0f7 | -12.4344 | -48.11038 | 2025-05-20 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3de9c36a-e945-3667-aba1-c3ea75f8c98e | -14.04644 | -45.51446 | 2025-05-20 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 424fc133-e68f-3b71-b269-e96148f54e38 | -12.42826 | -48.10931 | 2025-05-20 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 824e3c4d-42c9-36c0-89e4-e7d71978a4b2 | -9.59226 | -40.34418 | 2025-05-20 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5a98a2c5-0d5b-3e35-99a5-5daf3e5797e9 | -8.74736 | -49.74705 | 2025-05-20 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4c370f3-52e3-3998-be9c-d9c097918e82 | -11.41745 | -44.70584 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a6fc0b5-abd8-304e-b5e8-82450a3d9988 | -11.41298 | -44.70195 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7420f39-787b-322c-b17f-a636188d83a2 | -13.90278 | -43.80142 | 2025-05-20 03:42:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fb0a6d08-46a3-3d1f-8ffb-ee490a933b51 | -13.02706 | -45.06475 | 2025-05-20 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3807fae6-35df-3e7e-be36-b70a440e8a23 | -11.41609 | -44.70952 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e378dfb-d9e2-3662-a1c4-b89356a82ca3 | -10.58413 | -46.98381 | 2025-05-20 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac3178c9-fffc-3d92-9b67-49277e028ebf | -10.36026 | -47.97361 | 2025-05-20 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1606e3bd-bb61-3ab3-9d72-998749730fa5 | -10.60824 | -46.98544 | 2025-05-20 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c56ef8e7-acfb-375c-b74f-68dcbc1f33d9 | -13.03011 | -45.0759 | 2025-05-20 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5586249-e4c2-3fec-8407-2e8609278d92 | -11.41692 | -44.70877 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 793ea136-16d9-3e07-91c9-10b1ea545569 | -13.02513 | -45.07489 | 2025-05-20 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 660f19f6-b974-306b-aab1-72b9359f586e | -10.61415 | -46.98643 | 2025-05-20 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ff8bc99-208c-3a00-a135-acab07ea3890 | -13.3141 | -45.3741 | 2025-05-20 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cfc7ac67-0777-3207-8f3c-b66140ba1d5b | -10.36553 | -47.98008 | 2025-05-20 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| add217fb-ca4a-3929-88fb-b731209e3e97 | -8.74598 | -49.75419 | 2025-05-20 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| abdadc30-f756-349a-bf7f-aaa14445789f | -9.59268 | -40.34625 | 2025-05-20 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 22229968-5a44-3775-86be-70b2546e2aaf | -13.03094 | -45.07153 | 2025-05-20 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8cc2b28-1dd9-340d-8442-360e014f4c2c | -11.41219 | -44.70272 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72c8eca0-6d5e-3d39-827c-1ff7494961c4 | -10.58496 | -46.97953 | 2025-05-20 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62c15a03-1778-378d-9b35-ed09eb9fcd18 | -10.35668 | -47.9747 | 2025-05-20 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36064de7-c322-3469-a051-0ce3797b391b | -10.3997 | -47.04462 | 2025-05-20 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| fb4d5757-c7d0-3da1-bebc-a728c0946484 | -12.43442 | -43.72269 | 2025-05-20 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f97deaa7-c353-315d-a718-a28b7bd25d22 | -12.42893 | -43.72663 | 2025-05-20 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0cca95b9-e570-3f62-9a35-f9d094722bfa | -13.31971 | -45.37222 | 2025-05-20 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 83f89d4b-feea-3559-ac98-37c27afd22da | -10.5455 | -42.43092 | 2025-05-20 03:42:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ae5e52af-a7f3-3452-93d9-dfb4bfe07cad | -13.02457 | -45.07782 | 2025-05-20 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32d4f0d6-c113-3217-8144-c93356e40fcc | -11.5177 | -48.58025 | 2025-05-20 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75270ddb-69de-38c2-9927-f29c0c16f457 | -10.60321 | -46.97989 | 2025-05-20 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ba8c9b5e-6396-36e7-a64b-3db222284142 | -12.83468 | -47.39997 | 2025-05-20 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4d9d51c-2f8c-357d-b833-17e2df966762 | -11.30337 | -37.77738 | 2025-05-20 03:42:00 | NOAA-20 | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3edef435-0257-32e3-b928-ea9e4961f9af | -13.31581 | -45.36514 | 2025-05-20 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ec8bc1ed-36d7-3de0-90db-a46aae4f26e0 | -9.59353 | -40.34135 | 2025-05-20 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d4720cbd-fd9b-34df-916f-14e8b12d6cb8 | -11.41352 | -44.69902 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a477ee7-92a8-359c-a945-b18faee5a14e | -11.61034 | -43.12056 | 2025-05-20 03:42:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e779bae-1325-358a-9f6e-aff2af9cfcb8 | -11.41852 | -44.7 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0773a4a3-a120-30c2-a459-cd4f35bfd15f | -8.74247 | -49.74872 | 2025-05-20 03:42:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c9c6a9a-b564-3da4-ad77-a9a1b3b98392 | -11.41275 | -44.69982 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3cbb665e-b224-381f-8f8d-6b4114c169e2 | -12.98347 | -46.32407 | 2025-05-20 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccbc737d-ad2d-38c1-9d11-69b95a89628a | -12.86038 | -38.36518 | 2025-05-20 03:42:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 200e1ba6-ffe1-3399-9b86-ff0b0676146f | -13.31524 | -45.36813 | 2025-05-20 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18df2d23-f727-32f9-aa7a-227b3ae347fa | -10.59822 | -46.97414 | 2025-05-20 03:42:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a452c6ed-2220-30e9-a873-420b7a7d0ffb | -11.41245 | -44.70487 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 90ed6793-cbef-3562-aaae-6e79305ac466 | -13.31467 | -45.3711 | 2025-05-20 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42c30cbe-1bba-38ac-9b2e-a3ad22b6e135 | -10.39888 | -47.04893 | 2025-05-20 03:42:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 98fb52e7-8859-3f10-bcbf-a397c401931a | -13.15083 | -44.93038 | 2025-05-20 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09cce759-912f-3be8-b7ff-e69c4476ad28 | -12.98418 | -46.32049 | 2025-05-20 03:42:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a08ba2c-4d8d-38af-8335-b73013f19229 | -11.23538 | -49.49544 | 2025-05-20 03:42:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f688c4ec-8da5-341d-91c2-82449857e2dc | -11.23402 | -49.49288 | 2025-05-20 03:42:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ae5d911-32aa-326c-a36a-c66c4bf202cf | -12.06474 | -47.32219 | 2025-05-20 03:42:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 723b8c58-f89b-3bc5-a5fa-978a16dd25f8 | -14.04587 | -45.51741 | 2025-05-20 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86da48a9-4d6e-3c25-9eaf-9c3dbc255931 | -12.27838 | -44.59685 | 2025-05-20 03:42:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd6675d1-58c9-3702-b379-6779c7bf1b78 | -10.36301 | -47.97563 | 2025-05-20 03:42:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 65057291-25f8-3286-8ef3-16109059eceb | -11.79584 | -44.27451 | 2025-05-20 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 79465efb-fc7d-35d4-9ff5-48bd0ca91858 | -12.0706 | -47.32335 | 2025-05-20 03:42:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 985448c3-a604-3160-a117-b828e1a6c7f3 | -9.43436 | -40.37519 | 2025-05-20 03:42:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| d0b6a0a7-30e9-323a-8c0f-7c9038632d36 | -11.87472 | -37.87092 | 2025-05-20 03:42:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 97ded9dc-eb66-3cd5-8d45-6b79e4db63c8 | -13.31857 | -45.3782 | 2025-05-20 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84c90f54-73ca-3b80-be54-0b896e85ee8a | -9.0398 | -47.76503 | 2025-05-20 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2996c358-4cf4-3172-986d-05ad862b1c49 | -11.41775 | -44.70078 | 2025-05-20 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1e39d2e-76a4-3e46-a44e-2e98a1fb7515 | -9.03447 | -47.75858 | 2025-05-20 03:42:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c3e5226-f54d-3686-8158-8f9fab4ce766 | -11.791 | -44.27361 | 2025-05-20 03:42:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34c7a00c-ada6-3703-ab67-a3ef0ef4e84d | -13.31914 | -45.37521 | 2025-05-20 03:42:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48514f2e-52b8-3718-9d30-02af004eabe9 | -12.83466 | -47.40395 | 2025-05-20 03:42:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb059fef-dc14-3bfa-ba0d-0a2f635fce8d | -14.05087 | -45.51858 | 2025-05-20 03:42:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d5bfd8f1-89ee-3d2d-9b27-52994f51ebd5 | -11.51022 | -48.58447 | 2025-05-20 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e63a8d1d-c75d-3b98-9805-3d6ad55c58bf | -11.51807 | -48.58454 | 2025-05-20 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b51d7c20-b820-3bc8-997c-4cf05f5fab1a | -21.19515 | -48.49048 | 2025-05-20 03:45:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf3cbc27-56fa-3b03-965b-5f3f43ead1c3 | -21.21306 | -48.61203 | 2025-05-20 03:45:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| a1119077-586f-399a-a4fa-caaa56d65358 | -15.20862 | -43.82228 | 2025-05-20 03:45:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 57793c21-be4b-39e7-989c-4bcc3492c016 | -15.27796 | -43.07572 | 2025-05-20 03:45:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 1edf233c-b4ac-3fef-8694-78c95a570e42 | -19.45453 | -45.30957 | 2025-05-20 03:45:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29bc089f-05ee-3925-b2dd-7678fae0b3db | -15.88867 | -46.0073 | 2025-05-20 03:45:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README5.md)
