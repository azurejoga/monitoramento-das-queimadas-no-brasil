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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5060ce67-1f91-3479-9302-70c9766b6775 | -8.96 | -60.5358 | 2026-08-12 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 81f18ed2-09ba-3e5b-b11c-d0207ef3dcf0 | -11.9719 | -46.3871 | 2026-08-12 01:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 2fa3d882-7431-392d-9f8e-bed0232ef251 | -11.4681 | -44.5558 | 2026-08-12 01:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 234.3 |
| 5490e5d1-f737-35c1-8fa2-114502a89324 | -13.8989 | -53.8217 | 2026-08-12 01:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| ab1ac8f0-64e1-3e90-8f45-5c4124284272 | -9.1408 | -46.402 | 2026-08-12 01:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| a5ee6dbb-29b0-35c3-b65b-a62e90f14726 | -8.9601 | -60.5165 | 2026-08-12 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.8 |
| c66f31e5-8c55-34c4-9de8-2e16a0d1b00c | -11.8285 | -51.8359 | 2026-08-12 01:40:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b4ff71ce-066c-38b5-be6a-c0871e103353 | -11.9535 | -46.3444 | 2026-08-12 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 0503a82c-a84a-34cc-b240-512ff5c9003c | -8.9414 | -60.5367 | 2026-08-12 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c15f6e0c-49a1-318e-8d11-0719e0a044f9 | -8.96 | -60.5358 | 2026-08-12 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| dcf253f5-f94d-3cc0-82b5-183dc55375e0 | -13.8989 | -53.8217 | 2026-08-12 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| d964fc3c-5980-382c-9a41-fc6d30a81a58 | -9.1411 | -46.3796 | 2026-08-12 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| c1bc4c90-554c-3096-83de-12b552e76809 | -11.4873 | -44.553 | 2026-08-12 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 5582f9c1-c9ef-3163-98b9-ebf3f2b385e7 | -9.1408 | -46.402 | 2026-08-12 01:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 8def3ec5-0730-3b5a-8ae8-66c061980bbf | -8.9415 | -60.5174 | 2026-08-12 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 48ed9677-46b4-3993-b4b1-7f122d7984a1 | -11.449 | -44.5587 | 2026-08-12 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 46.2 |
| a5a950f9-ed72-31f2-8fc6-93132ff18f9a | -8.9601 | -60.5165 | 2026-08-12 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 11132f9b-7cf6-382d-92f8-5fa57e134c6e | -13.8986 | -53.8426 | 2026-08-12 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 5db75d02-d7a7-3592-95bd-42b66b3220a0 | -11.4681 | -44.5558 | 2026-08-12 01:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| d9df79a6-1fc3-3b7d-a7eb-d4e9e9c4d279 | -11.4681 | -44.5558 | 2026-08-12 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 13aec4c3-3ebd-333f-9205-1a6fbaee80af | -8.96 | -60.5358 | 2026-08-12 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 114.8 |
| 725b2636-5f97-3650-9649-7982fe7a395c | -9.1408 | -46.402 | 2026-08-12 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| b54c8a31-6019-3d86-86e4-b82bc95566f1 | -11.9535 | -46.3444 | 2026-08-12 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| c7aa6913-8000-37ef-b9be-63bdda2b1299 | -11.8285 | -51.8359 | 2026-08-12 02:00:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| d68bd6ee-f420-357c-9a8d-4e72b67f1686 | -11.9719 | -46.3871 | 2026-08-12 02:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 63a9e9df-b845-38be-a4f0-f435b5f9e6df | -11.4873 | -44.553 | 2026-08-12 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 5a3e1146-f83d-3b49-82f4-f5574904c9a5 | -13.8989 | -53.8217 | 2026-08-12 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| fbc1df07-9031-31ce-89e5-78bdc28d1def | -8.9601 | -60.5165 | 2026-08-12 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| f8280a08-945f-3018-a980-741d6bf43316 | -11.4677 | -44.5791 | 2026-08-12 02:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 5476b2c0-0c7e-3d0a-8ac4-c4f2cf9774ee | -8.9598 | -60.555 | 2026-08-12 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 279bc00e-dbb6-350d-ab10-a19b37e5ab68 | -9.1411 | -46.3796 | 2026-08-12 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| abc4b1ee-d918-3fd1-8633-ea9245982a71 | -8.96 | -60.5358 | 2026-08-12 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| ab88ee78-7932-3812-8d1d-6a35d8f16b07 | -11.4681 | -44.5558 | 2026-08-12 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 15247f1a-9160-34e0-8fb1-e2d99b290d53 | -11.4869 | -44.5763 | 2026-08-12 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 0c2e9279-0506-3e53-8a43-d28c4fe076a7 | -8.9601 | -60.5165 | 2026-08-12 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.2 |
| fec3b040-a741-3520-a679-3a550202e807 | -11.4873 | -44.553 | 2026-08-12 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| dc1e526f-b494-3fb0-a7ff-cec2123dc663 | -11.9535 | -46.3444 | 2026-08-12 02:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 9760ae3d-fad3-36c5-be04-af7b3833f839 | -11.4677 | -44.5791 | 2026-08-12 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 89.3 |
| 45d4e7bd-b607-333f-91ed-833cfcf59569 | -11.9915 | -46.3617 | 2026-08-12 02:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 5c0ae065-246f-3031-85ec-269aaccd4505 | -11.4869 | -44.5763 | 2026-08-12 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 2bf95d69-be47-3549-9159-8efb5b4f5f42 | -8.96 | -60.5358 | 2026-08-12 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| b6b6bbcc-9923-30af-9722-57e24df72038 | -8.9415 | -60.5174 | 2026-08-12 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 04f07c84-928a-3ccf-aca7-01b5808fc51c | -11.9535 | -46.3444 | 2026-08-12 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| db13b827-4650-35cd-b787-e8911183af7b | -8.9414 | -60.5367 | 2026-08-12 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 099afac5-b28c-3035-85a8-0003e1e2a7f1 | -11.9531 | -46.3672 | 2026-08-12 02:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 0b8499e5-6db9-3cd9-8368-2e62fca23bde | -11.4677 | -44.5791 | 2026-08-12 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 963155b2-bb60-3bf7-b3da-2da6bfa0840d | -11.4873 | -44.553 | 2026-08-12 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 74ddc9e8-2bda-303c-900a-816a4c70da64 | -8.9601 | -60.5165 | 2026-08-12 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| d1f2e286-da8a-3fa1-a852-35dee2caa5a0 | -11.4681 | -44.5558 | 2026-08-12 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| fd81bfcf-60a8-34f2-86b3-a2228af23e26 | -8.96 | -60.5358 | 2026-08-12 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 1847041c-1f3e-336a-94b2-3e8d7c117534 | -11.4677 | -44.5791 | 2026-08-12 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 84d84a95-3e09-3866-9349-95e30832c4e1 | -8.9415 | -60.5174 | 2026-08-12 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| bdb11bca-335b-3399-89ab-3c5c3a79fe96 | -8.9414 | -60.5367 | 2026-08-12 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 9c84b588-af3e-370b-99bc-40fedc753cdc | -11.4681 | -44.5558 | 2026-08-12 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 138.5 |
| cd25f976-8aa8-32bf-9b6f-6218a264402e | -8.9601 | -60.5165 | 2026-08-12 02:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 1342c04c-e775-37d1-b986-93b2c1139c94 | -11.9535 | -46.3444 | 2026-08-12 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 30699d82-baca-39c1-84e6-433d60637fde | -11.4873 | -44.553 | 2026-08-12 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| a38d3bac-6770-32e8-a93f-f1ef74e6d805 | -11.4869 | -44.5763 | 2026-08-12 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b36ea0e2-5492-3dc0-ba99-1a91490a3d64 | -11.9531 | -46.3672 | 2026-08-12 02:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| e535ef9c-091a-3ab2-ba81-acda74f881d7 | -9.6637 | -40.5819 | 2026-08-12 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 7053e009-fcf0-3964-b03b-e72546701b01 | -15.8854 | -48.9852 | 2026-08-12 02:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 284.2 |
| 014a2989-c1bb-3e54-a191-2241f2d0889f | -11.9535 | -46.3444 | 2026-08-12 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d68ef0c4-2610-33c9-98ea-a10fd2897405 | -11.4873 | -44.553 | 2026-08-12 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 1dbbddec-c1b6-3835-8289-eb3def983f74 | -15.8849 | -49.0076 | 2026-08-12 02:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 45351e31-d073-3049-9dba-1621317f7793 | -8.9601 | -60.5165 | 2026-08-12 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 4ad73089-fc8c-35c4-bb6f-9ad6b0851ae6 | -11.4677 | -44.5791 | 2026-08-12 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| efafcb9b-f4ba-398b-b1df-6f06ad411659 | -8.96 | -60.5358 | 2026-08-12 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 231ce3a9-7bec-35e9-b163-26d46f262f40 | -15.905 | -48.9819 | 2026-08-12 02:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 3a58c245-fd68-38f4-bb64-2ca4f2e6c616 | -8.9415 | -60.5174 | 2026-08-12 02:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.9 |
| df338a9a-3b31-3a7f-99c8-a07237e61ea0 | -11.9531 | -46.3672 | 2026-08-12 02:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| bff9b93a-b897-3687-9222-30f42334397c | -11.4681 | -44.5558 | 2026-08-12 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 7263b2ce-d8ae-37cb-8200-1e496db17f0d | -11.4869 | -44.5763 | 2026-08-12 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| e6ed42ea-1924-3b16-a54f-d64cad420ab7 | -11.4681 | -44.5558 | 2026-08-12 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 2cb42131-6710-3f1b-88f5-30f0dea263ec | -11.9535 | -46.3444 | 2026-08-12 02:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5a9bee40-f0fd-3474-91b9-e514ddfacba7 | -11.4873 | -44.553 | 2026-08-12 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 6d6b6c9d-0b74-319e-bb1b-b01651ec3894 | -8.9601 | -60.5165 | 2026-08-12 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 3b8080c7-8e87-3900-b278-4d749c5a1ee5 | -11.4869 | -44.5763 | 2026-08-12 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| 40f80918-856a-3a7c-8a06-a79faad47013 | -8.96 | -60.5358 | 2026-08-12 02:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| ffb2b120-0600-3fed-b363-433fd7c33106 | -11.4677 | -44.5791 | 2026-08-12 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f2318736-526e-326e-9463-8574d8836231 | -8.9601 | -60.5165 | 2026-08-12 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 5abedf1c-d041-3e30-a216-5971753a3224 | -11.4869 | -44.5763 | 2026-08-12 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| 05f60c93-f6f2-3a2b-b721-7b4db1e18cea | -11.9719 | -46.3871 | 2026-08-12 03:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 69.5 |
| f78fbbb7-f800-3b13-a671-43b101b98603 | -11.4681 | -44.5558 | 2026-08-12 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| ded1ce5e-9c6d-307d-bcd2-3da2d7b14312 | -11.4873 | -44.553 | 2026-08-12 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 9feea144-92ac-3f69-9480-fee4c88cc512 | -8.96 | -60.5358 | 2026-08-12 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| da6bcc11-cd0c-3bcd-86dd-8fcfd3aad57a | -11.4677 | -44.5791 | 2026-08-12 03:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 831fd715-a362-363a-a4c5-64680380ab6d | -11.4681 | -44.5558 | 2026-08-12 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| 1758459c-7da8-3218-ae64-9042a3421f17 | -8.9601 | -60.5165 | 2026-08-12 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 6eadfc80-9037-34e4-a901-2fcbac944d62 | -11.4677 | -44.5791 | 2026-08-12 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 4230d739-ae9f-3862-8a2f-b297cd5a54c4 | -11.4873 | -44.553 | 2026-08-12 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 0be173c4-f967-3a84-96ed-ee9fc39fff4e | -11.9719 | -46.3871 | 2026-08-12 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 74b08e86-0b8e-3057-9b92-b8ee9b6e91d2 | -11.9535 | -46.3444 | 2026-08-12 03:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 1f5c9766-9d7c-3664-b11b-a046d09e973c | -8.96 | -60.5358 | 2026-08-12 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 9d6d8f8d-882f-321a-8bcf-05b32e65f73e | -11.4869 | -44.5763 | 2026-08-12 03:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 107.6 |
| fe36f6df-0f62-397f-9cb4-aa57601d965c | -8.96 | -60.5358 | 2026-08-12 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 1e4e2930-923b-340f-b09b-b8ca1945aa66 | -11.4681 | -44.5558 | 2026-08-12 03:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 49fc375a-b5bc-3ed6-9948-048cfaa3d78d | -11.4869 | -44.5763 | 2026-08-12 03:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| cd85c172-5884-38d4-ac8f-7055a5ab5414 | -11.9719 | -46.3871 | 2026-08-12 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| edb0ebe2-d266-39ee-9a67-49d1a28c8e0c | -8.9601 | -60.5165 | 2026-08-12 03:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.8 |
| ef8b3482-bd02-31f4-868e-e2073c65cac6 | -11.9535 | -46.3444 | 2026-08-12 03:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |


[Clique aqui para ver as próximas entradas](README6.md)
