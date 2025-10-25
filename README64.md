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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83fcccb5-fc6e-3166-a734-a2ad67b35b54 | 0.3589 | -50.9206 | 2025-10-25 13:50:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e3b8e3c1-e339-33d1-8163-b2aa8e6575a6 | -6.7811 | -43.8097 | 2025-10-25 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 5cadd57d-e5d7-35a1-8d4d-fad80af198ca | -13.6488 | -48.1845 | 2025-10-25 13:50:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 37fe03de-991c-3d8c-bd76-2da81b36ac2f | -4.8935 | -43.2115 | 2025-10-25 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 1d760d61-b58a-3661-b881-7b84cb642d01 | -13.0635 | -47.5575 | 2025-10-25 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 51.3 |
| cfa3b59e-ba59-32c5-9e5b-0e1b4b209e8d | -5.9048 | -41.2831 | 2025-10-25 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 151.4 |
| 27dcfe35-8b9b-3c99-b857-34b0ef732cd9 | -4.912 | -43.2337 | 2025-10-25 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 0734d097-31b5-3055-8fec-299a4861f0f4 | -12.466 | -44.5428 | 2025-10-25 13:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| e9b628f6-8495-323c-bd16-a86b126d1cd1 | -6.7809 | -43.8329 | 2025-10-25 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 6e2a3b79-d431-3d74-ba8b-b5d6d37d3be8 | 1.6386 | -55.7258 | 2025-10-25 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 09dc67e9-3ecd-397f-aba5-38f8dedf21bc | -4.8933 | -43.2349 | 2025-10-25 13:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 155.3 |
| 1473af03-0011-3d26-a1ae-9692c255db13 | -18.6408 | -52.1242 | 2025-10-25 13:50:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 735259e3-69d4-37b7-8de7-d48de6649ea9 | -6.5475 | -41.0549 | 2025-10-25 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 146.7 |
| 9111ab3d-0a14-30ed-83f3-ea53b8a8a133 | -6.8017 | -45.4332 | 2025-10-25 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 630a33fd-e152-36ae-8245-f1daeae87c81 | -7.8238 | -40.256 | 2025-10-25 14:00:00 | GOES-19 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 212.8 |
| e6b87836-395a-3cb4-b6da-47684bdb2f4a | -6.5289 | -41.0324 | 2025-10-25 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 145.9 |
| 0ba5c28f-e726-3425-906c-937cd1f8f52c | -6.5478 | -41.0306 | 2025-10-25 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 136.4 |
| e7a25f48-8799-3409-bd96-8c6bdde7dcb7 | -5.6065 | -45.1852 | 2025-10-25 14:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| f353e0e4-8abc-37f5-9388-aaf03b008178 | -12.2475 | -47.0473 | 2025-10-25 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 49.2 |
| a33eaa00-0642-38c6-8c25-604d5c286bad | -5.9048 | -41.2831 | 2025-10-25 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 401.7 |
| 2a8a2739-9918-3773-8876-d35818dba6db | -6.5286 | -41.0567 | 2025-10-25 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 159.1 |
| fa07a3e2-3bcb-3dc9-821d-1973af7ebb79 | -12.466 | -44.5428 | 2025-10-25 14:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 75a4cb36-efbd-3e33-82db-2dc2d322d617 | -4.8935 | -43.2115 | 2025-10-25 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| bf836139-dd2c-30fe-b5a4-08c523a1c675 | -6.2857 | -40.8606 | 2025-10-25 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 123.9 |
| 9792e6be-b2f6-3005-9972-6e9298ccb87b | -12.852 | -48.653 | 2025-10-25 14:00:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 6767386d-845d-37b8-994d-1eca58097328 | -12.3427 | -47.0788 | 2025-10-25 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 203e7e2b-94f7-3100-b4e4-aaa05d6bcbec | -13.6488 | -48.1845 | 2025-10-25 14:00:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 286.1 |
| 300e60b9-f8cb-39c4-a1ce-58b5434a4dbe | -6.802 | -45.4105 | 2025-10-25 14:00:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e0d463b4-1706-3151-a57e-8b1db4bbe7b6 | -3.3103 | -42.3374 | 2025-10-25 14:00:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 05fcd8e2-a731-35af-9929-693303d12631 | 1.657 | -55.7058 | 2025-10-25 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 0ccd1c7b-ba85-337b-a469-ba1fdd2a9449 | -13.9147 | -48.4112 | 2025-10-25 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 44.2 |
| a8b65c32-1c1e-3826-9dd2-48284afbe63a | -17.3869 | -45.4926 | 2025-10-25 14:00:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 50013783-121a-33ad-97ab-217cb532587c | -18.6408 | -52.1242 | 2025-10-25 14:00:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 68d8dc4f-ef84-3bea-ad12-ce6769230c04 | 1.6753 | -55.6858 | 2025-10-25 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d823060f-3fe8-3348-8cc5-784b455361b2 | -4.8931 | -43.2582 | 2025-10-25 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 97d58d7f-13a0-345c-afbf-a02af18c8bd2 | -8.0184 | -38.5467 | 2025-10-25 14:00:00 | GOES-19 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 103.7 |
| 62d75969-6196-39ff-8e44-0fc3762c4b8f | -11.9453 | -46.8198 | 2025-10-25 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 83cf908a-1898-3ebb-97e5-4a89e9a13999 | -6.9371 | -45.0362 | 2025-10-25 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| dc97eaec-4b36-35f2-87ad-bb119d24ea37 | -5.6055 | -41.1145 | 2025-10-25 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 116.3 |
| 69dfa06d-ed2e-332f-93fa-8f03b78a46f8 | -16.1703 | -45.0881 | 2025-10-25 14:00:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 77122bc8-3ade-3828-b5a7-8cfc5d2d98eb | -6.5104 | -46.5097 | 2025-10-25 14:00:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 2848a17c-21fe-3df7-b3d8-cf3f982de534 | -5.886 | -41.2847 | 2025-10-25 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 520.9 |
| a82d82f7-bedc-3444-b332-671814a855b4 | -6.7811 | -43.8097 | 2025-10-25 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.8 |
| a470083a-d69f-35fc-aba4-f68c09dd8293 | -6.7809 | -43.8329 | 2025-10-25 14:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ad5f8d5a-aaee-306e-9ddc-abcd8dcc1c30 | 1.6386 | -55.7258 | 2025-10-25 14:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e8662607-de2f-367d-b8a2-5e197d96cc9a | -4.8933 | -43.2349 | 2025-10-25 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 235.4 |
| f710e75a-39b5-31c0-a0ac-3660a8c91c0f | -6.2854 | -40.885 | 2025-10-25 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 237.5 |
| 05e6afe3-efc4-309f-b918-6df105d344cc | -3.9928 | -43.7522 | 2025-10-25 14:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 5dc49074-6511-328b-aea3-086e724f81f9 | -14.9041 | -52.4566 | 2025-10-25 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 9d5a081b-f543-394a-a472-f70444b3b5fb | -12.3427 | -47.0788 | 2025-10-25 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 5632cd6c-57f0-3f36-a3a1-bf8f35e40dfe | -4.8931 | -43.2582 | 2025-10-25 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 39360db7-0425-3cac-8928-55be827fc03a | -6.5286 | -41.0567 | 2025-10-25 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 152.6 |
| bc70e982-c24b-3003-9acf-3718ce470589 | 1.6386 | -55.7258 | 2025-10-25 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 39f2b0e1-c610-3f2a-8a13-8102d5cee2eb | -6.7809 | -43.8329 | 2025-10-25 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 7d8ed373-2f3d-3ec2-9ceb-237538c16206 | -12.2475 | -47.0473 | 2025-10-25 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 8ed3ceef-5dcc-3607-a2fe-7484452ae7f6 | -6.5289 | -41.0324 | 2025-10-25 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 163.9 |
| 0539de67-6111-3a4b-aec4-40adf7d31d61 | -4.912 | -43.2337 | 2025-10-25 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 9a739764-2f7b-3bab-aacd-abb2ece1272a | -7.7971 | -45.3893 | 2025-10-25 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| fd5df7ee-0523-37af-80c5-b6fc49ef2dd3 | 1.6753 | -55.6858 | 2025-10-25 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 482dcf05-bd93-3e29-93d5-7c115e5cc653 | 1.657 | -55.7058 | 2025-10-25 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| b67da283-7561-3131-a10c-cc7f8609ec81 | -6.2854 | -40.885 | 2025-10-25 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 224.2 |
| e5ca5531-84a7-3ab5-b847-ec41de4efbb6 | -12.852 | -48.653 | 2025-10-25 14:10:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| f58801a9-59c5-35d9-92b4-ff2601cb7df7 | -6.9169 | -45.1743 | 2025-10-25 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| efb1fcd9-22e8-384a-8c07-4a8687581838 | -7.8238 | -40.256 | 2025-10-25 14:10:00 | GOES-19 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 153.2 |
| 41181d9e-283b-35cb-b80c-f13d31284db6 | -13.6488 | -48.1845 | 2025-10-25 14:10:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 15a14f86-db6f-3883-b937-d1de82aeef6e | -5.6065 | -45.1852 | 2025-10-25 14:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 97053bac-f6b3-34b0-931e-1c02857171dc | -5.886 | -41.2847 | 2025-10-25 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 301.4 |
| dd08246e-6e05-38da-af11-5fae77e24caa | -6.7832 | -45.4121 | 2025-10-25 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3f65e456-483c-31f2-9897-f0d611f68390 | -6.7811 | -43.8097 | 2025-10-25 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 9ed05e6b-d576-3003-be87-1d9f954ce008 | -14.8847 | -52.4592 | 2025-10-25 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| b158f861-11bf-3e1f-8282-4f2b5f5715fc | -6.5478 | -41.0306 | 2025-10-25 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 170.1 |
| ac8d9deb-af28-3577-a3b1-e78f144799f6 | -3.3103 | -42.3374 | 2025-10-25 14:10:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| bf7a59ba-e45b-36d5-a771-cef1f4653240 | -6.8017 | -45.4332 | 2025-10-25 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 95.0 |
| a93ee458-fa46-3464-b65f-74ec718b422d | -6.2857 | -40.8606 | 2025-10-25 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 136.1 |
| 0ce10016-5d10-3c66-8b6e-3f6b930dc638 | -4.2488 | -44.5648 | 2025-10-25 14:10:00 | GOES-19 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 3cf2257e-8822-3e17-a5db-1fc45757c14f | -17.4112 | -46.8881 | 2025-10-25 14:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 00521bbd-87bd-3536-8c07-d888be1c4e12 | -6.802 | -45.4105 | 2025-10-25 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 46ed8a57-20f5-3d36-8482-31e1540f4f8e | -17.3869 | -45.4926 | 2025-10-25 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 81.1 |
| fce871fd-e6a6-3d8e-a2c0-26bc0ddb1812 | -14.9045 | -52.4354 | 2025-10-25 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 431ad7a4-acc4-3597-a5fc-190725ba4909 | -14.8851 | -52.438 | 2025-10-25 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| b451620e-10ff-3f8c-ae2d-acae7855dee5 | -6.783 | -45.4347 | 2025-10-25 14:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 8d484a24-4026-3499-a187-e50384e49916 | -6.5104 | -46.5097 | 2025-10-25 14:10:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 0e557826-1de9-3659-8a9a-0de389f11094 | -18.6408 | -52.1242 | 2025-10-25 14:10:00 | GOES-19 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 60.5 |
| b97b6a03-4608-3412-89e1-ea576652e63f | 1.6386 | -55.7455 | 2025-10-25 14:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b3adb4af-69ab-33bf-ae21-98eac63609be | -4.8933 | -43.2349 | 2025-10-25 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 248.9 |
| 265f08dd-8f88-3080-b4bb-f24ef300b23b | -5.9048 | -41.2831 | 2025-10-25 14:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 210.3 |
| e1350267-1e05-3068-8a5b-1da2582c14f5 | -14.8463 | -52.4431 | 2025-10-25 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 9c3f91de-971a-3974-88ee-7772195d653a | -6.5475 | -41.0549 | 2025-10-25 14:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 155.1 |
| a7431e08-fb48-30e6-9368-19892b7ed65e | -4.3133 | -43.294 | 2025-10-25 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| b9bc394a-aa34-3ab3-919a-8b3ffc0b3350 | -12.2475 | -47.0473 | 2025-10-25 14:20:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 00bfd12a-b2ea-3732-b719-a547dc10940e | -6.5478 | -41.0306 | 2025-10-25 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 251.7 |
| 1d6c26ab-11a1-3adf-877b-7d13df6ac183 | -6.8017 | -45.4332 | 2025-10-25 14:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c552ebb3-70e6-32b5-b9ca-389d6e9e64af | -4.8931 | -43.2582 | 2025-10-25 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 110.5 |
| cdc469d2-d12d-3aa3-aeab-836126a22338 | -14.3168 | -51.7901 | 2025-10-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.5 |
| ed7c4b7e-0843-3fc4-a502-e0bf0c607015 | -14.2978 | -51.7713 | 2025-10-25 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 75360cc6-5c83-310e-bd57-651ce6baa991 | -6.5289 | -41.0324 | 2025-10-25 14:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 133.9 |
| fc3efc19-6dd8-38c1-b3fe-43a2fdee357a | -4.912 | -43.2337 | 2025-10-25 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 9c3c6103-ec2f-3704-9ddb-6f6bdebe7ba0 | -11.9453 | -46.8198 | 2025-10-25 14:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| c5d3c99a-fa52-3ab4-aa6e-12f0adcf7a2b | -4.8933 | -43.2349 | 2025-10-25 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 239.7 |
| 071fdf78-a235-3831-8890-b99b5e05a042 | -13.9147 | -48.4112 | 2025-10-25 14:20:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |


[Clique aqui para ver as próximas entradas](README65.md)
