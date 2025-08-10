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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a29d903-eb9a-3241-a90f-d5f517e815b9 | -9.48772 | -46.27862 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2937f3a-9b25-3f77-804c-1f4ab0d6f1d7 | -8.93187 | -60.75912 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b7d466e3-11ea-3eca-9224-98d447d273e7 | -10.34026 | -44.90614 | 2025-08-10 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 12339902-3a46-3b4f-9332-b21941d3cffb | -9.19987 | -59.67648 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e199371b-aef1-37a8-ba7b-7982cd466690 | -11.7813 | -44.95037 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af94bd4d-e99f-3b34-abd9-c247a9020389 | -13.61612 | -46.93967 | 2025-08-10 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49f40e30-baf9-3869-9fca-d69625555381 | -9.52791 | -45.39942 | 2025-08-10 04:46:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2f84416-51ad-3563-855e-816f4a0d6135 | -13.1095 | -46.89777 | 2025-08-10 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e61a5921-e594-31e8-8da5-20311130074d | -14.74405 | -45.15784 | 2025-08-10 04:46:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f8d5f02-470d-3a81-853e-ae083d23fec2 | -11.37772 | -42.09807 | 2025-08-10 04:46:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| c67098d2-0496-3b58-9222-2f924215115f | -11.3782 | -42.09409 | 2025-08-10 04:46:00 | NOAA-20 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b8e41305-3d7e-342c-b23e-08cb4f110ba0 | -9.52743 | -45.39734 | 2025-08-10 04:46:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| facf0232-d86a-3ad5-9954-a5530394bc53 | -9.36902 | -61.52737 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 0bbbf139-7259-3217-ba00-6bd15d41a389 | -14.37537 | -51.11299 | 2025-08-10 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0987ce3-d5c2-31fe-a47b-09447018b06d | -7.09124 | -59.192 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0167327-3f86-3063-b284-144a7918d006 | -7.07366 | -59.17752 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 92b6d52b-5659-32cf-ba7b-264b0ed8e4ce | -8.56901 | -54.68158 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8ae3cfd-ddb3-32c0-ab11-fd44f9530e0a | -11.32295 | -55.21549 | 2025-08-10 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b9594e3-2913-33af-bc74-020656f2d517 | -11.48833 | -50.28121 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a68682f-3096-38b1-976a-a3627362cd62 | -15.16052 | -48.1291 | 2025-08-10 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b86ab033-e7c5-3c96-abf4-55106b9521a2 | -12.56147 | -47.09568 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76e0c0dd-4664-3758-8a4a-8c1353d30cfb | -14.03729 | -46.34131 | 2025-08-10 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab85cbbf-3f7c-39f5-9805-ec57793c0824 | -8.92965 | -60.74168 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 110bc1ba-9f59-3a35-a66a-4b2d3be33f03 | -14.29921 | -51.97735 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 736539dc-e0e9-3d14-89e0-58a8886a3939 | -7.06501 | -59.19823 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8adf009e-8579-3f4b-8943-8f72ac6bfc06 | -7.08446 | -59.20207 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 709cee6c-743b-3c2d-8340-22507a65670e | -15.15702 | -48.12486 | 2025-08-10 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26e0e30b-aec6-36f2-872a-f7e0b44dade1 | -11.74675 | -45.03202 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ca7015c-0ce9-3dce-b144-33633582d0bf | -14.37879 | -51.11349 | 2025-08-10 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 264d4682-0b22-352c-8a5b-8fb3f7d1777a | -9.93665 | -60.50533 | 2025-08-10 04:46:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 636096cc-5249-31e3-b135-6e9e40d84751 | -8.92623 | -60.73089 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 7ff6c062-e979-3277-a2d3-fb241e3b3b3e | -7.06404 | -59.20375 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 13d7a1a8-4b64-3150-ba4d-31ec482b487f | -8.56184 | -54.68038 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a2d210c-a5e9-319a-a2a1-c64ecac1d0a2 | -10.46242 | -47.94156 | 2025-08-10 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ca574f3-3e60-35ae-8be8-7ec65173661a | -7.07177 | -59.18833 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a1ef41cf-315a-3c5a-9764-422dbf8b7c12 | -12.68768 | -48.20037 | 2025-08-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2692ddbe-765b-3142-a5df-6b87429e469c | -7.0611 | -59.19183 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47323ec7-b14c-3432-8f76-953cdc52ec78 | -7.40354 | -60.00058 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5332807-a95e-3798-848f-2f6eca9b636c | -8.56611 | -54.67687 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e905fcfa-5106-3976-b1ed-358567875667 | -8.57038 | -54.67336 | 2025-08-10 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 50cad598-b951-3c3b-97e2-41ceaa2ae24e | -12.64775 | -44.51293 | 2025-08-10 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1474705-0669-3624-8906-fbc965143db9 | -15.09427 | -46.54115 | 2025-08-10 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8b351ac-0fb5-32d9-b39f-de6917add822 | -11.11667 | -50.49406 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c68efef4-b40b-3164-8e51-e9d30d471509 | -7.07473 | -59.20019 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 394a473f-7e0b-36d1-a658-8f732ca07dc9 | -9.49077 | -46.2869 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| caf968b6-ee98-353d-b0d7-0217850179df | -9.8673 | -49.96276 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 15a83406-6797-3eee-8ebd-a7dd70173ed8 | -13.63598 | -48.98904 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ea1cf1c-98e9-3037-8ad0-b1b75903c936 | -12.64448 | -44.5137 | 2025-08-10 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b864d5bb-3a9d-307d-9192-8588a46dd2f3 | -11.11554 | -50.50147 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1c43693-b5e8-3db4-9d59-8e97d0899301 | -10.68345 | -56.55421 | 2025-08-10 04:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6007b566-d24c-35f6-b986-09e96ee5dbdc | -10.4392 | -50.97776 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b855f8e-3226-386d-8bcb-8656f6f7b1a8 | -9.19503 | -59.67551 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e663160e-4468-30d2-b816-2b2cface209f | -14.46657 | -47.8423 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ae39282d-82a7-33d3-ad8a-e39da0d6e063 | -8.9232 | -60.74728 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f77d0b0c-b83d-399b-b181-e65d2af561d8 | -9.70633 | -61.30543 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 926e568d-16c9-3a7f-a770-b6d67957c8ab | -11.37027 | -50.52837 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90ee9ee2-9f9a-3f51-a1d9-adb7089ffeb1 | -13.05717 | -56.84726 | 2025-08-10 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91e2eab9-3928-3d40-ba54-050863f67db1 | -14.0295 | -46.33688 | 2025-08-10 04:46:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bac7419f-d149-3924-bc91-08b0df4f9a24 | -14.28753 | -51.96434 | 2025-08-10 04:46:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 036f8bbc-5b77-3cde-929e-703b4dc5b9da | -9.19747 | -59.67739 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3655731f-d987-3c2d-8a98-2189c3090a48 | -11.4849 | -50.28068 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9edd516c-d020-335b-9093-d413be4f0408 | -14.44689 | -47.85878 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6332739b-eec5-3f2d-8056-fab2b1a4fb92 | -14.58626 | -47.15265 | 2025-08-10 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40ce3f4c-5235-3a2c-9755-dfb4a48b3c1a | -8.92259 | -60.75056 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eeae2789-f8e3-3fcb-8ad4-ebd228ebc350 | -13.61551 | -46.94256 | 2025-08-10 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd7383cb-f9d1-3694-8d9f-2a049ef8359e | -11.11214 | -50.50095 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42d71bab-23c4-3b48-9bf3-5a3c44eca372 | -14.46861 | -47.85033 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38098e64-840f-3232-a38e-fbf18733864c | -11.10077 | -50.46121 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff664ee4-42ab-372b-9fe1-0b125eb40991 | -9.36969 | -61.52373 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| f45e1204-7932-30ce-9774-85f3c778e9c3 | -9.36769 | -61.5346 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 79b5d7af-341a-3b0e-94da-94d658cde817 | -9.3745 | -61.52841 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e3886fc5-998c-3f6c-9a29-bcb274477391 | -9.49606 | -46.27974 | 2025-08-10 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 34e48d68-f5b1-3810-9cea-e697f7fd53dc | -9.70569 | -61.30888 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e66eda02-f095-327e-bbd3-8ed354da38b5 | -7.05717 | -59.1856 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43bce0bb-98fa-3ef7-ac1b-3ae3667f25e0 | -7.06878 | -59.1767 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55ad1e46-d64e-3857-a3c9-a6163695daa5 | -11.36913 | -50.5358 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 89a617c4-f5b1-32c4-9d51-5f9a54bbfc82 | -12.55023 | -47.08549 | 2025-08-10 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 800fdb1e-86cf-30fa-92fd-06e0cb51aa11 | -9.57357 | -48.44266 | 2025-08-10 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c9e3752-4117-3934-b91c-ca4ed2d6c211 | -8.92724 | -60.75479 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 807b3fee-ea8e-36f1-b533-63436caa8719 | -10.46156 | -47.94291 | 2025-08-10 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b197b9d-204a-3271-a488-062fad52eaa2 | -13.06097 | -56.84795 | 2025-08-10 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 793289f9-b8cf-34dc-9f63-3de1a1012f12 | -12.71263 | -46.36535 | 2025-08-10 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e854976-3c5f-317e-b31a-9e00a7ce803e | -11.72996 | -45.0142 | 2025-08-10 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f77e9516-49c7-3281-9ee9-ea6bda310d4a | -8.92079 | -60.7603 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6e46afd3-c6a6-37ac-ae73-24cdd19ab4e1 | -14.46461 | -47.84958 | 2025-08-10 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 744603a8-cd0a-34fa-bbe7-558ec36cf8fd | -8.93026 | -60.73839 | 2025-08-10 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ff71c132-699e-3f0c-b81c-cf27a1aaabb3 | -13.6364 | -49.01254 | 2025-08-10 04:46:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8078a40-9965-348e-862e-eb52f14536a0 | -10.43849 | -48.34573 | 2025-08-10 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0b5d971b-d799-3828-ab1a-379ee694e351 | -9.86331 | -49.96599 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de156e6b-e181-3668-a66a-f0bf0723cf19 | -12.71091 | -46.378 | 2025-08-10 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 53780270-ac89-36c4-8bd6-9c41c17e8186 | -7.07161 | -59.16052 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fb597fa8-4d33-3cdb-8b23-264fc3c61631 | -12.57771 | -41.28437 | 2025-08-10 04:46:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4f041b49-a921-37fd-981e-d0ac6d0bc3f8 | -10.4609 | -47.94765 | 2025-08-10 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79e56bd1-2a5a-3667-93f8-ae38886090e6 | -14.09232 | -46.57607 | 2025-08-10 04:46:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b38170d7-adbc-31b7-8abf-766164ef2dce | -11.65861 | -48.3209 | 2025-08-10 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43b963de-647e-360f-abb9-865130f3db97 | -11.10816 | -50.48135 | 2025-08-10 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f7ed675-3f6a-37ba-88fb-3e36911d0b4d | -10.41938 | -50.38067 | 2025-08-10 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4277f92c-5f37-3cf7-85cb-76a67584dd90 | -12.68988 | -48.19828 | 2025-08-10 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aaca489a-c593-334f-8a29-2773e1849156 | -7.07377 | -59.20572 | 2025-08-10 04:46:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 79d8c6ce-bdea-30a8-8900-4f8e1d15c1a4 | -10.34146 | -44.90491 | 2025-08-10 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |


[Clique aqui para ver as próximas entradas](README25.md)
