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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa1abfa2-b0ad-31f4-9c10-5193e9266f0d | -1.8424 | -46.6261 | 2024-11-24 00:40:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b0114ffb-d8e0-3aa6-87b0-046770febed2 | -0.8907 | -52.7481 | 2024-11-24 00:40:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| fa319b41-3902-3dcf-aa56-551b69cd2472 | -3.0582 | -53.2192 | 2024-11-24 00:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b90ddfeb-ace6-33d4-95de-2d9b173513a7 | -2.7149 | -46.2713 | 2024-11-24 00:40:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 8bb422b4-4860-3682-8aab-926cbfd18ffd | -1.3666 | -53.8362 | 2024-11-24 00:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 145.6 |
| 33c3632c-2ba2-370b-888a-a27006e8c4d7 | -4.2234 | -48.6986 | 2024-11-24 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 1d480c0e-7b70-38ef-908b-f177e0dbb098 | -2.7411 | -49.1162 | 2024-11-24 00:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| a4bbd279-e3df-3412-bcf2-bec3d5bff047 | -5.0998 | -43.151 | 2024-11-24 00:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 930c5435-a569-3928-85cd-549a22b6adac | -4.242 | -48.6978 | 2024-11-24 00:40:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 20399b99-48d6-3483-b1ef-8680b521f2fe | -20.32866 | -48.81892 | 2024-11-24 00:43:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 68b69db0-11c0-3a0a-a358-cc92b88c65d3 | -20.31742 | -48.82038 | 2024-11-24 00:43:00 | TERRA_M-M | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 10.6 |
| cf77a68d-f43d-3a49-b572-b363df2fc592 | -6.83988 | -44.39461 | 2024-11-24 00:47:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| a1ced246-4225-36c3-8021-dc70242830a3 | -5.00293 | -42.94373 | 2024-11-24 00:47:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| fc2c0852-7550-3c7e-b8ac-6f5c2407ce35 | -5.66043 | -47.34051 | 2024-11-24 00:47:00 | TERRA_M-M | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 32281cbf-4055-39b7-8f3e-524cef7ccf0f | -5.1059 | -43.1642 | 2024-11-24 00:47:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 36e716de-50df-3973-934f-3216daa33ccf | -5.87504 | -42.76622 | 2024-11-24 00:47:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| cd99ea51-2338-36bf-84eb-053ec62f5f32 | -6.83842 | -44.38431 | 2024-11-24 00:47:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8f42ea1a-c93d-30b3-8695-2d4e6963fb62 | -6.35561 | -47.30186 | 2024-11-24 00:47:00 | TERRA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1dbb28df-e888-3b10-8142-5ab5efb3d192 | -6.27296 | -42.20507 | 2024-11-24 00:47:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 0a09e1a4-c272-313f-93f3-d2811730b544 | -5.07398 | -42.57502 | 2024-11-24 00:47:00 | TERRA_M-M | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3e17d9b1-8841-3ed8-aea1-4975edd74185 | -5.9528 | -48.05635 | 2024-11-24 00:47:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 5daeb4de-aefb-3d8d-b64d-8338de0674dc | -5.59101 | -45.21285 | 2024-11-24 00:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4c827f07-b07d-3092-9be5-f817a6278ffa | -7.69022 | -42.98717 | 2024-11-24 00:47:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 3ee679c7-5803-3963-99c4-b84d84adeb27 | -5.44927 | -45.50909 | 2024-11-24 00:47:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0f8fefad-716c-383a-8714-6439d2b7f389 | -5.09939 | -43.15779 | 2024-11-24 00:47:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| d776ad56-1069-3384-a749-a8ffff83bb52 | -6.84382 | -44.38762 | 2024-11-24 00:47:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| b5ddca8b-d69c-3725-9bed-29cb3322b271 | -6.63758 | -47.34389 | 2024-11-24 00:47:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 34ab4c39-9a5a-3529-924e-1d48fbcafd34 | -5.41102 | -44.77565 | 2024-11-24 00:47:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| be2bbfbd-1338-3c24-820a-6472df6e3d4c | -7.58035 | -49.41141 | 2024-11-24 00:47:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2f1fedea-2a08-321b-8102-651059191ccc | -5.11451 | -43.14956 | 2024-11-24 00:47:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| cff53d91-5194-349a-9574-e7d745abf013 | -5.10395 | -43.15117 | 2024-11-24 00:47:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 1971e3a5-f67a-3645-b0a9-01d222281c88 | -5.55362 | -45.33218 | 2024-11-24 00:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0c3a625e-52d9-34bd-8487-9541d7685088 | -6.05888 | -41.92902 | 2024-11-24 00:47:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 2be4df71-03f7-3d9c-8b35-bf8da09c9231 | -7.68841 | -42.975 | 2024-11-24 00:47:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| add83fcd-47a2-3c57-80b0-0f57f46daad6 | -5.35577 | -45.03563 | 2024-11-24 00:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 454241dc-2c21-37f2-b6a6-b5687f4495a1 | -6.63882 | -47.35283 | 2024-11-24 00:47:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b85ef1c1-39b8-3d6e-9aca-afeff00f7fb9 | -5.00489 | -42.95695 | 2024-11-24 00:47:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| c0af5165-1196-3ee1-9914-38e83acd4a14 | -5.22639 | -44.9081 | 2024-11-24 00:47:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 307c0ca5-720f-3e08-b84c-9fc9b3031579 | -5.40958 | -44.76552 | 2024-11-24 00:47:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| dc3a7deb-3931-32cc-9743-93e7e5ca2692 | -5.46338 | -44.83425 | 2024-11-24 00:47:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 154fd4d2-5959-35a7-990f-082ea9defd61 | -6.05461 | -44.05139 | 2024-11-24 00:47:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| ae739f04-d2ea-3c95-bb46-9eeaf2de6a5e | -5.60617 | -46.29215 | 2024-11-24 00:47:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 51d29d4d-1817-35fd-9185-4ebac72bdd15 | -5.09753 | -43.14478 | 2024-11-24 00:47:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 8abda90e-f788-35cc-9b66-83ff69d06a69 | -6.68977 | -48.87004 | 2024-11-24 00:47:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 455a8a81-3402-35bb-a59c-0d12f814510e | -5.08002 | -44.16525 | 2024-11-24 00:47:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 3d07e76f-913b-3a46-b8d1-c6a6ef4fe482 | -5.08164 | -44.17632 | 2024-11-24 00:47:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eead45f9-d50f-31b7-80a8-cca47688cfe0 | -5.41146 | -45.75928 | 2024-11-24 00:47:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 56af88ec-dd1f-3589-b003-37cd7c797273 | -5.95154 | -48.04722 | 2024-11-24 00:47:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| e45b0692-1735-3cf3-b10a-161dff9e980e | -9.82377 | -48.17199 | 2024-11-24 00:47:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 560ca4fa-5c10-3693-9eb3-360061d95b37 | -5.06366 | -43.69975 | 2024-11-24 00:47:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 822011e6-b5e3-333a-8e5d-6ef18467d6a4 | -3.28783 | -49.91168 | 2024-11-24 00:49:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0a82912c-83b1-32e8-bd81-ec438818ab55 | -1.45116 | -48.2031 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c61ec41d-9423-3616-a064-35f1c58566ec | -2.70325 | -46.28355 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 34.7 |
| fc9038b7-f1eb-3643-a2d1-14909ab6b9d6 | -2.08456 | -47.05909 | 2024-11-24 00:49:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e5ebb467-a106-35f1-b383-bb917580b3a4 | -2.95571 | -45.12926 | 2024-11-24 00:49:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 06bf762c-cd7e-3e96-8033-a2e841e8e5f7 | -2.70193 | -46.27427 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e10cbe86-9135-320c-90a7-28ed32446111 | -5.11956 | -46.17152 | 2024-11-24 00:49:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 34345917-151e-33f8-a073-d16402135aa3 | -4.26337 | -48.69056 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| f8d5fb28-f22d-3e81-b98b-caa892ebafb4 | -3.49136 | -49.91319 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ea7333d7-66cf-364a-a611-5b0b03ffac1d | -4.27086 | -46.29278 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9f93fb6e-bf39-3d68-ab46-1e8f0a85d235 | -2.64237 | -46.56998 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 603a3095-cbf0-3c85-b841-9f17fbb0051f | -4.60005 | -44.73286 | 2024-11-24 00:49:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 36517c11-f870-3f4f-b27d-440d1e9aa4e2 | -1.77802 | -53.62949 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 76c30582-58ac-3afe-a7ac-ab8de111e727 | -3.91466 | -48.09879 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1c8a48b8-ffae-39c6-95e7-fa1f735c8254 | -0.9481 | -51.64477 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5f0b993b-8d84-3750-b4e5-7ddc40a258dc | -1.61024 | -54.42442 | 2024-11-24 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 5bf75c53-8871-3b6b-8370-cc1adf759d87 | -3.68118 | -45.77 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6a12ea9e-de69-3009-be17-34d556875d2e | -3.49565 | -50.47482 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d37a7854-f425-3159-b64a-1643dd237930 | -1.27804 | -47.68588 | 2024-11-24 00:49:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 70a981fd-7347-3c81-a076-4461a5f42791 | -4.23761 | -48.63748 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| af0d8bae-bba6-38ae-a077-16430827ad4c | -2.00411 | -46.28912 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 3d6cf0d1-09c2-31d0-b6f6-707700b2b620 | -3.2957 | -50.35765 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 41a20a69-016e-3fc9-b063-871f3f6bce08 | -4.40715 | -45.62673 | 2024-11-24 00:49:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3eda76a8-0431-3042-8fb9-5fc96763a9a1 | -5.444 | -46.91427 | 2024-11-24 00:49:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b41e173a-b864-3983-9967-c8331e8a6c8f | -2.16595 | -53.79205 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 68fee195-a811-3734-a00d-4ba46e4dded2 | -1.82156 | -46.6294 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 179.3 |
| 941ba083-445f-369c-9d97-4b8cdab7c729 | -4.08856 | -46.8312 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f4b70a02-197e-377d-bad6-df6aaf6b5cc2 | -1.12951 | -48.34474 | 2024-11-24 00:49:00 | TERRA_M-M | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e4266ca4-7c8e-33ae-914a-11053ae9c9a9 | -2.61755 | -46.26418 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5397dd3b-e64e-37c5-bb7e-a307bc69fe9a | -3.26732 | -53.81926 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 6ceaea4a-cde3-32d1-aa3b-6b02335112b1 | -2.70681 | -46.11179 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 950ea0fc-375c-3a94-b7fd-6ce10d943a7c | -3.6335 | -52.2519 | 2024-11-24 00:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cff26c6e-c6ec-3530-ae8b-50e522726894 | -2.66683 | -46.15246 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9d8f03f9-1ab3-3741-a1a7-a5dc1ef4b49d | -5.19267 | -49.15035 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| f96f8f00-9fde-3af1-8f9d-08ac293d53a2 | -2.5568 | -46.55099 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| d5cab64e-5476-3199-8115-81c7d7cf7b1d | -2.21284 | -48.91078 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dc7a996f-4158-363a-92bd-489892a4699a | -1.21968 | -53.69188 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| e45cbf7b-e5e2-324e-b0f2-b929615f3547 | -4.07968 | -46.83249 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7ef80919-5e24-379a-aba4-70dddf135067 | -3.39346 | -50.32723 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| f66aae0e-f9ef-3da9-ac29-65490061b14c | -2.71362 | -46.29152 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 34.8 |
| abeb5515-a42b-3ec8-85f4-b7bb8dc63ff5 | -1.88316 | -50.12128 | 2024-11-24 00:49:00 | TERRA_M-M | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 00c8304b-ff18-3536-9486-b5b6e1acb893 | -1.04639 | -51.744 | 2024-11-24 00:49:00 | TERRA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 1f60331b-1b02-3bbb-81a7-bd2e42dd7411 | -1.01941 | -48.07283 | 2024-11-24 00:49:00 | TERRA_M-M | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e0ea4697-dbc2-310c-9468-e62994670b15 | -3.13565 | -45.37138 | 2024-11-24 00:49:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 71fa0991-e86d-325c-9210-d92473496c3c | -3.90946 | -50.58865 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 02fedf78-a7c6-3453-a09d-31683b220786 | -2.46044 | -49.03635 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 36.1 |
| acfea357-ddaa-3fbd-859a-7ff324c483e6 | -2.18334 | -53.64007 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 83dee1b0-0060-3a82-8524-3e3e480e812d | -1.51446 | -54.19924 | 2024-11-24 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 0f34baaa-ebf9-3559-87c8-71e8d5619e7b | -2.25502 | -46.83072 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ae25aa00-85f8-3dae-99c5-0821c5704f06 | -3.11011 | -54.01331 | 2024-11-24 00:49:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |


[Clique aqui para ver as próximas entradas](README14.md)
