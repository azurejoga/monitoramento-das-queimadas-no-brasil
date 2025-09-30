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

## Dados Diários - Página 122

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2976a149-6e8f-30e2-9575-700d4c3e6a11 | -9.0425 | -46.7032 | 2025-09-30 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 5f5e5593-84ca-37b9-afca-eb77d0c2b740 | -10.6612 | -48.578 | 2025-09-30 14:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| f63bfad5-0516-3ed3-8dd8-c57a7930c021 | -9.7681 | -46.1519 | 2025-09-30 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 3fc39e84-eaec-3e8f-be3e-0eef96764d3a | -9.4009 | -54.6781 | 2025-09-30 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 3ad7db54-3eb7-38ec-a710-4553f261f03a | -15.1882 | -52.8215 | 2025-09-30 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.0 |
| dd94e71b-889d-3a4a-8acb-608ac3395909 | -17.7149 | -46.6631 | 2025-09-30 14:20:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 166cb66f-dad0-3831-8d7e-457454733dad | -12.4058 | -50.1708 | 2025-09-30 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 244.1 |
| 6c0cab23-1d02-311d-915f-3f9eceda5b6d | -9.4206 | -54.5753 | 2025-09-30 14:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 205.8 |
| 9216fedb-e6db-3106-a1cd-bf6ef7e9f010 | -9.0682 | -47.6313 | 2025-09-30 14:20:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 077fa44f-62b3-3f54-a0ff-3b769e30ef7b | -12.952 | -48.4185 | 2025-09-30 14:20:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| a0ae9cff-3561-3868-bab7-ef9ac3789d94 | -14.0412 | -45.001 | 2025-09-30 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 4170ea19-93fd-3881-b5bc-58ba1931ab42 | -8.874 | -46.6092 | 2025-09-30 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| c7c7f11e-0363-347b-bf85-4c39243cbae0 | -15.2746 | -49.263 | 2025-09-30 14:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 275.8 |
| 278738c2-e9c5-39fc-b818-438a6f4bc0cd | -5.4565 | -43.0554 | 2025-09-30 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 135.3 |
| d42d51d9-fc1d-3614-a229-bdafe7185886 | -9.8848 | -45.9349 | 2025-09-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 0cf91248-5140-3a7d-8bfd-1eb6c2ca8fe1 | -11.7537 | -46.8461 | 2025-09-30 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| faa164c0-3bfd-361d-ac4a-3e2fd1ce742c | -7.819 | -46.7561 | 2025-09-30 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| c8590a04-6a8d-393d-9327-c9f3f84e7a6b | -6.504 | -45.2312 | 2025-09-30 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 96e907cc-46ae-37ad-8011-97a83f3a416d | -6.2996 | -45.066 | 2025-09-30 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 53334055-0101-338d-b3d5-bd8179be7966 | -5.6815 | -43.0384 | 2025-09-30 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 95.9 |
| a0a2a723-ced0-32f7-8225-d07dd23cffe9 | -7.4414 | -46.9888 | 2025-09-30 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2dd5dd58-f43a-349e-93f9-e1fcc2939459 | -12.952 | -48.4185 | 2025-09-30 14:30:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 92d12023-6216-314d-9613-d7136d2b1482 | -11.1944 | -47.2334 | 2025-09-30 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 77efff4e-7eea-3b9f-af08-0b76275b75eb | -11.4608 | -44.9739 | 2025-09-30 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.5 |
| cdb906ab-f1eb-3723-94dd-2fdc325fbb2e | -6.098 | -42.6521 | 2025-09-30 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.2 |
| cf97abd4-ec23-3a61-a8e5-0e3c2649c864 | -15.6272 | -49.1837 | 2025-09-30 14:30:00 | GOES-19 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 130.3 |
| e24208bf-8795-3c37-baff-38a252c8741e | -9.9581 | -43.5987 | 2025-09-30 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 7144b4cc-44d7-30f8-b5b2-454d1317a959 | -6.5042 | -45.2085 | 2025-09-30 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 052f0dcb-7ba5-3543-aa7d-42ea7e5cf30f | -12.8774 | -45.1742 | 2025-09-30 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 01a7aa5c-39eb-345f-9647-6b163ff746b8 | -12.7022 | -45.2715 | 2025-09-30 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 6bdea614-569d-3431-991e-0dcfa81bde62 | -9.1246 | -47.6476 | 2025-09-30 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 5c915ccb-231e-3418-8142-aacdf85661ce | -7.5146 | -45.4385 | 2025-09-30 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| eabe3be1-aa27-3e92-8726-a46863d97985 | -10.0531 | -50.1978 | 2025-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 206f9b77-e176-364e-8ae7-c83272ac78dc | -15.1684 | -52.8453 | 2025-09-30 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 6725d033-dd0c-320b-b667-88d802483794 | -5.8632 | -45.7532 | 2025-09-30 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0db0f69a-088a-3990-bd5e-1a25e0b0a854 | -5.8445 | -45.7545 | 2025-09-30 14:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 930cee7d-7270-34aa-9472-8f34ce906f0f | -15.758 | -54.6793 | 2025-09-30 14:30:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 58.9 |
| d536278c-6624-3e2f-a018-75bd6aa6fe61 | -8.541 | -44.6515 | 2025-09-30 14:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 62f2cd8f-355a-38b4-9e8c-dfceb2171618 | -12.8823 | -46.9554 | 2025-09-30 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| f592291f-8c7f-335d-84e0-1d1dc83687b9 | -5.475 | -43.0774 | 2025-09-30 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 545.4 |
| e9b063b1-c925-3087-a06c-8e47eb0476d1 | -8.8516 | -51.6998 | 2025-09-30 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 888a3390-5eab-31ae-983f-93fd8e5a5215 | -15.9076 | -46.2139 | 2025-09-30 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 185.6 |
| 8aad1418-1f9b-3214-ad06-9cbc776ddda4 | -10.6423 | -48.5802 | 2025-09-30 14:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 44f72169-5dde-33da-a478-9afea9e03716 | -15.7917 | -43.6672 | 2025-09-30 14:30:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 351.9 |
| a2423e2a-78f2-3a37-aff0-aec36eead1d5 | -16.0779 | -51.0424 | 2025-09-30 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 86.5 |
| be00e882-b9e9-3a43-987b-ea1380c52dbe | -9.8845 | -45.9576 | 2025-09-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 214.1 |
| af828a33-38db-3d10-b72f-23b97ad69b18 | -5.7413 | -42.6576 | 2025-09-30 14:30:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 105.8 |
| 57a7e7a0-29fc-3576-acdc-04bab135f65d | -6.523 | -45.207 | 2025-09-30 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| e3624393-ff2e-369a-8011-fac9031469fb | -14.7361 | -45.2489 | 2025-09-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 185.9 |
| 0a1bf2fc-d4f0-32a7-ae2b-c7f19f739c8b | -15.4835 | -45.9006 | 2025-09-30 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 130.5 |
| d587199e-0132-3011-a5c1-83c39494f31f | -12.2153 | -47.8112 | 2025-09-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 200.0 |
| 26641aa1-10a9-34ac-86ad-91cd4d1e3bef | -17.7149 | -46.6631 | 2025-09-30 14:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 1e5ccc64-f034-35a5-93eb-c63fbf8c6f26 | -9.9585 | -43.5752 | 2025-09-30 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| 3698126a-d827-3f49-9368-c30ffba68aeb | -12.4058 | -50.1708 | 2025-09-30 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 223.9 |
| 30774af6-a21b-3b34-bca0-f2e1cab51fdf | -12.2348 | -47.7863 | 2025-09-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.7 |
| c84f39bb-db9e-3fbf-b02f-da55d50aab21 | -7.0478 | -45.2083 | 2025-09-30 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 0424752f-471c-366b-9528-a99f0eca129c | -11.1548 | -54.1054 | 2025-09-30 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 8afc8182-d890-33f2-86ec-c7079204d094 | -7.8188 | -46.7783 | 2025-09-30 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| f7d01fc1-4836-313e-9106-0259d0682be5 | -9.3206 | -45.6834 | 2025-09-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 7be37937-2899-36bf-8644-33229f326cc7 | -11.7984 | -47.6003 | 2025-09-30 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 028ede28-6502-3a8f-b3ff-f7adacb49411 | -7.4758 | -47.2728 | 2025-09-30 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 1405b2cc-d313-3e88-af65-cd65b0a9313f | -18.1977 | -53.3208 | 2025-09-30 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 67485fc2-fc3d-3f4c-9f13-affcc5e8279d | -5.7411 | -42.6812 | 2025-09-30 14:30:00 | GOES-19 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 254.3 |
| bb5b1e11-ca04-3888-8c59-1946e33205d5 | -8.2662 | -45.5018 | 2025-09-30 14:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f762e5b6-6fae-3bab-892a-bc97524bb38e | -10.0342 | -50.1997 | 2025-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 159.5 |
| b0a4185a-f155-39ac-a53e-6558a04ad799 | -7.938 | -44.6226 | 2025-09-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 8dc2df58-8517-36db-9753-ceffb1051cd7 | -18.4862 | -44.0191 | 2025-09-30 14:30:00 | GOES-19 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 45f23e1d-3c77-3021-9784-024d1ebf2c7f | -10.0339 | -50.2211 | 2025-09-30 14:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 228.5 |
| 82311ea2-e76c-3681-88aa-79703aeb9ca4 | -7.8375 | -46.7766 | 2025-09-30 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 29419b2b-3b6c-3cf1-9d36-6a0949b07e7b | -7.835 | -46.9986 | 2025-09-30 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 3fb4e658-4ae8-3869-ac47-1f7249d450b9 | -7.4131 | -44.4443 | 2025-09-30 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 70e3509f-bfa3-39ad-a36c-d9ee3a022294 | -5.7698 | -43.638 | 2025-09-30 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 113.0 |
| a58dad4f-1e0b-3972-955c-caebc2486f68 | -12.2344 | -47.8086 | 2025-09-30 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 280.0 |
| ea2b859d-7558-3969-b45c-188b4d6ba881 | -8.1428 | -46.3693 | 2025-09-30 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| ed2a0abf-952d-363b-bd7e-04845397e4ed | -9.3202 | -45.7061 | 2025-09-30 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b11094fe-3486-3a44-9365-bf9c5b6298ed | -11.8868 | -48.0323 | 2025-09-30 14:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 8bdc350b-acf9-3454-92e2-f6ad0b2cb7f7 | -15.9273 | -46.2101 | 2025-09-30 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 294.9 |
| 35e50bf0-2167-300a-ab51-4c6b8aeca33b | -14.7367 | -45.2255 | 2025-09-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 617ea100-0590-3ec7-b881-bbe12b42cbcf | -7.6272 | -45.4507 | 2025-09-30 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ba39abde-1d3b-3a56-ac23-c449e7ce7df9 | -15.7719 | -43.6714 | 2025-09-30 14:30:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 914.3 |
| 1e7663cc-5ff9-34e8-863e-6c6a93cbc468 | -9.7681 | -46.1519 | 2025-09-30 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| afa4d89a-457a-3d6f-9cda-0231bc0af890 | -7.8696 | -47.2606 | 2025-09-30 14:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 214.4 |
| c9ef895f-e1b8-3b82-8a9c-dff1c4b20fa0 | -10.1855 | -44.8709 | 2025-09-30 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 177.1 |
| 395e5fa9-6a67-3b76-b4f2-9163e68336b5 | -7.0481 | -45.1856 | 2025-09-30 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| b9498b32-d984-3a36-b981-870bbf3bc54e | -6.8148 | -45.9947 | 2025-09-30 14:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 4619c06d-9613-35a0-9940-a5324f970056 | -9.0685 | -47.6093 | 2025-09-30 14:30:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 7bcd8bcb-887e-3f80-b650-7af9b5ed7e06 | -18.2176 | -53.3177 | 2025-09-30 14:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 276.2 |
| 34d4cf2b-9f90-3111-a05a-006119fb3ac9 | -18.2171 | -53.3392 | 2025-09-30 14:30:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 54bfa122-bb14-3c0b-b167-3b4c611ff6c7 | -15.2746 | -49.263 | 2025-09-30 14:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 08c10cf8-26fb-3706-933d-2cc99a59d6a2 | -5.6813 | -43.0619 | 2025-09-30 14:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 76.7 |
| bb8d1398-0fc8-380d-95c1-e2ae32ead66c | -7.8378 | -46.7544 | 2025-09-30 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 16074286-535d-3f49-9b05-4cdad2f24668 | -7.8538 | -46.9969 | 2025-09-30 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 596cf845-e845-300d-b5b8-0f1162208e5a | -15.9071 | -46.2371 | 2025-09-30 14:30:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 242.0 |
| 0a02c1df-3e11-3b47-bbf3-e90891f6f4d4 | -16.7575 | -51.3482 | 2025-09-30 14:30:00 | GOES-19 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 5c4e6ea1-a225-33e2-ae0e-ddc96e5b1a2b | -8.1616 | -46.3675 | 2025-09-30 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 474f0fb4-15c7-3e35-b395-b38d9b1b5283 | -18.1583 | -53.3055 | 2025-09-30 14:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 82ec5592-4c3a-356d-8055-dd501076e01f | -14.7166 | -45.2525 | 2025-09-30 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 296.3 |
| d4332ac8-a59f-3f77-b0a6-e64099c51e39 | -7.0291 | -45.21 | 2025-09-30 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 67da337b-219a-33c7-bb22-0ed1a0fc28a8 | -10.1045 | -47.7851 | 2025-09-30 14:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 341.6 |
| de0749df-73dd-3216-878d-0923eb691bed | -6.2142 | -44.2041 | 2025-09-30 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |


[Clique aqui para ver as próximas entradas](README123.md)
