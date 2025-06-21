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
| 79300e92-d801-3ad1-9a13-96b4e1775920 | -8.5911 | -51.5537 | 2025-06-21 12:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a2e14936-7047-3f31-8a6a-7bce6c67f1e5 | -8.1827 | -47.7821 | 2025-06-21 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 009b3371-054b-3b09-965a-138649479a11 | -11.798 | -57.243 | 2025-06-21 12:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 3526f7d4-a15c-3daf-8a0f-97031adfdc07 | -11.5779 | -44.8413 | 2025-06-21 12:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 19eceb3e-1dd3-3298-8dc6-417f55283b51 | -8.1827 | -47.7821 | 2025-06-21 12:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 350e5a98-d646-3a76-8c80-2e4469f7e75a | -11.798 | -57.243 | 2025-06-21 12:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 130.1 |
| a5002e54-7448-33c7-a01b-f3f839eb2e14 | -11.5779 | -44.8413 | 2025-06-21 12:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 132.6 |
| f5b923bc-ddca-31fc-a25a-9833f8994b68 | -11.7791 | -57.2445 | 2025-06-21 12:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| f1cdfde1-9190-31f9-858a-789ab410d33b | -8.5726 | -51.5343 | 2025-06-21 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 50a3a169-bc35-3acf-aa5e-5c24daf084d5 | -8.5911 | -51.5537 | 2025-06-21 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d63ac658-4905-317d-b314-c177ea2b985f | -11.7791 | -57.2445 | 2025-06-21 13:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 5f344e0b-b11d-31d7-9db2-9d0708d65b91 | -11.5779 | -44.8413 | 2025-06-21 13:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 180.8 |
| 42eb04cb-1a15-3e0f-9808-056d381a731e | -11.798 | -57.243 | 2025-06-21 13:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 143.3 |
| 3c38dde6-dc4e-3697-8178-0740697f68ae | -10.8828 | -56.4767 | 2025-06-21 13:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 6039a16d-aa99-3be5-b1fe-88b7aefe1f68 | -8.5911 | -51.5537 | 2025-06-21 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 0b559e37-5c6e-38f1-a8af-854ced966ed1 | -8.5911 | -51.5537 | 2025-06-21 13:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 12423222-05f0-3d81-8092-38aff516c15d | -11.7791 | -57.2445 | 2025-06-21 13:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 6df40be7-d876-3c04-b134-1ee5715193cc | -10.883 | -56.4567 | 2025-06-21 13:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 5ca08c67-9b54-364c-a7b5-379a1041fd76 | -10.8828 | -56.4767 | 2025-06-21 13:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 134.5 |
| e9f27c54-32e8-39d1-8297-adbf12cd03f6 | -11.798 | -57.243 | 2025-06-21 13:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 137.6 |
| e37d20f5-d36b-34e0-9c7a-c5c08328afb5 | -11.5779 | -44.8413 | 2025-06-21 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| bc586ad7-8e5e-3943-bece-3ef917b459e5 | -10.5051 | -47.5845 | 2025-06-21 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| e3cba0ea-681d-376b-9b1a-f38db0cba970 | -10.8828 | -56.4767 | 2025-06-21 13:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 1d961e85-e811-3673-8177-7ed31384a73c | -11.7791 | -57.2445 | 2025-06-21 13:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 8582924d-9be4-3c02-b616-7426791f3a26 | -10.9018 | -56.4552 | 2025-06-21 13:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| df696502-33e8-330a-97a6-97079d692375 | -10.876 | -53.7614 | 2025-06-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 859f74e9-3c4a-3122-b451-e085a2e46743 | -10.5241 | -47.5822 | 2025-06-21 13:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 1c2e11f8-0ba4-3f03-a1ee-833a08f1c448 | -10.8571 | -53.7631 | 2025-06-21 13:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7e797af5-d93c-3673-b007-b4959f1e327b | -11.798 | -57.243 | 2025-06-21 13:20:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 134.1 |
| 25b203f3-ec6c-35ec-b5eb-284878e05300 | -11.5779 | -44.8413 | 2025-06-21 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 209.8 |
| 0b925136-2947-39c1-87eb-3c706b485fca | -10.883 | -56.4567 | 2025-06-21 13:20:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 68b00900-7ea3-3dfd-88e0-f867a6fe2d73 | -11.7791 | -57.2445 | 2025-06-21 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 121.9 |
| db75bd8c-443e-34a8-8fc8-d0bb7a4d5753 | -10.8828 | -56.4767 | 2025-06-21 13:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 159.5 |
| af6c803b-a0f8-37c8-a9b0-131af96992de | -11.798 | -57.243 | 2025-06-21 13:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 9e448308-ae43-3012-b94d-5f2777ecfec1 | -10.5051 | -47.5845 | 2025-06-21 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 5512479c-1f39-3670-a759-5043215d92d1 | -7.216 | -43.5836 | 2025-06-21 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 17410eb8-cebb-3f0a-b8ac-66a4abc92520 | -10.876 | -53.7614 | 2025-06-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 82f97b14-808e-39bf-bd8d-49a6309e292e | -10.8571 | -53.7631 | 2025-06-21 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 0747b764-d300-398c-bafe-d1ee8161b462 | -4.5429 | -48.0151 | 2025-06-21 13:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 6002d2a9-9888-3f5b-a329-7458c7326ca4 | -10.9018 | -56.4552 | 2025-06-21 13:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| e92bdbca-d93d-3fd7-9014-60297ce7aa7c | -11.5779 | -44.8413 | 2025-06-21 13:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 445b53f5-1052-317e-a484-5a0a7b73b302 | -10.883 | -56.4567 | 2025-06-21 13:30:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 86.1 |
| ffdfbd80-ad68-3ef3-8a01-86a48ea7c0d2 | -7.2163 | -43.5603 | 2025-06-21 13:30:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 92.9 |
| 040dc40d-084c-3dd3-ac62-891f900ac7e9 | -10.5051 | -47.5845 | 2025-06-21 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 981d9022-717e-348a-95b7-dcd14925b89a | -7.0672 | -43.4344 | 2025-06-21 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 88.0 |
| ec2a7a35-5f03-3015-9fa1-76b4e4a7a032 | -10.883 | -56.4567 | 2025-06-21 13:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 71855182-b8a8-3a4a-bd2a-77c6b7183b17 | -10.9018 | -56.4552 | 2025-06-21 13:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 140.3 |
| bab19aed-f709-36b4-b70c-f0171ad8d67b | -7.216 | -43.5836 | 2025-06-21 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 05e1cacd-f494-31df-966a-ad14267ae0d7 | -7.2163 | -43.5603 | 2025-06-21 13:40:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| df87618e-14bd-3389-95a3-595b1153785e | -10.876 | -53.7614 | 2025-06-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 1474d330-17de-3c52-9005-dc029dc8ceaa | -11.798 | -57.243 | 2025-06-21 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 209.0 |
| 4af2eeeb-35a6-32b6-bdd1-8009be95648a | -10.8571 | -53.7631 | 2025-06-21 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 193c7406-549c-3be8-850b-1127e094c1c7 | -10.8828 | -56.4767 | 2025-06-21 13:40:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 3887d394-acb3-3fa0-9c98-5a7aa0307503 | -11.5779 | -44.8413 | 2025-06-21 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 136.3 |
| bf887c23-e8f0-3bae-888a-b658ba508615 | -11.7791 | -57.2445 | 2025-06-21 13:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 28db70df-2147-3eaf-af76-a037729c2a74 | -8.5724 | -51.5552 | 2025-06-21 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 330543d8-8bf6-3474-92ed-4230c61fb14c | -10.883 | -56.4567 | 2025-06-21 13:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| df9ba9e2-e8a9-39a8-977e-06d26c17646a | -8.1827 | -47.7821 | 2025-06-21 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| fe1f3d73-7263-3654-b500-e61214bf2768 | -8.5911 | -51.5537 | 2025-06-21 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| e2dabe84-eef4-35ab-af4d-0d87e42021da | -11.7983 | -57.2231 | 2025-06-21 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 910e93b7-fc48-3345-bd43-5cd93370c20d | -7.2163 | -43.5603 | 2025-06-21 13:50:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 94.7 |
| 7c476a49-ee6f-34c4-bcd6-f22e5d0b6dd4 | -10.8571 | -53.7631 | 2025-06-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| f09b48cc-04b9-3d07-9a38-2ab427dffea2 | -10.5241 | -47.5822 | 2025-06-21 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| bf9ae7f4-6dd3-3caa-87f1-520b54c7e52a | -10.9018 | -56.4552 | 2025-06-21 13:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 1e23789a-71e0-3755-a06b-3b800c403b53 | -11.7791 | -57.2445 | 2025-06-21 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 150.0 |
| fb501a2c-cf74-33e4-b07a-45d30c1081b9 | -11.798 | -57.243 | 2025-06-21 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 196.3 |
| 6f823d63-7737-372d-b314-93a4087639a0 | -4.5429 | -48.0151 | 2025-06-21 13:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 93b6a0b3-2132-342f-b88b-415f9685e151 | -11.7794 | -57.2246 | 2025-06-21 13:50:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| dfbeed1e-4281-3648-93ce-517bba44cae3 | -11.5779 | -44.8413 | 2025-06-21 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 144.3 |
| f6a5792b-aeaa-3399-a9d2-f3499791fee4 | -10.876 | -53.7614 | 2025-06-21 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 9a835500-46d1-363e-ad11-00b7d364bfe1 | -12.58 | -58.3927 | 2025-06-21 13:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 879b975f-cd01-3a67-a675-2eae5e3a311e | -10.8828 | -56.4767 | 2025-06-21 13:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 247.4 |
| a45ec7a4-2226-3806-855a-ba8823280d90 | -11.798 | -57.243 | 2025-06-21 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 225.5 |
| 1acd2b92-e71c-322f-824b-13d064897365 | -10.8828 | -56.4767 | 2025-06-21 14:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 232.8 |
| 49f3bc8a-b795-3fc7-b179-72f17f26086a | -4.5429 | -48.0151 | 2025-06-21 14:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 56d7e9de-f8c9-314a-9141-a084e4cbd0a2 | -11.9436 | -51.76 | 2025-06-21 14:00:00 | GOES-19 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 133.3 |
| b3df33a8-1685-3b97-bc36-52dac67d6a65 | -10.876 | -53.7614 | 2025-06-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| c86b68af-58f1-333d-abfd-f3ee112642f2 | -10.9018 | -56.4552 | 2025-06-21 14:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 150.2 |
| b78d6421-2840-39b5-bbcb-b5857093f4aa | -9.9126 | -52.4427 | 2025-06-21 14:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 2c6777e1-1cc3-390e-9377-635605369629 | -7.8814 | -47.8964 | 2025-06-21 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 754a89d8-46e3-3c24-b77b-ec9fd81daaee | -10.5381 | -46.6445 | 2025-06-21 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 16851e8b-94af-3d33-ad4f-c6cd0eef3c75 | -7.2412 | -44.6897 | 2025-06-21 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 6c98d44a-c426-3f45-9fe6-5ba7222794fc | -10.883 | -56.4567 | 2025-06-21 14:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 151.3 |
| b0638e75-13a0-376f-a042-f4acad3c4bea | -10.8571 | -53.7631 | 2025-06-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 8a8cae0c-0fce-311a-867e-9c417d01a631 | -11.7983 | -57.2231 | 2025-06-21 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 913a8ca7-19af-306a-8a06-c1df9cdaaf89 | -7.216 | -43.5836 | 2025-06-21 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 103.9 |
| dada392c-d0ef-386c-9c67-e70788cb4bb5 | -10.5051 | -47.5845 | 2025-06-21 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 4a2606c0-671b-3a0e-a475-b66c912ff02d | -7.2163 | -43.5603 | 2025-06-21 14:00:00 | GOES-19 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 81.7 |
| b18d48eb-6525-3bb2-bbab-c5a4f5172cd2 | -11.7791 | -57.2445 | 2025-06-21 14:00:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| 47dd1ef9-b527-3b6d-9d7f-a887a688ab22 | -8.2015 | -47.7804 | 2025-06-21 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 293adb06-f249-3bda-beb4-ee76d56e6489 | -8.1827 | -47.7821 | 2025-06-21 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 92e68da7-00e8-3494-b300-b6e3f4c0f9fb | -11.5779 | -44.8413 | 2025-06-21 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| aa1b48a1-469f-3011-98e2-45354e4e4f9d | -9.4648 | -57.8449 | 2025-06-21 14:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 9c8a678d-2b45-3575-8247-9092c3e282b4 | -7.8814 | -47.8964 | 2025-06-21 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c2d899a1-ba36-337f-a3bb-8315f91cbb0d | -8.5724 | -51.5552 | 2025-06-21 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 58aafb12-dfc1-3fac-899a-a5009fd9c84d | -10.8828 | -56.4767 | 2025-06-21 14:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 252.8 |
| 31e3c868-1592-3a03-9041-242a349bafb0 | -8.2018 | -47.7585 | 2025-06-21 14:10:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 79566b4d-d697-3731-b736-7934cd840a48 | -11.798 | -57.243 | 2025-06-21 14:10:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 267.9 |
| 7e010d7a-1a40-30fc-b398-aa56804975bb | -10.8571 | -53.7631 | 2025-06-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 1373c2a9-f137-3c11-83a9-22310c46f5c9 | -12.5802 | -58.3729 | 2025-06-21 14:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |


[Clique aqui para ver as próximas entradas](README31.md)
