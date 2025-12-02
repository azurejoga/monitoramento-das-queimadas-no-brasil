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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08ed1e80-9ef5-3e17-90ef-c2680b021aaf | -3.0768 | -44.2541 | 2025-12-02 00:00:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 72912695-747b-3f20-9c3a-2476007e6682 | -12.885 | -52.5172 | 2025-12-02 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6eaaf9e8-d48c-3e81-8202-72ce592999bd | -4.3703 | -43.1508 | 2025-12-02 00:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 88f7b0c6-d79f-3250-bdb5-81d9a533ebbe | -11.119 | -53.9446 | 2025-12-02 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| c6a306d4-d9fc-38bf-856f-e0baf7d1a59c | -17.5138 | -57.2131 | 2025-12-02 00:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.7 |
| 0a72abdf-5eb5-3570-aff3-fd5c2015898a | -3.2564 | -45.5831 | 2025-12-02 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 902c3811-69ad-340a-b204-fa520c4d04b7 | -17.5335 | -57.2107 | 2025-12-02 00:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.3 |
| ce92e54c-8a03-328a-a6a9-92dd95124ffe | -12.8853 | -52.4962 | 2025-12-02 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 617b4f77-897d-3751-9262-c883acc89308 | -17.5141 | -57.1925 | 2025-12-02 00:00:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.3 |
| 392debac-4008-3d9d-9b32-ffc62923a738 | -4.389 | -43.1497 | 2025-12-02 00:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 265.9 |
| d101d7a8-9188-335c-b55e-534d26bf1f9c | -11.1382 | -53.9223 | 2025-12-02 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| a70ab234-7736-3f89-a421-a4113c968c3b | -11.1193 | -53.9241 | 2025-12-02 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 1a77945c-a9ff-3d60-99f4-09fb31c4f83a | -13.0392 | -53.7107 | 2025-12-02 00:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 35659002-df65-32cb-bd46-57a13a8fe606 | -2.3087 | -45.727 | 2025-12-02 00:00:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 265ea046-aedf-38c0-8f9e-d1709c59d1dd | -2.3088 | -45.7046 | 2025-12-02 00:00:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 4b8f4a3c-3c28-39bd-afc6-612aa8117a36 | -4.3892 | -43.1263 | 2025-12-02 00:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 39168550-aa37-3ccf-a5ae-c480bdde0cca | -4.4077 | -43.1486 | 2025-12-02 00:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| c7139f42-9b70-3841-98ea-a4e745d571ba | -3.8618 | -47.0438 | 2025-12-02 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 08a17632-56b7-3a14-aec5-b69b8d1c704f | -12.5021 | -56.9239 | 2025-12-02 00:00:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 361b8784-bbc2-30ac-9f17-ab587b2663dc | -12.5023 | -56.9038 | 2025-12-02 00:00:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 646b4ae1-a205-3011-ab92-297a3f7856b2 | -3.2565 | -45.5607 | 2025-12-02 00:00:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 8d3222ad-8fde-3cf8-bfd1-930af6af0363 | -4.3705 | -43.1274 | 2025-12-02 00:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 7b2ece52-3b16-3cb1-8d1a-fa9a166184dc | -3.8617 | -47.0657 | 2025-12-02 00:00:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5f187836-466b-390d-a2f8-8e0857575540 | -11.1379 | -53.9429 | 2025-12-02 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 197.9 |
| 98821d1c-1722-37ce-944f-72aa2210769b | -12.5213 | -56.9022 | 2025-12-02 00:00:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 110.4 |
| b3202b44-cff9-31db-a8b3-5419c2bc94c1 | -12.5211 | -56.9222 | 2025-12-02 00:00:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| a1b1812a-6dba-3477-a8ca-2293fda6a8f7 | -2.6079 | -45.1568 | 2025-12-02 00:00:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 57.2 |
| b6464488-39b3-3bbd-b752-262ed1e18b4d | -4.4077 | -43.1486 | 2025-12-02 00:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 44bdf22a-d04a-3cd6-8f83-26626588cd43 | -3.8618 | -47.0438 | 2025-12-02 00:10:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4eef0d1e-58b5-3844-be2c-50021c4c23a8 | -8.0513 | -43.1001 | 2025-12-02 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 97.5 |
| 380a202a-b6fe-33e2-a0c2-651d3e3f6fcd | -4.3892 | -43.1263 | 2025-12-02 00:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 8ed0d87c-bd04-3815-bda5-b4513ebb7752 | -17.5138 | -57.2131 | 2025-12-02 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.4 |
| d16f3f15-edba-3abe-aa16-008b85d127e1 | -17.5335 | -57.2107 | 2025-12-02 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.6 |
| 51f4fe4f-1a1a-3fb0-884b-b20fd4d3ce3d | -3.2565 | -45.5607 | 2025-12-02 00:10:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 26de3bf9-df56-31b2-9a61-36a4229465f9 | -11.119 | -53.9446 | 2025-12-02 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 41be909d-8d29-3a85-bd36-5a345386ea1d | -4.3703 | -43.1508 | 2025-12-02 00:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 8b1fd78c-4d68-3e37-957a-49bda59c7ed3 | -4.389 | -43.1497 | 2025-12-02 00:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 249.1 |
| a6159db3-6082-3259-a880-ca5ad5c99a5c | -4.3705 | -43.1274 | 2025-12-02 00:10:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 97eb7f41-76a1-3fbe-89db-791aaca2f8b3 | -12.885 | -52.5172 | 2025-12-02 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 2598a2b1-1691-324f-a0e4-0328ab6f3ea9 | -17.5141 | -57.1925 | 2025-12-02 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 91.6 |
| 766e0213-d274-3d0c-b438-6d324249f2b4 | -2.3088 | -45.7046 | 2025-12-02 00:10:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3d3394ff-87d9-321f-ad2f-56381f2375cc | -12.8853 | -52.4962 | 2025-12-02 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 82f0747f-795f-35e1-87d3-f5d25f7e9d77 | -11.1379 | -53.9429 | 2025-12-02 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 165.6 |
| 73f4e3ea-2982-3722-bb4f-060bf486755c | -17.5338 | -57.1901 | 2025-12-02 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.1 |
| 0897029f-2e21-3e65-b458-de7ce1e50895 | -11.1382 | -53.9223 | 2025-12-02 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 2a184019-cb84-3933-b377-13ecbf374270 | -8.163 | -43.229 | 2025-12-02 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.6 |
| 08939c54-ed39-31d5-82e1-e088891cdb21 | -3.5481 | -50.5267 | 2025-12-02 00:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1580dc75-cccc-35ba-8e51-7514ea8607b8 | -13.0392 | -53.7107 | 2025-12-02 00:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 9773cb53-3ad7-379e-9333-52680a6d1684 | -11.1193 | -53.9241 | 2025-12-02 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d518fe64-a3e0-324a-863a-616b8f49deb4 | -1.4737 | -45.7907 | 2025-12-02 00:10:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 95ee9fa4-ff5a-3911-8bb8-54ab2b2de33e | -17.5138 | -57.2131 | 2025-12-02 00:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 127.8 |
| 5044d583-3534-387d-96c1-4ae3593e3a69 | -4.389 | -43.1497 | 2025-12-02 00:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 222.5 |
| 7290ded4-42ce-3458-bf30-e949554f3bf6 | -4.4077 | -43.1486 | 2025-12-02 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 5a0110e3-785e-3cd5-8885-3d6693e25335 | -11.1382 | -53.9223 | 2025-12-02 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| b2c6f58c-f376-34da-855b-86a0f1003aac | -13.0392 | -53.7107 | 2025-12-02 00:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4071fb74-f637-3fc3-ae34-defdb9b982c3 | -8.0324 | -43.1022 | 2025-12-02 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 24846b62-4dc9-349f-b7bf-7fddf6edefc1 | -3.8617 | -47.0657 | 2025-12-02 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f43b3b84-bba5-3926-b9d9-706e755854c1 | -11.1379 | -53.9429 | 2025-12-02 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 154.5 |
| c3e50b5a-1e7b-3f82-9799-cc0181e26dc1 | -12.5211 | -56.9222 | 2025-12-02 00:20:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c3f01e81-34aa-3242-b253-801d5ff23538 | -11.119 | -53.9446 | 2025-12-02 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 64713242-f8b0-3243-86a2-5c707ffede41 | -8.0703 | -43.0981 | 2025-12-02 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 8e0aa8b5-dd4f-3975-b88b-815816f33369 | -3.8618 | -47.0438 | 2025-12-02 00:20:00 | GOES-19 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 96d16f7f-44b9-3bbb-8808-478482f7d8e1 | -4.3705 | -43.1274 | 2025-12-02 00:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| e671fe6b-b527-31ec-932a-8bf004ee386e | -4.3892 | -43.1263 | 2025-12-02 00:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 9145bc6f-b2e3-31fe-856a-eac5796b9855 | -12.5023 | -56.9038 | 2025-12-02 00:20:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| cffefb51-4314-31cc-9095-bd3dd7691586 | -12.5213 | -56.9022 | 2025-12-02 00:20:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| b54134c4-3aeb-3295-b7bc-e7db75207a75 | -1.4923 | -45.7903 | 2025-12-02 00:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f48ac2cc-13d0-3577-a948-19f7061a2937 | -12.885 | -52.5172 | 2025-12-02 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3d610036-35b4-3048-9be0-f23789283b05 | -4.3703 | -43.1508 | 2025-12-02 00:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 20f3760e-fc45-3e84-be27-0cc646751b96 | -12.5021 | -56.9239 | 2025-12-02 00:20:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8049080b-1db4-3815-8630-ca162d516d6d | -8.051 | -43.1237 | 2025-12-02 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.0 |
| 5be8f863-177b-3011-a013-4431b71d5fa6 | -1.4737 | -45.7907 | 2025-12-02 00:20:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c8aa60fe-f539-3f26-908f-83a15b4f0455 | -11.1193 | -53.9241 | 2025-12-02 00:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d5a9ece2-16ad-330e-94fa-a10728ca74f6 | -8.0516 | -43.0765 | 2025-12-02 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.6 |
| 5a2cb5e3-d831-348f-a4e0-054f5de42386 | -17.5141 | -57.1925 | 2025-12-02 00:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.4 |
| d4a2f408-4f40-3c9a-bb02-1f296a5f2dfe | -17.5335 | -57.2107 | 2025-12-02 00:20:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.2 |
| ef34aa60-e83f-3f21-9e9f-2b86faa9fdce | -8.0513 | -43.1001 | 2025-12-02 00:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 231.7 |
| b2a3c8d2-3547-34be-9153-afd3860cd9c7 | -4.3889 | -43.173 | 2025-12-02 00:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| deac8b75-bde6-37f7-9179-b8dac2cfbd4e | 3.4831 | -51.255699 | 2025-12-02 00:23:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 0b62b47b-9e35-341f-bcc2-b2ee341dcdef | 2.1781 | -50.8839 | 2025-12-02 00:23:00 | METOP-B | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| c724729d-98f5-32a3-a84c-3c5a514e7392 | 2.0114 | -55.707901 | 2025-12-02 00:23:00 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e34627aa-5650-3e5c-abbd-cb0d948e3cc5 | -8.163 | -43.229 | 2025-12-02 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 1c06e30e-7a25-3b71-9e08-e3e0e7f3eb87 | -12.5213 | -56.9022 | 2025-12-02 00:30:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ab0a3761-99f1-3ab8-9cfe-a6a42fe74acf | -12.885 | -52.5172 | 2025-12-02 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| b8130936-1f59-3922-aa0f-09a5fabfdd5e | -4.3889 | -43.173 | 2025-12-02 00:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 2e2a060c-3f4d-37a1-843a-b59b520d1e20 | -13.0392 | -53.7107 | 2025-12-02 00:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| feb87e07-f103-3c2e-8408-c39e846ee541 | -4.3892 | -43.1263 | 2025-12-02 00:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 138.0 |
| b2be5ed3-9541-3740-b7e4-94430df92c4b | -11.119 | -53.9446 | 2025-12-02 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| f6e4aa25-22e6-3a4c-b0af-46cc0dcb357c | -17.5338 | -57.1901 | 2025-12-02 00:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.5 |
| 7ef05863-f3ad-3b2f-a5f7-621277414e5c | -17.5141 | -57.1925 | 2025-12-02 00:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 118.8 |
| becd1ff1-a23e-397d-bb45-3a06c5578c41 | -17.5138 | -57.2131 | 2025-12-02 00:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.6 |
| b27da814-6e99-3989-bdf2-f49ded18e439 | -12.8853 | -52.4962 | 2025-12-02 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 85e4256c-1685-310e-9bc7-2a5de42e520e | -1.4737 | -45.7907 | 2025-12-02 00:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 3ace83d8-15b1-332d-89ca-f2f52f865388 | -8.1819 | -43.2269 | 2025-12-02 00:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 2a53f3b3-4ac5-3536-8250-f9af1fef6bb3 | -17.4944 | -57.1949 | 2025-12-02 00:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 15083f34-1656-3da3-843d-dea24b7535b8 | -11.1379 | -53.9429 | 2025-12-02 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 5e146cce-21c2-3ce7-8d18-20d48a413ae4 | -17.5335 | -57.2107 | 2025-12-02 00:30:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 142.3 |
| d4f43936-71f1-3844-b24b-09e15c1e3514 | -1.4923 | -45.7903 | 2025-12-02 00:30:00 | GOES-19 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| fd199814-3606-3310-a126-ffe36318fe34 | -4.3703 | -43.1508 | 2025-12-02 00:30:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 122.8 |
| a99902e3-322a-343a-8067-2490f66d4d1b | -12.5211 | -56.9222 | 2025-12-02 00:30:00 | GOES-19 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |


[Clique aqui para ver as próximas entradas](README2.md)
