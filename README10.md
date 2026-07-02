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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6f4c275-92dc-381b-9fda-2a77e1bdbf02 | -12.8746 | -44.3357 | 2026-07-02 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 377.9 |
| c2be2c63-6a34-3b4f-8e20-8dd4a6e65d8d | -11.8007 | -57.0032 | 2026-07-02 03:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| d3f10ed6-68a9-35a2-a2fd-a7a1083f7322 | -12.8548 | -44.3625 | 2026-07-02 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 232.9 |
| 4b93572f-bce2-34cd-b2d9-3ac107ec6545 | -12.8741 | -44.3593 | 2026-07-02 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 252.7 |
| 7d1a6fa7-6862-385a-88de-21ec4c921ad9 | -12.8359 | -44.3422 | 2026-07-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 51551c1c-05f6-3e58-9bef-6d0eae119efd | -12.8746 | -44.3357 | 2026-07-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 300.7 |
| 40d20edd-7866-393d-841d-781ba8990557 | -12.8548 | -44.3625 | 2026-07-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 243.8 |
| 0431793e-4fa8-35bf-bfe0-93e57b1676ff | -11.4149 | -56.0525 | 2026-07-02 04:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 8d59c13b-251a-3abb-af73-b0d7c9a5322b | -11.8007 | -57.0032 | 2026-07-02 04:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ecdd64f9-383f-3535-8ef8-c0c4607e5da0 | -10.9397 | -43.0593 | 2026-07-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| ed6d7b9c-274b-3234-927b-48d6a88b3e9d | -12.8741 | -44.3593 | 2026-07-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 192.0 |
| 38fd78b9-835a-310a-a3c7-a0265acb4f9c | -12.8557 | -44.3154 | 2026-07-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 4aec12ab-922d-301c-a44a-8e047961697d | -12.8552 | -44.3389 | 2026-07-02 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 412.1 |
| 90d4f7f6-fcdf-3752-ae7b-2711a06e1d43 | -11.8007 | -57.0032 | 2026-07-02 04:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 596adeb3-2990-330c-b643-873d62dedd3a | -10.3667 | -46.6878 | 2026-07-02 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 110cbc03-61e6-31cd-b11f-934ff64db7f3 | -10.3857 | -46.6855 | 2026-07-02 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| ce9f45ec-2f2c-3e06-b54c-1d10312bcbd0 | -21.7823 | -56.2976 | 2026-07-02 04:10:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 29c6c297-f7a0-3965-bf89-dd743ebe0863 | -7.83356 | -43.07547 | 2026-07-02 04:17:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a4a7b40c-da00-3bd5-ac00-9064bbc2b000 | -8.65245 | -47.77071 | 2026-07-02 04:17:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ac6df49-d69f-3f1f-8572-8afb64fac398 | -9.19763 | -45.32118 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f48b135-e097-3428-992d-cd321daa27ba | -8.7217 | -48.34226 | 2026-07-02 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cccded38-1b5c-3427-bea4-f7b4ec65f930 | -10.02491 | -46.66675 | 2026-07-02 04:17:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 24f73449-17a9-3c3f-b0a2-f11160e0eb86 | -6.59011 | -43.88556 | 2026-07-02 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8087365a-0b42-31bd-95d4-fa6bef8654e6 | -8.87455 | -50.18368 | 2026-07-02 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfda23df-d706-3b07-9ae6-c624bff67acb | -9.16128 | -47.23633 | 2026-07-02 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 234f8af1-311b-329a-933b-d92702632f78 | -9.28242 | -50.21777 | 2026-07-02 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3f90db5-6563-3324-a75e-4238d7cde95d | -9.19831 | -45.31709 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c841fdb6-ac23-3fba-9e92-1837efea9176 | -6.90522 | -48.04578 | 2026-07-02 04:17:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f0214da-da3e-3301-b425-bfe16b7609ee | -6.59357 | -43.8861 | 2026-07-02 04:17:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f15aff4c-80b5-3707-8c21-421bffbe96c2 | -9.15851 | -47.23772 | 2026-07-02 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f87f82f-9066-3772-9d98-760c3d2498d5 | -7.00711 | -42.7832 | 2026-07-02 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 399cfdba-5ad8-3a17-8b5d-66f349dc91fa | -6.90086 | -48.04502 | 2026-07-02 04:17:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 084fff35-784a-39c1-ace8-ce6ae03e0c7c | -8.06744 | -46.71462 | 2026-07-02 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbe6fd2f-58af-34b1-8da9-741b67344f4b | -7.28141 | -43.26978 | 2026-07-02 04:17:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e00920ac-ee7a-32a4-9ef5-62901c341082 | -8.87544 | -50.191 | 2026-07-02 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 91fb2eb5-a951-3743-9ab5-4fc1255771c4 | -9.28026 | -50.21425 | 2026-07-02 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3104a8d6-6a68-3eca-97c5-a5dde1b1f269 | -3.42023 | -41.70306 | 2026-07-02 04:17:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| eee9b2f9-4b35-3b0d-8543-87ad88246afb | -6.99991 | -42.76392 | 2026-07-02 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b98c0a29-4900-3bac-a151-bf1a8f99825a | -8.1781 | -47.12458 | 2026-07-02 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 291e7059-393f-3edb-aad0-77f02cefa1c9 | -7.09609 | -46.50845 | 2026-07-02 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7719169-ceb0-3451-ac4c-e8d9a1303951 | -8.87157 | -50.18464 | 2026-07-02 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 69c72346-b01c-3df7-b0bc-1adf6ba637ff | -3.8682 | -42.96606 | 2026-07-02 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72ca28fd-91a3-3ec6-b767-ebca48a8d238 | -8.06996 | -46.71678 | 2026-07-02 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1bbe1e05-874e-32ad-9641-bb5b1716626e | -9.15641 | -47.24084 | 2026-07-02 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 851acfca-0a41-34d4-b4b1-d96f9a481d7b | -9.81671 | -46.44137 | 2026-07-02 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| ed2c1b22-aafd-305c-b1c7-9d8505503b18 | -8.49799 | -47.19879 | 2026-07-02 04:17:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3458097f-f56a-338d-a080-f4152d90e1af | -9.24666 | -46.42529 | 2026-07-02 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6fdbae0-341d-3ba6-b7d5-8f3f518ee59b | -7.00989 | -42.78728 | 2026-07-02 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 9bfdac2a-5be6-38d8-b330-c540a4692579 | -8.71307 | -48.34068 | 2026-07-02 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0face55a-405d-3076-a4e4-9b1676f31abc | -9.19047 | -45.31995 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 032f262d-46d0-358c-8ed8-4f0b53309f02 | -9.20837 | -45.32301 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b971a7d2-6d79-3c8b-820b-5e4152a1d723 | -3.41356 | -41.70201 | 2026-07-02 04:17:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| fd62080b-cf86-3f1c-8049-59157ca531e0 | -3.87103 | -42.97029 | 2026-07-02 04:17:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0b9de00d-3ec8-3aa5-8ba2-8d19e23d0cc0 | -9.75391 | -47.88066 | 2026-07-02 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0531331-3da4-3dc6-aead-73a928881164 | -7.00433 | -42.77913 | 2026-07-02 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f51ff2c0-f981-32b0-bafc-0bc2b3ebdcfe | -2.48384 | -47.09142 | 2026-07-02 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e17184b2-c0dd-3cc9-8270-d3c70a71fa2c | -8.65789 | -49.71471 | 2026-07-02 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8f5977c6-4a2c-3275-aa6c-4f8687e6b0bf | -6.91879 | -43.71838 | 2026-07-02 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76cace70-3ddb-3d0c-bd2a-7de0348f2c95 | -7.09215 | -46.50782 | 2026-07-02 04:17:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bcb0939-99f0-35e3-a91f-0cef8582e8ba | -8.07137 | -46.71529 | 2026-07-02 04:17:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc88b926-91d6-385d-ad74-4ca6c19a337c | -7.09919 | -46.51414 | 2026-07-02 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 048d8290-49fb-3e59-bd2b-3df11d2c7dec | -8.31791 | -45.37587 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edbcdca4-1062-3bd8-ba3c-49e5f277d4f2 | -9.21195 | -45.32362 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bf779faf-c3f7-30ca-8fd8-e82bf6a6900d | -8.8736 | -50.18911 | 2026-07-02 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 024abde0-9314-3d0f-93a9-0330cecccc1c | -8.71808 | -48.33745 | 2026-07-02 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 1dc7c657-5c79-3e41-8946-1204b5583d6d | -3.40967 | -41.70496 | 2026-07-02 04:17:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59d19b42-05fe-3233-8ad4-dd9f64dbf8e5 | -3.41245 | -41.70897 | 2026-07-02 04:17:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| ccba82b3-02b9-313b-834a-f7983de9a264 | -10.30102 | -40.7231 | 2026-07-02 04:17:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 1ca1b386-4ebf-35f7-ba23-492c9fe04f59 | -7.66017 | -46.89096 | 2026-07-02 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d1733c6c-d5bf-3491-8016-55b4eb1afa82 | -7.50944 | -45.85993 | 2026-07-02 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bd9649a0-d387-3070-9adb-8387f622fa90 | -3.41022 | -41.70148 | 2026-07-02 04:17:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b6d8766-b570-3819-8482-383d63babe2a | -9.15729 | -47.23563 | 2026-07-02 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a2606a11-13ad-3a54-a953-0d6f6ac7f0a3 | -9.21553 | -45.32424 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1169df6f-f1bc-30f9-9ce8-950c0a6de777 | -4.16011 | -43.08285 | 2026-07-02 04:17:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6dcbd8a4-683e-3a25-b981-85917fa1f117 | -10.02605 | -46.6698 | 2026-07-02 04:17:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 179b38f5-6b7c-3e6f-a7d9-0e10efa57c6f | -6.92162 | -43.72267 | 2026-07-02 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d64748e5-280e-36fe-8e44-e3b7d9e99787 | -7.00269 | -42.76799 | 2026-07-02 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7da2dbc2-2998-30a0-8975-1b5aa04c7aa0 | -6.92565 | -43.7195 | 2026-07-02 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7afbb13e-a6b3-38de-86a7-c9fcbcde72e9 | -9.75803 | -47.88139 | 2026-07-02 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b8a44d9c-0c32-3fa3-9219-f8f6772d15d2 | -6.92222 | -43.71894 | 2026-07-02 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 11e0ad33-1835-311b-8d3f-9ee12172bdfd | -7.90617 | -48.24506 | 2026-07-02 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d89a913-115a-3c34-914f-7363fb62ba9c | -9.19405 | -45.32056 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e646f60-5645-3d01-8187-44b435cebe3c | -9.82125 | -46.43745 | 2026-07-02 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1aa5e8f8-8387-369d-8d98-1c00c99b1478 | -9.24745 | -46.42065 | 2026-07-02 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab93c880-e379-3c06-bd0f-c84ac34dc655 | -7.00212 | -42.77152 | 2026-07-02 04:17:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c3f5781-4519-3733-af77-27b33dca83b8 | -9.18029 | -49.6686 | 2026-07-02 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31ea7c1b-54e2-3ea9-b6fa-33256448a56c | -8.87643 | -50.18559 | 2026-07-02 04:17:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80ebcbf3-84dc-3a11-b860-c6c35805d990 | -3.41578 | -41.7095 | 2026-07-02 04:17:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 2586bab0-87c2-31e0-a568-d9c8d95f3b6e | -3.413 | -41.70549 | 2026-07-02 04:17:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 46c4583a-e990-3cb6-b359-f47c1221f7bd | -9.1625 | -47.23841 | 2026-07-02 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cbdd12c-9568-3bd1-9273-f175bb51d1cc | -9.2793 | -50.21964 | 2026-07-02 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32ca73bd-e123-3664-82af-b0bb45debb03 | -7.90526 | -48.24629 | 2026-07-02 04:17:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fabf28f-d509-3c90-8587-ec4cdf02178b | -7.10003 | -46.5091 | 2026-07-02 04:17:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 07bd5a3a-5578-364a-b42c-316d165cf3c9 | -8.65406 | -49.70876 | 2026-07-02 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f6705d1-4399-3dda-9ee4-59fa6bc14f71 | -7.50567 | -45.85933 | 2026-07-02 04:17:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3752b8b7-0a47-3696-871b-a0d512aa0815 | -8.7224 | -48.33823 | 2026-07-02 04:17:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8017bc83-e114-3bd7-ba00-c8b8992e174b | -9.81748 | -46.43681 | 2026-07-02 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0efca0c-f7f8-3dd1-859a-86f5117f66ad | -9.82278 | -46.42832 | 2026-07-02 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 508d2984-fa8d-39ea-801f-2f4fabc998d6 | -3.41634 | -41.70601 | 2026-07-02 04:17:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 133034c2-f8f4-33a9-9e6e-5c4143409ec3 | -9.18689 | -45.31935 | 2026-07-02 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
