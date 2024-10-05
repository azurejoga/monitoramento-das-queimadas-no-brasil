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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1e2470eb-2d35-37cc-b00d-2e006fce0701 | -13.13885 | -51.16804 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e0263a6-c787-3c2e-8bbc-ac8b9ddfea17 | -13.1372 | -51.15697 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afcffee4-5a80-3bde-a460-d8d6fa48ddc7 | -13.13664 | -51.1605 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccc34604-528d-360b-95d8-dd0c24fffe3a | -13.13609 | -51.16404 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 406907a6-d35b-3274-a821-0887e1524ba8 | -13.13605 | -51.1857 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a72e75e-4126-3de5-82e0-a33c0e5c1ab5 | -13.13554 | -51.16749 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 07bd4e85-2368-3b9a-8837-6b7145b15bba | -13.13389 | -51.15643 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60af5e7d-0178-3ce7-b8e4-e955b8c9c0ee | -13.13333 | -51.15996 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 989c9ffe-d2dc-33e6-9b4a-f83e4a30c92d | -13.13226 | -51.14529 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2e39f13b-0c99-35a9-b2e2-bbb09c573feb | -13.1317 | -51.14882 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c32fe888-49f2-3292-bb4a-52762bfdf22c | -13.13006 | -51.13768 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9c3f09cc-a4d2-33a9-adf9-320e77dcf31a | -13.1295 | -51.14122 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc711ab7-833d-3ae6-bcf4-f27d9679fd6e | -13.12895 | -51.14475 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 40bf05d7-4a23-3b4c-aeb3-137482b1e772 | -13.12668 | -51.18053 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2652ae9-d8ff-3bcd-ba1a-87e3823e03f4 | -13.12619 | -51.14067 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e4192fd8-fcf7-3120-ae52-53712b75accd | -13.12344 | -51.1366 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 9a1c9af9-3966-32af-9bdc-58bbc6073b67 | -13.12337 | -51.17998 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e7da799-0732-374a-ace6-57cadd278b7f | -13.12288 | -51.14013 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6b7b35c5-640c-3363-bad0-0f73e2ce9d20 | -13.12013 | -51.13605 | 2024-10-05 04:38:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ec44ff6c-8df6-30c0-be36-c65032f7e3b1 | -13.12006 | -51.17944 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cf3e1bb-0d16-324e-ba6d-d1efb3044078 | -13.11957 | -51.13958 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a220720-545c-3135-bc64-ffc1c6d123ec | -13.11902 | -51.14312 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 368ca616-cbda-3821-a52e-a818f2eb108c | -13.10466 | -51.14799 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20f83dc0-f6ed-33f9-8c31-621c40853b62 | -12.78875 | -50.56448 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e115d7b-9335-3110-8320-2df1bf5c965a | -12.78599 | -50.56042 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4710c47d-38b0-31f0-aecc-9dd5b1e282a5 | -12.78544 | -50.56394 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47882564-d199-37e6-8417-5865144361ac | -12.78543 | -50.54224 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 00d2da96-6266-31b6-8b62-4b83a5bb3045 | -12.78488 | -50.54577 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 64fb088b-16aa-37a4-afdb-d33f1704d988 | -12.78433 | -50.5493 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 05546566-2615-39c2-af63-c1dd171926f7 | -12.78378 | -50.55283 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| afefef75-a962-3426-be16-bcee1e3d9810 | -12.78213 | -50.5634 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34cb3070-9d5b-3d74-b80b-f3c93c100c52 | -12.78212 | -50.54171 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 54099ee1-2cc3-3d15-a463-2c0570500754 | -12.78158 | -50.56693 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db13c4cd-a7e8-38a9-8015-c0d97b5ede6d | -12.78157 | -50.54523 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 1492fea8-b258-30da-a3ae-393e56aa23db | -12.78102 | -50.54876 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 81cb9c32-cf00-3b6a-8b9c-1e45d59d038a | -12.78047 | -50.55229 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e05dc1c7-c2e4-3ff2-b2d6-86cdbd83c8bf | -12.77992 | -50.55582 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 015e2017-9470-38b4-939c-3fb0cc8155bf | -12.77826 | -50.5447 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ccd70874-c99c-3a7d-8248-b156c22dbdb3 | -12.77771 | -50.54823 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cb10fc02-d825-3d82-a4d2-6118d6cd1659 | -12.77716 | -50.55175 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5a091ef8-96a7-346e-9af0-10bc8742bfe1 | -12.77661 | -50.55528 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 6f0025d1-5fbf-38d5-abb4-adff850feb2c | -12.77606 | -50.5588 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| e6a5882c-02a3-37d0-b109-f95a865dfe89 | -12.77551 | -50.56233 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c9a2cbb-507e-3ad8-a06b-7f749b2c5201 | -12.77495 | -50.54416 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 85bc40b1-0973-398f-a2d6-deecdd2dccb0 | -12.7744 | -50.54769 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2dd2b975-f781-36aa-b83b-8772e037dd60 | -12.77385 | -50.55122 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cb5ca9f2-0515-3e42-a899-2b118f2d2cd9 | -12.7733 | -50.55474 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c334f6f2-efb3-3e48-b7e2-e9a9b6791156 | -12.77275 | -50.55827 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 441767f7-d44d-32c5-a4ca-cd58c947d7f8 | -12.7722 | -50.5618 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66065163-17cf-3fe9-9be7-733824fb9652 | -12.77165 | -50.56532 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 935b5cf1-d7e9-31a5-ba36-01b00d16967d | -12.77164 | -50.54362 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fefddb27-331b-3a8e-bc99-5f89ef1c19b8 | -12.77109 | -50.54715 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 98b0ef31-cfc5-331c-bcbd-8dcd3fc27e0f | -12.76999 | -50.55421 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6a3fb544-739b-3710-b2c0-f03afb385ed8 | -12.76944 | -50.55773 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 6b9018f2-4d60-3cff-b809-675d804f425a | -12.76889 | -50.56126 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c0cb4da5-bde3-3955-831e-0389aa427aac | -12.76834 | -50.56479 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| a31b36d8-e9bc-3cfd-b99a-1b9da23d2d62 | -12.76777 | -50.54662 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 0a81ade1-0c92-3af7-884f-25d30331c9fc | -12.76723 | -50.55014 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 0f98192a-0d10-335f-a29c-50b178156990 | -12.76667 | -50.55367 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 77239293-6004-3d93-8818-6dd03baf2670 | -12.76613 | -50.5572 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 87767a3e-ad99-3688-970c-9372c1a22cb8 | -12.76558 | -50.56073 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 53b7df32-9537-3490-a7ab-60b6f3b26b81 | -12.76503 | -50.56425 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 4b80c75f-471e-3bda-93fb-f621e557bc29 | -12.76391 | -50.54961 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 647c70a7-9c27-34a2-8863-05908bf03234 | -12.76336 | -50.55313 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da01dd9c-72e8-311a-8574-3c3f66470f3f | -12.76281 | -50.55666 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 70cce363-9151-3707-a241-b3675798df0d | -12.76227 | -50.56019 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| fab29b4d-517a-3bc2-a063-92ae330f315c | -12.76171 | -50.56372 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5360440f-8db6-39e4-9bd9-28069dd0327b | -12.76117 | -50.56725 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 06d32dc0-554f-3869-9a27-80add10ad388 | -12.76115 | -50.54554 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7becb3f0-5e79-3d56-83b3-019cd5f52e82 | -12.7606 | -50.54907 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27bba27f-7c80-31d1-bace-721db37c11af | -12.75785 | -50.56671 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88860951-cdb1-3f45-bf5e-7700e04db54b | -12.75621 | -50.59899 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 683975e2-2a7b-38e9-a970-531bf43fe3fb | -12.37137 | -50.9738 | 2024-10-05 04:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc34cea8-c977-32bf-bf8a-5dc859396ac8 | -12.37081 | -50.97731 | 2024-10-05 04:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82b0a117-5e4f-3f1f-9d31-0fd3dd03b309 | -12.37025 | -50.98083 | 2024-10-05 04:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 382a91e4-9b11-3518-9404-f1eb8d80f08b | -12.3697 | -50.98436 | 2024-10-05 04:38:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3c88749c-fc27-38f8-abfc-da17e7dca45b | -13.05895 | -51.11525 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9781959-c8c5-385d-8609-18515bb27b44 | -13.0584 | -51.11878 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51825a94-99a5-3851-a6ae-4265ea831c45 | -13.05509 | -51.11824 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d090562-7796-37e7-88df-6af396437d27 | -12.99439 | -51.1155 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbda4a96-897e-355d-9aaf-dc2a8ac6d169 | -12.99383 | -51.11903 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c8e13e4f-6291-348d-873a-e5b9daf86e02 | -12.99327 | -51.12256 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 527c7aad-fbae-3b9a-a172-a68902d03a1a | -12.99271 | -51.12609 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2994577a-ad36-3bff-8fd2-ac4b88567142 | -12.99052 | -51.11848 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9d6e80da-0bae-3c67-90a2-91573a8e1249 | -12.98996 | -51.12202 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75698175-28d1-3f10-90ef-f15b3d1d3349 | -12.97995 | -51.12012 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6eb5ed64-19b3-34a9-b43c-0744d52ecaf6 | -12.97609 | -51.1231 | 2024-10-05 04:38:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a5b85fbc-7852-3605-b842-3a189149941a | -12.83566 | -50.56846 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2083d01e-4d88-3c17-b284-c005dc2e19ec | -12.83014 | -50.58204 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b848c8ce-ea24-3207-85f9-087969208fd9 | -12.82738 | -50.55627 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f2fa2fd2-2464-3060-ad3f-84c425caf1c1 | -12.82683 | -50.5598 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 426adc36-dd86-37d4-9256-53f7b1124243 | -12.82407 | -50.55573 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| da8b3397-08a2-394f-8898-7fddac403a13 | -12.82351 | -50.55926 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 73475420-d65b-3f77-867c-d3ec25098229 | -12.82296 | -50.56279 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0bfa8b51-e3c7-3571-af06-42a8ac920d55 | -12.82075 | -50.55519 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a7d59fd4-8a47-3c51-821a-9bce3b289b50 | -12.82021 | -50.58043 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9bf8702a-63c9-386a-9778-3acaec197de4 | -12.8202 | -50.55872 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 58d050b7-2e2b-3cf4-9998-83ade6d3483f | -12.81137 | -50.55006 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ac0314ed-f86f-315d-8491-610807a18a8e | -12.81082 | -50.55359 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d4c5fd37-5b4c-32fc-b330-d2fc40aecf20 | -12.81027 | -50.55711 | 2024-10-05 04:38:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README105.md)
