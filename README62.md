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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a75dc54-4e03-392a-8702-20d4467a4629 | -8.89111 | -62.43699 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f1c32a81-57d9-39ad-b2b3-7718144b1ebb | -9.01472 | -65.38363 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| adcdf7f0-d434-3c87-909c-db28288d112f | -12.74529 | -48.14091 | 2025-08-25 05:04:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e66416e1-f40c-3b32-932b-edcbeb7165c6 | -8.38367 | -47.99544 | 2025-08-25 05:04:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a0c39b93-2e09-36e0-8bc2-d45f502fdb87 | -7.5312 | -63.33929 | 2025-08-25 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d06687-5d86-396a-8317-dd17b66b117c | -9.6891 | -48.3404 | 2025-08-25 05:04:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46bfe055-1482-35e3-9d4e-27c0ea70b759 | -11.60148 | -46.33667 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54014d30-d9d4-38b5-8c46-81e0a5e114ce | -10.03498 | -59.35641 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b489a407-136e-33fc-ae56-63571e65408c | -9.1739 | -58.30344 | 2025-08-25 05:04:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecfd8b41-a63b-3455-b7ea-31b9b36489fe | -9.16219 | -59.48031 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 676f4a3b-8b47-3aea-be3d-b221b2472729 | -9.15353 | -59.46615 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d7eebd1-22c6-303a-8578-b35cf3b1c018 | -8.06604 | -49.67196 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aea585be-62dd-3048-b2f0-78e1f630d554 | -10.61436 | -55.05731 | 2025-08-25 05:04:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a7ef2f05-2b40-3623-874a-c0ba3c608297 | -10.45632 | -59.12948 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b6365271-6aef-36f1-8b89-7a2e6d4ded82 | -9.64904 | -59.63351 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1193bf1f-abf7-3714-a045-44fc51755d15 | -9.15769 | -62.35373 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6f368bdf-b9af-3648-bd5c-49fe0e43b1fa | -8.05847 | -49.69349 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 78ab66df-c47a-3dbe-b2a2-81b4ff9e50f8 | -9.06529 | -65.72581 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3a6060e6-b437-356a-8cb6-4d9a0bc56ada | -10.41247 | -64.41363 | 2025-08-25 05:04:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7bec96d1-ad3e-35e0-af3c-0401f10dd0e1 | -8.58123 | -62.6302 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a847dedf-5f3b-3f44-a552-f982ed9885bf | -9.16205 | -59.68107 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1d78b95c-f24f-3fd6-ab3f-d986fe64366a | -7.52083 | -63.81634 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3d754c6-fc10-318f-ac3d-d36facef21f8 | -9.52324 | -60.51876 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 66f46aeb-c52f-3d47-9893-fa7a15d49945 | -9.19879 | -59.50342 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35ebb4b6-a99a-351c-b66d-4c6da6ec7776 | -8.89042 | -62.4663 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cab82c3-a307-308a-8d69-dab3cd2053a1 | -7.66076 | -63.52252 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d4a8d9b-4d14-3cfa-b938-5f0e4dc9c1cf | -7.8032 | -61.35924 | 2025-08-25 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea07ff05-1329-339b-af13-d48b8bf6bb16 | -8.89468 | -62.44183 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f13746b0-7d66-3514-840b-2dd5c67ebd4a | -6.79427 | -58.62999 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb402a71-526e-3b2b-972c-8d46601447b2 | -9.58 | -55.36977 | 2025-08-25 05:04:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4212c3e-38ac-35cb-b78f-33537b1a5613 | -9.16987 | -59.45627 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 86616d8a-c14a-3949-9657-48cf238d4160 | -8.87256 | -62.44207 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b5b723b-c24e-3329-b0a8-2a5aee6ace9a | -12.29972 | -49.14701 | 2025-08-25 05:04:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fe06073-7fbf-3ca8-bd45-84b06828c31a | -6.43764 | -58.26113 | 2025-08-25 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ee817af-0bcd-3f5d-8a42-7d8c88d088b3 | -7.27426 | -57.66706 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00d09c3c-f01a-3a6f-a1ce-79487d1edace | -8.23458 | -61.42517 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58381667-84fe-3e2d-84c1-e97c3f51b6fc | -6.49531 | -44.78851 | 2025-08-25 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ece06dc3-f1ed-3ae5-9c2c-a20bb761ea1f | -8.91393 | -62.43258 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ebe05402-dc6e-38ff-82ca-2b2244dd9565 | -8.11302 | -62.87596 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2308d56-815c-30b9-ac43-fa48859c4221 | -8.87755 | -62.43877 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bb9a4d7-8de0-36a6-92a2-ee5852f73786 | -8.97635 | -65.41624 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d1aea69c-ddee-31cf-8c39-c51c1b45619a | -9.24806 | -59.61687 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1afbdb0d-51e9-3957-a166-7959b08ebe17 | -10.71595 | -47.12595 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8e237004-0410-3f3c-8edc-78d88f6a4cde | -8.63219 | -62.65136 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b29c9053-436a-31f7-91ab-3848771da442 | -6.81041 | -58.95622 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 267446ed-c3d6-3159-a8a5-a00c2c2da7fb | -6.81963 | -59.43121 | 2025-08-25 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9181fbdf-9745-3885-a144-766f55bb6232 | -6.43227 | -44.56351 | 2025-08-25 05:04:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6994d0a-1a6b-39cc-b72e-023680346d89 | -9.16664 | -60.81245 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 879c63ea-717f-3e5c-8b45-ef3b8ce7ba05 | -9.72609 | -54.9351 | 2025-08-25 05:04:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18dfa909-086e-312b-8e0d-41feed827bf3 | -9.17922 | -59.46627 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c249bd10-715e-39d8-b164-1b594e0a4722 | -9.16439 | -59.48917 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27d60449-828f-3adb-8ae2-56e0f5fd7b95 | -10.70818 | -47.14254 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d3d58c9-5ce1-3206-ba7d-f65a79d49c93 | -6.20351 | -44.13973 | 2025-08-25 05:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 89533335-9de5-338d-bbe5-d2c5f58c36fa | -9.12917 | -60.73174 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 86867ed2-9ba9-3122-a332-4c84cb106ff8 | -10.72235 | -47.11957 | 2025-08-25 05:04:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4871be8-53aa-33cf-b37d-bf33319995be | -10.2523 | -59.11275 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5472e68-77b7-3d86-ba9e-44b98ac89c47 | -8.87186 | -62.39585 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34a920ae-3294-30be-8674-077760a1d7ef | -9.2044 | -59.49171 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 541c4a4f-4f2b-3fd0-808c-311e8cb82eed | -8.92107 | -62.44229 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72f2dd14-7385-3592-9dff-60ac06dac4e9 | -9.51354 | -60.50763 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7fc03c3-fc9b-3539-8cb7-69e668b37e2c | -9.21831 | -60.91339 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1762b9c2-927d-3e8b-8749-c4a177d3501c | -9.20107 | -59.786 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95040cbd-7838-384e-af88-5604c3a6e084 | -5.87753 | -57.75711 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcbf9984-452c-3d81-99ed-1a53a488e942 | -8.87114 | -62.42503 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e05b6492-d971-3a90-b6c1-ea34dbfcc03f | -7.5718 | -63.43819 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33765b93-8d37-3378-b025-13702846cf4b | -8.62932 | -62.64211 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1eba749c-bd54-39af-85b5-a82363d3d5b6 | -9.21915 | -60.90849 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a1123da-0457-33b0-9015-4daf8c2a963c | -9.12755 | -60.33274 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d24bcd6f-4464-3996-bdcd-a1f4e770ae53 | -8.54587 | -63.51304 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94b4d2d0-41cf-36bc-9ce4-baf7a457d1b7 | -9.01414 | -65.3868 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8aba9ea4-f52b-357d-adf4-e28f0236acbc | -9.17432 | -60.81376 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9ea2d66-a9bc-38f4-a1b9-45b06fc4024e | -8.21555 | -61.41449 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3fe575da-f9b4-3bd1-be1b-bedb7d89f8cd | -7.65989 | -63.52757 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 089300f2-8a57-3018-9cb7-129e37e863f0 | -8.86579 | -52.04562 | 2025-08-25 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb9da928-6c4e-34d8-bbd2-cd21f49ddaae | -11.18321 | -55.02072 | 2025-08-25 05:04:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 921104cf-b278-3215-8294-1623f3b0452d | -7.58697 | -45.23232 | 2025-08-25 05:04:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa6066a7-3da9-358d-8636-4bd7f32e7917 | -9.16966 | -60.81791 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cc271d8-f46c-3dc7-9904-8c865e80955c | -7.54035 | -46.02367 | 2025-08-25 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bf406ead-800c-3a39-9f9f-812b3a1f491a | -7.49683 | -63.81651 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5464f3c0-9a34-30d9-82cd-daf76c51a14e | -9.80023 | -61.20352 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a17318f-1431-3afb-bd58-04f42dddbb2b | -8.59687 | -62.59708 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b49e3f0-5d24-33c0-905b-2781c18ce4fd | -9.51869 | -60.52272 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 172c85a6-3859-373b-9492-178a4bd599cb | -5.88096 | -57.75764 | 2025-08-25 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f7fe159-6169-300d-bb77-1a4d5d272940 | -8.13088 | -62.87915 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5da02c36-b8b6-33fc-9893-79fb921b636f | -8.6099 | -62.59941 | 2025-08-25 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fcaefad7-92c8-301f-b774-399497d6dc36 | -9.26489 | -59.78341 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6596d973-63a1-3354-bbf1-bfe93b98dc52 | -8.22606 | -61.40163 | 2025-08-25 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23571db4-8c0b-3935-8f7f-0efb48da2583 | -8.05713 | -49.67051 | 2025-08-25 05:04:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b7dca60-6844-35e3-86b8-ba0aa7338edb | -9.15091 | -59.50381 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60025809-d9e8-3fd1-8e6f-1bf586dd4220 | -4.93967 | -55.82083 | 2025-08-25 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 301eae89-3ded-3823-878d-580d301c0584 | -9.96329 | -60.18354 | 2025-08-25 05:04:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e5701a66-42aa-34c6-8d01-3a2b6b7c1b0e | -8.86259 | -62.4235 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa7f46da-e8cc-34f0-bead-95f9e48005cb | -8.87541 | -62.451 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4c6e947b-0fa3-34fb-9c74-cc2c767f0939 | -11.63833 | -46.2295 | 2025-08-25 05:04:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 810dc3d6-abff-339c-9bc6-ca4beaebbec9 | -9.21027 | -59.70943 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91be140a-5b7f-35b8-ab4f-ef49921e9714 | -9.20064 | -59.46992 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b788c24-e0a8-3735-b2d9-e27dc13d366a | -7.57094 | -63.44318 | 2025-08-25 05:04:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f168610d-2dfe-3f6a-8b75-e2cd899152cc | -8.91609 | -62.44563 | 2025-08-25 05:04:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 647af9b5-af7f-3cca-bc37-fc7aafad6ddb | -9.19554 | -59.45638 | 2025-08-25 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ee24503-d6fb-3b31-a0ca-a0ed063c748a | -8.99201 | -65.41915 | 2025-08-25 05:04:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README63.md)
