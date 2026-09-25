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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fe90389-8fc0-32a8-9149-13a670b04dc7 | -9.6298 | -43.9453 | 2026-09-25 00:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 89.3 |
| c7d3ac30-636d-3316-821b-4f7c9ed8e53a | -11.8034 | -50.9491 | 2026-09-25 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 716f4f0d-d71a-3e69-9497-b487d281f467 | -7.8802 | -61.3305 | 2026-09-25 00:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| ea4363bc-e048-3cf9-8745-8626ddb400ad | -7.4038 | -64.3656 | 2026-09-25 00:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 12a3c266-94d1-3616-9c59-569789f11d09 | -7.6696 | -67.1451 | 2026-09-25 00:00:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| ee2c57ad-e8ae-3e94-8bfb-15dce29e18af | -1.1462 | -54.0796 | 2026-09-25 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| b52679ed-d0e6-3f4e-bebf-a47c12c8f02a | -12.0605 | -50.2989 | 2026-09-25 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 30e43f64-3853-3102-a50b-b2da6927e720 | -5.7754 | -45.1053 | 2026-09-25 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 161.9 |
| 9010c8f4-d1b7-33a5-81e7-41801ffce7a5 | -3.2315 | -46.9156 | 2026-09-25 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 180.3 |
| 7d12b0b0-3ffd-3e35-8457-5caea28d6232 | -9.1626 | -60.7948 | 2026-09-25 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 63df5768-3d93-3394-ba8e-5465961ba41e | -12.0609 | -50.2773 | 2026-09-25 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 5d2b4c6a-d2fb-303a-a3c2-60ac395423f5 | -5.8047 | -43.9132 | 2026-09-25 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| ceb3913e-840b-36b0-9a60-3a38904839e0 | -11.8037 | -50.9277 | 2026-09-25 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| efebb29b-a7aa-3fe0-9f87-e684ed6ca38c | -3.2314 | -46.9376 | 2026-09-25 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 237.6 |
| e6347b02-cefe-32fd-b7e9-8e6a74d074f7 | -1.1461 | -54.0996 | 2026-09-25 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| f3ca5f76-49bd-325f-8f2e-c14c9c54d546 | -12.0796 | -50.2966 | 2026-09-25 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 1bdb19e4-5877-3900-ac6d-cde2d8280c37 | -3.25 | -46.9369 | 2026-09-25 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 5baed5e6-e481-3026-bfa9-8ceba0ffda86 | -10.6283 | -53.9885 | 2026-09-25 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| c108334d-4c9d-3c75-898f-45fa2fcec58f | -5.786 | -43.9147 | 2026-09-25 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 142.6 |
| bf4e7c5e-e549-3b7d-9a93-2f2514cd7ca1 | -10.4421 | -64.5028 | 2026-09-25 00:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| dee9b28d-6200-3dd3-b1d2-348c2383384e | -11.7846 | -50.9299 | 2026-09-25 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 9b391e24-33ff-3d33-a21e-9ef1c1f1e80e | -11.6564 | -50.6031 | 2026-09-25 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| dc34fefe-883d-362e-9fa4-8970808021c5 | -5.8808 | -43.7918 | 2026-09-25 00:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 146.3 |
| 62c1b9e8-67d3-3a52-abd7-87315702bd9d | -1.2189 | -54.5592 | 2026-09-25 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 0ba0e071-753e-3a5c-af80-fb82b09b053f | -3.2501 | -46.9149 | 2026-09-25 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| fb5a9d40-c9ea-3863-b68d-b3b0b4686792 | -9.6295 | -43.9686 | 2026-09-25 00:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 74.2 |
| b2b2857e-d9dc-3828-a5fd-4e767d1d6a90 | -9.1627 | -60.7756 | 2026-09-25 00:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 99f79ba3-80a3-3313-95df-b3f3a7d8402b | -8.34 | -44.1427 | 2026-09-25 00:00:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 59.0 |
| b0729f24-74f1-3456-85b6-5a1a00ea8882 | -5.7756 | -45.0826 | 2026-09-25 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 49fbcf09-2530-3f88-839e-072a8bc603f5 | -7.8898 | -54.7407 | 2026-09-25 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 3c230c55-a7eb-3320-8869-ed7e0d1690f1 | -11.6754 | -50.601 | 2026-09-25 00:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 990b497c-0404-3ea1-bf5e-a69c0f7242bb | -11.959 | -50.7179 | 2026-09-25 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 82.0 |
| a0d49232-dc91-3084-bb68-636a665eeab8 | -10.4421 | -64.5028 | 2026-09-25 00:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 5e00c3f1-70f3-3d92-85ac-39defb32bf12 | -3.2315 | -46.9156 | 2026-09-25 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 162.2 |
| 96461ee9-d1de-37cc-b42f-c7d99c6b1a85 | -1.1461 | -54.0996 | 2026-09-25 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| bb9b57a7-dcd2-3261-8930-f1fb2f57f4ab | -10.6283 | -53.9885 | 2026-09-25 00:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| e325953f-6c93-34f6-ba64-2e084f0f9ed5 | -12.0796 | -50.2966 | 2026-09-25 00:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| d404ab44-6b06-3e13-ab78-828f89f1752b | -5.7756 | -45.0826 | 2026-09-25 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| d78c67c9-1495-3a90-9199-fce5b6d6b401 | -11.8034 | -50.9491 | 2026-09-25 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 6e50a238-0fc5-34a0-97bf-5eece74a568b | -11.8037 | -50.9277 | 2026-09-25 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 9aa54811-c465-368e-9fb9-e50ea35511a1 | -4.5046 | -54.9446 | 2026-09-25 00:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 1479e686-6be4-3837-a3d8-7f664d4c5dac | -3.2501 | -46.9149 | 2026-09-25 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| f4bfa89f-db14-38fd-9d1d-7c8a3d1eb34a | -11.9399 | -50.7201 | 2026-09-25 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 31873655-5b8a-3de3-b7a0-57cc9cf79e84 | -14.7344 | -46.2219 | 2026-09-25 00:10:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| f4d774a8-61fc-3253-a9c3-4c6f58f4e369 | -3.25 | -46.9369 | 2026-09-25 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 123.6 |
| 1a15fed6-13fc-3d20-afca-bb18f14ff7f5 | -8.34 | -44.1427 | 2026-09-25 00:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 51e0bb21-8e57-3603-878d-c934a9c10fb6 | -5.786 | -43.9147 | 2026-09-25 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 8abdfc00-4edb-33cd-b53b-8f8ee513297c | -1.1462 | -54.0796 | 2026-09-25 00:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| aacaf293-8d80-35a9-9df2-d45732f34113 | -5.7754 | -45.1053 | 2026-09-25 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 815f1a92-c7bb-390a-a234-5b0b28320be0 | -9.0157 | -60.533 | 2026-09-25 00:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 0c4359d3-512a-30d4-aa80-acaef45bd110 | -7.8802 | -61.3305 | 2026-09-25 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 405bc915-49a4-335a-84d8-67ebde5e3cf8 | -5.8808 | -43.7918 | 2026-09-25 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 119.7 |
| e5fa7f77-7427-3b94-83fc-00e866071dff | -11.7846 | -50.9299 | 2026-09-25 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| f210fcb8-dbd0-35e9-9491-39252cc44e4f | -5.8047 | -43.9132 | 2026-09-25 00:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 7ede62b9-81a3-38c1-95f0-1c6fcaa1b37b | -11.3048 | -51.3011 | 2026-09-25 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2fd7b615-b24f-3f6b-b674-60cca9e30f10 | -7.4038 | -64.3656 | 2026-09-25 00:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| edd66028-ceac-39be-9cb1-5f500c35fab8 | -3.2314 | -46.9376 | 2026-09-25 00:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 207.7 |
| edad7e37-f39e-3d04-98d7-fbbb480d0d87 | -3.23 | -46.93 | 2026-09-25 00:15:00 | MSG-03 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| edbc665e-85a0-3fba-a6bc-bac350ecab78 | -5.8285 | -47.745098 | 2026-09-25 00:18:00 | METOP-C | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 16a2bb28-b8b5-33f4-a9b6-fb17cb6666a2 | -12.3156 | -50.239498 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 55d4dcd4-ae21-385e-ab81-1b091d5946cb | -0.9309 | -47.544701 | 2026-09-25 00:18:00 | METOP-C | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80e9c955-844c-39f0-92d4-57619ae1707d | -3.2293 | -46.924 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3947947d-27ac-37ba-8302-bfad3ea8f837 | -1.1287 | -54.09 | 2026-09-25 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83f19858-03e7-388d-9a16-1bd84ab649fe | 2.2562 | -50.893799 | 2026-09-25 00:18:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 44d6d4da-3b71-3be5-956b-bbb0d68da07d | -5.1514 | -50.012699 | 2026-09-25 00:18:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a1a253a-7aac-39e9-ae1c-6356a43f1156 | -11.6643 | -50.575298 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 49b0b94c-7553-3f27-b95a-0840e3d9c5af | -4.4618 | -47.9216 | 2026-09-25 00:18:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1dea36b2-574a-36d6-98b2-69aea1959971 | -3.4166 | -39.292 | 2026-09-25 00:18:00 | METOP-C | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c3a102ad-670d-3203-9bfe-c949cf378706 | -0.5067 | -49.150101 | 2026-09-25 00:18:00 | METOP-C | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbcfbdb9-dabd-35d4-bfd8-854242e406fb | -12.0392 | -50.734402 | 2026-09-25 00:18:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54d0ed17-ec74-3131-b418-e3e9ba3ec8e6 | -7.1221 | -41.720699 | 2026-09-25 00:18:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9cedb1ed-790c-33ff-ad2f-1ba4a3b3ed00 | -11.784 | -50.9249 | 2026-09-25 00:18:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1d5d3f33-ac59-3f72-8bc0-40ecec571dd6 | -11.3549 | -43.422699 | 2026-09-25 00:18:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87b2a3e6-1228-3451-bd7b-703298b40fea | -7.3585 | -42.073502 | 2026-09-25 00:18:00 | METOP-C | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bb29cc69-25d3-34ee-8c17-f0ed30c63c49 | -6.0065 | -44.094501 | 2026-09-25 00:18:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbbe82ad-9e42-3b09-8dac-7e7ba87095d1 | -5.5688 | -45.2985 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6403ef2-10c6-3136-989f-0230e62210c2 | -11.9383 | -50.7346 | 2026-09-25 00:18:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f047980f-979b-33ed-adbb-0c7e263da504 | -5.7411 | -42.441898 | 2026-09-25 00:18:00 | METOP-C | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e0146f69-3309-37f3-87a5-0f8c6f170c8a | -1.1333 | -54.065899 | 2026-09-25 00:18:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 899af867-187e-375c-b9b4-68975e89eaa2 | -11.6716 | -50.612099 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac05e25f-5852-31fe-93ee-994aad96c9cf | -5.1456 | -49.986301 | 2026-09-25 00:18:00 | METOP-C | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d587a996-029e-3541-8b5c-1d735419f5f2 | -9.631 | -43.952599 | 2026-09-25 00:18:00 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 89d639e2-7dfc-3886-ac6c-15e2d998a71e | -11.6388 | -50.599499 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14d3f9b0-01d1-3a3d-bf7a-f50cdf5a0ecf | -3.2391 | -46.921799 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 075be509-4367-3bb8-b21e-809d248b966c | -8.5964 | -48.3717 | 2026-09-25 00:18:00 | METOP-C | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90f4abc8-3dfa-3b9e-bf22-231f104d1f1c | -3.0553 | -46.928299 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb38dffe-b84e-37af-a80f-8640caffdcff | -9.5801 | -40.351601 | 2026-09-25 00:18:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 51f4ab21-381f-3a20-a04c-06549304a4e1 | -11.9442 | -50.713699 | 2026-09-25 00:18:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e8df64c8-d82d-3ed4-80dc-c3c3549e7d49 | -5.771 | -45.099899 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2578affc-9796-3017-9603-f08d1592571f | -9.5748 | -40.328999 | 2026-09-25 00:18:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 3761831c-6604-3cff-99ea-e543963d6666 | -5.3216 | -44.254902 | 2026-09-25 00:18:00 | METOP-C | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 74714fa6-2f20-37a3-b631-9b47e6fa51ee | -5.6193 | -45.248798 | 2026-09-25 00:18:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e095318-a91a-3c70-b9e0-8b570491c889 | -3.4119 | -39.272301 | 2026-09-25 00:18:00 | METOP-C | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1a05c97d-4c8e-3e38-a071-c5b170b80cf2 | -3.9817 | -48.4366 | 2026-09-25 00:18:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3a2f134-6ee9-3aad-a0c6-171af28af027 | -11.6254 | -50.583099 | 2026-09-25 00:18:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9c688e67-5546-3328-910e-98aff5330384 | -3.9491 | -42.992599 | 2026-09-25 00:18:00 | METOP-C | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 37e7d417-f8aa-399b-9da6-d4f88b304c25 | -6.0081 | -44.101501 | 2026-09-25 00:18:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 332de097-4eb7-3685-8f38-d096b6dee59e | -5.5922 | -50.159199 | 2026-09-25 00:18:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70a86ca5-c7d4-3511-ba80-717f3e16ce2e | -3.7199 | -49.0532 | 2026-09-25 00:18:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98e4754d-f0c6-3bb1-b18c-d004f241ec0d | -3.0534 | -46.9203 | 2026-09-25 00:18:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
