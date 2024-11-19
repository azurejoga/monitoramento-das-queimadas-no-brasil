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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d0bc80e-222b-32b9-9daa-9ccbc491727d | -4.28536 | -48.2123 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 55f04bb3-d51c-3a74-a0b8-cb9283cfbb05 | -1.36252 | -51.98563 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 862d72b0-2701-3a43-8d15-6998eaef3011 | -5.51032 | -46.44353 | 2024-11-19 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0f27567-4adf-3833-bb75-db730e45d929 | -4.20535 | -46.58852 | 2024-11-19 04:46:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d6141a6e-2ef4-353e-a9cf-8e3a5a8fa1cb | -3.41603 | -42.38506 | 2024-11-19 04:46:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a2639afa-99cf-346f-9999-d7e74e4f9ca0 | -2.30193 | -49.05593 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 80f757fc-7a80-36a2-ad82-c9b3adf6d10d | -1.99828 | -49.54683 | 2024-11-19 04:46:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45efe562-f9cd-3d74-8505-44c3c145659b | -4.11894 | -43.59002 | 2024-11-19 04:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0ecd6d9c-a754-33a8-aed4-cf512c8c030c | -3.4156 | -42.38795 | 2024-11-19 04:46:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bfc78ba4-98ac-3848-9e3c-d5663c570f62 | -1.20331 | -51.7672 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b6b57c1-42ab-308d-a080-ae1a1de47f54 | -1.59105 | -53.80535 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| e27212a5-0f75-3be2-9ea8-c16c3a472082 | -1.13957 | -51.68694 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 220ad26c-f152-3e40-9959-f0333a7b8c30 | -3.38831 | -53.26558 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16a16104-910d-3723-ae09-f1fa00f48d44 | -2.21908 | -53.79269 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 32b04d8c-59ea-35c2-8fd3-9c3044801efd | -0.04721 | -53.25576 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cfd1b26f-c170-35b9-ba41-6f1d7fccba1c | -3.73179 | -51.32079 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 10d13993-4cf9-368b-89b4-f13da2c80508 | -2.96262 | -51.41045 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 778f90f9-fd57-3e5c-9b27-4f8a65a2bc64 | -2.84873 | -54.00616 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 1d63a5d7-e9d2-3f36-9bf1-45c071d8b521 | -1.41157 | -52.05396 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0bdd49b2-c874-317f-9b57-76cb0d30eee1 | -0.85453 | -52.59019 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a4a9d58-f437-3cfd-a295-9fe8080b7ecf | -0.0278 | -50.77395 | 2024-11-19 04:46:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a01d512e-d9bf-3c84-aa9d-faffae456a84 | -2.28568 | -53.63306 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 2b4e204f-8bb9-3ac3-8dc2-70d7881ab0bf | -3.77045 | -52.41306 | 2024-11-19 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc65ea7f-1c86-3659-bbfd-746b6f26cddf | -2.3788 | -48.91459 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae5e9a3d-2d49-3705-8602-3e2a436cb15f | -4.55143 | -48.00753 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e75f15e-da56-3913-828d-7c06d6c69915 | -2.35884 | -49.02105 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c8a9a733-4667-379a-b93c-0a26bbd3d802 | -4.48943 | -46.71212 | 2024-11-19 04:46:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8218389a-7c4e-3619-a24d-c7aeeb299026 | -5.60026 | -44.8831 | 2024-11-19 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e444f008-449b-3590-8ce1-ab8ccc2ca0ec | -2.20876 | -50.72778 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a7743c56-46cd-3fb7-83d3-65f00f6f811a | -1.37769 | -51.55769 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a598ba20-eee4-3e42-9fb2-0318dc9e7c4e | -2.36855 | -53.67914 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd899e8d-5565-39b4-8186-4dd569fda164 | -2.25667 | -50.46427 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e0fa8249-a956-36c6-8e7d-a87dbfbfff5d | -3.11516 | -53.70193 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34f6f62d-87c3-31c3-b2e8-b82fd5aa1b50 | -1.78603 | -53.59165 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10f27acf-c128-3087-8589-c35adda15a49 | -3.34093 | -53.31182 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22d3ffb9-5e42-34a2-9d26-a028dee38a41 | -3.99102 | -49.92015 | 2024-11-19 04:46:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e799a988-0d45-317a-b25a-7c5a5adfd57b | -1.67277 | -53.10514 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0e2caa0-9e41-3577-96bc-d6e7167a8d01 | -2.26158 | -50.45448 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8cfb5209-aaab-3880-8357-258993ea462a | -1.40172 | -47.45318 | 2024-11-19 04:46:00 | NOAA-21 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a4e2b26c-9da1-3a3e-9031-5a8445974fbc | -1.77963 | -50.75246 | 2024-11-19 04:46:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17d01e3d-0674-3c70-a696-f9d0b084667c | -1.66276 | -52.52995 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7f8f098f-73bf-34ba-834d-cba5ad4fc1eb | -1.34403 | -51.85913 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8de2b818-9b17-300e-bfad-bafff4f5d3d3 | -4.93441 | -49.1571 | 2024-11-19 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d9474147-f35d-3a37-8d33-db76a59d56b8 | -0.94342 | -51.63803 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 828364df-2705-300a-848d-3c3c384445ee | -2.10167 | -53.25914 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e63e835-e8a4-36a0-bfcf-b066cfb8084f | -1.99094 | -51.09794 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a46c17d3-a8c0-377b-8673-401070983c2b | -4.57259 | -45.64425 | 2024-11-19 04:46:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 697cb500-e886-3802-b701-8c3eb82f2da6 | -1.94815 | -53.3327 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 874034c1-7009-3686-a963-9d95d4ae155d | -2.64571 | -48.48288 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 392f1ea9-2bee-370c-8359-63241665b341 | -4.55853 | -48.00862 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5138b4c-e660-3ba9-85c2-f57c65c95a96 | -6.6423 | -47.91374 | 2024-11-19 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de14ba89-c4d3-35b0-b7b0-fd669a92da95 | -2.25381 | -50.56927 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a86a850b-34b2-31b3-b91c-d8c5f2ff13fc | -1.68058 | -52.55227 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc55b05d-8187-3c23-9700-49420bd355a2 | -0.88331 | -51.72552 | 2024-11-19 04:46:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a3495dd3-b371-30ce-a4ca-4af45cb83b63 | -1.27024 | -52.1267 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d70e371f-54a8-3196-b4fa-d65dbccf16d6 | -4.55792 | -48.01262 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 3098cc6f-4a5e-374a-a7e7-065939249f23 | -3.1078 | -53.74777 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ec987be0-b2d5-30bb-9b76-6fd1af179523 | -2.28197 | -50.63064 | 2024-11-19 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac0b015a-97b5-3dde-a693-49ddb95fd050 | -5.96363 | -43.99727 | 2024-11-19 04:46:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4938e94b-b1bc-367f-a5b3-b505e134a815 | -3.36574 | -54.10279 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45872888-6bcd-3616-9ab8-0e62d53438ad | -2.58289 | -51.92445 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f61a1cfa-75a1-3f3d-a46c-3e7effe11756 | -4.94784 | -47.80571 | 2024-11-19 04:46:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20dfac2e-71c7-3d40-b6c7-8cb967fe5940 | -3.10418 | -53.74721 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f5e86174-7cfc-351d-b596-8bb3bce5dd96 | -1.48785 | -52.1035 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21e03e09-d86a-3975-9b10-91a484e1bb4d | -6.50816 | -46.6411 | 2024-11-19 04:46:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fdf6ae1c-0067-32e7-96bb-8ebd2f9c6b7f | -1.62393 | -55.14548 | 2024-11-19 04:46:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84b64493-8291-36f2-99a2-9954d596855a | -3.05589 | -51.33563 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30000cd6-e334-3eaa-83a3-766a15a02193 | -4.1896 | -48.57101 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a50a776c-bbbc-33ba-84fc-781fe34d67fb | -2.8965 | -53.05162 | 2024-11-19 04:46:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5f423b3-5a75-3425-a2e7-e65a91cb6056 | -1.33398 | -52.23592 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5399c73c-015c-3bfd-9f7b-f4a5cddedbf2 | -4.05992 | -50.00243 | 2024-11-19 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b985384-9108-3d1e-b083-eb097d45a242 | -1.97491 | -52.15476 | 2024-11-19 04:46:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0069f59b-15e9-3948-92a4-18b7ac30828f | -4.95323 | -49.49716 | 2024-11-19 04:46:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7e5afba0-0038-3f1c-8b39-8ce609cbd213 | -5.58777 | -44.87722 | 2024-11-19 04:46:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dd0652c5-5c27-371c-9b2f-09f4952a7216 | -1.21349 | -51.79107 | 2024-11-19 04:46:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d91aea67-0710-3a7d-a9d6-b5ca049b8a85 | -3.78065 | -51.87733 | 2024-11-19 04:46:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9940ab5-2685-3f5c-a1cf-214f40c41c40 | -1.90213 | -53.33097 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 59812ef8-3bc7-3fc6-b39b-72498abe6312 | -2.64627 | -48.47918 | 2024-11-19 04:46:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bdc8c5fb-8270-31f7-ad71-1c9c246d7909 | -5.94798 | -39.67263 | 2024-11-19 04:46:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 433ce1a4-defa-3f00-ab46-99cb4a45c8c3 | -3.61047 | -54.74817 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de42635a-e330-3a93-a6e7-de03d22f2419 | -3.05312 | -51.33163 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1194e214-4d0c-354d-92c0-f741be827064 | -1.58666 | -53.80912 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d6312772-3943-3ac4-821e-c735b627b3e3 | -1.07213 | -53.65044 | 2024-11-19 04:46:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e096889-9009-3a55-a306-196c9c017e90 | -0.09422 | -51.45627 | 2024-11-19 04:46:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8238b52-db11-34ba-b613-3409e6c4f908 | -2.85241 | -54.00674 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 3e87f93d-f1ac-35be-b877-83297f4db773 | -3.54908 | -51.53113 | 2024-11-19 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbb7651f-b7cb-3249-b4c0-b86eac5f9895 | -3.3229 | -52.71225 | 2024-11-19 04:46:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 23331e98-16fb-3aad-8a7a-26824543a021 | -3.55152 | -54.58419 | 2024-11-19 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ccd2c1d-16bd-3384-9146-6e2b344bb818 | -3.04086 | -49.46899 | 2024-11-19 04:46:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e2a32f14-07a6-38fc-add4-93235ed07ef9 | -4.11497 | -43.58455 | 2024-11-19 04:46:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e01afd79-81eb-3818-99c8-d962ee9d0873 | -4.77481 | -47.84414 | 2024-11-19 04:46:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5a17de8b-fac3-38a2-bf07-777d091fbec9 | -3.31301 | -54.08192 | 2024-11-19 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e19c86e8-734b-3995-b7c7-e5339449ee93 | -3.84643 | -50.69624 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26290010-2a65-36f0-a775-ec14ec89cd1f | -1.7058 | -50.20285 | 2024-11-19 04:46:00 | NOAA-21 | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82c513d0-0751-3440-a1a7-1d486b055c0e | -5.9667 | -46.30723 | 2024-11-19 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47781a03-1c62-396e-9afc-a70c94dcf0b2 | -6.25676 | -43.56215 | 2024-11-19 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 528846d4-e747-3c32-a997-fd63a9bdf6ba | -3.71159 | -51.19007 | 2024-11-19 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f591e1d9-e551-30ff-afa7-8627a81a5dbd | -6.64595 | -47.91429 | 2024-11-19 04:46:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ec36f56-788a-39a8-9cd2-15a6eb3c17ac | -4.57921 | -48.01588 | 2024-11-19 04:46:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| dab8529b-5a06-3d59-a966-6f6e4725e4f9 | -2.88208 | -53.96257 | 2024-11-19 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README31.md)
