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

## Dados Diários - Página 147

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2498b15f-316b-3e35-b4b0-4a96f521a6eb | -2.5687 | -57.5135 | 2026-09-23 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 149d8366-da24-3ec7-bb23-6568c07dff1d | -6.5763 | -45.4968 | 2026-09-23 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 9e43f239-e4f2-3893-b4ca-d307397a0fc3 | -8.4472 | -47.648 | 2026-09-23 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| aa80ed71-c0c8-3c49-ba42-1974e7a3768c | -11.4209 | -47.3603 | 2026-09-23 15:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 211.5 |
| 439aaa59-fec6-3f79-abe9-d5da4bf53237 | -7.2994 | -59.5343 | 2026-09-23 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 4ce390b7-2b8f-31df-ba63-eb9763b37124 | -2.8792 | -57.7796 | 2026-09-23 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| dd3fb17c-4523-3772-8129-71244dbb7013 | -1.9088 | -58.2589 | 2026-09-23 15:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 8cafb021-8c5c-32e6-9800-783957e14c4a | 1.5285 | -55.8651 | 2026-09-23 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3380515e-9c17-3e67-9614-4a84d7551f7a | -1.8218 | -55.7234 | 2026-09-23 15:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 6f98f585-52af-36ed-9cbc-d7e97c5eb452 | -3.7167 | -54.1896 | 2026-09-23 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| dc51e464-5824-35fb-8a0a-b75216548c48 | -9.5542 | -47.9549 | 2026-09-23 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 212bcbe5-bb30-30c9-87aa-18418b73a913 | -6.5953 | -45.4727 | 2026-09-23 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 2575585b-094c-3c04-abf9-da80b8ab350c | -6.4671 | -59.9711 | 2026-09-23 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| e56b2610-0f70-38ed-8f6e-0ed1cf49f422 | -6.3015 | -59.9387 | 2026-09-23 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 980acd3b-948b-384c-bcf0-2a36349b01c6 | -9.8118 | -48.453 | 2026-09-23 15:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 153ce54d-2fe0-3b98-b68e-af875bea13d0 | -6.6357 | -45.1752 | 2026-09-23 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 26d0221c-1be5-3c25-b717-0b1fff27f244 | -6.4671 | -59.9711 | 2026-09-23 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 97cc9b2e-f349-3ed8-b4a7-b4f6cff069d0 | -6.5451 | -44.8643 | 2026-09-23 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| a196cbe7-0088-39d8-b202-67ae9de56144 | -6.5056 | -45.0723 | 2026-09-23 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d06607f6-7f87-329d-ada3-a014b2ac7469 | -6.6332 | -59.9073 | 2026-09-23 15:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 1ef90c11-941f-3272-8ad3-f26f6ab21cec | -6.5963 | -59.9087 | 2026-09-23 15:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| acec0a09-9426-3248-a548-423f44d1f98a | -8.4985 | -57.6075 | 2026-09-23 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 225.4 |
| 643164e1-1d89-3ee1-b63b-9a6ff57e922f | -2.5687 | -57.5135 | 2026-09-23 15:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| ae3dfd7e-37f0-3664-937f-f27ec67ee29d | -6.2832 | -59.9202 | 2026-09-23 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 003ced5e-4fc4-33e9-b470-3c21f9aa97bd | -8.8735 | -49.7328 | 2026-09-23 15:40:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| f866220f-8924-3329-bb5c-bcb5a015a875 | -7.6448 | -57.6337 | 2026-09-23 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 2616718b-f86c-3bc3-b360-cd0dae817516 | -1.3373 | -49.3159 | 2026-09-23 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 2fd3c619-f8a1-3caa-a397-3347a4ce6e91 | -2.7713 | -57.0229 | 2026-09-23 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 293629dc-573f-3696-ae0e-cc59f9daa383 | -2.7713 | -57.0424 | 2026-09-23 15:40:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| c94ea2b3-7429-32fe-8a77-cfbec894a7d3 | -4.2632 | -55.4303 | 2026-09-23 15:40:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 13e8ff05-7117-3320-93e5-7158dc8160fa | 2.0711 | -50.9631 | 2026-09-23 15:40:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 420f488b-604a-3486-9a01-b17cc278a9cf | -5.4179 | -60.2166 | 2026-09-23 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 73fe117f-12f3-3381-a4ee-47ef414ceb0d | -3.3367 | -57.8673 | 2026-09-23 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 43c703dc-70d2-3f2d-9c19-aec621639a43 | -1.4303 | -48.9316 | 2026-09-23 15:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 6705e1bd-eb19-35a6-bfd2-d49f0384d8b6 | -3.3183 | -57.8677 | 2026-09-23 15:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 932ee500-5863-3100-a1c1-4512db1ad2c8 | -1.3557 | -49.3157 | 2026-09-23 15:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| d857da20-4a2c-3a9d-b269-28212abe7fc9 | -6.5953 | -45.4727 | 2026-09-23 15:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| cca9798d-cd09-31fa-9976-f0a9ffa55f31 | -8.4983 | -57.6271 | 2026-09-23 15:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 44370983-6d31-3984-823c-2036a623b648 | -6.3383 | -59.9374 | 2026-09-23 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 12605d4c-b1d5-3bd9-b7e6-aea2957ad28d | -6.3199 | -59.9381 | 2026-09-23 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 149.1 |
| cf956260-b947-3f4c-920c-ec13cf61f303 | -6.4487 | -59.9526 | 2026-09-23 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| c020dc0d-c4c9-379d-96db-91ae3943d807 | -5.1606 | -60.3005 | 2026-09-23 15:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 26bc0cde-00e7-3764-8c9f-3e3f20c98675 | -3.3726 | -58.0796 | 2026-09-23 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ab952625-42a8-3b9d-8efd-d9a672fe4bf0 | -6.5953 | -45.4727 | 2026-09-23 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| dea217ec-1a5c-3ee0-bfd9-6465ffa59887 | -3.4279 | -57.9816 | 2026-09-23 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| a7953ccd-fb4d-352e-a2fc-32fa58abd187 | 1.4085 | -50.7451 | 2026-09-23 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 52.0 |
| a8e8445d-e9e2-37ca-a9aa-2348d2643d41 | -2.7332 | -57.6077 | 2026-09-23 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 4dd0d520-ec99-302d-977c-ec07d466d4f7 | -2.7713 | -57.0424 | 2026-09-23 15:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| f2e9fd09-5fa6-3301-878c-30096594f74a | -6.5442 | -44.9555 | 2026-09-23 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| b512f8c5-2555-30b3-a0f7-d4673c1ff8eb | -3.4096 | -57.982 | 2026-09-23 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 1816a745-4875-3888-af8b-df64e2ca53d8 | -3.3367 | -57.8673 | 2026-09-23 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 87d85af9-04a7-336a-83c2-78cb936f13cf | -6.8916 | -59.8397 | 2026-09-23 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 79bf091c-af6f-385f-ac7d-68d3e7988877 | -2.8805 | -57.2938 | 2026-09-23 15:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 26979f09-a0a3-3e14-bfc1-d770476e77b2 | 1.5287 | -55.727 | 2026-09-23 15:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| c93755da-7140-3277-bd4f-c66351adbbc3 | -8.8735 | -49.7328 | 2026-09-23 15:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 3fcd8f9c-5133-3019-a019-e8b070ede05e | -1.4487 | -48.9526 | 2026-09-23 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 27eddc57-a703-36e7-9da3-56d7d83d31d0 | -6.3199 | -59.9381 | 2026-09-23 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 135.4 |
| b436c558-7215-3d28-b9fc-05b590098f8b | -2.7713 | -57.0229 | 2026-09-23 15:50:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 209912d6-0b5d-382d-bbf3-56fb32638c52 | -1.9271 | -58.2587 | 2026-09-23 15:50:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 9a192814-fae8-39db-b256-b81813056019 | -1.4302 | -48.9529 | 2026-09-23 15:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 57bce09c-daf9-3fc5-a47d-cd782349dd2b | -6.2832 | -59.9202 | 2026-09-23 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| ff41759e-f349-3dcb-affa-1a58fb1bced5 | -5.4179 | -60.2166 | 2026-09-23 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2f0a31ff-9315-383c-bfc5-3d70d81d97e7 | -6.4671 | -59.9711 | 2026-09-23 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 2966c6f6-a82f-308f-b9d2-716eef32ecf3 | -6.3383 | -59.9374 | 2026-09-23 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 917f08a6-4b87-321d-bc8e-a68d18dd42c9 | -6.5444 | -44.9327 | 2026-09-23 15:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 373db757-3a99-30ec-a062-f2e1f099cdf6 | -6.4487 | -59.9526 | 2026-09-23 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 9dcd73c1-f971-3d39-948a-06ef17451a7a | -7.2996 | -59.5151 | 2026-09-23 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| a71a003a-5874-36f3-9192-9585010459e1 | -2.5687 | -57.494 | 2026-09-23 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 995a30c6-15c4-32a1-8d2e-f1f55d44989a | -5.9153 | -59.9139 | 2026-09-23 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 155.4 |
| bcbda1f7-5d9b-3ef7-abc1-9e32da1e6ec2 | -9.5731 | -47.9529 | 2026-09-23 15:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 954d3305-d4fa-3b0f-9529-5ce24fbbc255 | -8.3393 | -47.2396 | 2026-09-23 16:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 116.7 |
| cedd7433-d87e-3c70-a1c4-5400e95e393e | -1.0244 | -48.8087 | 2026-09-23 16:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 73579709-5e30-3ea5-be60-c69cb28b8fe2 | -1.4302 | -48.9529 | 2026-09-23 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| d2f95289-9a0e-377f-8f38-1e0290191eb5 | -6.5446 | -44.9099 | 2026-09-23 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1eb8dd7a-9d7f-3713-ae2a-d6a832d7123a | -6.3383 | -59.9374 | 2026-09-23 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| f5301472-7985-3152-82d5-5cf9ba6c459f | -5.9153 | -59.9139 | 2026-09-23 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 153.7 |
| ef709b15-2dde-3ba0-9f4b-856c06052e97 | -1.4487 | -48.9526 | 2026-09-23 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| ef05331c-0840-3531-9a2a-48eb61edcb83 | -5.6223 | -43.3701 | 2026-09-23 16:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5f89fdac-ccfb-3c74-9cc2-441d3e2570ec | -6.5259 | -44.9114 | 2026-09-23 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 537a5e29-5f51-3d1a-b7b4-191e22bc5e1a | -3.3367 | -57.8673 | 2026-09-23 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 3e02864b-0df7-3fcc-94b8-8a5e0aca15aa | 1.5287 | -55.7468 | 2026-09-23 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 4638f3fe-3385-34f0-a891-9784fa361965 | 1.4453 | -50.7655 | 2026-09-23 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 42bc2a4f-c888-3dc8-a241-c1b53805cdf3 | -5.9337 | -59.9132 | 2026-09-23 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| ee1804c6-ebf1-3777-92ae-5edba4cf39aa | -3.3914 | -57.9436 | 2026-09-23 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| dd3ccd29-44a5-3b14-9548-36349caafadc | -2.5687 | -57.494 | 2026-09-23 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 6c19a891-5990-339d-b561-0348ab5ea373 | -1.3933 | -48.9534 | 2026-09-23 16:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 4b3de27f-52b7-3fff-89ce-a330bad644db | -3.4279 | -57.9816 | 2026-09-23 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 1e98959d-de6a-33a7-9368-e9fd4fd87939 | -6.5444 | -44.9327 | 2026-09-23 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 4a28715c-0264-301e-8dd9-5a6f788bb765 | -6.5449 | -44.8871 | 2026-09-23 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 4f3b94c9-391d-3fb7-a536-306f8f3da951 | -6.5953 | -45.4727 | 2026-09-23 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 1d4ddf2b-89d8-337e-a5f0-f9836d9acf63 | -2.7713 | -57.0229 | 2026-09-23 16:00:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 31c0b93d-5f0e-3c07-895c-6179dd6fea30 | -3.4095 | -58.0013 | 2026-09-23 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e621343a-b8f5-3ac0-a6ae-06acb4f3ee47 | 1.5102 | -55.885 | 2026-09-23 16:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 790dcaa0-ae8d-3234-8d5d-66f67919a6bc | -6.5451 | -44.8643 | 2026-09-23 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| fe92e2b4-8fc0-3bb0-bf4a-c4ece4b6f07e | -6.5261 | -44.8887 | 2026-09-23 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 09be3ea4-eab1-3218-8348-65ddd3922e09 | -3.4096 | -57.982 | 2026-09-23 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4c6e44d2-ab4f-31a5-abd8-3a3d9ae89214 | 1.9056 | -50.8414 | 2026-09-23 16:10:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0810fd5e-138e-343f-a560-07869df57e04 | -6.5634 | -44.9084 | 2026-09-23 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 719b019b-20ed-33ed-b1a4-a4124d39bad4 | -7.5891 | -57.6561 | 2026-09-23 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 815cd914-30a8-326d-8193-b495128005d0 | -6.5444 | -44.9327 | 2026-09-23 16:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 80.9 |


[Clique aqui para ver as próximas entradas](README148.md)
