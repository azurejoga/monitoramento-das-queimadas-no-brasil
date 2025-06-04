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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b8312dc-708b-3f24-a80a-3b7fb818ecf4 | -7.14914 | -44.04347 | 2025-06-04 04:00:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 36de3fc7-93f5-3c12-b43d-c23cce9db32a | -7.90209 | -50.36293 | 2025-06-04 04:00:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c42900a-1c04-31c8-a58f-cc12bb6007ab | -7.08323 | -49.59745 | 2025-06-04 04:00:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79f16efc-1f8e-3a94-9f63-789cbb2c82a0 | -6.8117 | -44.9095 | 2025-06-04 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1213dd0d-5483-3152-8b15-7e75c1f2fbe5 | -7.98597 | -47.23331 | 2025-06-04 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4bd0c035-0f0e-3300-894a-c53a0c22fcb8 | -9.31332 | -49.49374 | 2025-06-04 04:00:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 540ee0d3-3592-3d26-8466-7e82ce6804b6 | -7.88152 | -46.18642 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0a42ec21-1f99-3b42-8467-42848c89aefa | -6.96804 | -42.91057 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 726568e8-e512-37be-8359-b34e22254571 | -7.55492 | -45.83656 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d133c802-9ed9-3df8-8de9-7bff9359f3fc | -7.58516 | -45.86163 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 650f01af-0d38-3455-95d4-554b97346d0c | -7.88939 | -46.1918 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69c38c9a-ce60-3507-b00c-0f421ab04eeb | -7.89997 | -50.35966 | 2025-06-04 04:00:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e8d682b5-5eeb-3457-898e-9795251063c3 | -7.90561 | -50.3607 | 2025-06-04 04:00:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ca497e3-71e7-382f-9777-995a46ac8b56 | -10.67551 | -44.38137 | 2025-06-04 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a868c1a5-b8f1-35e1-8dd6-c5ab84c9c2d0 | -6.54309 | -44.64438 | 2025-06-04 04:00:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9c67fcd-d55e-3f52-8dee-9abe3fee7946 | -8.74996 | -49.76953 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f1fdc8a4-4f82-314f-9cf3-adffa25176bb | -6.86609 | -47.84899 | 2025-06-04 04:00:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2afd7e29-bfd8-3746-af91-c30f3a6e63d2 | -9.39745 | -48.4361 | 2025-06-04 04:00:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 165d8724-beeb-36c2-ae20-62b78d22996f | -8.46326 | -46.51281 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60636d7b-2170-36d6-8471-5a8eb80d29a2 | -7.73713 | -42.70836 | 2025-06-04 04:00:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c234f4c4-2822-3cf7-9783-2cc2b2b8aee3 | -6.96027 | -42.91343 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 567d0778-fb7b-3502-b699-93667e069130 | -6.36799 | -43.68052 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f406faa9-25d3-33ed-86bc-7b553cbfd1b1 | -8.68705 | -36.248 | 2025-06-04 04:00:00 | NOAA-20 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e8d0fa28-f863-3a9c-9f56-ca3285cd1a86 | -7.58583 | -45.85772 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b584573a-6d04-36f6-8c69-0725e09890ec | -7.21705 | -43.13293 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 01decf5c-6b56-3a6e-9b90-3af03fcf2319 | -7.89272 | -46.19076 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 91f76c63-92e3-333d-b69b-7d185996870e | -7.23684 | -44.19492 | 2025-06-04 04:00:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8a228fd-e368-39e1-afae-c927d787e76e | -7.21863 | -43.13455 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| ef15ac36-29c5-377c-ae57-a77d5f68b45b | -7.16816 | -43.4698 | 2025-06-04 04:00:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 65c8f9b5-77ce-3297-9c87-2f1c847eb374 | -8.90499 | -50.04203 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 32d1a637-de1a-337c-bd95-f33802dc353a | -8.89721 | -44.78084 | 2025-06-04 04:00:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e89d3fbc-c775-33c5-b33a-a7b117e753b4 | -5.18246 | -48.0807 | 2025-06-04 04:00:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cefc6103-2657-3129-9e20-cb753fcd5651 | -10.55045 | -42.4351 | 2025-06-04 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c47983c5-62bb-364e-8c79-06f40c4d9dbd | -8.83825 | -49.84771 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aadba867-ae1a-3302-bc3c-fcb513c467b9 | -10.56515 | -48.51612 | 2025-06-04 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d93339f6-cf86-3a1a-a0a7-5119a45b6fcb | -9.2598 | -47.64986 | 2025-06-04 04:00:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a1322b57-6120-3ab0-9247-42698aeaf720 | -7.32339 | -45.56015 | 2025-06-04 04:00:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5b0a5f89-bab7-3ccc-b1e6-3bccc16241c4 | -7.11442 | -43.29695 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f817d17d-46f5-35c8-8628-32abb1b82744 | -7.01131 | -44.58831 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 30233c7c-6aea-30e0-b905-24d722aeef14 | -8.47185 | -46.48863 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 93894b57-40a7-30e5-a3a1-90c1c05722d8 | -7.89433 | -46.18852 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65ca7739-4787-3c48-bb08-bad5cb7e2b24 | -8.75057 | -49.76614 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 42d77b53-d3e9-3050-af34-4b12332cb545 | -9.20186 | -49.68973 | 2025-06-04 04:00:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53ea20e6-60c0-36f5-b4d8-6efb8b2802ee | -6.21509 | -43.33995 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| bb3420c9-c4de-3b5d-abd6-153c24f3595b | -6.63402 | -43.20695 | 2025-06-04 04:00:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9f5d4007-e1dc-31ac-8ab6-e38450d5ae27 | -6.71246 | -42.58924 | 2025-06-04 04:00:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| a261ede0-499f-3888-ab16-fbe2bef3e068 | -11.62573 | -41.83493 | 2025-06-04 04:00:00 | NOAA-20 | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 471e2358-b0ff-3d04-b1c7-9901851f2c86 | -6.81108 | -44.91308 | 2025-06-04 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 239a5c81-6957-34f9-bc64-7771baf622bf | -7.8858 | -46.18704 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 114f3473-20c2-3aa2-944d-e6b0f8dc01b3 | -7.0111 | -44.61339 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| db6612c7-f7a2-34cd-910f-4d27d26e8aaa | -6.71775 | -42.9099 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a686259d-44a0-35d7-8c2b-c67f9f959ee5 | -10.54986 | -42.43877 | 2025-06-04 04:00:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c7567f2a-b826-3f1a-8b16-3f5b4684e2b1 | -10.26048 | -48.45702 | 2025-06-04 04:00:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0f88f26b-ce2d-3f48-89a9-d8b3db4a26fd | -7.0826 | -49.60103 | 2025-06-04 04:00:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2da9275c-d038-3b79-a7b9-a05c938468f7 | -6.96449 | -42.90997 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 01f63614-f6c3-37f7-ac0a-b12293a33a02 | -10.69569 | -44.8161 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ab2b888-65ff-3f14-8ea0-4d0869b4fa29 | -7.00716 | -44.61294 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef81e416-812f-3991-aa6d-35780c338a41 | -7.55138 | -45.83207 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5fd668d-d42d-35ed-9654-82efe4951c45 | -7.68615 | -44.56962 | 2025-06-04 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 110bd1e6-f2fb-3ccd-9889-6fb060a78bff | -7.22986 | -43.12235 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7282fa55-5e31-34ae-befa-f185a6b23cc2 | -6.37097 | -43.68561 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23e44be8-9901-39fa-b07a-18477caa56da | -6.96582 | -42.90189 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.1 |
| dd0b5519-4090-3d63-8d1d-5d4bd263f390 | -7.5845 | -45.86555 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| de79eed6-6e50-304c-b7f6-a58201d804e2 | -8.55404 | -44.55421 | 2025-06-04 04:00:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 00233ebe-bab3-349b-8bb0-be3e6e2cba5c | -10.61549 | -44.76191 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 55e8d9f6-bc48-3758-aa51-be69c7ac31af | -7.69 | -44.57028 | 2025-06-04 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0a841a49-1630-3f22-a1ea-3ef2961caa79 | -7.1108 | -43.29636 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 69e7edf7-ad62-3155-a2b1-7b2278ae04c9 | -8.07628 | -43.11551 | 2025-06-04 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.0 |
| 1c2df819-b99d-371f-9f76-68c2d1ac68d8 | -8.36386 | -45.06137 | 2025-06-04 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 81832654-9f43-3b21-a2ce-38bfa3ba50d0 | -6.2092 | -43.33011 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 132ea56d-7d91-376e-b3fb-102b869eccfa | -7.88511 | -46.19112 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1937b243-2398-3e13-9817-edccb63b4e52 | -8.90975 | -50.04672 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9f037ab2-448c-3c9f-ad1d-0e0a6646927e | -7.0136 | -44.5985 | 2025-06-04 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| eb595d89-8494-3ce6-bf4f-0e34834e6973 | -9.34657 | -40.50669 | 2025-06-04 04:00:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4b32506f-6905-3323-9664-4a5f9a1cce47 | -8.91073 | -48.90623 | 2025-06-04 04:00:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f510de2e-2e24-33d2-8659-d00bed36a880 | -6.96871 | -42.90652 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 7359314d-88c2-3dbc-8e41-147088061a87 | -8.06919 | -43.11431 | 2025-06-04 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 93f93937-2ee4-3189-b510-3ed17e83ad9b | -6.56149 | -44.48845 | 2025-06-04 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f741c35c-c647-31b9-88fd-763d34f059c0 | -10.67845 | -44.38631 | 2025-06-04 04:00:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec28c230-f3b9-3610-8dbe-72fb829c1132 | -8.74934 | -49.77293 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a4d8f4e0-4c50-3cea-b37d-36cc54a8a9fe | -7.21637 | -43.12573 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 28bf2302-3563-3168-9529-9c47d9f7661a | -7.21504 | -43.13397 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d08a70ca-45e0-30fb-b040-4a3b71fb8517 | -7.21996 | -43.12631 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 052226d0-2ef4-3197-bfc4-e29fa7adb5a1 | -8.84363 | -49.84865 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2efafe05-e0f0-3308-baa0-95f299d9a2e8 | -10.61923 | -44.76257 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 47836b6b-2dfe-3e46-9196-a716c623cc2b | -6.81386 | -44.90944 | 2025-06-04 04:00:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f94ff1c8-f1b0-35d9-9258-8b953a1f73bb | -7.21346 | -43.13235 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| c94f388a-4834-31ad-a063-4a4fae9b3396 | -7.21145 | -43.13338 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c77a421c-36d2-3790-83a8-11751e757622 | -10.61175 | -44.76126 | 2025-06-04 04:00:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2b12f7ab-69b9-3717-b1ac-1a28c0c6f8a6 | -6.29159 | -47.01139 | 2025-06-04 04:00:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b2784526-228f-39b6-9ca3-b73e1c126206 | -9.56712 | -50.51707 | 2025-06-04 04:00:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f8468f7-6cb4-3509-86e7-7b02100c2a0d | -8.83888 | -49.84426 | 2025-06-04 04:00:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddbf5744-0f9c-385a-b433-e444058a04e6 | -7.98061 | -47.23698 | 2025-06-04 04:00:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feb7dc5a-919e-3cb4-a644-add5c68998fc | -8.09842 | -46.28096 | 2025-06-04 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5b9539d-8783-3bb0-912c-047a5df15a37 | -8.07693 | -43.11147 | 2025-06-04 04:00:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 400aae52-29c5-3f23-afa9-c5e66216411d | -6.24455 | -43.36692 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 5b21cf51-418b-30da-bc55-5cee20f4521d | -6.21286 | -43.3307 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cdfcf787-e015-3596-ba3a-3e78073ea254 | -6.96515 | -42.90593 | 2025-06-04 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.1 |
| c9fd64af-254c-33cc-af3e-7739f7cc1efc | -8.36695 | -45.06701 | 2025-06-04 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a0357fd-57ee-393d-9d24-41c6ed1f6bc2 | -6.24384 | -43.3712 | 2025-06-04 04:00:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |


[Clique aqui para ver as próximas entradas](README7.md)
