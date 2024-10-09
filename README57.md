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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3a6187e-8359-3aab-8516-696ce376b49e | -19.8131 | -45.6202 | 2024-10-09 03:06:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 2633e0f3-1c59-33db-8d06-400b6248f9e9 | -20.0122 | -42.4541 | 2024-10-09 03:06:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.8 |
| 137d258e-c774-34d6-9e02-80e1b8067677 | -20.013 | -42.4287 | 2024-10-09 03:06:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 120.8 |
| e531da60-a181-3f05-bf35-4ea36a53d57c | -20.103 | -55.9647 | 2024-10-09 03:06:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 96.6 |
| d501fc3f-2115-3759-9da0-ddc24a9ad56a | -20.1035 | -55.9434 | 2024-10-09 03:06:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.2 |
| 87fcedbb-702a-3629-ab48-9d3e99822de2 | -20.3346 | -48.7307 | 2024-10-09 03:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 6cd049c3-20dd-3e2a-815b-b41537599aeb | -20.3352 | -48.7076 | 2024-10-09 03:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 1c7c03a1-f4ea-36d4-83bb-6023bcf83cdd | -20.3551 | -48.7262 | 2024-10-09 03:06:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 8e8c327e-44a5-3c2e-a190-d48e96953fff | -20.5619 | -50.1175 | 2024-10-09 03:07:00 | GOES-16 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.4 |
| 2be71da2-5625-3d7e-a1fb-95531513d7ff | -21.0719 | -47.2094 | 2024-10-09 03:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 075e78d4-7bcb-3f93-8db7-946d7c3ba562 | -21.0919 | -47.228 | 2024-10-09 03:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 27665eeb-aab7-3b46-a8f4-83e67b986e33 | -21.0926 | -47.2043 | 2024-10-09 03:07:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 1799bb39-7fa3-3495-819b-e120092a96bf | -21.572 | -46.9898 | 2024-10-09 03:07:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 0dbb249e-fe3d-3d40-b107-01c706d65f1f | -21.5727 | -46.9659 | 2024-10-09 03:07:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 825603d0-8645-35f1-988a-4cb842940582 | -1.11 | -53.6173 | 2024-10-09 03:15:12 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 22c3cbd4-029d-3dea-8371-43e9941d05fe | -3.9021 | -46.4689 | 2024-10-09 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.1 |
| ff51bd72-9f19-3969-98fb-bda7db8cf326 | -3.9023 | -46.4467 | 2024-10-09 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1017810f-af39-31ba-a9a5-5b82cda4bc66 | -3.9208 | -46.4459 | 2024-10-09 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fc4980e3-c469-3afb-a5db-70791cfd917a | -3.9393 | -46.4672 | 2024-10-09 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3d47f56b-f50b-33c8-9735-8a246e642028 | -3.9394 | -46.445 | 2024-10-09 03:15:28 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 093da383-9fef-3b07-b5e8-6091b9850a29 | -5.5905 | -44.8687 | 2024-10-09 03:15:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 146f1d72-e820-37c4-a2dd-a185812c5c3f | -6.7614 | -60.0559 | 2024-10-09 03:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 145.9 |
| ecd5fe52-b546-3be5-9f04-43e71c03a2ce | -6.7615 | -60.0367 | 2024-10-09 03:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| a51faee7-12e7-314e-b13d-fd0d81edb346 | -6.7798 | -60.0552 | 2024-10-09 03:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 153.6 |
| d97094e3-ffc7-384a-807c-50bc4f75caf3 | -6.7799 | -60.036 | 2024-10-09 03:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 96814f1b-f18e-3e6d-8b2f-7bf3508a6f0f | -8.4919 | -48.6476 | 2024-10-09 03:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 13ebc7f2-12c2-3fe6-995a-c69aeef0a0cb | -9.5817 | -65.2497 | 2024-10-09 03:16:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 7a1f05cb-07fe-3f84-a319-1e1341cd1aaf | -10.3655 | -64.8451 | 2024-10-09 03:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 8838c359-f89b-35a7-bb64-baeea7af96e2 | -10.3656 | -64.8262 | 2024-10-09 03:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 37.1 |
| 8cfd8f66-bf3f-38cc-9232-2a68a3040222 | -10.3894 | -61.2502 | 2024-10-09 03:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b3d44762-85c5-3b50-99e1-8fbf45ab4cde | -10.3843 | -64.8255 | 2024-10-09 03:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 6fed8871-c2fa-3fea-b3e6-ec77aa68a068 | -10.4287 | -60.9979 | 2024-10-09 03:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| ee3d0e20-ac9e-337f-88c3-04f7a18b0e3e | -10.6253 | -55.9355 | 2024-10-09 03:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| c4a859eb-5112-3e3e-9788-9db733415ef2 | -10.6256 | -55.9154 | 2024-10-09 03:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| fbdd35c5-4104-3355-8645-575d9a2d4709 | -10.6258 | -55.8953 | 2024-10-09 03:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 4ec94ff6-a032-363f-96b2-cdec88a745e9 | -10.6446 | -55.8938 | 2024-10-09 03:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 3af56cea-961c-3a23-928f-ced4eb614c15 | -10.8754 | -63.9169 | 2024-10-09 03:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.0 |
| bc0e6719-a61b-3854-b05c-7383a3e12a02 | -10.8755 | -63.8979 | 2024-10-09 03:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 78.6 |
| a74c8757-a863-3272-9f38-a17204b3f7eb | -11.3467 | -51.021 | 2024-10-09 03:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 086488e7-b613-33f1-aa46-94b0d4aadf6d | -11.2583 | -60.3885 | 2024-10-09 03:16:10 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 83.9 |
| f67c7e66-2828-3003-a0c9-55da3b97c42f | -11.2771 | -60.3873 | 2024-10-09 03:16:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c5e58a75-9ff2-32af-8a79-d68a6a17102f | -11.5233 | -65.137 | 2024-10-09 03:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| f174e9c3-d46c-371f-a908-beb435aab9f3 | -11.693 | -65.0163 | 2024-10-09 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 94d8805f-2da1-3fdd-a0fe-8c36b4a1d09f | -11.6931 | -64.9974 | 2024-10-09 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 724332ae-070b-335f-89a2-cb13201f9372 | -11.7117 | -65.0155 | 2024-10-09 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 49c8d121-ab66-3faa-b88c-4aec4fd514ba | -11.7119 | -64.9966 | 2024-10-09 03:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 86d9344e-3e75-376f-9c86-74562c6759df | -12.0298 | -51.0722 | 2024-10-09 03:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| bb9a71c8-5ad3-3365-b3ee-8d1f1ef86b88 | -12.7501 | -62.269 | 2024-10-09 03:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.2 |
| d8e12666-562c-346c-8550-620781cb95bb | -12.878 | -62.8007 | 2024-10-09 03:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 4acc37fd-a52b-30a4-971a-2b48b059e999 | -13.8369 | -44.5691 | 2024-10-09 03:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| fbd571a5-2a3c-3554-bef3-efadb88a2ede | -13.8764 | -44.5386 | 2024-10-09 03:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 06fdebae-ddfb-3bfe-83fe-22b91cebc569 | -13.8769 | -44.515 | 2024-10-09 03:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 63c3bc1f-d8ee-3bf8-9cb8-c7b7c4a176d0 | -13.8963 | -44.5116 | 2024-10-09 03:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 74.1 |
| a19633a2-c2da-37ad-9930-6106e12750d5 | -13.9158 | -44.5081 | 2024-10-09 03:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 133.0 |
| a8662b7e-b871-3d19-88d6-9532d20166e1 | -13.9348 | -44.5282 | 2024-10-09 03:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 5eaa2e4d-010f-36bc-8886-538bf9191dc2 | -14.0975 | -51.0918 | 2024-10-09 03:16:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| bfc20b6a-2731-3c28-9edc-1609c02cc89d | -16.4184 | -55.9455 | 2024-10-09 03:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| a4dbb0fa-9e91-3e16-ad1b-abed84d4e7c8 | -16.8573 | -57.8218 | 2024-10-09 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 57.5 |
| a154a086-53ca-3ad3-9833-96ad0ea8e972 | -16.8576 | -57.8014 | 2024-10-09 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 53.6 |
| b403b65f-642b-3ed7-8854-2d2d7e68f0dc | -16.8768 | -57.8196 | 2024-10-09 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.8 |
| 849782c7-35ff-3daf-bd5a-64c49011c467 | -16.8772 | -57.7992 | 2024-10-09 03:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.7 |
| 24acc10d-6055-3116-b671-0e0c3ff7a9bd | -16.941 | -57.4654 | 2024-10-09 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.8 |
| d5312af6-9243-3c4e-abf9-085e97180487 | -16.9606 | -57.4631 | 2024-10-09 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.1 |
| 929b9109-7afc-3b1c-908d-8fd76ed68fae | -16.9609 | -57.4426 | 2024-10-09 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.4 |
| 22fe8772-ef65-338d-ac80-a0be6ae0d31d | -16.9802 | -57.4609 | 2024-10-09 03:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.4 |
| 0413d7d3-092c-3a39-89d3-8c5ff59b0ee2 | -18.1193 | -56.3921 | 2024-10-09 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 183.3 |
| ecff0d9e-1514-34b0-a8fd-afe608ccce77 | -18.1196 | -56.3713 | 2024-10-09 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.5 |
| a6ca213b-c9fb-364e-abfb-3ac0cfadc375 | -18.1391 | -56.3895 | 2024-10-09 03:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 30ce45bf-e241-3405-905e-5bfb8faec027 | -18.5993 | -57.2629 | 2024-10-09 03:16:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.0 |
| 688944d5-f5ed-329d-b0fa-e0e8076cdfaf | -18.5996 | -57.2422 | 2024-10-09 03:16:50 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 7c61ab5e-1801-364c-84c5-91fbc65f08c7 | -18.6597 | -57.2137 | 2024-10-09 03:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.5 |
| 6f071d25-21fd-3f05-ac0a-c00c657b868b | -19.8131 | -45.6202 | 2024-10-09 03:16:55 | GOES-16 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 102.4 |
| faeac324-7076-342c-8e05-deac97ae6fb7 | -20.103 | -55.9647 | 2024-10-09 03:16:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 95.8 |
| 6c5da07d-0495-3ce0-bff1-a01e14d1ff4a | -20.1035 | -55.9434 | 2024-10-09 03:16:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 102.8 |
| 7294e4d8-6cc9-3626-8d67-28de60810cba | -20.3346 | -48.7307 | 2024-10-09 03:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 4010ef0e-ca9e-33fd-8b85-377f761b1d99 | -20.3352 | -48.7076 | 2024-10-09 03:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 112.3 |
| cbbd012e-a2d7-39e9-881f-fa29e456148f | -20.3551 | -48.7262 | 2024-10-09 03:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 79889208-7249-3664-b695-37981e49d2ed | -21.0719 | -47.2094 | 2024-10-09 03:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 71.4 |
| e93f20cf-7f0f-3801-9de3-9b5691a679b2 | -21.0919 | -47.228 | 2024-10-09 03:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 2ca80c1d-fa62-3cb8-ab77-01d7538ab832 | -21.0926 | -47.2043 | 2024-10-09 03:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 82.6 |
| e8907f8a-132a-361c-96bf-56b1c8b4af61 | -21.1126 | -47.2229 | 2024-10-09 03:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 32ba2c82-8e34-3518-ac79-dc25a7db2f99 | -21.572 | -46.9898 | 2024-10-09 03:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 65.1 |
| d21d9c5e-4a17-33d4-9c88-bcb5b210104d | -21.5727 | -46.9659 | 2024-10-09 03:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 58de22af-db56-3062-bbd0-dab97ea7cc2d | -21.5864 | -47.8827 | 2024-10-09 03:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 86c7d150-1835-38fc-aaad-5804e624c098 | -22.1981 | -48.1541 | 2024-10-09 03:17:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 76cd72f8-573f-3706-bc14-e6bd2297bff8 | -4.85794 | -38.67057 | 2024-10-09 03:19:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5a131a39-9b44-3a0f-ae93-f13b77b263cc | -4.85743 | -38.6736 | 2024-10-09 03:19:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 077bb5fe-dea9-3b68-bc93-d7184459958a | -4.85178 | -38.6757 | 2024-10-09 03:19:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0eda1269-7e8a-3b6f-852d-52c857174f3f | -4.85075 | -38.68179 | 2024-10-09 03:19:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 33491c46-b94b-36d0-8e72-eee6a6ea91a8 | -4.72314 | -38.45669 | 2024-10-09 03:19:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65a147bb-a4bc-3702-b35d-5e9d0b21f02f | -4.72262 | -38.45974 | 2024-10-09 03:19:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1acdef82-9bd7-3a3f-9005-aafc7da5f152 | -4.24312 | -41.93322 | 2024-10-09 03:19:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5d337f83-ddfe-3fda-a878-f0635c5a7fe1 | -4.17618 | -42.9938 | 2024-10-09 03:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 23d1e68b-d645-399a-81bb-b66b8a4ce456 | -4.17511 | -42.99989 | 2024-10-09 03:19:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| babdebbe-39bd-3a30-8939-d127493b4bae | -4.16935 | -42.99259 | 2024-10-09 03:19:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c96a30cb-f7d8-30c0-9de0-6e1f437999a6 | -4.16825 | -42.99877 | 2024-10-09 03:19:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc4ef80e-fa53-3f1b-ade3-55d3e46081ca | -4.16253 | -42.9913 | 2024-10-09 03:19:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e98ab0a8-88e3-3732-a4b6-b02fe9d58466 | -4.16139 | -42.99767 | 2024-10-09 03:19:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86673b8c-a275-3221-86ac-66a1b8378342 | -3.81768 | -41.60673 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| fa5bc957-0c53-301c-8cee-ec9a252ead17 | -3.81137 | -41.60551 | 2024-10-09 03:19:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |


[Clique aqui para ver as próximas entradas](README58.md)
