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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90d2b935-8f78-36bd-801a-9d8edf28a4cf | -4.45049 | -45.46314 | 2025-10-27 04:59:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8bcd69d7-f59e-3af3-88da-a4642476af6d | -3.10977 | -51.20654 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b832cd9-8133-3ef9-9057-29a46c4bde25 | -4.46617 | -50.47508 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d739516d-ad59-3a24-934a-aa9aeafeca8e | -2.73622 | -49.3859 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ce62199-3efd-3253-ae38-5fd21c7e31d0 | -3.04393 | -53.01909 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a1ada15b-fa68-38fd-8340-d9b5d9365aaa | -4.45669 | -43.43549 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b4e3acd-ea58-387e-a2cb-cf72b03caceb | -3.57929 | -43.60842 | 2025-10-27 04:59:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9897601-eca3-3bd1-ae68-274433ef3d7c | -3.15418 | -50.33543 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d02ee502-eb3a-3762-8888-849f23dddc49 | -3.13808 | -53.00172 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bf6212a-9a39-33ba-a4bb-21373d1582e5 | -4.47657 | -43.42183 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 3f65c1d0-6d16-3d0f-a469-c7ce4acffc44 | -2.90116 | -53.13174 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6de29a4-47b7-39b2-8085-c1c2d2d90bb2 | -4.72742 | -46.81225 | 2025-10-27 04:59:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0629a69e-e5f1-34cf-bff4-30f7e65a8606 | -3.15482 | -50.33126 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc62e34e-305f-3c04-a50c-e202085ba16f | -3.75434 | -51.75731 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dac54565-cc91-3ba3-8290-fc8e5605da51 | -4.38963 | -43.32057 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 815c808e-d14b-3704-9cac-62a30de3e27e | 0.44096 | -50.82102 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f7d4103-cbf4-3424-9a88-a39d8059acd2 | -3.42401 | -52.43633 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 333c9eb1-20ba-3abe-8285-68884d0a9467 | 1.14422 | -51.07124 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74540bc1-181c-3076-8f3b-80d4b992f3fe | -4.14597 | -50.68725 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18f8308b-e56d-3254-b063-f43c23892e1e | -3.60459 | -43.56284 | 2025-10-27 04:59:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9d57e0c-44a3-32e8-9f60-00c7c6f1d56e | -3.11326 | -51.20709 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71137894-6660-3cf6-83be-830313a46958 | -4.39044 | -43.32287 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b19da5d7-5b2a-3cb7-92bd-ee2a96fc9379 | -3.86691 | -52.39531 | 2025-10-27 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44619fc8-f364-34e0-9a36-39bf38b45d12 | -4.44098 | -43.42071 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73e1c478-eff9-3c48-ad1b-c40d896558bd | -4.32605 | -48.09119 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb97d309-35ba-3605-a761-5b323201e26c | -3.71345 | -47.64633 | 2025-10-27 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcc321da-7c0e-3adb-a006-5591e0938c14 | -3.56689 | -44.5281 | 2025-10-27 04:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c418d31e-c853-3ed6-8b41-a36bf772411d | 0.43281 | -50.79196 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ac5f2aa9-a86e-3a10-9fff-fdf1a2e138a0 | -4.45789 | -43.42728 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1684a904-46dd-36d5-9d2c-1e193f7df5f7 | -3.86861 | -52.25237 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c03be95f-3d2f-3b50-ba4b-80446568dbf7 | -3.11826 | -49.10667 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f1580e7-13bf-3443-8c94-d67fd43888c9 | -4.4535 | -43.65905 | 2025-10-27 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f2310726-3666-3546-82b3-ed96f7540345 | -4.31817 | -48.08612 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b087cf1-f393-33b9-882f-7812e6681bec | -3.24328 | -48.77566 | 2025-10-27 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0c85cb4-f0b0-3f96-a1c1-0fecdaebefa6 | -3.09677 | -49.45341 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| daeb2948-7ac8-3a55-869f-5e41d8f9d2cd | -3.80991 | -51.78064 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 539ea9e5-01f2-3094-9c15-1c4dbaf17001 | -2.86925 | -52.79644 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96c13d95-e5d5-3428-8e87-657da7bae2b4 | -4.46911 | -43.42249 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b86cd949-d9e4-34a4-87f1-8a632aa2fc50 | -4.1436 | -50.68625 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d7dfd2ee-3499-3f44-809e-75c59725bc87 | -4.46682 | -50.47084 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1cb164d9-48bb-30f9-842f-0e080ebdf8f4 | -4.26299 | -50.51257 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 728ddadd-155d-3da5-9070-8e3270f87359 | -2.3234 | -48.58173 | 2025-10-27 04:59:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 08e509ca-7637-3f92-b240-119819e2986d | -4.26 | -50.50779 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7d94421a-043f-3949-9c5c-7305f0f2fdcc | -4.47075 | -43.42088 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0025a86f-cf88-3283-8650-0e0aa90b0ce1 | -2.2262 | -48.37253 | 2025-10-27 04:59:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6953446a-1d52-34f8-8511-43fbda5852ff | -4.48658 | -43.4254 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 34fbcc42-cd63-3b64-bb19-9b3cb57ff01e | 0.4438 | -50.81679 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d0b6e41-1ace-32a6-b7f5-d4941b97b639 | -4.20477 | -48.3539 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 201488c5-7979-3c7f-a681-f617abaaf825 | -4.26431 | -50.5041 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6adfaad-31c2-33ec-b851-c0ec09e0ec3e | -3.17743 | -52.49624 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28fbfe79-0c7c-34a5-ba21-ab714e748654 | -2.69333 | -48.46136 | 2025-10-27 04:59:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6d1a9d7-f4e2-3c6c-8079-1368787f419d | -2.25407 | -51.88789 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f107b121-1b36-3908-a82d-b654aa6593d1 | -4.4318 | -45.97824 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1999b462-14fb-387d-8ce8-f8e48da99fbe | 1.61138 | -55.72627 | 2025-10-27 04:59:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c7cfcb9-3b1d-3edd-b046-3c209b2d1c4e | -3.2492 | -50.03653 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0b05b5d5-c796-398b-adea-1cc1b3f32f0b | -4.15409 | -51.14161 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf0bac01-15d9-34fc-a83b-03290b53f718 | -3.86802 | -52.10067 | 2025-10-27 04:59:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 281b57d6-3769-36bb-930e-a73e623d18ec | -4.80487 | -43.30106 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6fc61360-e104-3bf2-b02c-ce7e7dd4f42d | -3.0974 | -51.28675 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9cda0fb7-df92-3b87-acf8-46c6d90db55b | -4.44562 | -43.42972 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f650b16d-6a8a-3930-8a10-c69d62db2ee3 | 0.43694 | -50.81786 | 2025-10-27 04:59:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78f8afae-111a-330d-a57a-d2d4b2fc131c | -4.47551 | -43.41934 | 2025-10-27 04:59:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d24b526a-567b-310a-b9a2-27e217765749 | -3.72211 | -47.64756 | 2025-10-27 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d730e48a-a4a3-3a89-85ea-e267cf80d629 | -3.14415 | -50.4487 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a70cc1f3-1ae5-3d47-b3c5-adbb59480dce | -5.02962 | -44.68506 | 2025-10-27 04:59:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 525f17db-3df5-394f-90f9-be9fecb5e78b | -4.83092 | -45.34528 | 2025-10-27 04:59:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e718f96-bf3c-3312-ad09-909ef2d17b63 | -3.54419 | -51.09951 | 2025-10-27 04:59:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be4a16cc-5dcd-34ea-84c7-a828b924c304 | -3.42457 | -52.43279 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce8c1191-f92d-39ce-a71e-ab832ef13bf9 | -2.78982 | -54.41795 | 2025-10-27 04:59:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b7ed240c-2586-3819-a141-7392e1a2d33b | -4.31386 | -48.23049 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1cec1225-0057-3138-9b5a-f968ac2a4baa | -3.756 | -47.6091 | 2025-10-27 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cbdecbc-4b55-3e0c-b52d-ac6ae947096c | -3.42065 | -52.43579 | 2025-10-27 04:59:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81f24280-3f18-3c5c-893b-ee2348c47ea6 | -2.23053 | -51.99429 | 2025-10-27 04:59:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5485209-4d2d-3fca-900b-159da08b2374 | -2.08122 | -48.37094 | 2025-10-27 04:59:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27470288-0a6b-3b71-9f00-b14752ebe162 | -3.15781 | -50.33601 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88bdf1b8-f465-3dbb-b0d3-4c5817c2c3d7 | -4.20528 | -49.76125 | 2025-10-27 04:59:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 89fa8f9c-5c2b-3575-a230-074b6df8e0e8 | -1.38112 | -55.34843 | 2025-10-27 04:59:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10235b5b-9d93-3802-bd8d-85cbf31040f4 | -3.34027 | -52.8372 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 804edc64-f7c4-36a8-9082-3aa583584f87 | 1.14637 | -51.01917 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da3a9421-3d2b-3a2f-ab32-6bfdbff97926 | 1.1487 | -51.05578 | 2025-10-27 04:59:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f15f278-f9d0-352a-90b8-29846fea083f | -2.9017 | -53.12828 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c45568be-be7e-3425-a7d1-852bdaf45a51 | -4.22858 | -48.36502 | 2025-10-27 04:59:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42765db8-c9a3-385d-b663-5c089b4ddf16 | -3.04726 | -53.01961 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65a15894-7a22-3614-856e-ede1b7f86cab | -4.42441 | -45.98018 | 2025-10-27 04:59:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0cb018e-0dea-3c05-a987-aa57e052a637 | -3.11267 | -51.21092 | 2025-10-27 04:59:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| caa4d777-ef07-3602-93c9-c326f9579506 | -3.15009 | -50.45808 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b3d38fc-371d-3d40-a65c-b288cf530a5c | -3.7085 | -47.64982 | 2025-10-27 04:59:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c6528c3-1959-300f-ad0c-e6ee298cdfb1 | -4.4523 | -43.6647 | 2025-10-27 04:59:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4963731-6571-3f43-bd12-408aa942a322 | -4.79837 | -43.30443 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3122c9a8-13e9-327c-b1cf-f537ad824fb2 | -5.03009 | -44.68185 | 2025-10-27 04:59:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8abd9176-a549-35e6-9530-be1c543f1b58 | -2.79626 | -54.86306 | 2025-10-27 04:59:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 85006c86-61ea-3e7b-886f-bfde0f5297cb | -3.11753 | -49.11145 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 704a71dd-01f5-30fd-bda3-b5b222408cc0 | -2.90061 | -53.1352 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f45d754-a5dd-347f-8ef8-e422ed38e266 | -4.80429 | -43.30523 | 2025-10-27 04:59:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8f7386b-6ca1-3caf-8138-7260790a25a7 | -3.25289 | -50.0371 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5cadf4c-029f-3cdd-82cb-5bbb5731b16b | -2.63729 | -47.29819 | 2025-10-27 04:59:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96465f53-ac32-33e3-8040-171def837c45 | -3.15055 | -50.33487 | 2025-10-27 04:59:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e6a6262-dc21-3f01-a139-76e7abc1616e | -3.28668 | -52.96072 | 2025-10-27 04:59:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b3f0574-310c-31c0-a51e-103190d0dc4c | -3.07727 | -49.47886 | 2025-10-27 04:59:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b02a3a1f-a687-3d34-8e07-90e85dbcc25e | -3.57175 | -44.53233 | 2025-10-27 04:59:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |


[Clique aqui para ver as próximas entradas](README54.md)
