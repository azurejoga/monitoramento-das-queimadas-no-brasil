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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39921cfe-7515-35cf-809d-3ef56ba561b4 | -13.73055 | -47.87606 | 2026-07-01 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33eeec7f-4f66-33ea-ab08-acdd57115545 | -13.08695 | -42.14114 | 2026-07-01 04:04:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bc76b7ae-fe4e-3a59-a298-1f85a056d6b9 | -17.03372 | -43.26171 | 2026-07-01 04:04:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f70a3ec3-bb5d-3239-aab9-7638fff72d80 | -12.75923 | -44.49208 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 1398b89e-b947-3fe1-8fd9-d8faa1a148b9 | -16.35789 | -49.33015 | 2026-07-01 04:04:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e1b0875-693c-3b7b-a4c7-1aa2b6408fd4 | -12.83562 | -44.34558 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| f7589066-7745-3c67-97d5-d9d2d3fcca70 | -12.79882 | -54.86058 | 2026-07-01 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 872c5669-5ff0-3adf-8732-c1edbbc1a4c6 | -16.35855 | -56.6607 | 2026-07-01 04:04:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 09113062-c07a-3f04-aa47-3fb1cfbf2720 | -12.76427 | -44.48425 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 0bf5a60e-d1c1-3a3d-8d15-d4d9630851f5 | -13.09083 | -42.13811 | 2026-07-01 04:04:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c1ab0000-c1db-3aca-b8e2-b272b329573c | -12.77432 | -44.49035 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bac96398-1991-3235-b597-63a86cb67569 | -15.60724 | -43.59827 | 2026-07-01 04:04:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d5fe69a-a720-300e-aaae-4c6d71388c7a | -13.481 | -47.87685 | 2026-07-01 04:04:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| aac10b67-1ece-3a1b-aafe-88eb57f3afe6 | -17.70937 | -46.78078 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15d3b542-0c40-3845-8e2c-b23634b2253a | -12.84136 | -44.35513 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 96aac895-337f-3eb8-aeea-15ffd2bb8599 | -12.75506 | -44.48401 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 51d25705-45cb-3174-afba-69495bb0e3a8 | -17.71108 | -46.78859 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 93298961-e018-3cef-b193-a664adbcbaa4 | -12.76569 | -44.49757 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| f31836e2-787b-3b2f-ac14-053d34b98553 | -12.44401 | -49.57768 | 2026-07-01 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd12dc6a-6c79-3d42-9601-431f9bed7816 | -12.75349 | -44.48238 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24579a47-1486-340e-8d31-c30dcef911cd | -12.76068 | -44.48362 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 579f3fe2-80ee-3d02-b040-a539d98aae3a | -12.75436 | -44.48825 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4dd016d8-1b2e-311d-a5e3-b7a828c96158 | -12.76283 | -44.4927 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| cb95d179-1758-37e2-b2cd-63e4f2af18af | -10.68071 | -54.53716 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 1b55c12a-d163-3cc8-9c4b-0b3a13e2b972 | -12.83206 | -44.34498 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 7787829e-b3b3-3f5a-928c-5ccced6e7ad2 | -12.75709 | -44.483 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d91e7b17-d994-3b77-a575-63f9fffe05bf | -12.84702 | -44.34325 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 7e3f440d-0054-34fc-8509-1682fac8e60f | -16.36559 | -56.66243 | 2026-07-01 04:04:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 3ca8d24f-1b02-3b9d-b55d-1535eb9ce8d4 | -14.62893 | -54.47001 | 2026-07-01 04:04:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e88169c8-f9b6-3e85-b6b6-d85864a90750 | -12.77001 | -44.49396 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 8e9b6d40-beb9-30a8-9084-68e88a1706a4 | -12.44899 | -49.57858 | 2026-07-01 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1991682c-6ed6-3192-a089-ad11192916b0 | -12.77504 | -44.48612 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fbd5602-8ba4-3806-8819-681956f44246 | -15.60663 | -43.60204 | 2026-07-01 04:04:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73302fe5-4752-3f26-8cb4-2929c5990e14 | -15.24232 | -48.56404 | 2026-07-01 04:04:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05eb4960-16b9-305c-a019-f6fe41e4d72f | -16.35749 | -49.3339 | 2026-07-01 04:04:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6063acd1-3fac-3213-87be-a9df3e1dface | -12.83423 | -44.35392 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 97f01870-5834-372b-a49b-fac5f941c6d4 | -10.66679 | -54.53459 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2ba2995e-6b0e-3ede-8469-5fd93af1b596 | -15.59987 | -43.60086 | 2026-07-01 04:04:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fc3424c9-bb25-34fb-acba-f51d7f8f3883 | -12.76642 | -44.49333 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 06236dbe-20a5-3536-944e-691c60ffe86f | -19.95909 | -42.24214 | 2026-07-01 04:04:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3f91db9a-1ba0-33a3-943d-b78c143b5468 | -10.66538 | -54.57621 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 524994f0-70f9-323f-8092-95eccfcf8f71 | -13.08752 | -42.13757 | 2026-07-01 04:04:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 228246ca-ed23-363b-a500-66a38fdcd5ff | -15.21693 | -42.59544 | 2026-07-01 04:04:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7179d7c5-1be7-3b03-9eac-efe1e0711aac | -10.66945 | -54.52176 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 48e82c28-9fc6-3a7c-ac14-303ce77e3893 | -17.70817 | -46.78302 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62f60a5c-9dfe-36ba-b872-20d9f85e7b34 | -17.44393 | -47.16607 | 2026-07-01 04:04:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e960bd4f-df4d-3e39-ae54-b07a38ffef17 | -12.79743 | -54.86709 | 2026-07-01 04:04:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10ad2133-a462-3e7a-8696-62ece2a970a2 | -12.75277 | -44.4866 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eda95367-a687-31ae-99da-bdfc3b3e441f | -16.35503 | -56.65974 | 2026-07-01 04:04:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.3 |
| 5ec85653-969a-3591-947c-db201fce4f36 | -12.77073 | -44.48973 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 313.8 |
| 4c81a435-bd61-326b-8459-4d4d82e714d0 | -12.83352 | -44.35809 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 78db7d9b-08b1-36f8-bcd4-0552351ed525 | -12.82779 | -44.34854 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 8adf5d6a-5bcb-364e-b200-d2032a4ed95e | -15.60325 | -43.60145 | 2026-07-01 04:04:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4bb7ed31-3b78-3380-86eb-4f4aa12ed6d9 | -12.76499 | -44.48002 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 243e03b8-a486-32ea-88e2-44640355b43d | -10.6599 | -54.5677 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d700cdd0-1ac2-3ad7-ad31-4835e796a16c | -17.7178 | -46.79486 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6908df6c-b3d6-3800-85f6-607bb17dc4ca | -15.94801 | -48.14771 | 2026-07-01 04:04:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88af1f83-572e-314d-bdf4-f620c4dd3188 | -14.2059 | -42.76626 | 2026-07-01 04:04:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7a75a707-28a4-38c0-bb87-b19f56301e25 | -16.58269 | -45.87702 | 2026-07-01 04:04:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2514594e-5362-3c28-9635-feee5c3acbc9 | -14.04925 | -46.33045 | 2026-07-01 04:04:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f965314-c5d8-394c-9593-9cd5320ff30b | -15.22024 | -42.59599 | 2026-07-01 04:04:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 282cfc2f-2727-321a-810d-459e67043d2e | -12.83919 | -44.34618 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| f06f5ed3-0439-389b-b403-ddf3f8c7f58d | -12.8371 | -44.3587 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5ac57167-b245-3b85-ac20-8c9f92c1570b | -10.66825 | -54.56237 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c4cbe43-9528-364d-a9c9-976d320e7a43 | -17.71578 | -46.78432 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b6740cac-e49d-39a6-b82c-06ed27280ac2 | -12.75996 | -44.48784 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 208.6 |
| b1bb8c9f-57d2-30c6-810f-42edd903bbd0 | -12.84276 | -44.3468 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 3700961f-1742-3ac2-9ca4-5a92da60dc46 | -12.44845 | -49.58147 | 2026-07-01 04:04:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6b74442-e214-3b9a-b1b4-e8a6b68c3517 | -12.76786 | -44.48487 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 313.8 |
| 4cd6acd7-1bd5-3fe1-9041-7a82729ff401 | -10.67375 | -54.53587 | 2026-07-01 04:04:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 871646a0-a75b-3392-8874-11891fff422e | -12.83779 | -44.35452 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| df9199db-ddb9-38be-90fc-0d034d040753 | -12.83849 | -44.35035 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 98b4f089-fd5b-3203-b4ab-e37fddc6b120 | -18.08988 | -40.07655 | 2026-07-01 04:04:00 | NOAA-21 | PEDRO CANÁRIO | ESPÍRITO SANTO | Brasil | 3204054 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a36fa738-f5e2-3f62-99a8-52513b69afdd | -12.77145 | -44.4855 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 313.8 |
| a519af5a-073b-37d2-93d4-8138108f1483 | -17.71018 | -46.79353 | 2026-07-01 04:04:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b48ae5d8-3a0c-3eba-855d-d3661d2994ee | -17.1202 | -50.09194 | 2026-07-01 04:04:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 934b6d0e-d0e3-324d-9230-2efd6c3cded3 | -12.75636 | -44.48722 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 580b4740-985c-3aed-a697-6ed62fdab6e2 | -12.84066 | -44.3593 | 2026-07-01 04:04:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46db20bf-c34b-3863-b45c-72871a235892 | -19.3292 | -41.25466 | 2026-07-01 04:04:00 | NOAA-21 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3f35c8f9-b002-39ee-a0dd-c405965785a6 | -16.36208 | -56.66144 | 2026-07-01 04:04:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.3 |
| d74d8d7c-a0f0-3ae5-97f2-32633ec7b0bb | -17.91434 | -52.7137 | 2026-07-01 04:04:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdee116d-3621-3de7-a6da-dbc704343a62 | -22.60566 | -47.04553 | 2026-07-01 04:06:00 | NOAA-21 | HOLAMBRA | SÃO PAULO | Brasil | 3519055 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe33f9f8-e46d-3cc5-b834-79c00d64c308 | -22.23091 | -50.86205 | 2026-07-01 04:06:00 | NOAA-21 | RANCHARIA | SÃO PAULO | Brasil | 3542206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 59ce47ce-6d17-3ac0-b28e-9659857d78e3 | -21.09752 | -57.46476 | 2026-07-01 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f40027ca-3960-3c3e-b302-f284c19de524 | -20.55175 | -48.5331 | 2026-07-01 04:06:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68909dae-7f27-3cd6-9e0d-f295b0c8e32d | -19.51031 | -52.74266 | 2026-07-01 04:06:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ce0164b8-60bb-33a0-9eb0-def5f23a8643 | -22.69934 | -53.96243 | 2026-07-01 04:06:00 | NOAA-21 | JATEÍ | MATO GROSSO DO SUL | Brasil | 5005103 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 20b71cec-5977-3c15-8eaa-051d19111f4d | -21.49257 | -48.53985 | 2026-07-01 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b67f6a4c-7f2f-3840-ab16-a8acfa20d93d | -22.80325 | -49.35022 | 2026-07-01 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 800f01bb-69a9-3ddc-ad3a-6dd68af0d827 | -23.56615 | -47.51054 | 2026-07-01 04:06:00 | NOAA-21 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 561a5d8c-ce24-3702-96a8-cb6faee61020 | -21.09588 | -57.47141 | 2026-07-01 04:06:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac3107ef-7835-3a06-b729-ada4ea83fb16 | -22.4372 | -51.86576 | 2026-07-01 04:06:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 010abf8c-3b00-3cd4-b62a-9566b217efbd | -21.80633 | -52.71805 | 2026-07-01 04:06:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b54c2506-78d5-3303-9d91-6e20bc7675a2 | -20.54776 | -48.53215 | 2026-07-01 04:06:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ebcba42d-550e-33d3-ab94-e79552d021cc | -24.31913 | -53.59376 | 2026-07-01 04:06:00 | NOAA-21 | ASSIS CHATEAUBRIAND | PARANÁ | Brasil | 4102000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4cdf42b1-785e-381d-b9f0-dd94519d6c4f | -22.80317 | -49.34949 | 2026-07-01 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67cb414e-9d80-32b6-8247-8fad685ed77d | -22.43122 | -51.87046 | 2026-07-01 04:06:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 784079a1-8491-3acc-a06b-d72aea9b41e4 | -23.82257 | -48.71386 | 2026-07-01 04:06:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c395c4f4-fb98-3ff5-9f6c-bf49c0f19bcc | -19.51636 | -52.74047 | 2026-07-01 04:06:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 940e9493-1eb7-3799-a944-84128c383854 | -22.79115 | -49.34731 | 2026-07-01 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README13.md)
