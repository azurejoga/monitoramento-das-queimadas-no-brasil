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
| 99aa598f-c741-39e4-a5cf-3718ce5eab27 | -2.3463 | -45.5917 | 2025-11-27 04:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 48.3 |
| eeb3d5b2-80b1-3312-b4b7-4eea7e1ec509 | -2.3278 | -45.5698 | 2025-11-27 04:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| dea4ac5b-5d34-3524-87b6-2293040e4582 | -2.3277 | -45.5922 | 2025-11-27 04:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9ce386d5-3149-31b9-9655-423cee0d913e | -13.3848 | -51.164 | 2025-11-27 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 13a1df3b-5135-3be7-b38e-e50c8ebb3aea | -2.3463 | -45.5917 | 2025-11-27 04:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 52.3 |
| f2e2f31b-30b7-30bb-b410-9fd876f50419 | -2.7105 | -47.3929 | 2025-11-27 04:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c5828488-f9da-316f-9f7f-a96e6bc9a174 | -13.4037 | -51.1829 | 2025-11-27 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 7b205e5d-9208-3862-aca6-dba8eb1a560f | -13.4041 | -51.1615 | 2025-11-27 04:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| b646620e-3b89-35f3-ae1e-66c08f14a421 | -2.3464 | -45.5693 | 2025-11-27 04:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 4c00564b-8e23-38ff-9c57-cf31664deb46 | -4.7204 | -46.4497 | 2025-11-27 04:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 111.3 |
| c23e9c61-b378-3547-a8d9-f16331db52c7 | -2.3277 | -45.5922 | 2025-11-27 04:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 66d2a9bd-4167-3e37-ad34-94657bb332b4 | -13.4041 | -51.1615 | 2025-11-27 04:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f4c2e644-3f3a-3a55-80e7-8d9f493e2292 | -2.3278 | -45.5698 | 2025-11-27 04:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 459df4f5-5c49-39b1-9012-ac61d637e9da | -2.3463 | -45.5917 | 2025-11-27 04:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 8e64031c-a234-3735-98cf-91966567394e | -2.7104 | -47.4147 | 2025-11-27 04:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a0b22c12-b72f-348a-ab1d-730478eee6af | -4.7204 | -46.4497 | 2025-11-27 04:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 7687c695-5e5a-339b-8cc0-a418d9d02799 | -2.3464 | -45.5693 | 2025-11-27 04:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 35.5 |
| df3de764-66e1-3506-8ab5-71080cc81464 | -3.5269 | -43.6828 | 2025-11-27 04:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 39.5 |
| fb24d966-d290-38dc-be72-ef075a7a0f45 | -2.7105 | -47.3929 | 2025-11-27 04:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 214f2378-4b17-3f27-af8b-32864cd5bccb | -2.3278 | -45.5698 | 2025-11-27 04:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6cbc4f47-ce6a-3897-a03c-449e517c063c | -13.3848 | -51.164 | 2025-11-27 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a940f7e8-8918-31d4-b659-2782230462e5 | -3.5269 | -43.6828 | 2025-11-27 04:30:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 22bf7a3c-4203-32da-974b-cfc83fc12573 | -2.3277 | -45.5922 | 2025-11-27 04:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f7a9bc00-1be9-31d3-8487-41f6f8f1f006 | -13.4037 | -51.1829 | 2025-11-27 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| fa9c2466-075b-3e6d-9c1c-94c67b0ac228 | -2.3463 | -45.5917 | 2025-11-27 04:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 5378c2ca-7c13-3f5f-84f1-7e093388f1bc | -4.7204 | -46.4497 | 2025-11-27 04:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 76.8 |
| dcb6b9d9-768c-39d5-b621-9be625e82895 | -13.4041 | -51.1615 | 2025-11-27 04:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b91f11f5-9c10-3b40-9510-1776a19f1ec3 | -4.7204 | -46.4497 | 2025-11-27 04:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 087e5b00-7937-3aae-9852-4ffc8f1b150c | -13.4041 | -51.1615 | 2025-11-27 04:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.6 |
| e9c21d67-e09e-356b-9507-58538623f258 | -3.5269 | -43.6828 | 2025-11-27 04:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 253ce438-7ed2-3359-bcfb-3613ff5e5880 | -2.3277 | -45.5922 | 2025-11-27 04:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 28b77f91-2b77-3619-9694-3d40b42cf76f | -2.3278 | -45.5698 | 2025-11-27 04:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 16f9be8a-44b8-3ff5-8947-18351c321438 | -3.5268 | -43.7059 | 2025-11-27 04:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 0177a316-1a00-3bd5-bf57-5c6559f9f643 | -13.4041 | -51.1615 | 2025-11-27 04:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1c6af645-6615-3b7d-8e4a-3f331a60e7f3 | -4.7204 | -46.4497 | 2025-11-27 04:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| a8dc6c67-f7de-3902-a9b7-c3c62227dd85 | -2.3278 | -45.5698 | 2025-11-27 04:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 32.8 |
| ecf2999e-9d8d-3f1d-9455-5fbf1085c1d1 | -3.5269 | -43.6828 | 2025-11-27 04:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| d1ceb24f-67c7-313b-a292-a76722d52d56 | -3.5083 | -43.6837 | 2025-11-27 04:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| a7ac29a0-90f3-3097-a237-6b21a9830efb | -2.3277 | -45.5922 | 2025-11-27 04:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 44.8 |
| f729f8a8-947a-38bb-829c-a854c4a6f76b | -4.7204 | -46.4497 | 2025-11-27 05:00:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 5a71443f-6550-3f07-9ae4-7413b460d9cc | -2.3277 | -45.5922 | 2025-11-27 05:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| ab9327f1-28ee-39d7-87cc-64bfa04e119d | -2.3278 | -45.5698 | 2025-11-27 05:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 39.2 |
| cb30649f-153c-3c64-89ec-c62a4b4f74c7 | -3.5083 | -43.6837 | 2025-11-27 05:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 7a8c3bd7-1dbd-39bf-a291-ced4f19d9674 | -3.5269 | -43.6828 | 2025-11-27 05:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 106bd2b5-f6c3-3fe1-b9c8-e29cde50c157 | -2.3463 | -45.5917 | 2025-11-27 05:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6efc894f-74b7-3dca-a402-8e61ad27ea5c | -2.3464 | -45.5693 | 2025-11-27 05:00:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 39.1 |
| 4ab75a83-23af-3335-9a88-5bf1d9a08e12 | -2.3463 | -45.5917 | 2025-11-27 05:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 9eb09733-05a2-3259-833d-972904a641a6 | -2.3278 | -45.5698 | 2025-11-27 05:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 97.2 |
| e9be343b-6d95-3eca-bd3a-de50d7ef2e10 | -5.703 | -47.0532 | 2025-11-27 05:10:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 89808a85-14d5-3f50-97a4-19babe72ae3e | -3.5269 | -43.6828 | 2025-11-27 05:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5ee2bfde-7315-3b16-8a9c-e9ef06a0a426 | -2.3277 | -45.5922 | 2025-11-27 05:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 118.7 |
| 3985f238-ad71-3d76-a3b5-87869764da10 | -2.3464 | -45.5693 | 2025-11-27 05:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 4c5ee7f6-4538-3706-b811-91502b7c3104 | -13.4041 | -51.1615 | 2025-11-27 05:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| eea83e7c-72bb-3f69-8bf2-564be9c8fdba | -2.7105 | -47.3929 | 2025-11-27 05:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 96d8cb94-335b-338d-8665-8de55e1b2325 | -4.7204 | -46.4497 | 2025-11-27 05:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c73a1f8e-7178-3a39-bf8b-1f8b841c3684 | -2.3277 | -45.5922 | 2025-11-27 05:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 70a25857-7d39-3dd5-81d1-1aa685fe9915 | -2.3278 | -45.5698 | 2025-11-27 05:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 96aa5f04-30b6-354b-bf9b-323498a60b9b | -13.4041 | -51.1615 | 2025-11-27 05:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 57325b23-8532-38e7-8ebe-1861e62ecde6 | -3.5269 | -43.6828 | 2025-11-27 05:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 670153c1-0c43-361c-8d8a-66332a30dafa | -3.5083 | -43.6837 | 2025-11-27 05:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 9360b020-c4a9-34ba-8732-d074e457bf52 | -2.3463 | -45.5917 | 2025-11-27 05:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| e6eca5ee-6736-39a3-9393-7a616909b3d0 | -2.3277 | -45.5922 | 2025-11-27 05:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 4d86c0e5-d1e8-35d3-a604-b164c266ee45 | -13.4041 | -51.1615 | 2025-11-27 05:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| b4a4886c-6387-3f6f-8686-8f39298e25e9 | -2.3464 | -45.5693 | 2025-11-27 05:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| aec30b5c-1322-33ba-ab5f-9725fd0fd61d | -2.3278 | -45.5698 | 2025-11-27 05:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1c92e91c-b41b-368a-9366-5fc7027a8aff | -2.3463 | -45.5917 | 2025-11-27 05:30:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 3eb6bfbe-63e6-3634-b389-8b80d6af4e4a | -2.3278 | -45.5698 | 2025-11-27 05:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 842be75b-48f2-3042-981d-d1c0c822549c | -2.3277 | -45.5922 | 2025-11-27 05:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| f7961d3c-4913-3298-9bc1-0a38eb24ea22 | -2.3463 | -45.5917 | 2025-11-27 05:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a3bbdb0c-9e08-3631-932a-aca17e8e331c | -13.4041 | -51.1615 | 2025-11-27 05:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 0b9e86f0-1760-383b-ac6d-a66cd8bf223b | -2.3464 | -45.5693 | 2025-11-27 05:40:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f6ba43ec-9ca0-322c-badc-140813286f93 | -3.5083 | -43.6837 | 2025-11-27 05:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 41.9 |
| d3952f24-4a14-3cf1-9038-3c6a4956aca8 | -5.703 | -47.0532 | 2025-11-27 05:40:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 5b90ca81-a216-3a73-89e2-172fd5a1339d | -3.5269 | -43.6828 | 2025-11-27 05:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| dab18db6-3cff-3419-8f5a-5856a6ad432b | -3.52261 | -43.68423 | 2025-11-27 05:48:00 | AQUA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 5a455f0c-526c-3840-a2d3-1afbbbad66e4 | -2.70025 | -47.39024 | 2025-11-27 05:48:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c467a169-5117-371c-b547-2cc7a531a60e | -3.63686 | -44.86812 | 2025-11-27 05:48:00 | AQUA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e3fb4328-1a78-3700-83d1-e796a9066a49 | -2.92768 | -48.21127 | 2025-11-27 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dbd65a45-a674-34e8-bd56-0be559546ac8 | -1.48207 | -45.78995 | 2025-11-27 05:48:00 | AQUA_M-M | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d8a7cfea-edd6-37a6-978b-72c4b139d304 | -2.92487 | -48.22895 | 2025-11-27 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 93a079b5-e993-39e4-9966-acc3e5ff6350 | -2.92014 | -48.22279 | 2025-11-27 05:48:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 426eccde-823f-321a-87ec-a2910bd7bad1 | -2.69782 | -47.40573 | 2025-11-27 05:48:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| d33d9a7c-b2b5-3183-87ca-67db60b9a464 | -3.6353 | -44.87823 | 2025-11-27 05:48:00 | AQUA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 6e7204c9-d8e8-36f0-90fb-746fd98bf07e | -2.33378 | -45.58389 | 2025-11-27 05:48:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 206.6 |
| 0e04b4c0-86b3-3e8b-af04-6ea5bea948ce | -2.48468 | -47.82322 | 2025-11-27 05:48:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 46b46d7c-7d80-31a3-8e8e-2ee5705409d5 | -2.32556 | -45.57087 | 2025-11-27 05:48:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 0b41fa72-67ab-3ff1-91af-3862b73362ee | -3.13908 | -45.21992 | 2025-11-27 05:48:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2cce0724-50a4-3494-90fd-7b576dc33b63 | -3.51275 | -43.68541 | 2025-11-27 05:48:00 | AQUA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| dc80f9bb-e180-366f-ab77-238e66f1bba0 | -2.7527 | -49.32922 | 2025-11-27 05:48:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| c3e88308-1886-3daa-8012-2fb6da0f26f8 | -3.524 | -43.67518 | 2025-11-27 05:48:00 | AQUA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 811835e2-3c45-3a0e-b6b5-312cb8306163 | -2.33556 | -45.57238 | 2025-11-27 05:48:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 2e14343e-93c3-3c20-8e03-ce50aeb6c623 | -2.51589 | -45.0064 | 2025-11-27 05:48:00 | AQUA_M-M | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2af2d8bd-fc85-3202-979e-0b2a9dda504c | -3.51411 | -43.67636 | 2025-11-27 05:48:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| e89b2a09-80c9-3a7b-9478-2088d5fe4617 | -2.32377 | -45.58239 | 2025-11-27 05:48:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 1741f6b5-ee49-3c9e-ac24-a41ee8859800 | -2.3463 | -45.5917 | 2025-11-27 05:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 52.5 |
| acf0a2f5-3ad4-38d6-8c47-f8880e3b908b | -5.703 | -47.0532 | 2025-11-27 05:50:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 76994cf8-a143-3467-8d82-8116e2038ce7 | -3.5269 | -43.6828 | 2025-11-27 05:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 60200d8a-73a5-3c4b-99c0-8bb4bc5a263f | -2.3277 | -45.5922 | 2025-11-27 05:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 1e143abb-ec66-3631-87f1-33167fc16343 | -2.3278 | -45.5698 | 2025-11-27 05:50:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3be04712-a2d2-35bc-9a3d-23ff475fd007 | -5.69513 | -47.06475 | 2025-11-27 05:50:00 | AQUA_M-M | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |


[Clique aqui para ver as próximas entradas](README6.md)
