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
| b324c8bb-9b0a-3a11-8e96-331fb5aeddba | -11.7902 | -54.7015 | 2024-11-27 01:00:00 | GOES-16 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 7d302f91-762e-3574-b3de-54d6e1c3ef18 | -3.0577 | -48.5291 | 2024-11-27 01:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| aeea4df6-91cf-3e79-bf04-c2300dd2b306 | -5.9975 | -45.3607 | 2024-11-27 01:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 556edbaa-eb0e-3c5f-89a7-bf51cd53ada4 | -3.1877 | -48.4172 | 2024-11-27 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 58666d56-d37c-3006-852a-c3c46a627594 | -2.8346 | -54.1326 | 2024-11-27 01:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| a6437657-e794-3ce9-9e8d-8ba5fd10466b | -3.1506 | -48.44 | 2024-11-27 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f5c9f313-5180-340e-8ad6-7e237a12c975 | -2.861 | -46.8406 | 2024-11-27 01:00:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 6db964b6-ec7c-324f-9fd2-5ceefd6b7e84 | -3.9859 | -48.0843 | 2024-11-27 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 88934476-a44e-33ac-a9a4-02a002e2ab00 | -3.1692 | -48.4179 | 2024-11-27 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 157.6 |
| a4b9c101-a650-3362-8a7d-f7a3b3335df4 | -3.0578 | -48.5076 | 2024-11-27 01:00:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 158.5 |
| 192c68a7-45b2-3cf2-a0aa-b093adddc914 | -3.11 | -53.27 | 2024-11-27 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33f3ccf8-df54-363f-9d2e-f3ea798d98de | -3.16 | -48.47 | 2024-11-27 01:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f04bdf1-f00b-3836-b8c3-4f7a04b68f97 | -3.16 | -48.42 | 2024-11-27 01:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a63e154-211c-3ebe-a729-88daaeadc793 | -3.08 | -53.26 | 2024-11-27 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa58215-00ab-3f77-978d-2ff53d2cea5d | -3.19 | -48.42 | 2024-11-27 01:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 052b70e5-d366-3515-a67c-833828e11e07 | -3.04 | -48.51 | 2024-11-27 01:00:00 | MSG-03 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 066afaf5-b8ea-3623-957e-5f350a5eb488 | -2.2513 | -53.6101 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e0b79971-dc79-3f40-833f-2bbe256d512d | -1.6108 | -52.746799 | 2024-11-27 01:01:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a68d025-6551-3987-b8b3-ff8bb6129975 | -2.6037 | -54.202702 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 479fa491-99dd-303b-bfed-31eb1b65837c | -1.451 | -52.587898 | 2024-11-27 01:01:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba942d2c-ef47-3306-b95a-2bfdb6398dd3 | -3.0483 | -53.720299 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d30cf11b-e703-38ef-8b67-b87968bcbd4c | -3.3434 | -53.305599 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a99f7f33-86d6-3b9f-852f-81da7cd5cd62 | -2.2463 | -53.633202 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c398c9e0-4bb3-3e24-9344-1ca7034e266c | -1.7701 | -53.619099 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 267636ac-4166-3c15-b241-1ff7543f3e9e | -1.6648 | -52.446201 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9752e5b-2573-3f8d-8b53-73c7e00ed549 | -2.8096 | -54.0243 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd82aeee-e3b4-3133-a24a-f6df0eeed309 | -2.6069 | -54.262001 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3259773-7eef-3866-8db5-54753e3219b4 | -2.6036 | -53.9785 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17990485-6202-325c-ac0d-d65d263f6f85 | -3.0918 | -54.131901 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e99be011-9ed6-3bc8-8565-62ec56af7e60 | -2.7966 | -52.898602 | 2024-11-27 01:01:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0104c46-5575-32e7-94f7-a79b2a2b6580 | -2.8222 | -54.751202 | 2024-11-27 01:01:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67fec40a-157e-381b-9338-f1c1e4782478 | -2.8646 | -53.950298 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28ccd531-4268-36c5-88a8-a39e36d985ce | -3.0624 | -53.291599 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50c2948f-f33f-3d6f-ac02-a6527e82f6d4 | -2.1822 | -53.756802 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee5fa29a-8118-3a02-917d-2674a53992c0 | -2.1115 | -54.930199 | 2024-11-27 01:01:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4fcb31ff-b345-345f-a760-b464ce0967b7 | -2.9059 | -54.174198 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dcd3a302-e392-324d-8d00-93fc0a4fcb61 | -1.6843 | -52.441799 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfc3e81a-cdfb-3b5d-81e0-c62a68cd5742 | -3.0457 | -54.0215 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8007e71-c0b2-3e19-a00e-4a8448377292 | -2.1869 | -53.777302 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fb8aa0d-f3ae-3ade-9343-23541617e2a2 | -1.6926 | -52.611801 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec89b93f-3a02-3f0a-a0ba-04a8d1aced71 | -2.1967 | -53.775101 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4564ebcb-fdbb-36cd-900b-0091701c6749 | -3.1063 | -53.258999 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79ff2ac9-2bfc-3252-b8bf-b271310d3323 | -1.4539 | -52.600498 | 2024-11-27 01:01:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 960a8234-e149-322d-86d1-9c3b42a8c390 | -2.2439 | -53.622799 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d7befb5-4eed-3f46-8640-2a81ce3515a9 | -2.6088 | -53.9566 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0935cc3c-b9f5-3991-9260-cda3f28b663f | -2.7771 | -52.903099 | 2024-11-27 01:01:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 689a0a02-fa8d-332f-a91c-259547e60fa1 | 1.4602 | -56.061298 | 2024-11-27 01:01:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc37e7f2-135c-3217-b964-b34e915cd0b9 | -2.8403 | -54.068298 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c184ceb9-b5e1-38e3-8030-f75614515f43 | -1.6346 | -52.493099 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b91d0587-5e23-3831-ba7c-4076b635ba78 | -2.3708 | -56.112 | 2024-11-27 01:01:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa242199-ce5e-353f-9ddf-fd1ee34ef04b | -1.6775 | -52.456799 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55881e0d-f188-3d77-b0ba-eda7702db90b | -2.8398 | -53.976398 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45aecc9b-f396-32b6-b8c7-78f314c968af | -3.3189 | -54.090199 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54fdfe57-f5ac-3f6e-b33b-01f4216edc68 | -1.6665 | -52.721298 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43af4b05-fdf3-327c-96fa-f89f80aabd0e | -3.2363 | -54.0891 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 936cd774-181c-34c1-8348-326d1f689886 | -3.245 | -54.216 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbb2a1d-65bc-328f-a542-4e5a3e8404d6 | -3.5156 | -54.631001 | 2024-11-27 01:01:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82ab13cf-0417-330b-a7a8-88f7bd039762 | -3.0574 | -53.2701 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0633aad6-51f8-3357-873b-284d88eb2277 | -1.656 | -52.407902 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc1e862a-3583-3749-895a-e67743fa403a | -3.1018 | -53.729301 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f07f541-c6b6-3fdd-8885-fc4c1f423591 | -2.5991 | -53.958801 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2c932a-2c30-3117-9538-126af4aff535 | -1.7949 | -52.743301 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66ff5375-ca6e-3d48-bfe7-9f422b64dbf6 | -2.6058 | -54.2122 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42a1af12-b4e4-3a1d-b27a-b1a413331a8f | -1.6443 | -52.490898 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47c2c588-5fe6-39a8-985d-e44188d9bb62 | -3.5025 | -53.815102 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18362157-00a3-304b-bd98-12e72fbea2a7 | -3.1013 | -53.237499 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74553ce9-e5d4-3f74-9f1b-4a17b6960b65 | -1.6589 | -52.4207 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab98139f-78c0-38a8-93ad-e01ce32746f9 | -2.5317 | -54.562302 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 125bd950-ce26-33e7-bcc5-75682200de94 | -2.8438 | -54.128101 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3abe6e65-a416-31af-acfe-e83a81fa179a | -2.4941 | -54.532299 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78d16d72-7efd-3ead-9188-f9eef564a420 | -3.4374 | -54.1129 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99158e28-062b-31b0-9c24-882170d3e915 | -3.5135 | -54.6222 | 2024-11-27 01:01:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b27d6ade-06db-3b0f-8066-9b41220b5166 | -1.6677 | -52.459 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 564d2796-d6f6-3322-aee9-abc272c52881 | -3.3135 | -53.754501 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c8bdb617-0405-3451-8b1c-43a1cc9dd746 | -3.1135 | -53.245998 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14ef7179-efa8-3b5b-930f-5aeecb04599e | -2.1213 | -54.928001 | 2024-11-27 01:01:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74243d0c-24f4-3a7f-8446-36356974ed37 | -2.6048 | -54.252499 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa9bf136-31d9-336d-ae1c-28c2a907adb5 | -1.7921 | -52.731201 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 153c82e7-6546-36a5-9735-a108e05d5162 | -3.094 | -53.2505 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ff2c93c-2b5c-3d09-affa-fa020cc1f90a | -3.0915 | -53.239799 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5907a727-3de5-312a-8f33-edfb80fb0a39 | -1.6716 | -52.431301 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d00149b6-9642-314e-99d3-2e3e4188b5f4 | -2.1845 | -53.766998 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 420170cf-868e-315c-ad50-e3253cb3820a | 1.4719 | -56.055 | 2024-11-27 01:01:00 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 517afd37-87b1-3563-b05e-0c89cef984fc | -1.6745 | -52.444 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 916731c2-963c-31cc-8f64-75fb0947bb98 | -2.8314 | -54.029598 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 085cf7a8-fb53-30f7-9e13-8a3236839a3d | -2.8416 | -54.118599 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3efd88eb-6e1d-393a-97a2-57893d3011a1 | -2.8145 | -54.1348 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b453ac73-f69b-3d99-8d55-ae635bc5e3fc | -1.6472 | -52.503601 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51478b08-5c7e-396e-b1e5-79d5c5cad40c | -3.3112 | -53.744598 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12d2444b-0f8b-305e-be58-3ca2447fcdd4 | -2.6013 | -53.9687 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2511b0a9-ae41-3301-ad64-d4fb0ea7fff9 | -2.834 | -54.130299 | 2024-11-27 01:01:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87603697-8b90-357c-b08b-2e719c5cac05 | -3.2443 | -53.633099 | 2024-11-27 01:01:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f1057b4-d2fc-3b20-8559-2ab33652f6b8 | -1.8046 | -52.7411 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 90535f3a-75bc-383b-bd94-98c84114665e | -1.6763 | -52.719101 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5db6cba0-208c-31eb-970e-3f8f4f261a67 | -3.1101 | -53.098099 | 2024-11-27 01:01:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 878135df-d715-30d4-9905-06e5a83da565 | -2.2537 | -53.620602 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac644c15-1561-379f-a574-d3745c61f5cb | -2.8291 | -54.019901 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80931046-3855-3a92-a322-339d8364810e | -2.611 | -53.966499 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4d003fc-3da8-355f-95c7-55e89eecf28a | -2.1991 | -53.785301 | 2024-11-27 01:01:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 102ee25a-0f0d-38a4-97e1-91e1a536dbd1 | -1.6686 | -52.418499 | 2024-11-27 01:01:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
