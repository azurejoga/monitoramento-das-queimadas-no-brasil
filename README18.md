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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d55553eb-e2a2-37e6-8e74-4153e80abacd | -3.1471 | -54.0849 | 2026-10-01 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 73e1b09d-aeb1-3f71-ad7d-11d2039f58a1 | -11.4503 | -43.4091 | 2026-10-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 6320816c-252d-3c73-8a9d-146738a710cc | -11.4687 | -43.4537 | 2026-10-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| f7f14edc-5516-3d68-9cdc-d082be65dc4f | -3.106 | -50.2896 | 2026-10-01 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 7e13309d-0a8f-3bb3-89ca-199c165f9160 | -11.4499 | -43.4329 | 2026-10-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| aa81588e-37d7-34ba-8744-9d101fb7186f | -13.6479 | -53.9336 | 2026-10-01 03:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 2f91d14e-c11e-3a0c-807c-89eaa63230a7 | -5.7357 | -43.2682 | 2026-10-01 03:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| b991979f-dd87-34c2-8f94-aee126c14740 | -9.0046 | -65.6988 | 2026-10-01 03:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| c4daadc3-d0ec-396a-b09f-82fd5b6a415b | -11.4691 | -43.4299 | 2026-10-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.1 |
| fb3db1e2-91d8-3693-a8f0-bc7e77174e7f | -14.4031 | -51.265 | 2026-10-01 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 9b375a23-ca0a-30b0-9778-4df56cd5f606 | -5.7563 | -45.152 | 2026-10-01 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 5dff9b14-11f4-3515-af42-b7eed5625973 | -1.9003 | -45.8043 | 2026-10-01 03:10:00 | GOES-19 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 470513fc-69dd-3ba5-a1ff-af97ae4e40cc | -14.4027 | -51.2865 | 2026-10-01 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 04c22e8d-21d0-3647-8926-85cabbbdd0b0 | -3.1061 | -50.2686 | 2026-10-01 03:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| eb5282c7-5a46-35c4-8835-7d2cf1f069e3 | -3.1838 | -54.104 | 2026-10-01 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 203.9 |
| 406cff6f-cba0-35c9-b237-0e3b37d36f26 | -14.4225 | -51.2624 | 2026-10-01 03:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.8 |
| f146c6bf-7ba0-3e41-9b89-44af26ad113b | -14.8762 | -51.8427 | 2026-10-01 03:10:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 05576f57-8105-3529-990a-d779a3b86c26 | -3.1655 | -54.0844 | 2026-10-01 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 149.7 |
| e80fd80b-ea93-35cd-bcb9-aff5c463049e | -12.1857 | -48.4345 | 2026-10-01 03:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 07040657-e0e5-3e61-a348-9e98faaf5145 | -11.4495 | -43.4566 | 2026-10-01 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 188e4937-fd1a-3ab1-b4a8-a3831be300b0 | -11.2903 | -50.9846 | 2026-10-01 03:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 50fbc7cb-1c15-33a0-8b67-152d0f1ec38c | -3.1655 | -54.1045 | 2026-10-01 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 196.7 |
| 7bbab245-1f50-385e-80ae-405b0795d135 | 3.2742 | -60.6105 | 2026-10-01 03:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.0 |
| c18e3f5f-559b-37d9-a9c0-04b66d241d16 | -13.1156 | -51.2193 | 2026-10-01 03:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.1 |
| ec2743a6-30a7-3b1f-9150-bd9d7a05374f | -11.45 | -43.44 | 2026-10-01 03:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98ed9867-9438-31db-b381-d74834906748 | -4.29 | -50.81 | 2026-10-01 03:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23676dcd-65e6-39b5-bd1e-c23b2b9675c1 | -4.26 | -50.75 | 2026-10-01 03:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e398cb6e-ce30-3f2d-aa5c-875bb1f786e1 | -4.29 | -50.76 | 2026-10-01 03:15:00 | MSG-03 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b8a71bb-c80c-3bc3-b552-3f26d86f4d0b | -4.26 | -50.81 | 2026-10-01 03:15:00 | MSG-03 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0594f7b2-ab6a-3cc5-9ba8-414453bb628d | -13.6479 | -53.9336 | 2026-10-01 03:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| b24c0ca9-b306-39fd-a7e9-ea34c2212343 | -5.7376 | -45.1533 | 2026-10-01 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 987ed012-1bb2-398e-a261-31a9217b1428 | -3.1839 | -54.0839 | 2026-10-01 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 7276c352-bd48-3ef4-ab6d-8c5fdcc51a93 | -3.295 | -53.8597 | 2026-10-01 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| f775e192-da15-3176-a3f3-09fe2567c8bb | -3.1245 | -50.289 | 2026-10-01 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9dc3e6c1-dc9d-3e88-9ecd-205674144abc | -11.2903 | -50.9846 | 2026-10-01 03:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 7a1af0b9-4171-3192-aaf0-756d700fecff | -11.4499 | -43.4329 | 2026-10-01 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.7 |
| 77cc6e95-ec6e-37a4-b4c4-b68c606108d0 | -5.7355 | -43.2916 | 2026-10-01 03:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 7ae6e1ef-0bee-39c4-85e0-daeb01dd62e4 | -3.2022 | -54.1035 | 2026-10-01 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 10502230-82f3-3d29-8525-2450f3c46002 | -11.4687 | -43.4537 | 2026-10-01 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 7cba6ac2-7578-3ef4-bd98-bd7c38edaa6e | -11.4495 | -43.4566 | 2026-10-01 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 2f4e91d0-8dbd-3a38-9e63-f6d42f6a5b2c | -5.7563 | -45.152 | 2026-10-01 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.6 |
| a8d37a53-8551-36ae-bce2-65398449b055 | -11.4691 | -43.4299 | 2026-10-01 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 0362afcb-9526-37d3-b923-b22adbd6bab9 | -11.4311 | -43.4121 | 2026-10-01 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 6758069e-0795-3038-b3b5-2446adca40a7 | -14.4031 | -51.265 | 2026-10-01 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 142.6 |
| f8c5f25a-d1a9-32b9-bd4d-982e3f453ea9 | -14.4225 | -51.2624 | 2026-10-01 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 339327ed-4faf-379c-b6ae-0184a3f1ff50 | -3.1838 | -54.104 | 2026-10-01 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 275.4 |
| a592ea16-33e3-304b-b496-ce3baa7de661 | -12.1857 | -48.4345 | 2026-10-01 03:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 160.8 |
| a48f44f2-720e-3444-90f3-39751a33af3a | -5.7561 | -45.1747 | 2026-10-01 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ee1ce0d6-b90f-3d05-bcdd-0e3b14490ec1 | -13.1156 | -51.2193 | 2026-10-01 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 4ed88192-1560-34c2-802e-3e8a15a46c5e | -3.1838 | -54.1241 | 2026-10-01 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 421da73d-49d3-3c44-9c34-efb93c2e88c6 | -3.1061 | -50.2686 | 2026-10-01 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| b965d1d2-3015-370b-b081-8aceb54a0dc5 | -14.4027 | -51.2865 | 2026-10-01 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 15af98ee-be76-3241-9861-9abc9f79dad6 | -3.1655 | -54.1045 | 2026-10-01 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 226.3 |
| 3df3d160-2de2-3703-b83d-6abd8fe6571c | -11.4503 | -43.4091 | 2026-10-01 03:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 917d4029-fed1-33bb-ba85-98d362ab5e78 | -3.106 | -50.2896 | 2026-10-01 03:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| d96c50f5-2e43-38bb-9ebf-e4e6de1a9b96 | -13.116 | -51.1979 | 2026-10-01 03:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| d1e9f7fe-26c8-3561-b9ad-a2353f8ba605 | -3.1655 | -54.0844 | 2026-10-01 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 134.5 |
| 90620f15-b5d5-3801-8b63-f96db3ed08bb | -13.6671 | -53.9314 | 2026-10-01 03:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 349f8575-cfee-395f-aaa7-4913608b9097 | -11.4495 | -43.4566 | 2026-10-01 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 80a34955-40a3-3c23-8027-b55cc352413a | -14.8762 | -51.8427 | 2026-10-01 03:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 09f26712-72df-352a-af7a-f28716b5ae33 | -11.4687 | -43.4537 | 2026-10-01 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 0f4eaf54-929e-3dbb-a68e-b4cb44bf277d | -3.1838 | -54.104 | 2026-10-01 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 203.2 |
| 9d5fe74a-de23-3553-88b4-9f78c9ab262e | -14.8758 | -51.8641 | 2026-10-01 03:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 144.6 |
| 277b9d62-306f-3efa-b372-9fbea6bac278 | -3.295 | -53.8597 | 2026-10-01 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7a10c1a5-bb66-31d8-aa3a-4dd0613d009a | -11.4503 | -43.4091 | 2026-10-01 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 18c7559a-1a59-3ebd-9b8b-ca4eeaf57bfd | -5.7563 | -45.152 | 2026-10-01 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 7c517dc9-7bbf-350e-9cea-dde9cc0b0e1b | -12.1857 | -48.4345 | 2026-10-01 03:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 44036b57-5038-3bba-940d-252b3b2b0b4f | -5.7376 | -45.1533 | 2026-10-01 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d26e43b1-30b2-3f65-94d5-77da6f4d4053 | -3.1838 | -54.1241 | 2026-10-01 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4d7591b0-619c-334d-a989-3d8698029c3e | -5.7542 | -43.2901 | 2026-10-01 03:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 9b1c0ec9-1440-3414-b7a0-aa21efb0b9df | -14.8952 | -51.8615 | 2026-10-01 03:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 4b720b9f-00c4-3667-8291-bb1a70fdfd58 | -14.4225 | -51.2624 | 2026-10-01 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 833bbd8c-fe8c-3c2f-b13d-498e6df3c38d | -3.1061 | -50.2686 | 2026-10-01 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 633f341e-1aa2-39b0-9188-2fdfb84e9c72 | -3.1839 | -54.0839 | 2026-10-01 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 7a69b3f8-779e-3613-a20b-01b36c30b59b | -10.7853 | -50.5279 | 2026-10-01 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| e9891428-de54-37b8-aeeb-cd2e14959f62 | -3.2766 | -53.8602 | 2026-10-01 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| cbb04c75-f2bf-3eec-885e-112254ea87dd | -3.1245 | -50.289 | 2026-10-01 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 2b3284f4-3786-3d69-ba63-66fef8b3a7a9 | -11.4311 | -43.4121 | 2026-10-01 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 8fdec314-cd51-3ec6-8e09-612647f78290 | -14.4228 | -51.2409 | 2026-10-01 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 101.7 |
| dd2c8d11-d229-369c-bd0c-3aca23d424b0 | -3.106 | -50.2896 | 2026-10-01 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| fa83669b-1c89-3586-bfa0-63ac09a36668 | -8.5554 | -66.9945 | 2026-10-01 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| fa1f63e3-43dd-3317-b3e5-2c54f11896cb | -13.6479 | -53.9336 | 2026-10-01 03:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 1093e6d8-199c-34f1-a59a-11ebbde59781 | -14.4035 | -51.2435 | 2026-10-01 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 107.4 |
| f749c997-42ae-3a30-9cdf-bd6ed8d0791a | -5.7561 | -45.1747 | 2026-10-01 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| de445071-e302-3783-989e-02f970721693 | -5.7355 | -43.2916 | 2026-10-01 03:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 04e236cd-e65f-3624-8d0f-6c491cea8e78 | -14.8949 | -51.8829 | 2026-10-01 03:30:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 117.9 |
| d80e1165-d562-395f-9b52-198733b500c1 | -3.1655 | -54.1045 | 2026-10-01 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 190.7 |
| 50ff7610-c657-336c-aa63-594e04c7c36f | -3.1654 | -54.1246 | 2026-10-01 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| d813bf15-ab4a-35ee-876b-20b5d0634de1 | -11.4499 | -43.4329 | 2026-10-01 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |
| ae3744c8-2b4a-3272-bf93-9d9c751044d6 | -13.6671 | -53.9314 | 2026-10-01 03:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| eba2c4e4-10cc-3c96-ac25-9c5dcb44bc22 | -13.1156 | -51.2193 | 2026-10-01 03:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.6 |
| ce30538e-7a0a-3bee-92d8-9bff5a1e3841 | -14.4031 | -51.265 | 2026-10-01 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 216.6 |
| eb1f5cb3-db54-304d-a0f1-2dc46a53c6be | 3.2742 | -60.6105 | 2026-10-01 03:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| a1ee6fe2-ef6b-3292-9800-f5f6747825bd | -11.4691 | -43.4299 | 2026-10-01 03:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 04f9d31b-6b1e-35b2-b763-157b87291bf4 | -14.4027 | -51.2865 | 2026-10-01 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 9f34f747-4303-392c-b65e-88c0089e21dc | -3.1655 | -54.0844 | 2026-10-01 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| c62228f6-6df3-3d2a-bd18-e12e53efc4fe | -12.1853 | -48.4565 | 2026-10-01 03:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 69985df3-57d0-3178-99e2-b4997626adb8 | -7.07126 | -42.325 | 2026-10-01 03:36:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3073b538-d35b-33a3-8d6c-d6ab646eb81c | -1.91075 | -45.81003 | 2026-10-01 03:36:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| da40a30b-b8e1-3ee5-985e-8df3964eafbe | -5.10289 | -45.66822 | 2026-10-01 03:36:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README19.md)
