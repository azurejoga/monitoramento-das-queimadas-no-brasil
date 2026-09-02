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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d232ff9b-51ab-3b0b-8410-38f55f67b14e | -8.8925 | -62.3538 | 2026-09-02 16:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 116.2 |
| fbe1d969-cf71-385b-ae2d-36703f8a5718 | -5.8537 | -57.5576 | 2026-09-02 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| c8892fab-ed87-3f30-adf0-03a2e3110a58 | -3.4002 | -61.3276 | 2026-09-02 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| b10827b9-0db1-3547-95da-52ec33515c46 | -9.6633 | -48.2721 | 2026-09-02 16:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 2dafc33c-059c-33d2-b907-7f9b6234cfa2 | -5.9635 | -57.6899 | 2026-09-02 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| bfb97faa-2bf5-35af-9780-fd6d44b55a1e | -6.8784 | -58.9343 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 402681a8-5778-3d6a-8672-76b96c5cc0f1 | -6.8412 | -58.9746 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 8b98e3f8-63f6-3b1f-b1e6-643c42f4bcb1 | -4.2383 | -62.2349 | 2026-09-02 16:10:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 8a44c5bc-8089-30bd-83c8-a91d68df46d1 | -6.7453 | -59.6341 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| d7c27de8-ba76-3006-afda-755042c26241 | -13.9664 | -58.6736 | 2026-09-02 16:10:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| d032ccdc-639c-31b2-a4c5-b0828b545c70 | -6.8571 | -59.4179 | 2026-09-02 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| af1aa3c7-429f-3508-8d24-9028a651f561 | -7.2745 | -60.6486 | 2026-09-02 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 3f0a9f64-de89-3a4f-a3c4-8ec74ab9e7c0 | -5.565 | -60.1739 | 2026-09-02 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 6b0cf17f-9674-34a5-b3e3-7dcda7c4189a | -3.3688 | -59.4079 | 2026-09-02 16:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| fc940805-fe86-3500-bd0c-d519611d876b | -12.08 | -47.07 | 2026-09-02 16:15:00 | MSG-03 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7f80445b-49f2-3fd5-874d-ee4fef872716 | -15.3852 | -53.7652 | 2026-09-02 16:20:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| f66a36d0-1cdb-3143-9687-0cb3f703cd62 | -3.3688 | -59.4079 | 2026-09-02 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 66.8 |
| d65b595f-32f0-3539-9335-1c89bc2c011c | -6.1844 | -57.7395 | 2026-09-02 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 13adfae8-e1c8-3c1c-a4af-81668f9bafa6 | -1.4761 | -54.2365 | 2026-09-02 16:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| d7525323-5f40-3b97-91e3-c3649009d531 | -5.9635 | -57.6899 | 2026-09-02 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 983e23f2-3aff-3cee-a57a-46203c3642ca | -5.5649 | -60.193 | 2026-09-02 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 921e80be-2227-3f9c-b21b-da394dc302c5 | -3.8263 | -59.3982 | 2026-09-02 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 7f4be9f1-1226-37f6-b1cb-671fabe668b3 | -7.5526 | -60.4651 | 2026-09-02 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| c27377e2-936b-3ff1-92c7-8e7041404afe | -7.2932 | -60.6096 | 2026-09-02 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bc5c774a-bd23-3a56-b942-3d4537b4b193 | -3.4185 | -61.3273 | 2026-09-02 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ee0ddaad-c456-3ec1-a12e-2bbfedf541f2 | -7.2745 | -60.6486 | 2026-09-02 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| ed8fdbde-7757-3f41-ba92-e35b59ae62e5 | -3.1449 | -61.1997 | 2026-09-02 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3d60477a-eed9-3c36-a84c-45cd184ac027 | -7.1822 | -60.6713 | 2026-09-02 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 44d73279-3302-37c6-9851-39437eb6cd08 | -8.3413 | -71.0108 | 2026-09-02 16:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 3b6001e2-4002-3b02-8cb8-86bb21faf251 | -7.2934 | -60.5713 | 2026-09-02 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| c50891ab-732a-3f3b-a41c-4b9174db6318 | -8.2236 | -62.7405 | 2026-09-02 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 5b0d4981-0a46-3e74-9d2b-2108aa20eb3c | -3.3871 | -59.3883 | 2026-09-02 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 38e7ec16-e40a-3e4a-a23e-ac7f35923f9a | -7.5479 | -61.2866 | 2026-09-02 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| e8d52323-85ae-3a73-b385-88baa60e8a8b | -3.4002 | -61.3276 | 2026-09-02 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| f233fe49-5410-36e1-8aa0-86ddcf2a99d2 | -10.2564 | -68.2487 | 2026-09-02 16:20:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 80c74aed-fde1-32af-8a5f-940423e0a33e | -6.8412 | -58.9746 | 2026-09-02 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 954f7a19-2176-38f9-97f0-6696b33181c8 | -15.3057 | -53.8802 | 2026-09-02 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 829fd8cf-e433-33bf-ac2d-cf6779390fdc | -6.7453 | -59.6341 | 2026-09-02 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 78bb2194-cfc4-38f2-8f4b-c099348d6827 | -7.5293 | -61.3063 | 2026-09-02 16:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 23d4745d-5de4-34d8-8771-84ec4b3c0786 | -15.3654 | -53.7887 | 2026-09-02 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 2725fcca-5ef6-34b2-940f-c9be0f15d126 | -14.2562 | -51.9472 | 2026-09-02 16:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 59.7 |
| a7eb3cbb-803e-3be9-a865-d5b04323e0d9 | -2.9447 | -60.9002 | 2026-09-02 16:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 3ae1263f-8d37-303a-a899-efdb3012d5bf | -7.1121 | -42.7963 | 2026-09-02 16:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 71.0 |
| 1b9f55a9-0eb2-3f93-b94e-389b910ad741 | -3.3505 | -59.4082 | 2026-09-02 16:20:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 77d06a57-71e0-3480-b265-6a53630cd37e | -15.3651 | -53.8097 | 2026-09-02 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 292877b0-3f2b-38cf-89a0-436b61560e6f | -6.8203 | -59.4001 | 2026-09-02 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 2a160214-dc09-3d3e-9fc6-b095a3eb0e73 | -3.1267 | -61.1811 | 2026-09-02 16:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 68837a93-d9d7-35b1-a78d-8d147b118dfe | -9.8434 | -64.9777 | 2026-09-02 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 7bff438e-53c4-33b8-8adb-36a95ce2ff22 | -5.6016 | -60.211 | 2026-09-02 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 7503aaff-23a5-3b20-b1c4-772f4916f021 | -7.2931 | -60.6287 | 2026-09-02 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| f7c22638-67eb-3e75-bdea-207e418bce16 | -15.2863 | -53.8827 | 2026-09-02 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| e1f42e6b-eba5-3663-b6e9-dd1b749c7957 | -3.7533 | -59.3231 | 2026-09-02 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| b4bd6954-96ab-32b0-a760-ef6cb9ef779b | -15.346 | -53.7912 | 2026-09-02 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| f83efae5-5fe1-3356-8c2d-0841670e4934 | -3.0347 | -61.4846 | 2026-09-02 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 61e3ddac-19a7-3486-8818-e2f8db7f9dfd | -14.2989 | -51.7072 | 2026-09-02 16:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.4 |
| f35e0c58-fb8b-397c-bea9-91d2b550b18e | -7.2536 | -61.1074 | 2026-09-02 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e7c1738f-c932-398d-9edc-b5e66288085c | -8.7631 | -46.4418 | 2026-09-02 16:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 00dfde7b-cd05-3a03-a185-f18c11eae87e | -5.9451 | -57.6906 | 2026-09-02 16:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 940f627d-5924-3069-99e1-b625b56dea74 | -3.0347 | -61.4657 | 2026-09-02 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 4782ec49-d89c-3fb2-84a9-86a85dcee667 | -13.9664 | -58.6736 | 2026-09-02 16:20:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 2c4feca2-c3cb-35f9-aec2-47b64854d85c | -7.2007 | -60.6515 | 2026-09-02 16:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 42d493f6-5980-3abe-90fe-5273e9cd11ac | -3.0893 | -61.5403 | 2026-09-02 16:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| a4171845-6499-36f6-81f7-9d2f0b81ffa3 | -3.8446 | -59.3977 | 2026-09-02 16:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 0f4486e4-3026-38c0-a547-3690586e23cd | -15.4429 | -52.681 | 2026-09-02 16:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| c2914556-3a8f-3026-8107-577d3ad8a6b3 | -3.7533 | -59.3231 | 2026-09-02 16:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| ea571abb-5c98-3867-af83-a7319fc094f0 | -3.8263 | -59.3982 | 2026-09-02 16:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 3f7fc5b2-0fac-3956-a35a-9df1bbe2e7ce | -15.2866 | -53.8617 | 2026-09-02 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 107.6 |
| bf7f23b2-2676-3755-ad66-1f5706cdcd4e | -15.3061 | -53.8592 | 2026-09-02 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.1 |
| aa5f55ec-e374-346a-83c1-f936b17973f9 | -3.0347 | -61.4846 | 2026-09-02 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 7c297afd-de87-37d9-aa41-4da489b4741c | -3.4185 | -61.3273 | 2026-09-02 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| c795bbbf-2dc4-31c5-aa3f-a8ffe23e7180 | -6.8387 | -59.4186 | 2026-09-02 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 23470671-f26d-3acc-be93-0e2dbfa52c3d | -3.1997 | -61.1799 | 2026-09-02 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 3f6ee295-5c17-30e1-8b28-6b1eb93b8747 | -1.4761 | -54.2365 | 2026-09-02 16:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| dd99a536-6572-33e5-b4f0-73e97fc5db05 | -10.2209 | -50.3517 | 2026-09-02 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| b823a5ec-5793-30db-85b0-87e34429bff7 | -10.202 | -50.3536 | 2026-09-02 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| efaae730-fdc5-3282-b256-8b776e3e2d43 | -4.2383 | -62.2349 | 2026-09-02 16:30:00 | GOES-19 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 1db82875-477e-3694-99b0-f13178cc28c7 | -7.2745 | -60.6486 | 2026-09-02 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 49554a90-1257-3a0c-bdfb-c25656ed197d | -15.3654 | -53.7887 | 2026-09-02 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 1cbc8534-00de-3a1a-b77b-ba68e5d8bd75 | -3.218 | -61.1607 | 2026-09-02 16:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| b341eeef-f52e-33c2-873c-8ae1deb125f9 | -5.9451 | -57.6906 | 2026-09-02 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 33594895-04f6-332c-aa44-004172fb3dea | -15.346 | -53.7912 | 2026-09-02 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 48b8e63e-d9de-3e6e-914f-3af04db43e19 | -5.9635 | -57.6899 | 2026-09-02 16:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 5383807e-8f30-3529-8878-1306c29f3d7b | -10.2023 | -50.3322 | 2026-09-02 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 99d86906-2d7a-3cf0-80f1-39a4345b6c4b | -8.2606 | -62.7391 | 2026-09-02 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| aacaaa9e-3a18-317b-87d2-472251080ad3 | -3.4002 | -61.3276 | 2026-09-02 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 980116cf-9f9d-329d-a5b5-6968f671ba4a | -7.2932 | -60.6096 | 2026-09-02 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| a155da44-117a-33be-a300-ef3ed99494bb | -7.5526 | -60.4651 | 2026-09-02 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 2d0685be-ba0b-3fa3-9cd3-2d48674c3265 | -3.0347 | -61.4657 | 2026-09-02 16:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 87d448e9-9b4e-3106-9960-3e5edec7ec8a | -13.9855 | -58.672 | 2026-09-02 16:30:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 5317e372-3730-341a-822d-08a040d85743 | -10.2564 | -68.2487 | 2026-09-02 16:30:00 | GOES-19 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 2dc59538-8006-3d85-ae66-ed7709106884 | -10.1084 | -50.299 | 2026-09-02 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| f584666a-12ad-3a12-9432-b32931ca29ec | -15.2672 | -53.8642 | 2026-09-02 16:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 29b40887-76d5-3823-967c-718f7d3b22d5 | -10.1538 | -45.6982 | 2026-09-02 16:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| d0440a56-d1cd-3ce3-b497-93543695dfb0 | -10.1648 | -50.3147 | 2026-09-02 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 6cbdbe14-7e6d-33fa-a18e-e81d639e3f0a | -7.2933 | -60.5905 | 2026-09-02 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 7f517243-7d12-3362-b523-9a451737bee1 | -3.6398 | -60.5656 | 2026-09-02 16:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| cee787fb-c333-3bb5-bfb1-d8f22d039862 | -10.1081 | -50.3203 | 2026-09-02 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 7a83e3f4-306c-30cb-ae75-dcbe93858431 | -10.1645 | -50.336 | 2026-09-02 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 207f1df9-c289-3ab8-818b-d512b8a48fe6 | -8.7628 | -46.4642 | 2026-09-02 16:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3055f505-8b2e-3013-9cc6-cb536ed61ddc | -10.1456 | -50.3379 | 2026-09-02 16:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |


[Clique aqui para ver as próximas entradas](README89.md)
