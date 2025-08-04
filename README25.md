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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3a5142f-c256-36ec-81e8-2d7284583675 | -12.69546 | -48.0814 | 2025-08-04 05:31:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| d61be398-d16c-3895-bf13-4e0d009681e4 | -22.5625 | -42.15256 | 2025-08-04 05:33:00 | AQUA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 4a2ac467-6b3c-3995-b317-5a01de9665e2 | -22.56103 | -42.16381 | 2025-08-04 05:33:00 | AQUA_M-M | CABO FRIO | RIO DE JANEIRO | Brasil | 3300704 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 6e281f19-156b-3f06-98e0-741d4bc0815c | -7.994 | -43.1534 | 2025-08-04 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 2215084d-b8d4-3806-ac9a-cc9a55d6240b | -8.0132 | -43.1278 | 2025-08-04 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.3 |
| 35e72026-d350-3cae-bec0-7653747c0362 | -8.0129 | -43.1513 | 2025-08-04 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| fbf2fef9-2680-3205-a50d-d4f3ed72214b | -7.994 | -43.1534 | 2025-08-04 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| be694a9f-cf0a-3c25-98c7-5084cc759121 | -8.0132 | -43.1278 | 2025-08-04 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.0 |
| 355aa85e-ff2a-3a30-b407-e73fe36cd62e | -8.0129 | -43.1513 | 2025-08-04 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 122.7 |
| 99f7a2a4-b714-3fe9-924a-5008ce22a54e | -6.65229 | -59.10082 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 39a8e420-8b4f-3f51-8f03-337e60f3d759 | -9.46649 | -57.83762 | 2025-08-04 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 798271f2-74bc-32c3-b8ec-031310cd064c | -6.67334 | -59.16686 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4f78e9df-2f54-3239-8f9c-8508fac25bbe | -6.67907 | -59.16183 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 657ac622-d976-3721-9e5f-cd50a3b7dad1 | -8.74478 | -69.37501 | 2025-08-04 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c09396b2-11c2-3ff8-861d-8a83fb82381c | -7.0147 | -59.83746 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c8bc5847-d491-3263-ae14-5e14e48151a6 | -6.61989 | -59.95401 | 2025-08-04 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d38b74c-ee45-36e6-92a3-b5866ba06159 | -6.62171 | -59.97411 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| beeb83ff-dbf4-3e1e-b01d-aa15969d7eaf | -6.62313 | -59.96438 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c8305a8-b841-34e4-8be6-efac9bc63b1c | -12.38222 | -63.67345 | 2025-08-04 05:50:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3119550d-9d1d-3bab-80f2-f3a998c8d988 | -6.62454 | -59.95469 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f0047496-3692-3d59-9c77-7544f0ff4ca9 | -7.02012 | -59.83315 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a6be957c-70b9-3cc1-98c4-0e7ee54dd9df | -7.02083 | -59.8281 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6589bd87-570f-35f6-9b77-af7d4280f87b | -8.73398 | -69.37704 | 2025-08-04 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ace1a8e0-90be-3ade-b403-bd01fda2bf60 | -6.62052 | -59.97157 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98a8865f-38bf-3809-b376-b143ee885dcc | -9.46699 | -57.83381 | 2025-08-04 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60d5e887-ea44-3492-b5fd-b7eca282b850 | -7.01541 | -59.83242 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 62b2bc24-d7b2-348a-aaf6-ba698719ffcb | -9.46453 | -57.83932 | 2025-08-04 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fd61a4f-4ca7-37c4-b55f-6d60b16957b9 | -6.62242 | -59.96925 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4f12e7c8-4d16-3516-a7a0-fd89e53c0f07 | -7.02555 | -59.82881 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f705aec-7dd5-3268-97bd-ea3e0a237816 | -6.62638 | -59.97466 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 0f5d687b-db73-3614-bce1-c60efdb79a3b | -6.61918 | -59.95886 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0beba61d-6c1d-3e3c-b38b-60355f16cb88 | -7.52008 | -61.32294 | 2025-08-04 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f842c8f-f79c-3356-ac4d-4ff3fb36f096 | -6.62252 | -59.95696 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93145ffc-8806-3985-a0ae-a0dbaeb0a1a6 | -6.61721 | -59.96108 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ca02abc-2258-3f21-9eca-1a36aae2722b | -6.62186 | -59.96182 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 602f55b8-7e64-3790-86ca-d2378b6875a4 | -6.64043 | -59.99894 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a211df90-226c-3ec4-a623-f92bf772b8a6 | -6.61855 | -59.95133 | 2025-08-04 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1d7632ee-2f84-33bc-829c-731652f36f23 | -7.03028 | -59.82948 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 51db83cd-2319-3701-b538-115509a44e1d | -9.465 | -57.83554 | 2025-08-04 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bcda056e-97ff-3c69-a1b9-449e5d9c9b88 | -6.62384 | -59.95953 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 692fe6f4-42e2-3567-8742-c6c9de3b2429 | -6.62061 | -59.94906 | 2025-08-04 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| da6ccf87-35ef-3e1d-9004-c06f3644633a | -7.31907 | -59.62023 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5d25ebe-3a54-3315-9f52-7e6916d2afcb | -6.62709 | -59.96983 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 50166224-1a9b-3480-93be-be166de1bfd4 | -7.31885 | -59.61711 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccde5c47-a6fe-3efd-9cbb-dff55af4d91b | -6.62119 | -59.96669 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35885a66-da84-39af-b646-8b32fdefa933 | -6.67826 | -59.16762 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c411b499-4644-3890-8ced-319ec6bd2fa7 | -7.03219 | -59.85 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00fdbc74-90d9-3a61-9150-ddc31659169a | -9.98569 | -67.57373 | 2025-08-04 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 085da32f-03d3-34e8-a677-82b842f05cee | -6.62984 | -59.97274 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bd600213-4c04-3847-ba39-aecef3b99876 | -7.00999 | -59.83669 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 35fb8f5e-867f-3faa-90fc-641f50382549 | -6.63051 | -59.96789 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| facae638-1b7f-3c6c-b231-b5863c2f57e0 | -7.01942 | -59.83815 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5ba617fa-99f1-33c3-91bf-e1cf1ec726c7 | -6.65073 | -59.11225 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 408efe54-14c5-3de3-ae70-39cffb1bb1c0 | -6.62451 | -59.97701 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 47786ef3-7e1f-346b-93d1-426fd20bfe14 | -6.62652 | -59.96243 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ef1d3a0-cf40-3408-8031-3cfff987e1e4 | -6.82694 | -59.26511 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 98fe8295-7090-318b-b870-703d65b1c705 | -6.62518 | -59.97216 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 97b789b4-c8f3-3edb-92f9-d090f97d4a93 | -7.01139 | -59.82664 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4578bbb3-e18b-374c-ab06-1135a25582bb | -7.01611 | -59.82737 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8cf85380-ec1d-3944-be29-bd8f9aba3a9f | -9.46089 | -57.83682 | 2025-08-04 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f32b2b7e-5e51-3104-9ff0-cecdead590ac | -6.62585 | -59.96729 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| a54b66ce-8815-3a9f-ad79-ac3eaacc3422 | -6.81639 | -59.26899 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4896abd2-2c00-3957-b919-0319e2daa35a | -12.05037 | -63.56011 | 2025-08-04 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a84ef840-738a-3d94-bbf5-e2c4836f6ea2 | -7.01069 | -59.83166 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01a88793-2b3c-37ef-ba2d-f5b26b37e4d7 | -11.40963 | -54.71898 | 2025-08-04 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d58bd861-33ec-34bc-b3ec-c1bfc325e70a | -7.0362 | -59.8557 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7217ac2c-c559-327c-bc7d-d93690dde280 | -6.6232 | -59.95205 | 2025-08-04 05:50:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2357155a-54f3-3e7b-a5d3-68575ab09cff | -7.02485 | -59.83381 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| adb220e8-f49d-3433-b216-082c19333ebd | -7.03149 | -59.85496 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b930bc88-d598-362b-8741-d17d48c3d28c | -6.65151 | -59.10656 | 2025-08-04 05:50:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 370736c0-3a90-345a-870e-b28ac5052024 | -12.05001 | -63.5569 | 2025-08-04 05:50:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18a8840f-a090-3e9a-9bca-e89a53e5dbb7 | -6.61787 | -59.95625 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fcc3964-944e-3b04-842e-73fe5b4ab023 | -6.62779 | -59.96497 | 2025-08-04 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b46b4da-34d5-3dba-9d7f-7d095ebd6ba4 | -10.7492 | -60.7097 | 2025-08-04 06:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| d16c5033-4fd1-309c-8bc2-d50d970f9810 | -8.0132 | -43.1278 | 2025-08-04 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| c2de6c52-8352-358d-8d9f-2bda0a0330f4 | -8.0129 | -43.1513 | 2025-08-04 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 62a31a05-4508-3dc7-a0c9-15b2eb7b3b77 | -7.994 | -43.1534 | 2025-08-04 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 687ad350-c272-3640-806a-290e06b2d825 | -6.6507 | -59.11563 | 2025-08-04 06:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6e4070f2-84f7-3189-81b9-2c39f734f053 | -7.01218 | -59.83716 | 2025-08-04 06:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5b6af15d-0651-3ceb-b66b-8446cab0da6e | -6.65268 | -59.1003 | 2025-08-04 06:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 00598384-2139-36b9-bdc5-1118a5ac2d07 | -7.01306 | -59.83047 | 2025-08-04 06:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1df0289e-8373-3c3c-bd89-ab19d8f732fc | -7.02007 | -59.83158 | 2025-08-04 06:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8a7e41a7-260d-3e42-8927-ea15914b9cc1 | -6.62183 | -59.97676 | 2025-08-04 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c57ebe66-ccb8-30bb-b960-cf635e0a8265 | -6.64973 | -59.1135 | 2025-08-04 06:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1a1d4c2d-77a6-35c4-a372-50c8663bc322 | -6.62965 | -59.97095 | 2025-08-04 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6ad7da83-0847-3285-bfb6-26e328dbfdae | -6.62266 | -59.97035 | 2025-08-04 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e6f0fb4-fb8d-38c3-b5fe-4cabee553a07 | -6.62318 | -59.9774 | 2025-08-04 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d50903b-8f4e-3a43-8611-f0f3b96c1ce7 | -9.98678 | -67.5728 | 2025-08-04 06:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9ad2945-576f-3024-9448-1d9d1889cf99 | -6.65077 | -59.10585 | 2025-08-04 06:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a647a1d8-77b0-39fb-ae36-bab564fda129 | -7.0192 | -59.83818 | 2025-08-04 06:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 87cdf2bf-9a33-3b67-8947-61dec52dc4b3 | -6.65167 | -59.10812 | 2025-08-04 06:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f03da201-1165-3797-b247-4537ebdb1cfe | -9.98618 | -67.5772 | 2025-08-04 06:16:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 609cdcad-6488-375c-be56-f63b1330eb69 | -6.62883 | -59.9773 | 2025-08-04 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 53e2e6c5-62b9-31d6-a3c8-1cb40afb460d | -6.62405 | -59.97101 | 2025-08-04 06:16:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4622919c-b746-3032-878a-7a008a0c8cdf | -8.0129 | -43.1513 | 2025-08-04 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 3aa14a53-6b51-320a-993c-bf8b8e702c7e | -8.0132 | -43.1278 | 2025-08-04 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.4 |
| 02286349-9020-3dd6-972e-b02698c6f915 | -7.994 | -43.1534 | 2025-08-04 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.8 |
| 5e1e4bf4-9412-31bd-a14c-4d0f36a53b7d | -7.994 | -43.1534 | 2025-08-04 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.9 |
| ed55d134-7659-3d0f-8c2c-e0697ad3ccd9 | -8.0129 | -43.1513 | 2025-08-04 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| e7bebbba-b0a6-3fcc-a08d-842a8f093cc4 | -8.0132 | -43.1278 | 2025-08-04 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.9 |


[Clique aqui para ver as próximas entradas](README26.md)
