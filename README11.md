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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdde113a-7fd3-3083-aef9-a95df3f1ce4f | -4.27068 | -45.13147 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 80880eaf-37ea-3026-bcf0-4b2f8c7d22a1 | -3.48093 | -43.43234 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 81d9ce88-8deb-3e49-92bf-385dc3517d7d | -3.42206 | -46.96797 | 2025-11-26 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdf78296-c9f7-32d9-859f-7babaa92309a | -4.60146 | -44.41056 | 2025-11-26 03:57:00 | NPP-375D | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 116377ef-b916-33c3-a960-ff8ea8bc4342 | -5.33005 | -43.56459 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ce479d88-2322-3abb-8f8e-5e9b012fd358 | -4.72658 | -46.46395 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f522cf8-80b2-3924-84eb-7fe7acfdb5d1 | -4.28433 | -47.30683 | 2025-11-26 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 829f141b-dafd-302b-8226-ffde1da3728c | -5.3761 | -43.72477 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb8b18a5-e632-3f26-bc96-a2bdf070077b | -8.23469 | -39.97742 | 2025-11-26 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 334a4af1-b963-3216-96ee-7c1541ae1b16 | -3.1466 | -40.17953 | 2025-11-26 03:57:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0509ad62-d3b0-35a8-824e-7c58e5c69925 | -4.57006 | -43.2958 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3596a5dc-c666-3a1f-a93a-616cbf6062c6 | -3.59974 | -38.77811 | 2025-11-26 03:57:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5caf273f-0665-3f29-887c-16211d568320 | -4.25823 | -45.11922 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91f9d578-6c00-3460-b7ed-fe58c0323515 | -4.72095 | -46.46606 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e6c1ce21-7ed9-30bc-a593-7d6357647bc0 | -4.70871 | -43.98864 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebfec9f3-c0a4-3bd6-85b1-817fb3f1608d | -4.61775 | -41.06347 | 2025-11-26 03:57:00 | NPP-375D | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f0bb0399-f9a5-3b43-961e-29b82934cfa1 | -5.03708 | -43.2628 | 2025-11-26 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b402d4e-7be1-3e7a-bfd2-1fcd95931753 | -5.3424 | -40.59816 | 2025-11-26 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e4d13d82-5e7c-38ef-90e5-3bf113d443e4 | -6.30797 | -43.78934 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2b06c452-fc00-32b9-804c-6064e30e253c | -5.21032 | -42.89891 | 2025-11-26 03:57:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 69c4eee4-ba83-3860-b2c8-cc106160ce00 | -3.3604 | -49.50804 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f79de6ff-5fd7-3702-b1c6-d5fb8ac43358 | -3.33223 | -50.27342 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8e419557-7ded-395b-b6d6-ab403e9cfecd | -4.70569 | -43.9968 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b81b901b-46f4-3d3c-919d-543046bd07ec | -6.11124 | -42.95565 | 2025-11-26 03:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 68418c4e-1306-3637-8f20-bbfff2060846 | -5.29028 | -43.6444 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 309de0a4-31b5-3fed-a018-11764dc09fca | -5.48489 | -37.77324 | 2025-11-26 03:57:00 | NPP-375D | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 15a028e8-46c4-34e3-864c-1ac1a2aae8ee | -4.52839 | -46.42689 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c65c600b-5fae-3296-892a-061702118069 | -3.77659 | -38.46861 | 2025-11-26 03:57:00 | NPP-375D | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aa38f5d6-03f2-3600-8a18-ddf6510de98b | -8.08346 | -41.0825 | 2025-11-26 03:57:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7f35e2ac-f3ff-30af-9a11-4c72ea0c6494 | -4.8968 | -42.08367 | 2025-11-26 03:57:00 | NPP-375D | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4eaba854-2e79-35c9-81d0-c8c67f220364 | -3.97842 | -46.02333 | 2025-11-26 03:57:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b6033a3b-4cf5-3cf6-876b-7dfb07e062df | -5.23037 | -45.42605 | 2025-11-26 03:57:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 796e94d5-efa7-3fa6-9d04-16cbd602aff5 | -4.72041 | -46.46914 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e33e860-6dd8-30e8-835d-4229f4a9e8dc | -4.71896 | -46.4632 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ff10dcb-7865-3ded-a09e-9b632da3bb55 | -4.14509 | -42.54514 | 2025-11-26 03:57:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6f64a783-4eb3-3e66-abb1-8500d475afa8 | -6.05125 | -45.83543 | 2025-11-26 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 375ce893-cc04-3b53-b656-bf8bc336aac4 | -4.1639 | -43.71713 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e249a8f5-1fce-3a53-a0da-79207e666410 | -4.56945 | -43.29951 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 436888a9-4bb2-3d52-8a2a-7daea13a9981 | -2.71224 | -45.69766 | 2025-11-26 03:57:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d2788c96-83f3-3ca1-92cb-cdfdbc2b51aa | -6.60535 | -35.23042 | 2025-11-26 03:57:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8e16bee6-cbee-3fa9-9372-876dc8acacdd | -6.30925 | -43.78178 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74770996-2201-35bb-a9b3-814bd43b6d13 | -7.05989 | -38.85752 | 2025-11-26 03:57:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e51e8373-92b8-3aa6-beb7-d133e52d3a23 | -3.51523 | -43.69574 | 2025-11-26 03:57:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5787db82-b1ac-38b9-be48-c13de2c93d4f | -6.30666 | -43.79709 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7ddfee3-02a7-3ba1-89a3-059818027654 | -2.50593 | -47.82414 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67e041ad-9e0d-3bdc-b90c-ece3cce73483 | -4.56241 | -43.29081 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4e9f67b-b39b-3b30-a0e3-b374c409c746 | -7.0157 | -45.17111 | 2025-11-26 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01a65b08-e627-38d8-855d-8286b2788efe | -5.17827 | -35.70744 | 2025-11-26 03:57:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 34989858-770e-3498-a224-1e1b691a286f | -2.55463 | -45.3864 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 103e3a99-6b98-3904-8c79-3adf1efd4d5a | -4.65885 | -43.98482 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c1a0732f-9d8b-3ad9-a946-467cd0b9e4c1 | -4.91101 | -43.79385 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4767d309-5b29-33ee-a7f3-9ba376ff441d | -3.13662 | -49.40914 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c6f32cf-ead9-3f3d-91e8-a2bd4326f067 | -3.59584 | -40.98849 | 2025-11-26 03:57:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b975a66-2bfd-33f9-9874-e730e695404e | -5.28193 | -43.64294 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f50f3e8-6eb6-30e4-addf-09238b557936 | -3.32658 | -50.26654 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d8ad8e7e-7362-3246-9a58-dfabac0e4cc8 | -5.80513 | -35.587 | 2025-11-26 03:57:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 24818d09-b969-352d-b424-d1749d9ab746 | -6.35983 | -43.75953 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3c7a1fc-ba3f-312c-a30e-f7a30233359a | -5.33355 | -43.56913 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 108ca57f-8728-340d-b074-90ee611cfb90 | -5.28674 | -43.63984 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a5921e9-606a-31e9-aa3b-2150b97d0a85 | -3.5929 | -40.98362 | 2025-11-26 03:57:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca56592a-7476-3cc1-b4f5-7dc7c087eb4f | -4.27151 | -45.12648 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| eae434d4-49ff-3ab7-b7a8-5c56a7341b75 | -4.55707 | -43.29744 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 206b2467-cb82-353b-97be-f9ca8a90a492 | -4.11909 | -44.83272 | 2025-11-26 03:57:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53e41d5b-281c-3c91-a1ed-f1cfaaf9dcd4 | -6.87059 | -47.2368 | 2025-11-26 03:57:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b7844a5-0907-394b-8b05-eb8901a4194f | -6.74453 | -39.04983 | 2025-11-26 03:57:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 13626714-9b02-368b-85ab-4e582171cb5a | -2.48136 | -47.82832 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 616fd46a-5332-363f-b7e7-d6c37cb7ad39 | -7.30292 | -45.43871 | 2025-11-26 03:57:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b5771d0d-9c48-3487-852e-b796d7ef57fc | -3.04 | -45.11797 | 2025-11-26 03:57:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82f32108-586f-3ce6-b7e0-825cb161cbc3 | -2.28761 | -47.04081 | 2025-11-26 03:57:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c156739a-9aac-3d98-8612-30c15c84a444 | -6.06472 | -43.25688 | 2025-11-26 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 012bfe59-6ea1-363b-9a90-45362f20bcf1 | -4.82976 | -43.81856 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fdfc7072-2fb1-311a-9c88-aff5bf20fa3d | -4.17542 | -43.72715 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e0173463-ca2b-360c-a060-fbdcecadec02 | -4.37264 | -49.77356 | 2025-11-26 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7c4a43f9-d003-31be-a854-c8c5dfa84849 | -3.96449 | -49.03551 | 2025-11-26 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25dcfa4a-7d51-358d-baa5-bcda56a61694 | -3.67054 | -43.56681 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ef674969-ed37-3973-bfab-93cabfb79aa0 | -7.46491 | -45.18187 | 2025-11-26 03:57:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ef55f6f-3fdc-3c0c-b1da-7cc633ff47e2 | -2.55279 | -45.3974 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bf39f471-6301-32a3-a764-e2bda41bcdcc | -2.99118 | -49.60257 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a474bf73-e601-32e2-9171-0731f64267ae | -3.7552 | -46.16517 | 2025-11-26 03:57:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0128cc66-be12-3f04-ac93-7ad44961538f | -4.17246 | -43.71844 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| bc18b4d9-fa0c-321c-afc6-3e9e22de37b7 | -4.71557 | -47.15637 | 2025-11-26 03:57:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6af178db-9253-38cc-b9af-2f01f1f195ec | -6.06992 | -43.25057 | 2025-11-26 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 216b3036-b174-3cd2-bf45-26813964cca8 | -3.96351 | -49.03654 | 2025-11-26 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3c2dcee-e199-33a9-904a-74514deaa149 | -4.70767 | -43.98466 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fafac6e-89be-3a98-bd87-93dd85951aff | -4.17115 | -43.72644 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 47004859-1a82-3b26-8f30-a4453dc65426 | -4.10204 | -49.07302 | 2025-11-26 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cc323c5-c3cb-354c-86d8-1c1ca064a2be | -2.99222 | -49.59795 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4808f16a-4c15-3c40-98d7-36a284b5e465 | -5.3199 | -44.82847 | 2025-11-26 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d57a0099-2fe9-3e65-9377-9e78b73e366c | -6.73012 | -39.03321 | 2025-11-26 03:57:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 75fbc2c7-f804-3158-ad26-17fceb87dfbe | -6.606 | -35.22616 | 2025-11-26 03:57:00 | NPP-375D | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 07674e8f-5715-3a58-9c14-4c397992c881 | -4.70203 | -43.99203 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2aa0d193-c93f-3245-a82c-fd7d0458baaa | -5.9278 | -38.11983 | 2025-11-26 03:57:00 | NPP-375D | RODOLFO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2411007 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a55bb90b-a2db-3f3f-90ae-1f6a47324860 | -3.92445 | -49.22113 | 2025-11-26 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a5220b27-3859-352f-9810-79c2053d35cb | -6.68657 | -42.47874 | 2025-11-26 03:57:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 968f3530-484a-318c-ba64-eed778965aa7 | -4.56471 | -43.30252 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 14070ac1-059d-3a12-95bb-986a579bc70d | -4.99766 | -40.78782 | 2025-11-26 03:57:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4e2642db-e50a-37a8-b434-55794efb7848 | -4.13768 | -42.92076 | 2025-11-26 03:57:00 | NPP-375D | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca183e96-7f30-3796-8159-43011d836869 | -6.07287 | -39.55051 | 2025-11-26 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8a520a2d-9194-3a58-9cbe-79f9f16e90cc | -3.47309 | -43.42704 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 033b287a-f12f-39be-835c-5f832dbaca9e | -5.06115 | -44.16171 | 2025-11-26 03:57:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README12.md)
