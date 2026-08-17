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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4641feef-2935-3393-b816-cb121d3e9e11 | -6.7832 | -59.4401 | 2026-08-17 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 186c610d-11bc-38e0-8f8a-c343d9fdc4c1 | -6.2376 | -47.7624 | 2026-08-17 14:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 9e361912-656b-3862-a27f-dc621ab42e21 | -15.2645 | -52.896 | 2026-08-17 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 131.4 |
| f629d248-091b-3c74-9be0-cb46f34d712e | -7.8068 | -47.8591 | 2026-08-17 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| 2e0d7d99-195f-3f68-82f5-9de975b9c080 | -7.7881 | -47.8607 | 2026-08-17 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 251abe2e-7120-33ab-98df-061cfb21b931 | -6.97 | -59.0465 | 2026-08-17 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b628c7d0-ef5d-310b-ad12-50b87b698c19 | -9.1996 | -60.8122 | 2026-08-17 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.3 |
| 6ef3e333-6640-3b9b-9236-910908a07850 | -14.2947 | -53.1052 | 2026-08-17 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 162.1 |
| dd3d7ca5-5f22-3aba-9c60-98f39ca8f60e | -10.951 | -57.1497 | 2026-08-17 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 153.8 |
| 29cdb705-9aba-39db-a909-594ae4ff8325 | -6.2378 | -47.7406 | 2026-08-17 14:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 145.9 |
| 9292af20-478b-350f-bc4c-e287d1ad2eb6 | -8.96 | -60.5358 | 2026-08-17 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| dcaa3c18-8c68-316c-8f85-c68afa0ee4a4 | -14.5054 | -52.0421 | 2026-08-17 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 2639051b-4f7b-37cb-a373-3dcc51696a69 | -11.4907 | -46.5892 | 2026-08-17 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 18a9b3be-f142-3f80-af87-0e094c50432b | -9.2184 | -60.7921 | 2026-08-17 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 158.5 |
| 4af54f06-1775-3187-9382-64accfdb8575 | -9.7905 | -47.2452 | 2026-08-17 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 439.8 |
| 07b5bb97-d8fb-39c6-a1dd-ed9a7dcbc175 | -11.3235 | -46.3182 | 2026-08-17 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 245.5 |
| 573b6a0e-4a99-37bd-9e75-81c622f1ddc7 | -15.4384 | -52.9361 | 2026-08-17 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 3a703047-f1e3-342d-87a7-1449439e2e48 | -14.4663 | -52.0685 | 2026-08-17 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 8cb2e907-e302-3c96-99c0-46f08aedddbb | -12.5392 | -47.9 | 2026-08-17 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 5adb709c-130b-3933-bc40-dfd22bdebe17 | -14.4678 | -51.9832 | 2026-08-17 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 343ea897-b1e4-30c8-80cf-61ed2ea319cc | -14.3878 | -53.3037 | 2026-08-17 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5fba419e-20ca-3fa4-a844-555adad82a35 | -11.472 | -46.5692 | 2026-08-17 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 153.7 |
| 750edfdd-7f80-3737-99e3-96c8131d6176 | -5.5074 | -43.6576 | 2026-08-17 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| b1dd0579-b8cc-3ec3-b218-15e83cf25533 | -12.1392 | -50.1388 | 2026-08-17 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| be09cefa-823a-3538-8841-fc39e3b725b2 | -10.5085 | -50.0228 | 2026-08-17 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| ab550a53-fd53-3857-b276-fbf44a1d312d | -14.5247 | -52.0395 | 2026-08-17 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 115.1 |
| 0c5408a1-2a99-3ee0-8e45-50af87a89ecf | -11.8536 | -50.13 | 2026-08-17 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f9d625a7-1bed-3120-8e69-50c844d3e1fc | -11.9174 | -47.3393 | 2026-08-17 14:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 167.3 |
| f4c12f9e-c15f-3572-99b5-fb34851e9c84 | -9.1998 | -60.793 | 2026-08-17 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 262.1 |
| 73981634-3467-380d-87ec-9192f118fe21 | -8.6346 | -54.7326 | 2026-08-17 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9a527b16-0936-3583-9ed5-e1c08a560183 | -6.9701 | -59.0272 | 2026-08-17 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 9aeef2e8-d079-336a-9410-007309abfc85 | -7.6053 | -45.7238 | 2026-08-17 14:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 263.8 |
| b7a65fa3-a745-3686-bb71-5d12e91bf584 | -14.5441 | -52.037 | 2026-08-17 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.4 |
| ee411ac5-8e32-300e-9684-e10c68c11388 | -6.6014 | -58.9844 | 2026-08-17 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| e3517ad5-2f7b-3fef-95c1-e3e4af35c20e | -11.5095 | -46.6092 | 2026-08-17 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 275.8 |
| 90309964-1035-361d-866a-654141cd11cb | -11.7351 | -54.5636 | 2026-08-17 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 114a63ce-9008-359a-87a9-66e75e594da3 | -8.579 | -54.696 | 2026-08-17 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 58b3d0a0-23f1-3223-b035-fab05681d56d | -11.4172 | -46.4186 | 2026-08-17 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.6 |
| d431d566-07d8-37e3-b709-061eef37286a | -22.0767 | -55.9708 | 2026-08-17 14:40:00 | GOES-19 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 8dba3626-a8e8-39b4-a10c-8b64c6b2cbb4 | -6.2563 | -47.7611 | 2026-08-17 14:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 1039a457-1d54-300e-ad68-a42a066da46b | -9.7908 | -47.223 | 2026-08-17 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 04e7850e-56f7-3e80-b819-856b44fc9287 | -14.4871 | -51.9806 | 2026-08-17 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 178f7d02-48d3-3304-ab87-d06d2016dea8 | -15.2839 | -52.8934 | 2026-08-17 14:40:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 212.3 |
| 5c586eff-4574-30ea-b076-6926d61fc266 | -8.5212 | -54.9016 | 2026-08-17 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 41dc306c-aba2-3101-b844-fa15ab2815a9 | -11.4904 | -46.6118 | 2026-08-17 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 336.9 |
| 3c682973-9c6f-3b5d-81cf-7f8c783635fb | -10.9508 | -57.1696 | 2026-08-17 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2dacc3ba-5357-36ef-a765-a94633fe644d | -13.2805 | -51.6886 | 2026-08-17 14:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| c0d18bb2-d92d-3fbc-9058-715316f73709 | -7.3824 | -55.4924 | 2026-08-17 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| 811578f2-1276-38ec-bdc5-b28c47bdf98c | -6.9886 | -59.0264 | 2026-08-17 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 2b7262c6-e145-3829-b8cf-d3d9e04b359c | -8.6348 | -54.7124 | 2026-08-17 14:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 6b02bd3b-5bf6-34c5-94f2-54625427d333 | -12.5588 | -47.875 | 2026-08-17 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 112.9 |
| da085b48-f43a-393e-8d3d-795a229fc582 | -11.7349 | -54.5841 | 2026-08-17 14:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 4a76ea46-acd3-3e3b-a0a9-5349c70f1fae | -7.5674 | -55.5619 | 2026-08-17 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 55cde166-6118-3387-8a6e-c0b69cd6b7e8 | -14.2387 | -51.8431 | 2026-08-17 14:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| cfee161b-4c05-35a7-88c1-2c5ebf8d4fc3 | -6.2565 | -47.7393 | 2026-08-17 14:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 2ee65dea-2491-3bb5-88fb-a60788be8f22 | -7.3637 | -55.5134 | 2026-08-17 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 585ef102-e12b-3551-bf1c-fb37ebea9032 | -10.9322 | -57.1511 | 2026-08-17 14:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 98231e4b-e00f-39b5-bfef-c9194d38f946 | -9.3196 | -62.3353 | 2026-08-17 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 70.3 |
| d795400f-bea2-3ba9-aa7c-b8e99379b007 | -14.8619 | -46.6351 | 2026-08-17 14:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.1 |
| e8905ab7-068b-3f75-8168-842f3eb70539 | -6.3909 | -51.7475 | 2026-08-17 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 7f8f36ad-c619-3ea7-9272-2ce2f7edbabf | -14.2758 | -53.0866 | 2026-08-17 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 97.3 |
| 62898732-54aa-31c4-ac7a-872629067b76 | -7.3823 | -55.5124 | 2026-08-17 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 9e4c4f98-16eb-39e6-8773-c6441e82797d | -14.2568 | -53.0679 | 2026-08-17 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| bae766e5-0885-346c-84d7-d053108fd1bb | -8.0834 | -61.3603 | 2026-08-17 14:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 065f27d9-ab7c-3c5c-ba52-6349b51f0976 | -11.4716 | -46.5918 | 2026-08-17 14:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 39b9860e-ffb8-37f1-a918-e4c6fb3d29fa | -7.8071 | -47.8372 | 2026-08-17 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| a02ba486-6b4e-3487-bdfa-90ec4d3caa22 | -13.4123 | -54.3324 | 2026-08-17 14:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 756.6 |
| 70ef71de-7d82-3085-a710-6787f398a740 | -7.1361 | -47.5425 | 2026-08-17 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 19cdd139-556b-3208-9849-cbfdae000e5a | -6.2192 | -47.7419 | 2026-08-17 14:40:00 | GOES-19 | LUZINÓPOLIS | TOCANTINS | Brasil | 1712454 | 17 | 33 | nan | nan | nan | Cerrado | 97.9 |
| c7bd6bd2-de22-39d0-9451-5cf5e214365a | -16.6797 | -49.4498 | 2026-08-17 14:40:00 | GOES-19 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 507c948b-2ffa-3392-b809-b5e11df7e058 | -10.5275 | -50.0208 | 2026-08-17 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| cc721fd2-bc02-308c-b5d7-961c7faef4f4 | -8.9601 | -60.5165 | 2026-08-17 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 659b7291-9b24-3fb4-8997-2bc9dc566a74 | -11.4176 | -46.3959 | 2026-08-17 14:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 155.5 |
| b106ffec-95fb-36ed-a9a3-f0c76d495124 | -7.3639 | -55.4935 | 2026-08-17 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 46f0047f-72eb-3cc4-9b4b-0f56d1f01fe5 | -6.7123 | -58.9412 | 2026-08-17 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| dc08d29e-c367-3e4d-90d3-1027c80c39a7 | -7.1363 | -47.5205 | 2026-08-17 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| df58e724-f678-339d-918f-1011dd94f17c | -12.7009 | -48.5195 | 2026-08-17 14:40:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 7a955e9a-b692-30a8-951a-0287bd157a1f | -9.3382 | -62.3344 | 2026-08-17 14:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| dae7df7a-8743-3b83-920b-d3633f763e10 | -5.5072 | -43.6808 | 2026-08-17 14:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| ed6b2b72-d828-3212-9377-a372b9158966 | -14.2565 | -53.0889 | 2026-08-17 14:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 24f304b0-1820-393e-8e68-64d33cefa18f | -12.5396 | -47.8777 | 2026-08-17 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 0470d49a-0e14-3b7f-bd66-9c5f12f2ce86 | -6.6198 | -58.9836 | 2026-08-17 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4e9572c4-8b93-3626-86eb-5a8061b5c647 | -9.1706 | -59.6762 | 2026-08-17 14:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| c90adf93-9eb8-303e-bd0e-f71cefef3ecd | -6.6015 | -58.9651 | 2026-08-17 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 2d22b3d6-0725-3e98-8d13-8bfda63924f4 | -8.3682 | -46.3921 | 2026-08-17 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 215.1 |
| 31c05191-4bec-3a56-8e71-e6ce81df521b | -11.7157 | -54.6063 | 2026-08-17 14:40:00 | GOES-19 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 108.1 |


