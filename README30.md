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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3144c31f-8b5a-3710-b9b0-2b5445466502 | -14.2442 | -45.5002 | 2025-06-28 12:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 2369f12b-7727-3dc0-bcab-2b80923646d1 | -12.2527 | -46.754 | 2025-06-28 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 5c1f3947-fe84-3478-b5bc-0d804a735045 | -12.2523 | -46.7766 | 2025-06-28 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| d7da3268-6ca8-3402-be8b-99155fb5c64a | -11.2664 | -52.7527 | 2025-06-28 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 184.1 |
| d65ccdd9-7fcc-346a-8b51-ec86268fd0db | -12.2715 | -46.7739 | 2025-06-28 12:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| b6dfdfac-73a3-366b-8504-4a507c823965 | -14.2442 | -45.5002 | 2025-06-28 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c890216b-a7fd-3fcd-9338-383a20dd1f9c | -14.2247 | -45.5036 | 2025-06-28 12:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1672683b-7ddb-3d57-afd0-4633e8c4182f | -11.2853 | -52.7508 | 2025-06-28 12:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 1acd7c0e-896d-3cd6-a74d-94ce379d159b | -14.2247 | -45.5036 | 2025-06-28 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 78178015-5df9-3874-b2cd-7111771e131b | -12.2527 | -46.754 | 2025-06-28 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| dac77d61-ea0b-352f-95ef-edeeb9d4be06 | -11.2664 | -52.7527 | 2025-06-28 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 152.9 |
| 18791502-d39a-3e02-939d-b6e6f503c610 | -12.2523 | -46.7766 | 2025-06-28 12:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 2071a8ec-e09a-31da-984b-9fc65fa7d925 | -11.2853 | -52.7508 | 2025-06-28 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 52c2d9ed-3db8-385b-b9f0-51466f80c30d | -14.2442 | -45.5002 | 2025-06-28 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 530019b5-fa31-3cd7-ac06-7e2194293099 | -11.2664 | -52.7527 | 2025-06-28 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 209.2 |
| 7d4993ee-9414-3831-98b3-b646aac0e750 | -14.2442 | -45.5002 | 2025-06-28 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 2bd10d90-40f0-3d41-9161-27933be43fbd | -12.2715 | -46.7739 | 2025-06-28 13:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8ff192f1-6f9f-3d69-92bd-7c07a3239b5a | -8.6097 | -51.5731 | 2025-06-28 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 17089c83-e4d9-393e-a8d8-cd2322e57acb | -14.2247 | -45.5036 | 2025-06-28 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| fb4d62ee-3d9c-3628-af9f-46b3f1e06bc5 | -6.9108 | -43.9834 | 2025-06-28 13:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 88c02293-8a7a-3f34-84dc-19cf5d8aea86 | -11.2664 | -52.7527 | 2025-06-28 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 191.6 |
| b56afe41-3c9b-3b02-9dd7-489517748420 | -12.2527 | -46.754 | 2025-06-28 13:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| f65dd61f-889f-39ab-9265-a5c400ad7bd4 | -8.6284 | -51.5716 | 2025-06-28 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 5f5d063a-0e22-368d-951f-4a81ebd90385 | -8.6097 | -51.5731 | 2025-06-28 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 069a1c4c-726f-3d4e-87c2-a28fe6d4af36 | -11.0455 | -55.3773 | 2025-06-28 13:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 4015ca6d-0e1e-3861-a927-3cc30c9c6a26 | -11.2664 | -52.7527 | 2025-06-28 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 151.9 |
| eb1c43d3-42c5-33eb-a985-51916a79b122 | -6.892 | -43.9851 | 2025-06-28 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 4e92f317-0d02-35aa-a379-ba120e7370aa | -8.6097 | -51.5731 | 2025-06-28 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| dd76e07d-f323-3b3e-ac5b-1302488c4809 | -11.0455 | -55.3773 | 2025-06-28 13:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 05e5c3f6-4841-321a-be43-79735c04f5d6 | -8.6284 | -51.5716 | 2025-06-28 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 114acf40-4766-3eee-a970-5f0edf1cae50 | -10.8382 | -53.7648 | 2025-06-28 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 3eda8d8c-5b55-37af-8b4f-cfa334fd1997 | -4.5429 | -48.0151 | 2025-06-28 13:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| ac497d5b-9d31-3fcc-9bea-9a12f75c2aff | -10.8571 | -53.7631 | 2025-06-28 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 4e8c3d27-c6d3-3224-904c-035e530dd226 | -12.2527 | -46.754 | 2025-06-28 13:20:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 0e64fbd5-0f05-3a56-894e-16cc4be5dfd4 | -6.9108 | -43.9834 | 2025-06-28 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 6cc7aab8-b882-39d9-b740-181ca201c644 | -11.2853 | -52.7508 | 2025-06-28 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 2d15a0d3-82ec-3d88-9c01-552b695fd0bb | -12.2527 | -46.754 | 2025-06-28 13:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| e3e822e3-8ad6-3771-b29f-b5745a5f0f5a | -8.6284 | -51.5716 | 2025-06-28 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| d9e64b56-ca96-3670-b71f-c04deda720b3 | -11.2853 | -52.7508 | 2025-06-28 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7ee25911-4443-385a-aa8f-59dce09665af | -11.2664 | -52.7527 | 2025-06-28 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 177.1 |
| 1eb269a6-4eff-3264-a50b-d2d83f97ce05 | -6.9108 | -43.9834 | 2025-06-28 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 1fe29641-a2fc-37c5-9285-4e6f53d9d78c | -10.8571 | -53.7631 | 2025-06-28 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 980d3011-935d-338c-bae8-19cbd3725d9f | -4.5429 | -48.0151 | 2025-06-28 13:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| c0c5b7c1-2348-3865-8092-d7b929921f37 | -8.6097 | -51.5731 | 2025-06-28 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1fbad3ba-8897-31f0-abb5-ef75e99da2fa | -10.8382 | -53.7648 | 2025-06-28 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 07dd28d2-93c5-3bb4-9295-02d45a5e1da7 | -11.0455 | -55.3773 | 2025-06-28 13:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 59493599-4ee7-30f0-9513-a34f1a632ab2 | -6.892 | -43.9851 | 2025-06-28 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| b284d443-b867-3c20-a198-fedfaa5340dc | -6.892 | -43.9851 | 2025-06-28 13:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| b3aad77f-fd5d-31b7-b246-3407def91348 | -11.0455 | -55.3773 | 2025-06-28 13:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 793000f9-0cdc-3c8c-94c2-52ef30e052a2 | -8.6097 | -51.5731 | 2025-06-28 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| fac4ed24-045d-383c-a39e-1a572ec0b53d | -10.8571 | -53.7631 | 2025-06-28 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| bc229641-a8be-337f-be95-9fdc889a6424 | -11.2853 | -52.7508 | 2025-06-28 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.7 |
| 351a5b76-05ca-3157-9c8e-2aaebae1e803 | -7.2206 | -43.1857 | 2025-06-28 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| b9c78bea-6d8d-3b8b-8aac-ee68f30d3488 | -7.2203 | -43.2092 | 2025-06-28 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.5 |
| cfb13de3-3c41-394d-92cf-2695748aadb4 | -11.2664 | -52.7527 | 2025-06-28 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 248.7 |
| 5eb03a5a-492b-34f4-9130-805d541f46f1 | -6.9108 | -43.9834 | 2025-06-28 13:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 4ff5ebde-d4de-3393-b329-210b2fb9953b | -4.5429 | -48.0151 | 2025-06-28 13:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 6f315cff-4e60-3478-9c7c-29b9eda05929 | -10.8382 | -53.7648 | 2025-06-28 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| cd615895-4d2e-3b78-944f-ac96a109f017 | -10.8385 | -53.7442 | 2025-06-28 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 97ddfcbc-b73c-303b-afbe-f5cd81e2be53 | -4.5429 | -48.0151 | 2025-06-28 13:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 7fe08064-5260-3d75-85dc-97980337b291 | -11.0455 | -55.3773 | 2025-06-28 13:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 16bcae5d-b161-3188-813a-c351619df955 | -11.2853 | -52.7508 | 2025-06-28 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 125.2 |
| 0920877f-83ed-303e-927c-3c994ff2db99 | -11.2664 | -52.7527 | 2025-06-28 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 338.2 |
| b64b8e49-0a38-3451-bad8-afcb31bcd625 | -6.892 | -43.9851 | 2025-06-28 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f5f28be8-cd40-3001-84c1-37ae85bd62ec | -12.1141 | -54.5685 | 2025-06-28 13:50:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 94fcb966-7e77-3fd4-bd74-0b5a3a5497db | -10.8382 | -53.7648 | 2025-06-28 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 2ed4973e-f89d-3001-80b2-67fe288e5eab | -8.6097 | -51.5731 | 2025-06-28 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| f848c82f-ae66-3c75-b823-63c013b5bc1c | -10.8571 | -53.7631 | 2025-06-28 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 47ab5add-06e9-3a3d-861b-d6f97a517f2b | -10.8385 | -53.7442 | 2025-06-28 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| df5d6ac6-aff3-35a4-876a-187245c60818 | -11.2664 | -52.7527 | 2025-06-28 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 349.8 |
| 320616b3-c2b2-30bb-8e3d-dc8a427a0ce8 | -6.911 | -43.9602 | 2025-06-28 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e2e2d7b1-23da-3325-b7ad-d393e437ae22 | -12.1138 | -54.589 | 2025-06-28 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| c03c8624-6239-32b4-851f-84b0c3852a63 | -10.8382 | -53.7648 | 2025-06-28 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 2d5c593a-41ef-3422-a353-63681139ddb1 | -10.8571 | -53.7631 | 2025-06-28 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 2d2129ec-ac5d-3a57-ad27-b681e744e0ff | -6.892 | -43.9851 | 2025-06-28 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 243c6455-83d5-3762-a2c4-bbe4d0b7f6c0 | -10.5579 | -52.0289 | 2025-06-28 14:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8ef79f63-25a3-31d1-bd7b-235a88166ce1 | -11.2853 | -52.7508 | 2025-06-28 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 931ba35c-6c66-3815-90b4-d07463b85d0f | -10.5576 | -52.0499 | 2025-06-28 14:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 3102c5fe-6dd5-3053-a5f8-0ad741582453 | -12.1141 | -54.5685 | 2025-06-28 14:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 64db5aaf-a7da-3611-9d98-473d22542ef3 | -6.9108 | -43.9834 | 2025-06-28 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 332aa93d-9a2e-3ee6-824f-a4477fb4ffa3 | -11.0455 | -55.3773 | 2025-06-28 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 97c70b3d-d874-39d0-80f2-d110e9302bf9 | -12.1138 | -54.589 | 2025-06-28 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 097ff1df-b668-3c86-a76b-8775e44eb066 | -10.8385 | -53.7442 | 2025-06-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| e70c893c-b278-3a81-ad0e-3d9c8767b48b | -12.1141 | -54.5685 | 2025-06-28 14:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 6b4bb154-9da3-34c1-bc44-2f2ebf48739a | -6.892 | -43.9851 | 2025-06-28 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 01e55381-7586-3d09-96e5-f41f7efb7049 | -11.2664 | -52.7527 | 2025-06-28 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 334.3 |
| db2213c0-ea25-383e-b192-84ec5efd5034 | -6.9108 | -43.9834 | 2025-06-28 14:10:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 7b45a473-b707-314a-a587-c12d4c58d4a2 | -11.2853 | -52.7508 | 2025-06-28 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 1877ff5f-da30-374d-bc1e-1869c259c2dd | -10.5576 | -52.0499 | 2025-06-28 14:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| ffc5a1d7-0942-3869-9954-7ae26bd20078 | -10.8571 | -53.7631 | 2025-06-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 8a9ee0bd-4e3c-3b7f-9ada-39b6f15b3829 | -10.8382 | -53.7648 | 2025-06-28 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| c1f1dae6-758d-3262-8557-e35837f8a8b1 | -11.0455 | -55.3773 | 2025-06-28 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 92.1 |
| ddc9273d-2572-370b-ac97-a702aff32efb | -4.5429 | -48.0151 | 2025-06-28 14:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 1d2f0eca-6985-32aa-b150-759ea30eca3c | -10.5579 | -52.0289 | 2025-06-28 14:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 2b32ff5e-8f4b-311b-aa0a-021fa94c97fb | -11.0455 | -55.3773 | 2025-06-28 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 4347b562-5837-3f05-9d89-81e322bc30cf | -6.9108 | -43.9834 | 2025-06-28 14:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 1b109574-8b9f-3de8-865d-5a31d4b6ef03 | -10.5576 | -52.0499 | 2025-06-28 14:20:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 175210d9-ddf4-3b28-9d0a-003ea84889e0 | -16.2625 | -53.6694 | 2025-06-28 14:20:00 | GOES-19 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 6d5b6c49-7104-35ef-bde2-d45c973afa8d | -10.8385 | -53.7442 | 2025-06-28 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2a20e250-fc75-3122-88dd-e3d1b4b3f889 | -12.1138 | -54.589 | 2025-06-28 14:20:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |


[Clique aqui para ver as próximas entradas](README31.md)
