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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f1f03f5f-830b-347a-af53-b5fdcaf4bc31 | -19.59416 | -47.61994 | 2025-07-08 04:19:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 723b38c4-d1f5-3fc2-9766-a93c0c2d649b | -19.43785 | -44.34027 | 2025-07-08 04:19:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 287129fb-7f67-3fce-bfb5-29fdde1e023d | -17.67559 | -52.90455 | 2025-07-08 04:19:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0a48a1b-c484-36b3-b75a-84e88fd1fa3b | -23.55633 | -54.79978 | 2025-07-08 04:19:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 83c483c9-676c-3d86-a1a3-b9db66dce3f7 | -11.4201 | -45.1181 | 2025-07-08 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 9fd07550-ba3b-32f5-87c5-363ef03af842 | -11.4397 | -45.0923 | 2025-07-08 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 35f3c4bc-5103-3650-917a-5148218fcbfd | -10.6489 | -49.4483 | 2025-07-08 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| e3ffbfa1-8e55-3f62-abdf-32b02d92b660 | -10.6486 | -49.47 | 2025-07-08 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| d5c894f7-8e26-318a-99b4-9b6db189baa9 | -11.4393 | -45.1154 | 2025-07-08 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 16715393-dab4-3445-8c6c-af7da6459944 | -10.6299 | -49.4504 | 2025-07-08 04:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| d8093b23-6b63-34f8-bf76-a7108e7c1f13 | -11.4205 | -45.095 | 2025-07-08 04:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 52b06f03-c442-39ee-b04c-77e8ec1c17c4 | -11.4201 | -45.1181 | 2025-07-08 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 015bc78f-579c-306c-bf11-f0aa9d78e22e | -11.4393 | -45.1154 | 2025-07-08 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| d70bda1b-3bf2-36c6-b0d8-cece90d1bab6 | -11.4205 | -45.095 | 2025-07-08 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 3d12cfbc-96ff-35fe-983c-f9583b5af07c | -10.6486 | -49.47 | 2025-07-08 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 5b333824-d240-3aa1-a223-1a4d89b0d553 | -11.4397 | -45.0923 | 2025-07-08 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 439a589a-89f4-3543-8d22-6c23781f3fb6 | -10.6299 | -49.4504 | 2025-07-08 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 7b33d99f-cb2a-3e03-b0b9-ef16b0812949 | -10.6489 | -49.4483 | 2025-07-08 04:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 646bc8e0-da91-3695-a93d-43241f76d884 | -11.4393 | -45.1154 | 2025-07-08 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| e7f086a3-a6da-3ca9-8185-f883787485c3 | -11.4397 | -45.0923 | 2025-07-08 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 99f0e444-6900-3f95-b0c4-a6a380b06bce | -11.4201 | -45.1181 | 2025-07-08 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 048e8ba7-a4dd-36c6-a40d-14f560c632b3 | -10.6486 | -49.47 | 2025-07-08 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 11ebc62b-08ca-3aab-b5d5-86d84422a663 | -11.4205 | -45.095 | 2025-07-08 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.6 |
| cd0918d3-e270-3726-bd56-fc72dec9ed21 | -10.6299 | -49.4504 | 2025-07-08 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b3bc0dbb-5e78-339e-8c0f-da90f392ab22 | -10.6489 | -49.4483 | 2025-07-08 04:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c9962b2d-3d4e-3c81-915c-48d168c7a9ea | -6.49726 | -43.64468 | 2025-07-08 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12642546-65fa-37ee-bce1-5aa28b1ef5ae | -7.22133 | -43.11868 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0233e8e3-953f-3775-84d8-397f5571b2aa | -8.22351 | -44.93157 | 2025-07-08 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b3103284-f02a-3928-bc2f-a5924e818847 | -6.86148 | -44.06633 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3fb31ee5-d409-31bd-b2b9-086c475da636 | -6.52925 | -43.54284 | 2025-07-08 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d89394ee-74d1-3c7b-b302-c874b9b35caa | -4.27861 | -48.18923 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 24ff37b3-86e4-321f-b550-90c5280e34b8 | -4.32167 | -48.38845 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2599573-7e86-3293-8fe7-21c66327915c | -7.63757 | -45.3597 | 2025-07-08 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dcc20e3-1dcb-3af3-ba1c-31dd7d1c8cbf | -6.68244 | -43.76613 | 2025-07-08 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7df87ee-9646-33cd-bf7e-fe51ad19674e | -7.67157 | -44.35064 | 2025-07-08 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caab70ac-dfc3-3c46-aeda-e2ac59e3c354 | -7.25211 | -43.08036 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ec06a19d-804c-3113-a784-1ce91fb95388 | -7.10531 | -44.17062 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f9dadfe-007f-3849-beed-51a9063845ad | -6.53412 | -43.53946 | 2025-07-08 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33ccfc1c-bf7e-31d5-ba2c-6b00ea498ef5 | -6.67818 | -43.76557 | 2025-07-08 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1c245cb-b4b1-31af-a4ff-96e1d7160a5b | -6.84245 | -42.84662 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 021ba6ec-4aff-3b19-a709-4363a02d4010 | -6.35022 | -46.36494 | 2025-07-08 04:40:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 461ab519-ee88-3a0b-8e87-224a8016aa2b | -7.19641 | -43.13302 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b19037ec-c4a6-38c9-93d1-e74dc8930794 | -6.26418 | -45.27293 | 2025-07-08 04:40:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b1581eb-0145-3a1f-838e-cb2a6c8ded6c | -8.04088 | -49.88533 | 2025-07-08 04:40:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0c80597-2d92-3aa4-9c2d-559b6c0f1ff2 | -6.89095 | -47.40017 | 2025-07-08 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de0d6681-9839-310f-b831-dd30a2c2fa44 | -4.42357 | -48.14387 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1f3e1f1-d4fa-39f7-809c-9356ea554903 | -6.6691 | -43.76836 | 2025-07-08 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7226b7c1-3bb2-360c-a786-4f0764c63c9d | -5.14322 | -48.89013 | 2025-07-08 04:40:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e043346-e167-3f69-bfce-617b4e9a63a0 | -7.19322 | -43.12358 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5fac8b05-4798-39d6-ae3b-726d3a143869 | -5.41554 | -46.06906 | 2025-07-08 04:40:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c9c04bf-99b4-3483-9875-07436bca1ed5 | -5.23701 | -46.04153 | 2025-07-08 04:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0536164-3a5f-3451-b632-39430debb553 | -7.40881 | -43.73746 | 2025-07-08 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0c58083e-7472-36be-ac79-8133831f5eef | -7.28051 | -44.64574 | 2025-07-08 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e25cdca4-28e5-3710-a87a-43efe3883168 | -6.85676 | -44.06942 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 284f0f04-912b-3e68-86e5-4a9218a238fc | -6.88748 | -47.39967 | 2025-07-08 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 062c267c-4bde-3f4a-babc-cb47e50556be | -7.31615 | -43.873 | 2025-07-08 04:40:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ace40e88-b55a-396a-820e-dfdbd231e536 | -7.58241 | -45.2211 | 2025-07-08 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e9e24c1f-a5fd-3f3f-a669-88c6d10d5da3 | -7.48689 | -43.93795 | 2025-07-08 04:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cc4f4a0f-d5db-34d0-9351-c1c1a8666381 | -8.21497 | -44.93387 | 2025-07-08 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53f6ad8a-c7f3-31a4-aac3-d7ca4bb57273 | -7.09441 | -44.15786 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db1174ed-1ecb-3e1f-a122-b8a8271304eb | -5.23403 | -46.0368 | 2025-07-08 04:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d738e59c-181b-3d09-9685-9e9882423211 | -7.25722 | -43.07655 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81cd57f2-398b-3436-ad18-c4bc03bc24d7 | -6.67878 | -43.76157 | 2025-07-08 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d96e1e05-9806-340d-8959-4f1820b6ba1b | -7.10324 | -44.15555 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5983c239-fea6-3be6-9145-94d42818c5d6 | -5.65726 | -46.58995 | 2025-07-08 04:40:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a6a7cdc-0ee8-3e77-9466-79a8890df6e4 | -6.33739 | -43.74413 | 2025-07-08 04:40:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45cce248-83ce-3f6e-ae18-e0d0e18cf960 | -6.67394 | -43.76498 | 2025-07-08 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6eca051-449c-3d20-97f0-71ff982ef76e | -7.19258 | -43.12797 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 36d7e84d-7934-3b80-ba9c-f6c3e6abdcf6 | -6.0131 | -44.5341 | 2025-07-08 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2bb9e2e8-ec9b-3262-a8d1-ae64bc3ec765 | -7.43815 | -45.4166 | 2025-07-08 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| aceb5d8b-b334-34e4-96c5-e3e727cffe1d | -6.93397 | -43.05313 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3371efa9-2a98-3093-b72e-c3ac50ba5c15 | -6.8562 | -44.07318 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29832c1e-d044-3aaf-b118-a23be67d2b9e | -7.63684 | -45.36452 | 2025-07-08 04:40:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3779f4b7-7d19-3cbe-bb8c-0108b14ac03a | -7.219 | -43.12086 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bf14d9df-1a1d-30d6-86e6-d4af01d006ba | -5.23765 | -46.03737 | 2025-07-08 04:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef59287a-93b9-3af1-8063-9e5b313d478c | -7.30866 | -55.30987 | 2025-07-08 04:40:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27d74af4-098e-3440-b713-39ac436d8477 | -8.12064 | -47.15749 | 2025-07-08 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8938f426-2e95-3fa1-bae2-254877ab8f4c | -6.88499 | -45.23869 | 2025-07-08 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9014ea71-a26b-361e-b06f-1b356f6f0bc6 | -7.27645 | -44.64529 | 2025-07-08 04:40:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43b7a4f6-7f30-3b8b-958a-14524e2aa435 | -7.24377 | -43.07452 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| aa25ad29-5b72-3d3c-8ad1-414b31723db9 | -8.14225 | -47.17994 | 2025-07-08 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1785fb4-dbe1-3778-8102-cab471cf5cce | -6.88429 | -45.24338 | 2025-07-08 04:40:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fbe11ff-f7cc-3231-a95d-0d0d339d01dd | -5.41676 | -47.56786 | 2025-07-08 04:40:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9672a7f-5528-38ea-a66e-0279f3a91812 | -8.21445 | -44.9374 | 2025-07-08 04:40:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10811a97-f152-3646-b25b-832bf54d0302 | -4.28195 | -48.18975 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 706e2dcd-3e9c-3915-8e31-1b78c7305957 | -7.44826 | -44.60185 | 2025-07-08 04:40:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dfc0cb52-ebf5-3ec5-bbf6-cf72ffd3b6c8 | -7.19195 | -43.13233 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 20bdf442-60fa-315e-813a-3b40c147badc | -4.28584 | -48.18678 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f7338a0f-516f-3fff-b93e-7cb26b0be48c | -4.42636 | -48.14788 | 2025-07-08 04:40:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c555a720-1660-3b63-ab98-2edfc680ccd5 | -6.67335 | -43.76895 | 2025-07-08 04:40:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ea404d16-0947-3093-b836-4dbd01118db7 | -6.4341 | -44.8055 | 2025-07-08 04:40:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 806ebb37-775d-313b-af44-d31353b3860a | -7.10477 | -44.17431 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c43fcacb-1dbc-31e8-ad59-276275be8dc5 | -8.15318 | -47.62873 | 2025-07-08 04:40:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8ff1a55-1649-3e5e-9ac5-dd195188252f | -7.25274 | -43.07587 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 85b5b101-adac-39af-9932-bf97bd694f73 | -6.90135 | -47.4017 | 2025-07-08 04:40:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 838e79b0-f25e-335a-9e51-7da1e1af3317 | -7.10742 | -44.15602 | 2025-07-08 04:40:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04c22e06-d460-3339-90cc-d7544005a636 | -2.58716 | -51.92184 | 2025-07-08 04:40:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e7ccaeb7-5c18-3871-98d6-6966b5c8bbb0 | -5.32657 | -50.0577 | 2025-07-08 04:40:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07b0cfec-4e15-33bb-84cd-dcf937562fa0 | -7.20087 | -43.13367 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 447a9376-42a1-3c76-ba9a-7b5b2652b4b5 | -7.18875 | -43.12291 | 2025-07-08 04:40:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |


[Clique aqui para ver as próximas entradas](README12.md)
