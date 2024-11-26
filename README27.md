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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6cab71c-b65e-391e-ae7c-826eccf983ee | -3.50137 | -53.81958 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08d62356-6184-35aa-8fd2-dd7f5014f5bd | -3.26911 | -50.441 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a6d6d4f-f987-393d-a629-c1bf095d5580 | -4.5377 | -43.28732 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a1ab87d-ac05-3313-91da-5350c27e97f4 | -3.50376 | -53.80493 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebc7b53a-d54b-3bce-a765-3843ed8de120 | -2.40172 | -53.68245 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9715088f-2468-38f9-a16e-c0857caca8bf | -2.71522 | -46.24264 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 815452dd-f76f-33f1-af7a-21acb9d8675d | -3.94235 | -47.98761 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa8290b4-d63e-3e50-bbfe-8f3ad8a37245 | -3.07403 | -49.20316 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 87d218a2-279e-3992-930a-e792c6f19bf1 | -5.07092 | -46.77206 | 2024-11-26 04:38:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 125d8f63-34ec-3a41-bec1-04f5bdb7a930 | -2.1502 | -48.04289 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0b13eaa-a6a6-30d5-9936-0239fd0ac71e | -1.48169 | -53.8114 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ee9014e-f528-34e4-8750-3d17516af4ce | -3.3984 | -50.0224 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 827cadfb-3e65-33e9-aa77-8f33c9e0b160 | -3.94569 | -47.98814 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d5b664be-10a0-3f3c-ad66-43bedc82ce80 | -3.2892 | -50.53508 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8d30dc7-0ad3-3ad3-b65b-f25feee887ac | -4.23874 | -48.70566 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e42cdbfa-a181-3d0d-b2cf-848b2893f5b7 | -4.51654 | -48.91949 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c699170-75ac-3fac-97ee-229884e6f0ce | -6.91728 | -37.10616 | 2024-11-26 04:38:00 | NPP-375D | SÃO MAMEDE | PARAÍBA | Brasil | 2514909 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c1032e6c-2b86-38e1-b909-1e6af353e5e2 | -2.59673 | -46.26443 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e5e6aa7-4d46-31d2-8c28-f4464a09065c | -4.1906 | -48.41138 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f02a82a-0817-3b83-be9e-6d0dcf22e53b | -2.79282 | -51.68179 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b43f85ae-5de0-3e30-a199-40ea1748e68f | -2.71172 | -48.66788 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 727e4d58-9763-3378-ae9b-aff71889e374 | -6.07304 | -48.03038 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a747732-a5d7-3fa7-af8e-12c264b6d05a | -3.54514 | -50.39705 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17ea804f-97d6-30ca-8aa6-17c56a364fe8 | -2.57926 | -45.47588 | 2024-11-26 04:38:00 | NPP-375D | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cf92ebc9-5fdd-3ab0-b1f6-132508dfe80f | -6.94197 | -42.83163 | 2024-11-26 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b6282b64-45a9-3da6-9f7d-214c8acfd7a9 | -3.9756 | -48.07503 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2c9819a9-a793-3f66-95bc-54f7e5e17784 | -3.29548 | -50.53983 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3b2e3a1-3555-3a70-a1fa-633fc487b471 | -3.28056 | -50.0184 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4a9967a-4cce-3036-b19c-aac8fa12248d | -6.9426 | -42.82715 | 2024-11-26 04:38:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 14ecfb37-ae11-3489-b194-4317ecf6d784 | -3.99398 | -48.08858 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfd00328-e1b7-3770-a2c0-d85a7bfbf618 | -3.48149 | -48.22942 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d39729ee-06e9-3a0d-b940-adff9cddfa24 | -5.27931 | -45.12528 | 2024-11-26 04:38:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bea37f6-a459-31f0-b358-9cdc9bc79901 | -2.90078 | -51.56606 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f85eb8f0-d698-30b4-93d5-240913cfe4b1 | -5.98154 | -43.76451 | 2024-11-26 04:38:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 941a6321-c072-3fdd-a844-5fddbc979f41 | -5.9472 | -39.67119 | 2024-11-26 04:38:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 1139ff32-45ad-3c94-846a-02c453c6e969 | -2.64343 | -48.48027 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dcdaa33-a0ea-3313-a877-d88e9331d291 | -3.30147 | -47.02222 | 2024-11-26 04:38:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2f0ffbb-a8e7-3463-a5fa-2c6f39903fb9 | -2.7372 | -54.13465 | 2024-11-26 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1eb23f55-708f-39b6-9c38-dafbf4f54a64 | -6.07811 | -48.04212 | 2024-11-26 04:38:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8706cd5f-9c0f-3ac4-af13-3da4c492601f | -3.50197 | -53.8159 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d405fe74-4f05-3ee1-ba55-f0943b8bd48c | -3.98771 | -49.92447 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91c0cfcb-1439-33ba-9a14-816695145901 | -4.12337 | -48.51439 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0a22367-4581-3582-a51b-24ae6dd8dc3b | -3.18055 | -48.44113 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 7327ab44-62fb-31ee-a2a0-aac74f0f503b | -5.81837 | -51.30189 | 2024-11-26 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b34d07af-56f3-3e5d-92e0-91ebd458a308 | -2.80665 | -53.02468 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1820029e-7e9c-31b0-b815-e6a27f0ce25e | -3.763 | -43.25454 | 2024-11-26 04:38:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 210a349b-68ed-3760-9f9e-66d7e43f3543 | -3.39331 | -44.75402 | 2024-11-26 04:38:00 | NPP-375D | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3d648890-0388-37e2-901f-0469adbfb6a1 | -3.04164 | -48.50737 | 2024-11-26 04:38:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b88e22e9-9a5c-35c2-b8db-df1c8fbf4de8 | -6.19263 | -44.42964 | 2024-11-26 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 96fadbf1-4ff2-321c-a70d-34a6502ab90b | -2.35939 | -48.56314 | 2024-11-26 04:38:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0efa9144-63c3-3fde-8520-08a077dd472f | -2.86215 | -51.57671 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 858325e9-d656-3cc7-a869-929077403af9 | -4.31753 | -47.51329 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a1de4970-54aa-366b-bd11-85e09c1b3ebf | -3.34534 | -50.51352 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfa2ebbd-e773-33ef-b751-b500e2f47355 | -3.91182 | -42.41263 | 2024-11-26 04:38:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| b829c34c-df85-392f-9016-2b68a1e7ebdf | -4.35693 | -48.57895 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 039b6f3c-7b2a-3bfb-81f1-34213ba840c9 | -4.65856 | -47.94778 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 261a7abd-ac9e-34cd-9426-b1c420a4adba | -4.258 | -48.66973 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eddfa3d9-0c07-3371-82b5-30edb100d719 | -4.04634 | -48.3138 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d66b1c1a-e149-35d9-879f-9c348e5889bd | -4.05088 | -46.84518 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9282bc6-46c7-3b22-88a6-bf5ed4508333 | -3.39296 | -44.17059 | 2024-11-26 04:38:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fd81e6c5-0705-3279-894a-e1494016b237 | -4.1151 | -48.52372 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed63a03a-bc7f-31c2-8ef6-808a93a23cf1 | -3.27335 | -48.98925 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fbf71b10-e978-3ff8-ace0-3b4a0549dbfc | -3.68245 | -49.63827 | 2024-11-26 04:38:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2e4f77f-2a32-359e-ae5f-8fd2b27c4944 | -3.30234 | -50.40853 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc126e37-46ca-3f6e-9969-dfc57639aa3b | -3.68153 | -50.22092 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13602833-21f5-3dd8-bfcd-472fe3e48512 | -3.1559 | -50.58263 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 048a7ebf-c7ce-3746-8e8d-01da0735ac15 | -3.07125 | -49.19917 | 2024-11-26 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c8d94de-803e-335a-945c-a0a47ca6deb6 | -3.22908 | -50.7787 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23f0bcf5-0b6a-3580-aec9-f68653c5392d | -3.94534 | -48.15948 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 878a9b13-23c8-3808-aaad-c3d4898580f2 | -3.32205 | -50.30667 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2435a8b7-4a30-3216-abe3-3c10d80b9031 | -1.21757 | -54.54101 | 2024-11-26 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7de13696-f227-3abf-976f-44dad116e1d3 | -4.35246 | -48.56407 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32b0e5e5-e942-3c20-a38a-39403eb3cd9f | -6.64283 | -47.34802 | 2024-11-26 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7459b8e3-bf6c-3bf5-80dc-8b823820d2aa | -2.71282 | -46.25788 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0dfde999-63d0-3525-9575-878ac2f516fe | -3.97499 | -48.05705 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 570085b0-d07c-3631-9293-1d22df2005ee | -3.96138 | -46.90812 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4ff7bdbd-5094-3b12-b53a-ef80b61b87a1 | -3.07269 | -50.94593 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cb898b1-a0b6-3521-9336-020dce8c0e06 | -3.95168 | -49.94819 | 2024-11-26 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 141ca672-7cd0-3421-8249-ed9192989d4b | -3.77026 | -46.6771 | 2024-11-26 04:38:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a8d197e-2426-375f-b9b0-7e51d9043afa | -3.28814 | -50.51966 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9bcfdfe-0d78-37c6-a32f-e3a7ad1ce894 | -3.33085 | -53.72004 | 2024-11-26 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cdaa240-3887-35bc-9281-00641f9c9701 | -3.2763 | -48.75994 | 2024-11-26 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3c0b2dd-1727-3ed1-a86c-601130e12e70 | -2.71677 | -46.28889 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af098c34-8a59-3b9c-bd44-aaa13d68b5c5 | -2.35598 | -53.71305 | 2024-11-26 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae445faa-fd10-3732-8e3d-0472469fcc4b | -3.05889 | -53.21949 | 2024-11-26 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f6b08f6-ed95-30f8-9ce8-9d0421f23ab3 | -3.99009 | -48.09157 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ff3af70-130c-35f7-b698-ff8032d2bc65 | -3.98397 | -48.08705 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e230b8f-4d4e-3425-9bb5-3be78d14083d | -2.69809 | -51.36559 | 2024-11-26 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2223b156-d20a-3424-bee7-82ed289919d9 | -1.28779 | -54.55676 | 2024-11-26 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a897ed54-3177-36e0-83cf-ad503b46e000 | -6.15619 | -46.8148 | 2024-11-26 04:38:00 | NPP-375D | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54d7793e-cd75-31c8-a021-b3954f9f41c9 | -2.6016 | -45.40353 | 2024-11-26 04:38:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53c00316-3182-38dd-a4e5-bbaaa36a8e8a | -4.54614 | -43.28854 | 2024-11-26 04:38:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d7088698-89d5-3cae-b008-cdda01bcac3e | -3.59318 | -50.38176 | 2024-11-26 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fb9ca2d-8f64-32ea-8d54-5d6bb30844d7 | -3.95909 | -46.90023 | 2024-11-26 04:38:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9475c546-f321-37e7-a0fa-f6f3f9b788ba | -4.11442 | -48.48464 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2665944e-6f03-32b5-a7da-266773cc16e2 | -3.97785 | -48.08253 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8f164164-e261-32b0-962f-545368645b02 | -2.32428 | -52.00294 | 2024-11-26 04:38:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db8ab859-3ec1-36de-89d5-a074df0a9d1b | -3.98009 | -48.09002 | 2024-11-26 04:38:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18fcd2e4-d72f-314d-9a7c-0fe2694be9cd | -2.98692 | -51.34707 | 2024-11-26 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e0e9cf4-0751-3075-8090-b3322cb07854 | -4.13001 | -48.51541 | 2024-11-26 04:38:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README28.md)
