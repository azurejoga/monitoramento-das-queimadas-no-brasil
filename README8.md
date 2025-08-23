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
| 85e41da4-8512-3372-bad4-976a83ae4219 | -18.9683 | -46.9278 | 2025-08-23 01:30:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 189fb1a2-2e62-35ad-9198-4c2921083b1b | -9.5179 | -60.5461 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 127.5 |
| ddbda61a-1852-3b37-80c5-3a3e3748856a | -9.9681 | -60.1743 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 268.8 |
| 97aa8010-7ae8-33f1-8183-c330a3f65600 | -8.9106 | -62.4289 | 2025-08-23 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.0 |
| e7f65c58-3017-3501-98a8-c90d81192c4a | -14.6706 | -54.9142 | 2025-08-23 01:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 58.5 |
| a836d7e9-7347-37b5-beab-36557d3abeaa | -5.7429 | -57.6009 | 2025-08-23 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 01f90184-aa2d-3369-b1e2-b24177e6c2af | -13.0114 | -45.222 | 2025-08-23 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.6 |
| ffa0e4e8-0884-3ad5-95c5-0358a0b9e10d | -17.8278 | -52.0433 | 2025-08-23 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 74e31fa3-41cf-32d8-9580-7fce624917fa | -9.1897 | -59.6171 | 2025-08-23 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| 7370788b-fee9-31ef-852b-39994aa069a8 | -9.1895 | -59.6364 | 2025-08-23 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| bd6722b5-7e3c-3281-b592-88de5600f181 | -6.5781 | -59.871 | 2025-08-23 01:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 27b8eb88-131f-3b6c-8220-a0d52fcea979 | -9.5181 | -60.5075 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| ef04a8d5-bff9-3747-9890-b973cd0bd0ee | -9.5177 | -60.5653 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 6957901a-e593-3cbb-8154-870f39a3338b | -9.5366 | -60.5258 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 5cf3fe5a-6ee8-3ff0-a9a2-5a39f5d96acb | -17.5985 | -46.5481 | 2025-08-23 01:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 3a7a1742-633e-33cc-ac04-ac358a562e44 | -20.0963 | -47.791 | 2025-08-23 01:30:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9c9d84e7-a21c-33aa-a6ad-b77862154457 | -17.5779 | -46.5756 | 2025-08-23 01:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 0f4fe0e9-161f-37c4-920c-abb1c5d7a075 | -5.7615 | -57.5807 | 2025-08-23 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 6a2ab73a-1504-3e99-b55b-2d0738778ddb | -13.3777 | -46.2208 | 2025-08-23 01:30:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 63.9 |
| b6b52e65-7046-3171-985c-67fc3f447b06 | -3.4439 | -49.051 | 2025-08-23 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 3b237a6b-8044-37d0-b32a-59fa0530182b | -11.1816 | -55.0211 | 2025-08-23 01:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c6313bf5-6e60-3cce-ac55-b8cc10d313da | -6.4327 | -41.2114 | 2025-08-23 01:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 35eb472d-e3fe-3462-b079-b86b4b3a191b | -17.8079 | -52.0465 | 2025-08-23 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 146.4 |
| d460ad80-a751-3760-8cc2-9c4489b0e3f8 | -9.9495 | -60.1754 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 314.3 |
| 1af69ccd-ac72-3282-88e7-97dd86931743 | -12.9921 | -45.2252 | 2025-08-23 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e805e1de-9db3-3eaf-8fea-653f5b4d97a8 | -9.4449 | -47.6585 | 2025-08-23 01:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 35e35470-05c7-38e0-bc1f-5bdae7f4a3ca | -7.0352 | -44.6396 | 2025-08-23 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 99583b8b-c1d0-3aed-b744-fb12b49ba37c | -17.5979 | -46.5715 | 2025-08-23 01:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 2b167053-c8a8-3b5b-8767-dd8fe72d85e0 | -9.5365 | -60.5451 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 9d244813-d23e-33aa-9ced-5a9e1d635818 | -5.7431 | -57.5814 | 2025-08-23 01:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6390e18e-fe98-3e8e-9884-ad2d832ca1f5 | -6.6231 | -44.5608 | 2025-08-23 01:30:00 | GOES-19 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| bd362cd1-89fc-3fd3-af1d-70fb0d073d4f | -9.9492 | -60.2141 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| deb3663c-8ab7-3c91-8701-45c19e36e365 | -9.9493 | -60.1947 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 611.1 |
| 2b98a3bd-c9a8-3d7b-94b2-dad0e47b9ddf | -9.1712 | -59.5987 | 2025-08-23 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 937b4ada-6656-3082-b42f-f9405848ddb4 | -20.097 | -47.7676 | 2025-08-23 01:30:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 0fa17f66-c914-3232-9981-52bf1001c819 | -17.8075 | -52.0683 | 2025-08-23 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 82894bef-690c-3680-9d0c-5785ed6f4960 | -6.6044 | -44.5624 | 2025-08-23 01:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 61119f5f-3964-336e-a074-fd3882c36644 | -9.518 | -60.5268 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 7d84d6b5-6f9d-387c-bc9a-89ea0bc95c0b | -17.8273 | -52.065 | 2025-08-23 01:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 116.3 |
| f5056ccc-d0da-3bbf-ae90-0e117d18dc1e | -17.2751 | -46.777 | 2025-08-23 01:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 0e49544f-b651-335e-bcea-caba5ff01f73 | -6.4138 | -41.2132 | 2025-08-23 01:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 7dfe79cd-8069-3b64-8e33-96cb97ef5b5d | -8.8921 | -62.4297 | 2025-08-23 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 59dd4ece-fb73-3ea0-b68f-f447f3f92489 | -9.968 | -60.1937 | 2025-08-23 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 528.2 |
| 99fb29c1-4f2b-3bba-aad4-5c9f65815e45 | -17.5785 | -46.5523 | 2025-08-23 01:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 9879f6e3-c06d-32a4-a58f-060d41e983f9 | -9.9495 | -60.1754 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 258.7 |
| 8d4fea1a-6117-3c40-8bdc-9175dbcee211 | -9.9678 | -60.213 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| ec4e5e0c-c585-32c9-994a-dde1d0523e21 | -17.8075 | -52.0683 | 2025-08-23 01:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| fbcb8bd0-2bce-3cb3-8902-a8f70f89b50b | -6.4138 | -41.2132 | 2025-08-23 01:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| 25d5c506-e641-319d-950c-0ef430f97254 | -9.5179 | -60.5461 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| edd9db40-f477-3dad-b5ea-7cfc94279d42 | -7.813 | -63.5656 | 2025-08-23 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 116.3 |
| afc3823f-151f-3b53-a8c9-a320b6bf0cb7 | -9.1897 | -59.6171 | 2025-08-23 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 22d0ddac-07a4-3c0e-b257-96d90d99e3cb | -9.968 | -60.1937 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 446.1 |
| bdf4f5fa-ad93-3c77-a992-3e70ee06ca69 | -9.5181 | -60.5075 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 6588c739-7016-3c1f-bfb5-b262dd2ef36f | -9.4449 | -47.6585 | 2025-08-23 01:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 624d5bb0-bf1b-3567-86c4-522c2e09f069 | -6.4327 | -41.2114 | 2025-08-23 01:40:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 87.9 |
| 55c7d7ef-5760-3741-9333-f589d0e626a6 | -7.0352 | -44.6396 | 2025-08-23 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a824d09a-e1ab-3d4e-9094-2795ac36f282 | -9.9492 | -60.2141 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| c1cff6f8-a502-3fb6-bc40-6f537e3fddc7 | -7.8131 | -63.5468 | 2025-08-23 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 11be67bd-d69a-3ff7-b9a9-b2404e9c8573 | -20.097 | -47.7676 | 2025-08-23 01:40:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 0ba5728a-96bc-3586-9359-54a64a625f6e | -3.4439 | -49.051 | 2025-08-23 01:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 0d95a4bf-d555-3ee2-9e53-a458e1b3cbac | -8.9106 | -62.4289 | 2025-08-23 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 2cbe6f78-9135-3954-bc54-c0e61e8856b0 | -17.5979 | -46.5715 | 2025-08-23 01:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 8ba7ca55-c3c1-321c-a1c9-c6b67b220ae1 | -9.9493 | -60.1947 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 508.9 |
| 9f00375d-9803-3cc4-aff1-69ebaf3fde38 | -9.9681 | -60.1743 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 227.8 |
| cf44da36-df77-35ca-bfe9-cd5be28730de | -9.5365 | -60.5451 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7121d4be-3ed4-3cf8-8264-4903c64bfede | -7.0164 | -44.6413 | 2025-08-23 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| a5ccacc6-737d-3261-a99d-f5c075ff7db0 | -8.8921 | -62.4297 | 2025-08-23 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 87e9cc29-bf8c-38b4-84d8-478d36317545 | -9.1895 | -59.6364 | 2025-08-23 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| ac4ca3a7-5212-340e-af01-49855f61e4f5 | -6.6044 | -44.5624 | 2025-08-23 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 82869d47-9d49-3668-ad58-0af39dd569f1 | -14.6706 | -54.9142 | 2025-08-23 01:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| c8460ab7-d3ed-3b23-8c2a-ce8eba23fbb3 | -17.5985 | -46.5481 | 2025-08-23 01:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 7269d1b6-cf67-3431-9d08-ad8a4eab277f | -6.6041 | -44.5853 | 2025-08-23 01:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 68ca6d7e-9b97-3707-a3fa-43aa004f1bb5 | -9.5177 | -60.5653 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 111.8 |
| a0cad817-aaeb-3712-9ece-90d4c7914cc7 | -9.1712 | -59.5987 | 2025-08-23 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e3607d38-2daf-30c0-9634-cf704cc3c92e | -17.2751 | -46.777 | 2025-08-23 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 29dcbf1e-2fa8-31ab-a746-b801759304ed | -12.9921 | -45.2252 | 2025-08-23 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| f33a5587-293d-3f47-826d-5e6f73b2c554 | -5.7431 | -57.5814 | 2025-08-23 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 38ee0ea2-99a7-3abd-8375-6f67380a863f | -5.7429 | -57.6009 | 2025-08-23 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 59e381c0-c45f-3dfc-87f0-12a1388aafd1 | -9.5366 | -60.5258 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| c4f0e365-2404-3d85-a920-f4023c2692f8 | -5.7615 | -57.5807 | 2025-08-23 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 51ed25fb-352c-3ec2-b3ac-b05932a3fe58 | -9.518 | -60.5268 | 2025-08-23 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| ce5c9e3c-3f96-33ff-a0d9-ca255521cb98 | -17.5785 | -46.5523 | 2025-08-23 01:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 136911d5-ad1e-3532-9576-eb006148e673 | -5.7614 | -57.6002 | 2025-08-23 01:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 6e797a22-d01b-3832-9c37-5952d253a361 | -17.2757 | -46.7538 | 2025-08-23 01:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 78f55ffa-21a2-3844-ad6a-934338d0e388 | -17.5779 | -46.5756 | 2025-08-23 01:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 54.2 |
| adfef902-15e2-31a7-b377-d5c58cfd82f6 | -11.11108 | -62.66574 | 2025-08-23 01:47:00 | TERRA_M-M | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0bf55b2b-cac5-36b4-a6fa-402ccf8b069e | -15.02022 | -54.87074 | 2025-08-23 01:47:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 56cf9771-22a7-3a22-a2e8-19043c45db93 | -15.01889 | -54.87756 | 2025-08-23 01:47:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 30b55c77-56b7-35ef-ba5c-250894a46a9f | -14.28147 | -60.38639 | 2025-08-23 01:47:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 7bb50b1b-1b5e-3479-8860-d5b15ae3c857 | -13.02284 | -56.83697 | 2025-08-23 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| bc805516-4a1e-371e-801f-823e72206fc2 | -14.6676 | -56.60172 | 2025-08-23 01:47:00 | TERRA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| d176e06e-83be-38ff-b084-35ba2c3071f4 | -13.02815 | -56.84128 | 2025-08-23 01:47:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 3c54cd33-fd50-36d8-804c-d64ad03c81ba | -14.66231 | -54.93151 | 2025-08-23 01:47:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 80.0 |
| fed8ba6a-1ca6-336d-a081-fac4e0e5861a | -14.32161 | -58.55407 | 2025-08-23 01:47:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| aea24a38-f1a9-31f6-8ecf-7393f9b2572b | -14.67177 | -56.60637 | 2025-08-23 01:47:00 | TERRA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 59.5 |
| baa2775b-b9ed-303b-9fae-cd909db4f0ba | -14.66335 | -54.92424 | 2025-08-23 01:47:00 | TERRA_M-M | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 30cfee4d-f6f3-3cbe-8be9-b71d024b3246 | -9.1604 | -59.60734 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5dc68aea-2687-36fc-9891-8b724a8988b8 | -9.23312 | -60.47966 | 2025-08-23 01:49:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.0 |
| f49b85fd-63d4-334c-a20d-f81944e45c15 | -6.58304 | -59.87425 | 2025-08-23 01:49:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 313b3811-935c-3042-9e80-359b53ca0a82 | -9.5215 | -60.5445 | 2025-08-23 01:49:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |


[Clique aqui para ver as próximas entradas](README9.md)
