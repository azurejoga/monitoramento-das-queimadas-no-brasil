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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6999415e-084d-3ddc-940e-471eff4f2fbc | -10.53681 | -47.72709 | 2026-06-21 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af52a588-27e9-3eb4-9a3e-06753960d549 | -10.11655 | -51.65985 | 2026-06-21 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74bef7ab-aeac-3b51-ba87-ecc0e41a411c | -11.05951 | -52.46666 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc2b3ee9-7cce-3d55-b6a2-2d80b4aeac33 | -9.18324 | -58.05459 | 2026-06-21 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 423d709c-2d10-31a2-a969-c653b319021f | -11.10787 | -54.14567 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 0083fefc-13fc-3ed3-aaaf-11bef8d219ae | -10.58291 | -44.32961 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 712ddf40-b852-329a-90bc-8488fdd3e211 | -12.42102 | -54.18769 | 2026-06-21 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cef25df4-565c-3f72-829e-4cb231105290 | -8.35142 | -50.5008 | 2026-06-21 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7deb236-5677-30d5-a678-d50c32eeb3f5 | -10.54274 | -47.71144 | 2026-06-21 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba86ac47-6e64-3037-8a40-64b5a726d91b | -12.51332 | -48.30724 | 2026-06-21 04:44:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a44a5bd-b7f7-3ff6-aa0c-bedc9323c363 | -13.5277 | -52.16872 | 2026-06-21 04:44:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48a387ab-348b-3cd6-bbf6-9fc26c9fc1ff | -10.5835 | -44.32547 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 82120c2a-dcef-3f2c-946f-f27daefca617 | -10.25329 | -47.34525 | 2026-06-21 04:44:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dfdccea-f517-31bf-8207-cd66dd3d104a | -9.18713 | -58.06085 | 2026-06-21 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c2286cb-ffd7-3d29-9019-c28478213259 | -10.71956 | -50.15685 | 2026-06-21 04:44:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30ce3d00-1e6d-3240-88c4-049569ff6c3c | -10.82407 | -56.60402 | 2026-06-21 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3896ad36-8809-3bc8-90c9-3d01c82e6736 | -10.80676 | -48.56691 | 2026-06-21 04:44:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e47ac29-ae43-3f75-a010-7f45bf99b5ad | -10.155 | -51.64775 | 2026-06-21 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 019b0250-6fba-3e88-af74-9f537078969e | -9.29373 | -48.66665 | 2026-06-21 04:44:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 433b7b15-8890-3f19-ade9-881c0e065aac | -10.12084 | -52.19847 | 2026-06-21 04:44:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3979a33b-c9da-3133-8c01-0b386a389c04 | -8.35749 | -50.50568 | 2026-06-21 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e8be2554-3140-3bb0-8ed2-d16c17a15701 | -8.07658 | -46.22663 | 2026-06-21 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8147f647-6081-3dfb-ad14-8481052cc58b | -11.10494 | -54.1406 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| cd5480e6-3713-3045-b1a4-7f08016b8ee0 | -9.18811 | -58.05546 | 2026-06-21 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd480015-a33e-30a2-bca8-55f107a38b12 | -10.68385 | -60.75819 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 10d59b4c-d28b-35da-b39c-6b037c566c03 | -11.64664 | -52.86707 | 2026-06-21 04:44:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94169913-5fbc-384f-9698-754579af1a70 | -10.27454 | -60.54718 | 2026-06-21 04:44:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82ec3373-3fa5-3171-8b33-004db12b621f | -11.09904 | -54.15319 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 478f751d-2cfb-327a-a7f4-52fef5e49af9 | -8.34866 | -50.49677 | 2026-06-21 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe56ccce-4332-3ae4-8d0a-c0eb6a67f0f9 | -8.7592 | -49.36068 | 2026-06-21 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d7817fce-8b1d-3794-9c00-807074439874 | -11.89312 | -43.83315 | 2026-06-21 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b027bc33-081a-3115-b2a2-d589e6d9645f | -10.53932 | -49.46375 | 2026-06-21 04:44:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13ab7e1f-7eb1-3ee1-b2ea-3e7778aa11f2 | -10.68896 | -47.69938 | 2026-06-21 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9247777c-e5f0-3db5-961f-52823c0dad4f | -11.09537 | -54.15253 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0f0d5be-683c-3024-a26f-6e4296526080 | -9.29171 | -48.67002 | 2026-06-21 04:44:00 | NOAA-20 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3d3dd1b-f5c9-3818-9711-c8c200b66cd7 | -8.65104 | -47.7627 | 2026-06-21 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f2b6687-baf8-37da-a3ef-74b734df5705 | -10.57858 | -44.32901 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 052d8d54-d419-3ff5-8ec1-5bf4a61484f1 | -8.00749 | -46.43983 | 2026-06-21 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ee6ca46-7fb4-3710-bb1e-e9e374b06f0e | -12.06915 | -48.42851 | 2026-06-21 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09cea251-ae3f-326b-b83c-5fbd269516ea | -11.09245 | -54.14742 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7e085c34-a4c8-3c14-9878-2e4337c55e5c | -11.54746 | -48.26864 | 2026-06-21 04:44:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4bbf4b44-5ee9-3baa-82f8-d42a02c142e3 | -11.88794 | -43.83718 | 2026-06-21 04:44:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bf43636d-fd0b-3800-ac4e-2baeb8d77193 | -11.10271 | -54.15385 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d3cfe21f-bd7e-3509-b5d3-266cb7702e26 | -9.18227 | -58.05997 | 2026-06-21 04:44:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a11e7445-ada5-308b-bab1-b2d9c674a365 | -13.56421 | -43.51185 | 2026-06-21 04:44:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54242985-2a1e-336e-80e3-0225992d4e78 | -12.42606 | -54.17986 | 2026-06-21 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 917de87c-4f53-3471-98f4-5c2d40b29a8b | -11.10127 | -54.13995 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 20f9802b-1f00-3c7d-b023-381572293765 | -10.6942 | -60.74821 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0288dc3b-26bf-3bb1-81a7-fa3136b92064 | -8.46423 | -51.53284 | 2026-06-21 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14c53783-84d4-302a-8cb4-99d3eb523015 | -11.11008 | -54.13247 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 38aa158c-73cb-3d28-883b-c81dc4b8eb22 | -12.29642 | -50.10545 | 2026-06-21 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc232654-9df6-3bab-8ba5-fc949b73ce69 | -9.36735 | -48.4113 | 2026-06-21 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87a7263e-b5c4-361a-8277-f1ed03db2b01 | -8.13825 | -46.88388 | 2026-06-21 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58d5daa1-24da-38dd-989e-44ab36d985ce | -11.06354 | -52.46348 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2747b73-2b98-32d1-98e1-538968148020 | -11.10201 | -54.13556 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 22ebca5e-55a7-329a-9883-30a5f295f109 | -11.10053 | -54.14433 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| cd68b913-4e35-3618-9f13-c2d33f820116 | -10.40655 | -49.44257 | 2026-06-21 04:44:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71fb0d39-d46b-3ec4-a195-e0b453d0a7ac | -11.10565 | -54.15889 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c942344-de49-3cd5-99bd-fb07e123582c | -13.499 | -54.42832 | 2026-06-21 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a3bb24d-02bd-3d8b-af2e-d48f4e87d154 | -10.15835 | -51.64832 | 2026-06-21 04:44:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5baca5f1-3ab7-3651-a63f-c33b1a2a4eaa | -10.59363 | -44.33019 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| fe997b49-292c-32ea-b9b9-0a92d00cd032 | -10.83392 | -49.11931 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 49a4a91d-75b6-3524-bced-5ca06869c17d | -11.30131 | -54.72428 | 2026-06-21 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0cbdf9f-d4f5-37ad-a1d0-df2f9b919246 | -8.35473 | -50.50166 | 2026-06-21 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52a6aaed-10de-3bca-a72b-af49455cbdea | -9.31131 | -47.63213 | 2026-06-21 04:44:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4234bbc-dd8e-35f0-9806-ab471d122baa | -11.10568 | -54.13621 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 6b20162f-3437-3c43-a3bc-36a319d56e1c | -12.82896 | -49.79695 | 2026-06-21 04:44:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d41f6ae1-7047-34a1-a71f-cd92b70af177 | -11.30212 | -54.71958 | 2026-06-21 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8bfaf5b-1b0a-3ea8-8001-efee58862bbd | -11.01176 | -45.20955 | 2026-06-21 04:44:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63a596f9-69c3-3892-8e7b-bb94a8dc9e41 | -11.06231 | -52.47098 | 2026-06-21 04:44:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9200fa9-0d46-34da-8b00-78e96ccfd537 | -10.68215 | -60.74988 | 2026-06-21 04:44:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 078b3d1f-f05f-35bf-a4b9-a5b86e6c0d5f | -12.42173 | -54.18345 | 2026-06-21 04:44:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b09ac4b1-2b68-3f6f-90e8-da189a5b7c16 | -11.08952 | -54.1424 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| afd3838a-8065-35a2-81a5-6cb201d3b5d1 | -11.08783 | -43.18263 | 2026-06-21 04:44:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ce5cacc-8cfe-3216-bf32-cf238a614693 | -13.7843 | -52.74048 | 2026-06-21 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0f93b88e-73c5-312e-97df-606aed103a76 | -11.66514 | -56.76279 | 2026-06-21 04:44:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcfaa51c-2eb1-3a04-83fb-892e8432d65d | -8.2595 | -43.93037 | 2026-06-21 04:44:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7700b741-996f-3b32-9fbf-8bbf04f7ffd8 | -10.81165 | -44.56616 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb494d98-0d79-3989-b041-7e5af1016044 | -8.46085 | -51.53229 | 2026-06-21 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53d7a382-2d8e-310b-bbd1-2cc75ccc123d | -9.59139 | -48.72768 | 2026-06-21 04:44:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea5bceaa-744a-3f7a-a461-8b08c034ddf1 | -10.54214 | -47.71551 | 2026-06-21 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1ce10128-f39d-37e5-ae14-ec61e24d3818 | -11.1086 | -54.14127 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| f8eb11bd-e241-3824-bc77-7f105a23677e | -13.49538 | -54.42769 | 2026-06-21 04:44:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fcc04d0-29b3-3c99-bc6e-d4f6eaa7b797 | -14.09161 | -52.19301 | 2026-06-21 04:44:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9c7e4d8b-6185-3120-800b-eef0fb161431 | -10.82332 | -56.60814 | 2026-06-21 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28e6e3b3-418f-3c88-9e0d-d08704eb691d | -11.63722 | -48.53541 | 2026-06-21 04:44:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5f92cc84-72dd-3e03-929d-bb0a39ca9069 | -11.50957 | -56.12243 | 2026-06-21 04:44:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1eb63bd-8ceb-3520-9ca7-e3a3da176750 | -10.58498 | -44.32898 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a152d2dc-493d-336e-8aaf-a5b1ce665ad2 | -13.24879 | -51.89739 | 2026-06-21 04:44:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8049a2ed-ef1b-3435-b7c9-4aecda3fcae2 | -9.68958 | -47.69096 | 2026-06-21 04:44:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bd126b13-7c84-3623-9200-865925974159 | -12.29032 | -50.10083 | 2026-06-21 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c1d8284-e356-349f-8c2e-2ecdb0fb14b4 | -10.92928 | -56.84587 | 2026-06-21 04:44:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee2b3d51-73f2-3c13-87b9-943f556eebfc | -10.58065 | -44.32838 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a7c80a5b-1cae-387b-9e49-932ede0146bc | -10.53975 | -47.73166 | 2026-06-21 04:44:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 21ec85cc-5334-32e4-ad33-6890be39cfca | -10.5893 | -44.32958 | 2026-06-21 04:44:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 035b79c6-a8d6-3fe4-8819-7bc45c746f4a | -12.29587 | -50.10901 | 2026-06-21 04:44:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2bc938b0-527b-3785-bf57-ff684616906b | -11.62083 | -55.18603 | 2026-06-21 04:44:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 28bffa03-c2b2-378b-8b67-d174b5a01a5d | -11.0976 | -54.13931 | 2026-06-21 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 422f5192-c513-389f-93a3-9f986776e00e | -13.56012 | -43.50596 | 2026-06-21 04:44:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72c9169f-f66c-351b-bd39-11f06ba55c21 | -8.00748 | -46.44148 | 2026-06-21 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README8.md)
