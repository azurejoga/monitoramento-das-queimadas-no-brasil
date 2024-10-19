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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5618fe97-6bf0-3250-82ea-b374bded3ee2 | -3.51758 | -43.23129 | 2024-10-19 04:25:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2e95de1-5a06-3e83-8f93-a3f55fabb1ce | -3.23217 | -44.41109 | 2024-10-19 04:25:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50338c93-68e8-3185-ad2f-1b0d12b188fc | -4.65057 | -43.75611 | 2024-10-19 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c860ccac-5c29-3ee4-91f5-535892b163a0 | -4.43975 | -43.96367 | 2024-10-19 04:25:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3766a5a8-3bab-3782-9c7d-bfa1e278277d | -4.60113 | -44.61903 | 2024-10-19 04:25:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f29708c4-5be6-3134-8e8d-22f65c2e664e | -4.60058 | -44.62256 | 2024-10-19 04:25:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 11bc44e9-d8cb-3de7-ace0-6deec74682af | -4.19763 | -43.78012 | 2024-10-19 04:25:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6659c6d8-8a5e-3e36-9dee-72eb9d2aef7e | -6.30235 | -43.77334 | 2024-10-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39fd6a71-ad4d-3bc2-8329-e9872893b93a | -6.30176 | -43.77731 | 2024-10-19 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45b1d7ec-e2f8-3319-8535-122d6f1f3c57 | -5.57078 | -44.88137 | 2024-10-19 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d3f0198-1564-3c21-bd26-72ddaddfae5d | -5.57023 | -44.88491 | 2024-10-19 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b19ef8ee-1d04-3e32-9a37-3a16f12589d5 | -5.56968 | -44.88844 | 2024-10-19 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b3209ee-e91a-3fcf-8c17-edc6bd9c2fca | -5.56913 | -44.89196 | 2024-10-19 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81486e1c-d6a3-3e8b-a142-c4cd53305466 | -5.56579 | -44.89144 | 2024-10-19 04:25:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f51ee18-91cb-3e17-8f35-0a5069a7f458 | -5.20003 | -44.79128 | 2024-10-19 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7268a64a-ae5a-371c-96ae-f58216d2e156 | -5.11373 | -44.73462 | 2024-10-19 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f2a757e-de0b-3f79-848b-d3c7682ae164 | -5.11038 | -44.7341 | 2024-10-19 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b114f668-0d26-3148-8c58-09037fd62e2c | -2.57238 | -45.49706 | 2024-10-19 04:25:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d273664-74d7-38b7-92fd-97d14251fe64 | -2.56908 | -45.49655 | 2024-10-19 04:25:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b7c15b-fafc-3bb4-a86c-f212ea5da8a9 | -3.00091 | -45.60665 | 2024-10-19 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92e7fee7-83c2-3f30-ac2f-a9d0821aabf3 | -3.00038 | -45.61007 | 2024-10-19 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d6671d2-b595-33ac-8618-b1847acf5f25 | -2.99708 | -45.60957 | 2024-10-19 04:25:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93dfd4ab-1f7e-3f0b-9481-a634d61f13f1 | -3.55797 | -45.35405 | 2024-10-19 04:25:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 15f59074-7f7d-3648-9ef1-55268c004f80 | -3.55743 | -45.35748 | 2024-10-19 04:25:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26d4cdbd-67e8-3ec7-8752-a65842955ca4 | -3.55467 | -45.35353 | 2024-10-19 04:25:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 74801329-48bd-3e24-bf6a-94d10b280d11 | -3.55413 | -45.35697 | 2024-10-19 04:25:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26796d9b-6bff-36d3-a3aa-8ccf076520b8 | -5.12075 | -45.14946 | 2024-10-19 04:25:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6582fc81-43c7-3488-b3ea-98ee29cd5aaa | -5.1202 | -45.15295 | 2024-10-19 04:25:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7eef405e-0bf0-360d-a59c-c68d5800c663 | -5.11966 | -45.15644 | 2024-10-19 04:25:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2539a88e-910a-3ead-8b17-b03a4560d072 | -5.02277 | -45.12361 | 2024-10-19 04:25:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5151db3d-36c3-35bd-96d1-be79bd882a2b | -4.92628 | -45.72115 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f262980c-a431-311d-83f7-23a70440e20e | -4.84568 | -45.10279 | 2024-10-19 04:25:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6b06957-b250-3c28-b065-2472ff37f1cf | -4.81639 | -45.81316 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82fc22ad-bcdb-3d78-9e91-10f572850307 | -4.71869 | -45.85003 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6974f9ad-2d3d-380d-ad4c-f5398e2f1906 | -4.71707 | -45.86034 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d26a3fd-cb2f-3e85-ae45-eef5c2882570 | -4.71593 | -45.84608 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 504821c6-1b30-30ab-b976-135005e4c56e | -4.71378 | -45.85982 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 079adfe1-42f6-3fa0-983c-3256322fd447 | -4.71317 | -45.84213 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3b4be68b-d12f-301b-abed-f2f90a23de0c | -4.71263 | -45.84557 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a7e4d74c-ffa6-3e80-bcdc-af89f110f41e | -4.7121 | -45.849 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1684175d-4de6-3891-90e2-35f395732905 | -4.71102 | -45.85588 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f708a5f2-b3aa-3f4a-9e43-f6b2eb0e8435 | -4.71048 | -45.85931 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64791e61-0917-3c06-bfbc-7692bbfdfc55 | -4.70994 | -45.86275 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 455c99cb-a406-3223-ba14-c125569c6507 | -4.70934 | -45.84505 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2f954c24-869c-3ce3-aa65-ba97b2d33f63 | -4.70766 | -45.83424 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 25cbebd9-6a36-39c7-ad36-63aa33305363 | -4.70712 | -45.83767 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 74c58b81-7bdb-35f5-97ce-a1af28f88331 | -4.70658 | -45.84111 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| f1e34976-9262-3924-afae-cfcf47c14458 | -4.7055 | -45.84798 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ee70db66-6fd4-3df2-9c46-4a575258365f | -4.70496 | -45.85141 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5bd68125-bbe2-3c84-9914-e884de0f6048 | -4.7049 | -45.83028 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3eb11f8d-4c9c-3b58-a35c-f8c9f9f08529 | -4.70442 | -45.85485 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 345372b6-0405-3f95-8002-18a0754fa738 | -4.7022 | -45.84747 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0754d16d-21a3-3052-b0bd-aa2f4a52a47c | -4.70166 | -45.8509 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5a683428-ebc4-322e-a890-7edba6862936 | -4.69998 | -45.84008 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d17d7c49-661f-3885-bea9-559790675990 | -4.6995 | -45.86464 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c10f045-1335-32d9-9a98-861fb914d7d0 | -4.6989 | -45.84695 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ec11667f-f0ea-3939-bf9d-769f424721fa | -4.6983 | -45.82926 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bdbf0863-7656-35f6-b81f-93d27e743a6c | -4.69776 | -45.8327 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 722afddb-a6ef-3dc1-a4a7-26e4d2936078 | -4.69668 | -45.83957 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7bd9689a-1acf-3200-ac08-01cf37413ae8 | -4.69614 | -45.843 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d3cdf51b-2165-347d-80b3-990fa92d6c3b | -4.52612 | -46.0766 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04c5dc1b-e6ab-3758-a577-87344ed39e3a | -4.52558 | -46.08003 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60f1e4a8-6b57-3e73-afeb-8dc241ca1ee8 | -4.52282 | -46.07608 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dba5bdae-4087-3e1d-8c8d-859200430fb9 | -4.52228 | -46.07951 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed6f3f8d-5302-3e34-83d7-95d16257643b | -4.46627 | -45.89841 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4d02c0f-170f-3bdf-bd5e-d0933d8e01b8 | -4.4477 | -45.81759 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4514ed93-eaab-39d7-b43c-1c04e31eaa86 | -4.75101 | -45.81635 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9b8da90-c0ab-3ef5-a728-d12bc89dbf64 | -4.75047 | -45.81978 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 770feddd-8b2c-38a5-80c1-0478d2007c19 | -4.72199 | -45.85054 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8c07dfd-5904-38c0-9f7d-3c5e6189b224 | -4.71815 | -45.85346 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05c8f167-d871-3f05-9b79-9535c8840dda | -4.71702 | -46.03277 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 015b9a7f-f067-3f46-832f-f329b8270409 | -4.71653 | -45.86377 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 18eb518c-4bde-3f68-9a90-5542fe612456 | -4.71539 | -45.84952 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b6b689a-3779-3668-b2af-6c7403875bef | -4.71485 | -45.85295 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e69327f4-2413-3dea-a070-dcd6ab9fa1ac | -4.71431 | -45.85639 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9023f197-4464-3bd6-bc25-002be299d586 | -4.71372 | -46.03226 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 689a9838-1607-3037-8842-8d6340ed1643 | -4.71324 | -45.86326 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 32827939-fa67-3057-95cc-90ef1ac4df6d | -4.71318 | -46.03569 | 2024-10-19 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a5d4bcfd-305f-3fc1-948e-42ed169b28b5 | -4.71156 | -45.85244 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a88094c9-c868-31a6-8c11-f1ee67f778a5 | -4.71041 | -45.83818 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5d1eff0a-1f66-3f3b-9eaa-bbb80cf4328f | -4.70988 | -45.84162 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02d54df1-cfbb-3964-b663-bbc59649111d | -4.7088 | -45.84849 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1244c909-09d6-3cc3-967c-235d00c57e12 | -4.70873 | -45.82737 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47ccfe6e-1c64-36b6-90c0-916162ceffcd | -4.70826 | -45.85193 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01a802be-fbf9-314c-abcb-e776e468f673 | -4.70772 | -45.85536 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d5a1f7e-b408-3640-b785-c96e3f38349b | -4.70718 | -45.8588 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4af975e0-6f65-33fc-9078-6067e56c8835 | -4.70664 | -45.86223 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac25da36-127c-3e91-b7a8-1449b11df8c5 | -4.7061 | -45.86567 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ab9f07cd-249e-373c-a598-92952e8f1aaf | -4.70604 | -45.84454 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 1bc6fe11-dd2b-3cd6-866e-8f82e847293a | -4.70597 | -45.82342 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab6a9390-8c3f-3a73-943d-caca3f7a4918 | -4.70544 | -45.82685 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de5c7e53-afda-3d02-b90e-f2efc794b617 | -4.70436 | -45.83372 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d6cf307a-07d4-328a-8730-f78247c2c6b2 | -4.70382 | -45.83716 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bab8c745-c2d3-3d26-89c7-f6adb3ccb0f9 | -4.70328 | -45.84059 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| f9c9b57a-3a6d-3ab1-827f-f7898bad96b2 | -4.70274 | -45.84403 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 53af270b-d464-3729-9713-572f53408205 | -4.70214 | -45.82634 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7f00a7e-d11f-3dc7-91c6-c62ccf490d1f | -4.7016 | -45.82977 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f90a93fc-cd30-3f1f-81fb-41770a7b8bee | -4.70106 | -45.83321 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7581dfcb-8b24-3e23-9290-88e6ea8eb301 | -4.70052 | -45.83664 | 2024-10-19 04:25:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69164762-987a-3ac1-a699-aecc6e9c7d66 | -4.70004 | -45.86121 | 2024-10-19 04:25:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
