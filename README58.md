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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c40d6369-9dd9-32b5-aa15-8f9289c21580 | -9.74649 | -67.69766 | 2025-08-28 04:59:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fa54d27-fe95-3ac2-9151-953309f7a195 | -10.26222 | -64.50013 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b5bab12-a11f-333e-a8c4-8b2f9ac1b5bb | -9.12432 | -65.76876 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b3d62109-3244-3c2a-bd30-84915f74f58a | -15.6734 | -52.74154 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 915f837c-5293-31d0-9abc-bb03b357a9cf | -12.44146 | -48.70982 | 2025-08-28 04:59:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f369fa82-20b4-30b1-8a47-5632427dbacd | -13.53104 | -46.93167 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c6c63ec-6e99-376e-bb8d-87a5fc3e8ed3 | -9.5427 | -68.58147 | 2025-08-28 04:59:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4da9bc2b-f8f8-3f38-ab89-c3f1010b9d49 | -12.79203 | -48.1445 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 44e9dd61-e027-3658-8089-9221d1199ef4 | -11.33331 | -43.533 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f24a23f-e9ac-3bb6-8fe2-0dc65975de5e | -9.20238 | -59.64528 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aacb8f6c-59ef-32e6-a97b-a75b1be75899 | -11.57361 | -46.38622 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 68cc265a-ab9d-3802-a250-a5326e880502 | -9.19143 | -60.79788 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70248de8-df88-3af3-807d-08ddde3399e6 | -9.54479 | -62.39881 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 36546669-ab7d-3e6d-b0e2-41c0b8169bf7 | -9.80088 | -64.26997 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c9858d2-3863-394f-a684-71714ea6adcb | -10.47132 | -57.95825 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 857b6a72-b5da-3fb0-9d57-4f7ef2b8a725 | -13.42824 | -46.85334 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71697fb6-4a7d-39ac-968d-b1dc95d00339 | -12.81245 | -48.13711 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4a092efe-9564-3bf1-b866-0cbea98da341 | -10.81548 | -60.76803 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 93c11c15-f6ac-3b90-bca1-98112cc39239 | -9.01284 | -65.69745 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f74d8d9a-a88c-3cb8-8f82-75817b76c88c | -9.31552 | -57.70109 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b4a9e6c8-f040-385d-8d6b-1726bd67dc50 | -8.94822 | -65.96629 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3a18ff24-0433-34cc-8d8e-c8f8e156bb1e | -14.26103 | -53.06278 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f58267a-ba27-309b-91e7-552fd24731fe | -13.63221 | -48.24444 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a0bed4f-28ca-33a6-8d5d-00d3b35b6a0e | -10.60808 | -52.32843 | 2025-08-28 04:59:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a6d852cb-cd59-3d69-8f70-59711f32eb2a | -13.38796 | -51.753 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e245f2f-4020-3115-be85-d268f7d4fd33 | -9.1552 | -59.59132 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99cfa4c1-9266-3a0a-8a1b-8f1ce93d0760 | -12.80093 | -48.15133 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 805adf17-e40e-3e7e-b89a-525dc41d044c | -13.08429 | -46.34519 | 2025-08-28 04:59:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8c746a7-e507-3169-9dd4-c41bef36acfa | -13.4417 | -46.96272 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bc8541c-c3b1-32e1-9b59-bb2625b1cafd | -15.0795 | -48.63856 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9462220d-cc0b-3d7b-b68e-b221a0c22bb9 | -9.80822 | -61.199 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a2f6bc5-4233-32b7-b599-9d512b73e4c4 | -11.33644 | -43.53024 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ffbc1c8-5ed5-3d99-944b-2ecfca0d7302 | -9.41233 | -60.53034 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36b12550-70ff-3477-9391-c29bda7ddcd7 | -14.33537 | -51.91089 | 2025-08-28 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb528310-451d-3c81-8f1e-8d3f1eb7ecac | -11.24697 | -45.00397 | 2025-08-28 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77806a4b-3ed7-349a-b1bd-482c90f243f9 | -13.46106 | -46.98323 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9177e56e-fd42-3fec-9932-3775a73c3d1a | -13.54896 | -46.91594 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e71279d5-e9a7-3214-95e4-fddf0265693a | -10.31862 | -62.61834 | 2025-08-28 04:59:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9b8b5e37-f6a3-30e9-9e30-386f1ccbe0a3 | -13.14165 | -54.92249 | 2025-08-28 04:59:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd95dfce-e140-3e82-b628-3df2b5ab6233 | -12.12221 | -55.19012 | 2025-08-28 04:59:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 662a9418-1501-3fdf-b6b3-0ed48a2a61ca | -10.31774 | -62.62333 | 2025-08-28 04:59:00 | NOAA-21 | THEOBROMA | RONDÔNIA | Brasil | 1101609 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 580f3567-72d3-3b16-bba0-5865348942fb | -13.43417 | -46.98074 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2e0c2ded-40c4-3f48-a5d2-212559b93d79 | -8.95589 | -65.97411 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8eb90bc9-7da1-30d5-a445-13c35d772046 | -9.15948 | -59.56617 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1090a88d-0749-38c8-bfaa-239420d86612 | -8.93973 | -65.94643 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 516ca0e4-3ce9-38aa-b058-50158628be6a | -9.41038 | -60.54156 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6264183b-ecd3-3ec2-a970-bada60e2416f | -9.55129 | -65.69983 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43f94778-a56f-3027-835e-0c05f57610db | -9.40606 | -60.51764 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95ff8410-2397-37c1-8dbb-b30c16589bab | -12.89336 | -48.11537 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| d506f18b-0378-3ba7-acfc-1c6051ab0844 | -13.41776 | -46.85137 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3cdab6ca-86fd-316c-87fc-f1661379c113 | -9.13283 | -65.78791 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 191edf10-7b24-3d35-84de-fdeb9ef5f2c1 | -10.79716 | -60.77627 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 57d59d76-df0e-3a8f-ad71-8194b200b843 | -13.43387 | -46.85112 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19900cd4-1cb2-39aa-8536-e568b506edbd | -9.0136 | -65.69328 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9dbbe2d1-c663-31d3-996a-6b3dbf186590 | -13.37771 | -51.77122 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15b1d1c0-ea43-3919-9da2-9a22bd54082e | -9.22087 | -60.80325 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2e2c732-70fb-389c-876c-4146b4b292ce | -9.40926 | -60.57243 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6f4bb394-475c-34bb-9ef5-77b10575305e | -8.93464 | -65.94091 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cac03b74-d786-3e74-911d-3f11bf86761c | -13.34797 | -51.79409 | 2025-08-28 04:59:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b02f81f4-baeb-330e-bda8-440cb251673c | -9.52531 | -60.53116 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bc09345-6cd1-388c-bd31-b748eccce243 | -14.27395 | -53.0629 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 3f571c49-f63a-3a3d-bae4-17fb499547e6 | -12.67991 | -48.17989 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c34c80d-630a-3968-ad7d-cc09290b4266 | -9.08842 | -65.74139 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.0 |
| ef1885b0-9feb-3757-9a63-6665212d915f | -9.06797 | -66.06466 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bcf08ec2-b4b6-3ee5-bad8-e01a5e21d7cf | -9.13609 | -65.77068 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0fa253b7-1035-3576-8b8c-c08898178bf4 | -9.15147 | -62.35865 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0c961832-6189-3d5c-af17-8fa7967ad4c0 | -13.61797 | -48.24063 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bbc72e72-02d9-3140-beda-bd423c3cb723 | -12.52151 | -53.81904 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2eb19fab-26c8-3b94-9ca3-f217ce570870 | -10.32534 | -62.62189 | 2025-08-28 04:59:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 91c772e8-fd76-3bda-a85a-600f8ee83b86 | -10.88486 | -55.77349 | 2025-08-28 04:59:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fca24f93-5e60-3e52-b40d-5b693a30228a | -11.22467 | -55.05737 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aeb797e9-b428-37e3-87fa-19d69e5d79c4 | -9.15555 | -60.77966 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb0eeebf-1646-34af-8336-2bb5c94b2629 | -9.41339 | -60.57313 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 4210dc88-4ab7-3b7e-be19-007158264c1a | -13.49737 | -46.85498 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c620508c-6b00-3aeb-bf22-8cff31494520 | -11.92419 | -46.70391 | 2025-08-28 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4a3cb15b-7ad8-3f17-8ffd-b56f2b90168e | -12.86496 | -48.10806 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15dda741-18f1-3056-9e86-b002ab045c11 | -14.32872 | -53.26766 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81530af8-84bf-3a7d-a405-58b0cec78a42 | -11.65262 | -44.87637 | 2025-08-28 04:59:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5f6130d-9af4-3047-830e-250a5bbd6b21 | -13.46061 | -46.98708 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9168c172-549d-31b7-8760-6cf1156e20ff | -9.47285 | -62.38237 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18d99947-b451-34fe-98aa-b1f8e6cbe57b | -12.89369 | -48.11068 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 03088a91-7871-38e0-87dc-c90c05be6e67 | -11.33268 | -43.53823 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9884e81f-6f66-3f00-8f00-4501831e1fd8 | -14.51633 | -53.08852 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14c134ce-8e8e-3031-a33b-551afe8af858 | -9.31684 | -57.69317 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1a43f6f4-6e26-3db6-99d4-2be868bfccbf | -13.42231 | -46.99087 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2eb1a5f2-6b42-311d-b8a4-f0dc7ae487a7 | -11.579 | -46.38617 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e22045d-d9a5-33ca-b3fe-f991b5a2796c | -13.83148 | -46.68497 | 2025-08-28 04:59:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f325eb1-1486-3e36-8069-aafc9e103ad0 | -9.1302 | -65.76973 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 42bf7be2-73d2-3d49-97d1-340a55f25674 | -15.62388 | -52.75507 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0b98186-e53a-3cfc-b532-9df022dc41da | -10.47265 | -57.9503 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2af893d0-3d04-3e99-81ca-3449faa3d538 | -11.3283 | -43.5452 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b318382a-90f2-3aaf-8782-1bc2c1ecc229 | -9.13203 | -65.79211 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6172e9b5-cbc5-3c24-b57f-3c99f7338ffc | -9.57211 | -55.38205 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 75bb6f6c-be72-357d-8049-9e859cf8770c | -10.48252 | -57.95604 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6a14a10f-da9b-3763-9efd-8036c3310a46 | -11.837 | -46.80136 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1db110c-d53d-3954-92f9-fea0115fae65 | -9.19865 | -59.54756 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f30966dd-96b1-3657-9f2c-30b891004527 | -9.41646 | -60.53104 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3972246b-9efc-341b-a08c-d99d32f09b80 | -9.56164 | -55.38396 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| daf8bbcb-0935-33ba-bd60-b9f81ca0076b | -8.3493 | -62.93453 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12230f7b-63b2-3fab-8db7-b4d62b6f60e5 | -12.89497 | -48.10021 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README59.md)
