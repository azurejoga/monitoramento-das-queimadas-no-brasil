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
| 4671d9fe-024c-3a9a-b330-14ee2d75b582 | -18.0254 | -51.1591 | 2025-09-28 00:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d131c3b0-91ef-3a6e-8b2f-8937d89ca1e1 | -5.8374 | -44.4399 | 2025-09-28 00:00:00 | GOES-19 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| d15f21d5-ea03-39f3-90a8-cb8a884b2c0f | -5.2869 | -43.1613 | 2025-09-28 00:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 01369963-c111-3091-b94a-c5398247f514 | -14.8294 | -45.4415 | 2025-09-28 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 70327c99-fd87-3ce0-aefd-e503b88ce44a | -14.766 | -45.6621 | 2025-09-28 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 108.5 |
| a59a90e1-0793-3391-9055-6d74ae4170b2 | -11.0083 | -57.0658 | 2025-09-28 00:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 7114a294-0f8d-377d-a03f-b6647bbeba68 | -13.0106 | -49.4641 | 2025-09-28 00:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 2b49afbf-bf6e-3197-8820-b9cb5ac1534d | -13.011 | -49.4423 | 2025-09-28 00:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 592f6fc0-b110-3666-a5bf-ecb31a097aad | -4.9503 | -45.566 | 2025-09-28 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 50f58de3-eb87-3b4f-8085-fc950d8e9840 | -14.7861 | -45.6353 | 2025-09-28 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 78.3 |
| c6a526d5-5695-3cd7-b25b-33273ee09393 | -7.3847 | -47.0378 | 2025-09-28 00:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 0a810561-39aa-396b-afa8-68c6b7fe38c7 | -18.1977 | -53.3208 | 2025-09-28 00:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| e1e88982-b409-3fd3-a693-b73635d2b6c1 | -18.0448 | -51.1777 | 2025-09-28 00:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 37493398-abc2-346c-9be7-6e07b47ee532 | -16.271 | -50.2036 | 2025-09-28 00:00:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d6f44d3b-6490-3e19-9331-47cbfd947a4c | -7.4283 | -40.079 | 2025-09-28 00:00:00 | GOES-19 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 4b155145-06dc-3ced-bb50-243f0a36444b | -5.0454 | -45.3125 | 2025-09-28 00:00:00 | GOES-19 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| ba146713-a777-3924-a37d-5e78502b6b3d | -5.3057 | -43.1599 | 2025-09-28 00:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 52c3ca5a-e306-3f8d-ad1f-b5b5be85cbff | -5.992 | -43.9219 | 2025-09-28 00:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 0319c28a-4173-3fe4-84a6-2e4314983d12 | -8.483 | -47.7983 | 2025-09-28 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b23ca50c-1cc4-3153-b40c-00b8fd19d2cd | -5.8149 | -42.8167 | 2025-09-28 00:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 93.7 |
| f1e9b66e-a067-3f1c-839a-dc25919499c7 | -10.9894 | -57.0672 | 2025-09-28 00:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| e27d2351-301d-30e4-bf66-1759dc4c4dd7 | -8.4827 | -47.8202 | 2025-09-28 00:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f7d84ca3-c760-3e66-9b83-cdf57825768e | -14.7856 | -45.6586 | 2025-09-28 00:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| e009a688-32f2-31f9-8444-516d7c70123c | -16.9667 | -53.6975 | 2025-09-28 00:00:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| dd06ea79-e636-38d2-a59f-d822d24c1210 | -12.9918 | -49.4448 | 2025-09-28 00:00:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 1268f0c5-774c-3103-a195-aaed407520fa | -18.0453 | -51.1556 | 2025-09-28 00:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 06a2f04c-084d-31c5-8d43-35eb456b4c5c | -4.8557 | -45.7511 | 2025-09-28 00:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 04e9d9af-5021-32de-a45e-672558230ffa | -7.3849 | -47.0157 | 2025-09-28 00:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f717b386-f1de-3fc5-8b9d-512208964177 | -5.7396 | -42.8461 | 2025-09-28 00:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 79.2 |
| fc79d2b0-1a81-3a07-ba12-252db3336283 | -7.5449 | -46.089 | 2025-09-28 00:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 39.9 |
| 1a1e1cc2-62d3-3ae5-964c-38dc6e8bb3a8 | -5.2871 | -43.1379 | 2025-09-28 00:00:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 8ef9919a-8d53-34f3-8120-e681d364bc61 | -7.7787 | -47.0036 | 2025-09-28 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 202d3136-d569-3715-9d43-2df6e652824d | -10.9894 | -57.0672 | 2025-09-28 00:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| edc9dc3b-d114-3c67-9144-1d4c5bf8cbe6 | -14.766 | -45.6621 | 2025-09-28 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 96.2 |
| 17a639bf-e1c7-39a2-8670-a4dba90d0cd2 | -11.0083 | -57.0658 | 2025-09-28 00:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c218f434-9bd8-39b0-93ea-9fa648518856 | -15.9662 | -57.4929 | 2025-09-28 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 833a7148-838f-3713-b982-5968b345ce83 | -13.0106 | -49.4641 | 2025-09-28 00:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 11930f9c-ae29-30b6-844f-478d88e18673 | -13.011 | -49.4423 | 2025-09-28 00:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 80af8575-c9e1-3645-9d9e-69153e746186 | -15.9468 | -57.495 | 2025-09-28 00:10:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 36f8680d-c1bd-3d12-ab45-d2044863271d | -5.3057 | -43.1599 | 2025-09-28 00:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7341cb2d-0749-35b2-9b0f-4a562f9e7bca | -14.7856 | -45.6586 | 2025-09-28 00:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| bc37e46d-acbe-3012-8b31-95cc05850a91 | -7.7412 | -47.007 | 2025-09-28 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 85bccd00-31f9-33dc-8128-47bd71648f00 | -5.2871 | -43.1379 | 2025-09-28 00:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 4a8987cb-2b86-31cc-b01b-5649a5501347 | -8.483 | -47.7983 | 2025-09-28 00:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| e8712b32-0c8e-3aaa-9060-84d4cd7d29be | -3.7381 | -49.4445 | 2025-09-28 00:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| c847182f-7be4-309f-a56b-61d2f8803de9 | -18.0653 | -51.1522 | 2025-09-28 00:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 54.6 |
| e84629c8-9488-3d3b-97ac-c14920ff7d93 | -18.0458 | -51.1336 | 2025-09-28 00:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 6170f235-ad5f-3cdd-96e4-720cb548a19c | -18.1977 | -53.3208 | 2025-09-28 00:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 27e9bb55-29fb-3e80-96db-772d6fcd5455 | -18.0249 | -51.1811 | 2025-09-28 00:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.9 |
| b7507554-32e2-34f3-8659-2e21b09712c6 | -7.7975 | -47.0019 | 2025-09-28 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 101.7 |
| 67184796-09b2-3e99-9b52-c6d2ff71c024 | -11.9989 | -47.0371 | 2025-09-28 00:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| a52a9366-2e4e-3268-8b13-2be6044a2217 | -16.9667 | -53.6975 | 2025-09-28 00:10:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 799ae76c-2baf-3555-890a-2cc6c5612153 | -16.2706 | -50.2256 | 2025-09-28 00:10:00 | GOES-19 | SANCLERLÂNDIA | GOIÁS | Brasil | 5219001 | 52 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 54272e95-eec7-3fc0-8e72-c587a293e765 | -5.2869 | -43.1613 | 2025-09-28 00:10:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| da6cc1f1-ef21-3e89-8627-8efb7f7f53e4 | -18.0254 | -51.1591 | 2025-09-28 00:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 9db93f15-7cf5-331e-bf0f-94f089c5966c | -18.0453 | -51.1556 | 2025-09-28 00:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 280.5 |
| 3e09ac44-f96c-3350-a06f-d6a6e3f88b89 | -7.7599 | -47.0053 | 2025-09-28 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 6846e0cc-f2ee-3821-8f70-06aa58f87a07 | -18.0448 | -51.1777 | 2025-09-28 00:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 7d961dfe-0648-3821-85e0-5d22a20b5abc | -16.271 | -50.2036 | 2025-09-28 00:10:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 00eab801-7f0b-3652-948e-a9f644be28d5 | -7.7785 | -47.0258 | 2025-09-28 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 754759ef-a599-3c0b-9c4a-c957b4fa1cb3 | -12.9918 | -49.4448 | 2025-09-28 00:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 165e6038-03a4-3dec-aa89-a1892f6fa045 | -9.6512 | -62.8336 | 2025-09-28 00:10:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 57.3 |
| ad29fcbc-6a0d-36ef-96c5-48a75bd4ab6b | -5.8149 | -42.8167 | 2025-09-28 00:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| 5f801308-89da-3233-8db0-750638ab62b7 | -7.3847 | -47.0378 | 2025-09-28 00:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 127aaf62-1b5f-3f58-b111-9f061554f236 | -6.7782 | -44.0876 | 2025-09-28 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 7a602de8-5b88-3552-8bce-acf91c495569 | -7.7412 | -47.007 | 2025-09-28 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 2e85150e-2507-3111-a2f7-4a233e906c03 | -14.766 | -45.6621 | 2025-09-28 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 8aa60842-998f-380e-a1a3-e26a195dcbf4 | -6.7782 | -44.0876 | 2025-09-28 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| f15c4447-0026-37bc-b442-624e5bc21dc6 | -15.4519 | -48.2318 | 2025-09-28 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 53aee1e1-ca34-363b-b441-5a1a01368513 | -9.6512 | -62.8336 | 2025-09-28 00:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 39ac7400-fb7b-3d77-a92c-1c835e593fbd | -7.3847 | -47.0378 | 2025-09-28 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 8e3adbda-63ac-310f-b6a4-3919367d1ed2 | -14.7856 | -45.6586 | 2025-09-28 00:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 77.2 |
| a2bb0077-b1a9-3e4a-b074-1e11fa829edf | -18.0249 | -51.1811 | 2025-09-28 00:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| e09a7a06-fd1d-381f-85c5-c23dc7bf2e69 | -7.7975 | -47.0019 | 2025-09-28 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 8ad7066f-31f1-3bf9-a971-7d0236b5b72d | -16.271 | -50.2036 | 2025-09-28 00:20:00 | GOES-19 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 7547d4cb-925f-3ca1-b565-3b934f6c4cc3 | -9.6511 | -62.8526 | 2025-09-28 00:20:00 | GOES-19 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9451accd-a4af-398d-acb0-cd1365caba34 | -13.011 | -49.4423 | 2025-09-28 00:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 9e6b97b1-765f-3542-b5b7-52207017a41c | -5.2871 | -43.1379 | 2025-09-28 00:20:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 36.4 |
| db4f576d-b4a7-38f6-a479-013591dc09d4 | -7.7785 | -47.0258 | 2025-09-28 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 0aef61ce-c094-3c10-8cc2-3166348e92ff | -13.0106 | -49.4641 | 2025-09-28 00:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 0c55efd3-b29b-310f-8214-6ddc35e2ef3e | -18.0653 | -51.1522 | 2025-09-28 00:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| bd0a4bff-e3ff-3403-88ea-29036aca60f6 | -7.7599 | -47.0053 | 2025-09-28 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 125ce7e9-3be3-39d5-abf0-81a93b5c1869 | -18.0453 | -51.1556 | 2025-09-28 00:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 291.4 |
| 7b3d7ce4-bf95-31f8-ad2f-cd0faa6581ef | -18.0254 | -51.1591 | 2025-09-28 00:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 177.1 |
| ce88e1ab-01cf-38a7-9306-46125413e0bd | -7.7972 | -47.0241 | 2025-09-28 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 476a4319-577a-3bf7-b4b5-675ff4e88d95 | -18.2176 | -53.3177 | 2025-09-28 00:20:00 | GOES-19 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 75.9 |
| fba86272-b171-3a6e-bdae-e9decdc266da | -7.7787 | -47.0036 | 2025-09-28 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| feeb6293-8d2a-34a0-9b61-a944d9444369 | -3.7381 | -49.4445 | 2025-09-28 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 51619e1e-060f-31bf-8079-26d21b2e9a68 | -12.9918 | -49.4448 | 2025-09-28 00:20:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 7d793be5-7992-32e1-8074-e7584cd85c5f | -16.9667 | -53.6975 | 2025-09-28 00:20:00 | GOES-19 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 3f7c0b05-db63-3a1b-ab12-77f37695deab | -7.3659 | -47.0394 | 2025-09-28 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 0eb8a5f1-c89c-3455-baf9-16ff4c04cb98 | -11.0083 | -57.0658 | 2025-09-28 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 4b3525a5-1bc9-39b4-bdb1-e6795994e6ce | -18.0448 | -51.1777 | 2025-09-28 00:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 173.2 |
| eba3a6e4-3322-3e57-b2c9-ca3e56550e7e | -7.7977 | -46.9798 | 2025-09-28 00:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 8d94587a-a538-384a-b1e9-5fea4024979b | -6.2969 | -39.8258 | 2025-09-28 00:20:00 | GOES-19 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 96.9 |
| f0c77f46-8ad1-3e0f-9153-b874430818df | -10.9894 | -57.0672 | 2025-09-28 00:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 43592807-27a5-39d4-bf85-de901b73066d | -18.1977 | -53.3208 | 2025-09-28 00:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 128.4 |
| d1b85cc6-336a-3115-8bf2-b6da2684d80c | -5.8149 | -42.8167 | 2025-09-28 00:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 32e8edb9-33e7-30ec-b613-90cf8bfdb747 | -7.0318 | -39.9988 | 2025-09-28 00:30:00 | GOES-19 | POTENGI | CEARÁ | Brasil | 2311207 | 23 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 160dff45-436e-34a3-878a-54c62b62ee19 | -18.0448 | -51.1777 | 2025-09-28 00:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 323.2 |


[Clique aqui para ver as próximas entradas](README2.md)
