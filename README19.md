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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 876141e5-f4c7-34d0-9762-ce18b9bdc0d9 | -3.9669 | -48.1716 | 2024-11-10 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 30e63a95-6feb-3f34-9eb9-dfdd76f19a20 | -3.1423 | -50.4352 | 2024-11-10 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 244.1 |
| 5d3eee61-e8ea-3012-8693-bf326a57e102 | -2.9355 | -51.482 | 2024-11-10 02:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| c2ffe7f8-0353-31e8-b580-5759dc26f364 | -2.8857 | -45.3726 | 2024-11-10 02:30:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 0e90669b-220c-3b54-9281-85bb56a9d828 | -3.9483 | -48.1724 | 2024-11-10 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.2 |
| a89b72f8-6d2b-3bf9-b3fd-a49705d67e2c | -3.4383 | -50.2999 | 2024-11-10 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| b963be37-0d4a-34b7-8e7b-5a31773d42fc | -3.1422 | -50.4562 | 2024-11-10 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 91022826-c156-3324-a3bd-cba056b2cc84 | -2.931 | -52.7753 | 2024-11-10 02:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 7e025c06-cc02-318b-b1e0-e39982d54ef2 | -8.3964 | -44.1597 | 2024-11-10 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 3e94b2e9-5f29-3146-ab69-4f211ae7e658 | -3.2243 | -53.0727 | 2024-11-10 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b2d868ce-2aae-3456-a459-79ad0418b62c | -8.3778 | -44.1386 | 2024-11-10 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 122.5 |
| dc3c99d6-b43f-3247-9c65-9dfd71daef6e | -3.1239 | -50.4358 | 2024-11-10 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 239.6 |
| 9ff2f169-acd2-3e45-b912-e9f44313895e | -3.6003 | -47.3614 | 2024-11-10 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| e6698d49-fc7a-363d-bd4c-adc89bb7b961 | -2.9494 | -52.7748 | 2024-11-10 02:30:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d807e87e-f68a-3c37-9de7-f481fb68f563 | -2.8802 | -51.4835 | 2024-11-10 02:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| e975b01b-adbc-358a-8e60-a25e7861a9c4 | -8.4153 | -44.1576 | 2024-11-10 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 82.7 |
| bcd6c3ad-6456-3770-b165-999251ae50b9 | -3.2244 | -53.0524 | 2024-11-10 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| cc44ea87-6068-319b-9ec1-d7f2cf85af23 | -3.1095 | -49.4241 | 2024-11-10 02:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 2a8fa7fe-7584-38d0-93b8-8f7a97719ed2 | -3.9486 | -48.1291 | 2024-11-10 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 5702f7be-f758-3240-9614-57b7956c8779 | -3.5064 | -44.0294 | 2024-11-10 02:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| c33d18bb-3ee1-3d04-b24a-2d4530c5fb57 | -2.0954 | -48.8125 | 2024-11-10 02:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| dd01043c-d11b-3dd5-ace9-fbc877befa44 | -3.6004 | -47.3395 | 2024-11-10 02:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 5ab86d0d-0794-3752-b939-2e19a38e2cc6 | -17.293 | -57.5062 | 2024-11-10 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| c68be6a3-94f0-343b-b307-096f42eaf9dc | -1.5347 | -52.2104 | 2024-11-10 02:30:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 76584e8e-714c-396d-ac71-14123ff03fde | -5.5608 | -43.9775 | 2024-11-10 02:30:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 1134ed50-eb21-3c1f-82ca-f4739209be06 | -2.9171 | -51.4825 | 2024-11-10 02:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 0514c8e2-af72-3a8c-ba1f-e2623b4be7bf | -8.3967 | -44.1365 | 2024-11-10 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 6318d308-8d15-3ee4-a01c-cec2ae909fa5 | -3.525 | -44.0286 | 2024-11-10 02:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 61.4 |
| dd451dc5-a63d-3646-98d6-127b9cbcc063 | -8.4156 | -44.1344 | 2024-11-10 02:30:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 33c353b6-8126-3c7e-81d5-3475b718c761 | -2.2095 | -47.733 | 2024-11-10 02:30:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 73686d1d-e4d4-3d6b-964b-69c8cdf66d21 | -3.9485 | -48.1508 | 2024-11-10 02:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| f5081d05-eab0-3b6e-b9e5-6fe67a9baa27 | -17.2933 | -57.4857 | 2024-11-10 02:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 162.5 |
| cb76d213-7936-36bc-9564-997a0d9cfb4a | -2.0953 | -48.8338 | 2024-11-10 02:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 30ccf4d1-e669-3348-aa74-4623b62f5a01 | -3.4198 | -50.3005 | 2024-11-10 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 45c840b6-05af-3e1d-80e9-603cf35e8d93 | -2.8802 | -51.4835 | 2024-11-10 02:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9ffdb1fa-be92-30cf-8afd-dd15b13f9d39 | -8.4156 | -44.1344 | 2024-11-10 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 8c86e450-9f57-3124-a6c6-fdb3ee381edb | -3.4383 | -50.2999 | 2024-11-10 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ad062d62-0b44-3e6b-933b-f1e299b2c8d7 | -2.9171 | -51.4825 | 2024-11-10 02:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| efbe20d8-bf68-3665-969c-fe36475a2f42 | -2.9355 | -51.482 | 2024-11-10 02:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 026f0949-3424-31a3-a877-93934cd58fa7 | -2.8618 | -51.484 | 2024-11-10 02:40:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 75101ab6-4fd2-387b-9a47-00fa54d42a6b | -8.3778 | -44.1386 | 2024-11-10 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 128.8 |
| bef394df-3d04-3e37-9b43-334342b85c7f | -3.1423 | -50.4352 | 2024-11-10 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 238.3 |
| 94223f90-fd2d-37e8-bceb-1c0b79b82776 | -8.3775 | -44.1617 | 2024-11-10 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 72.8 |
| fd1a93b5-9b92-3f17-80b6-1d6961de2690 | -3.1095 | -49.4241 | 2024-11-10 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 2ad8b15d-fc51-3e0f-9b67-e2e35bbcdee7 | -3.9668 | -48.1932 | 2024-11-10 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 580cd8e3-3f75-3079-8709-5c76654f0537 | -5.5608 | -43.9775 | 2024-11-10 02:40:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| dd77dd30-89a9-3025-ab11-bded7fcd5aaa | -2.931 | -52.7753 | 2024-11-10 02:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 24d809f2-960b-37f8-a033-a6dfcadbbd13 | -3.9669 | -48.1716 | 2024-11-10 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 114.5 |
| edecc83a-0176-3c04-bfbb-c46634c941e7 | -2.8857 | -45.3726 | 2024-11-10 02:40:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 47.2 |
| c11d49bf-0a3a-39b3-a266-2e24d9a80ca3 | -3.128 | -45.2285 | 2024-11-10 02:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 75658c54-13fa-3441-ac8e-606db09cb62c | -3.2244 | -53.0524 | 2024-11-10 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 46818cb5-d4e7-3888-8ce7-485f816fee5d | -3.1422 | -50.4562 | 2024-11-10 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 173.4 |
| e1cd82e8-4c0c-3d7a-9a5a-ed9d7713873a | -1.5347 | -52.2104 | 2024-11-10 02:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| d10943ad-4331-3667-a058-89457217e9ec | -3.1239 | -50.4358 | 2024-11-10 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 249.2 |
| af20472c-06c9-325b-b849-bc7b1c5e1bda | -3.2243 | -53.0727 | 2024-11-10 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 49a418dc-850b-35a4-b9f4-f58ced94df11 | -3.5064 | -44.0294 | 2024-11-10 02:40:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 744f59f9-059c-36d6-ac84-7e47f543a3fa | -1.5163 | -52.2106 | 2024-11-10 02:40:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 92cc53e2-1f2e-3076-8aad-76384a5bd869 | -3.6003 | -47.3614 | 2024-11-10 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 485d0b98-f519-3e19-a2f7-6de9ca8c7c4e | -3.9483 | -48.1724 | 2024-11-10 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| e4185742-fda8-3bd1-a19b-e948fd96b819 | -2.0953 | -48.8338 | 2024-11-10 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 7e9d50e0-045f-32fc-84af-7967f5e7f98f | -17.293 | -57.5062 | 2024-11-10 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 106.6 |
| 3f767c74-85ed-301e-93ab-0be59d04e145 | -2.9494 | -52.7748 | 2024-11-10 02:40:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9842e336-60da-351d-9219-1796f0b9bb67 | -8.3967 | -44.1365 | 2024-11-10 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 916fcbb5-2023-3cf6-bed1-dd9424b76a7c | -2.4365 | -46.3019 | 2024-11-10 02:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 2d6229e5-a65e-3ef4-928a-80d7f4672cff | -17.2933 | -57.4857 | 2024-11-10 02:40:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 135.8 |
| 83f3c703-4b0b-3c65-89a2-a70fc51ce2a6 | -8.4153 | -44.1576 | 2024-11-10 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 84b901b3-7677-377a-be39-3f8efa02846d | -2.7587 | -49.3497 | 2024-11-10 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 11d88c59-62e2-3951-8547-fca4c2edfaa5 | -2.7772 | -49.3492 | 2024-11-10 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 04dc41c9-a285-3c7e-96ff-cb76c0d11d06 | -3.1238 | -50.4568 | 2024-11-10 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 157.5 |
| cdb20d98-6961-3721-bf92-3fd202ecf345 | -3.5819 | -47.3403 | 2024-11-10 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| c5593a7e-9ecf-36f6-9ae5-a0e5cf10812e | -3.6004 | -47.3395 | 2024-11-10 02:40:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| 4ea407a0-f7ef-3c26-9ad1-09ce1db69086 | -3.9671 | -48.1283 | 2024-11-10 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9f29f0d3-53b0-3f9f-ab4d-3e898fe765bc | -3.9485 | -48.1508 | 2024-11-10 02:40:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 9fbb826e-dcbc-331f-a9dd-734aef10185a | -8.3964 | -44.1597 | 2024-11-10 02:40:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 92.9 |
| c8b56a3e-e43b-376f-88c9-9cd45a56d8e2 | -3.1095 | -49.4241 | 2024-11-10 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 697a97f9-cada-3a58-be69-3b7d60070690 | -2.418 | -46.3024 | 2024-11-10 02:50:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 8250b722-6b0e-3099-aac5-4c633cd6cee6 | -8.4156 | -44.1344 | 2024-11-10 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1cae78e8-a797-3581-950b-e96d2bd1767e | -3.1422 | -50.4562 | 2024-11-10 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| a19e61bf-7964-3739-b4f0-b2acc8d05824 | -3.9485 | -48.1508 | 2024-11-10 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 4da1d615-b298-3367-93c1-b672d9dfa9c9 | -8.3778 | -44.1386 | 2024-11-10 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 306431a7-234d-3ddf-889d-cf794071649f | -2.931 | -52.7753 | 2024-11-10 02:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 403ce556-c21c-3364-be4a-c557fb845a81 | -2.931 | -52.7549 | 2024-11-10 02:50:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 06d76348-5995-32eb-a848-1f83591ad7d4 | -2.7772 | -49.3492 | 2024-11-10 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e255813d-fed2-3d36-91d9-9195b80e2c01 | -3.525 | -44.0286 | 2024-11-10 02:50:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 4bc0df90-cae1-30a3-a232-c7c48df169a8 | -2.9171 | -51.4825 | 2024-11-10 02:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 4e048015-fa5d-382a-b286-a1cac96bef98 | -5.5795 | -43.9761 | 2024-11-10 02:50:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| cc258eb1-581c-310e-88be-b125018d49e0 | -3.6004 | -47.3395 | 2024-11-10 02:50:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 16716ef9-56d2-35f5-9a10-dcffcbfcaae9 | -3.1239 | -50.4358 | 2024-11-10 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 2803797c-fc5c-3368-8437-77a19fd40b72 | -1.5347 | -52.2104 | 2024-11-10 02:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 104.9 |
| ca5877e7-35b2-34fe-bcd1-61b19256e055 | -3.9483 | -48.1724 | 2024-11-10 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 61afa265-f7ac-3257-bdd9-9474282c933f | -3.1423 | -50.4352 | 2024-11-10 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| f4fa1375-ff4c-31aa-8a65-0d3ef78abe99 | -3.9669 | -48.1716 | 2024-11-10 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 537af96d-f457-31da-949f-a6b38729c1ea | -2.0953 | -48.8338 | 2024-11-10 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9767c803-5ac2-3471-9871-094e7a2ba319 | -3.4383 | -50.2999 | 2024-11-10 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| ebed3723-8ea2-31a7-a2e6-09221ae19f4b | -5.5608 | -43.9775 | 2024-11-10 02:50:00 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 3730ec17-8059-35b7-b5f9-20e7520c95c1 | -2.2095 | -47.733 | 2024-11-10 02:50:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| b7494f7a-8af4-3036-81c0-60173df9bb03 | -8.3964 | -44.1597 | 2024-11-10 02:50:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| ec349c46-c84f-3363-9eba-bee4e07971a4 | -17.2933 | -57.4857 | 2024-11-10 02:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 156.3 |
| e8bb1dfa-a722-3d93-bcfb-1e5bf6c2440d | -2.8857 | -45.3726 | 2024-11-10 02:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 347676e0-86f0-3277-979e-f02c57ba0db2 | -2.8802 | -51.4835 | 2024-11-10 02:50:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |


[Clique aqui para ver as próximas entradas](README20.md)
