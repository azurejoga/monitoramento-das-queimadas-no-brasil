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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 178dda7e-e0c6-3b18-8f13-28020e6339b0 | -3.3096 | -50.1781 | 2024-10-11 00:25:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e45f85c4-5c85-3858-8223-303a36fc6ca2 | -3.614 | -44.7783 | 2024-10-11 00:25:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 9af05e8a-9ad5-3e66-b61e-e835aefd277a | -4.0962 | -48.2523 | 2024-10-11 00:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 4eb4e69b-ce2e-3581-b835-44407780c1ae | -4.1148 | -48.2515 | 2024-10-11 00:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 0a4ea3f9-b35b-3151-b640-d55b273886a7 | -4.1149 | -48.2299 | 2024-10-11 00:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 25c75ab5-de66-3c14-b18e-c177d48dc3b9 | -5.1539 | -48.2859 | 2024-10-11 00:25:35 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 5d55e2d3-c47e-3b6e-b962-6dfc3f941e98 | -5.1724 | -48.3064 | 2024-10-11 00:25:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 22dbfad1-2add-365f-8454-c861125e6a6b | -5.1725 | -48.2848 | 2024-10-11 00:25:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 215.0 |
| 6a04a755-86b3-3ac6-843a-1290e5a69f3d | -5.1727 | -48.2632 | 2024-10-11 00:25:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 305d6e88-36ec-37a8-bec8-5be1326169fe | -5.3449 | -60.1233 | 2024-10-11 00:25:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 28e601c9-54ca-3811-bdae-6e21c4ae3c55 | -6.1301 | -47.2664 | 2024-10-11 00:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7c8fb650-3e6c-39f3-9a98-ea072dbcf237 | -6.5404 | -60.0259 | 2024-10-11 00:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| cb51bc7f-848a-3f00-b570-434417712b6d | -6.5589 | -60.0252 | 2024-10-11 00:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6c7e6858-e062-3328-9d4d-71361e542a78 | -6.747 | -59.3259 | 2024-10-11 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 59a150b5-a16a-3523-aec4-d73b4b47df27 | -6.7654 | -59.3252 | 2024-10-11 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 07c82166-dfba-3606-9861-f69519540d13 | -6.8006 | -59.6319 | 2024-10-11 00:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.0 |
| fb205693-567e-327b-aa80-1fff5db673ee | -7.0786 | -59.4087 | 2024-10-11 00:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| b58d2db1-7a9c-32fd-8f47-6f353515b3ea | -8.4231 | -55.4704 | 2024-10-11 00:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 589f68e1-03b6-32ae-b6db-fb0d55213275 | -8.4417 | -55.4692 | 2024-10-11 00:25:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 8d5dd82c-f0f2-3826-bfea-def9504233a9 | -9.4685 | -47.3025 | 2024-10-11 00:26:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a48a649d-65f8-39c4-9291-ae04ab57c661 | -9.4688 | -47.2803 | 2024-10-11 00:26:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 7729cda1-20a2-319e-a3bd-f4c200cb3cca | -10.363 | -55.8755 | 2024-10-11 00:26:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 95177d6c-373e-3a5d-b0fa-fc12ea8976f9 | -10.3632 | -55.8554 | 2024-10-11 00:26:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| de88729d-853a-384c-bae0-ed017735f24a | -10.382 | -55.854 | 2024-10-11 00:26:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 233e7e5d-fe07-3200-8c93-d1bb1255a38d | -10.6171 | -47.704 | 2024-10-11 00:26:06 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 0ec8f3a1-495d-3a7c-80ad-7711bf68c857 | -10.6962 | -53.0354 | 2024-10-11 00:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 19b192b3-5781-3604-b15e-7b6000de76e0 | -10.6965 | -53.0147 | 2024-10-11 00:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 166.0 |
| e661fbcd-f220-35a8-ad3d-917fb75644f9 | -10.7151 | -53.0337 | 2024-10-11 00:26:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 299f1d7d-21cf-3a93-a9cb-58eb83d270f4 | -10.7059 | -64.1138 | 2024-10-11 00:26:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| f21ba435-116d-39d8-9a68-5ee6ffa61991 | -11.2526 | -50.9675 | 2024-10-11 00:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 7d986751-9123-3cb9-bf59-f1d8572789a3 | -11.2407 | -53.2738 | 2024-10-11 00:26:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 9dab1bf2-1774-3690-8049-e8b0b2648046 | -11.241 | -53.2531 | 2024-10-11 00:26:10 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 76a06628-0bca-361e-9479-33aae31cde4c | -11.2716 | -50.9654 | 2024-10-11 00:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 19fd9983-3164-366b-98b7-0b062379fc18 | -11.2597 | -53.272 | 2024-10-11 00:26:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| cd2f18ec-2de8-3a33-af40-985042bf2fcc | -11.2599 | -53.2513 | 2024-10-11 00:26:10 | GOES-16 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 7f074806-d6d4-3deb-b798-0fc96543a308 | -11.2859 | -51.3031 | 2024-10-11 00:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| d6436fb2-bed7-35ab-a4c6-8ea85b3d8f95 | -11.2909 | -50.9421 | 2024-10-11 00:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| af10ad47-a4e3-31b6-b1b2-3cb4cf26962d | -11.3048 | -51.3011 | 2024-10-11 00:26:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 867cc51e-ceff-39fa-9cd5-7d0beced9d75 | -12.3171 | -45.3083 | 2024-10-11 00:26:15 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 05d681e4-1a60-3e3f-b490-7b0ae247d568 | -12.3463 | -43.7638 | 2024-10-11 00:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| d199a722-f794-372e-86fa-232e1f19b39e | -12.3467 | -43.7401 | 2024-10-11 00:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 493d1ce4-3cbd-38bd-8de6-769422421ab3 | -12.3656 | -43.7606 | 2024-10-11 00:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 59f26bfc-5956-3b50-9e06-db729bca4795 | -12.366 | -43.7369 | 2024-10-11 00:26:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 407fb288-1b5b-3674-b285-093c432a6397 | -12.4563 | -53.1503 | 2024-10-11 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 230.8 |
| 325546a6-4fda-33d1-b3ae-220b666d8a84 | -12.4566 | -53.1294 | 2024-10-11 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 303.0 |
| 0cc0f207-99b7-3318-9d16-22069b3193f2 | -12.4754 | -53.1482 | 2024-10-11 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 863295bc-bfd5-372e-a104-571a628fee0e | -12.4757 | -53.1274 | 2024-10-11 00:26:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 130.4 |
| aaa3952f-45ca-3a05-afa3-4ad1f4d2456c | -12.7673 | -44.8904 | 2024-10-11 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 4081f108-d322-3a6c-999a-260ae5e8a728 | -12.7678 | -44.8671 | 2024-10-11 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.7 |
| 573e6055-de9d-3a66-a373-8e5a0e20557e | -12.7866 | -44.8873 | 2024-10-11 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 232.1 |
| aa1a2513-2d23-3cdd-a67a-fa1b0332677e | -12.7871 | -44.8639 | 2024-10-11 00:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 269.9 |
| b4ac4fda-1b49-301c-962a-7f44d0b52d88 | -12.9661 | -53.4902 | 2024-10-11 00:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 12661e5a-cef7-3908-bbc3-d1b8d1c9706e | -12.9664 | -53.4694 | 2024-10-11 00:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| f448d126-af55-3df4-a138-d5951960a908 | -12.9852 | -53.4881 | 2024-10-11 00:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 2c9fe837-e552-3c74-a04c-5a059013a86e | -12.9855 | -53.4673 | 2024-10-11 00:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 113.1 |
| c5a61ba1-03c7-363e-bc51-f79fe33fb07f | -12.9858 | -53.4465 | 2024-10-11 00:26:20 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 173a90fd-db80-32ac-909e-1da1891b2f94 | -13.7346 | -60.6079 | 2024-10-11 00:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| d3a3bc33-f21d-34eb-b92b-a87bac5cd781 | -15.429 | -60.0156 | 2024-10-11 00:26:34 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 3f3d58cf-c14b-3226-9165-d938c8e5fff9 | -2.6533 | -53.3506 | 2024-10-11 00:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 1b5cef61-6518-365b-a8b2-8d1248ae9185 | -2.6716 | -53.3502 | 2024-10-11 00:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| eae2f2ac-88bf-331f-9362-e3f4495631ff | -2.7663 | -52.4937 | 2024-10-11 00:35:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| a35eeded-e38d-3f19-831c-27a233eef419 | -2.7664 | -52.4733 | 2024-10-11 00:35:22 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| be877802-28bf-3b0f-8989-83d8452f2345 | -2.7847 | -52.4933 | 2024-10-11 00:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 276.6 |
| 57dacba2-f2e2-339a-883d-ba4794114c05 | -2.7848 | -52.4728 | 2024-10-11 00:35:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 208.0 |
| b43e23da-070c-34ba-bb5f-d73734c35cfe | -2.8081 | -51.0084 | 2024-10-11 00:35:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| a9593832-d49d-3b4e-9a97-12673b1b3580 | -2.9674 | -47.9931 | 2024-10-11 00:35:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 385eb18d-c4c6-32c4-ac70-a486cce2220a | -2.9673 | -52.9169 | 2024-10-11 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 8ff58b2e-c1aa-33bb-a1f4-19cb08e6a4d2 | -2.9673 | -52.8966 | 2024-10-11 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 161.0 |
| ab7e4f9f-7cee-317e-80af-997a9137530a | -2.9728 | -51.3568 | 2024-10-11 00:35:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| abd37f44-a790-3638-984b-4d5eae8f3808 | -2.9857 | -52.9164 | 2024-10-11 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 180.7 |
| cf27d364-3b32-376e-9664-ecee93f6abd5 | -2.9857 | -52.8961 | 2024-10-11 00:35:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 214.9 |
| 0d824e8f-28fc-3aa0-bbd8-5b482762acc2 | -3.0343 | -61.6918 | 2024-10-11 00:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 3ec7f5dd-6ca9-3cab-8542-e74123b6c95c | -3.0343 | -61.673 | 2024-10-11 00:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 79e7a6c7-9bfc-3485-89f3-b251ffe5d0eb | -3.0525 | -61.6916 | 2024-10-11 00:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 0aaf83a8-32a4-3ce1-92ac-79ee9e1ae935 | -3.0525 | -61.6727 | 2024-10-11 00:35:24 | GOES-16 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| ac975e48-4b44-3a48-8570-ff8af77601d8 | -3.1423 | -50.4352 | 2024-10-11 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 473a2a5c-3f73-3bdf-b327-30122708609b | -3.1607 | -50.4556 | 2024-10-11 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| e52c3d4d-9fd6-3774-ad20-f81ccfde5fff | -3.1608 | -50.4347 | 2024-10-11 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| b20f1d7e-eb21-3c9e-bcd0-af0ce1196049 | -3.2912 | -46.0731 | 2024-10-11 00:35:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 99d64f3b-740a-3665-8e2a-7785b8fca516 | -3.3097 | -46.0946 | 2024-10-11 00:35:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6ec8380b-0348-314b-b8e8-a0baee0a0eb3 | -3.3098 | -46.0724 | 2024-10-11 00:35:25 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 96.9 |
| bed170e9-d53a-356b-b11e-aca6ab1095f8 | -3.3096 | -50.1781 | 2024-10-11 00:35:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d9b89746-34e3-36c9-abf1-4ae4b26b0f1b | -3.614 | -44.7783 | 2024-10-11 00:35:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 92b44916-790a-349a-b4b2-0cb5af31e122 | -4.0962 | -48.2523 | 2024-10-11 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 0058fb4b-6286-32ba-8a71-fb2420c10bd9 | -4.0963 | -48.2307 | 2024-10-11 00:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 755090b7-d4c1-3494-b751-e2fdf94170bd | -4.1146 | -48.2731 | 2024-10-11 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 0ba8fbfb-34dd-3ee0-96ed-ab09d0a7d4ef | -4.1148 | -48.2515 | 2024-10-11 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 240.6 |
| 9cfb9f67-18b4-3472-97b6-37e89f46f277 | -4.1149 | -48.2299 | 2024-10-11 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 4d859c09-1076-3fbd-9b31-864dec72f1a9 | -5.1725 | -48.2848 | 2024-10-11 00:35:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 119.5 |
| ccce1e05-94a6-310a-ac5c-2574012655b3 | -5.1727 | -48.2632 | 2024-10-11 00:35:36 | GOES-16 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 288097bf-83c7-3e71-8a45-115b00b9d6c0 | -5.3264 | -60.143 | 2024-10-11 00:35:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 1d7d9f5b-0d9b-34fb-bf1b-8e1997f837f3 | -5.3265 | -60.1239 | 2024-10-11 00:35:37 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2177a9e3-631b-3d75-8ccc-8ffe3bb7f404 | -6.5404 | -60.0259 | 2024-10-11 00:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 505efb7a-2930-333f-bf86-79be95efa5b2 | -6.5589 | -60.0252 | 2024-10-11 00:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| ffd2dc98-a8b9-32c1-b227-50d3af925ce0 | -6.747 | -59.3259 | 2024-10-11 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e476cf51-a783-3f4b-9b04-13b87c8ee781 | -6.7654 | -59.3252 | 2024-10-11 00:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| dad4e8f8-d86d-3715-b63a-78aaaf8dd372 | -7.0786 | -59.4087 | 2024-10-11 00:35:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 98a4d0c5-4add-369d-a0a7-639d1a079c74 | -8.4417 | -55.4692 | 2024-10-11 00:35:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a2d5fc28-3251-3e7f-b138-3ad868efb6ea | -9.2742 | -60.7893 | 2024-10-11 00:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 829da90b-f11d-33d6-9d60-e0cd0d1cb105 | -9.7374 | -46.9844 | 2024-10-11 00:36:01 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |


[Clique aqui para ver as próximas entradas](README4.md)
