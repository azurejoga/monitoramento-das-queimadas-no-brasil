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
| 6ec711d7-e0ee-3e79-8430-faf1636a38e6 | -7.2742 | -44.6395 | 2025-06-17 00:38:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5907e77-3dde-3e0c-b723-784e95dc14e0 | -6.2881 | -44.2248 | 2025-06-17 00:38:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18c0e926-0026-387a-b937-493bd175a162 | -9.727 | -48.316601 | 2025-06-17 00:38:00 | METOP-C | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aadba583-577b-333f-b138-6a8fc62fcb35 | -6.0719 | -46.106499 | 2025-06-17 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5851fe9e-5fb3-35ff-922b-01eaa83d5c26 | -9.2015 | -49.690701 | 2025-06-17 00:38:00 | METOP-C | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 87c8c983-1c8a-3f8b-b480-e17968f242fb | -6.0639 | -46.116501 | 2025-06-17 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8c822dd9-fed8-3161-a2cc-8aca8f8497c1 | -9.6747 | -48.769798 | 2025-06-17 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 46506200-fa9f-310f-a181-b8ce5344be4f | -11.1374 | -53.9394 | 2025-06-17 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b94ccad1-b6de-3fd7-bcbf-fa8cc5d9b389 | -2.4572 | -47.5075 | 2025-06-17 00:38:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54eaf1ac-04ec-3c34-94f7-158e6f379b5a | -12.209 | -49.6287 | 2025-06-17 00:38:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8d9571a-304e-326b-8aa1-598c6b5113a8 | -12.3444 | -49.307598 | 2025-06-17 00:38:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1f6d78fb-e548-3d53-b6ee-d50f629c460a | -7.7217 | -55.130501 | 2025-06-17 00:38:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 526699f8-036d-3d9a-8c31-2b23ce6500c6 | -7.5421 | -45.642502 | 2025-06-17 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5dcb6291-2bfe-350f-adae-f32477fd47a1 | -6.2927 | -47.010399 | 2025-06-17 00:38:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 81352015-7d34-3a1c-aebd-6c83f081e114 | -2.4458 | -47.502399 | 2025-06-17 00:38:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e70d240-0e00-3700-8218-5d623fcc3414 | -8.3985 | -47.462299 | 2025-06-17 00:38:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39aff4ff-abc4-3361-b576-031bff601883 | -7.7247 | -55.144501 | 2025-06-17 00:38:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf0c867d-7a2c-3d71-be0e-3f8b8c918aac | -7.2868 | -50.007801 | 2025-06-17 00:38:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8de8f4db-ae3f-3f63-afe3-56fe40e5a55c | -6.8465 | -47.844799 | 2025-06-17 00:38:00 | METOP-C | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38354a29-99af-35b8-bef6-3da6928bdac2 | -6.3025 | -47.008099 | 2025-06-17 00:38:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dc83fce1-65d5-3a35-a7ec-ccbacfded1b3 | -9.6762 | -48.776798 | 2025-06-17 00:38:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20cc1075-ef36-3c41-a6b4-60e1ab70bb01 | -5.5728 | -45.2117 | 2025-06-17 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| be857e74-dc6d-3815-bc70-5fcf437debf5 | -11.1346 | -53.926201 | 2025-06-17 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0e39ca54-3961-3160-8af3-175942eb1ed9 | -10.14 | -46.738098 | 2025-06-17 00:38:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e2d9368-eef2-337b-bc6b-3d60d1350da8 | -2.4556 | -47.500198 | 2025-06-17 00:38:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4518d1e-7308-3500-94fc-c69413d29bc7 | -8.606 | -48.054199 | 2025-06-17 00:38:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 933c2810-0951-3544-a508-7bfbc7830ace | -10.7426 | -48.5742 | 2025-06-17 00:38:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 228c3b07-d269-37d4-bcc7-b5f675213648 | -10.3644 | -46.996201 | 2025-06-17 00:38:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47ce5acd-22bc-38f8-9713-3ded33fcde1d | -7.277 | -50.009899 | 2025-06-17 00:38:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01144a2a-64c8-32ce-a644-edaa97473c96 | -10.1368 | -46.723999 | 2025-06-17 00:38:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a385c255-b828-3710-9e13-24aa7fa33ad9 | -6.3008 | -47.0009 | 2025-06-17 00:38:00 | METOP-C | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 561e635a-e338-30c8-89ad-b92734053235 | -8.6155 | -45.028198 | 2025-06-17 00:38:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b7cd4d19-1027-3f58-a353-3fcc8260211e | -11.1499 | -53.9506 | 2025-06-17 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1522ee84-7990-330e-b154-506821688296 | -6.0621 | -46.108799 | 2025-06-17 00:38:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ba297817-7588-327d-9f7a-e85ee214fe78 | -6.2904 | -44.234299 | 2025-06-17 00:38:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8853297a-eb78-3036-a13b-6d324d1be5a0 | -12.4296 | -50.031399 | 2025-06-17 00:38:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 12a84cf9-9088-3af7-8604-a2a0c5a790e9 | -6.1534 | -48.059898 | 2025-06-17 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d712040-e490-3a27-aa85-28f07e1b6847 | -6.1632 | -48.057701 | 2025-06-17 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6feb2631-4230-3115-8f8d-41eea6699177 | -10.1417 | -46.745098 | 2025-06-17 00:38:00 | METOP-C | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7abc12a9-9be6-38ca-8f5b-97e198265821 | -13.3938 | -48.469101 | 2025-06-17 00:38:00 | METOP-C | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37969977-e16b-320b-a2cd-31d605c781e3 | -10.9294 | -56.8214 | 2025-06-17 00:38:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d93cbc4-08a7-3d5a-af3a-69c0d6c81dfa | -8.9687 | -47.971901 | 2025-06-17 00:38:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0a42cea-0fdc-3027-ac9e-110f72236e56 | -8.0769 | -43.122299 | 2025-06-17 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 025cb3c9-08a0-35e5-95bc-1ea255594e0a | -7.6812 | -44.571201 | 2025-06-17 00:38:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 132b3559-8e30-3431-9a9e-50635045394e | -11.0353 | -44.648602 | 2025-06-17 00:38:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a02a1b0-5ccc-389e-a6fd-7f6aa48fe62c | -7.2051 | -45.350899 | 2025-06-17 00:38:00 | METOP-C | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1244cc64-a1bb-3249-aa0e-f5e04b86c0e0 | -7.1156 | -47.848999 | 2025-06-17 00:38:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39a99354-0e82-3461-bc03-548270bae9c5 | -10.3562 | -47.005501 | 2025-06-17 00:38:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8366a1c4-c437-33ef-8bd2-d3fdbffa4299 | -7.456 | -45.495899 | 2025-06-17 00:38:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5938858b-47f5-329d-aeb7-2d17dde335ee | -6.3002 | -44.231998 | 2025-06-17 00:38:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ae54048d-c1d4-3916-9af7-3e5f5b97d45d | -5.2906 | -44.715302 | 2025-06-17 00:38:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| add77c05-8e21-3d8a-bea4-61d6e2d0f4d2 | -12.3461 | -49.315201 | 2025-06-17 00:38:00 | METOP-C | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c87b4774-c324-3bf5-9ee7-7b9b61693393 | -8.0743 | -43.111801 | 2025-06-17 00:38:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 009254aa-1914-354a-82a6-e74aa394853b | -11.1444 | -53.924198 | 2025-06-17 00:38:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3e15cc6a-a1d5-3879-bd11-7d58783d03d7 | -8.3351 | -48.448898 | 2025-06-17 00:38:00 | METOP-C | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3875759e-25da-3719-ab1a-18acc09be6ab | -13.2789 | -49.8797 | 2025-06-17 00:38:00 | METOP-C | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9d8402c6-b90a-39ad-a15b-2c0a9ff11f8d | -6.2927 | -44.2439 | 2025-06-17 00:38:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8f3f2b7-8eae-3246-afbb-258795a97b0b | -8.6116 | -45.011902 | 2025-06-17 00:38:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40548bc1-1759-3797-990f-ca80887dfa6e | -4.2498 | -47.587898 | 2025-06-17 00:38:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c59d71-6e9b-32ea-977f-d9855939b0b1 | -10.9678 | -45.105999 | 2025-06-17 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ae2b34b-60f6-3c0f-860c-ce2710597ef4 | -6.155 | -48.0667 | 2025-06-17 00:38:00 | METOP-C | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66b31ae2-79d0-3bfa-802d-20803801393e | -10.731 | -44.890099 | 2025-06-17 00:38:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0089b5de-2baa-3c89-9a1b-d7267b3c7c9d | -12.4279 | -50.023201 | 2025-06-17 00:38:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ba46f2f5-8f30-3acc-b17a-508e64245f66 | -5.5708 | -45.203098 | 2025-06-17 00:38:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b83554b0-9a24-331f-bdbd-325b03c74270 | -10.958 | -45.108299 | 2025-06-17 00:38:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 533f4743-8e2c-3769-9f16-e33254260275 | -8.7084 | -46.972198 | 2025-06-17 00:38:00 | METOP-C | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b81eb3fd-0bdc-39ab-9bf2-ec548e188920 | -10.9167 | -56.8336 | 2025-06-17 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 8ed9c5a5-9753-343e-afe1-97ab08a4108a | -11.1568 | -53.9411 | 2025-06-17 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 13c8c7c4-805a-3d41-b18a-927ba463e249 | -17.454 | -52.922 | 2025-06-17 00:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 4ab04534-0b8e-30f4-a9a6-561a36fb0054 | -10.2827 | -60.5432 | 2025-06-17 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 34.9 |
| f0156d8b-c6ea-313d-a979-5f47c04c2866 | -11.1379 | -53.9429 | 2025-06-17 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 155.5 |
| 9204294d-f088-3f13-bf1c-870a9d39e216 | -11.1382 | -53.9223 | 2025-06-17 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| b922fb51-6b86-3368-8382-06756c421fcd | -10.9355 | -56.8322 | 2025-06-17 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| ad3fe183-8f2f-3e72-822d-de7a41e59b00 | -10.9353 | -56.8522 | 2025-06-17 00:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 4ff1e84b-7528-35cc-869f-ac55e5ae9fa2 | -13.272 | -49.8859 | 2025-06-17 00:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 56.4 |
| ff57078b-bcc8-3417-9053-1fa1978f90e8 | -11.1571 | -53.9206 | 2025-06-17 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 4b0d52fc-9cab-36b6-8639-1260b52286f2 | -13.4751 | -46.256802 | 2025-06-17 00:41:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 91269d47-76a3-3e70-8571-6d074e9a02ac | -21.430599 | -48.6394 | 2025-06-17 00:41:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a517ac4f-d5d3-3618-84ee-2c3fd3f6b7f7 | -20.2423 | -46.741901 | 2025-06-17 00:41:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb65914a-08f5-3498-9cda-0a0d6d534129 | -19.668699 | -49.785 | 2025-06-17 00:41:00 | METOP-C | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7509c3b6-02d0-363a-8843-abafeb4be25e | -19.678499 | -49.782902 | 2025-06-17 00:41:00 | METOP-C | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| be5f6377-3ff4-3da5-adfc-b38ff6435dee | -19.2906 | -48.464802 | 2025-06-17 00:41:00 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2f155bbd-c68c-325e-adec-f998e4886b9d | -19.149099 | -43.5065 | 2025-06-17 00:41:00 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 43ceaf10-1f33-3470-b7d2-d987d49f323a | -17.445299 | -52.948002 | 2025-06-17 00:41:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3e587dd2-5556-3564-9345-676026469a3b | -17.4426 | -52.9338 | 2025-06-17 00:41:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e2a7bd38-a744-33ae-8034-d08c5c0251d9 | -19.1376 | -43.501202 | 2025-06-17 00:41:00 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fb674f14-fb45-364a-8d17-319c599ca4b3 | -19.141199 | -43.516701 | 2025-06-17 00:41:00 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e065ade4-9a3e-3140-bf72-5acb8b748d2d | -21.4324 | -48.648499 | 2025-06-17 00:41:00 | METOP-C | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 14d13550-f7ab-35d3-b9c4-63b4fb165e73 | -19.6668 | -49.775101 | 2025-06-17 00:41:00 | METOP-C | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 552f25be-a4c1-3ba7-9024-4b720e89c504 | -18.321899 | -49.882099 | 2025-06-17 00:41:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9ed5187a-73f4-379a-b4d1-3f07ebf714f7 | -19.1394 | -43.508999 | 2025-06-17 00:41:00 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f11767f0-fb43-30e3-9bc9-4a0c1a130167 | -20.156799 | -45.2118 | 2025-06-17 00:41:00 | METOP-C | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c335158a-ff85-30ce-a8e4-10c491e26856 | -18.323799 | -49.891602 | 2025-06-17 00:41:00 | METOP-C | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0b667363-b897-3fcf-b888-12314c537620 | -19.6766 | -49.772999 | 2025-06-17 00:41:00 | METOP-C | SÃO FRANCISCO DE SALES | MINAS GERAIS | Brasil | 3161304 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bade4fd6-cb9b-3913-9d71-6ef2522275b3 | -17.439899 | -52.919701 | 2025-06-17 00:41:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a0563497-3aac-3e40-9b00-05da51ebb33f | -19.2889 | -48.456402 | 2025-06-17 00:41:00 | METOP-C | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6a8f09e9-3809-36e0-939b-eef78d56dad8 | -20.155199 | -45.204498 | 2025-06-17 00:41:00 | METOP-C | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47054513-5344-3408-b3ae-69edffa9f452 | -14.0068 | -46.191299 | 2025-06-17 00:41:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 58e83264-d63e-32c0-93c4-f4977f1e01f4 | -11.1568 | -53.9411 | 2025-06-17 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bc601013-1942-3ca9-b3c8-5b082efa9ed4 | -10.2827 | -60.5432 | 2025-06-17 00:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.3 |


[Clique aqui para ver as próximas entradas](README4.md)
