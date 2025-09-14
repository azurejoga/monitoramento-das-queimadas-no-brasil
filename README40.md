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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80b293b2-70a7-3098-b140-26fcb3bb5fc8 | -11.45241 | -50.77597 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd295b7d-97e5-3984-b06e-bab72099f72d | -12.12315 | -44.83599 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2dc90d28-e52a-3672-b20f-10d319bf2b8e | -13.01593 | -47.98616 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3044ccde-4d83-3972-b06a-c24b4d312579 | -6.82765 | -47.87135 | 2025-09-14 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 372a4d09-2889-39e0-9b7b-903308a73ed8 | -11.30124 | -50.82645 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c25d7f71-26df-3510-9a0a-7f7aa8cc7c90 | -11.47166 | -50.76113 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| acf1ad09-c482-368a-9fc2-478f6d59e3b2 | -8.11403 | -50.17054 | 2025-09-14 04:40:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aff9707a-d869-353c-8f86-323aeceda44e | -11.47497 | -50.78318 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 03eb826b-3847-3441-b860-f02c3a1b7ed3 | -5.77017 | -52.35872 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2aa97227-9986-3758-a72c-7a572c48e1d8 | -6.67919 | -45.51615 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 82b96b53-f4af-37a1-a62c-c22527fbb5ff | -11.78375 | -46.62899 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 050911b6-d999-37cb-96d3-f0e8bbf39179 | -11.84034 | -50.49034 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a91ce6d0-6b76-341b-abb3-3cebd131e59d | -10.89579 | -45.55894 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9424e3ca-d5d0-3efb-a2c7-6177348769ca | -6.68233 | -45.51867 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58d8e397-f0b9-3df4-8a0e-958140b669b7 | -11.87304 | -46.76289 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5f08fa3-819c-3dd9-a8fb-b1e18815bde2 | -12.788 | -48.01159 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf84ac72-4a6d-335e-9409-564dd023a8d1 | -9.82122 | -47.17729 | 2025-09-14 04:40:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04303d3a-4332-3c28-918e-0bb2a916a1c5 | -11.44911 | -50.77544 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2f5021d-cf2c-3dd9-a65d-25c33d5c6308 | -9.01767 | -47.03941 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee7bf8c4-8192-350b-b74a-7179b5429b1b | -11.44745 | -50.76442 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 541a5a6a-ac11-3ae2-8b50-5e6e8712a957 | -11.46726 | -50.7676 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| add25b4d-c6f7-300d-b5e8-ae691f2c9681 | -10.34536 | -50.50032 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6eb6240-1ce7-37fc-a967-9c8c3453257e | -7.3983 | -49.98207 | 2025-09-14 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8393e9da-c557-3140-932d-fe3111febf7f | -10.93581 | -47.35144 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76f9b9c6-04d3-3bfd-b593-90015bcdf32a | -11.50414 | -50.79145 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 232d658d-888c-3a50-99ff-539e549441a0 | -12.24831 | -46.78833 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 04d0e74f-acb7-3588-8545-dd75e389721f | -12.08942 | -44.7266 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6ebc584-5896-3412-bfc8-b02d842cdbf2 | -11.4992 | -50.80141 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3074d700-5cfb-3fc5-a1e6-c85c9e89d40e | -11.77744 | -46.61869 | 2025-09-14 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cce0068-7d31-3b1f-8e6e-2ac284225db1 | -11.38998 | -47.33982 | 2025-09-14 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0c1cce2a-9bd8-35e9-a5e3-1a3afc31767d | -9.05807 | -47.02704 | 2025-09-14 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49784d6d-9401-3f7f-bee5-b0a005b4fccf | -8.95357 | -44.43893 | 2025-09-14 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b261ce4f-b4a4-338c-96f9-3447b5a0c8c1 | -6.4609 | -51.02937 | 2025-09-14 04:40:00 | NOAA-21 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4461bd0e-f1d9-37d0-8d3f-746c627d7c7f | -11.71726 | -46.9075 | 2025-09-14 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a62b913-3651-35c0-b9c0-200bf952b140 | -10.35193 | -50.47995 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58cbd0a7-2316-38f2-839f-99ae605d8b2e | -8.08772 | -44.50788 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3715977f-4696-3ee1-9696-185dc77409fd | -7.38042 | -44.35726 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9233e545-0b50-3ac8-b628-02c5c64c301d | -8.76554 | -46.04345 | 2025-09-14 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 213259a6-e45e-378d-9d95-2740875476cf | -6.69683 | -45.52576 | 2025-09-14 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7e03f13-0193-3be9-91a6-ed07adcf7cb0 | -6.55894 | -43.95243 | 2025-09-14 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e72c2747-9435-3516-a536-531f1515e96c | -10.35247 | -50.47646 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6c9ac667-fa3d-3376-b847-3ddc52ab6f0b | -10.40949 | -48.60149 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 707147f0-50fc-3142-ba09-85d4b200ed8b | -11.4843 | -50.74523 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adc6e591-baa0-31fe-a570-bbeac1b85f92 | -12.76659 | -48.00816 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0e1111d-cab3-34a3-a340-02f0ef79009c | -11.44414 | -50.76389 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e2bfd3dc-e4c0-312b-b8ed-5e5133c2247d | -10.67728 | -46.25665 | 2025-09-14 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83d7f631-0542-34df-9857-f9202aaa2e2d | -10.77102 | -44.78376 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4d4f41d8-a74f-3bd4-a424-32df0e8f94d2 | -12.12473 | -44.82415 | 2025-09-14 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1968b2e1-54cd-3257-a62e-2024384593de | -11.45682 | -50.79102 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b3679416-600a-33f6-b752-26fc433d0916 | -10.39949 | -50.59099 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38c2b6a7-9b5c-3cdd-a41a-b6d1c4c73abf | -7.38236 | -44.35408 | 2025-09-14 04:40:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c0cab2f3-7505-3431-8ebb-0cfdeeabdf55 | -11.48486 | -50.76325 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 0cb9b8fa-fc70-3054-94ca-8ec13d04445b | -7.30924 | -43.93901 | 2025-09-14 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38ae3dca-7cd9-31de-8f6a-6c919a1abfc0 | -8.93605 | -48.6572 | 2025-09-14 04:40:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a1aafb3-e594-39f3-9c06-d7b10a1a8582 | -13.01293 | -47.98168 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 346a57d9-b8b9-3cb6-84d3-1b79c4c9f5f0 | -10.42882 | -48.61213 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a5aa31b-7f13-3d36-a10f-e76c1bff19ba | -12.79263 | -47.97984 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74aa8c93-d2a3-3468-8bf9-ed67d50e269b | -12.96897 | -48.03259 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22aa5e75-9ba6-356e-93a6-bec93317c8a6 | -11.46699 | -48.70198 | 2025-09-14 04:40:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| e89f0438-1fe1-32c4-8989-ad79168e6c46 | -11.49699 | -50.79388 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8f3fe82-1f1b-3a5c-bdd8-b7aee295d06a | -10.40224 | -50.595 | 2025-09-14 04:40:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86272479-040e-31fc-850f-89130c3112f0 | -11.45792 | -43.57097 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 330bb74c-7d5c-3a22-9cda-3f5f861514e1 | -7.61541 | -46.70837 | 2025-09-14 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4dc2b32e-36bf-3ea8-82c2-1117d0a351a1 | -7.31404 | -43.93579 | 2025-09-14 04:40:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e311527b-f5ee-346c-b7b4-a1f9fb6af491 | -7.43499 | -47.43027 | 2025-09-14 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0f99bc22-d81d-3c0f-9d56-e36a80787bbd | -12.81533 | -47.15011 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 992cf054-3c93-3d10-b6e5-2625eea09d2a | -7.6112 | -46.71199 | 2025-09-14 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3e2821c-b1d1-352d-a5cc-bc57d2c24804 | -10.90487 | -47.20719 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 31f6dd90-9b31-3b95-80c4-0844944b61a0 | -11.47935 | -50.7552 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 6987a211-1812-3bba-9757-5dbc88b1e716 | -12.80851 | -47.14439 | 2025-09-14 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6143231e-4113-327e-b674-28e13eacb155 | -10.90549 | -47.20287 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 284de5af-8f84-319f-bc04-5e0f27c4849b | -11.43643 | -50.74831 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba3f69c0-6e66-3587-9084-bbc0d0720457 | -10.9213 | -47.19651 | 2025-09-14 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b659d646-d3da-3fc6-b574-4ab0db368184 | -11.14357 | -45.32352 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 977289e2-2edd-36c0-be11-ec6435f78df3 | -6.61129 | -51.04183 | 2025-09-14 04:40:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d773dcdd-db90-3fda-badb-6972d1acd232 | -13.95183 | -44.85153 | 2025-09-14 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a52085bf-714f-3ce6-a11c-3b65f821d44c | -11.4411 | -50.47601 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 251f9ff3-a3c9-377e-bd97-4c0d076ddb62 | -5.76595 | -52.36218 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 101e87c8-bc8c-348c-99dd-0c1b07042e79 | -12.80238 | -47.96313 | 2025-09-14 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a57fe587-cbb8-39f5-aba3-8ce2b703ac25 | -11.48981 | -50.75329 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 1ed6925e-d009-338b-a673-cadc92ed05b9 | -11.48598 | -50.77777 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0a0307ea-ff1d-34c2-90e3-c3a728858ab0 | -11.47386 | -50.76866 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 97e248fa-3221-39f8-86a7-79769504e278 | -11.47275 | -50.75414 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 78bb69d5-58f4-35fb-9af5-1f15e882f20b | -11.86624 | -50.49808 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b06eb392-9ab7-3b04-bdcb-8ed183358c25 | -9.62914 | -40.61868 | 2025-09-14 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 9e01f76a-0245-3070-89e8-edcced66f94b | -10.92586 | -45.57847 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66492a2d-fffb-3d8e-a171-13ccdc2e0dc9 | -11.31105 | -50.83164 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ceb7ece8-85c0-3e7d-9694-27fde29bdc38 | -10.69999 | -48.6759 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47229827-0555-3dfb-850b-ec57332ca014 | -8.76585 | -46.04148 | 2025-09-14 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 75c7b0b3-bfed-323b-ad89-327852c2e234 | -10.7159 | -48.68604 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c7155da-fd9a-31a2-bcda-eb6e347d9c15 | -8.62095 | -40.19688 | 2025-09-14 04:40:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a3c956cf-0f4e-3340-96ca-39310350ae7f | -6.80648 | -51.37775 | 2025-09-14 04:40:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b2579e88-6d56-3332-bee6-e70e84b329be | -10.43222 | -48.61267 | 2025-09-14 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c705955b-4b76-3755-a520-99ddca783aaf | -8.09184 | -44.50854 | 2025-09-14 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9bf284c-91a5-3637-9de8-e314b5fb53aa | -11.35037 | -43.49953 | 2025-09-14 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02b968f3-824a-3747-851a-b26c5cd47ecf | -11.49203 | -50.78233 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a681b1b2-aa2f-3980-8e3b-da93b16267a0 | -10.90436 | -45.46559 | 2025-09-14 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a074417c-5fbb-3541-b016-dbfa509ffa77 | -12.1076 | -44.85438 | 2025-09-14 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b1471a2-8aac-36c4-9b9e-4dfede7fc636 | -11.49862 | -50.76188 | 2025-09-14 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 749823d9-bf59-31ac-9f26-5bd097671382 | -7.01976 | -46.00874 | 2025-09-14 04:40:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README41.md)
