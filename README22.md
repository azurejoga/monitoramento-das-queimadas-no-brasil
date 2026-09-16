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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5eebf0f-8aba-3c74-bdc7-b6c842a2e9d3 | -4.49343 | -45.91201 | 2026-09-16 04:14:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 983dc850-4222-34a4-a29c-fcf0cb84e847 | -7.0986 | -41.76646 | 2026-09-16 04:14:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3e2f2af7-0bce-368b-8848-4185b4619de9 | -7.1441 | -42.10019 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6cd24a67-5dd7-33f9-9dd8-2e9a067bf8a6 | -10.83185 | -46.19989 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 168114a2-5a64-3ba3-928a-18a546e6b165 | -7.17061 | -42.10446 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1573c5fd-40c5-3dd0-a22d-318aad61f35c | -7.17789 | -43.51838 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| eec122d3-3ae9-35b5-bd4f-836745e65e5c | -10.39777 | -46.64038 | 2026-09-16 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49f49fba-e9c0-3e36-817a-f4780c46a586 | -7.08288 | -42.10109 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24be2690-af6c-3fdd-afd6-efc8da88b99f | -6.95623 | -42.57629 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5734055c-b761-314b-8ff6-a241f50033ae | -9.22751 | -46.70178 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7016eaad-0fea-31d9-9475-d442ba2767d4 | -2.91004 | -50.43642 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 001e43c9-eba6-36cf-9da2-16fcd0a35fbd | -6.32832 | -41.76047 | 2026-09-16 04:14:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 18a6d740-1c24-3369-90e5-4249aa48a27a | -6.95292 | -42.55428 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a9afd6b6-bb02-3583-a847-d1cc6acdf365 | -7.17848 | -43.51474 | 2026-09-16 04:14:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 03d4187c-678f-3a63-b7ef-cc52c6424fbf | -4.71582 | -48.31205 | 2026-09-16 04:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b141e0cf-f16f-3bb7-abdf-9ff923538c3d | -8.85954 | -44.91178 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a0ac585-dace-3a42-a45c-5196a3d13b70 | -10.777 | -46.2153 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0029ae2-597b-33b8-a686-f661e7cf073b | -10.31554 | -45.27071 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78ad89d9-fb53-37c0-bb0e-b5c22f62bdf5 | -11.83056 | -37.57993 | 2026-09-16 04:14:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 423060c5-c88d-37a9-a838-7520a5ff2c1c | -8.79548 | -46.90355 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e1246de-646d-3235-b82a-c25d0f9772fe | -10.09913 | -45.60962 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c0bc0d5-b259-396d-bdb8-ce4e0d054d7d | -2.89426 | -50.42997 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbe4f009-1f0a-31b5-958d-8dd24f618f3f | -5.10762 | -47.60542 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ffb49ea7-821d-3ca5-b05d-c1f6eea2a157 | -7.54349 | -42.66357 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f5e8e62a-3965-3676-afef-198a046bfbb3 | -3.39841 | -50.76209 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a568a5cb-c4a6-3989-8e89-9a32f62b4fe7 | -10.41115 | -48.65831 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4833a53b-8090-3d09-b0ea-992d0d4c6b00 | -8.05291 | -43.74467 | 2026-09-16 04:14:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| d6210427-7d4a-355c-b426-56bac0f61e09 | -7.85422 | -55.46108 | 2026-09-16 04:14:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 289b30e7-37b6-3b27-a634-49e36b67e789 | -2.90032 | -50.42736 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6879087-70e9-333e-8def-93b0f760d622 | -4.51407 | -54.97537 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de1968c0-e31f-35e7-b038-3a5f9e65da99 | -10.09406 | -45.59603 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ffe2a23-46dd-3a71-a8bb-5d201f1fc6c7 | -6.78431 | -48.65586 | 2026-09-16 04:14:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37f74aa7-f532-3e61-adad-3d130374bc86 | -8.38644 | -42.21354 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 84cca06f-e174-3af8-a098-c62b66551708 | -11.17388 | -42.82042 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fd514c65-aa97-3780-a9db-32431703ac15 | -7.11986 | -42.14606 | 2026-09-16 04:14:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| bd493bf3-4346-3de4-9d9a-76ddddf5c0b2 | -7.18412 | -41.80485 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d21c1f5a-914f-3199-8923-8d6abead2618 | -5.62978 | -40.84838 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c837bba6-b97b-31e4-91d3-1bcc5ef3daee | -7.43731 | -44.56863 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1cce418a-f768-3472-b887-e4e1cfc490d5 | -11.17664 | -42.82447 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e3a34a1e-6da2-3566-b883-1e7446cc47c1 | -9.3412 | -44.38683 | 2026-09-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17d2761e-1620-3f68-ae56-efe5bcf29978 | -4.46487 | -55.25236 | 2026-09-16 04:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a06fd3-2f58-3361-9439-dcbbf6f445f6 | -10.41285 | -48.63913 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0cb019f6-87ca-39c0-940e-ebd384a0e155 | -2.90697 | -50.4212 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f204104-472d-3399-9c5f-4443037bb84a | -10.1125 | -45.57388 | 2026-09-16 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ceb0f7e7-6c12-3f87-abc7-f104bfd9fa31 | -10.85239 | -46.18988 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6642d90e-3a11-36f8-8efc-921779dbabff | -9.10046 | -45.7268 | 2026-09-16 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 50203000-a10b-35d1-9e78-cd2aa0f64259 | -3.02064 | -51.3414 | 2026-09-16 04:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b3878749-4d7b-3a08-8af4-6d85d9508bf2 | -10.36865 | -45.12831 | 2026-09-16 04:14:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 27bd8b97-06fd-3756-bce2-77ef4621855e | -10.84656 | -46.18005 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37e8c049-17ed-3a2f-8fd1-bb8a58ac5482 | -11.16622 | -42.80481 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 53b3144c-53a2-32c7-9ede-8a4d46b17880 | -4.675 | -42.09431 | 2026-09-16 04:14:00 | NOAA-20 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c978e216-768b-3c08-b9d7-c703beca3fd5 | -9.7924 | -48.81379 | 2026-09-16 04:14:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdd75860-2bbf-3235-8e5a-09f4697e99b5 | -11.23049 | -43.44608 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 160a0b0e-9483-341b-b3b5-02b170d11169 | -11.82804 | -37.56812 | 2026-09-16 04:14:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a02f4f76-a3db-3218-8ffb-8e88f0a9bd84 | -11.35766 | -43.96338 | 2026-09-16 04:14:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b1f75557-dcb3-3bda-a938-09555ba13f64 | -9.04069 | -45.06689 | 2026-09-16 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73a818da-b837-302b-8d09-88856392d568 | -11.16678 | -42.80131 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f86121a1-43f5-3ebc-9a6e-7dcf12660992 | -11.19762 | -42.82068 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1f08fcba-6dd3-34d2-be11-7bb57b10608c | -6.76225 | -42.74688 | 2026-09-16 04:14:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4f7455a3-cb4d-3810-9044-bcb0b68129fe | -2.91169 | -50.393 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50fd3a37-bd1d-3bf0-aabc-b18d7b79ab96 | -2.89308 | -50.43697 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6f4d1d6-6665-3aed-a553-c10534af03fb | -6.32279 | -44.09419 | 2026-09-16 04:14:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38dbefcc-8b7c-38bf-8afc-a325f26c15c2 | -3.1429 | -51.1083 | 2026-09-16 04:14:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9bd65f4d-ea4c-3293-a664-a06f38d7bc13 | -5.71319 | -46.19418 | 2026-09-16 04:14:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc456c55-040a-31b1-8412-9a82b90202c9 | -8.36528 | -54.73345 | 2026-09-16 04:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a6ecf99-876e-3fb9-a7b7-caf3a50c79cf | -11.24491 | -43.4412 | 2026-09-16 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e194e5d-3dbf-35d7-be61-380b3054d9c0 | -3.47426 | -54.6826 | 2026-09-16 04:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 919bcb00-0554-3a47-9540-512aeaafca8d | -8.95381 | -44.39807 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a30e4f2b-78c0-3e33-b7a9-74f9c8beeb3a | -6.75891 | -42.74635 | 2026-09-16 04:14:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f04b648-b7b6-3899-9c96-fbc668ba3690 | -4.71581 | -48.31004 | 2026-09-16 04:14:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd44ef97-2e88-3407-a6b7-a5ee412a1758 | -11.17333 | -42.82393 | 2026-09-16 04:14:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 20f42051-2ad6-38f4-89d5-5750ad414449 | -8.85734 | -44.90308 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1374c001-ec95-3ecc-b675-c8e27f8a3f19 | -9.22429 | -46.72108 | 2026-09-16 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62590d39-b7e0-3dc2-9dcf-293a1f5f4440 | -7.35062 | -44.47914 | 2026-09-16 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fc8b66f-95ac-3cab-aacb-e32d1557d4e7 | -5.36968 | -50.16378 | 2026-09-16 04:14:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 902d7459-f688-35d0-a682-ff48382f88c3 | -10.77773 | -46.21096 | 2026-09-16 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba419a26-ed7a-3cd8-ba9c-cb013a2495a0 | -2.95472 | -50.40393 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e365e94-af0e-3715-bf5a-f32bb7437c06 | -7.18358 | -41.80832 | 2026-09-16 04:14:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b8f7be0b-6ce1-394c-93ae-8ec29aa14544 | -5.10549 | -47.6181 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4b2bfca9-3cfb-31e9-917d-1113ba70ee86 | -9.46794 | -45.45955 | 2026-09-16 04:14:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acaf92a8-2343-3973-92fa-d61d00b7599e | -9.57197 | -46.58528 | 2026-09-16 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 236f1314-2789-37c7-aa45-ddfa50adfb40 | -5.98976 | -52.10711 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f63eec9b-1a59-3704-aad8-01bb26e1f81b | -2.9142 | -50.41152 | 2026-09-16 04:14:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 364b3870-e7d5-38b9-ae7f-7037a942564d | -7.2646 | -46.67471 | 2026-09-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eda1bf03-365d-3ad4-bbf3-9f075a3da2e3 | -5.8373 | -51.9584 | 2026-09-16 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| adc637c7-42b7-36b1-a771-6008e136756b | -5.1394 | -47.60247 | 2026-09-16 04:14:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a3e8a115-12f0-3ff5-af9c-d1261bd6ac1d | -6.35428 | -41.74693 | 2026-09-16 04:14:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 732c9dba-6883-3aab-a3b0-3410d01c5a88 | -6.84494 | -47.43737 | 2026-09-16 04:14:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50d07892-3b14-3c45-b593-2c2ba1f08196 | -10.58871 | -47.75026 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb5f7c7a-6e2e-3e4b-89a1-b9be2c32c010 | -9.7827 | -46.4893 | 2026-09-16 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9316e68f-e25d-3ea2-91ea-ea57a9cc85cc | -6.66225 | -43.64773 | 2026-09-16 04:14:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b57cf66e-04c3-331d-b0e4-f1a4122c0e06 | -10.40976 | -48.64089 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92124cdd-4539-395b-8949-d9cc2bb46a7c | -5.62591 | -40.85135 | 2026-09-16 04:14:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7500d31b-88c9-3792-a312-9fc4f9ca27e4 | -8.95657 | -44.39728 | 2026-09-16 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 952fb3a7-9006-3d4d-83af-0f93ffde7e68 | -5.60677 | -44.84556 | 2026-09-16 04:14:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2fad05aa-67d5-3aff-a2b6-36b1117c623f | -7.28976 | -46.74172 | 2026-09-16 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e791663f-64d4-36e3-a0b1-68e05b3254e2 | -6.73043 | -43.0731 | 2026-09-16 04:14:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a29f070-0000-391d-b349-1d502ecb0e21 | -10.59671 | -47.75188 | 2026-09-16 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 08fef785-711c-354a-a7d6-7031a673421c | -11.82645 | -37.57934 | 2026-09-16 04:14:00 | NOAA-20 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 26a51af7-0998-3fe0-bd79-54c7eb8670ab | -10.4192 | -48.65284 | 2026-09-16 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README23.md)
