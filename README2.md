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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce6a5201-df10-3014-8498-78f7041c2c90 | -1.5299 | -54.9941 | 2024-11-10 00:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e28f14e1-1f75-3226-912e-a3a20332db29 | -1.3472 | -54.6178 | 2024-11-10 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| b699c963-7dba-3113-86cc-82411d7c5dc8 | -3.1239 | -50.4358 | 2024-11-10 00:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 9f20af1e-7c2c-3277-9095-2a1d8428a657 | -23.8678 | -54.0468 | 2024-11-10 00:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 115.3 |
| 752bb0c7-9666-3d6d-8a6c-89a160d0d7af | -8.39 | -44.16 | 2024-11-10 00:00:00 | MSG-03 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 493fb6b7-589b-3a6b-88be-b4c96407fac6 | -3.23 | -50.32 | 2024-11-10 00:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd5c2433-20ee-34a7-a13c-5c2de96e2d70 | -3.23 | -50.26 | 2024-11-10 00:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7f211536-887c-3776-8b19-250bce475453 | -17.59 | -57.51 | 2024-11-10 00:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5b987e56-c5cc-38cb-bb7e-ec6ed60d567e | -3.22 | -53.04 | 2024-11-10 00:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ee6b3ab-a1b9-3a91-bdea-6d5cd50c3209 | -3.14 | -50.42 | 2024-11-10 00:00:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b574dc89-299b-3eb2-a945-17558038932e | -3.61 | -47.35 | 2024-11-10 00:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 753bb546-243a-34b6-9970-50386bba986f | -17.59 | -57.44 | 2024-11-10 00:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e276db9-ff57-31fe-aaa7-c544cbe02a33 | -3.58 | -47.35 | 2024-11-10 00:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 550ee281-66bc-37a9-9fb5-b5ee85efb33d | -17.62 | -57.46 | 2024-11-10 00:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5d1abdba-76dc-3a20-a3e2-2665422bfb2e | -17.63 | -57.54 | 2024-11-10 00:00:00 | MSG-03 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bcb8c6e3-e706-3cfd-a724-ecd528ddaa41 | -9.8402 | -62.3877 | 2024-11-10 00:10:00 | GOES-16 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 4893b608-4768-3054-a2ac-b6b2f2c21e92 | 2.8552 | -60.0853 | 2024-11-10 00:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.8 |
| d957aed4-2d50-3969-ad47-23c96e0a956e | -3.2169 | -50.2651 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| e5cca0ac-69b5-3c85-827b-485b7ba2cc03 | -3.1422 | -50.4562 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 58801be7-60c8-37c0-9dfb-7dc586cc8c01 | -2.4661 | -48.4606 | 2024-11-10 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 2ca9f521-8730-352a-a6f8-270d1709f099 | -3.9483 | -48.1724 | 2024-11-10 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 3e58ddb3-121a-345f-9b6d-0b706ff101ba | -1.5163 | -52.1901 | 2024-11-10 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 58b0578e-eb11-34e7-b901-720a7b1490e4 | -1.4926 | -55.431 | 2024-11-10 00:10:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| 2a96df69-ffea-3076-a0c6-fed7dae87455 | -3.619 | -47.3388 | 2024-11-10 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| b65bc05e-2d8a-37a0-a431-466b7fe4db1b | -4.6736 | -45.1541 | 2024-11-10 00:10:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 64edc1cd-6b8c-3d72-a7a0-a1f852a0cb9c | -2.931 | -52.7753 | 2024-11-10 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 1f3ee255-eddb-3468-b97b-a48a14ab1bbf | -2.2487 | -47.0561 | 2024-11-10 00:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| fbbf7c4f-8cb1-3b32-a6a1-eb1421d3b9f0 | -2.9171 | -51.4618 | 2024-11-10 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| d6fe899b-74e8-326b-8392-c81816b2ff59 | -3.5712 | -45.8163 | 2024-11-10 00:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 95c47e19-7723-3b30-9af8-c4e80a397e4c | -3.1238 | -50.4568 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| afb3320c-5d6f-3d43-b30d-da38a60282bf | -2.7771 | -49.3704 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 03689ee9-99ed-31b4-9d17-8c77338ec8ff | -4.2058 | -45.4502 | 2024-11-10 00:10:00 | GOES-16 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e2d04b8a-927c-3d9c-971d-38f7e1b0b49e | -3.76 | -52.6491 | 2024-11-10 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| d6094dd4-7c8b-39c0-bb8e-37e2a8cc2a32 | -2.0768 | -48.8342 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 9754a19b-4788-3783-bea5-f8d9051102d1 | -2.7587 | -49.3497 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 533626e8-1168-301d-8914-09b8ef1e0b4e | -2.9257 | -49.1534 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 16b98243-bf20-3143-a4a9-0784a8836b97 | -2.4662 | -48.4391 | 2024-11-10 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 35eda712-9c5b-3dff-91d1-be232bc27493 | -4.1112 | -45.7018 | 2024-11-10 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 123.7 |
| 839a630e-80b1-3d90-bc6f-0eee20722aa9 | -1.4742 | -55.4312 | 2024-11-10 00:10:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bef1cffa-5af3-3fad-9c5b-388c79163e35 | -3.9669 | -48.1716 | 2024-11-10 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 196.6 |
| eb0c1613-fb99-3909-bbdf-57dde69ef509 | -3.5819 | -47.3403 | 2024-11-10 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 845ae2ac-1aa5-36a4-8ce0-617d4e725006 | -3.2244 | -53.0524 | 2024-11-10 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 221.7 |
| 942de5e9-fe1f-3b39-9949-53157d608a8a | -2.2672 | -47.0556 | 2024-11-10 00:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 8ae45624-6b4a-3989-8fcc-01ab8d7d3090 | -2.2095 | -47.733 | 2024-11-10 00:10:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 6f760213-0c6b-3012-9bea-b9ad8693b456 | -5.1774 | -47.6114 | 2024-11-10 00:10:00 | GOES-16 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 5aa5f1ea-b50a-3eef-97e9-ba5608ce019f | -3.967 | -48.15 | 2024-11-10 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 103301b0-0484-3a45-9b8a-a806c7934489 | -2.109 | -50.5663 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4473b783-f60d-36ed-b173-775356771b3f | -2.2075 | -48.3811 | 2024-11-10 00:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 901f20f3-c409-3909-9fb5-3108e789333a | -3.2352 | -50.2855 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 317.2 |
| b6c5cbb5-f88c-3916-b01e-c03557284de7 | -2.2094 | -47.7547 | 2024-11-10 00:10:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 2fc7d4e0-a416-37a8-82ca-5f1173c7e049 | -1.5163 | -52.2106 | 2024-11-10 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| e21507f0-1d65-3b42-8773-b8e9f397dd89 | -1.5347 | -52.2104 | 2024-11-10 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 244.3 |
| 9c35bd55-3acf-3fc1-b8ea-8bf948d2d3bc | -2.9355 | -51.482 | 2024-11-10 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 1ed4e7bb-0040-3080-91a1-9f7c13cca136 | -23.8672 | -54.0692 | 2024-11-10 00:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 80.1 |
| fb1dcfd6-3cf8-3bb4-b576-a06f73e6da82 | -3.2243 | -53.0727 | 2024-11-10 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 201.2 |
| 334e6cde-db80-371e-8389-1a5a5359a13e | -3.0351 | -49.5325 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| aab83a37-09fe-3e86-8d0e-aa88e1db26ae | -3.2167 | -50.3071 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| a6a4494c-9700-35b8-9176-b6317913a7f9 | -8.3964 | -44.1597 | 2024-11-10 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 32284651-422e-3229-a121-4539b199c7f4 | -3.2427 | -53.0722 | 2024-11-10 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 148.3 |
| 66d78a78-5959-3137-bb89-c1996dbc8ffa | -2.9249 | -49.3661 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d88ad94c-6d0b-3045-a9b7-65eb4ae4a10a | -8.3967 | -44.1365 | 2024-11-10 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| bc480adf-afff-3caf-9770-c5cafb73f610 | -2.9356 | -51.4613 | 2024-11-10 00:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b0e5b7c6-bda8-3282-a6f7-c53d6cb3ad3c | -2.7772 | -49.3492 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| a4af4469-a7ee-3632-b59e-5197a5141c32 | -2.9442 | -49.1529 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| fd1edf67-8a81-37c8-acd1-59cf07ab55ce | -4.6922 | -45.153 | 2024-11-10 00:10:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 22d4cea8-4d6b-35d0-96b0-46e6b8f6dcc1 | -3.035 | -49.5537 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 7b2d25fd-f21d-3593-a277-5cffa990de68 | -23.8884 | -54.0649 | 2024-11-10 00:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 112.2 |
| cd8eaa1f-c9fd-31de-89ab-37708f2a82ef | -3.5818 | -47.3621 | 2024-11-10 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| df068ea2-6b71-3a5c-9db9-dc1d9ceee5ff | -3.1239 | -50.4358 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| 897e86ad-f214-365d-9115-02584ae613ff | -17.2933 | -57.4857 | 2024-11-10 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 206.8 |
| be62e7ad-2a3e-39b4-a143-a26803054022 | -3.6004 | -47.3395 | 2024-11-10 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 325.0 |
| 14534320-8257-35f4-841e-33c7b073fcf6 | -17.293 | -57.5062 | 2024-11-10 00:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.1 |
| 61f9675b-904f-38df-bacf-7620490427f2 | -1.4925 | -55.4508 | 2024-11-10 00:10:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| bb384ade-8a49-354f-8bcf-9b48db7339c5 | -8.3778 | -44.1386 | 2024-11-10 00:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 91814b1c-f591-3e72-a574-4a42d4d4130c | -2.4847 | -48.4386 | 2024-11-10 00:10:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 83bdb894-a26d-3f3e-b1ae-0af733f6b1b8 | -3.2168 | -50.2861 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 159.8 |
| e84cfcee-e359-31be-86bc-8666561e77cf | -3.9668 | -48.1932 | 2024-11-10 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 6d723879-45ef-30bc-b9e3-8af3189d77c3 | -2.7586 | -49.371 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| c8014a81-3577-33a5-aa16-6d56afbfd400 | -4.2083 | -48.1176 | 2024-11-10 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 2bfdda0b-ed97-369a-b894-5b6547861de2 | -3.525 | -44.0286 | 2024-11-10 00:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 152.1 |
| 320a4f2c-11ea-3e2b-ab74-6a83d44e27f3 | -3.8413 | -44.1283 | 2024-11-10 00:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 1978b4a9-8139-35a5-a015-ca33839023e7 | -23.9095 | -54.0606 | 2024-11-10 00:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 08da6b50-2a22-3d9a-938c-ec802ace8877 | -3.1423 | -50.4352 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 204.5 |
| dc123cce-eafb-3e42-999b-6af1f96f4649 | -4.054 | -49.1978 | 2024-11-10 00:10:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 37c68988-792d-37ad-b94c-9ec9a8ce8c5a | -3.76 | -52.6695 | 2024-11-10 00:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 7386357d-213b-3fcc-87e1-dcefc3c04422 | -1.5347 | -52.1899 | 2024-11-10 00:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 623e2bee-6538-3002-bf3e-77a1c1ccaf6c | -3.0213 | -53.2607 | 2024-11-10 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| e45622bf-80bf-3338-a876-c9451363a24d | -2.2671 | -47.0775 | 2024-11-10 00:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| fd3ed93e-7930-3f36-a074-16101ff4e4c0 | -2.2076 | -48.3596 | 2024-11-10 00:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d997f98a-5328-3860-9a9f-97f3de7710a1 | -1.4742 | -55.451 | 2024-11-10 00:10:00 | GOES-16 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| da15aebd-3a55-3ecc-9922-13751e055ba8 | -5.0101 | -45.0433 | 2024-11-10 00:10:00 | GOES-16 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| ff911ca3-0637-3ed9-af93-7d125477a168 | -3.1095 | -49.4241 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| c994f48e-a9f5-37dc-b81a-c8c2dc228e1f | -3.3097 | -50.136 | 2024-11-10 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| cd8b4dad-b5aa-3deb-a396-edddb6a90938 | -3.2428 | -53.0519 | 2024-11-10 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 6095fc62-95b8-38c9-944f-5f5228699ef8 | -3.2352 | -50.3065 | 2024-11-10 00:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 4dc8cd11-807b-3ed7-830c-603ef1a5878b | -2.0953 | -48.8338 | 2024-11-10 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 151.5 |
| d16c2afb-03f5-31e3-8a37-b349e37525db | -4.8916 | -48.6234 | 2024-11-10 00:10:00 | GOES-16 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 06e600cd-5f96-3733-bd2f-61a5714b6d4b | -3.9482 | -48.194 | 2024-11-10 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| e24d7068-445f-3d88-a885-9e9254493ac9 | -3.5064 | -44.0294 | 2024-11-10 00:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 9d3b0822-cf78-3396-8ef2-a2cf6dacee06 | -3.6189 | -47.3606 | 2024-11-10 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |


[Clique aqui para ver as próximas entradas](README3.md)
