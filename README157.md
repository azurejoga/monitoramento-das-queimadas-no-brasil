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

## Dados Diários - Página 157

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bfb9bf2-041a-3a70-a244-979083dee407 | -18.6387 | -57.2785 | 2024-10-06 07:46:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.2 |
| 2e4311fb-1567-3c35-9a03-4c6e262ec809 | -20.4712 | -51.2806 | 2024-10-06 07:47:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.1 |
| 4f903efa-78d0-3169-bd0d-2ddd896fd4f3 | -20.4508 | -51.2846 | 2024-10-06 07:47:00 | GOES-16 | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 6f2ec475-7787-3703-b812-c7af0dd80de2 | -12.6726 | -54.0189 | 2024-10-06 07:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 8d64ca25-17fa-3ac9-a87c-78d022947012 | -12.6535 | -54.0208 | 2024-10-06 07:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 145.4 |
| 131a14e1-93ce-347d-b2a5-ae01ad4208bf | -12.6532 | -54.0415 | 2024-10-06 07:56:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 5e05f050-e852-3171-a6a2-1eb4c5c071f2 | -12.6283 | -53.1108 | 2024-10-06 07:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c4df604c-147b-3897-bc74-667b6d8da65c | -12.628 | -53.1317 | 2024-10-06 07:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| aa478d91-97e4-39a8-8955-7e09e065d355 | -12.6092 | -53.1129 | 2024-10-06 07:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 008b34a6-8601-34eb-938e-0a5bdb63cff7 | -12.6089 | -53.1338 | 2024-10-06 07:56:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 94771b03-0c75-3c17-af19-e961f39b18e8 | -13.3786 | -61.9582 | 2024-10-06 07:56:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| b1f43188-b005-3902-9567-7c9bb80c61d9 | -16.4151 | -57.3823 | 2024-10-06 07:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 69.1 |
| 2c94c009-e712-385f-a71f-0b9d39ce4b54 | -16.3959 | -57.3641 | 2024-10-06 07:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.9 |
| 92e86136-b478-37bd-8a45-e26475c69073 | -16.3956 | -57.3845 | 2024-10-06 07:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.3 |
| fce9ad02-71f5-3b21-a243-1998db0b1faa | -16.3764 | -57.3663 | 2024-10-06 07:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.6 |
| d5d3099f-5bf6-3704-8921-39cd20c2bd29 | -16.3761 | -57.3867 | 2024-10-06 07:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.0 |
| 08e127b0-0fad-3dfa-8465-3c99d0df9937 | -17.0116 | -56.7186 | 2024-10-06 07:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.7 |
| dbf7d3e0-6a3d-33b5-b893-1fc82c103f7f | -17.0207 | -55.0371 | 2024-10-06 07:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| adff919c-c74a-3400-b28b-994e98e11113 | -17.0203 | -55.0581 | 2024-10-06 07:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 9c027692-af4c-36e1-9cc2-5ef0f3e940c7 | -17.02 | -55.0791 | 2024-10-06 07:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 82.2 |
| c6dd3ff2-3fd7-3ead-aae7-dad222c58ecd | -17.0007 | -55.0607 | 2024-10-06 07:56:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| b1e79849-ab39-39b2-a4a7-4a25ac4dbb0e | -17.1182 | -57.4039 | 2024-10-06 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.7 |
| c0b7cf41-eb0f-3df7-a919-6d149d71cc55 | -17.0989 | -57.3857 | 2024-10-06 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| ec193d4a-bee8-369b-933d-ee9bbb90f3da | -17.0985 | -57.4062 | 2024-10-06 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.2 |
| e601e721-876c-3c95-8ce5-3304306a6670 | -17.1188 | -57.3628 | 2024-10-06 07:56:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 7001254e-30c4-36cd-8b88-3a9a080fec8c | -17.1185 | -57.3834 | 2024-10-06 07:56:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 130.4 |
| 5031ef38-2404-3367-8887-67e85935a6bc | -18.659 | -57.2552 | 2024-10-06 07:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.7 |
| 68bf1b05-5c49-3fef-a2d6-55ee081789d1 | -18.6586 | -57.2759 | 2024-10-06 07:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.6 |
| 0d6dee5d-3ddc-3015-8165-04d350ca7783 | -18.6387 | -57.2785 | 2024-10-06 07:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 83f79286-8d21-3955-8a34-62bdae54ada5 | -9.176 | -61.5603 | 2024-10-06 08:05:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 41f52c48-2c45-3bab-a59a-9dfba221e0f7 | -12.6092 | -53.1129 | 2024-10-06 08:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| e2861d71-5372-377b-b50c-84cd748fa332 | -12.6089 | -53.1338 | 2024-10-06 08:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 67792f81-129d-38df-a50b-1e8dc90b0fd1 | -12.6726 | -54.0189 | 2024-10-06 08:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 114.9 |
| 182469b1-c2a4-3387-83dc-2f574b3a4c5c | -12.6283 | -53.1108 | 2024-10-06 08:06:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 74a3604f-66b7-3bf5-8a85-439c439c8162 | -12.6535 | -54.0208 | 2024-10-06 08:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 152.3 |
| 77ddc623-5e73-3f30-a613-d9f4f87d8c45 | -12.6532 | -54.0415 | 2024-10-06 08:06:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 86.7 |
| de05593a-721a-33f5-b2aa-2ced4218d05f | -13.3786 | -61.9582 | 2024-10-06 08:06:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| df5fc56c-f3ca-3841-b105-4c038b416b2a | -13.3976 | -61.957 | 2024-10-06 08:06:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.7 |
| dff2f5b4-af5d-30cf-adec-d60a4cfe22b1 | -16.3764 | -57.3663 | 2024-10-06 08:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 66.0 |
| 434d2a05-9d84-39b0-bd62-e8ad1a24570b | -16.3956 | -57.3845 | 2024-10-06 08:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.9 |
| ca380094-381a-3ecf-b75a-40dc40185479 | -16.3959 | -57.3641 | 2024-10-06 08:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 84.6 |
| 6d1c1461-bade-3bf2-aaeb-4098b28106d9 | -17.02 | -55.0791 | 2024-10-06 08:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b46fd4dd-9003-30dd-8121-fd839d1a2790 | -17.0007 | -55.0607 | 2024-10-06 08:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9e3a1dbb-4bd2-328c-a3fa-e578fc73c9a4 | -17.0203 | -55.0581 | 2024-10-06 08:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 4938e76a-bc39-36ca-b735-bc9f4045e499 | -17.0207 | -55.0371 | 2024-10-06 08:06:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 5372155e-ffac-3aeb-bc95-132fae4361e3 | -17.0116 | -56.7186 | 2024-10-06 08:06:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.0 |
| b4111a24-15b6-3de2-b12e-2a772cbcae71 | -18.6387 | -57.2785 | 2024-10-06 08:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| f8555636-0740-36dc-b040-a9eaf36f48a7 | -18.6391 | -57.2578 | 2024-10-06 08:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| 7b1d7235-238d-38c7-b0fa-38f933582f4f | -18.659 | -57.2552 | 2024-10-06 08:06:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.5 |
| 6595cc1f-b4fe-392b-a4bf-06f288c04826 | -9.1759 | -61.5794 | 2024-10-06 08:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 7322caf1-a553-3e64-aade-4660f5e23ed6 | -12.6726 | -54.0189 | 2024-10-06 08:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 3e9d8a90-f5df-323f-8ebd-7d1e74c81b15 | -12.6283 | -53.1108 | 2024-10-06 08:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 241822e3-88b0-3ea8-8da0-56ac0059b269 | -12.6535 | -54.0208 | 2024-10-06 08:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 167.6 |
| 2ddf3be4-90d2-307c-97fd-13ef4df89039 | -12.6532 | -54.0415 | 2024-10-06 08:16:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 7e2e2d31-f93f-36a0-80ca-ab947e013f2b | -12.6089 | -53.1338 | 2024-10-06 08:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2a79e8ed-e2c7-341b-b6a6-68e1b33a6df4 | -12.6092 | -53.1129 | 2024-10-06 08:16:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 8b1feec2-c601-3035-aeea-e2510138e06f | -13.3786 | -61.9582 | 2024-10-06 08:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| fc524fa1-879f-3c42-8884-3434c88e3cba | -13.3976 | -61.957 | 2024-10-06 08:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 38e3031a-4d5a-322d-bf35-41190c64555b | -16.3959 | -57.3641 | 2024-10-06 08:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.9 |
| d8d777c6-1159-3bc3-93bf-7c31b5a1e39a | -16.3956 | -57.3845 | 2024-10-06 08:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.1 |
| 91432430-877f-37a3-997d-83f32afb372f | -16.3764 | -57.3663 | 2024-10-06 08:16:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 86f4b790-74da-3291-8a6d-4ff1baa2413c | -17.0007 | -55.0607 | 2024-10-06 08:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| d661ea99-bc5f-3cec-b428-2b0a4b4ab081 | -17.02 | -55.0791 | 2024-10-06 08:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 87847992-1d28-3482-b17d-97693c89951d | -17.0203 | -55.0581 | 2024-10-06 08:16:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 165.1 |
| d549073e-e0bc-3fd5-a4b0-85a4f0e9fdc6 | -17.812 | -53.7859 | 2024-10-06 08:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 4c58b463-dcc1-3311-b0ae-ca2827d02128 | -17.8319 | -53.7829 | 2024-10-06 08:16:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 44c9a26f-c62a-30e2-ab8b-d4005a74352c | -18.659 | -57.2552 | 2024-10-06 08:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 96.4 |
| 76bbcef6-1517-3582-8210-0d037c9e5ec0 | -18.6586 | -57.2759 | 2024-10-06 08:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.5 |
| bbf9db07-97d7-3192-83e9-6c54b6392e18 | -18.6391 | -57.2578 | 2024-10-06 08:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.8 |
| 3c72c1d7-5fc1-3779-93c5-b692efcbf681 | -18.6387 | -57.2785 | 2024-10-06 08:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.2 |
| dbc1f7ab-9b63-3150-b471-268156485617 | -12.6283 | -53.1108 | 2024-10-06 08:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1d64f6c3-5e89-3e87-9ae5-c748bd1a8276 | -12.6532 | -54.0415 | 2024-10-06 08:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 0d892eeb-ed37-3805-860e-9954036bdc21 | -12.6535 | -54.0208 | 2024-10-06 08:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 156.7 |
| 5ae17ba5-2868-3243-a061-c25e2e5cdd9c | -12.6726 | -54.0189 | 2024-10-06 08:26:18 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| f0544d0a-bebe-3a48-bc37-fa4a1d24617b | -12.6089 | -53.1338 | 2024-10-06 08:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 17c304ad-9383-35af-976e-59205c1b5fb0 | -12.6092 | -53.1129 | 2024-10-06 08:26:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 828a02af-9497-33ff-a6e7-22e91cb9c23b | -13.3786 | -61.9582 | 2024-10-06 08:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 6d99039d-e737-3759-bee2-29e97a1e8529 | -13.3976 | -61.957 | 2024-10-06 08:26:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b7793844-0b51-3ec0-8849-2f8c8a9160cf | -16.3764 | -57.3663 | 2024-10-06 08:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.0 |
| 50279688-ead0-3a2a-8df4-97edf7aca5c2 | -16.3959 | -57.3641 | 2024-10-06 08:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 91.8 |
| 761d7121-1140-350f-b577-eb006ba6f2e5 | -16.3956 | -57.3845 | 2024-10-06 08:26:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| d596e1d7-94f8-3fd5-bf0e-ed93b0542e0a | -17.0203 | -55.0581 | 2024-10-06 08:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 211.4 |
| dd03036a-e196-349a-be30-f6a985846efc | -17.02 | -55.0791 | 2024-10-06 08:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 8f1eac3b-9010-3bc7-91ac-484b54d65d6d | -17.0116 | -56.7186 | 2024-10-06 08:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.1 |
| c7ad630d-782d-3f8f-bb0c-1288fd44b92f | -17.0207 | -55.0371 | 2024-10-06 08:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 88c2aae0-d6a8-3bc8-bf4d-3b96b89391ef | -17.0007 | -55.0607 | 2024-10-06 08:26:42 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| cb599817-3113-3401-abf1-eee37b64fb1e | -17.1188 | -57.3628 | 2024-10-06 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 05d2ceff-5948-353f-947a-5a5bc7434186 | -17.1185 | -57.3834 | 2024-10-06 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 100.3 |
| fdd6e7ca-3d0a-3cf9-ac7e-0b4e86244269 | -17.1182 | -57.4039 | 2024-10-06 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 55.4 |
| ff31ec27-abc8-3149-8f23-f1c1c5234d4b | -17.0992 | -57.3651 | 2024-10-06 08:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.6 |
| 05da8d24-49df-38d6-8d44-525a5d10fede | -17.0989 | -57.3857 | 2024-10-06 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.6 |
| 3a99fec9-a0eb-396f-8e05-051286c9f65a | -17.0985 | -57.4062 | 2024-10-06 08:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 39.3 |
| 465b97db-5cc5-3621-a7f6-9e77782eda76 | -17.8319 | -53.7829 | 2024-10-06 08:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 4435b7a1-c57e-3054-b467-ab1ac9dcdb13 | -17.812 | -53.7859 | 2024-10-06 08:26:46 | GOES-16 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 628afa14-7d98-3866-af1d-4457c1e789b9 | -18.659 | -57.2552 | 2024-10-06 08:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 111.9 |
| d2753f04-69ed-35f3-b7a3-f1ece96f3fc1 | -18.6387 | -57.2785 | 2024-10-06 08:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.7 |
| b55b2eea-49f5-3f64-8e7a-a75a6f2a49eb | -18.6391 | -57.2578 | 2024-10-06 08:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.2 |
| 04230f44-6ec2-3396-9efb-4acc400ac016 | -18.6586 | -57.2759 | 2024-10-06 08:26:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.9 |
| bb50484e-c266-372d-ac7c-af255ae94b5b | -12.6089 | -53.1338 | 2024-10-06 08:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 36ddb2ec-5552-30df-9ad6-67c7cb4a988c | -12.6092 | -53.1129 | 2024-10-06 08:36:18 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |


[Clique aqui para ver as próximas entradas](README158.md)
