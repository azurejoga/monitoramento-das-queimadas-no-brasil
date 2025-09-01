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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3792ad20-d653-3b17-a45d-9a0240e03265 | -8.55166 | -63.01248 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a05f8b6-343f-3e34-993f-0a58602b332b | -7.93757 | -63.006 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 16e1afcb-c559-3852-bd8b-27c15879db0d | -4.15517 | -46.7823 | 2025-09-01 05:23:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6927771-d545-34df-9298-071d41e89635 | -8.62327 | -61.39171 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70aaac13-9fae-3fdd-a615-a5970e8b9772 | -7.36393 | -61.65399 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2511cfd4-1f9a-35c2-81c0-eebc37608d4d | -7.10516 | -63.02814 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e9f8e5ec-0f2f-3db8-abdf-5888327ef130 | -8.68412 | -62.40482 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be9bbeea-088b-3365-83ca-ff3d0417710b | -6.99148 | -63.01419 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38f97c02-3c16-36dc-8bcf-0f3f6b809ff2 | -9.11797 | -61.20778 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 04041f9e-8998-3be3-afe6-084000a2414f | -8.61676 | -62.58884 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 952e605a-d2cb-3644-af7f-eb915aa36847 | -8.97373 | -65.96162 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c1633dc-1da0-3afc-9114-fd7bfc984b54 | -10.87765 | -55.75548 | 2025-09-01 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3a87f5e-c3ba-3f8b-9e47-716d7d9b2275 | -8.38096 | -70.75455 | 2025-09-01 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a51d22b-5671-3082-aa58-c18977d3eab0 | -8.62465 | -62.58271 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd1278d1-5e01-338f-9d03-63e20a50a652 | -9.87051 | -65.02813 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 066d7824-8cea-3fa3-898a-44140db7ef5b | -8.65385 | -67.24746 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 884a38cb-e62d-300b-a456-120dfb239adb | -10.24448 | -51.10672 | 2025-09-01 05:23:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d42412d2-fc95-3c20-adfb-b533b8d98058 | -9.07882 | -65.43111 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 44d60f7c-1b2f-3ee2-bb97-8d6766107a78 | -7.10456 | -63.03192 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f248405f-3991-3338-bf91-07262762ee88 | -9.87857 | -65.02498 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d424b33a-a207-3d9e-a550-2e65e4588a84 | -9.16938 | -67.56332 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ae90b3a-9f45-35d3-9d54-11cf82ff73a2 | -8.09276 | -70.21977 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92f8e476-65bf-354d-9372-0bb956d88f1b | -7.53617 | -61.38159 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4476b19f-213a-3c07-b8e8-391e81cf94cd | -9.6765 | -47.82211 | 2025-09-01 05:23:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17f563cc-be3b-3f4f-be0e-51c22b6292da | -9.34489 | -65.42202 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 888cf7fc-04bd-3463-9dd1-09d3ed287d03 | -7.09645 | -63.0384 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b2108ab4-868c-33fc-a541-b4ab85da71a4 | -8.95108 | -65.95259 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3c285b0-ca3b-38ad-b897-bcb360870cef | -9.15502 | -59.53248 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ac3ccef-e794-3050-becb-7cdac75c3e63 | -9.83178 | -65.05939 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0e886e3-fca9-376e-aa1e-50969394893e | -8.75586 | -62.40158 | 2025-09-01 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f7bec4f-2ba5-3acf-a3e5-8bc0ac294885 | -7.07434 | -63.06599 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a4a89b2-5f41-373d-984e-4d0cadc82b73 | -7.56698 | -63.8576 | 2025-09-01 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 365d09f0-0ea9-3b14-a4fd-d2d5789aa1d8 | -10.05131 | -48.10526 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c26ef02d-6ce2-3162-a79b-1e793e1edfb3 | -7.55992 | -60.8815 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbdd8d9c-80e7-3258-8169-a5a6d1ff9748 | -10.36856 | -52.28703 | 2025-09-01 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38b88a81-8bac-319e-91f6-d080d801bfe3 | -10.4804 | -51.62748 | 2025-09-01 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c305bcf9-6be4-39ee-8961-a585371a6a6c | -4.07587 | -47.96043 | 2025-09-01 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 439b2a04-6e6b-3be4-9a15-be95ca044402 | -8.97288 | -65.96664 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bf50d8f7-79af-3523-bd2a-c41ea8fa198f | -10.88188 | -55.75639 | 2025-09-01 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bf24ffae-6fb1-3a66-9198-8970b4186683 | -9.14641 | -65.8443 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69c4f241-8839-36e6-98a3-f78163975462 | -8.73491 | -62.38739 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a7255ef-dd95-33bf-9f49-f979247ca675 | -9.84406 | -65.05062 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5376010-8887-3c67-878e-f13baf0f2dcf | -8.73321 | -62.39808 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4443da39-d084-3dcf-8a6c-e1cb55d30f7f | -9.45842 | -62.3511 | 2025-09-01 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57153b1f-4e62-3d4d-a646-8e49e04c1cec | -8.75983 | -61.43159 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| b7b96200-ec64-35ca-a4ed-b747c364e790 | -9.6934 | -65.01003 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 540c8641-fd91-395a-9505-8df5e0b523a5 | -10.27923 | -54.2499 | 2025-09-01 05:23:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| edd44b0d-214e-3f50-87d9-be13fbb3cff8 | -3.48302 | -59.5858 | 2025-09-01 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cef307b-c5e3-3ed0-8078-eb5b1ab29e01 | -9.83523 | -65.05814 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49c8c35a-3b33-3ac2-81b3-c82bcfa21555 | -8.96333 | -65.97536 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc0961d8-a156-3dd5-940c-0a4cacd57dae | -8.65543 | -62.93088 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7aa6094f-8e61-3fd4-9e8b-68f1e5885012 | -9.8323 | -65.05315 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5ff1215-dea4-3d12-971f-8a2e2ee2b386 | -9.44062 | -60.575 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 20416ef5-8829-31ac-acaa-2e3abe6c32ce | -9.87783 | -65.00698 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31300d19-2497-3b3f-9364-a1e7ce5c0a29 | -9.1251 | -65.54771 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 106f2d8c-f7ba-3dc4-86d9-5a47e7105061 | -8.74156 | -62.41034 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d95b75d-f6c3-36f7-8cc6-308b85c18e6d | -8.72035 | -62.41429 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 375b101c-3949-3686-8d51-9f92b16a26be | -9.68827 | -65.01817 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99a0476e-aba3-3d20-9ae3-53490746a15f | -9.28269 | -67.64667 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb3fb4a6-78a3-3678-96e4-2e8fc4715859 | -9.88149 | -65.0076 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea9ff10e-34f3-39f5-87e5-ff72f7d55ba0 | -9.64156 | -63.11612 | 2025-09-01 05:23:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41e69015-e8d1-3981-b587-2bf7026afc8d | -7.93415 | -63.00544 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30f7569d-ff62-3315-8824-9d615ebcbacc | -9.83322 | -65.05063 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7b3397f-a68c-386d-aac5-c3d55463d052 | -7.6865 | -61.09639 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d272af1-4d9e-321d-9ccb-cae787fb55a5 | -9.07268 | -65.44452 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 44850e5e-b9be-339b-b519-039e58c7ddd9 | -8.90831 | -64.46746 | 2025-09-01 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69a0136e-de05-32b1-9d3b-66e6b192aca6 | -8.77028 | -61.4297 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce4792f3-94e8-39a3-b16f-83678c3a0b72 | -8.24879 | -72.82004 | 2025-09-01 05:23:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6908327e-5cba-3ca9-87a8-0a65407abb46 | -7.40232 | -62.97057 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31e40954-c957-3db9-bc7f-7520addecc06 | -2.34334 | -47.58652 | 2025-09-01 05:23:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cb28b10-fe44-3129-8c7b-c4e11d629dcf | -11.07581 | -52.06927 | 2025-09-01 05:23:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f828276-d8a7-39f8-841b-46b95c357826 | -7.73381 | -61.57369 | 2025-09-01 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5ae0407-073a-3f69-aa73-53923e697b98 | -8.89867 | -60.56227 | 2025-09-01 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebb27eb0-1b3d-32a2-be82-9e589d6ca87a | -8.50892 | -67.13253 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d04bf3a-2504-38b0-9510-eb7283c2b5b4 | -8.73209 | -62.4052 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 95f42f25-cb7c-3de8-820d-79ef9867161a | -8.63519 | -62.60289 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0e67d894-1b23-3215-aa3d-e8fabd5d1158 | -7.68151 | -61.08497 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 184e5d5f-31fa-3737-b011-e8ccec02ef0a | -7.67821 | -61.08445 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| b34b05dc-bd7d-368c-84a0-3f9510b3dc0c | -8.74269 | -62.40322 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0693a549-9f65-3309-bb66-65b4e33a86c4 | -7.10335 | -63.0395 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2828b9f6-beac-3afc-9067-980e446090f2 | -10.05175 | -48.09756 | 2025-09-01 05:23:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 6ea63218-e57e-321a-8157-5d76b9e40e11 | -9.44449 | -60.57199 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ea479f8-71c9-3ee3-a3ed-e7a6c4b77198 | -8.6605 | -62.92763 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5355a846-f03c-31fa-9ca5-222835b8b640 | -9.8837 | -65.0169 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e67a4e89-0d67-3c8f-8fcf-4c0ec2da8eee | -9.17732 | -67.72928 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f548af4c-64e0-384f-a9e1-4d0ac1c4d68c | -11.07733 | -52.06012 | 2025-09-01 05:23:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7bbd83c-2547-3d43-b11c-e1a2789f748a | -8.84447 | -64.14835 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e724ca0d-0d49-37d4-b47d-316c4d9a9c51 | -9.44781 | -60.57251 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 191fbd59-6f25-3f36-afbc-f42a97e7881a | -8.73712 | -62.39505 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e456a66b-5f62-3eb6-89d9-ffaa5b6471ae | -8.66839 | -62.82774 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3346257f-dd2f-3506-a21a-4929c440fa3e | -8.73378 | -62.39451 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be2a00ac-10db-3a95-b740-88af8f0bcdb3 | -8.84381 | -64.1524 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bad7f5e3-7148-34ec-811d-7ffce0575e09 | -8.50811 | -67.13151 | 2025-09-01 05:23:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dac0fa7b-f460-32b7-a653-093d47e78d00 | -7.81059 | -71.9472 | 2025-09-01 05:23:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c6ce8722-a4b0-3434-a655-1d231e70713b | -9.13477 | -65.84232 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 847fafe2-f8b6-3722-9d12-d73fab94cbb1 | -7.67875 | -61.08099 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.1 |
| e06062d6-4795-3bbd-89d1-f2b250d95ec2 | -8.69579 | -62.41768 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60c485ee-94a2-3ebd-b571-31bb122288f5 | -7.28248 | -60.65678 | 2025-09-01 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cbdc2fe6-3c5f-3650-83fd-a23d10e0a195 | -8.55105 | -63.01618 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 082b8482-1630-3690-bed0-f045e8310706 | -9.48259 | -65.5968 | 2025-09-01 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README78.md)
