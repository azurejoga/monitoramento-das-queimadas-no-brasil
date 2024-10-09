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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0752ab7-a20b-3105-8b6a-2a7e62f68d3e | -10.3895 | -61.231 | 2024-10-09 02:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 33e36df9-a6cf-3042-b719-274e1dbecd34 | -10.3842 | -64.8443 | 2024-10-09 02:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 7a9df2f3-ef11-36d7-a54c-54705dd4cc63 | -10.3843 | -64.8255 | 2024-10-09 02:16:06 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| edb60715-31ee-3934-ae7c-1ee9ab4e39b0 | -10.4287 | -60.9979 | 2024-10-09 02:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 03a123f1-b4da-3286-bc33-ffcf9a5268a8 | -10.6068 | -55.9169 | 2024-10-09 02:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 5f23b380-02df-30fe-b753-2803a346f807 | -10.6253 | -55.9355 | 2024-10-09 02:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| ee22c864-3e05-3fa7-9836-97c1ad733617 | -10.6256 | -55.9154 | 2024-10-09 02:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 579c0b16-351d-32ad-bca8-a41bad661fe0 | -10.6446 | -55.8938 | 2024-10-09 02:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 5561c37f-151e-3bd2-bbcd-8fb781907939 | -10.6258 | -55.8953 | 2024-10-09 02:16:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| c3853c92-b88a-36ba-b06a-f1d9c8c02e4e | -10.8755 | -63.8979 | 2024-10-09 02:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 41b6f13a-99d3-3f08-a3b3-f54be0626fb4 | -10.8754 | -63.9169 | 2024-10-09 02:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 94.5 |
| b9ddae69-9bd0-3901-8895-770fcedc82bd | -10.9112 | -64.1615 | 2024-10-09 02:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e80658e5-8901-3ca6-b664-cce905203c8d | -10.8941 | -63.916 | 2024-10-09 02:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.9 |
| fa854a3b-864b-31b3-be73-133c72033153 | -11.3235 | -51.3202 | 2024-10-09 02:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 3e01374f-9adf-3a5a-9372-4ed6db0e847c | -11.5233 | -65.137 | 2024-10-09 02:16:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| cff88da5-4bc9-3cd6-b5ca-f1f3605115d9 | -11.7119 | -64.9966 | 2024-10-09 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 5996dbf4-c42b-3b1c-9257-3bc1d9aed750 | -11.7117 | -65.0155 | 2024-10-09 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 7438567e-ccf4-3c6b-b9b2-0ed40733211c | -11.6931 | -64.9974 | 2024-10-09 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| ba574064-0f52-361c-8702-d35b49ebd1f7 | -11.693 | -65.0163 | 2024-10-09 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 5a22ad39-e7a5-371b-b58d-de5bf85e00de | -11.6806 | -64.0312 | 2024-10-09 02:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| a1477e02-3f60-3715-af15-daa55883c954 | -12.2086 | -50.5815 | 2024-10-09 02:16:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 609854b0-fe96-32f1-99d9-1a1b582656de | -12.1895 | -50.5838 | 2024-10-09 02:16:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c32238ec-4511-3c7e-b426-e680703c8f5c | -12.6676 | -63.0819 | 2024-10-09 02:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 7dcb2925-4acd-30ad-82f3-ab0bb8af7602 | -12.9756 | -62.4673 | 2024-10-09 02:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 93d133df-635a-39f2-8841-ad3d6843ac47 | -12.878 | -62.8007 | 2024-10-09 02:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 6bca859b-46ee-3932-a881-f4df147a504e | -12.8779 | -62.82 | 2024-10-09 02:16:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 57.9 |
| a6448db2-676e-390d-a1ac-9e84d055fb7b | -12.8591 | -62.8018 | 2024-10-09 02:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| d9deb9b6-219a-31e4-9edf-3bb0e13004ef | -13.3065 | -53.7227 | 2024-10-09 02:16:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| e178c70a-121e-3e3c-8f1a-369f37fe4587 | -13.3062 | -53.7435 | 2024-10-09 02:16:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| a7abd2a3-6543-3c12-a582-110ca9a68624 | -13.2874 | -53.7248 | 2024-10-09 02:16:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 877a7932-3601-3838-8cba-4ec72e6df27e | -13.2871 | -53.7456 | 2024-10-09 02:16:21 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 851bd707-8c84-345e-95ad-bc273b4b28de | -13.817 | -44.5961 | 2024-10-09 02:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f7f3ee5b-512c-3b26-97bf-c3ebe1554e24 | -13.8364 | -44.5927 | 2024-10-09 02:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 0876929d-9ed1-3e5b-9602-8221b924bc1e | -13.8369 | -44.5691 | 2024-10-09 02:16:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 159.9 |
| f0cb3a0b-47af-3b9b-a4b4-40d91bf1ea86 | -13.8564 | -44.5657 | 2024-10-09 02:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| e4a6c0e7-6cc2-3438-a90f-4642d1be20bb | -14.1197 | -44.9637 | 2024-10-09 02:16:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| dfd6b275-1805-3ebf-a816-4a01ff6887c3 | -16.4187 | -55.9248 | 2024-10-09 02:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.9 |
| fd977479-8ca4-3647-80b4-017a9a3c3f9e | -16.4184 | -55.9455 | 2024-10-09 02:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 79.0 |
| df7f26d5-6100-354a-8005-827fe58b77eb | -16.929 | -55.7989 | 2024-10-09 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.1 |
| 8ee50a30-8d31-3404-a548-804ae1a4298b | -16.9098 | -55.7806 | 2024-10-09 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 124.4 |
| 8bbe04c2-1a41-3288-9e3c-a2ea142da953 | -16.9094 | -55.8014 | 2024-10-09 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 182.2 |
| b7cfac4f-64a7-3dba-83a1-46d53e3d57a1 | -16.8901 | -55.7831 | 2024-10-09 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 122.7 |
| dc2788bb-6f71-3dd4-8e84-60a6b7adc4b6 | -16.8898 | -55.8039 | 2024-10-09 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 156.1 |
| 3ee5ad6a-8a57-3d32-9c2d-3fa978ea8e5a | -16.8894 | -55.8247 | 2024-10-09 02:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.9 |
| 875b0e72-ca26-3bb7-8605-5d8a1ee5337c | -17.0623 | -56.0308 | 2024-10-09 02:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.4 |
| c8f7d9bd-f21d-3b11-ab00-896bee900a93 | -17.3353 | -55.0156 | 2024-10-09 02:16:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 100.7 |
| df76e357-567e-318d-b56c-733517f3ab14 | -17.335 | -55.0366 | 2024-10-09 02:16:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| 9ef3805e-5f3f-3d12-9310-90fede3b96f4 | -17.1588 | -56.1222 | 2024-10-09 02:16:43 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| 7aa0f885-59d2-342f-b369-05f5ae98da76 | -17.1467 | -56.8463 | 2024-10-09 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.3 |
| d3d76ce7-1b16-3da5-a08e-46d51fc8ddb3 | -17.1271 | -56.8486 | 2024-10-09 02:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.2 |
| f775d634-556f-3ef7-93e6-cd14f556364d | -17.5713 | -40.3079 | 2024-10-09 02:16:43 | GOES-16 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 67.8 |
| ad153cfa-9991-34dd-a9c9-72950b8ea36b | -17.3551 | -55.0129 | 2024-10-09 02:16:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 129.3 |
| 02ed89a6-067d-3cee-a44e-05a78e291ff4 | -17.3547 | -55.0339 | 2024-10-09 02:16:44 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| f7ea9977-75a5-341f-b55c-f0d1af9e0527 | -18.1193 | -56.3921 | 2024-10-09 02:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.8 |
| eb0b797c-2f80-3aa9-bad4-de83fc908346 | -19.9924 | -42.4346 | 2024-10-09 02:16:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 112.5 |
| 30957a17-8a8e-34ed-b95a-f3fb967bed1e | -20.0122 | -42.4541 | 2024-10-09 02:16:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 257.2 |
| 1cfe7203-a04a-3769-ab68-829ceedaa7ae | -20.013 | -42.4287 | 2024-10-09 02:16:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 272.1 |
| ae69802e-85e4-33eb-ae02-a45c18270f4c | -20.0336 | -42.4229 | 2024-10-09 02:16:56 | GOES-16 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.7 |
| 60e67b02-3f9d-31ba-a0a8-56c0b1d46f87 | -20.3142 | -48.7353 | 2024-10-09 02:16:58 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 93.3 |
| af99446e-2a76-3500-af2b-1db4aefa1bd6 | -20.3148 | -48.7121 | 2024-10-09 02:16:58 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 725b73aa-a55c-3588-bfc7-03c066e36292 | -20.3346 | -48.7307 | 2024-10-09 02:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 389.0 |
| 0969abbf-aa41-357e-8560-5667f2a10991 | -20.3352 | -48.7076 | 2024-10-09 02:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 375.1 |
| c2ac7b8f-1911-339d-bfca-0a5a8d4b1911 | -20.3551 | -48.7262 | 2024-10-09 02:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 329.1 |
| ed119ee5-0ae5-37aa-b41d-18ab9ae3e315 | -20.3557 | -48.7031 | 2024-10-09 02:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 235.6 |
| c6d7298b-4c78-35e5-a91f-a79dd0b48c70 | -20.7839 | -47.2559 | 2024-10-09 02:17:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 80.3 |
| b0655092-714a-3e02-9689-411c7c8d16f3 | -20.7846 | -47.2323 | 2024-10-09 02:17:01 | GOES-16 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 9659ffce-bb17-3139-b704-9353e905cffa | -21.0926 | -47.2043 | 2024-10-09 02:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a810b88b-454d-34b5-9d0e-68e335d6aff2 | -21.1126 | -47.2229 | 2024-10-09 02:17:02 | GOES-16 | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 05c9473a-a4f2-3917-8701-79acd9544137 | -21.572 | -46.9898 | 2024-10-09 02:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 3074e7a9-b2e7-3b4c-a9c1-73f23cdf2890 | -21.5727 | -46.9659 | 2024-10-09 02:17:05 | GOES-16 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 6979aa37-1ca7-30c8-99c7-e5b997b2e341 | -21.5864 | -47.8827 | 2024-10-09 02:17:05 | GOES-16 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 86038e0c-9700-3206-b79a-fcbeaedaf099 | -22.1369 | -48.1224 | 2024-10-09 02:17:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 83043f68-7ffb-30fa-ab13-bba41337ff55 | -22.1571 | -48.1409 | 2024-10-09 02:17:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 098d2377-78d2-39de-8a02-3573dad0ed32 | -22.1578 | -48.1172 | 2024-10-09 02:17:08 | GOES-16 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 183.7 |
| 847e7323-7a50-3ede-a352-3220bb2d35a3 | -22.1772 | -48.1593 | 2024-10-09 02:17:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 2f55191f-c457-3864-a465-2c33354d54aa | -22.1974 | -48.1778 | 2024-10-09 02:17:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 9ccfb0fc-66f7-3fa2-98b7-d81bd998d680 | -22.1981 | -48.1541 | 2024-10-09 02:17:08 | GOES-16 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 168.4 |
| f27b6a61-e4ca-3179-9153-d8a998cbb9d4 | -22.7927 | -48.4278 | 2024-10-09 02:17:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 8c607874-9b90-379f-9351-4628425c5d62 | -22.813 | -48.4462 | 2024-10-09 02:17:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 04ea428e-165e-3382-9aa9-ac3ba72b0088 | -22.8137 | -48.4225 | 2024-10-09 02:17:11 | GOES-16 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 75d95ac7-dd31-37fd-a1a1-aa5c1087af44 | -13.7123 | -60.600101 | 2024-10-09 02:20:03 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 20cb4f2a-8d75-3a70-ad5a-df8919b2ef2e | -13.7181 | -60.621498 | 2024-10-09 02:20:03 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3dfcf31a-791a-3f2b-a098-01aea637445c | -13.7085 | -60.624298 | 2024-10-09 02:20:03 | METOP-C | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5f947011-d00c-37fb-aa6d-e8587e9d3086 | -13.3788 | -61.908901 | 2024-10-09 02:20:14 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f21d7602-fc26-312f-bde8-55f01221f0c3 | -13.3835 | -61.926701 | 2024-10-09 02:20:14 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0ed54dd9-7ca8-3c51-b54a-200716d68be5 | -13.3692 | -61.911598 | 2024-10-09 02:20:14 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ad250827-04ca-3c7c-96dc-d3d60c08b0db | -13.3739 | -61.929401 | 2024-10-09 02:20:14 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6b9ef005-f274-376a-90c7-70b14b30ad8f | -13.3595 | -61.9142 | 2024-10-09 02:20:15 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 88b76cf3-d0ec-3c7b-b225-4f8c10505f88 | -13.3639 | -61.970001 | 2024-10-09 02:20:15 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bf945994-923a-3808-a5de-61406af55f04 | -13.1281 | -62.293598 | 2024-10-09 02:20:20 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0934e603-e7b9-38a6-bdef-80b31a261aeb | -13.1325 | -62.310501 | 2024-10-09 02:20:20 | METOP-C | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cec3052b-ed11-3d03-9670-be5f5f9ffbfd | -12.9655 | -62.463299 | 2024-10-09 02:20:23 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8ed3e7c4-4409-397c-bf76-3bc09af36725 | -12.9515 | -62.449299 | 2024-10-09 02:20:23 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| dd014f9e-d3cc-36cd-8790-ac60b95b93c8 | -12.9558 | -62.4659 | 2024-10-09 02:20:23 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b76f9565-eeb1-3734-8eb0-45baf753755a | -12.9419 | -62.4519 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5b61d4-7ea9-3906-8e78-1708cf14f402 | -12.9462 | -62.468498 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8dba2291-b2e7-3a79-8257-c12cd15d4a0c | -12.9322 | -62.454498 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6733a2c3-3db8-392e-bc68-d349c8d12314 | -12.9365 | -62.4711 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| db251fea-2c28-38a1-94ac-00167ebd7f0a | -12.9182 | -62.440399 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 329cd43a-d712-3119-853d-aa1e5563a50a | -12.9225 | -62.4571 | 2024-10-09 02:20:24 | METOP-C | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README52.md)
