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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 83ea9873-7ad7-3eb4-8859-4d58f816db72 | -9.518 | -60.5268 | 2025-08-17 06:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ad78155b-c059-3e85-b818-2d56618f0e60 | -14.9819 | -54.7536 | 2025-08-17 06:10:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 32cb69ab-9f90-337f-95ba-2638821c9759 | -8.9788 | -60.4964 | 2025-08-17 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 26408871-6e67-3979-80e7-dab618b9b369 | -8.88345 | -68.51419 | 2025-08-17 06:46:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e3de1a6-663d-30ba-8053-908c279e2272 | -8.88267 | -68.52058 | 2025-08-17 06:46:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ec4052a-09f5-347a-97d8-990b3c3e379a | -8.87728 | -68.50682 | 2025-08-17 06:46:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 597b5b42-7b7b-3ca0-957b-9219072aff63 | -8.87032 | -68.50598 | 2025-08-17 06:46:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93fbf25a-6e13-37f4-aa99-062ebc057212 | -8.87651 | -68.51321 | 2025-08-17 06:46:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6c971fe3-11a7-3ef5-8df3-904dbbdcfe77 | -8.02957 | -72.50074 | 2025-08-17 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fdcbaae0-0c80-3579-b62d-ff07fa56ae06 | -8.02913 | -72.50411 | 2025-08-17 06:46:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 505e68a8-08fd-36b6-9df1-fdf4a1cdcab1 | -7.9252 | -63.2608 | 2025-08-17 06:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 5545c6f8-e453-38b9-aefd-fbf6a1325dbb | -7.9068 | -63.2615 | 2025-08-17 06:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 607990ae-b5ec-353b-9c5a-f7c0aea85393 | -7.9252 | -63.2608 | 2025-08-17 07:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 24037574-05f5-3472-acea-8ef8e7696121 | -7.9068 | -63.2615 | 2025-08-17 07:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 9db21e55-7fba-3338-91e2-859547074ac2 | 0.97354 | -60.40767 | 2025-08-17 07:18:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 260fdf17-676e-36fd-a8b3-c06762814e35 | -8.87393 | -68.51404 | 2025-08-17 07:22:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4ac84a8f-76dc-31cf-9959-15f003294ea0 | -8.97784 | -60.485 | 2025-08-17 07:22:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 6af43608-c716-3464-834b-57cbd275be74 | -8.87525 | -68.50508 | 2025-08-17 07:22:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c269b209-9c30-3c33-a437-138d4049e544 | -9.50259 | -60.5234 | 2025-08-17 07:22:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 41c63e65-6c8b-3d73-b62d-4f3148ab3473 | -9.55353 | -63.66059 | 2025-08-17 07:22:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 85fe28ef-fd63-3899-a863-5f5fd7424f4a | -9.50789 | -60.5164 | 2025-08-17 07:22:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.3 |
| d1a37fb9-d397-3df4-b86d-a3ebab12d614 | -8.96821 | -61.67226 | 2025-08-17 07:22:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 23.6 |
| df74be8a-92d5-34d0-8111-019d9d2d96cf | -8.88278 | -68.51535 | 2025-08-17 07:22:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d977dfce-717e-355d-98a4-8fb1ecb1bf1e | -8.96446 | -61.66447 | 2025-08-17 07:22:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 3714c8df-2e5c-376e-902f-6380e6d0cf22 | -9.5039 | -60.54744 | 2025-08-17 07:22:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 818d9b6d-4187-342e-a1ea-9ecbffac5759 | -13.4514 | -57.0793 | 2025-08-17 07:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| cb9e3582-8df6-3930-87e4-3a1d20ec86a5 | -9.5531 | -63.6709 | 2025-08-17 07:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 747523fd-242d-3ecb-8f16-945256df094e | -13.4511 | -57.0995 | 2025-08-17 08:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 69e7640a-8bd6-386b-b7f3-fb3185cd8a57 | -13.4514 | -57.0793 | 2025-08-17 08:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| f79f769f-a746-3f49-addf-d7b6a6f804a1 | -9.5531 | -63.6709 | 2025-08-17 08:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 72df1508-b536-3a70-a2d7-b860a095ee7d | -13.4514 | -57.0793 | 2025-08-17 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.9 |
| edd756e1-2dcc-38ea-bf2e-6d35aacaced4 | -13.4511 | -57.0995 | 2025-08-17 08:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5991e993-d47e-37d6-b47d-a9ef20c83d90 | -9.5531 | -63.6709 | 2025-08-17 08:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 3da4de1f-f290-3a26-b5a3-617b82c02b26 | -9.5531 | -63.6709 | 2025-08-17 08:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 410a62cc-dec0-3586-897d-d975571b8487 | -13.8942 | -45.5378 | 2025-08-17 11:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 92c65e6a-a990-378a-9907-6a1e9bd35aa9 | -13.8942 | -45.5378 | 2025-08-17 11:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 1b48f4ce-e8b1-3c5a-bac4-ff66990b10d9 | -13.8942 | -45.5378 | 2025-08-17 11:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 4bcbd9eb-f4f8-39f7-8b41-4108efe959fe | -13.8748 | -45.5411 | 2025-08-17 11:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.4 |
| f7c402b2-ee53-3e9e-8e68-e0d4c7999171 | -5.6784 | -43.3892 | 2025-08-17 11:50:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 4538b01c-22c2-3513-9285-d106d979c6ab | -14.1897 | -45.3241 | 2025-08-17 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 117.8 |
| d4b9f563-0dc0-3914-8bde-52c4bf9b7631 | -15.8602 | -50.204 | 2025-08-17 11:50:00 | GOES-19 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 6bfc1d05-c348-3a2b-8ff2-269beb37b8be | -13.8748 | -45.5411 | 2025-08-17 11:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| b2c16bc9-fa39-35c9-a326-c7f604382acf | -7.48778 | -39.96438 | 2025-08-17 11:53:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| da317c1f-d350-3126-9a8e-e0c000a08b52 | -9.61034 | -40.3969 | 2025-08-17 11:53:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 69a2f428-2070-3caa-886f-b788676f1bce | -8.04368 | -47.67059 | 2025-08-17 11:53:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 28.9 |
| dcd6ed94-71de-359e-9ce1-f853b41cbf1a | -7.02625 | -42.11799 | 2025-08-17 11:53:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 9013452e-2ada-368a-980d-e0bbb76fbeed | -7.6596 | -43.84832 | 2025-08-17 11:53:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 7e2e0a08-571a-3b6a-8339-09c9264082e3 | -7.65782 | -43.85992 | 2025-08-17 11:53:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| b5845c52-1b45-3ebc-8625-054a44ccb387 | -6.48723 | -45.45938 | 2025-08-17 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| dbdd90b3-7b86-3fab-b25d-d46c4dd29f7c | -6.55293 | -43.02082 | 2025-08-17 11:53:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| d54d3d99-647b-36ae-939a-4b2b51d46a10 | -7.60363 | -44.94894 | 2025-08-17 11:53:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c51ab7f8-a942-3efd-b114-a7f07898197b | -8.52302 | -47.20951 | 2025-08-17 11:53:00 | TERRA_M-M | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| df791e02-35d0-3920-a93e-b5c9ee05a828 | -7.14374 | -44.62951 | 2025-08-17 11:53:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 7f0070de-6a06-3942-b78e-455ee58e7a08 | -6.55134 | -43.03159 | 2025-08-17 11:53:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 40847c54-b116-3a1b-9c19-29e0aabd9898 | -7.60585 | -44.93456 | 2025-08-17 11:53:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 8423ab10-bd41-3d0a-a355-1663e0bbe5bc | -7.82138 | -38.77621 | 2025-08-17 11:53:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 99d85909-81f1-38d0-883b-f98f4436bc7a | -7.1417 | -44.64309 | 2025-08-17 11:53:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 53733d59-5723-3795-8ae5-4edb7733c1d0 | -6.62164 | -43.87567 | 2025-08-17 11:53:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c79a851d-799d-388d-b1b2-2a48b99f2025 | -5.6812 | -43.37522 | 2025-08-17 11:53:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 243ff87e-c657-33ce-8c8f-2f6eaab4081f | -6.19145 | -45.42968 | 2025-08-17 11:53:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 88645f4b-af21-353c-98f1-bea68f15c2d0 | -6.50212 | -45.59469 | 2025-08-17 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 0acc4252-7c2a-3c23-81a4-f270533ef553 | -4.60505 | -43.30586 | 2025-08-17 11:53:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 1c58082a-2f1b-3936-8663-7d3bdc68cd62 | -6.43398 | -42.50916 | 2025-08-17 11:53:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3b6f024b-8fd4-3481-9aca-1f4b869926f2 | -6.95358 | -41.73312 | 2025-08-17 11:53:00 | TERRA_M-M | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| aa4386f0-2ba7-3b72-b6e6-82b13fd4f6e2 | -7.48905 | -39.95551 | 2025-08-17 11:53:00 | TERRA_M-M | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 17.9 |
| d7390782-c31a-3686-8fb7-202911485680 | -6.19341 | -45.43974 | 2025-08-17 11:53:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 63441838-0169-327c-931c-9f0ffac11988 | -4.60326 | -43.31777 | 2025-08-17 11:53:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fe75740b-e251-3452-ade2-d1c685a14d7b | -7.85763 | -38.70883 | 2025-08-17 11:53:00 | TERRA_M-M | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| cabc7eec-64bf-37f7-b567-3de047dd38aa | -5.6801 | -43.38129 | 2025-08-17 11:53:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 59492132-0bae-3dce-9658-9055d2d9d056 | -6.49032 | -45.5932 | 2025-08-17 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| e2a8ae1e-e8fe-391d-b102-9cbd4b9f54e2 | -5.67833 | -43.39291 | 2025-08-17 11:53:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| c7c4eabb-59e5-3f07-9aba-2bdd1032f456 | -9.3164 | -41.09544 | 2025-08-17 11:53:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c5446095-7584-3ed6-bc34-64fe6cbb63cd | -9.02088 | -38.35284 | 2025-08-17 11:53:00 | TERRA_M-M | GLÓRIA | BAHIA | Brasil | 2911402 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 34e9a472-c494-335d-b074-a0cfb874a86b | -7.14683 | -44.63607 | 2025-08-17 11:53:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 11a2a5a0-b47c-3fca-b1a7-ac02fb3d1cc2 | -3.97223 | -42.53766 | 2025-08-17 11:53:00 | TERRA_M-M | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 21d004f4-1a1f-3370-a9eb-c78692a332bd | -9.15795 | -40.08245 | 2025-08-17 11:53:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| eb079632-d214-39c4-918e-a9e6c955af2a | -6.61832 | -43.88175 | 2025-08-17 11:53:00 | TERRA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 18928987-2d7d-3163-8be0-daaab46ffbfd | -6.8079 | -43.03378 | 2025-08-17 11:53:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 91927c49-068a-3533-8eda-150ba4c8e23b | -6.4897 | -45.44357 | 2025-08-17 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 8225d06b-f45e-3bbf-b0ce-e90a0d2c1f64 | -6.08616 | -44.62649 | 2025-08-17 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d0ece3bb-c48b-3861-b280-4da905d716ad | -3.97385 | -42.52679 | 2025-08-17 11:53:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 35.3 |
| 924f1c28-91cd-3b9c-bde1-fdc45d609050 | -5.67949 | -43.38687 | 2025-08-17 11:53:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| 04fb21a5-ee16-3c86-9bf7-f69032bd1958 | -8.20593 | -44.94175 | 2025-08-17 11:53:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cb98217c-c619-38e6-a0ab-d33f8a1d1883 | -6.33827 | -44.71159 | 2025-08-17 11:53:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5b1f6d45-538a-3ddb-82f4-edba5a8d7ca5 | -7.02482 | -42.12769 | 2025-08-17 11:53:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| ef7e0544-743b-330a-81b4-64dffc5a2fa5 | -9.21318 | -39.49529 | 2025-08-17 11:53:00 | TERRA_M-M | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| b8fbd471-ac05-35a0-8e06-a0c12a316ce6 | -3.98359 | -42.52816 | 2025-08-17 11:53:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 20b447d9-5005-3e9d-a798-e0bf348e242b | -9.15668 | -40.09143 | 2025-08-17 11:53:00 | TERRA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 4a8fa37a-0a7b-3da2-9192-4dd4c5a72147 | -7.14468 | -44.64976 | 2025-08-17 11:53:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c97e92b2-e49c-3b01-8e6e-4ddce1f0ecd8 | -12.63069 | -46.8965 | 2025-08-17 11:55:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 413afaf2-0127-3550-a758-dadaff0167e7 | -9.76908 | -41.91497 | 2025-08-17 11:55:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 91532568-fd56-3988-989b-ce59da58e69e | -12.14212 | -47.92683 | 2025-08-17 11:55:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 2b30c6be-e581-325c-b7da-b1346fbfb584 | -12.62796 | -46.91294 | 2025-08-17 11:55:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 31.7 |
| c191da3d-f6f8-36d8-9166-38a94f1b180f | -9.95558 | -42.40648 | 2025-08-17 11:55:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ba7b0e64-5ade-316d-87f6-c37b33e8b17d | -12.82236 | -45.99764 | 2025-08-17 11:55:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 42ccb9a9-d231-36ff-9984-eb22c057cd0b | -10.99349 | -43.17716 | 2025-08-17 11:55:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a8879f2d-b3a6-3939-8a00-ae67e9d6e208 | -12.14272 | -47.92057 | 2025-08-17 11:55:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 81c741b5-96c0-3c66-91db-c4973566ac0b | -10.82894 | -45.31898 | 2025-08-17 11:55:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6b97bbf3-50f5-3644-b3a4-eddf4082c58b | -9.95697 | -42.39704 | 2025-08-17 11:55:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ca561843-ef42-3e13-99a8-d773e5b5b0ec | -10.8348 | -45.31287 | 2025-08-17 11:55:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |


[Clique aqui para ver as próximas entradas](README41.md)
