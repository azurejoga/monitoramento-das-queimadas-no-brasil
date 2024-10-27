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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6fecc7f-a837-3f43-8b33-cb18e790f525 | -3.0913 | -51.239899 | 2024-10-27 00:14:56 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f898d66-57de-3f79-b05d-27d857625b2c | -1.9999 | -46.376701 | 2024-10-27 00:14:56 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 939082dc-d2e5-3c71-b6aa-79cbdf9d94f1 | -2.6326 | -49.2113 | 2024-10-27 00:14:56 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29265b2c-575b-3b62-ac5f-8626d290a973 | -2.635 | -49.222099 | 2024-10-27 00:14:56 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf58b288-c1d3-3fb3-8250-e996c19da04d | -2.6374 | -49.232899 | 2024-10-27 00:14:56 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 441dc281-6728-321b-ade9-5897677611aa | -2.6543 | -49.308998 | 2024-10-27 00:14:56 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 566fac67-1b5b-3014-ac28-1ae76d1a375c | -2.4501 | -48.482498 | 2024-10-27 00:14:56 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 579e1b43-a973-3548-8c2b-a8ad80bf67c8 | -2.4522 | -48.4921 | 2024-10-27 00:14:56 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec93ecd1-00b1-3552-8ed7-36b5abc4d381 | -2.5618 | -49.215401 | 2024-10-27 00:14:57 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb715ac-2bd1-3c9e-8bb6-c8a3f9e100c2 | -3.3111 | -52.613701 | 2024-10-27 00:14:57 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4270eeca-45e2-3802-a35d-92ec90a21caa | -1.9724 | -46.621399 | 2024-10-27 00:14:57 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05336d04-7915-3a72-9da9-1e2f30348b2b | -1.9741 | -46.629002 | 2024-10-27 00:14:57 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cc4e8b1-a905-3449-ae8d-2a8293853417 | -3.6583 | -54.254902 | 2024-10-27 00:14:57 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c1973ca-4d48-3f3f-b7e6-bee4f1ba6e4f | -2.1137 | -47.298 | 2024-10-27 00:14:58 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdae4f5b-7fb7-3c64-8776-d8382c8729ae | -2.1155 | -47.306198 | 2024-10-27 00:14:58 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30d439f4-a74b-3f2e-9fad-a2b587cbcae1 | -2.4821 | -49.087898 | 2024-10-27 00:14:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 308717b4-796d-3017-a79b-0b85f441c5dc | -2.4845 | -49.0984 | 2024-10-27 00:14:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20a5e9e7-dda1-36a0-8116-b6b099ccc992 | -2.6065 | -49.648102 | 2024-10-27 00:14:58 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac80186d-ae7d-33b7-b8a7-b9f5c96f62e5 | -2.6091 | -49.659599 | 2024-10-27 00:14:58 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 973a3477-35c4-3d02-948a-0dacc55086de | -2.47 | -49.079498 | 2024-10-27 00:14:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fd3be8c-3792-3df2-8ed7-457c0c9cbd6c | -2.4724 | -49.09 | 2024-10-27 00:14:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a30ef55c-7d52-3d36-9069-9ff834a692a1 | -2.4626 | -49.092098 | 2024-10-27 00:14:58 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1be03923-0b23-3028-a50e-3a6b485bfac8 | -2.173 | -47.931198 | 2024-10-27 00:14:59 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7703078d-13a2-340d-8008-84714ee4e3ff | -2.1632 | -47.9333 | 2024-10-27 00:14:59 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| daee8851-248d-3002-9cf8-502d146b7e39 | -2.1652 | -47.9422 | 2024-10-27 00:14:59 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1a87e84-e2eb-3f20-a62a-7532ca21b628 | -1.7936 | -46.374901 | 2024-10-27 00:14:59 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f60533c-29a7-3b77-a5ee-4c5b66342feb | -1.7969 | -46.389801 | 2024-10-27 00:14:59 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90edf24d-0f97-30d7-82b4-a1bdee8b2dad | -1.7838 | -46.377102 | 2024-10-27 00:15:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43d73131-1b7c-34d4-a2fc-72eb1426ff98 | -1.7855 | -46.384602 | 2024-10-27 00:15:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd28b6f4-a290-316b-a340-1268ba02c313 | -1.7871 | -46.391998 | 2024-10-27 00:15:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2f2f18a-f3fb-392f-b65f-7bc990975edd | -2.8155 | -51.008202 | 2024-10-27 00:15:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2287ea99-6b4e-373d-9e61-142ca712a5e6 | -2.9203 | -51.715199 | 2024-10-27 00:15:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a384f66c-95a5-3dde-a974-413f08d47388 | -2.9239 | -51.731201 | 2024-10-27 00:15:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3332f51-7610-3d81-af86-39158173a706 | -2.9071 | -51.701199 | 2024-10-27 00:15:01 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6e022e7-f0ba-31e4-812b-da611c073761 | -2.9106 | -51.717201 | 2024-10-27 00:15:01 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94225a26-0e6f-3758-8db1-e30da492874a | -2.9142 | -51.733299 | 2024-10-27 00:15:01 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17a37d82-2543-35a0-a0d0-5a89a632878f | -2.9177 | -51.749401 | 2024-10-27 00:15:01 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7d6d3f8-d94e-3bf7-bb60-8cb9b1b3aa3e | -2.378 | -49.357601 | 2024-10-27 00:15:01 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed7b2290-4ed2-323f-ade4-81f862cee67e | -2.1621 | -48.434799 | 2024-10-27 00:15:01 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe6a4720-c0c3-30f9-a826-0125197776b2 | -2.1503 | -48.427502 | 2024-10-27 00:15:01 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd0e7ce7-a9ed-3cf5-bd58-b3d5c1f1d506 | -2.1524 | -48.437 | 2024-10-27 00:15:01 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29419b34-de79-305c-becb-eb675c8fe495 | -2.1545 | -48.446499 | 2024-10-27 00:15:01 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88f4330d-b9c6-3c63-aa1b-cf977982261a | -3.4604 | -54.508301 | 2024-10-27 00:15:02 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cde5ffd7-3b68-3203-9932-bb5012281444 | -3.466 | -54.5341 | 2024-10-27 00:15:02 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 730b5ef0-8deb-363f-99a6-46a286345f84 | -3.4507 | -54.5103 | 2024-10-27 00:15:02 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f5677dd-c6c7-3b8d-b96d-246cfe790cbe | -3.4563 | -54.536098 | 2024-10-27 00:15:02 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69026876-1cb9-326c-9f86-1188c5043053 | -1.6636 | -46.529701 | 2024-10-27 00:15:02 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a334291-730e-350f-917d-bf19ebb1216a | -1.6653 | -46.537201 | 2024-10-27 00:15:02 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64d059b9-2f10-3fdf-8e44-926db71452c7 | -1.667 | -46.5448 | 2024-10-27 00:15:02 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bda47fc-0f97-3498-af31-4cb88be27c98 | -2.83 | -51.768299 | 2024-10-27 00:15:02 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed45caa-8b02-3539-a77d-85a5d1e30df4 | -2.8336 | -51.7845 | 2024-10-27 00:15:02 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2624429-29d2-32cc-b5d0-249f7075989d | -2.4749 | -50.254902 | 2024-10-27 00:15:02 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85df4b78-dc11-3619-91dc-6f031d110254 | -2.4777 | -50.267502 | 2024-10-27 00:15:02 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7e0c991-0475-35dc-8104-4c04c962493c | -2.4651 | -50.257 | 2024-10-27 00:15:03 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 957f4df5-a41c-3eb0-b288-b96ddce68e82 | -2.4679 | -50.2696 | 2024-10-27 00:15:03 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8808bf4c-2d1a-3f6c-adf5-8ef53ff236af | -2.4514 | -50.379398 | 2024-10-27 00:15:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3081b41d-4417-30cd-948e-8ec7bfa1a215 | -2.4542 | -50.3922 | 2024-10-27 00:15:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c030f555-69fa-3b6a-ba57-ab52586a5142 | -2.4416 | -50.3815 | 2024-10-27 00:15:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d287fb2-180c-3732-bd7c-897a0a55290a | -2.4444 | -50.394299 | 2024-10-27 00:15:03 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c96ce5bb-6da9-36c7-bdd2-ce1c5caaae0a | -2.9569 | -52.9925 | 2024-10-27 00:15:04 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52500ebd-8203-377f-a795-c0ef6158ac5c | -2.9612 | -53.012299 | 2024-10-27 00:15:04 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7181832-f611-3f23-a98c-6f9dcc78c68c | -2.5486 | -51.141102 | 2024-10-27 00:15:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d469c949-5111-38fa-a81d-3b4069b7e884 | -2.5518 | -51.155602 | 2024-10-27 00:15:04 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9339f42-3d20-3f1b-b73d-e45862142aa1 | -2.5357 | -51.128799 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75e1b872-2bed-3510-912d-fd1905802a54 | -2.5389 | -51.1432 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1522fa64-20d1-37a3-a6d8-709913d645ed | -2.5421 | -51.1577 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36dab12f-4a1b-3ef9-9a14-64aaea367c63 | -2.5453 | -51.172199 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efc1aa36-2892-3c53-8b9f-25908990634c | -2.9472 | -52.994499 | 2024-10-27 00:15:05 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d6dc694-c4ab-3ea6-acac-b3037c868f9b | -2.9515 | -53.014301 | 2024-10-27 00:15:05 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a4353cf-bd80-3aff-b5b4-9db47694d285 | -2.5259 | -51.130901 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ada746-61a4-3448-ba73-2d4398c83e9d | -2.5291 | -51.145302 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2414dd4b-d568-3a73-a3f0-cd8f4329692a | -2.5323 | -51.159801 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fbac7d6-0f14-3d38-9916-90e3d6510dfb | -2.5355 | -51.174301 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a8c4588-189d-313b-8e0c-b23707b1d5e1 | -2.829 | -52.503799 | 2024-10-27 00:15:05 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 355f4202-2b6c-3abf-b2d8-df466e6b55bd | -2.833 | -52.521999 | 2024-10-27 00:15:05 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0901b32d-8e28-3ec8-a3a4-a3ad10adac18 | -1.9681 | -48.669102 | 2024-10-27 00:15:05 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64e05a16-5d81-31ae-8532-b6eccf46146d | -2.5161 | -51.132999 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e120df8-ebf4-3ef3-bef2-5ef8af47fbc8 | -2.5193 | -51.1474 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 370f4dce-54d7-3959-96fd-bdfd8d1cd8e9 | -2.5225 | -51.1619 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 505f7197-777e-3bba-b0a3-aa74d11ca68c | -2.5064 | -51.135101 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b779c0d0-3046-33b9-b3ab-a3c8345aa688 | -2.5096 | -51.149502 | 2024-10-27 00:15:05 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 494ac08c-43e7-3bc5-bf77-ffdb3d74507d | -3.0698 | -53.785599 | 2024-10-27 00:15:05 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f2dfa57-12b0-3ba2-b0cd-301a981f4225 | -2.5919 | -51.752399 | 2024-10-27 00:15:06 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0084d762-c0dd-332f-b429-ae147632ad6f | -1.5234 | -47.188801 | 2024-10-27 00:15:07 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b649c844-e83c-32d7-a138-203a35849d22 | -1.5252 | -47.196899 | 2024-10-27 00:15:07 | METOP-B | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8e69b69-ec4a-36a5-8810-dc736435c196 | -1.7885 | -48.417599 | 2024-10-27 00:15:07 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abb54d39-fa0a-3a2c-861a-0a0ebf3912c5 | -1.7906 | -48.426998 | 2024-10-27 00:15:07 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b349e979-06b2-342a-8747-4aa58b7a199d | -1.7788 | -48.4198 | 2024-10-27 00:15:07 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e144d7ba-3d29-3cea-bb44-24371a6b389f | -1.7809 | -48.429199 | 2024-10-27 00:15:07 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 552c655e-a76c-31f6-8576-231821902518 | -2.2573 | -50.611801 | 2024-10-27 00:15:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 606a0883-ec25-3469-87eb-6ff5bc51354d | -2.2603 | -50.625 | 2024-10-27 00:15:07 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a9d7962-43ea-3762-8e14-a1377fe9fcf6 | -1.7995 | -48.6045 | 2024-10-27 00:15:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46b1aec0-80ab-3aca-aafa-2f728ed70b4f | -1.8017 | -48.614101 | 2024-10-27 00:15:07 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43af41fd-628e-369e-8b04-3cfab3945617 | -2.8398 | -53.292599 | 2024-10-27 00:15:07 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa1660c-6254-39d0-9b71-d57298ff42b3 | -0.9815 | -53.7192 | 2024-10-27 00:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.6 |
| f5fa0f85-a19a-309d-b46e-0f9ea23b2f33 | -0.9815 | -53.699 | 2024-10-27 00:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 358.0 |
| 252ea472-f472-3160-a043-7189f7077ada | -0.9815 | -53.6789 | 2024-10-27 00:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 7c0943d4-2df2-3bb4-86ed-e26595669cea | -0.9998 | -53.719 | 2024-10-27 00:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 7e68b59b-49a8-3b9b-9dde-abc662740244 | -0.9998 | -53.6989 | 2024-10-27 00:15:11 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 338.9 |
| 3dcd3bd5-151e-31fa-8792-1f09b215ba70 | -0.9999 | -53.6788 | 2024-10-27 00:15:11 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |


[Clique aqui para ver as próximas entradas](README11.md)
