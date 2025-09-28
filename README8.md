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
| 663f046f-b3f7-3a5d-8947-46ea9cf78cf4 | -7.7787 | -47.0036 | 2025-09-28 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 7b1e13ba-f624-3809-a6d1-d9eb5dd4958b | -5.2869 | -43.1613 | 2025-09-28 01:30:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| c33df11b-9a79-3629-b3d5-6fb8f628faad | -3.3184 | -52.5403 | 2025-09-28 01:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 383820fd-e79c-3d5b-9691-583962be1246 | -11.9846 | -47.8865 | 2025-09-28 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 86276989-57bf-3984-b33f-b84a137ee715 | -9.6512 | -62.8336 | 2025-09-28 01:30:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| b0a21cc8-91be-32f2-a842-f3a337060a03 | -7.7975 | -47.0019 | 2025-09-28 01:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 3da37dfb-1793-32ed-b9f6-e9bdcea9d4c2 | -14.7861 | -45.6353 | 2025-09-28 01:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 41e89b40-0e99-3400-8565-a68c18a26550 | -11.9846 | -47.8865 | 2025-09-28 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| e24d0255-1135-3c8c-a606-33228566f6bb | -6.1252 | -41.8175 | 2025-09-28 01:40:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| 04c1b3cf-4afa-3a0b-8661-3b1e5fc4b802 | -18.0448 | -51.1777 | 2025-09-28 01:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 8394c600-9211-318b-803c-6cffcf0c9354 | -5.8374 | -44.4399 | 2025-09-28 01:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| b46dd080-da56-37be-b019-2def2cc2e9a1 | -14.7856 | -45.6586 | 2025-09-28 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 4bf1d6d6-1de9-31ab-a4c0-b0ef63e53c5a | -7.8538 | -43.7995 | 2025-09-28 01:40:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 86e04320-d29c-3441-967c-96a6850aecd9 | -7.8634 | -44.5612 | 2025-09-28 01:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b7ac140e-c9db-3e7e-abe6-48039492f67a | -7.8163 | -47.0003 | 2025-09-28 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| c32c684e-e2c7-38fa-81ec-fd6719b7de2a | -11.6058 | -45.4364 | 2025-09-28 01:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 76a7799c-3120-3768-904a-902f43847cfd | -5.8149 | -42.8167 | 2025-09-28 01:40:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 77.9 |
| 8f9fcf0e-ceda-36d6-a593-0a6923a0507b | -7.7975 | -47.0019 | 2025-09-28 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 106.9 |
| a46a08b3-b85e-37a3-9126-a5e655ab79db | -14.7846 | -45.7051 | 2025-09-28 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0f511de2-d0be-3ef1-b4ef-5a0703e33292 | -9.6511 | -62.8526 | 2025-09-28 01:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 127.6 |
| ca542c3f-e514-377b-84e5-674d8b2d0f2f | -18.0458 | -51.1336 | 2025-09-28 01:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 263.4 |
| 31eee787-30fe-3930-8be1-a2228c2e5cdc | -12.0038 | -47.884 | 2025-09-28 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6811ddff-14a0-3875-b042-40c7440439aa | -7.7412 | -47.007 | 2025-09-28 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 539c882a-877a-30d5-b58a-88662181b257 | -15.9382 | -59.5107 | 2025-09-28 01:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 28ee11c3-b65e-39a0-ae15-bc965d5a85d5 | -14.7655 | -45.6854 | 2025-09-28 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 63b6d082-8240-36e3-a2a8-177a9d9b0610 | -5.8187 | -44.4413 | 2025-09-28 01:40:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 56f8648d-6bc1-3995-b630-ccee8a16fbd0 | -9.6512 | -62.8336 | 2025-09-28 01:40:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 116.0 |
| f42b2fa3-2b71-32d7-982d-49fba3c613c1 | -14.7851 | -45.6818 | 2025-09-28 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 151d523d-9bae-3251-bfa6-73e1fe71ad74 | -18.0254 | -51.1591 | 2025-09-28 01:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 59aeafb2-89b3-3ffc-8cfd-377f3ba9ce0c | -7.7599 | -47.0053 | 2025-09-28 01:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 2c4572b4-68da-3e44-8d9e-a1721e0c5fb3 | -18.0259 | -51.1371 | 2025-09-28 01:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 270.2 |
| b9637fed-4711-397f-a947-702ba5a927bc | -16.9667 | -53.6975 | 2025-09-28 01:40:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 6fc0624d-d7a1-3526-9f33-d4ebe5664ce7 | -14.766 | -45.6621 | 2025-09-28 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| d496d97f-a9df-31dc-b428-791877f5a61b | -18.0453 | -51.1556 | 2025-09-28 01:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 235.3 |
| c8402111-6135-37b3-b8da-a385aaf8c33c | -5.7396 | -42.8461 | 2025-09-28 01:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 273.1 |
| 14ac05aa-3696-30f7-8f14-eaa735d6ba6f | -9.6511 | -62.8526 | 2025-09-28 01:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 65163fa7-42a5-3663-877c-d1f6688dd54c | -5.8187 | -44.4413 | 2025-09-28 01:50:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 8f11a9ae-83f2-32a6-8f43-74ddaee58aab | -7.7975 | -47.0019 | 2025-09-28 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 200a6bcb-fe4a-35e0-b18b-6acdf378cde3 | -6.1063 | -41.8191 | 2025-09-28 01:50:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| f32ba70a-215e-3fb1-829e-d2d944945a24 | -18.0458 | -51.1336 | 2025-09-28 01:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 102fdf2b-f94a-3c9e-973c-dfb363bacabb | -5.7398 | -42.8226 | 2025-09-28 01:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 4c70c3f5-e9eb-3bbc-a1db-a317bf22d518 | -11.3642 | -45.0339 | 2025-09-28 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 5294527f-2b05-30c6-911d-e98894cc44a7 | -12.6917 | -46.8708 | 2025-09-28 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| c965bdc6-9144-3db9-88ae-1622b6bd6f69 | -11.3646 | -45.0108 | 2025-09-28 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| a41fa068-06b1-3ca5-93f2-547624fd4938 | -5.8151 | -42.7931 | 2025-09-28 01:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 77.0 |
| e57a9912-d928-3fcc-800f-853e5afcbb4f | -11.3834 | -45.0312 | 2025-09-28 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 4ae9cd9a-3438-3057-8f37-d78f2fc62515 | -7.7599 | -47.0053 | 2025-09-28 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 36e3d8aa-1fe9-3bee-aff0-af26dae9b67e | -11.9846 | -47.8865 | 2025-09-28 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| e5ef35ec-b01e-38db-84f4-cabf3cb4a8df | -14.7851 | -45.6818 | 2025-09-28 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| c773561d-9acb-33ef-8576-252b37e778ea | -18.0254 | -51.1591 | 2025-09-28 01:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 07b38dc0-b473-35d1-8cd4-ee6996b46db2 | -5.4742 | -41.0767 | 2025-09-28 01:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 73.8 |
| e5445e68-d97b-3593-9f86-d952a934f442 | -18.1977 | -53.3208 | 2025-09-28 01:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 87d8e663-a5fb-3bef-8cb6-bd692ede9ad5 | -14.7655 | -45.6854 | 2025-09-28 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| e16a590c-c10c-360d-8fa9-584a8afaf03c | -5.7208 | -42.8476 | 2025-09-28 01:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 419358fe-ed4b-38b9-88d9-b05ad690e92b | -5.7393 | -42.8697 | 2025-09-28 01:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 93.6 |
| 0b3e8c61-a4d5-3506-a099-af192a9bb320 | -5.8149 | -42.8167 | 2025-09-28 01:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| 567eb1e1-d766-362f-a36d-4d7cfd4880e7 | -16.947 | -53.7003 | 2025-09-28 01:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 85bf503f-047e-3538-9bc4-ce636601fcda | -14.766 | -45.6621 | 2025-09-28 01:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 60.6 |
| b922ccb9-03d9-33f0-804d-2dbfb993fac5 | -11.3838 | -45.008 | 2025-09-28 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 21f67d0b-124f-364c-bb28-50ad83f36d03 | -9.6326 | -62.8344 | 2025-09-28 01:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| fe7847b8-8825-3d2a-b500-4fd1143f718b | -11.4417 | -44.9767 | 2025-09-28 01:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 3f9c775f-55be-3d6f-8703-4d4fa57fc1b6 | -18.0259 | -51.1371 | 2025-09-28 01:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 246.2 |
| f4e20d8c-9a38-3ccf-b52d-5aea52b3dc01 | -7.7972 | -47.0241 | 2025-09-28 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| 8866f3d9-5d26-3611-85f7-c90594266795 | -7.7412 | -47.007 | 2025-09-28 01:50:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 6fec56ac-5991-3c76-825d-790695415f91 | -18.0448 | -51.1777 | 2025-09-28 01:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 8b00909c-0dff-373e-ad19-2eda56327a64 | -9.6512 | -62.8336 | 2025-09-28 01:50:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 117.7 |
| eeb7bb8e-d7e0-3311-8984-692899285a78 | -18.0453 | -51.1556 | 2025-09-28 01:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 9ef01341-04ad-3a5d-ab3a-0bac13b52e61 | -16.9667 | -53.6975 | 2025-09-28 01:50:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 135.7 |
| ef90fc04-e59a-3452-94f2-33c9609aec73 | -9.058 | -45.5313 | 2025-09-28 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 5c66a4b2-7df3-390c-af2e-c268a2253955 | -9.6697 | -62.8518 | 2025-09-28 02:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 08b42946-f892-3a43-8a82-b20f56ef52fe | -11.4417 | -44.9767 | 2025-09-28 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 234.2 |
| 91625543-9818-3c3e-a7b1-3a8f581f29b0 | -5.7393 | -42.8697 | 2025-09-28 02:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 9c581da8-574f-312d-96e9-c63d508551ff | -9.6326 | -62.8344 | 2025-09-28 02:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 4cfde37a-38e2-375b-8edc-9eccefe6e2ba | -11.5858 | -45.4851 | 2025-09-28 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| e1b4a527-138f-387b-9824-e17cb5426993 | -16.947 | -53.7003 | 2025-09-28 02:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 99b0d936-5bf6-32e7-9345-634292d144b5 | -16.9671 | -53.6763 | 2025-09-28 02:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 4ffbbe9b-baa5-35ea-85ea-6a0291aadb94 | -6.0937 | -49.3897 | 2025-09-28 02:00:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 3eb2d23c-c21f-32ba-be84-4158ce2c305f | -5.8187 | -44.4413 | 2025-09-28 02:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 26394b73-cfaa-3bed-9460-2ea965814dca | -16.9667 | -53.6975 | 2025-09-28 02:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 155.1 |
| 9b9b9ac2-e1ad-329b-b6ee-1ec7c8ff7e1a | -5.8149 | -42.8167 | 2025-09-28 02:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 74.0 |
| 153a8bbc-40a3-3af8-8bda-fd2cd18bf913 | -11.9846 | -47.8865 | 2025-09-28 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f9f5c437-fb3c-3787-a3da-cc32a361caa4 | -8.1614 | -46.3899 | 2025-09-28 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 7f68f1fb-9bc9-3b5e-9e5f-ed3503dc8fd1 | -6.1063 | -41.8191 | 2025-09-28 02:00:00 | GOES-19 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 66.5 |
| 2ef8ad70-f304-3e96-b71f-6fc33b358b6f | -5.4554 | -41.0782 | 2025-09-28 02:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 5f28537c-1559-36ca-a052-c3131cd4da81 | -7.7975 | -47.0019 | 2025-09-28 02:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 25aee509-9868-36bd-aaa9-2ac6bea640e2 | -5.4742 | -41.0767 | 2025-09-28 02:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 80.7 |
| 86336b12-6fca-3340-b549-e45439ded49c | -18.0259 | -51.1371 | 2025-09-28 02:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 185.8 |
| 74297033-0b0c-327f-8923-6d15c9c649ba | -11.3834 | -45.0312 | 2025-09-28 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 3f8644ef-65f5-3e96-b64f-8da986ea4d90 | -5.7208 | -42.8476 | 2025-09-28 02:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 81.6 |
| acd7592c-1aaf-3ece-b328-01808558967e | -16.9864 | -53.6947 | 2025-09-28 02:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 19be4260-6955-376b-a08c-939ddfe63cf8 | -11.3646 | -45.0108 | 2025-09-28 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 1cb50c83-266a-3c37-8eb4-08abec61a4d7 | -5.7398 | -42.8226 | 2025-09-28 02:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| 9b32facb-d68e-34ae-9d41-b16ea911ef1a | -11.4413 | -44.9998 | 2025-09-28 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 399.1 |
| b9c09c72-6f38-3744-bce9-8be65673c133 | -11.4604 | -44.997 | 2025-09-28 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 2d442d62-b5f3-37db-881b-a0532666dacb | -18.0254 | -51.1591 | 2025-09-28 02:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 151.2 |
| cdd384c5-25fd-3d96-bd4a-3d6ac7a1b25e | -11.4608 | -44.9739 | 2025-09-28 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 3dd46801-8248-3fb2-9d82-1d793c186302 | -9.6511 | -62.8526 | 2025-09-28 02:00:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 0866f2f5-b830-3767-820b-cb2dcac984ff | -12.6917 | -46.8708 | 2025-09-28 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| cbd581de-b75d-37b7-b225-cc2fc425fd45 | -8.2856 | -45.4545 | 2025-09-28 02:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 573a81b6-9c1e-3acc-9542-0b4466c3fc65 | -11.4221 | -45.0025 | 2025-09-28 02:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.3 |


[Clique aqui para ver as próximas entradas](README9.md)
