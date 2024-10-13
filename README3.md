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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4cf4766d-6b09-31cb-a12a-3ab223d90b92 | -7.8895 | -63.0171 | 2024-10-13 00:15:52 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| a1008c03-7247-3dbe-818a-97151880a77c | -9.5185 | -47.8049 | 2024-10-13 00:16:00 | GOES-16 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 284007e5-81dc-376f-91ff-675ce88f02bc | -9.7359 | -64.2295 | 2024-10-13 00:16:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 437ddb98-f1b9-31c3-9a92-ba80f1508a8e | -10.9311 | -44.6789 | 2024-10-13 00:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 4751e8aa-253a-3f00-8505-068afa2ab5b7 | -10.9315 | -44.6557 | 2024-10-13 00:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 6eaa17c3-ab46-3dfe-ba61-55b70cb9f76b | -10.9502 | -44.6762 | 2024-10-13 00:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 81579d50-80b6-3bef-a3fc-eed1df717bcc | -10.9506 | -44.653 | 2024-10-13 00:16:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 2acca01a-898b-3d73-81e5-f87b79012839 | -10.9519 | -61.1226 | 2024-10-13 00:16:09 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| a1b13ddb-3e84-3f2f-820c-2566a43f15fd | -11.2532 | -50.9249 | 2024-10-13 00:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 0a561a09-ed0b-3c94-a01f-35a93db44136 | -11.2535 | -50.9036 | 2024-10-13 00:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 7a221e3d-9fae-37ec-a2fe-4eebfadebb82 | -11.2722 | -50.9228 | 2024-10-13 00:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| be15aaae-ca4a-3214-8fe8-af38ba049123 | -11.2725 | -50.9016 | 2024-10-13 00:16:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 9aeefafe-17cb-35b8-a49b-49d0bcba613f | -11.7479 | -48.3591 | 2024-10-13 00:16:13 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| a6df4f6e-b53b-311b-a644-2103b1ed94c3 | -11.712 | -64.9777 | 2024-10-13 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 8700d416-e2f9-3a3e-a0d3-a5ea50abb3e3 | -11.7308 | -64.9769 | 2024-10-13 00:16:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 42153b48-f596-3279-a1e6-f10099cf4145 | -12.2563 | -47.6499 | 2024-10-13 00:16:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c5a0d7b0-7042-3f94-a083-853e98b5f9e6 | -12.2754 | -47.6473 | 2024-10-13 00:16:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 65673b13-587d-3c95-8ae0-5b3dc261004f | -12.2946 | -47.6446 | 2024-10-13 00:16:16 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.7 |
| ad3994dd-f9e0-3cb3-9531-8b50f4b15ea2 | -12.3792 | -63.7485 | 2024-10-13 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 104.7 |
| d3724e77-325a-3f05-9235-46e73bc880b4 | -12.3793 | -63.7294 | 2024-10-13 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 357e9ee1-fa6c-3885-a0fc-bde354ca9c5f | -12.398 | -63.7475 | 2024-10-13 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 151.9 |
| a39887fa-4ac6-31d9-87e8-7fa6652a6e64 | -12.3982 | -63.7284 | 2024-10-13 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 236.5 |
| c9ab1f4a-2467-3daa-9785-e9cc3e1942a4 | -12.4171 | -63.7274 | 2024-10-13 00:16:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 74.4 |
| d1a29ec4-0246-3371-9f55-5ac302aff125 | -12.7688 | -62.2872 | 2024-10-13 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 86319253-fcf7-3da7-b100-1f36efa7fc48 | -12.9181 | -62.548 | 2024-10-13 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 84.2 |
| fc05c866-6a28-3412-9a90-afe4a92361ff | -12.9182 | -62.5287 | 2024-10-13 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 137.0 |
| 460acb41-6053-3947-932b-afd07397a0c2 | -12.9372 | -62.5275 | 2024-10-13 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 219.0 |
| a759c179-0350-396b-be4a-4070571ee5d7 | -12.9373 | -62.5083 | 2024-10-13 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 0788b009-b1f5-3678-ae28-844c9656d84b | -12.9561 | -62.5264 | 2024-10-13 00:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 83.5 |
| e3d39a5e-690d-38fb-95b5-9a94b5ad7a68 | -13.1475 | -62.3215 | 2024-10-13 00:16:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 329c2ddc-a1f8-3918-8c26-45589e4286ed | -13.7346 | -60.6079 | 2024-10-13 00:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 165.1 |
| 720e9e0d-f8c6-3112-9714-7d15bc8bfbf8 | -13.7348 | -60.5883 | 2024-10-13 00:16:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 144.6 |
| f054d343-4858-32ef-9d5b-33c18e47e90f | -14.7638 | -57.799 | 2024-10-13 00:16:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 169.0 |
| a3ef15e7-c129-3a0c-8f3a-6b769c27bd3e | -14.7641 | -57.7789 | 2024-10-13 00:16:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 028e44c0-8b78-3cec-89c6-47f730aa4742 | -14.7831 | -57.7971 | 2024-10-13 00:16:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| f5e51316-f0bc-3dc8-bf21-61e1e8dbeae3 | -15.6419 | -59.9767 | 2024-10-13 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 8c2dba1b-6e14-359d-a18c-25e2b6b7ca02 | -15.6421 | -59.9568 | 2024-10-13 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 2bd70d7f-9b03-3806-ac58-23cde92f63c9 | -15.6424 | -59.9369 | 2024-10-13 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 4e19cdeb-ebbe-39a1-9333-229a4fb1cbe6 | -15.6426 | -59.917 | 2024-10-13 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7b5b4e0b-6d35-3aa6-9f9a-bd80ccf05831 | -15.6612 | -59.975 | 2024-10-13 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 28702cea-a10b-330b-8710-eaf139046631 | -15.9435 | -59.1098 | 2024-10-13 00:16:36 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 477d5740-d078-3518-92fc-c3fd41dbb1c7 | -15.9437 | -59.0897 | 2024-10-13 00:16:36 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6ba1d667-bc71-3023-875e-7e9a0905eedc | -16.9998 | -57.4586 | 2024-10-13 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.3 |
| 95b0b304-ee60-3b77-a7f3-c727d40b7cf2 | -17.0001 | -57.4381 | 2024-10-13 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.8 |
| 3252ba3e-260f-3b82-9555-9a27b3701e15 | -17.0623 | -56.0308 | 2024-10-13 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 57.4 |
| 89610495-444d-34d7-b1fa-f34b3bbe7723 | -17.0626 | -56.01 | 2024-10-13 00:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 63.1 |
| befd0a1f-879f-3006-bf60-ebe535047c9e | -17.1761 | -57.4585 | 2024-10-13 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 202.1 |
| a80f05b6-804b-3824-8a85-9b67d632b9ec | -17.1764 | -57.438 | 2024-10-13 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.5 |
| bfef1962-600c-3c1f-8104-3d6572df1d77 | -17.1954 | -57.4767 | 2024-10-13 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 118.0 |
| 1ac4153a-f897-3540-a80e-4371a6ab277c | -17.1957 | -57.4562 | 2024-10-13 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 164.8 |
| ba5e07da-e504-36a0-8f40-667cbce8802f | -17.196 | -57.4357 | 2024-10-13 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.9 |
| 030d58b8-7f7b-317e-b6c0-8e155ee44c88 | -17.1172 | -57.4654 | 2024-10-13 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| c910f2fc-e1b4-3489-93be-480adb024732 | -17.1758 | -57.479 | 2024-10-13 00:16:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 134.1 |
| 92ce35fe-9986-3657-9ee1-64ae7b07cf96 | -17.6862 | -56.3241 | 2024-10-13 00:16:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.4 |
| e5a186c4-4e2f-3cff-a068-4df17aadd272 | -17.964 | -57.3843 | 2024-10-13 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.5 |
| c954a079-f68c-34a6-a03d-33de40576429 | -17.9643 | -57.3637 | 2024-10-13 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.8 |
| 1e0cdce5-4ba8-3a1e-9e4e-e03ded4936cf | -17.9837 | -57.3819 | 2024-10-13 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.4 |
| 49418394-3646-3e50-a49b-4e8dfb1c0a3c | -17.9841 | -57.3612 | 2024-10-13 00:16:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.2 |
| 3c3654fd-b413-37e7-bc94-dd5fb2e063db | -1.9217 | -61.7432 | 2024-10-13 00:25:17 | GOES-16 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| fd50cfac-47e2-3d9b-a73f-ef71a7006ead | -2.1508 | -48.8112 | 2024-10-13 00:25:18 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 9875b30f-dd0c-39b6-b7f9-f68a1253cdc0 | -2.1692 | -48.8322 | 2024-10-13 00:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 8482f133-6c41-37d1-9f14-b833bc6ce36f | -2.1693 | -48.8108 | 2024-10-13 00:25:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 318c0792-47bb-35d6-9561-563740a34f66 | -2.7958 | -49.3062 | 2024-10-13 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| cdef1b30-b25f-3510-8d4b-72c322343b26 | -2.7959 | -49.2849 | 2024-10-13 00:25:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| eb6604b5-dae7-3c32-946e-a2b47bbcd987 | -3.0731 | -54.2473 | 2024-10-13 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 3b397457-3c6f-343b-9557-769b2a9046b9 | -3.0732 | -54.2273 | 2024-10-13 00:25:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 2acc9c68-8e28-3a66-9867-7b5ddc8b8ba3 | -3.0773 | -53.036 | 2024-10-13 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 086ba69f-ba22-3464-8f8c-f83140b53935 | -3.0956 | -53.0559 | 2024-10-13 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| f2fb44f4-dd70-3795-a11b-019bbe354340 | -3.0957 | -53.0355 | 2024-10-13 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 282.6 |
| 2c183b32-b785-3e74-b4a8-d4216c3dcc99 | -3.0957 | -53.0152 | 2024-10-13 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 6f76c96e-0dc9-3894-a321-6540a270000b | -3.114 | -53.0554 | 2024-10-13 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 2fcd4d53-54b7-3734-9727-d205b484d921 | -3.1141 | -53.0351 | 2024-10-13 00:25:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| bf60731c-6ddd-3cf9-bd9b-9b4288dfc794 | -3.1792 | -50.4551 | 2024-10-13 00:25:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| aed47480-9dd6-3d96-bf51-c3b44e54eb1c | -3.2225 | -48.9306 | 2024-10-13 00:25:25 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| fefa2eee-35d3-3cbc-a826-6f693494c06d | -3.2226 | -48.9092 | 2024-10-13 00:25:25 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 073bd0c8-7aa2-3c70-b3a9-dd7f31dbf6d7 | -3.5264 | -51.257 | 2024-10-13 00:25:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 4268c4ba-6630-363e-bb9d-d4a9eb236dcf | -3.7127 | -40.7346 | 2024-10-13 00:25:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 66.1 |
| e0297cbb-88f6-3990-a8ff-f64d8a9ae486 | -3.7128 | -40.7102 | 2024-10-13 00:25:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 116.6 |
| 4b70b8ca-5ab4-331a-a50b-26dde42026c6 | -3.7316 | -40.7092 | 2024-10-13 00:25:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 67.0 |
| 8c0a3dd7-9653-3834-a847-01efbcee84c8 | -3.625 | -54.132 | 2024-10-13 00:25:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 551d660d-0d89-302a-8280-ce59778254cb | -4.1148 | -48.2515 | 2024-10-13 00:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 192.7 |
| 7dd1a1d5-8cdb-3bdc-9e7d-2315ef8f3f68 | -4.1149 | -48.2299 | 2024-10-13 00:25:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 164.1 |
| 0f1a976b-5213-3185-b737-3ef22b9a75ed | -4.1479 | -45.7896 | 2024-10-13 00:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 808acc7c-2770-3c29-bf48-678d6218d373 | -4.148 | -45.7672 | 2024-10-13 00:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 40b1d392-d4b3-3bb2-ba1e-d338885a2082 | -4.1665 | -45.7886 | 2024-10-13 00:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 1644b581-6751-376e-9fb7-84d91b39f338 | -4.1666 | -45.7662 | 2024-10-13 00:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 64c05801-045d-36d7-8317-e794bd95e0f1 | -4.4026 | -49.7563 | 2024-10-13 00:25:31 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| e524db8d-a1d4-3958-810c-08c73484fa98 | -4.7188 | -60.8072 | 2024-10-13 00:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| afa19b5c-7f23-33b1-9b2a-a61b331f38ad | -4.7188 | -60.7882 | 2024-10-13 00:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 637a05e1-9bbc-35b1-a148-42fdcfaa262f | -4.7189 | -60.7692 | 2024-10-13 00:25:33 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| ab8f9004-d16a-31fb-ae47-ca740f777b4f | -4.7371 | -60.7877 | 2024-10-13 00:25:34 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e91cfe0b-1872-328e-874f-4e8db3085157 | -4.7372 | -60.7687 | 2024-10-13 00:25:34 | GOES-16 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 123fd924-e34a-39f1-a3d8-71c8e4981e10 | -4.8418 | -47.739 | 2024-10-13 00:25:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 37.9 |
| e73f06b6-baa1-331b-9d20-9b722362a45b | -4.898 | -47.6707 | 2024-10-13 00:25:34 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 3624b803-ac83-3c9c-b2e8-a0083ca7cb79 | -5.0713 | -46.8499 | 2024-10-13 00:25:35 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 0ada8e8d-5651-3c56-9508-69afe507afb2 | -5.1381 | -45.3969 | 2024-10-13 00:25:35 | GOES-16 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| ad7edfed-d35f-39a9-9303-eb6bb5adf3f1 | -6.1299 | -47.2884 | 2024-10-13 00:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 91d0fdb4-621f-3e14-bd88-499892bbc631 | -6.1301 | -47.2664 | 2024-10-13 00:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 73115e15-1957-3caf-8bce-8fe0f871978b | -6.1487 | -47.2651 | 2024-10-13 00:25:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| ac639509-1280-37cb-9914-fcd43feed954 | -6.6925 | -62.8493 | 2024-10-13 00:25:45 | GOES-16 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |


[Clique aqui para ver as próximas entradas](README4.md)
