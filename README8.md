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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 27949d02-a595-3e3c-b16f-f0f0343df155 | -2.5842 | -51.8623 | 2026-10-04 00:30:00 | GOES-19 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| eb91763e-6c39-37e8-a8cf-f7585fb35120 | -3.4761 | -50.1094 | 2026-10-04 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 080d2530-3338-318c-a5b3-39d931127eb0 | -3.0364 | -54.2282 | 2026-10-04 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| f55cd083-b6b6-3571-b743-76c09e614fc4 | -2.2297 | -53.7026 | 2026-10-04 00:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 9d602f84-8e2a-32a6-bf03-8f0265bb8dcb | -3.0932 | -53.7441 | 2026-10-04 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| b990fbf8-b92e-3f4a-8bdb-7e0dc9683a16 | -4.2559 | -46.3633 | 2026-10-04 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 166.8 |
| 9bec4ae7-bfa4-3dcc-ac0b-bdf82cdbce0a | -8.593 | -66.8081 | 2026-10-04 00:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| b479bec8-1ce1-3fba-a103-56ff9e764ca8 | -3.13 | -53.7229 | 2026-10-04 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 188.2 |
| e82b8bef-fd6c-3378-837e-e6714e6b7eef | -3.1116 | -53.7234 | 2026-10-04 00:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 228.2 |
| 77142b37-57a5-3467-b506-e31b07f985a6 | -3.4762 | -50.0883 | 2026-10-04 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 57c7d626-10dd-3464-8371-a911c1b450ca | -8.3526 | -62.8302 | 2026-10-04 00:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7f244a58-9c90-3a3d-a635-c51553589b57 | -3.8848 | -49.6933 | 2026-10-04 00:30:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| a7f2bace-81f9-3ce6-b0fe-3d28c45b8b2f | -3.4576 | -50.11 | 2026-10-04 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| feea0139-646b-3205-b8da-a69d11cdeea2 | -4.7434 | -43.2679 | 2026-10-04 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| 574e4f91-47be-3b48-a260-38b5921cbda5 | -4.2558 | -46.3855 | 2026-10-04 00:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |
| f3652738-c743-39cb-9b52-f20ba299319e | -6.0552 | -47.2935 | 2026-10-04 00:30:00 | GOES-19 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 5f90a08d-535b-3c91-b8f2-cf1383d26be6 | -3.4577 | -50.089 | 2026-10-04 00:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 3cd3afe8-1847-3b32-9648-95255c74cefa | -3.0548 | -54.2277 | 2026-10-04 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 625d2710-4cf9-3a09-a1bd-f444edcce6b1 | -4.2886 | -50.2886 | 2026-10-04 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 4f49b09a-fc49-3cf5-8f4d-45a302399fa7 | -3.7744 | -49.5704 | 2026-10-04 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| b296cf75-3a4c-3ca2-8a4c-5316816f668f | -3.0721 | -49.5313 | 2026-10-04 00:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 23000ffa-d765-3a9e-a330-27d4df41bf44 | -2.8163 | -54.1129 | 2026-10-04 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| b4b3b4b5-bc14-3d4d-9bfb-1117cda4d97d | -4.3072 | -50.2668 | 2026-10-04 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 059e20e8-9a6f-39e0-863d-0f858d413952 | -4.2702 | -50.2683 | 2026-10-04 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| bdb8cd84-db02-3463-a814-1421e4a2ec38 | -1.0852 | -54.118198 | 2026-10-04 00:31:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7be16e3c-60de-3115-be57-c42bf5534590 | -1.8612 | -47.974899 | 2026-10-04 00:31:00 | METOP-C | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28652b99-7413-3914-9b24-56dc6899112e | -4.1397 | -49.694 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9040965-f660-3160-a842-390ef84c72c7 | -3.2925 | -53.821701 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb92a810-45eb-3b19-9785-9c889ac3b1dc | -2.9369 | -54.1073 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b20c694c-da20-3fdf-835a-9b1b25671e83 | -1.4988 | -49.452099 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f86ee2ca-f747-3912-ac2c-d98970073256 | -4.4592 | -47.927799 | 2026-10-04 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36a866ee-4b10-32b5-839d-4cf4931b1204 | -1.1572 | -49.265701 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8696d337-323e-3911-a034-4677a4ff1f68 | -4.4869 | -45.5383 | 2026-10-04 00:31:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20d0d91c-087f-3c49-b9fd-07e83a4046f9 | -7.272 | -49.2593 | 2026-10-04 00:31:00 | METOP-C | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2289240e-ca4c-3bdc-87ff-f1a863394efc | -1.4841 | -49.432701 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cee2e453-f307-3c3c-afbe-dab372ba2b13 | -4.113 | -49.077099 | 2026-10-04 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06544402-efad-39fb-8c66-adcf7398bc72 | -1.8103 | -47.843201 | 2026-10-04 00:31:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b65e43bf-5bc9-340d-ad97-23e02e72c9c9 | -4.2618 | -50.736099 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8269790-7173-3b2c-8363-49ece985d005 | -6.0551 | -53.464199 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 94cef858-0052-3eec-9175-979dce53dce8 | -6.0635 | -47.2789 | 2026-10-04 00:31:00 | METOP-C | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 050d3c1a-ef99-36cf-a938-4c7c1d58449c | -3.1899 | -54.094601 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2b9370cc-bf30-3267-bd87-98f8ab6751d4 | -1.6053 | -55.005501 | 2026-10-04 00:31:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb286d8e-5bb8-32f3-80da-22924dab9fd4 | -4.0226 | -44.827702 | 2026-10-04 00:31:00 | METOP-C | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 25f4be00-b3dc-3abd-aba7-8452f15ba2e7 | -14.5565 | -52.870701 | 2026-10-04 00:31:00 | METOP-C | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cce4cc45-7228-368d-bfd3-0b703b9bab64 | -1.4711 | -49.4659 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29485250-4084-31ce-8a24-6b4f17ec8617 | -3.8939 | -49.699799 | 2026-10-04 00:31:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0de3c583-a58d-3673-a7bf-de2af29cfce7 | -5.8555 | -55.693699 | 2026-10-04 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a847c45a-287e-3d2b-b738-f087ca43c29a | -6.2057 | -52.7962 | 2026-10-04 00:31:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82c22fc9-fd3f-3bc2-bb31-b7f2be0f34ce | -3.4988 | -54.607201 | 2026-10-04 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9585e2c-7dc4-32f2-b226-76fcaae44e28 | -3.0783 | -49.554699 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc8e7460-230c-3e2a-a590-5d383ce3ed00 | -2.7944 | -54.110298 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55ffd56a-9c8c-3a2c-8370-cb79e642baa6 | -3.1771 | -54.083199 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47b8bf4c-d277-30f0-a18a-0272c5814c23 | -5.8458 | -55.695702 | 2026-10-04 00:31:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75c4cb87-cebf-398a-82d0-36b844a7f936 | -13.4772 | -42.479198 | 2026-10-04 00:31:00 | METOP-C | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0372ab2a-199b-3f0d-8d1c-a1fd3feca8be | -2.692 | -49.035999 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7044f3-c4cd-329f-abfd-b4fd9a2a091e | -2.5902 | -51.845001 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a719df7-8b85-36eb-834f-bd79090e9575 | -3.0668 | -49.5495 | 2026-10-04 00:31:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e081e84b-951c-3ff7-9c6d-e241fdbf1dfe | -2.2498 | -51.93 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5968d0cc-b6d6-35a5-bf04-b657fb675b98 | -1.615 | -55.0033 | 2026-10-04 00:31:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0c4a08-346e-3de7-8e8b-1ba664600252 | -5.5445 | -49.764301 | 2026-10-04 00:31:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ed57f0a-34c2-3668-be9d-219488165bdf | -2.8461 | -51.2962 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f487fcb-2a3e-3cd3-ba58-a0b8d7019cf3 | 2.3571 | -50.752499 | 2026-10-04 00:31:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ba3c5bc2-a085-3519-9230-2ec2a180aacb | -3.0527 | -54.167198 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40f679e3-0851-3243-b05d-47943b7f5357 | -5.9905 | -53.636299 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b35af690-8f94-3bb3-8d65-e33ad631da2a | -2.7505 | -51.554699 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c782c0c-da9c-321f-b22a-fe2da19fcb6a | -1.0949 | -54.1161 | 2026-10-04 00:31:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a368afa7-86dd-3285-a2bd-1eadf4b36361 | -2.7974 | -54.123699 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b50088aa-8671-399b-ab3a-f2de267a6d6b | -3.5086 | -54.605099 | 2026-10-04 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f44d94bd-db87-3f54-b368-f1ac3d4b325c | -5.5567 | -45.256802 | 2026-10-04 00:31:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4dc0ebf2-54bb-300e-8065-b499b635a707 | -3.1947 | -50.746799 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e4385c1-9f43-3142-888b-6a726abbe2e5 | -6.0678 | -53.4757 | 2026-10-04 00:31:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59048431-7531-3450-ae43-a83cca834a20 | -3.5021 | -54.622101 | 2026-10-04 00:31:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99f2f7b5-3579-3341-9b4e-822d105e590a | -6.8163 | -46.6479 | 2026-10-04 00:31:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab3a26bd-5540-38d2-a6f4-c6e14af4d504 | -3.0096 | -50.475101 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41582834-b046-3cfa-9c57-d471cd030e8a | -3.5715 | -55.299702 | 2026-10-04 00:31:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dae5a601-5ea0-3faa-ad95-8432ea6da46c | -3.2064 | -50.753101 | 2026-10-04 00:31:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46a37ecf-e344-3857-a760-efbac5cd3756 | -1.0823 | -54.105598 | 2026-10-04 00:31:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 281db763-bb51-3cd1-9169-bbd6596c7dc4 | -1.0903 | -49.199001 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74210cda-b314-3ba1-8ac9-2635a3226a07 | -4.2572 | -46.373901 | 2026-10-04 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e4362a96-53cb-3a32-a923-78cc436ffd47 | -1.167 | -49.2635 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b175e78e-817a-3d81-91be-aaf2d5154950 | -3.8922 | -49.692101 | 2026-10-04 00:31:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46ecdf59-7ba4-3cfb-9dfb-8f494efe5d3b | -3.4673 | -50.0882 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d7fc742-114a-30db-8204-d9173854fba4 | -4.2727 | -50.282501 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6a158ad-3ebe-3859-ba87-431ea4f7dd4c | -1.5642 | -46.8633 | 2026-10-04 00:31:00 | METOP-C | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0ec4921-3d6e-33ef-ad35-b44adfa990ae | -4.8034 | -48.2169 | 2026-10-04 00:31:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01a3990f-cb03-3a7e-9dad-8441c3f19b59 | -1.4809 | -49.463699 | 2026-10-04 00:31:00 | METOP-C | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 439702c2-465e-3ee0-af01-bd185066ab3c | -4.4576 | -47.920799 | 2026-10-04 00:31:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09333eae-e8e0-3edc-8711-4d1db60c2ea3 | -3.4655 | -50.080299 | 2026-10-04 00:31:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4089854b-6558-3bad-9475-af41da4cc1fc | -4.8197 | -49.287399 | 2026-10-04 00:31:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc01af7-1ffd-3adc-9636-550288138742 | -4.1113 | -49.069801 | 2026-10-04 00:31:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e767cf1-33d2-31c8-b437-94068b5f896a | -3.0455 | -54.2262 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76656f7e-c7e1-330a-ad0e-09b75dc85fd5 | -4.5216 | -49.6991 | 2026-10-04 00:31:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0099ba09-07b7-3ff3-a00d-8700badf9e01 | -3.0394 | -54.198799 | 2026-10-04 00:31:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1d2d396-4829-33fe-92a8-bf9e1da43694 | -3.1131 | -53.752399 | 2026-10-04 00:31:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 199d0047-4aad-3b62-8545-6e915fd5e626 | -2.8139 | -54.105999 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a84573c2-e089-3ee7-bce3-ea191a15f4d7 | -4.2654 | -46.364799 | 2026-10-04 00:31:00 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10d9601a-c680-3498-a474-5a15fee64709 | -6.7107 | -45.963699 | 2026-10-04 00:31:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab243af9-0d96-31d9-98e0-f11d1cbd8fce | -4.5559 | -47.494099 | 2026-10-04 00:31:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2073c27-b3fd-3c9f-b546-5d0c0ef5c5f4 | -2.5651 | -51.870499 | 2026-10-04 00:31:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b78be46-628e-3834-b929-6696a70de68d | -2.2198 | -53.6978 | 2026-10-04 00:31:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
