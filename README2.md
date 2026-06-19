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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 453c2b5c-f3c2-305d-9099-dcc853f05d4f | -17.31766 | -43.64996 | 2026-06-19 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2a3f46d9-2ef3-3f17-a7b8-0fd3ea1ea12c | -16.02631 | -43.42845 | 2026-06-19 03:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c6b9376e-7942-3493-a22a-1e6f2da23af9 | -16.01952 | -43.42677 | 2026-06-19 03:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4a00e931-8258-39e7-ba7c-5981543bc26e | -17.3191 | -43.64385 | 2026-06-19 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9fcea765-e66d-36cf-8151-a507b0ae7165 | -16.02102 | -43.42022 | 2026-06-19 03:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d7833f8f-b613-35c4-ac81-368c59f0285f | -17.31732 | -43.64795 | 2026-06-19 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dc1c9eff-8a97-348b-88da-af21ff2da9d1 | -17.31871 | -43.64185 | 2026-06-19 03:23:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 54e4bd05-28a1-393c-afeb-fbd86fc4f808 | -16.02783 | -43.42181 | 2026-06-19 03:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b437efd2-bc2b-3edc-9c17-d3cfbf1f5aa2 | -16.02093 | -43.4197 | 2026-06-19 03:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f01f3c6-d201-310f-8649-2e124ca7f510 | -16.01947 | -43.42625 | 2026-06-19 03:23:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f257ce06-32d0-3752-b5b6-ca935da8f297 | -21.22861 | -44.15188 | 2026-06-19 03:25:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a466ae16-a374-386b-9d9f-5846f3a706a3 | -21.22293 | -44.14907 | 2026-06-19 03:25:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 3845ed76-a0b4-36ce-bc12-250a8bd0bbc9 | -21.22224 | -44.15 | 2026-06-19 03:25:00 | NPP-375D | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2e1759d0-7933-35b1-98d5-3bc9669e192c | -12.8741 | -44.3593 | 2026-06-19 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 138.7 |
| c84668d9-8ec4-3b1e-b1d3-0a788eb1c782 | -12.8736 | -44.3828 | 2026-06-19 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.5 |
| c137420c-a096-311b-a66c-458e776dd697 | -16.0342 | -43.4224 | 2026-06-19 03:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 95dafd36-6694-362f-9038-67eec90d514e | -12.8548 | -44.3625 | 2026-06-19 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| ae24a179-6597-3ef7-a7b8-bc811f096a8c | -12.8736 | -44.3828 | 2026-06-19 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| c896c620-f1f3-3949-97d4-f751c660b02e | -12.8741 | -44.3593 | 2026-06-19 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 61503c7a-ec45-33a1-8479-d942c698e871 | -8.5699 | -45.98641 | 2026-06-19 03:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ab4f8e5b-abb2-3c5e-b4ae-41cc401fb208 | -7.79704 | -46.45757 | 2026-06-19 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a1011a61-ac8a-3c10-87ec-360a97d685ca | -5.16714 | -38.14242 | 2026-06-19 03:40:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a2d3d0e9-0dc8-3891-9da8-124c757576ef | -10.53861 | -47.70873 | 2026-06-19 03:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 63605cae-b516-3517-b851-d929a12726b2 | -7.47702 | -38.95721 | 2026-06-19 03:40:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 265d211c-8ab7-32f6-a51f-021f937d2c4b | -10.90631 | -46.33401 | 2026-06-19 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 110d052b-6be5-396a-b9f4-7504fdceb1e0 | -6.90477 | -42.84265 | 2026-06-19 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d04306d-15c4-356d-a190-69eed70f14f0 | -5.28843 | -43.95595 | 2026-06-19 03:40:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 6589d8f2-1cfb-35fd-87ed-68685bb3b23a | -7.4776 | -38.9537 | 2026-06-19 03:40:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 61448d30-3f5c-35aa-994a-36feb5d341bb | -10.2458 | -47.34142 | 2026-06-19 03:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4e1eb3ec-a7f6-3b3c-8e4d-d3002f2b81cf | -5.52078 | -37.48283 | 2026-06-19 03:40:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d2f20289-3496-37ed-ae89-88be3e854c4b | -5.28771 | -43.96007 | 2026-06-19 03:40:00 | NOAA-20 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 73d5d137-fd9a-38f4-9dfb-d41ca766b74d | -10.2524 | -47.34278 | 2026-06-19 03:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 66cea336-d5ed-3afe-a493-b25faff77b97 | -10.06062 | -48.08945 | 2026-06-19 03:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c7d90f79-6609-323e-b51b-cc755bed48d2 | -6.62952 | -38.73336 | 2026-06-19 03:40:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6b73ac98-c0b7-30f5-bdb3-984e6b2ed123 | -10.53744 | -47.71442 | 2026-06-19 03:40:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1551f537-4ff7-3206-bb74-d286950cdace | -10.25626 | -47.34422 | 2026-06-19 03:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bede0807-1b2f-3d7c-9a50-2b3ed31d2117 | -8.56898 | -45.99131 | 2026-06-19 03:40:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdd0f1d2-2d52-355b-a62a-b7133e38bbe8 | -5.52152 | -37.62207 | 2026-06-19 03:40:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 23193e0e-f7a1-3e85-b1b2-15359fbb8e4f | -6.9089 | -42.84462 | 2026-06-19 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| aa619262-7b5e-3112-8d25-0c4903940e6c | -6.90363 | -42.84364 | 2026-06-19 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8ebb562c-a4eb-3cb6-98ef-3c988caf9c0a | -6.91005 | -42.84365 | 2026-06-19 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e96428d-56be-3e19-9ac9-10bd7b700aed | -7.7301 | -42.66584 | 2026-06-19 03:40:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ee633305-2fc0-3a32-9c1e-0cb44f9971d4 | -10.05244 | -48.09426 | 2026-06-19 03:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 62e04a8f-09ee-3cbf-8cde-f14a5302df6a | -10.05917 | -48.09657 | 2026-06-19 03:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 89f6a41e-8bd9-3b0d-96dd-886c5650ad0a | -6.90946 | -42.84704 | 2026-06-19 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 17b2f1c8-f67f-3967-a450-8444fbb08780 | -5.61015 | -37.5284 | 2026-06-19 03:40:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 111eabe3-3b60-3f79-b61c-de831b4cccfb | -10.91102 | -46.33639 | 2026-06-19 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a99440d-6722-3481-98da-4d6fd0e176ed | -10.8436 | -41.95144 | 2026-06-19 03:40:00 | NOAA-20 | JUSSARA | BAHIA | Brasil | 2918506 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 589ef129-3cd8-37dc-ba2c-e62c52bd3c1f | -6.6347 | -38.72705 | 2026-06-19 03:40:00 | NOAA-20 | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3a9c91bf-d565-348d-aa4b-2cd2dc70ed88 | -9.6801 | -47.04086 | 2026-06-19 03:40:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1cf630b-77b5-38f9-b569-f089c4e66199 | -10.90533 | -46.33906 | 2026-06-19 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 544cd3f2-7943-3075-b9ed-8c1d3e2abcad | -5.03844 | -39.86012 | 2026-06-19 03:40:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dfa698a2-42a4-36d5-b7d3-9d97c163b99a | -6.72623 | -39.27616 | 2026-06-19 03:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 432fdfcf-6107-3761-861e-090f78ff1446 | -10.90479 | -46.33558 | 2026-06-19 03:40:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| af4c9366-a612-35ac-a95e-ddba1b336e42 | -5.52002 | -37.48743 | 2026-06-19 03:40:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 7a218eff-0adb-3d40-b5a4-75f78d4b9c6d | -6.90419 | -42.846 | 2026-06-19 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 71746025-18d2-37cf-8fb0-3302ce0d291c | -10.0509 | -48.10188 | 2026-06-19 03:40:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aab369eb-4faa-3930-b8ec-1c082e49162c | -7.47781 | -38.95709 | 2026-06-19 03:40:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 621cbb18-3eb3-33f1-b26f-627b72bfaf35 | -6.64578 | -43.91608 | 2026-06-19 03:40:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3efd6bb4-933e-3367-a910-2eca3ccdfa13 | -10.6428 | -36.97223 | 2026-06-19 03:40:00 | NOAA-20 | CARMÓPOLIS | SERGIPE | Brasil | 2801504 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 484691a6-a3ab-3d89-b6c5-9ffa1f49c752 | -7.79816 | -46.45173 | 2026-06-19 03:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 59fe9d72-1f7e-355d-b190-dffc598b6c8a | -10.24966 | -47.34283 | 2026-06-19 03:40:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 686c0635-144e-305a-8047-deecf58895ac | -12.87279 | -44.36091 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8c79c320-904a-3ab1-b14a-b862da30af9c | -12.49519 | -43.76581 | 2026-06-19 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d4f3eccf-6e94-3137-8881-5116759faa3e | -11.54665 | -48.26501 | 2026-06-19 03:42:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 502b1e67-490b-37c9-a138-c0c6c75d81dd | -12.78459 | -44.50347 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fee7d805-e82d-3dd3-b1ff-8cc3bd1c5a2a | -12.77861 | -44.5058 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25eb3e25-9f61-39eb-9912-6dcb47acefc4 | -12.87023 | -44.37419 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| c5d1a2d0-e32a-3628-aa04-2c2cb342196c | -16.02811 | -43.42855 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| d47cdc8b-4698-3bed-8a5e-bf63390f0d8e | -12.13815 | -48.27206 | 2026-06-19 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28aa2346-9448-36f4-8142-41446eac12e9 | -16.03007 | -43.41821 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5246997e-f010-332b-9f0a-8133947ac97f | -12.13146 | -48.27038 | 2026-06-19 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4bf7b98f-56d5-32e2-8e8a-955ab40d1d41 | -12.44981 | -44.75227 | 2026-06-19 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f65a5d89-0866-3e25-89d4-58429bc557cb | -12.77453 | -44.52641 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a070b99-4972-3d81-ba8d-2d0b16d9f057 | -16.02909 | -43.42337 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2b41fdd5-9acd-3e0d-918d-502ac6923a33 | -12.49967 | -43.76994 | 2026-06-19 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 963c1d4f-71ec-3464-913f-3dfa9f4d557c | -16.02443 | -43.4224 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.3 |
| af15d817-e7c2-3e8c-8112-ae89ca44a339 | -12.83347 | -44.3666 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c896c79-2064-3ef8-8102-eb6869328eb1 | -12.49908 | -43.773 | 2026-06-19 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| fafc276b-5a99-3d80-a4de-72480cd5a176 | -17.32033 | -43.63792 | 2026-06-19 03:42:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 59841d6a-4949-32fa-bf09-06e68a7cb42b | -12.87151 | -44.36756 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce6b554d-202e-3af6-816a-f5b22841a902 | -12.77384 | -44.52988 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15d8fea4-8fee-3d0f-8853-435e10c65a0a | -12.8761 | -44.37203 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.9 |
| d35ae1ff-abf0-36c3-8273-52b5bde625ef | -16.02169 | -43.42229 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6c29a827-a648-3ee6-b49c-78413f9cab22 | -12.87674 | -44.36872 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd468c4e-7879-3dc3-8c79-a4aa4137da27 | -12.85974 | -44.37196 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 0ff02c9a-a931-3523-93df-501a96115964 | -16.02737 | -43.41811 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| ec56e77d-f325-303a-a2da-06423950a783 | -12.86884 | -44.35311 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 03c1ff4b-63c5-3073-bb28-7e52f5d6a494 | -16.02271 | -43.41718 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1b9ee25b-6662-3536-a488-6d19f2e56a3c | -12.49578 | -43.76274 | 2026-06-19 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a82b7aaf-7992-31f6-9f08-237c80a7bcd4 | -12.13417 | -48.26655 | 2026-06-19 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4309895a-1c49-3264-a6cd-e0bf67560dff | -12.28666 | -42.66447 | 2026-06-19 03:42:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c70b515-e056-3934-8bf1-1324bfb92944 | -12.13552 | -48.26022 | 2026-06-19 03:42:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cd1af4a9-6581-3deb-b693-2a98dbb41a1b | -12.87343 | -44.35759 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d702d944-d3c1-328f-90fe-d46f05bb1d0c | -12.86959 | -44.37752 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| cb555fb4-5d5b-3a10-a758-65a6bbbc35ec | -16.02635 | -43.42326 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 3f665592-a500-33a7-809b-1c22445dec16 | -12.86434 | -44.37639 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 17ef4bc5-b262-387c-8149-e1b063ce6881 | -12.86038 | -44.36863 | 2026-06-19 03:42:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 4ece41fc-6033-3281-8285-b8215673b6dd | -16.02541 | -43.41725 | 2026-06-19 03:42:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bbdd4c3b-0ff9-3203-b569-f1daef97a06a | -10.98701 | -47.75207 | 2026-06-19 03:42:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README3.md)
