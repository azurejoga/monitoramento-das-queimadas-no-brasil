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
| 2c2a3f8f-e3a9-3e64-9875-1f36e167b751 | -6.1832 | -47.5915 | 2026-09-20 00:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 6924094d-d962-326b-bb2e-c0836f84cdf4 | -2.4636 | -49.2301 | 2026-09-20 00:30:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 558badc5-b8db-30ff-bd84-aa75f4e09de1 | -11.1369 | -54.0251 | 2026-09-20 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 721785bb-dfbd-3ef0-9abe-93ca7e121b00 | -5.841 | -53.5205 | 2026-09-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| b73e3f1b-a4e3-3656-a29b-c046612f8cbd | -7.3259 | -55.6153 | 2026-09-20 00:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 5eb7f9cf-91da-3c7c-8a5e-781ff4a61f7e | -2.8974 | -57.8181 | 2026-09-20 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| ef67b2ae-4b6d-3246-9b6b-5792239575bc | -5.8408 | -53.5408 | 2026-09-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| b5ff96cd-a899-3c2f-ace2-de348de919ab | -12.7428 | -46.183 | 2026-09-20 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 779f5919-6c90-3919-9e22-c9d1e17ebabc | -11.2307 | -54.078 | 2026-09-20 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| b8d22bd6-4b8e-3cfb-a0b8-956986df97bd | -11.0259 | -48.2944 | 2026-09-20 00:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| a14ff295-76c7-3023-92a8-c67806291d94 | -8.0279 | -61.3626 | 2026-09-20 00:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 38b43b14-86ac-3bf2-a071-76a955562bbc | -11.8547 | -47.6596 | 2026-09-20 00:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f4947aee-82e0-3b32-a07f-60d1db85d6d7 | -8.1686 | -54.7634 | 2026-09-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 0eae1766-bcb2-3e28-9e21-bfedcd77f0a9 | -11.0802 | -54.0302 | 2026-09-20 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 13b479d3-b86b-3f35-96f4-3d58a0273773 | -11.118 | -54.0268 | 2026-09-20 00:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.6 |
| 2e3a4579-7324-38b0-8e3a-32e7726ce0c8 | -7.5522 | -45.435 | 2026-09-20 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 10022ffc-0cdd-3bfe-a877-f2f6aabc5829 | -3.6946 | -60.6025 | 2026-09-20 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 65a346f1-e727-3824-8efb-351c93368166 | -5.4087 | -44.2644 | 2026-09-20 00:30:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 2108b3d8-540e-3537-baee-e69cf6c87290 | -8.1874 | -54.742 | 2026-09-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| c95fb0f8-f48c-3508-b8f0-74e65193d8aa | -7.5334 | -45.4367 | 2026-09-20 00:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| c1b921bf-fdce-30c9-aa73-77152b6f8b07 | -2.4636 | -49.2089 | 2026-09-20 00:30:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 4ef18823-d223-3d05-add9-0153057f8008 | -2.4451 | -49.2306 | 2026-09-20 00:30:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 11b5a033-ce92-3fa6-a2f3-ce119fea0f16 | -5.8595 | -53.5196 | 2026-09-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.8 |
| a4851d69-5765-37d0-8321-fdfb26f88079 | -5.8593 | -53.5399 | 2026-09-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 3b4d78fc-c584-31c2-afe6-c1e113957e2e | -3.6946 | -60.5835 | 2026-09-20 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 06745517-34e8-3cf4-a57d-d971807949a3 | -8.1688 | -54.7432 | 2026-09-20 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 3ad5a4ce-3b3b-3ba9-877e-d4daeb5a1df1 | -13.0177 | -46.9125 | 2026-09-20 00:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| e85f58c3-3ad3-369a-a6d3-77d0228e1f1f | -2.8791 | -57.799 | 2026-09-20 00:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 0bfc581b-07b2-3172-aa36-cb2db336cc2f | -3.6945 | -60.6215 | 2026-09-20 00:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ccb780cf-d32c-3b99-83a7-300ed213ab5d | -12.8896 | -50.991 | 2026-09-20 00:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 79e54b41-cca0-3457-8a1e-2b52ad3174d0 | -2.4451 | -49.2093 | 2026-09-20 00:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| d10f5b64-e25d-3082-a954-b028d475859d | -14.6856 | -46.6886 | 2026-09-20 00:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 5abff371-6376-3644-805e-8fe568f1740e | -7.5284 | -45.8885 | 2026-09-20 00:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 9316b68d-5740-3dec-b1dc-a9735e69ccff | -11.118 | -54.0268 | 2026-09-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 142.4 |
| 654419d7-7fb3-38c6-89a7-d1bd6b1a4f12 | -3.6945 | -60.6215 | 2026-09-20 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 93e76c77-36a6-3c27-bc08-6c9119be2c09 | -2.4636 | -49.2301 | 2026-09-20 00:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 63df868e-d3c2-3190-97a3-3151e36f75f6 | -11.1369 | -54.0251 | 2026-09-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a6f95049-12a4-3eb7-bbf6-fd50c1487391 | -7.3073 | -55.6163 | 2026-09-20 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 41.0 |
| 629069a2-816d-3345-9670-fd9167fc214e | -2.8974 | -57.8181 | 2026-09-20 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| d34d727f-c211-341a-89af-d2cc32816837 | -7.3259 | -55.6153 | 2026-09-20 00:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 193ce721-5313-3b71-880e-26bd0165ca2b | -8.1688 | -54.7432 | 2026-09-20 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 372981d3-f120-3706-a88c-b85ee2befc80 | -7.5522 | -45.435 | 2026-09-20 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| d83568e6-2d79-3992-8be4-2228302b14f2 | -12.7629 | -46.1343 | 2026-09-20 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 49666b82-1f65-3498-a21b-efcb017682fe | -7.4286 | -44.7409 | 2026-09-20 00:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 136678b3-9a66-3737-913f-a79189f80fe4 | -6.1832 | -47.5915 | 2026-09-20 00:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 670d19d9-5d23-3a5b-b1c3-009814b4f403 | -11.8739 | -47.657 | 2026-09-20 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| ca6bf403-607d-3297-9f80-fa972a2fdb49 | -12.8896 | -50.991 | 2026-09-20 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 97.4 |
| b2faf811-9029-32ef-a5e3-c4ff6dfb2712 | -11.0991 | -54.0285 | 2026-09-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 25afa3d4-a3a3-357c-be7e-08c7234bf391 | -2.4636 | -49.2089 | 2026-09-20 00:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 680434ca-4bf3-3ec5-a253-f77b3fb84ab2 | -11.0802 | -54.0302 | 2026-09-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 2cab6797-742f-38db-88ad-81dd68cce0d3 | -8.1872 | -54.7622 | 2026-09-20 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| fa7feb32-6902-39f0-a423-57f96c977752 | -9.0096 | -44.9209 | 2026-09-20 00:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 15c0ab55-9fb2-3495-b56e-876e5b64e668 | -2.4451 | -49.2306 | 2026-09-20 00:40:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 99a4df4f-fdb6-3c8c-9b5e-043dd90e2927 | -9.0093 | -44.9438 | 2026-09-20 00:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 3070e3f7-427b-385d-b9aa-9eb161ce02b8 | -6.2018 | -47.5902 | 2026-09-20 00:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 8e78f785-9aca-3030-98d4-a4dafd5ee1ef | -13.0177 | -46.9125 | 2026-09-20 00:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 20f0ee50-0d0c-32c5-880d-dd67097f457e | -6.183 | -47.6133 | 2026-09-20 00:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 9ee8ce27-fa81-37f6-8c89-23d28c073aa7 | -6.9498 | -62.9166 | 2026-09-20 00:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 1a94dbfc-57ce-3cac-a41d-f436e77665d1 | -8.8097 | -60.7926 | 2026-09-20 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| f389e97f-db38-3e58-bbcf-1d0cb7462cb9 | -12.7428 | -46.183 | 2026-09-20 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 60fbcbdc-a729-3403-9a5c-044135d87a48 | -7.5525 | -45.4123 | 2026-09-20 00:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e09a8f3b-28c4-38e7-93c4-0e9f301a5829 | -11.8547 | -47.6596 | 2026-09-20 00:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 0bffd977-40af-3095-a125-1400ae899e18 | -11.2307 | -54.078 | 2026-09-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.9 |
| d89d3d0e-3455-35c9-b3a3-64f31e57dd49 | -6.2024 | -47.5245 | 2026-09-20 00:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 0ae9ee6b-905b-3fce-ad8e-cd2526bd9406 | -12.8893 | -51.0124 | 2026-09-20 00:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.9 |
| e5689aac-3759-3d8c-8d4c-429dfea3ffdf | -6.2017 | -47.612 | 2026-09-20 00:40:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| ffaa2d3a-841b-3c3d-8ce4-1890da1b8d89 | -3.6946 | -60.5835 | 2026-09-20 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 831378a6-6575-389c-a433-04f45aec561d | -2.8791 | -57.8184 | 2026-09-20 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 9e8a07d5-5da1-3547-8b12-5f5c90aef309 | -8.7911 | -60.7935 | 2026-09-20 00:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| acb00890-6755-3de3-875c-746b836eaf37 | -8.1874 | -54.742 | 2026-09-20 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| bd602a55-859c-3e5f-8018-2c0a48f4b1fe | -11.2118 | -54.0797 | 2026-09-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| d2bab26f-7530-3a0e-a00c-c181fa5f35c0 | -11.041 | -54.1567 | 2026-09-20 00:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 9a6f0a13-a6d2-393c-8282-44e19a364123 | -9.0286 | -44.9187 | 2026-09-20 00:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 00890ab3-ba49-30cb-a939-97d3b7555459 | -8.1686 | -54.7634 | 2026-09-20 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| def0bee7-57f8-3c53-b4e7-13e2ece9aa37 | -2.8791 | -57.799 | 2026-09-20 00:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| d351b522-a353-322d-9184-f192807862a9 | -9.131 | -45.7273 | 2026-09-20 00:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| d4dfb400-32df-36e8-9533-408e09f86868 | -3.7453 | -51.8288 | 2026-09-20 00:40:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 25cbcedd-652d-316e-8fe7-a154d0c5d11e | -3.6946 | -60.6025 | 2026-09-20 00:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 50929d0e-ef9f-3f92-af3d-b6e3f56ecdb1 | -2.4636 | -49.2089 | 2026-09-20 00:50:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| d8e8871b-cc6d-379b-8854-3d497dc3f8f4 | -13.037 | -46.9096 | 2026-09-20 00:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.7 |
| dda36d4b-a9ed-325c-b527-da4fb0da9032 | -11.0802 | -54.0302 | 2026-09-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a677776a-9303-3bef-b3e3-da20eea3f603 | -11.8679 | -46.8755 | 2026-09-20 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| cf9112f1-7d1c-3e8a-b009-7ad318d0ea96 | -2.8791 | -57.8184 | 2026-09-20 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d873721b-2709-3c4f-ab03-faa6c763bd1b | -3.7453 | -51.8288 | 2026-09-20 00:50:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 3af0dc9c-fcc3-3ced-b6c4-49d69ff3313b | -3.6946 | -60.6025 | 2026-09-20 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 3abceaba-11ad-37f9-9388-088330330b83 | -9.112 | -45.7294 | 2026-09-20 00:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| c2443369-34dc-37cb-bd5f-cd5397cb59f1 | -6.2017 | -47.612 | 2026-09-20 00:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 50bbf073-bea9-3fd0-be45-7f70fe4f5e1d | -2.4451 | -49.2093 | 2026-09-20 00:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| ebcde780-c418-3d54-b01c-8c8b3b3b5af0 | -7.5522 | -45.435 | 2026-09-20 00:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 33b88731-7c73-3401-8381-a414ecedc6b8 | -2.8791 | -57.799 | 2026-09-20 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 2e9688a1-42e4-3a17-9c89-029e1e52d82e | -12.1332 | -47.0185 | 2026-09-20 00:50:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 742dd6d6-2ab4-37f6-8d07-fc05d3a0d9ff | -11.0991 | -54.0285 | 2026-09-20 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 141.4 |
| 464c4e68-b9ee-3e6f-a1ef-4ab0c9e9d8a0 | -7.5284 | -45.8885 | 2026-09-20 00:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 73c7712e-ebd6-3714-9d7d-30dc5e573dea | -6.1832 | -47.5915 | 2026-09-20 00:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 2447c71d-902d-30ab-9034-2e2e46cb9e88 | -2.8974 | -57.8181 | 2026-09-20 00:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e92cc80d-6dbb-3de3-9309-b58046f0fd62 | -14.6856 | -46.6886 | 2026-09-20 00:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 105.9 |
| db2b51d2-6b63-36b4-952c-75550f47e248 | -8.1872 | -54.7622 | 2026-09-20 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 92007317-46c5-3990-a0fe-974040dbeabc | -11.8491 | -46.8556 | 2026-09-20 00:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 75a760d7-08c5-3d0b-9bd9-93259ffa489e | -6.183 | -47.6133 | 2026-09-20 00:50:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 72230c7e-5d34-3d31-8ff5-d44a4189d1b4 | -12.7621 | -46.18 | 2026-09-20 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |


[Clique aqui para ver as próximas entradas](README4.md)
