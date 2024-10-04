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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ab6df48-a0a2-388e-bb7a-3fc4070098b5 | -13.1443 | -46.3261 | 2024-10-04 10:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 177.6 |
| 78383e8a-927b-3bb0-8a3c-8fdb458aae4d | -13.1447 | -46.3033 | 2024-10-04 10:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 115.1 |
| e467d6eb-dcf3-31d5-b04e-7c7304c02510 | -13.1636 | -46.3231 | 2024-10-04 10:46:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 125.4 |
| cceb3aec-f7e0-3da5-bd56-a8fca314e5e5 | -10.2378 | -47.726 | 2024-10-04 10:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 6bead266-7c86-3e0e-9901-56a49f9941da | -10.2571 | -47.7017 | 2024-10-04 10:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 81ab5177-034a-3027-a064-73dbbab2a827 | -10.2568 | -47.7238 | 2024-10-04 10:56:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 173a4c50-0fe3-3adf-b119-14dd3043e95d | -10.4613 | -50.7317 | 2024-10-04 10:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| 144b0ce2-37f8-34e3-81b4-3c2159325c2f | -10.4424 | -50.7336 | 2024-10-04 10:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 238.6 |
| 0853234d-36c0-3bd3-935d-6a40d58a5732 | -10.4427 | -50.7123 | 2024-10-04 10:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 176.1 |
| fac5e391-e46b-39b3-8807-68557852293b | -10.4616 | -50.7104 | 2024-10-04 10:56:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 128.2 |
| e802a753-e145-3fbc-889e-22df7a49eaad | -10.7445 | -45.6002 | 2024-10-04 10:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 79ac5bb2-8332-38de-a5d4-a60fcd9402a5 | -10.7636 | -45.5977 | 2024-10-04 10:56:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 7fa3959b-e057-3b1e-842a-c340915c87a4 | -11.2369 | -46.9597 | 2024-10-04 10:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 425.0 |
| bfe4eda3-1245-3329-b34d-56bad59c5a82 | -11.2365 | -46.9821 | 2024-10-04 10:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 96418e86-9d14-35b3-953b-8aff43794076 | -11.2178 | -46.9622 | 2024-10-04 10:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 133.4 |
| c64bf1ca-5ca1-3be4-ae80-1dddd8d44813 | -11.2174 | -46.9846 | 2024-10-04 10:56:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| a8ad1c0e-595c-3cd5-b508-f8e081460600 | -13.1779 | -48.6737 | 2024-10-04 10:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 946214ad-9cb0-3834-bdae-fdc439cd35da | -13.1587 | -48.6764 | 2024-10-04 10:56:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| a9c4edbb-eb04-38f2-a0bd-3eccba00b2cb | -13.1636 | -46.3231 | 2024-10-04 10:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 136.6 |
| c992973a-fc88-3111-9cb5-a7b958dbdfbb | -13.1447 | -46.3033 | 2024-10-04 10:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| ffe6de34-1d18-309f-a060-8dc24ac87756 | -13.1443 | -46.3261 | 2024-10-04 10:56:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 6349baa3-e1ec-33dd-940f-83b5d7b79c3e | -10.2378 | -47.726 | 2024-10-04 11:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| e312917c-8d6e-36b1-a217-73023d84ee2d | -10.7636 | -45.5977 | 2024-10-04 11:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 0ad186fd-f180-347d-b3fb-8b6036ba073e | -11.2369 | -46.9597 | 2024-10-04 11:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 252.5 |
| 48bd1424-553f-3cf7-a28a-204f425d6b8e | -11.2178 | -46.9622 | 2024-10-04 11:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 097ee1c7-2be9-32fc-b72a-f76093ce4607 | -13.1166 | -51.1551 | 2024-10-04 11:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 2f2aac01-d09e-3bd0-a532-8f9e06e2d51a | -13.0786 | -51.1385 | 2024-10-04 11:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 3f5c0913-bbe7-3e58-9885-8a7124eb2222 | -13.079 | -51.1171 | 2024-10-04 11:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 4985bd44-809f-39d7-9023-b2377a91c0c7 | -13.1443 | -46.3261 | 2024-10-04 11:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 4fb4ff4f-e3ad-3de5-909f-95d6f4f596c2 | -13.1447 | -46.3033 | 2024-10-04 11:06:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 7cffb775-482b-30bb-be1b-b17804c76ced | -13.0598 | -51.1195 | 2024-10-04 11:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 8e9418b3-e7ff-31dc-a1c1-a0fb1c3f50e6 | -13.1779 | -48.6737 | 2024-10-04 11:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 86.7 |
| d1927909-d191-3d12-8181-68d6ea87a6a3 | -10.2381 | -47.7038 | 2024-10-04 11:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 3f2dcb20-9845-3862-bc1b-5900463b5012 | -10.2378 | -47.726 | 2024-10-04 11:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 171.6 |
| c1003c4d-671e-3396-a39d-fcdfe8b0d616 | -10.2571 | -47.7017 | 2024-10-04 11:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 0da3bc3b-985a-3d54-b28f-88d59748293f | -10.7359 | -46.1465 | 2024-10-04 11:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 35d7a04c-bb65-3613-9b27-cfa903f7c810 | -10.7636 | -45.5977 | 2024-10-04 11:16:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| ece07e5f-8bc0-35ae-a636-7b773bfe5b85 | -11.2178 | -46.9622 | 2024-10-04 11:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 015b5f56-b0f9-3d9c-9b71-258af959e44c | -11.2372 | -46.9373 | 2024-10-04 11:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 86762fe9-3afb-3549-b67c-12dd7a78a736 | -11.2369 | -46.9597 | 2024-10-04 11:16:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 347.7 |
| 5113febc-bd81-3f3a-8f7a-58c12f15aa29 | -13.1636 | -46.3231 | 2024-10-04 11:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 413e8879-f347-3323-b6e3-5c049d282e80 | -13.079 | -51.1171 | 2024-10-04 11:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 195.4 |
| 0cd1c834-d6b6-3259-b84a-1e1d9194789c | -13.0786 | -51.1385 | 2024-10-04 11:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 9218146e-3e80-346e-8c1c-080f402aad5d | -13.1779 | -48.6737 | 2024-10-04 11:16:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 3befa434-2bb1-38a0-b58a-5496a01f2295 | -13.1447 | -46.3033 | 2024-10-04 11:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 12d7dcb2-d804-30ab-a06d-5b6faf092390 | -13.1443 | -46.3261 | 2024-10-04 11:16:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| f933d3ca-24a9-35f8-ba85-df57dc56cd7b | -13.0598 | -51.1195 | 2024-10-04 11:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 67b44aa8-f03d-36d9-abca-780197b97d0f | -13.1166 | -51.1551 | 2024-10-04 11:16:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 0f3e5c39-e916-32e5-b04b-997544bf16f7 | -16.5938 | -57.1783 | 2024-10-04 11:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.3 |
| 5a84d4ab-2582-381a-9c1b-f8f5a338a979 | -9.8353 | -46.7502 | 2024-10-04 11:26:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| bf1c29b1-60b8-3dda-914a-1ce2a3cf5d96 | -10.2378 | -47.726 | 2024-10-04 11:26:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 1fed8991-1169-3435-bc97-b30fd6f7dc90 | -10.7359 | -46.1465 | 2024-10-04 11:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 600f9bb8-0738-3747-8c48-0488022fe618 | -10.7636 | -45.5977 | 2024-10-04 11:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4e8209b0-06b8-3600-87a4-070bb27b7a3d | -10.7355 | -46.1692 | 2024-10-04 11:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 6deb60aa-33aa-3a14-b6d3-20793bdc2b3a | -10.7445 | -45.6002 | 2024-10-04 11:26:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.8 |
| b455d436-ee63-3cca-829b-6dbd7eb61aa7 | -10.8996 | -46.6216 | 2024-10-04 11:26:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f8216732-e9a9-3456-9579-22a231261218 | -11.2369 | -46.9597 | 2024-10-04 11:26:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 165.2 |
| 69b10541-6850-30cc-aa6b-534dcbcf42fd | -13.1636 | -46.3231 | 2024-10-04 11:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1bf40547-a1f6-3ee3-abbc-11445fdc5ab0 | -13.1443 | -46.3261 | 2024-10-04 11:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 4aecf681-9e8d-3498-aa5a-0ac88e8cfa36 | -13.1447 | -46.3033 | 2024-10-04 11:26:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 118.1 |
| c1dd0a1d-68bf-320d-a9a3-4bc742e154ce | -13.1591 | -48.6543 | 2024-10-04 11:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 85.2 |
| fe2432c1-ab52-3756-bdf0-8753e3d7489d | -13.1587 | -48.6764 | 2024-10-04 11:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 813422d9-ce24-3156-a644-34a243569719 | -13.1779 | -48.6737 | 2024-10-04 11:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 0c1f6320-4790-3551-87c5-1f6dbf32750a | -13.0786 | -51.1385 | 2024-10-04 11:26:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 97c279c8-8265-3d26-a213-e08a1290d161 | -13.1595 | -48.6322 | 2024-10-04 11:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| de7e5f05-4043-3b12-b96d-af1bde6dc53e | -13.1787 | -48.6295 | 2024-10-04 11:26:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 1be9a56a-7f29-39ee-9332-99487811dd62 | -15.6304 | -47.2063 | 2024-10-04 11:26:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 6fe83474-633e-3175-9fff-d7b24a1f0924 | -16.5938 | -57.1783 | 2024-10-04 11:26:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 131.3 |
| 8a5e54e9-61c9-36e7-a922-021ec6a4c3ea | -9.8353 | -46.7502 | 2024-10-04 11:36:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f4bdf29d-eb62-36fd-9f53-b7a2864cdb59 | -10.2571 | -47.7017 | 2024-10-04 11:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 8b74de50-5e23-395e-b1f8-8f9cd0d26365 | -10.2378 | -47.726 | 2024-10-04 11:36:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 49528a8d-cdc1-393f-b252-6c8110749b8d | -10.7165 | -46.1716 | 2024-10-04 11:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 1a99cf11-3469-3cda-a30f-75624e24aec0 | -10.7168 | -46.1489 | 2024-10-04 11:36:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 8fd2e08e-f607-36b8-b08f-556c43a09e2e | -10.7636 | -45.5977 | 2024-10-04 11:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 2f971b78-284f-3f49-9784-f6e7ec1a84aa | -10.8805 | -46.6241 | 2024-10-04 11:36:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 4d7967e9-54c1-3277-a8a0-d34a6c1b7419 | -10.7445 | -45.6002 | 2024-10-04 11:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| c9a9623c-f2fc-3eba-81a6-afa016a8135c | -10.7355 | -46.1692 | 2024-10-04 11:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 167.1 |
| d108cdef-9eac-3c21-9388-43eed51af906 | -10.7359 | -46.1465 | 2024-10-04 11:36:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 247.4 |
| ff3ecdcf-bbf7-326b-a7d5-96292376d9fe | -10.8992 | -46.6442 | 2024-10-04 11:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| ce438d9a-44af-3bb7-a728-412d663ac990 | -10.8996 | -46.6216 | 2024-10-04 11:36:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 105.4 |
| f93a307d-7558-3215-99ec-d6daaa03d588 | -11.2369 | -46.9597 | 2024-10-04 11:36:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 319.6 |
| c1bde7bd-b0a4-3552-bc8d-6060721b0da0 | -13.1443 | -46.3261 | 2024-10-04 11:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 60097eb6-60c3-3ee9-80bd-e932624fcf8f | -13.1595 | -48.6322 | 2024-10-04 11:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4c3291f5-c5a3-35fb-911c-cffaf02ec7d1 | -13.0786 | -51.1385 | 2024-10-04 11:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b64f0033-6c84-3103-8cc1-5d8b05228cd6 | -13.1166 | -51.1551 | 2024-10-04 11:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| f2c4fbfd-bf5f-368c-b135-7d3e142460a3 | -13.1779 | -48.6737 | 2024-10-04 11:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 452c978d-10ea-3ab7-8344-a3968d4a0dd7 | -13.1791 | -48.6073 | 2024-10-04 11:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 90ea0f1f-ea9f-3f05-ae38-e55b5504ba84 | -13.1447 | -46.3033 | 2024-10-04 11:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 090b4c16-28fa-3f92-bc9a-92005a96ec83 | -13.0598 | -51.1195 | 2024-10-04 11:36:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e4541ac0-6240-36f5-ad8d-70931d370aea | -13.1587 | -48.6764 | 2024-10-04 11:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1e14bfb3-b4c0-3922-8c17-44daec7cf082 | -13.1787 | -48.6295 | 2024-10-04 11:36:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 131.2 |
| e0d25115-c585-38e3-ba84-a86261a58d02 | -13.164 | -46.3002 | 2024-10-04 11:36:20 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 6ded1573-76e5-3cd6-84a5-600320d61620 | -13.1636 | -46.3231 | 2024-10-04 11:36:20 | GOES-16 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 7bc3daca-7b0e-3e9b-9048-3e628977789f | -15.6304 | -47.2063 | 2024-10-04 11:36:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 0f68da68-6a96-3c5e-abdf-f2d8ca455369 | -16.5935 | -57.1988 | 2024-10-04 11:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 784955ab-3b36-3a63-8927-4a277902a9e2 | -16.6133 | -57.176 | 2024-10-04 11:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| 7faac2e7-6849-3fc4-b7d3-0c6921e4e3b5 | -16.5938 | -57.1783 | 2024-10-04 11:36:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 180.4 |
| e9dbb8ce-9109-3dda-a616-5311e7b18a8e | -9.8353 | -46.7502 | 2024-10-04 11:46:02 | GOES-16 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| f5d6dc6f-0e2d-3139-9570-4da1744d37f7 | -10.2378 | -47.726 | 2024-10-04 11:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 2f05d253-b5df-3b04-a0c4-4bd1ddd5014b | -10.2381 | -47.7038 | 2024-10-04 11:46:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |


[Clique aqui para ver as próximas entradas](README186.md)
