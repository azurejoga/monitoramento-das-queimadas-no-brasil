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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5edbe1e7-86b7-34dc-b1a7-a8b6aed1a68f | -3.35765 | -59.44004 | 2026-09-12 01:05:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 22.3 |
| c727caa9-0bbb-36b4-9808-4aa2f11a467a | -2.72117 | -57.62181 | 2026-09-12 01:05:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 42a873df-4d17-30c0-b67c-52fe68cd481e | -6.10442 | -59.89355 | 2026-09-12 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 2f0cd9ef-3233-3a31-b0d7-cfc6d8a9c8e6 | -3.73554 | -61.74457 | 2026-09-12 01:05:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 6271b259-de52-3d0c-840b-2fd950ccfce6 | -6.10675 | -59.90914 | 2026-09-12 01:05:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 4d45c598-6f31-36fb-9b24-f77d90b4a5be | -2.72517 | -57.64864 | 2026-09-12 01:05:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 09b41038-eae2-376b-bba0-2a563a4630d6 | -3.2128 | -46.9602 | 2026-09-12 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 3260e4d4-0758-3dfc-847a-508379f6e54a | -4.3137 | -49.1226 | 2026-09-12 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| a0ff31bf-6b54-34e6-b720-e4eee373c7c1 | -14.5916 | -52.6461 | 2026-09-12 01:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.9 |
| a8e2acf4-39d0-33ca-a4bc-281a9ed178e8 | -2.7331 | -57.6271 | 2026-09-12 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 60a223e3-9baf-35fe-a864-fd604c0f37f2 | -6.2243 | -51.6949 | 2026-09-12 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| eef75aee-7376-386a-9f7b-d41c5e75cac1 | -10.6829 | -54.1475 | 2026-09-12 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| aafdcc63-0f9b-3bb6-9761-608e511823e8 | -5.7756 | -45.0826 | 2026-09-12 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 319.3 |
| b3fb4d12-889c-357f-888f-e8a381820b23 | -8.9607 | -67.3918 | 2026-09-12 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 197641c6-8518-31ee-8785-7b2f6f2a1588 | -5.7754 | -45.1053 | 2026-09-12 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 363.0 |
| 9253c6e9-c00d-3fcf-96c9-ced3356dbc51 | -9.1799 | -68.2194 | 2026-09-12 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 88c663db-9ff6-30b9-93ee-dfba64d2af4a | -6.9612 | -44.5316 | 2026-09-12 01:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 065e7e15-5280-3650-80e2-f26002557cd8 | -7.413 | -46.1456 | 2026-09-12 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 5a8a26c7-2148-3c44-829a-8f59c8cb6a0c | -6.6021 | -58.849 | 2026-09-12 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 2f93cbdc-0752-380a-a608-cceabe44c733 | -9.1613 | -68.2383 | 2026-09-12 01:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 28f16171-b85c-35fe-b32e-b9fd56d6d696 | -3.2313 | -46.9596 | 2026-09-12 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 177.2 |
| 5111991c-aa38-3eae-aa03-195ab573e70e | -6.2429 | -51.6939 | 2026-09-12 01:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| b2575696-eef4-37b8-aaef-4f156c79125e | -10.6827 | -54.1679 | 2026-09-12 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 240.6 |
| a1339042-2511-3046-842f-7e3fdf4552c3 | -14.5912 | -52.6673 | 2026-09-12 01:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 165.6 |
| 1ff241e9-7e37-30ac-a774-8429dfe9628d | -2.7331 | -57.6465 | 2026-09-12 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 150.9 |
| 5b04bbf8-f855-35bf-8132-85c89405dfa4 | -9.6451 | -49.6817 | 2026-09-12 01:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 857e15ba-1028-3dfe-8ca4-ccec7dc0f0b5 | -7.4317 | -46.1439 | 2026-09-12 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 859ecab9-81fe-332d-900a-1f84cc65e521 | -9.7133 | -64.9637 | 2026-09-12 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.6 |
| fc76cb42-0b8b-3138-82f3-c08e3afeba1d | -2.733 | -57.6659 | 2026-09-12 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 0b4811d0-5e72-39a4-893e-8e30810dad6b | -4.3587 | -47.7853 | 2026-09-12 01:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6c6e4719-e217-3a4d-9226-cfa3b426cfcc | -3.2499 | -46.9589 | 2026-09-12 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| a99205c8-e3b7-307c-b31b-3ab4024115ae | -5.7569 | -45.084 | 2026-09-12 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 225.2 |
| c8fefb55-1e85-31ad-9e04-9baee85db5b8 | -3.2314 | -46.9376 | 2026-09-12 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| b3a631a8-97a4-3a4b-b1d9-221dd5c693c1 | -6.961 | -44.5546 | 2026-09-12 01:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ca6f49ca-27f1-3bd9-8e30-00a1cfe53e6e | -2.7148 | -57.6469 | 2026-09-12 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 2560e299-0c3d-36f5-a69a-0f9e053620d6 | -2.7148 | -57.6274 | 2026-09-12 01:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| b8cb07d8-424f-3074-9379-993e87e9419c | -12.8543 | -44.386 | 2026-09-12 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.3 |
| ff3abb2b-468a-3c36-86d8-be2d09f9e648 | -7.4127 | -46.168 | 2026-09-12 01:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 10395423-48ed-3747-8a54-91bd1e771dd9 | -10.7015 | -54.1663 | 2026-09-12 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 289.6 |
| 3c561fec-a2b1-35c1-a66f-353effce0082 | -18.8868 | -46.9692 | 2026-09-12 01:10:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| ef1e721a-5d06-374c-9f27-84435b75a64e | -3.7462 | -61.7552 | 2026-09-12 01:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 03f4e497-511b-3992-acfb-27b6ce1e0d89 | -10.7018 | -54.1458 | 2026-09-12 01:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 0b6f2f03-ceed-35ae-8333-97b6362fe74c | -14.5719 | -52.6698 | 2026-09-12 01:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| b1de0958-ab86-3663-b499-53752fcc2200 | -5.7567 | -45.1067 | 2026-09-12 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 240.0 |
| 8dab3ad0-6207-3a5f-a9a2-a8e07ad79cfe | -2.97 | -50.4 | 2026-09-12 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd0df35d-0265-309e-8d8d-aeb9f1b450a8 | -5.79 | -45.1 | 2026-09-12 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b374dd53-00f5-3388-b8f6-af6992ab70f9 | -2.94 | -50.46 | 2026-09-12 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d643ddc2-3954-32da-808a-5b41c083bdc2 | -2.94 | -50.4 | 2026-09-12 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5169306f-f484-33dc-9fe0-96dc27fac694 | -2.97 | -50.46 | 2026-09-12 01:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 841ef4a9-b82d-36d1-9a83-fbd29570ceb5 | -5.76 | -45.09 | 2026-09-12 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2172adca-9aaf-323a-90e7-ae380c153969 | -10.69 | -54.2 | 2026-09-12 01:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b02ae6e-e462-3c7c-b39a-79ea26e32920 | -4.3138 | -49.1012 | 2026-09-12 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 4f5a6dcb-4176-3b82-81cf-ff7134165732 | -18.8868 | -46.9692 | 2026-09-12 01:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 548e10ed-e58e-3fed-83cc-70e9b290e4fc | -12.8543 | -44.386 | 2026-09-12 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.4 |
| b2c520c8-7490-39d2-9157-9be2e5e55995 | -3.7462 | -61.7552 | 2026-09-12 01:20:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| eb60ae90-9fcd-34d4-a7b2-aa8c24f9c747 | -18.6668 | -41.9962 | 2026-09-12 01:20:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.0 |
| b29eb2d6-a82c-383a-b0a2-5c7a356832fd | -2.7331 | -57.6271 | 2026-09-12 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 2dd86045-82b8-3f5f-a5b4-7ec7b0f1348e | -3.2313 | -46.9596 | 2026-09-12 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 158.4 |
| ef67d2df-74d1-3b4f-96b1-a66a86156a55 | -2.7148 | -57.6469 | 2026-09-12 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 941d2851-baa2-3bcc-8868-fad81a43d271 | -3.2128 | -46.9602 | 2026-09-12 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a7199b63-b020-3098-a074-7faf4b49884e | -9.7319 | -64.9631 | 2026-09-12 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 443fe5e7-14dd-3c8a-a73c-ed71175d2ae5 | -14.5719 | -52.6698 | 2026-09-12 01:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 51d7119e-37fe-3f57-a045-f35ff20a26e6 | -7.413 | -46.1456 | 2026-09-12 01:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 3fcf8948-2fdc-34cb-9c70-1d5a1a183dcf | -2.7331 | -57.6465 | 2026-09-12 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 165.9 |
| 73aee61f-2404-38d7-9138-ba9f820771ae | -10.6827 | -54.1679 | 2026-09-12 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 187.9 |
| a673f7b7-1801-3a20-9a8a-7a1264b69f9a | -9.1799 | -68.2194 | 2026-09-12 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 30657855-8d8e-3a58-bb6e-b2ebb0d76665 | -14.5912 | -52.6673 | 2026-09-12 01:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 0f003f93-649a-307e-87fc-8e8497761ba4 | -3.2314 | -46.9376 | 2026-09-12 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| 6b03f649-bb99-3efa-9f41-2c4341ce04cb | -4.3137 | -49.1226 | 2026-09-12 01:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| e2936ff9-b6dd-3482-abbf-76fd0e7ad919 | -6.2243 | -51.6949 | 2026-09-12 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| a214d590-f16a-37a6-9393-bbec6a564878 | -6.2429 | -51.6939 | 2026-09-12 01:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 7f36bc5c-69f3-357b-bd6c-249884766eed | -10.7015 | -54.1663 | 2026-09-12 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 231.4 |
| 2ffd0ee2-bcd0-3c59-9e52-89fec47390f8 | -5.7754 | -45.1053 | 2026-09-12 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 291.9 |
| 87caf500-3095-3c30-bbfc-6fe8eb2b30b4 | -2.7148 | -57.6274 | 2026-09-12 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 83231b9b-3861-3a74-9b1b-e525071c5e12 | -5.7567 | -45.1067 | 2026-09-12 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 190.6 |
| 919bf39f-9251-3572-94f9-e7eba43bcaf4 | -10.7018 | -54.1458 | 2026-09-12 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 99.0 |
| fb37b521-3466-3820-8345-425da13a43b3 | -9.1613 | -68.2568 | 2026-09-12 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 560562eb-7353-311b-8781-85a147b298cd | -5.7569 | -45.084 | 2026-09-12 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 258.1 |
| ab70a0b3-fd20-3718-95d0-5650cba5af3c | -6.961 | -44.5546 | 2026-09-12 01:20:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 7cb2964e-1a06-33d2-be83-40ae6f05c603 | -9.1613 | -68.2383 | 2026-09-12 01:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| d131227b-0ed2-300c-b2c5-117dfb1fd3ac | -9.6451 | -49.6817 | 2026-09-12 01:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 5c86fde5-75f0-38ec-8fa3-16cf6a6a4ab2 | -9.6947 | -64.9644 | 2026-09-12 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 70f23cc9-9ff3-3caf-847f-bd7171131f07 | -10.6829 | -54.1475 | 2026-09-12 01:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| eed5017f-f5e7-39a3-bb2b-a2617a6fe6c0 | -5.7756 | -45.0826 | 2026-09-12 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 367.7 |
| 0195648e-d10c-3f6f-956d-b32c9cfa5de1 | -9.7133 | -64.9637 | 2026-09-12 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 8c89d544-5515-39d1-94c6-3edf28bdbbc0 | -4.3587 | -47.7853 | 2026-09-12 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 642fd98d-cebd-3532-a6f4-2653fc81ca35 | -6.6021 | -58.849 | 2026-09-12 01:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 5eccdf63-640d-3d1f-97fc-92b2c41271c7 | -10.6948 | -54.159901 | 2026-09-12 01:26:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| afc00f29-5718-3034-bec2-db5b34f0e40e | -6.8796 | -55.627499 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d26715b8-6c29-3b34-bd65-b73ec54d0dbf | -8.2259 | -55.260899 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b667d6e-f81a-37f3-932a-716a2bc0cd1b | -6.2378 | -51.6991 | 2026-09-12 01:26:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59d159fc-8d75-3cbf-85c6-591abea3343b | -18.643101 | -47.272701 | 2026-09-12 01:26:00 | METOP-C | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 37734101-5891-35d7-9f99-60691ad9384b | -9.7398 | -64.953903 | 2026-09-12 01:26:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6836a183-e0bc-3772-9004-efebc644a878 | -6.6074 | -58.848801 | 2026-09-12 01:26:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 72406f7d-35b9-32d1-a2b4-7b557edea54c | -5.9754 | -57.776798 | 2026-09-12 01:26:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44207811-f75c-301d-89a7-7d82baeaad28 | -6.2047 | -55.265598 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1ae7363-4ef4-3c0d-b81d-5d218754b296 | -8.5728 | -54.563702 | 2026-09-12 01:26:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6804ecb9-9d53-38b8-96d6-91cd1fe68054 | -9.153 | -68.232201 | 2026-09-12 01:26:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc764be-ff23-30b7-8012-bc34a5978719 | -9.645 | -49.667099 | 2026-09-12 01:26:00 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2b222cc-bb3c-3131-a88c-3ba42b46e269 | -6.8609 | -55.249401 | 2026-09-12 01:26:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
