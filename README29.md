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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43e72f81-6e3b-389e-a47e-588a1cce300a | -8.6598 | -63.258499 | 2024-10-12 02:04:56 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 38ed9a4b-04ec-3a3a-b12b-22f577a13462 | -8.6501 | -63.261002 | 2024-10-12 02:04:56 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ff5e120a-e642-3ca7-8791-d1d7c963be26 | -8.594 | -63.242699 | 2024-10-12 02:04:57 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8f664779-a9b6-30da-aabe-45fee2e7fe27 | -8.5978 | -63.2579 | 2024-10-12 02:04:57 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bddb2377-17d8-3c05-949a-da996ab455f8 | -6.7306 | -59.3326 | 2024-10-12 02:05:11 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca3f7f65-d722-3dc5-8419-0e968d1c8d4d | -6.742 | -59.297401 | 2024-10-12 02:05:11 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa608ca8-d7ce-39a1-8525-7646fa79bc6b | -6.7497 | -59.327702 | 2024-10-12 02:05:11 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 733ef3c6-d71e-3e32-9467-1b2cdf9148e7 | -6.7324 | -59.2999 | 2024-10-12 02:05:11 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dcc949f4-40dd-3dc1-94bb-c54fb44ad8da | -6.7401 | -59.3302 | 2024-10-12 02:05:11 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4048db1f-eff6-37e9-b4aa-bf95a02b138a | -6.7228 | -59.302299 | 2024-10-12 02:05:11 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73735c7f-504f-37d7-9f8a-11b2c39aaa2a | -1.5877 | -53.3494 | 2024-10-12 02:05:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| a4ddef10-c4c5-33c2-9c29-47935176b26e | -1.8793 | -54.4312 | 2024-10-12 02:05:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 8dd0da1a-2760-3fa9-a30a-0556270ab686 | -1.8977 | -54.4309 | 2024-10-12 02:05:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| a3afa3f3-e1f2-3f6f-92c2-82eb5a71a17b | -2.77 | -51.3829 | 2024-10-12 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4476cff5-b503-314c-83a5-33058d19e126 | -2.7701 | -51.3622 | 2024-10-12 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| ef5f5c12-b125-32f2-9dfc-530d9e75be47 | -2.7884 | -51.3825 | 2024-10-12 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 1dc3b238-b3da-39fd-a95c-edc563934984 | -2.7885 | -51.3618 | 2024-10-12 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 95fed80f-8842-3388-99bb-2a28d3a8cac5 | -2.8319 | -49.5385 | 2024-10-12 02:05:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| f611e6e3-f7b3-3166-9b57-8036dfc0781f | -3.0311 | -50.5642 | 2024-10-12 02:05:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 7a2ded3f-2150-32dc-aabe-aa49e078f57a | -7.3028 | -64.666298 | 2024-10-12 02:05:23 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b61f1642-9445-36c1-b0d7-56490b560e6c | -7.2998 | -64.653503 | 2024-10-12 02:05:23 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4854ea58-3f6d-3221-a0ac-999792a3f00d | -3.2136 | -46.7843 | 2024-10-12 02:05:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| a410e7c3-8d7b-3d65-a14d-a06dcfaaea8d | -3.483 | -52.8211 | 2024-10-12 02:05:26 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| b2d2ef09-2383-3b1c-bad0-277a504cf337 | -3.69 | -47.9451 | 2024-10-12 02:05:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| daaeeafd-fb87-3485-b50e-2355c67f330c | -3.6901 | -47.9234 | 2024-10-12 02:05:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 9ade1fdc-6603-32ce-a3ef-34e0114b5e69 | -3.7086 | -47.9444 | 2024-10-12 02:05:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 06bbae00-991b-32bb-9a46-6fe68ca3b74d | -3.7087 | -47.9227 | 2024-10-12 02:05:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 754de773-34e8-340b-ab17-11fc74338d1f | -3.8167 | -52.3403 | 2024-10-12 02:05:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| b9340516-cab8-33e6-9bce-88ff90483d02 | -3.9208 | -46.4459 | 2024-10-12 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| d15c1833-8aa7-32b1-b3d8-c31ae61c2862 | -3.921 | -46.4237 | 2024-10-12 02:05:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 93a0fcb3-be94-3556-ac13-a14fad7afcdc | -3.9394 | -46.445 | 2024-10-12 02:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 122.4 |
| 55e7df8f-757a-3939-a9d0-dc5fbfd626cd | -3.9396 | -46.4229 | 2024-10-12 02:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.4 |
| a7bb5d1f-8dfc-36e2-915e-59b514dac31d | -3.958 | -46.4442 | 2024-10-12 02:05:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.0 |
| dba083a4-240c-3758-94f6-d79b3d2e2801 | -4.1148 | -48.2515 | 2024-10-12 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 5f699196-d93b-313f-ab36-f14f53bd40c4 | -4.2665 | -50.9594 | 2024-10-12 02:05:31 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 8f0bf4e1-36bb-32de-8a68-bdb7bddaa464 | -4.3782 | -50.8087 | 2024-10-12 02:05:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f889f03f-be9b-34d1-bd28-4e6b59a46e73 | -4.7188 | -60.7882 | 2024-10-12 02:05:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| bbdc2332-d46e-35a6-a17e-7715ff2f71d7 | -4.8562 | -45.6838 | 2024-10-12 02:05:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 5aca9d67-617d-3364-b509-e1d3b9467e2e | -6.0791 | -44.6276 | 2024-10-12 02:05:41 | GOES-16 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1d57f60e-c039-321f-860d-1feee7795495 | -6.7285 | -59.3267 | 2024-10-12 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| a3258078-0dfb-3354-8d68-c85c6ebf7104 | -6.7469 | -59.3452 | 2024-10-12 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| 5823b53e-ff4d-32f3-a86e-79d2a57d3a3f | -6.747 | -59.3259 | 2024-10-12 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 183.9 |
| ed39f27e-0948-3b99-a4ba-0f1827f28037 | -6.7654 | -59.3252 | 2024-10-12 02:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 20912379-e34a-3443-bb2b-ae81896b4ad9 | -7.292 | -64.6676 | 2024-10-12 02:05:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| d34e9fe8-0968-3a8b-b667-00d3f1dd157c | -7.3105 | -64.6671 | 2024-10-12 02:05:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| a9385cf5-6a90-3fe3-8865-ddc87d7cfb46 | -8.4231 | -55.4704 | 2024-10-12 02:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| abb01747-b411-30ab-bc58-c1710581fd8e | -8.4233 | -55.4503 | 2024-10-12 02:05:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| c056908e-1ea6-3605-8595-d941ff23f380 | -10.4079 | -61.2685 | 2024-10-12 02:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 2df8a86a-b925-3edf-b3d1-97add7910313 | -10.3898 | -61.1925 | 2024-10-12 02:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 83e6c65a-30ca-3bd4-895a-1f978f5970f5 | -10.3897 | -61.2118 | 2024-10-12 02:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 4ba21689-753a-3afe-9639-9b26daa76902 | -10.3892 | -61.2695 | 2024-10-12 02:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 9cb6ea84-dcd7-3600-a329-c6c9bd1d6402 | -10.3708 | -61.232 | 2024-10-12 02:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 29.2 |
| ef9d127c-0ae4-36c6-a63f-ae23464eb9b6 | -11.2761 | -60.5038 | 2024-10-12 02:06:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| e9e37d96-71bb-396e-96ad-d3ad45f56bb6 | -11.8377 | -58.8445 | 2024-10-12 02:06:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 329d69b6-6aeb-3626-bfc4-6a10b31175c9 | -12.456 | -54.5554 | 2024-10-12 02:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 67e115e8-977e-3856-b720-fca0ca8fe22e | -12.4558 | -54.576 | 2024-10-12 02:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| c20bace9-d429-307e-bd92-9dde1ee378c0 | -12.437 | -54.5573 | 2024-10-12 02:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 35d9628f-309c-3a2c-a6f1-260a137ea9da | -12.4367 | -54.5778 | 2024-10-12 02:06:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5a93bd8d-14ec-38f2-b48c-dd2f23d2d3e2 | -12.7871 | -44.8639 | 2024-10-12 02:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 156.0 |
| 30ee79d0-768d-3bd4-9acf-7bdedc34e4ae | -12.7875 | -44.8406 | 2024-10-12 02:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 78.9 |
| b775b21a-7935-3e5c-b854-ab1d91866c30 | -12.8064 | -44.8608 | 2024-10-12 02:06:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| f2f6275f-08a7-3c12-b685-4a1d723e5838 | -12.8135 | -53.4861 | 2024-10-12 02:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| fafb1692-d589-3542-a4f4-c482de349b0e | -12.8132 | -53.5069 | 2024-10-12 02:06:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 120.4 |
| 3e999772-67a1-3550-806e-5b5fe1bda0d1 | -13.9473 | -45.7827 | 2024-10-12 02:06:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c85a3e53-6aa1-3bbe-aeaf-622e70466d42 | -14.3249 | -57.58 | 2024-10-12 02:06:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 11be96a4-2a4b-3749-ba1e-632df9962d2b | -14.3246 | -57.6002 | 2024-10-12 02:06:27 | GOES-16 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 49ca9ded-be84-3ea8-a773-84c576156a9f | -3.4983 | -69.189301 | 2024-10-12 02:06:42 | METOP-B | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 371ff576-5bd6-3a8b-a9df-4f3af8a99bc5 | -3.4965 | -69.181503 | 2024-10-12 02:06:42 | METOP-B | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6faa8156-7e0b-394f-a0bf-5411ebabae11 | -17.1761 | -57.4585 | 2024-10-12 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 117.8 |
| 8af59763-a3e4-3ed7-8ec1-5d7c6b604173 | -17.1758 | -57.479 | 2024-10-12 02:06:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| e3265db2-ce33-3279-8351-28eb556e10bf | -17.627 | -56.3318 | 2024-10-12 02:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.4 |
| 784ca3ec-1bff-304e-893a-19bb319c5ab9 | -17.6467 | -56.3292 | 2024-10-12 02:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 167.9 |
| 34a92a00-3ddd-380e-82f4-2f8aa8473c10 | -17.6471 | -56.3084 | 2024-10-12 02:06:45 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.7 |
| 3584c210-6a5e-3f8e-8e0d-84af79537a2c | -17.964 | -57.3843 | 2024-10-12 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.6 |
| c1bf5f17-d8af-35a4-a823-a0867326bd3f | -17.9643 | -57.3637 | 2024-10-12 02:06:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.7 |
| 4217fc3a-d471-3a13-b2a1-f7f1c334ecb2 | -18.196 | -56.5275 | 2024-10-12 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.7 |
| e4055385-4bc6-3ee6-aa27-30cdc23183a1 | -18.2158 | -56.5249 | 2024-10-12 02:06:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 61.3 |
| b5cf835c-16e4-37a1-a1ff-0ce71ee7c41b | -1.5877 | -53.3494 | 2024-10-12 02:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| c2091222-b496-3bc9-949e-edb6ab583162 | -1.6061 | -53.3492 | 2024-10-12 02:15:15 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| c1463037-8c61-3ff7-9785-a4c7cc261119 | -1.8793 | -54.4312 | 2024-10-12 02:15:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 655f51bd-e879-3e76-88d7-8f1218a01d3b | -1.8977 | -54.4309 | 2024-10-12 02:15:17 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 0cd4e563-9267-3a2e-b3e5-ea2aa0c0fb2f | -2.77 | -51.3829 | 2024-10-12 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 63e522a7-9330-38bb-a7ec-713cd8c1762a | -2.7701 | -51.3622 | 2024-10-12 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| e928771e-ac8f-35e1-bd26-38185b876bda | -2.7884 | -51.3825 | 2024-10-12 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 9936ed2a-a324-35b8-9597-afe212640512 | -2.7885 | -51.3618 | 2024-10-12 02:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 9e1a7be8-2684-31dd-8be0-44471b5a1088 | -2.8319 | -49.5385 | 2024-10-12 02:15:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| a1bae895-00f8-3cbe-ac04-e4b1c81677cf | -2.8795 | -51.6695 | 2024-10-12 02:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| c5a5a504-a721-3386-9a12-9c3fade29eb5 | -3.1426 | -50.3724 | 2024-10-12 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 43db443d-5761-3d9b-a03f-84faaa4af1f4 | -3.1427 | -50.3514 | 2024-10-12 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| ad1f8680-4ba0-3719-8a40-7049fb979111 | -3.161 | -50.3718 | 2024-10-12 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 0aee18dd-f3af-3ece-9278-1a4386a2e527 | -3.1611 | -50.3508 | 2024-10-12 02:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| eb0a4a6c-c8bd-35cb-a242-c41c695647e7 | -3.2136 | -46.7843 | 2024-10-12 02:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ce21ec89-6341-3406-a486-b97b5b365478 | -3.483 | -52.8211 | 2024-10-12 02:15:26 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1440c774-02f0-323d-963e-13d5e63be99f | -3.6901 | -47.9234 | 2024-10-12 02:15:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 3fe3f516-b0ec-3fae-a9ba-a4dd69aedcc7 | -3.6978 | -50.1225 | 2024-10-12 02:15:27 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| edb39ffd-659a-38e0-a495-d3ab35240beb | -3.7087 | -47.9227 | 2024-10-12 02:15:27 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| a5dd9241-d00b-3bef-985d-5cfcd3633d63 | -3.8167 | -52.3403 | 2024-10-12 02:15:28 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.6 |
| f5f25df7-6fd2-390d-8095-0026e97edd59 | -3.9208 | -46.4459 | 2024-10-12 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 45.0 |
| ee9e996d-e96a-3326-a44e-1971a424f17c | -3.921 | -46.4237 | 2024-10-12 02:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 17ef5fca-cb11-3ba6-97f3-d34d90adf559 | -3.9394 | -46.445 | 2024-10-12 02:15:29 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 86.6 |


[Clique aqui para ver as próximas entradas](README30.md)
