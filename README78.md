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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5d4a2a71-0db4-31a1-93f5-e29db9ed1aac | -15.5637 | -52.4516 | 2025-10-06 07:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| b3ea3855-758b-35f2-bd42-d240b0942ffc | -17.9813 | -57.5262 | 2025-10-06 07:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.8 |
| 8ef73fd4-193f-3e9f-994a-c459cf5fe3a2 | -15.6007 | -52.5529 | 2025-10-06 07:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 330439b3-ddd1-304b-8d04-3cf05ff048da | -18.1163 | -53.4192 | 2025-10-06 07:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 2766702c-d5bc-3efa-88df-c9c5cd8c36cc | -17.9813 | -57.5262 | 2025-10-06 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.1 |
| 5c74351e-c224-3d90-9fa8-dde3e0e70a33 | -18.1167 | -53.3977 | 2025-10-06 07:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.2 |
| f95d4a86-82cb-3649-a3c3-9f26b130aa86 | -19.5111 | -44.8545 | 2025-10-06 07:20:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c43bd1a5-f1cc-3d46-80ee-4cd9437a6968 | -19.4907 | -44.8596 | 2025-10-06 07:20:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f8f90068-8b7b-356e-9ea0-daef70670eba | -17.981 | -57.5468 | 2025-10-06 07:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.0 |
| d3e9130f-7e11-36d0-a11c-f500bfcd912c | -18.1366 | -53.3946 | 2025-10-06 07:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.6 |
| f2a08caf-8e2b-3db1-9d2d-9d7e1186b4ae | -15.6011 | -52.5315 | 2025-10-06 07:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4599bb15-b6d0-3e0c-919a-b877266731ae | -14.863 | -51.5019 | 2025-10-06 07:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ac7680c5-1b77-3bed-a3a9-5caf7cb9258a | -18.1366 | -53.3946 | 2025-10-06 07:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 79b947a3-538c-3db8-9a6b-c5ab8d991bc8 | -18.0008 | -57.5444 | 2025-10-06 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.3 |
| 243a1090-460f-3d89-aec4-7f37a237af72 | -19.4907 | -44.8596 | 2025-10-06 07:30:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 7488d35f-3539-3e2a-b836-86a00fab3e3d | -19.5111 | -44.8545 | 2025-10-06 07:30:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 90b27acf-d636-346e-81f4-ca9b0a148377 | -18.1163 | -53.4192 | 2025-10-06 07:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 0927c925-1af7-3b0c-9980-9d1126296587 | -15.2351 | -49.2914 | 2025-10-06 07:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 3fcd2902-287a-3b25-b7a9-ca71e069ef2c | -15.2156 | -49.2945 | 2025-10-06 07:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 8d4b7445-4789-35de-a66a-0d0457cf90cf | -17.981 | -57.5468 | 2025-10-06 07:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 4c081043-4274-374e-ae2e-99517ddbba55 | -15.2351 | -49.2914 | 2025-10-06 07:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 1227e1c4-5dc0-3a0f-8612-362fab955458 | -18.1371 | -53.3732 | 2025-10-06 07:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 5e836727-bde4-38a6-9598-2efaff273fc4 | -15.2156 | -49.2945 | 2025-10-06 07:40:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 6a4761f6-7e3a-3d04-af23-3b19289a40e3 | -19.5111 | -44.8545 | 2025-10-06 07:40:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 3859709f-3030-3ebe-aa29-d1e4356e189b | -19.4907 | -44.8596 | 2025-10-06 07:40:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 537db371-d772-38bf-ae53-632d4934b36d | -18.1366 | -53.3946 | 2025-10-06 07:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 8523cee0-86d5-3b42-8e95-163e359dfd85 | -18.1163 | -53.4192 | 2025-10-06 07:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 740ccd07-8892-36de-8e12-206a041b247e | -17.9813 | -57.5262 | 2025-10-06 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| ea621bfd-07e7-3e96-b1b0-10aa28c479a1 | -17.981 | -57.5468 | 2025-10-06 07:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.7 |
| b969b06c-f113-3d92-bee0-1506edb9f613 | -18.1565 | -53.3915 | 2025-10-06 07:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 8407088b-860c-3862-9e85-f3f91566c87a | -18.1371 | -53.3732 | 2025-10-06 07:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 0c9fbb91-3ca0-3540-ab09-63aaa9915d6e | -18.1366 | -53.3946 | 2025-10-06 07:50:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 3d9176bb-62ef-37df-bf7c-83a9f6a34cd4 | -19.5111 | -44.8545 | 2025-10-06 07:50:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 856e423d-2efa-3f09-9128-0c8fa66fc2f7 | -17.9813 | -57.5262 | 2025-10-06 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.3 |
| b33ed3c1-0e98-383a-8d4e-fde7da2fd6bc | -18.0008 | -57.5444 | 2025-10-06 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| 32ccb0fb-7cfd-3acd-a7b6-32f74d225857 | -19.4907 | -44.8596 | 2025-10-06 07:50:00 | GOES-19 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 057b6fa8-6c17-34c2-b4f9-67d0702ba858 | -15.2156 | -49.2945 | 2025-10-06 07:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 61b2dab7-31a9-3db0-bfbd-2532146fec53 | -17.981 | -57.5468 | 2025-10-06 07:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.4 |
| 6544f447-9074-3b6e-9fca-88bc0d50dd9a | -15.2351 | -49.2914 | 2025-10-06 07:50:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 41d70e2d-f47c-3248-95fb-42c561b280f4 | -15.2156 | -49.2945 | 2025-10-06 08:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 8081c7e4-8e4d-3775-96d3-0b3356e746ff | -18.1371 | -53.3732 | 2025-10-06 08:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 63.3 |
| e2534894-695b-3854-8be6-c095b8be6f24 | -18.1366 | -53.3946 | 2025-10-06 08:00:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 58.7 |
| f36e292d-47b4-3712-b8ee-062aacfd9938 | -18.1366 | -53.3946 | 2025-10-06 08:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 98864967-eca3-3b86-ad23-52134e2ae522 | -15.2351 | -49.2914 | 2025-10-06 08:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 148.1 |
| e552e7ec-02a7-3a96-ba34-6f636d675582 | -15.2156 | -49.2945 | 2025-10-06 08:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 731615f2-dec8-3572-a49b-e17d5ba258f5 | -18.1371 | -53.3732 | 2025-10-06 08:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ae166ba7-0084-3b27-ba8a-b045d5801bc9 | -18.1366 | -53.3946 | 2025-10-06 08:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 61.0 |
| d2397569-c3d1-3d9a-9fba-558855627aa3 | -18.1371 | -53.3732 | 2025-10-06 08:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 1c46a54e-eeda-3735-af01-fb1bcc22ed90 | -18.1366 | -53.3946 | 2025-10-06 08:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 83.0 |
| c139432f-d2d1-3465-ac36-c72339ac8114 | -18.1371 | -53.3732 | 2025-10-06 08:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 95.7 |
| de38d0be-4cd2-3f54-aec8-ac715ee7b1a6 | -15.0071 | -47.1341 | 2025-10-06 08:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 221.0 |
| 57ef84a2-a99a-36af-ada9-3f5754178a4a | -14.9875 | -47.1375 | 2025-10-06 08:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 346.3 |
| 53616c6a-7005-3b70-8384-f3fb1bdf36c4 | -14.988 | -47.1147 | 2025-10-06 08:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 874.4 |
| e0a53f2f-dfe8-3e1b-bd48-f6bc151ed070 | -15.0076 | -47.1113 | 2025-10-06 08:50:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 604.8 |
| 5a7e9de4-4a9d-34d4-b6f7-3ce51362669f | -14.9875 | -47.1375 | 2025-10-06 09:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 08d377c9-3bc9-380b-816b-cabc49c996b8 | -14.988 | -47.1147 | 2025-10-06 09:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 195.3 |
| 1c3e9f7d-2581-323e-a583-7c6de4b70721 | -18.1371 | -53.3732 | 2025-10-06 09:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 3496c47a-15b1-3756-864a-72518d4cbadc | -14.988 | -47.1147 | 2025-10-06 09:30:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 104.9 |
| ff9f287f-6a8a-3ff8-aafe-09c534c4228c | -18.0008 | -57.5444 | 2025-10-06 09:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.9 |
| 5adca131-8d89-3692-a2a3-83494942763e | -18.0011 | -57.5238 | 2025-10-06 09:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 160.4 |
| a1cd7cae-bc1e-3d5c-8287-7c7d94c05527 | -15.6202 | -52.5501 | 2025-10-06 10:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| f7e6f352-cb24-34e2-82c8-502aaa37479d | -14.5438 | -46.9633 | 2025-10-06 10:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 5a84993e-1145-32a5-be7d-9605a0d9d502 | -14.6893 | -48.4021 | 2025-10-06 10:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 98b5369a-36c9-3db4-9305-0af51b14edb6 | -14.5633 | -46.96 | 2025-10-06 10:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 147e66c1-c8cc-3930-8def-049d3e6ce60f | -14.5438 | -46.9633 | 2025-10-06 10:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 170.8 |
| d40d84d8-f98a-37b6-b263-7d45fd508c9b | -14.6897 | -48.3797 | 2025-10-06 10:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 1d521147-fc25-393d-9fb9-55f23ac309f2 | -14.5628 | -46.9828 | 2025-10-06 10:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| b19248ee-e3a0-3ca6-866f-71df01c27b77 | -14.5438 | -46.9633 | 2025-10-06 10:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 575ccc6e-0d6a-3fbd-a80e-2a38b078f0b5 | -14.5633 | -46.96 | 2025-10-06 10:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 159.8 |
| 2fba0d20-a395-3a80-98e1-29da976f9793 | -14.6897 | -48.3797 | 2025-10-06 10:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 802e72d8-1f11-3bf8-bbd2-754af039048c | -14.5433 | -46.9861 | 2025-10-06 10:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 110.1 |
| daaf0fc2-7864-3262-aa5f-6f8c7ef71e8e | -14.6897 | -48.3797 | 2025-10-06 11:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ffdb19ce-e4c0-3de4-9189-dea24fab4768 | -13.3237 | -48.0547 | 2025-10-06 11:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 30cad9e4-5709-30da-839b-04061215f35e | -14.6893 | -48.4021 | 2025-10-06 11:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 87cf29f4-44c0-3693-a3fe-9d73b58d9994 | -14.5438 | -46.9633 | 2025-10-06 11:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 124.2 |
| e30253f7-2c89-3928-b098-64cbcbd5d6f8 | -13.3237 | -48.0547 | 2025-10-06 11:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a1e2b533-9e36-3cbe-8bc2-c7753e088ea0 | -18.1565 | -53.3915 | 2025-10-06 11:10:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 95.6 |
| aae96f1c-9810-3c87-b4e1-d56f1af89d1f | -17.9813 | -57.5262 | 2025-10-06 11:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.0 |
| d8b29fde-d73f-335c-9573-f5553586b142 | -14.5438 | -46.9633 | 2025-10-06 11:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 0c5228cc-9e35-3b53-82e2-9c1402e90963 | -18.157 | -53.37 | 2025-10-06 11:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 1c9739fc-433a-387c-9ce1-c6dc57ecc0eb | -14.5438 | -46.9633 | 2025-10-06 11:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 170.2 |
| 285b62bd-7955-34c5-a33b-f99f52a8a834 | -12.4857 | -45.5356 | 2025-10-06 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 460e02b7-6dae-3be2-b9db-f9b32e534a57 | -10.3643 | -48.1519 | 2025-10-06 11:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c3684921-aa92-38f8-91f7-59b4e411a4b8 | -18.1565 | -53.3915 | 2025-10-06 11:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 178.1 |
| 3c3159f7-bfe2-33da-bc04-8d909fc7aab6 | -18.1366 | -53.3946 | 2025-10-06 11:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 149.6 |
| db5ab42e-3389-303c-8774-01d3adaaf303 | -10.4285 | -50.3518 | 2025-10-06 11:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 2e44e1da-cffd-3138-90a3-44cb9039b9f8 | -12.4853 | -45.5587 | 2025-10-06 11:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 31f582dc-fb56-3493-afef-f59a718712e1 | -18.1371 | -53.3732 | 2025-10-06 11:20:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 9e5b87d0-284f-3ea8-9544-4c1e2a407ac1 | -14.5438 | -46.9633 | 2025-10-06 11:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 238.6 |
| 3ef14df9-5360-30b0-9ff7-315f0ec0a10d | -12.4853 | -45.5587 | 2025-10-06 11:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 101d5c59-dbe3-3a5f-8919-9e532ecdd048 | -10.3643 | -48.1519 | 2025-10-06 11:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 8ec9378e-8b0c-3ae3-9d9b-4346bf540940 | -18.1565 | -53.3915 | 2025-10-06 11:30:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 711d0fc7-b7f4-3366-8016-19ea72144626 | -18.0011 | -57.5238 | 2025-10-06 11:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.6 |
| a0d73360-4600-37e9-9879-fd8d4adc0f86 | -14.5438 | -46.9633 | 2025-10-06 11:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 225.7 |
| 8fb4f819-f65b-3eae-8784-98d570897ee1 | -10.3643 | -48.1519 | 2025-10-06 11:40:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 66164a2f-519c-3090-a46f-6321bdf58bdc | -18.1366 | -53.3946 | 2025-10-06 11:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ec99cbb6-b005-3f3e-bb77-3c5a060602ba | -10.4285 | -50.3518 | 2025-10-06 11:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 96c0feb7-2986-30db-9d62-47a6e72d9c6f | -18.1371 | -53.3732 | 2025-10-06 11:40:00 | GOES-19 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 8bcb850c-5025-33f2-8fec-c0c5b1c2b2a3 | -14.863 | -51.5019 | 2025-10-06 11:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.1 |
| e4398c0f-b70a-31e6-8276-605728d20e08 | -13.0939 | -47.9992 | 2025-10-06 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |


[Clique aqui para ver as próximas entradas](README79.md)
