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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a2f8950-ac0c-3948-8d34-3940d924a1a6 | -3.5887 | -52.54475 | 2025-07-30 00:50:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| fb98616b-c87a-3c93-bcad-cff3cc1a4c52 | -2.92512 | -48.67812 | 2025-07-30 00:50:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b950d348-640e-3702-91f0-83ebadb80351 | -3.07955 | -52.92508 | 2025-07-30 00:50:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3d0e96d0-305b-3ad2-930d-6fafee14539c | -2.90522 | -48.24179 | 2025-07-30 00:50:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| a6de0050-a1e1-32e0-b22c-09776bae72c4 | -3.8346 | -48.95976 | 2025-07-30 00:50:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 3e29919f-84a8-3838-867a-0ea257a64248 | -2.90191 | -48.29408 | 2025-07-30 00:50:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0448effa-8024-3713-a4df-4c5a1381663e | -21.327801 | -48.697899 | 2025-07-30 00:51:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69a2f690-01b4-3d8c-baca-7ea1dfe281b3 | -21.3262 | -48.690399 | 2025-07-30 00:51:00 | METOP-C | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1555ef63-97d8-3934-93b0-0d378ef13a61 | -4.6511 | -43.1104 | 2025-07-30 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3946a869-07c2-34f5-9d4f-e548815ddcf8 | -9.1538 | -49.857 | 2025-07-30 01:00:00 | GOES-19 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| abac4ae0-2279-32ed-950b-5e5f81f70159 | -11.4776 | -45.1099 | 2025-07-30 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 58127bcf-c855-3cf2-a6db-cc78f5ebee20 | -10.6172 | -45.2282 | 2025-07-30 01:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 102.1 |
| 968a1f99-e67b-3eff-8d51-0bd699625fbc | -8.5211 | -43.3063 | 2025-07-30 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 47083483-891b-3a09-9520-f015d08ee515 | -9.4383 | -40.3668 | 2025-07-30 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.7 |
| f00de80f-37c7-35e9-8636-d5c6ea090030 | -4.6509 | -43.1337 | 2025-07-30 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 507c1063-ec07-3c13-80c8-b5729d0e1a93 | -9.4387 | -40.3419 | 2025-07-30 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 100.0 |
| b64a9321-9db1-3f84-a0e4-81b30479fddd | -2.9109 | -48.2325 | 2025-07-30 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| c74d95ca-b2de-38e0-9564-c80e82eb5c1f | -11.4584 | -45.1126 | 2025-07-30 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 3b2246aa-326a-3c4b-946f-614eb4abf261 | -11.5503 | -44.2407 | 2025-07-30 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 232f73c8-39d6-3300-a399-efbc1c627e83 | -10.0972 | -46.9656 | 2025-07-30 01:00:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 02f9e0b4-fd57-3004-8945-0554bb243f5b | -17.4939 | -46.7554 | 2025-07-30 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 72.0 |
| a0cbdd9c-6246-3333-878a-0423ad4a3e86 | -10.6169 | -45.2512 | 2025-07-30 01:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c310e190-ed03-345f-b8a4-8f5f16dc92b8 | -2.9108 | -48.254 | 2025-07-30 01:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 98.8 |
| b3d3270d-2089-31ba-a031-8f1e6be624f1 | -17.4945 | -46.7321 | 2025-07-30 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 227.4 |
| ac8bb354-59c4-38fa-b1b5-95cffafd0611 | -17.4745 | -46.7363 | 2025-07-30 01:00:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 727651c9-4ee4-3124-8ad5-c77cbc76f494 | -15.7174 | -41.9272 | 2025-07-30 01:00:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 118.8 |
| 839f3eea-37cd-3c0b-9508-70484c74684b | -11.5307 | -44.267 | 2025-07-30 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 0b984874-f86b-3998-89ba-69b704f634fd | -17.4939 | -46.7554 | 2025-07-30 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| ccb98011-73fc-32fb-8b1b-bf562835f650 | -17.4951 | -46.7089 | 2025-07-30 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 39f25eae-1cfe-3349-8173-e33c11515fb0 | -4.6509 | -43.1337 | 2025-07-30 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 069e6ea1-acec-3149-83ed-61301b30bd08 | -2.9108 | -48.254 | 2025-07-30 01:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 93bbd9ac-8f3c-3e26-bb3e-395e2de81d02 | -11.5499 | -44.2641 | 2025-07-30 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 97893d99-d957-3e8e-a50f-df7ec593fb75 | -11.5503 | -44.2407 | 2025-07-30 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 61f017cd-16be-3212-be99-d5fa40eee386 | -12.4733 | -47.2846 | 2025-07-30 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 35cee4f6-fb4d-364d-98b6-232ade1676aa | -4.6511 | -43.1104 | 2025-07-30 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 57fc660b-0f91-32f4-a8e8-e3e9e87583db | -10.6169 | -45.2512 | 2025-07-30 01:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 3264784f-7829-3049-bebc-350c98b0655c | -12.4737 | -47.2621 | 2025-07-30 01:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 7a705125-78ae-3e10-a0d5-57fb3825aa4a | -11.4776 | -45.1099 | 2025-07-30 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 128.8 |
| 1756727d-dc37-3701-a94e-387d2b4005dd | -17.4945 | -46.7321 | 2025-07-30 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 258.8 |
| b59295b7-47a5-32cc-bd89-b56db98f5a27 | -17.4745 | -46.7363 | 2025-07-30 01:10:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 169.1 |
| 159cba84-2705-3a67-a480-8d56880707f0 | -11.5311 | -44.2436 | 2025-07-30 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 95ee1a51-a451-3e40-9c88-b1fb29c5a100 | -11.4584 | -45.1126 | 2025-07-30 01:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 064d4c04-f848-3557-99bf-a859818f1d64 | -10.6172 | -45.2282 | 2025-07-30 01:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 27504f5b-0b8e-34fc-8524-83a4439e1ed5 | -17.4939 | -46.7554 | 2025-07-30 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 117.9 |
| ef06241d-3126-31f1-9123-669fe13339a3 | -10.6169 | -45.2512 | 2025-07-30 01:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 74.5 |
| ea98f84a-51c2-32cf-b0ed-75c0f0ec858f | -4.6509 | -43.1337 | 2025-07-30 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 9ac8eb20-f85c-376e-ac22-6e632221515b | -11.5307 | -44.267 | 2025-07-30 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| d84e9ff5-72d8-30d2-ae61-2eeb216bd108 | -17.4945 | -46.7321 | 2025-07-30 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 534.8 |
| f0aea906-a2fe-3b12-80de-7315d56b8575 | -11.4776 | -45.1099 | 2025-07-30 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 542c8f80-38ef-36f6-864c-ef413a02d1fb | -10.6172 | -45.2282 | 2025-07-30 01:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c2055044-df12-304d-911c-e9c4dc942679 | -12.4733 | -47.2846 | 2025-07-30 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| ba022dc2-cd6c-30ea-9372-ce5d28cdfea9 | -4.6511 | -43.1104 | 2025-07-30 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| d4d14b0e-b516-3bd7-86b6-9215b7aa491d | -12.4929 | -47.2594 | 2025-07-30 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.4 |
| e82c391f-4b7b-33d4-a9af-d622d0c795ae | -11.4584 | -45.1126 | 2025-07-30 01:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 8efa5397-af10-3cab-a6c8-090243561446 | -2.9108 | -48.254 | 2025-07-30 01:20:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 20e7e173-a9c2-320d-8872-3a207eb35b2f | -17.4951 | -46.7089 | 2025-07-30 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 49d71526-9d06-351f-a0f5-f3369e01c53f | -12.4737 | -47.2621 | 2025-07-30 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 8e50b9f6-4235-3373-90e3-fd2bd390a16f | -17.4745 | -46.7363 | 2025-07-30 01:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 156.4 |
| af85a30a-ff3b-3637-9683-1adad16bed1f | -12.4925 | -47.2818 | 2025-07-30 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 4615fd59-e633-3dfb-aa04-9e5071e5fa04 | -4.6509 | -43.1337 | 2025-07-30 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| a8e5211e-c5ce-31dd-b98f-a02fc53dadfc | -4.6511 | -43.1104 | 2025-07-30 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 41de2eb1-898c-3147-8de3-33e57dc46f00 | -11.4584 | -45.1126 | 2025-07-30 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 38232d63-6049-3253-8838-c13a0917e94b | -12.4929 | -47.2594 | 2025-07-30 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| dde625b7-3356-3e27-bbf1-86f751b666e5 | -12.4737 | -47.2621 | 2025-07-30 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| da68bebb-ffd5-3d1b-bc8d-6a0993376b25 | -10.6172 | -45.2282 | 2025-07-30 01:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 952500f5-f243-32a9-9739-c9be627bf1b3 | -10.6169 | -45.2512 | 2025-07-30 01:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 9b6cac66-f0ab-3d81-9b32-088e3d668638 | -11.4776 | -45.1099 | 2025-07-30 01:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 48b7d9bd-3416-3fea-b980-14662c4b44a7 | -2.9108 | -48.254 | 2025-07-30 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 274d9da6-4a6b-345e-a84a-1070a377e576 | -12.4925 | -47.2818 | 2025-07-30 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 4eaacaaa-8fea-325c-882b-e7ba07204c0c | -12.4733 | -47.2846 | 2025-07-30 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| bb6abd15-c524-3fd2-b2bb-2eebfc193bb4 | -17.9635 | -50.3765 | 2025-07-30 01:40:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 1ecf065c-8bc3-3d59-9a16-d0036f23befe | -10.6169 | -45.2512 | 2025-07-30 01:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 661a5b1f-1c5d-3e2b-9129-a3c035233907 | -17.963 | -50.3987 | 2025-07-30 01:40:00 | GOES-19 | MAURILÂNDIA | GOIÁS | Brasil | 5213004 | 52 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 90289c8c-a3e3-37a3-a8a2-8f22a37b544c | -12.4925 | -47.2818 | 2025-07-30 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 2e13ce92-ebc5-3c9c-806f-92f4d0e78c20 | -17.4951 | -46.7089 | 2025-07-30 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 0703a78a-dc31-39b3-9437-6867859d0dd8 | -4.6511 | -43.1104 | 2025-07-30 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 44cc31f8-e12d-3634-98cb-cb9c2556a035 | -17.5145 | -46.728 | 2025-07-30 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 6538d307-a368-38b3-a2d0-7628b50baa97 | -11.4776 | -45.1099 | 2025-07-30 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 229164dc-29af-3822-9c3f-24f4d548a7a5 | -12.4733 | -47.2846 | 2025-07-30 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 135.3 |
| 5d2000e0-6c11-3ce9-baf6-dce0e27a0724 | -17.4745 | -46.7363 | 2025-07-30 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 95714a3f-7fe2-34f4-97a5-dec015b29178 | -17.4939 | -46.7554 | 2025-07-30 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 5a89e931-4721-3842-9c1f-83c6d10ae719 | -4.6509 | -43.1337 | 2025-07-30 01:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| c77d52e1-6909-30f0-936b-e234d9454b73 | -2.9108 | -48.254 | 2025-07-30 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 1656cad5-592b-3e0b-b17d-9d8a1b1d6080 | -12.4737 | -47.2621 | 2025-07-30 01:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| ae197c1c-5bc9-3cbe-884b-58af51b2a2f8 | -15.7167 | -41.9521 | 2025-07-30 01:40:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 41.3 |
| f39d92f4-6c4e-398f-aa5d-24d5617074cf | -17.4945 | -46.7321 | 2025-07-30 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 294.0 |
| f6f94864-d361-3225-a580-445198614cc6 | -15.7174 | -41.9272 | 2025-07-30 01:40:00 | GOES-19 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.1 |
| 4d900f93-b819-393b-a708-ade6491173f7 | -10.6172 | -45.2282 | 2025-07-30 01:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 7077342a-0752-3df1-97dc-256a0230fa0e | -8.5211 | -43.3063 | 2025-07-30 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 55.4 |
| c3fc6238-f9f8-314b-a45b-25f49656f4db | -11.4584 | -45.1126 | 2025-07-30 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| bbc9d785-7ea0-3e91-a28f-1d90b428fe87 | -6.526 | -56.1923 | 2025-07-30 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 2c15dfa9-b423-3b8c-ab60-bc16a028dec3 | -4.6509 | -43.1337 | 2025-07-30 01:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 8d7533a7-8a80-3372-add5-573cde5882d0 | -12.4733 | -47.2846 | 2025-07-30 01:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 6f86f98c-e3f4-3a11-b7da-c8e417730318 | -6.5075 | -56.1932 | 2025-07-30 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 600a6efc-38e2-31c3-a6a1-e55079d47211 | -10.6169 | -45.2512 | 2025-07-30 01:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a5e9974c-590b-3fad-a354-d58a5e3084eb | -17.4939 | -46.7554 | 2025-07-30 01:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 895aa5be-8d6f-300c-9092-4a67896f2b9d | -8.5211 | -43.3063 | 2025-07-30 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 6af13172-df8d-3a27-97e8-823c4b1bba13 | -2.9108 | -48.254 | 2025-07-30 01:50:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 3b667a8e-3631-3e6a-a670-98ce6232148c | -6.5258 | -56.2121 | 2025-07-30 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 3241f2f3-64b2-3fbd-b9dc-c5cf3988791e | -17.4945 | -46.7321 | 2025-07-30 01:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 178.3 |


[Clique aqui para ver as próximas entradas](README9.md)
