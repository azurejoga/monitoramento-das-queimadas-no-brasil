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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4fa10d22-709f-39fb-adcb-a19aff232897 | -12.97259 | -54.78821 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38ed3668-66c9-3f8d-b070-d1787b1b3385 | -7.89984 | -44.93602 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d66a8bfb-0328-37c5-82f0-4892148d2cd2 | -6.26686 | -53.54015 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3dd1bf2f-e826-32a5-9eac-3a34978d62ac | -12.9854 | -54.79392 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e27263bb-9067-381f-a029-db30df3d5140 | -11.4846 | -55.51712 | 2025-09-05 04:57:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c5d2066-26e5-3e1e-b16c-64112be2abe1 | -5.89869 | -57.7317 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3674e53-14ae-3165-9945-91a3e050e2c3 | -12.95243 | -56.99641 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e1789be-9d2d-339e-b3b2-766f43b5269a | -10.09343 | -54.77652 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 60cac3cd-651d-3417-81d1-09d1d5a0f9b4 | -12.97318 | -54.80668 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d6c81257-ccc0-311f-8521-eff9ef79a009 | -11.54637 | -47.31573 | 2025-09-05 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1ce75115-23fd-3368-92ae-277df258b796 | -11.64154 | -54.53423 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afa4066a-1e9f-3fc9-a736-b535c55f826a | -12.50236 | -53.84671 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6633d79d-e668-3ddd-bc3f-9034211bf688 | -6.85004 | -52.80626 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b39753a8-520d-30ba-9e25-e62e8a955a05 | -7.05663 | -52.71788 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 293494b3-db13-3d61-888a-3595c008c182 | -10.09012 | -54.77599 | 2025-09-05 04:57:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4971ee50-e136-3555-a18c-d9ee80c881c0 | -5.85138 | -57.7748 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1468835-71fb-3491-89f4-90ca3ea77c20 | -7.97576 | -44.53045 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57c78118-8d26-3881-a084-fe7bbedf7857 | -10.06489 | -58.39717 | 2025-09-05 04:57:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c99ba1f-b61c-3449-b4ee-610217081911 | -9.81643 | -54.87584 | 2025-09-05 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efb00995-5cc5-3193-accd-cb19146b9d07 | -10.47142 | -53.62562 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fbab75f-a422-32bf-8720-ebd21ddb68a2 | -13.50757 | -50.80941 | 2025-09-05 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5f35358-88c6-3a42-a7fc-d91ebf5bd4f1 | -11.60138 | -52.15777 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c834f7cb-0f40-3e71-ad80-564e3edb66f5 | -12.29347 | -50.01954 | 2025-09-05 04:57:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10b82cd8-61dc-396b-bd2e-c501e41f99d6 | -7.97744 | -44.51766 | 2025-09-05 04:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9ed96241-cff2-3062-b27e-d3931b5fd2c1 | -12.52905 | -53.80856 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| da900f65-d34b-36f4-beaf-57d69389e713 | -11.62406 | -52.20452 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c8ed0dc7-c7aa-3a93-8bf2-3a8bd931fd40 | -11.64542 | -54.53119 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bf8bf2e-5f02-34b3-8171-4d3ec4b3fb5b | -12.64251 | -57.00111 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69e028f2-e786-37bc-b522-7dbbc7298bc1 | -12.98595 | -54.79033 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fe7ef6ed-6c0f-3348-af80-2644a005704d | -12.99097 | -54.80219 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bd1e4504-87c5-3cae-a96d-ae6480d9d323 | -8.04406 | -45.3974 | 2025-09-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ef969167-28c3-3902-a84a-ef9891c67e1b | -11.62107 | -52.19973 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aaa1dd98-cdfa-3fb1-9699-0786e819fbe5 | -12.71368 | -45.08971 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9fdca67e-a1ee-3488-96a9-e238fe9d97d0 | -12.96838 | -48.07746 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8eb2ad9e-85e8-3954-855c-d37e49ef4dba | -11.65152 | -54.51385 | 2025-09-05 04:57:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f13f254-2729-3a35-b953-fdeb357d80bd | -12.98206 | -54.79339 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87706a86-b848-3d39-86b0-24b1b978b341 | -10.5228 | -57.77777 | 2025-09-05 04:57:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ed1e3e3-7d0c-3b50-b4de-1ade59f48314 | -13.00984 | -45.22694 | 2025-09-05 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2876b8f8-25ce-356e-af50-117d4ddeade3 | -8.51834 | -51.31864 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f837c61-0e1b-3dc7-9832-572d2f602884 | -10.97455 | -45.95071 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c23841a8-8594-3c52-bb26-d944057c4486 | -10.47596 | -53.6413 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7e2d03f6-3016-3633-ba18-846cdc46e70c | -9.70168 | -48.96707 | 2025-09-05 04:57:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fea61fc-04ee-3048-97e1-994fed83121b | -10.47198 | -53.62195 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41296e00-553c-37a3-922a-fb31286d2f18 | -12.97876 | -54.81493 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a3f0d2d8-9526-344c-ae34-922083b8dc4b | -6.4974 | -55.8923 | 2025-09-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5376df3-3c9f-3a27-843b-2043ea1a3ff5 | -8.08786 | -45.33709 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0ee8835-6b71-3464-8b95-3a0479814e87 | -5.90169 | -57.73655 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6efa14eb-2430-3aab-a6ad-09afe93f2b6f | -5.50616 | -60.1303 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b5c76cb7-b991-3dec-a59c-917271f1abe6 | -8.03921 | -52.35688 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66f77a65-e2ce-3401-8981-295d6847a346 | -9.64145 | -47.10667 | 2025-09-05 04:57:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9589b307-8ec3-3276-8854-1ff90dd60db9 | -12.09605 | -44.72676 | 2025-09-05 04:57:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba28f29c-2fef-3b90-92ea-cec633f50f2c | -12.48956 | -48.0872 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1feb3a08-69d6-30ec-b097-dfe1912189d7 | -9.43035 | -46.76766 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f5e4415-458e-3310-b820-7965cade88fd | -8.65578 | -68.7455 | 2025-09-05 04:57:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 068ba6d2-71ac-37b3-996a-bde583d477cc | -5.89797 | -57.73605 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8838bf2c-f63b-395b-b1e5-d9868b95e5ed | -9.78393 | -57.44438 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ac62674d-88a8-3a2e-937d-0d163a2052ce | -11.58976 | -52.18636 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| abfb4f98-2b9c-3d98-8d8d-30953ca3a30e | -7.77608 | -51.08649 | 2025-09-05 04:57:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e9177f04-2352-32fa-b6fb-4dda909ad6f1 | -12.18441 | -53.89039 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c4d591a-5a03-35db-a78f-4d48cf500e8b | -10.09709 | -48.07225 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50a9467f-e347-3cc8-a9d9-dd24df95b3b4 | -12.60395 | -56.99495 | 2025-09-05 04:57:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 86b7121e-d0b1-36f2-afb0-c7d99fe7cb8c | -12.96797 | -54.78035 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b23ba062-a743-3d3f-93cd-ced67652250c | -7.72278 | -50.31236 | 2025-09-05 04:57:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b72a9b4f-108d-3869-9cb0-52f649103037 | -11.59887 | -52.17478 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 357ec3b0-9e09-3f5e-b7f7-f3b08b337e56 | -8.33852 | -52.52896 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c345a787-bf4a-3cb4-ac00-c403a738bc33 | -10.10094 | -48.07836 | 2025-09-05 04:57:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82faceac-e4bd-36f6-b4f1-52a700f7f325 | -11.62456 | -52.20734 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ecfcfea2-38c0-3df7-bdea-0bdb0d4104e1 | -11.20354 | -55.01506 | 2025-09-05 04:57:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71a44fd3-833a-3d27-9c21-af593aab4224 | -5.90096 | -57.74096 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ec9f57d-939c-38ce-977b-0dfa17cd625d | -11.33995 | -50.28733 | 2025-09-05 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 933c1e0e-9e4d-3ca5-ab36-85f92ce47440 | -5.89572 | -57.72674 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e4e952d-b6bc-3acb-a7eb-48e818b50f8a | -8.48107 | -45.08361 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 361d4e77-a3e2-3a9f-8d78-858f6b02af17 | -8.35001 | -52.52295 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7e217aa-ec94-34d7-8ec3-c97c336b9919 | -13.77457 | -52.71279 | 2025-09-05 04:57:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ba7cdbe-52bd-399e-8fa5-db6c648cc12b | -12.99489 | -54.82119 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8a2df17d-286b-3759-acd0-a3fcb8776daf | -12.99434 | -54.82478 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8dde743c-22a3-3811-bdec-8011d3666f79 | -12.99768 | -54.82531 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| f16b713b-715f-3d31-afd7-621e60c4bfac | -11.63358 | -52.22169 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f3731466-0ee5-3e97-a94e-06d0bff4de56 | -5.90454 | -57.71925 | 2025-09-05 04:57:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f204ddf6-2270-3654-a119-ef038ba665a7 | -9.80357 | -48.31125 | 2025-09-05 04:57:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4caafd8-caaa-3172-ba44-bf1b28b661ae | -12.99101 | -54.82424 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89c5374b-b054-37f8-aa0b-e2f03aa43664 | -9.43979 | -46.81 | 2025-09-05 04:57:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d1f15d14-2b0b-3c6b-8d21-07ff8caa1e35 | -6.28268 | -53.43896 | 2025-09-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3ac4b2e-b65e-304a-9854-6576b44ba9ce | -10.97735 | -45.95123 | 2025-09-05 04:57:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 143a8e15-60c7-3121-90fd-7164badb92bc | -8.05763 | -52.37573 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42ecb7ff-1271-3d70-8648-4c8cbd412e43 | -12.50584 | -48.07997 | 2025-09-05 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b55d83da-db3c-3cf9-bff7-010aa7a92c04 | -12.9687 | -54.79127 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eda288ca-7dcd-3c85-a9b0-254719fd8ae5 | -8.20837 | -49.59906 | 2025-09-05 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a0acc4-9215-331d-b498-fe9305e91915 | -12.9832 | -54.8083 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7779d149-a59f-32d1-b423-ca7d23a12357 | -9.50375 | -57.8251 | 2025-09-05 04:57:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cb7e8f9-1fc2-3864-87e6-b4a41b6ac47e | -5.48745 | -60.13565 | 2025-09-05 04:57:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0299b6e8-03fd-3e72-9728-b1eb4d4c1a6c | -8.4816 | -45.07971 | 2025-09-05 04:57:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db22e698-b981-3bea-8ed2-55e99d25a8a2 | -10.15796 | -46.24654 | 2025-09-05 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8dba69a0-9f22-38c4-96f2-99d5a9af03e6 | -12.9843 | -54.80111 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90e41cd9-b80c-39bf-a0b5-42d501769114 | -6.68513 | -49.76714 | 2025-09-05 04:57:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 01582d43-2f74-3f07-83ec-84a6d727b562 | -12.49782 | -53.85365 | 2025-09-05 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf5c7b46-0807-3494-8d8c-c5d7f884ead2 | -10.15754 | -46.24971 | 2025-09-05 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b5dc821d-1dad-3bf8-bbae-4edbcd31b851 | -12.96463 | -54.80191 | 2025-09-05 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ddfa1851-2938-3f94-b411-57f40fc1ff4f | -10.47875 | -53.62301 | 2025-09-05 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4928a11f-1363-317a-948d-19a46cf834bb | -6.86694 | -52.78664 | 2025-09-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README47.md)
