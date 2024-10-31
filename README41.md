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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15748b52-3991-3a73-b041-4c9106d9226b | -19.53043 | -56.72025 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.2 |
| 4d2a299b-9b2d-3c83-97cd-8b4609564b28 | -19.51223 | -56.70547 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| c0384935-cff7-3b79-a25d-d0a4180c966b | -19.62711 | -56.70987 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| c3a32e0a-308c-34b8-bc02-b24cc7c4970c | -19.62559 | -56.69812 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 5f9dd56a-05f2-3414-a3a5-401d8b6fc91c | -19.62165 | -56.70123 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| bf02df18-fd80-30d5-8c1e-2058f3a425f8 | -19.62044 | -56.70866 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| ba36419d-7143-36e3-b203-2cb73f19ad16 | -19.61589 | -56.71548 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d9130573-b339-3d94-90d6-f6a8bda1ed04 | -19.61104 | -56.70313 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 6ae4c6d5-7600-3f5d-9e67-08ef340c1f84 | -19.60983 | -56.71056 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9ea28086-cdb5-31ca-a90f-096b57b8acad | -19.60953 | -56.69139 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bd02cd2b-4faa-393d-8fb6-d24ee628884a | -19.60589 | -56.71367 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 335875b1-6917-3d0d-a26a-ccb3818857bc | -19.60559 | -56.6945 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f9a7afad-2e15-3df4-929c-a6df0061fb84 | -19.60437 | -56.70192 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3fb3fe32-723b-3696-9fcb-bd9c56d5b98a | -19.60377 | -56.70564 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| afe4fa09-d620-318e-b382-83f4ad80c149 | -19.60316 | -56.70935 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e4ff2f88-822e-36c1-af63-dc2c4ba1c6a2 | -19.59922 | -56.71246 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6564d3ac-a0b1-32c4-81bd-8423a2620507 | -19.57954 | -56.71386 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| c0224b29-1d6d-3315-a9be-81fbb683529a | -19.56637 | -56.60458 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9b697e55-07be-380f-ba61-502b8ae737ed | -19.50975 | -56.59434 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| fd7a34c4-7dd2-3a4b-8dac-e925fd7f4f76 | -19.50495 | -56.70797 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| f5b28e4a-8667-3b45-8650-f8b0d06d7252 | -19.5043 | -56.58574 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 8ac1b6a3-c61e-391c-90a4-073879a10bb4 | -19.50278 | -56.57405 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a32fbb70-eb33-3912-bb01-363725103075 | -19.50249 | -56.59684 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| ed03084f-2266-36f1-9196-118e92cf9912 | -19.50161 | -56.70737 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 2cec9dcc-e333-3a27-a6ee-2391e6a1d3b2 | -19.50157 | -56.58144 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e46a3112-f86a-3bba-a8fb-c2a5caa4727b | -19.50129 | -56.60424 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 15cd0291-ac0f-3962-8c80-40df25e619dc | -19.50079 | -56.57 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e4ff6626-cbf0-372f-bbf3-ec2058a03a8c | -19.49856 | -56.59994 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 16697318-0789-3ed1-b1eb-b5eb7088fb1e | -19.49796 | -56.60364 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4b27a4d3-407d-3f6a-82b0-7efa9510e715 | -19.49766 | -56.62645 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 11dc61ed-9711-37e6-b66f-f500d271b07c | -19.49566 | -56.5805 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 41b4d83d-2ffc-3e45-81d4-204a28b66db3 | -19.49433 | -56.62585 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 389c19b3-f86c-32d2-8119-7e3d4bf93d73 | -19.59255 | -56.71125 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 7b793985-b405-3dc0-b640-b4e6cd172cce | -19.57681 | -56.70954 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 686a84fb-438b-3425-b08a-e988395e3c63 | -19.57134 | -56.70089 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ba942327-b582-34b2-aa8c-56aaa4a7d876 | -19.56528 | -56.69597 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b50d3414-b4f0-3406-b070-2cc4cc344cb0 | -19.56287 | -56.71083 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 3d93316c-7c9c-3b3f-9dc5-ca64bd077ede | -19.6262 | -56.69441 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 11d97997-a6cc-3894-939f-4d2844bf6dbe | -19.62438 | -56.70555 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 234161fe-ba02-3bf1-ae5b-a471770cbe60 | -19.62317 | -56.71298 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 7fdce741-f978-36f0-bd6e-abd7da0bc041 | -19.62286 | -56.69381 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8997993b-084e-387f-8d63-ea965c1a9103 | -19.61832 | -56.70062 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 266e6763-4f62-34a3-a54f-aa450150d8bd | -19.6165 | -56.71177 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1c7fc4f7-e49e-37d1-9120-d5b3f9b9f6d0 | -19.61438 | -56.70373 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 4c9c29ed-18e0-3c03-bcf8-0872e1b6d33f | -19.61044 | -56.70684 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d33d7b59-7fbb-3377-8673-4d2dca6bf87d | -19.60831 | -56.69881 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 55ab27c7-d801-335c-add4-97359187d32a | -19.60771 | -56.70252 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 0db7b10c-3368-36db-b318-953af5f7e385 | -19.6065 | -56.70995 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| e9971fc9-e3ce-38d0-969c-4016e12fbc84 | -19.60498 | -56.69821 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 764c6f04-5187-30a5-a13f-07adc787acfb | -19.60315 | -56.62535 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 759f570e-6459-365d-a37f-9f381913e2bb | -19.60255 | -56.71306 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| e53db18f-3ebf-32ab-b224-88a06989e158 | -19.60104 | -56.70131 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| eabb1c1e-8749-30a5-be0b-911bffa4c9e9 | -19.60043 | -56.70503 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 47eaf126-ce8a-3e8e-88c0-1770da63fdf6 | -19.59377 | -56.70382 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 18b55788-83e1-3ea0-b38e-15414feeb329 | -19.58802 | -56.70392 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2fe8f012-f773-3449-8efe-ded7ceb7b724 | -19.58455 | -56.61929 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0b54d6e4-1771-3995-bcfa-b11b79d12ade | -19.58336 | -56.62671 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 8fffd38f-17b5-3875-a958-211447d4aa1b | -19.57347 | -56.70893 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| e5dc6821-7ef3-31c3-9bea-4da6b4e2f9fe | -19.56407 | -56.7034 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 32f8ea98-8114-36a7-a5cf-01ad69c36ad9 | -19.54165 | -56.71463 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 36268859-b3f5-3d14-85f5-989a3280c035 | -19.52617 | -56.70417 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 490c1908-58aa-31b7-b651-e5383208d3f9 | -19.52436 | -56.71532 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.2 |
| eec08407-0ea7-3450-aae7-d00e8ca6fe59 | -19.5101 | -56.69743 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.8 |
| bb458da8-3c36-39c3-afa6-2636385cbbc1 | -19.50889 | -56.70486 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7ee7e390-7ee9-3c47-9d12-a65768abf62a | -19.50858 | -56.68569 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c96cbcd7-45c9-358e-918d-934e2ba342d6 | -19.50763 | -56.58635 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 09072581-6226-39fb-ba97-8438a1e0015e | -19.50703 | -56.59004 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 1c813e7d-e785-3d89-9cbe-5d4ef6821b1e | -19.50643 | -56.59375 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 0702d46f-77bd-3920-b4c7-1399905f5758 | -19.5049 | -56.58205 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| b2b44311-0a07-3418-aa84-93666860ac0b | -19.50309 | -56.59314 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 1e5e2397-ea01-31e0-ba27-02805d08f4c1 | -19.49977 | -56.59254 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 41e2e7f5-0ce9-3dc0-ae41-5e55408c03c5 | -19.49601 | -56.59961 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 2e1d84d8-2652-3ffd-9487-aeaa0073cb8d | -19.49494 | -56.70615 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f7b860cd-336e-3f01-a0a6-878d2be4516f | -19.49328 | -56.5953 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 62658bc0-2236-3eeb-a31c-122873327034 | -19.49221 | -56.70184 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| afb57ae3-3b3b-3986-a8b5-a277a714e372 | -19.491 | -56.70926 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 94da6c05-911d-3a6f-a31e-e8d814441467 | -19.53376 | -56.72085 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| e5f42c0c-5731-3c5a-aa3a-6c282d8e67d7 | -19.62075 | -56.72784 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4b18d32f-bc1f-37b2-99d9-6e5b676f5759 | -19.61681 | -56.73095 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 9c97d4fd-4313-3f92-b0e9-1579ba6e39a0 | -19.61529 | -56.7192 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 85f7c41e-df8d-3c7b-b684-7a50840cfc09 | -19.61438 | -56.74582 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| b04ca578-dc94-3b10-b508-cce6e5242651 | -19.60862 | -56.71798 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2c3bee61-6307-31ed-9cbb-216328d8258f | -19.60831 | -56.74089 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 89.6 |
| baa1b4b5-78c6-315c-9091-9668ea6b7bf2 | -19.60528 | -56.71738 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 17a153da-cc3d-3e07-8b52-55a873b5de7a | -19.60285 | -56.73225 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 8971786a-21a4-370a-918e-24145dea38fa | -19.60132 | -56.7626 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6f26b3ad-ab45-3761-844d-7670474041a9 | -19.59314 | -56.74962 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 23.0 |
| f28822a8-034d-3b54-bb89-650f59c00bfc | -19.59163 | -56.73787 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.7 |
| 36f20865-da0f-34bf-a467-c8804f969964 | -19.5377 | -56.71774 | 2024-10-31 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 3965f661-dcc7-39fe-a7ad-339b11d17d07 | -19.59861 | -56.71617 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c8b84278-910e-3dfe-8171-18624bff6df7 | -19.565 | -56.71887 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 9.7 |
| 81a2c77c-d821-3d4d-b2ee-d37d7ac57c70 | -19.62469 | -56.72473 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c9211bcf-a9f6-3df9-9716-cfe0f3dcf18e | -19.61923 | -56.71609 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 28e9421f-e343-3123-a9ff-d5c3dc359239 | -19.61802 | -56.72351 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| c5556b22-7876-31d8-a200-9c7771cef161 | -19.6162 | -56.73467 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 26.4 |
| a8402ebb-fdf3-3b8e-9c96-b4203653809a | -19.61377 | -56.74954 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9ff95d62-5d9c-38b9-a25a-c859296df20a | -19.61226 | -56.73778 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 833ad9e1-6219-3ca5-a315-b7f5c81834f2 | -19.61195 | -56.71859 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 366e5f99-5d62-3e16-b056-90d2166448b1 | -19.61165 | -56.7415 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 007decb3-7785-3288-b504-e8439b8c6c7c | -19.60982 | -56.75266 | 2024-10-31 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README42.md)
