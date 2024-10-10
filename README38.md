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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c3442ee-c38e-32c7-a424-fae508f35155 | -9.0656 | -61.3934 | 2024-10-10 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 290c3e88-01d6-3140-aa5e-59a2a3d980d8 | -9.0841 | -61.4117 | 2024-10-10 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| f4628534-f9ad-362c-ab5a-748205493a37 | -9.0842 | -61.3925 | 2024-10-10 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 42b9ee27-6a81-31b3-b0cf-cbfc305dea41 | -9.1035 | -61.2769 | 2024-10-10 03:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5aef25c1-378d-3929-b685-82e3da4d4a0a | -9.122 | -61.2951 | 2024-10-10 03:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 112.5 |
| eca5951e-77cf-334c-b617-e89f04d98aee | -9.1221 | -61.276 | 2024-10-10 03:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 243.5 |
| 8dc989ad-5879-3b81-a111-72c3fe1e6a2a | -9.1223 | -61.2569 | 2024-10-10 03:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1823b91f-6280-3449-8b15-d7806c853576 | -10.6832 | -51.0907 | 2024-10-10 03:06:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| fd27daf7-3f28-3790-ab2d-bf17bd0ee5f9 | -12.3065 | -59.1838 | 2024-10-10 03:06:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 8597b9f6-d66c-30bc-9f2c-68e81f82d270 | -12.3067 | -59.1641 | 2024-10-10 03:06:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| ca4d4a3c-a30f-345a-bedf-4480ce805dcd | -12.9447 | -51.1337 | 2024-10-10 03:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 513e2162-ac41-33ae-ad80-44b48bb0eb5d | -12.973 | -46.216 | 2024-10-10 03:06:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| d0d93a1b-564e-3997-a47d-de3fc91c9153 | -13.7346 | -60.6079 | 2024-10-10 03:06:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2122ada1-d251-3222-9af6-aec56bae9ef1 | -2.69 | -53.3497 | 2024-10-10 03:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| e3567803-8605-34bb-8201-fc48bf367de6 | -2.6717 | -53.3299 | 2024-10-10 03:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 6b2ae779-0d7c-31c5-b098-b260092a3560 | -2.6716 | -53.3502 | 2024-10-10 03:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 327.4 |
| 6d788543-36f2-373f-9dd1-ea7a5c376cca | -2.6716 | -53.3704 | 2024-10-10 03:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 126981cc-2763-373e-af29-91ef44fb90a4 | -2.6533 | -53.3506 | 2024-10-10 03:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| b72a2c0c-1493-35d2-829e-b93cdac41e8f | -3.8147 | -45.4918 | 2024-10-10 03:15:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 34d6dc7d-53e9-3dca-88e7-ae46531b6f6b | -4.0962 | -48.2523 | 2024-10-10 03:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 63197f42-7085-3034-a994-f3ead7ddc7e8 | -4.0961 | -48.2739 | 2024-10-10 03:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 9a82a460-8c97-3053-8cf7-5215213299fb | -4.1148 | -48.2515 | 2024-10-10 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 159.5 |
| 83e2fca4-c226-375b-b20f-d4dc586899ae | -4.1146 | -48.2731 | 2024-10-10 03:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 244.5 |
| f2d83900-26c2-3ed4-b81c-532e3644fd98 | -6.784 | -59.3052 | 2024-10-10 03:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f5c2b5b5-50bc-3323-9fce-4718360f9fd4 | -6.7839 | -59.3245 | 2024-10-10 03:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| f11c067b-a73d-3c93-93a4-e7aba3e0c688 | -6.7655 | -59.3059 | 2024-10-10 03:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e8b610cf-fa02-3382-9d41-1864802ef12c | -6.7654 | -59.3252 | 2024-10-10 03:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| c9793288-5a44-3af8-970d-f74be4f74c50 | -9.1035 | -61.2769 | 2024-10-10 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| b90e4a25-415b-38ba-a39f-a7a4dc20c795 | -9.0842 | -61.3925 | 2024-10-10 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 140.9 |
| 141c4c3f-935c-3e9c-b2e1-546f386b6ef8 | -9.0841 | -61.4117 | 2024-10-10 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 00c5fd0e-bee8-31e2-b7d3-1d983c21d12e | -9.0656 | -61.3934 | 2024-10-10 03:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| bcef9a27-4746-333b-8bb7-6436c99a5683 | -9.0084 | -61.6253 | 2024-10-10 03:15:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 43196638-06b1-3717-ba83-96000815b930 | -9.1221 | -61.276 | 2024-10-10 03:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 200.7 |
| 97923538-3f08-3e81-a482-bcdc23472394 | -9.122 | -61.2951 | 2024-10-10 03:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| f791ac03-a435-3305-8b8f-964944914050 | -10.6832 | -51.0907 | 2024-10-10 03:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| b0177753-0937-3eca-9395-a751231242b1 | -10.6643 | -51.0927 | 2024-10-10 03:16:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 2292a559-a3f9-3617-aa65-61d426d9e776 | -11.8188 | -58.8459 | 2024-10-10 03:16:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 7a2ea5ca-c210-365e-a8f4-4f68a7a1080e | -12.3067 | -59.1641 | 2024-10-10 03:16:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c8cea812-8969-3e15-94e6-175fae58dd20 | -12.3065 | -59.1838 | 2024-10-10 03:16:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 70e5470a-1f1b-3834-bc18-cebf660c4e7c | -12.973 | -46.216 | 2024-10-10 03:16:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 28759212-ec8a-3424-8a2f-a6c08edf2c12 | -13.8379 | -44.522 | 2024-10-10 03:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 101.8 |
| c2f1904d-09f7-3229-8048-9dd1cf041201 | -13.8579 | -44.4949 | 2024-10-10 03:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 2379f2b4-2937-319c-bafe-46bcfa0e6ba9 | -13.8574 | -44.5185 | 2024-10-10 03:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 329.2 |
| 03615709-fee7-31e1-87b4-00b820dca7f6 | -13.8569 | -44.5421 | 2024-10-10 03:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 1da744c1-176d-352e-ae3a-b40b73160505 | -2.6532 | -53.3708 | 2024-10-10 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 54df443c-d662-3256-bedd-d7af12a3f50f | -2.6533 | -53.3506 | 2024-10-10 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| f7080f14-1701-3088-8d2e-fd6402b1795f | -2.6716 | -53.3704 | 2024-10-10 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| cdefdab7-c3ed-351f-8616-72ddedd7b804 | -2.6716 | -53.3502 | 2024-10-10 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 349.3 |
| 1c55da73-0786-3ae5-a929-1504adc25f8f | -2.6717 | -53.3299 | 2024-10-10 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| e79b548c-4018-3df1-9118-9e29f569a875 | -2.69 | -53.3497 | 2024-10-10 03:25:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 4390427e-f2db-3719-9d6f-9cd63a6ee1e8 | -3.8147 | -45.4918 | 2024-10-10 03:25:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 45b1503f-18f0-3f9f-8fbb-006b85d41e3b | -4.0961 | -48.2739 | 2024-10-10 03:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 127.1 |
| c4dc7e72-248e-3689-9fdd-9919a46ae466 | -4.0962 | -48.2523 | 2024-10-10 03:25:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 5d4edc9d-0795-3c05-99a9-f81424ce66eb | -4.1146 | -48.2731 | 2024-10-10 03:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 223.8 |
| ff4a07e7-bbac-31e2-9830-14de5cccc148 | -4.1148 | -48.2515 | 2024-10-10 03:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| edc71252-f60c-3357-a94f-54a944e5a9ce | -6.5218 | -60.0649 | 2024-10-10 03:25:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5a0e3f0b-d4b0-390c-bf47-1a3daeaf42f5 | -6.747 | -59.3259 | 2024-10-10 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 890ca6c6-f463-3128-9e8f-f0b5917e177c | -6.7654 | -59.3252 | 2024-10-10 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| ea67caf4-50c0-35e5-ac8b-66b8eb76a697 | -6.7839 | -59.3245 | 2024-10-10 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| f446b514-7a1e-3455-a464-c3e8d7f68be0 | -6.784 | -59.3052 | 2024-10-10 03:25:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| a57c246f-551c-3827-a0f3-6e33449b7825 | -7.0416 | -59.4296 | 2024-10-10 03:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 2fbd3c3e-5a6a-3687-bff8-2329585ccea8 | -7.0417 | -59.4103 | 2024-10-10 03:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 796e49ce-22d3-3d68-9540-747548cd8499 | -7.0601 | -59.4095 | 2024-10-10 03:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| e1b2b930-3721-3fdb-b06b-b2982ab2c1b6 | -7.0785 | -59.428 | 2024-10-10 03:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| bfa4c07e-8108-3ea3-921f-86e73e4376a7 | -7.0786 | -59.4087 | 2024-10-10 03:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 178.6 |
| 3fc9a12f-a8fc-3011-a423-873be750b092 | -7.0971 | -59.408 | 2024-10-10 03:25:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 0644abb1-b65e-3ac8-ba0f-5c116bbc50f3 | -8.1475 | -42.9717 | 2024-10-10 03:25:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.6 |
| 93298861-0a42-38ee-aec0-18a52da78a2a | -9.0084 | -61.6253 | 2024-10-10 03:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 828fe332-3224-3b77-aab8-09d317cfca96 | -9.027 | -61.6244 | 2024-10-10 03:25:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 60.7 |
| b140a916-aa1b-3d55-be27-3176a6e65f8d | -9.0656 | -61.3934 | 2024-10-10 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 8e08f23b-7f96-3aaa-a5b3-f4f98849c997 | -9.0841 | -61.4117 | 2024-10-10 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| a31d2501-35ae-3d79-b9c8-7dbbe6af618b | -9.0842 | -61.3925 | 2024-10-10 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| d5141214-02a8-3213-8da3-a795a1362599 | -9.1035 | -61.2769 | 2024-10-10 03:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.2 |
| eff12a1d-5a83-303d-ad40-f7463bad494f | -9.122 | -61.2951 | 2024-10-10 03:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 21315569-a794-3fde-b87f-390a36ca91bd | -9.1221 | -61.276 | 2024-10-10 03:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 162.9 |
| 303bbf32-2a89-3b15-b505-526ad7126d18 | -9.1407 | -61.2751 | 2024-10-10 03:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| b07ffa3e-a486-3210-878a-561f52dd08d4 | -10.3632 | -55.8554 | 2024-10-10 03:26:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| bd5f2569-1837-33b7-98ce-2d4ef3bb372c | -10.6832 | -51.0907 | 2024-10-10 03:26:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 100.0 |
| b34670a9-2501-30bf-848e-8447ea9261ba | -11.0256 | -57.2038 | 2024-10-10 03:26:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 91744353-76bf-3645-82f6-131d45304f71 | -11.8188 | -58.8459 | 2024-10-10 03:26:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 7cc85b8f-d699-3e0e-8a66-608f035d59c8 | -12.3067 | -59.1641 | 2024-10-10 03:26:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 921a13fd-9243-39f9-9b36-e6836cc017a0 | -12.3065 | -59.1838 | 2024-10-10 03:26:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 7b0272df-6de2-37cc-9f22-cdc0dc653aa2 | -2.6532 | -53.3708 | 2024-10-10 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 374fea8a-6b0e-3741-ba9b-7cfc58d48c60 | -2.6533 | -53.3506 | 2024-10-10 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| c1926c5e-52ec-365e-a9f3-24eb2a17ce3e | -2.6716 | -53.3704 | 2024-10-10 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f91355c7-720b-3775-9d27-41ff11f1f3ae | -2.6716 | -53.3502 | 2024-10-10 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 348.4 |
| b52e8241-26a0-3f0a-84f4-b6f6ff0784e8 | -2.6717 | -53.3299 | 2024-10-10 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| d694ffa9-7513-3880-b27f-38b20cc66c6e | -2.69 | -53.3497 | 2024-10-10 03:35:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| c83275c4-8d39-365e-a05c-ea91ec263fdc | -4.0961 | -48.2739 | 2024-10-10 03:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 85d19bc7-cb94-36be-9e06-7b7468f09920 | -4.0962 | -48.2523 | 2024-10-10 03:35:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| e596199b-059b-3d41-a2a5-c3b3bb015771 | -4.1146 | -48.2731 | 2024-10-10 03:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 187.0 |
| 01b55146-77ad-3089-8493-d9e64abc8b84 | -4.1148 | -48.2515 | 2024-10-10 03:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| b4ed14e6-3ee1-356f-9fdd-88a32d13aae8 | -4.2508 | -47.2013 | 2024-10-10 03:35:30 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 47.1 |
| be25eda7-6584-3ebd-b142-072d6aa36a92 | -6.5218 | -60.0649 | 2024-10-10 03:35:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 5d0ee230-dc06-3a5a-8c4d-43b76a26b47e | -6.7654 | -59.3252 | 2024-10-10 03:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| aa1ebb0f-adc0-38dc-b6eb-47b5d728576b | -6.7839 | -59.3245 | 2024-10-10 03:35:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| a1243221-ed9b-3e8b-ae34-85e115433951 | -9.1035 | -61.2769 | 2024-10-10 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| a4ccfa79-d129-3c0f-a052-d4de37248732 | -9.027 | -61.6244 | 2024-10-10 03:35:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 295f5331-a30c-3794-8bb4-ba3491620e31 | -9.0656 | -61.3934 | 2024-10-10 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 4431dab0-292e-3c22-92d4-2fd27ec7919f | -9.0841 | -61.4117 | 2024-10-10 03:35:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |


[Clique aqui para ver as próximas entradas](README39.md)
