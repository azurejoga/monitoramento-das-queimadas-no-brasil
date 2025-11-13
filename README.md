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
| a210ddfa-b1cd-35a2-8f33-8bd08af5c6da | -3.4019 | -50.175 | 2025-11-13 00:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| e5522764-5d9d-3172-9118-f84aefd2f7c1 | -3.8658 | -49.7998 | 2025-11-13 00:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 08fd652b-930d-3793-aff9-41ecc7d22659 | -3.2378 | -45.5839 | 2025-11-13 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d1bf7140-d15e-38d7-b38e-a6b5132617a9 | -4.3003 | -48.2431 | 2025-11-13 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 3a3bbdc2-bff2-3db6-8295-a3ff147ca6df | -4.7204 | -46.4497 | 2025-11-13 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 06c8db34-b3a5-383f-8f86-76a182ef5e82 | -21.8962 | -56.7275 | 2025-11-13 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 101.6 |
| ab8e400b-14d6-3efa-bf9d-46227a57e464 | -3.0916 | -49.2759 | 2025-11-13 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 290.2 |
| 30477c72-ca8c-3e0f-82d0-88f687480c47 | -4.5344 | -46.4376 | 2025-11-13 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 8d3d2b15-9a53-361e-b804-40bd4946af3f | -3.0917 | -49.2547 | 2025-11-13 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 6f26329e-67e9-3a37-9a03-84de2f304035 | -2.445 | -49.2519 | 2025-11-13 00:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3814b2ce-1382-3e82-b790-d34ec53c0236 | -4.2056 | -48.5706 | 2025-11-13 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 63954088-4e93-3cd6-a349-f16f09eaf810 | -4.2156 | -50.1022 | 2025-11-13 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| ab7d45f4-105c-3e1b-877a-f3c73e0d60b1 | -3.0731 | -49.2765 | 2025-11-13 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 72399a84-a384-34ec-915a-b4f6c9f825fd | -4.2157 | -50.0812 | 2025-11-13 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| bac8dc24-1d69-321b-be7c-40ca47ad070d | -3.2192 | -45.5846 | 2025-11-13 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 65895e22-026f-3e46-9aba-7a058f9dc0b4 | -4.7018 | -46.4508 | 2025-11-13 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 0b5a33c8-1df6-3f28-b9b2-fb053d5335a0 | -21.8957 | -56.7489 | 2025-11-13 00:00:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 101.6 |
| f2b3132a-c80e-384f-affd-2fc806eca63a | -5.4559 | -47.6822 | 2025-11-13 00:00:00 | GOES-19 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b14fa4ea-0f63-387f-ba41-2c5da467c088 | -4.5346 | -46.4155 | 2025-11-13 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 92962ba7-4a04-3838-9f66-fc94551efa13 | -2.4449 | -49.2731 | 2025-11-13 00:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7abf6c25-2f65-3e28-a5ca-a27ff2d57e2d | -3.2377 | -45.6063 | 2025-11-13 00:00:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 6b0e8c3c-bee7-3713-aa37-d00690ed2e51 | -4.3188 | -48.2422 | 2025-11-13 00:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a9042dd8-bd4c-3f37-ba72-b351fdbcb9d4 | -4.7206 | -46.4276 | 2025-11-13 00:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 88.4 |
| fe50e1ae-2a25-3ce6-84d7-885c831f3629 | -2.4634 | -49.2727 | 2025-11-13 00:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| ea6f179a-4a7d-3261-a809-d92d8d81ca28 | -4.0976 | -48.0144 | 2025-11-13 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| a6a683cc-e529-3bc2-9a1c-4f615a552997 | -3.1101 | -49.2753 | 2025-11-13 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| ae56ef50-0a4b-3ec6-bc46-7d3137bcb879 | -2.893 | -48.082 | 2025-11-13 00:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| b1a0ecf8-3acf-3c88-86ae-ef464412655f | -4.1971 | -50.103 | 2025-11-13 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 281734af-21d1-3399-b7d7-54d924383049 | -3.0915 | -49.2972 | 2025-11-13 00:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 40244274-b86c-309b-b6d2-e9c23b963b44 | -3.3729 | -48.4107 | 2025-11-13 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 31004ebf-def0-3dd0-a7d0-a9d406bbb05f | -5.3885 | -46.7645 | 2025-11-13 00:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| af055a38-b196-3e00-9002-4fdef17b1424 | -2.4635 | -49.2514 | 2025-11-13 00:00:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 9a3c6ff0-e274-34e5-a656-650cfcb0040f | -4.1972 | -50.0819 | 2025-11-13 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| e04d3704-22e5-390c-9fd8-32ce8469b4f3 | -6.5619 | -35.0247 | 2025-11-13 00:10:00 | GOES-19 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 86.0 |
| b3afc739-9865-3c71-ab90-aa188b81fc12 | -4.7206 | -46.4276 | 2025-11-13 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 89.5 |
| b094f30d-0c63-3d7a-8fc3-cb077cfef643 | -2.4449 | -49.2731 | 2025-11-13 00:10:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 6b2f6f46-f784-3d43-815a-811b64bc3031 | -5.4559 | -47.6822 | 2025-11-13 00:10:00 | GOES-19 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| a5e92279-e718-3ee9-8e14-fd076c5e504c | -4.2156 | -50.1022 | 2025-11-13 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 34.1 |
| b7a2b6c0-35a8-3675-baad-45473098078c | -3.0731 | -49.2765 | 2025-11-13 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 3a7c12f0-2d6f-35e3-b3ce-a53de2cf59dc | -4.1972 | -50.0819 | 2025-11-13 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 1540be61-7696-34e6-99a3-9499d2d08e0c | -4.5346 | -46.4155 | 2025-11-13 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 0163b7cc-89c8-3afa-ac1e-a37493f63483 | -3.0917 | -49.2547 | 2025-11-13 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| d074e525-b623-36ba-9b44-8ea8c4f35018 | -4.2157 | -50.0812 | 2025-11-13 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 36.6 |
| 0a5c5834-477e-3c9f-990d-008f15204b5c | -3.2378 | -45.5839 | 2025-11-13 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e0c443fe-534d-37c4-a14c-a1838462e276 | -3.0916 | -49.2759 | 2025-11-13 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 286.4 |
| 64037de3-d2b7-3663-a5da-8968564320dc | -3.0915 | -49.2972 | 2025-11-13 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 72892a6c-75af-3cea-b78d-4a288f07e06c | -3.1101 | -49.2753 | 2025-11-13 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 82cb0ed8-dd0c-38b2-88b6-d2fb87d38ade | -4.7018 | -46.4508 | 2025-11-13 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 018d8025-a68b-3b0e-b19a-a996fb5efdbd | -3.2191 | -45.607 | 2025-11-13 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| e285ecec-ac7e-3c4a-aec7-6119e32f5312 | -3.4423 | -45.5756 | 2025-11-13 00:10:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 92e209fd-3fd5-36bd-a560-9b8fa52d276a | -5.3885 | -46.7645 | 2025-11-13 00:10:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 0aaec3ee-8720-3d1c-9456-08c940c1bce1 | -4.7204 | -46.4497 | 2025-11-13 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 142.7 |
| fd661692-8555-3ef7-98e1-a60abe7cfbe8 | -4.1971 | -50.103 | 2025-11-13 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| e9f33d49-cb05-3a45-898b-14275644854d | -3.8658 | -49.7998 | 2025-11-13 00:10:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 2e840816-cd5a-32c8-ad6e-f3eddb79356b | -3.2192 | -45.5846 | 2025-11-13 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 4c462645-6f15-33da-9c13-c75c81d62727 | -4.5344 | -46.4376 | 2025-11-13 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 1bb5cc10-bbfb-3892-ba16-4c7f64fe136f | -5.4557 | -47.704 | 2025-11-13 00:10:00 | GOES-19 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| dffa8d38-6f72-390c-be74-d25ad0f8880d | -4.516 | -46.4165 | 2025-11-13 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 60.0 |
| c1dbc8d4-f026-3490-bd6e-5fa6e51c4559 | -6.5622 | -34.9972 | 2025-11-13 00:10:00 | GOES-19 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 65.9 |
| 92930fa3-6fca-3d6e-affe-5e10fa05f950 | -2.8297 | -45.4419 | 2025-11-13 00:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0c03ddcf-57fb-3cf0-bf15-719cb67f604a | -2.445 | -49.2519 | 2025-11-13 00:10:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| c1fa99b2-6325-3893-aef4-b9f61219ee7f | -2.893 | -48.082 | 2025-11-13 00:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 9282a8c7-ac27-340e-8c44-c995b3d52d0f | -4.5158 | -46.4386 | 2025-11-13 00:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 3f8af938-69a5-3668-987f-692c172e1fc3 | -2.1758 | -48.360298 | 2025-11-13 00:11:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 404ac435-af20-3d60-88e2-73390afa70bb | -2.4001 | -49.3885 | 2025-11-13 00:11:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01ac85d1-c7d1-3717-a08f-81145668033c | -2.3985 | -49.381599 | 2025-11-13 00:11:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 179fe783-30bb-322c-bd15-f60ef00ecb40 | -9.3218 | -47.826698 | 2025-11-13 00:14:00 | METOP-B | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dc9cd246-444f-316e-98a4-4479d6b4ad4a | -6.1559 | -48.050499 | 2025-11-13 00:14:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9e52d49-59b4-3ba1-8503-39c5493cd1dd | -10.7563 | -44.896599 | 2025-11-13 00:14:00 | METOP-B | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9be74ba5-7d47-3981-a803-4cff7b8c7eb0 | -3.4636 | -43.178001 | 2025-11-13 00:14:00 | METOP-B | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c8b0025-221b-3424-b645-2ddce4d19466 | -2.8249 | -52.8592 | 2025-11-13 00:14:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb8e124c-4e40-3464-a6f2-e4dd5ef86357 | -2.7356 | -45.4687 | 2025-11-13 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32035e21-58c8-3efa-9cb8-bf7fdf6ddcbf | -3.2269 | -45.590401 | 2025-11-13 00:14:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6643d262-b475-3075-afa6-4077c9987f05 | -4.7236 | -46.445999 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9e760553-f9dc-35ef-af0c-bb1b35831599 | -2.7283 | -45.4813 | 2025-11-13 00:14:00 | METOP-B | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25ec7eec-3885-34d8-95b5-ef741dd5b18f | -3.1633 | -50.615898 | 2025-11-13 00:14:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b28bb8e4-c5c3-3b00-9f1e-49a15ee11e69 | -4.7079 | -46.422501 | 2025-11-13 00:14:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 88d62a0e-3e29-3618-b813-b9c257bc3526 | -3.6676 | -45.936199 | 2025-11-13 00:14:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cb0158ab-1f2b-3fd1-8f01-b2f0959f7159 | -3.344 | -48.376099 | 2025-11-13 00:14:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4a9dec6-b6cb-3f7f-b1a3-47e9b777bc61 | -13.0016 | -49.7882 | 2025-11-13 00:14:00 | METOP-B | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9617c863-2927-3395-82a1-b93905343b0e | -11.3169 | -48.491699 | 2025-11-13 00:14:00 | METOP-B | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 741c8afa-527d-314c-ab46-de54c5f149e9 | -14.1721 | -43.579399 | 2025-11-13 00:14:00 | METOP-B | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2b277b4f-6fac-355a-a815-afbf50a62471 | -7.4957 | -47.329399 | 2025-11-13 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 68133644-a8a2-3b56-a8ce-f56374fc5261 | -7.8198 | -41.758301 | 2025-11-13 00:14:00 | METOP-B | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 092e22a8-3244-3810-a090-1a62ad9e2422 | -10.3619 | -47.3242 | 2025-11-13 00:14:00 | METOP-B | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| af4a20f1-f7a5-3f2c-aeb7-8ec96a2d014c | -10.3703 | -45.0546 | 2025-11-13 00:14:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 39b2e139-27df-332e-b18e-ea82dca8a3b2 | -7.8101 | -41.7607 | 2025-11-13 00:14:00 | METOP-B | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8d26628c-0247-3cdc-a540-e4a8b4a1b5b0 | -3.6709 | -45.6847 | 2025-11-13 00:14:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c55f5c99-9d1f-37b6-ae53-d513a35b6a9f | -6.0364 | -43.490101 | 2025-11-13 00:14:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc929604-9ea9-3c3f-a539-24874b807ec2 | -3.1524 | -45.491299 | 2025-11-13 00:14:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 95a2b12b-73fe-324f-847b-e82736ab3ad6 | -2.0079 | -54.4394 | 2025-11-13 00:14:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a67f84b6-8370-3f3f-8842-8a5d72919369 | -4.205 | -50.074699 | 2025-11-13 00:14:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c748d0a-dba0-301d-9aeb-031013f2656d | -3.9007 | -52.105301 | 2025-11-13 00:14:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fe59928-219f-326b-a502-1aef61baf7c7 | -7.494 | -47.321999 | 2025-11-13 00:14:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d605525-2807-3d18-8299-9ee41f2e6d70 | -9.862 | -44.566502 | 2025-11-13 00:14:00 | METOP-B | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b5824ee8-8c78-3e81-9130-91dbc1891c5c | -4.1038 | -48.003201 | 2025-11-13 00:14:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33f5ec45-5438-39e6-af53-c24d1b096e49 | -10.9258 | -44.610199 | 2025-11-13 00:14:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d7d1852b-71ea-3187-b591-e09e29a26ce7 | -14.4993 | -46.652901 | 2025-11-13 00:14:00 | METOP-B | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3ad40aa4-4ca8-3369-872e-ab06847075de | -12.6525 | -46.7416 | 2025-11-13 00:14:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1b919342-a284-36b7-8f60-bdc361af7995 | -4.8169 | -47.338902 | 2025-11-13 00:14:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
