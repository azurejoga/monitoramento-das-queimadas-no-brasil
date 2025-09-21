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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e43b68a-6c46-31f9-b248-81c2ebaaf289 | -12.2794 | -45.2679 | 2025-09-21 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 9657df00-de98-36a1-bdf7-1b2b2f362162 | -10.6741 | -46.4477 | 2025-09-21 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d22fed5b-d16f-30f5-ae46-d6b0c0264281 | -23.1523 | -47.6245 | 2025-09-21 13:30:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 221.1 |
| 81ff1e5c-3566-33c8-94ea-6f693f4bfd9e | -12.3399 | -44.0946 | 2025-09-21 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 347.2 |
| f2c268aa-6eab-38dc-9b1a-d4656d202e16 | -12.2987 | -45.2649 | 2025-09-21 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 106.7 |
| df0c7be0-8054-385f-8d00-465c259f0b19 | -12.1156 | -44.7839 | 2025-09-21 13:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 8b3c5453-eeef-3a3c-9c98-570709c15512 | -23.3989 | -49.1191 | 2025-09-21 13:30:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 395.6 |
| c54ab52b-c6ea-3767-902c-55259015f05a | -12.8781 | -50.5207 | 2025-09-21 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| e3ea062c-b174-3a42-8236-76c6fcab2cbd | -12.711 | -46.868 | 2025-09-21 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 3c72231b-78b5-3dcf-835f-13947748c17f | -8.3082 | -43.6813 | 2025-09-21 13:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| d68076f8-e689-3074-b53e-cc803a1cfb84 | -14.502 | -45.2683 | 2025-09-21 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| e905453f-2a76-3c96-bbe3-cc36958924ff | -10.6932 | -46.4453 | 2025-09-21 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 28d4afa0-1211-3a50-a773-d7454f5aff6b | -14.7877 | -51.3836 | 2025-09-21 13:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| a4a8d3c5-3cc9-3758-87cd-58fa9fdc8e33 | -12.0767 | -44.8131 | 2025-09-21 13:30:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| c8f141e3-faca-3ca7-9746-d693e47790fd | -5.5771 | -42.1493 | 2025-09-21 13:30:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 129.4 |
| 44e48ec5-c65c-3610-abb3-3a0bde06050f | -12.6088 | -45.1244 | 2025-09-21 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 321.6 |
| 8502e061-ce69-3cc3-b40d-e77413439595 | -23.3981 | -49.1427 | 2025-09-21 13:30:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 307.6 |
| 93d7d855-ce05-3f19-b367-b0e5626474b4 | -14.8479 | -45.4846 | 2025-09-21 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 308.8 |
| 26c06b93-95b6-3f27-8f4c-877045b29a80 | -10.2994 | -46.1109 | 2025-09-21 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e3c7994b-379b-307e-be01-4135dfb34fb6 | -3.8663 | -43.0854 | 2025-09-21 13:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 119.1 |
| ac6bb9bf-d512-321b-9144-301138cb5d04 | -17.1173 | -45.9491 | 2025-09-21 13:30:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 97.8 |
| b2162491-c27c-327c-b17a-1841501c4045 | -12.2794 | -45.2679 | 2025-09-21 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| c90f2655-89fa-3620-aacc-3555f5e7ddca | -14.5107 | -44.8695 | 2025-09-21 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 575893b0-c02a-32aa-a4d0-8e6356ae004d | -6.8192 | -43.7599 | 2025-09-21 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| b9eb8be9-daec-3c3e-9d53-52589f0634ba | -7.714 | -44.4612 | 2025-09-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 320.1 |
| b962bc2c-277b-3367-bfec-2364cbba5c4d | -5.5773 | -42.1255 | 2025-09-21 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 6d85c608-9276-3c01-9f0e-29e74c5d85c3 | -12.711 | -46.868 | 2025-09-21 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 5437b2cf-ba19-3bc9-8c93-574422fb8dbe | -6.704 | -44.0017 | 2025-09-21 13:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 056f27e0-70ff-35e5-9f9a-933973ffbde7 | -14.8479 | -45.4846 | 2025-09-21 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| c175790d-e4d7-3461-ae71-f77bd4a225fb | -14.5302 | -44.8659 | 2025-09-21 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 746d1ae4-07ee-3842-932b-c722c306b4d7 | -12.8589 | -50.5231 | 2025-09-21 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 325dc87f-c55e-326b-9f2f-51f795c2f473 | -7.966 | -43.8809 | 2025-09-21 13:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 9ee5ea57-ab6a-3d3b-8228-da2006d96456 | -23.3981 | -49.1427 | 2025-09-21 13:40:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 298.7 |
| 57d4d27c-98ec-35ee-9915-d60c17b1504a | -15.8829 | -47.2973 | 2025-09-21 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 76.8 |
| a3c143d6-fad9-3bdf-b01a-accbb018eef8 | -11.585 | -50.2902 | 2025-09-21 13:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 2f1b5cf4-0da2-3f5c-9b9f-513ff9737069 | -12.6921 | -46.8482 | 2025-09-21 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 0ed34e5e-a167-388f-9e31-38427974afaa | -12.7341 | -47.7168 | 2025-09-21 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4e041e90-e35c-3a5f-a403-14fe641dadfb | -7.5272 | -44.3413 | 2025-09-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| e63ff1bc-f7d5-30d8-8c11-55ca2ff8e8ac | -6.9308 | -43.8658 | 2025-09-21 13:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 34e6c320-46a4-389d-8eed-d0606a888bad | -10.6932 | -46.4453 | 2025-09-21 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 55b74139-9b44-3ce8-bb44-1df06b3ff638 | -12.6093 | -45.1012 | 2025-09-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 83ac81fe-3e9a-3527-9a54-01aa96b8c2e4 | -10.2998 | -46.0882 | 2025-09-21 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| cfa42f4d-909e-38a6-8100-2f58c8520020 | -12.2987 | -45.2649 | 2025-09-21 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 8729d745-542b-36c0-845a-b83ea789b1dc | -12.8781 | -50.5207 | 2025-09-21 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| b0248ee8-30dd-390c-b396-ba14389f175f | -14.8675 | -45.481 | 2025-09-21 13:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 06b159f1-8ba9-364b-9507-5505651d50d0 | -5.5771 | -42.1493 | 2025-09-21 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 111.9 |
| 6b935904-50a4-372c-96d1-01bc9eaeb641 | -7.62 | -44.4474 | 2025-09-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 6bab1442-1981-3a88-a865-029b553a915f | -12.1353 | -44.7576 | 2025-09-21 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| fb86d431-add9-3e9a-8a80-4747f4a179a1 | -16.0011 | -47.2757 | 2025-09-21 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 9a964c74-e7cf-3e09-bfbd-0bb152d6bb72 | -12.1156 | -44.7839 | 2025-09-21 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| e428e994-91d9-336f-83de-649f49a437b6 | -11.6438 | -46.5684 | 2025-09-21 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| ff7667f1-f687-3f57-a4bd-7719cc9164e9 | -10.0321 | -46.2335 | 2025-09-21 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 31c26dde-7f92-38bb-a75c-86a7747ae3e7 | -5.5959 | -42.1478 | 2025-09-21 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 142.0 |
| 0c3041db-b54e-3e44-ada0-f79555f38af9 | -12.7302 | -46.8651 | 2025-09-21 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 2a81480c-dc91-375f-8cf0-8d40c9295604 | -8.3082 | -43.6813 | 2025-09-21 13:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 97d7f992-90ba-3343-81ed-a6fb9b3baf30 | -5.5583 | -42.1507 | 2025-09-21 13:40:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 103.1 |
| 9c549c11-8fa6-3b58-a76e-2f571bf6a1de | -10.8805 | -46.6241 | 2025-09-21 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 6eac5cd8-dec4-3fc2-bf51-e710c8604720 | -12.6088 | -45.1244 | 2025-09-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 221.2 |
| 825e2137-fdef-3a09-b18b-806a1875d308 | -14.6241 | -49.7595 | 2025-09-21 13:40:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 118.2 |
| b46f946d-d3a2-3c42-b866-a3d14ff99e84 | -12.1344 | -44.8042 | 2025-09-21 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| cd65fb3b-ed67-3c8e-b126-f6738ac3becb | -10.2808 | -46.0906 | 2025-09-21 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 107453f1-0936-37cc-b760-f9f110e0e577 | -11.2306 | -46.1722 | 2025-09-21 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 92918c88-91a3-32f0-9597-09fa7dd9b66c | -3.8663 | -43.0854 | 2025-09-21 13:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 5b6c7f4b-c852-3b92-8a8b-e29ce095de6e | -12.8777 | -50.5422 | 2025-09-21 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| e7e295ed-7665-34fb-ba45-4804c34557bf | -12.3399 | -44.0946 | 2025-09-21 13:40:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| dc474034-e66e-3391-b02d-5cc09615a808 | -12.9157 | -50.5589 | 2025-09-21 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 358b7d86-7e33-3d32-9a72-917faf09825e | -7.5275 | -44.3182 | 2025-09-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 93.1 |
| db83b5cf-863c-30c1-89bc-03c0602e70e4 | -12.0767 | -44.8131 | 2025-09-21 13:40:00 | GOES-19 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 96.6 |
| f44e6b43-9f58-3f7a-8853-61a2e9a5d4ca | -23.1523 | -47.6245 | 2025-09-21 13:40:00 | GOES-19 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 266.3 |
| f097eafd-479d-3e29-a8d3-61ba41fcae89 | -14.6047 | -49.7624 | 2025-09-21 13:40:00 | GOES-19 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3d3fcd05-8a3b-30e1-a1f5-11fafa6a92ec | -20.8809 | -49.6179 | 2025-09-21 13:40:00 | GOES-19 | JACI | SÃO PAULO | Brasil | 3524501 | 35 | 33 | nan | nan | nan | Mata Atlântica | 138.2 |
| 9064f2b0-0e9f-3768-a21a-af4c4eb14daf | -8.6076 | -45.3302 | 2025-09-21 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 76e1de5f-27aa-3134-bb9a-955aa11ceb51 | -12.2983 | -45.2881 | 2025-09-21 13:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 183.6 |
| a21f6c02-5047-3e34-b345-73e2d95c6009 | -11.6927 | -42.7518 | 2025-09-21 13:40:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 07fee33e-bd9f-39ed-8c01-c1cbc0e99ee5 | -12.7114 | -46.8454 | 2025-09-21 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 187.4 |
| 5db6437b-0478-31b6-b40e-c9e3846ddbaa | -2.9528 | -42.8938 | 2025-09-21 13:40:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 51e87fc8-2dc5-3f81-a035-aea0e9774257 | -14.8479 | -45.4846 | 2025-09-21 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 65348873-92c5-34ef-bc1c-5f96168d2b20 | -12.8777 | -50.5422 | 2025-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 8914311f-d763-3a07-9c2e-0a39fdee8258 | -12.2987 | -45.2649 | 2025-09-21 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 176.3 |
| a60a431b-57f7-3ebe-a4ae-dfce062aec66 | -7.5272 | -44.3413 | 2025-09-21 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 2069f1d2-0c1f-331f-8d0c-1b94b79c4080 | -7.6007 | -44.4952 | 2025-09-21 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 99d0b306-eec4-382b-8324-151b2b1d8cd4 | -10.2808 | -46.0906 | 2025-09-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 3d935ef2-9c2e-3588-a543-7b8ee22b5181 | -5.5773 | -42.1255 | 2025-09-21 13:50:00 | GOES-19 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 82.3 |
| f7e59d4f-5c00-3b7f-994f-afc5fb96d81b | -12.1156 | -44.7839 | 2025-09-21 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 591e9bea-7f97-3a29-8db0-162b52093450 | -10.0128 | -46.2583 | 2025-09-21 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 74de0605-cdee-32bc-8f29-fde86cdebd17 | -10.617 | -46.4549 | 2025-09-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| feb81c78-6869-3ce6-8534-a7843ef83697 | -11.2306 | -46.1722 | 2025-09-21 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.4 |
| 5b977e15-620c-3db1-b063-2c09a2041b20 | -10.8805 | -46.6241 | 2025-09-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 196.1 |
| 1be3dbac-2407-3a44-8741-4aa00bd0f41b | -17.1173 | -45.9491 | 2025-09-21 13:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 0c0a1115-edaf-3ddb-8eb5-85d580cc0069 | -14.8675 | -45.481 | 2025-09-21 13:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 41972465-df9b-3baa-885f-b98e277b4cab | -15.9586 | -59.4288 | 2025-09-21 13:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 8928a0b9-08a0-3fce-859b-b64ba69f9ec3 | -10.7746 | -47.3303 | 2025-09-21 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 29a28c2d-79a6-3c79-85a1-6c1ca1c0add9 | -12.8969 | -50.5398 | 2025-09-21 13:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 249dc9e4-dfd1-3905-8cf5-bf445b0cfe17 | -12.7114 | -46.8454 | 2025-09-21 13:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 182.8 |
| 212bf4e1-eef5-3946-8fae-2260824dafdc | -2.9528 | -42.8938 | 2025-09-21 13:50:00 | GOES-19 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| cb015e1f-3d65-30bc-aa9d-37590c8f39b4 | -7.714 | -44.4612 | 2025-09-21 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 346.1 |
| 7c68ec33-e4c9-3932-b942-dd472f06d475 | -23.3981 | -49.1427 | 2025-09-21 13:50:00 | GOES-19 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 160.5 |
| b746f8a2-578f-3b88-83f8-19e2b78e90b8 | -12.1344 | -44.8042 | 2025-09-21 13:50:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 79bac839-fa42-3881-8f65-37ebc533756e | -12.7153 | -47.6972 | 2025-09-21 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| ed12c981-a64e-3a87-b81c-673ea4146769 | -10.598 | -46.4573 | 2025-09-21 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |


[Clique aqui para ver as próximas entradas](README53.md)
