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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f4edf63-b932-3e37-a2b5-1c09926e8a57 | -18.19526 | -56.54324 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| f4cd6ca4-518f-3fbe-81ec-d06f50216df4 | -18.19473 | -56.54774 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 1805f7aa-4379-32d8-add1-c26ea66c22dd | -18.1944 | -56.52762 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b2049ed8-37a9-32d4-9dca-c57fc6994eee | -18.19405 | -56.51554 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ca0bddd8-e325-35a2-98ac-873870cc85d6 | -18.19351 | -56.52007 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 11e09a4e-bc1d-35a7-9a09-8766bcaeaefc | -18.19212 | -56.54562 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 2f4ce2b1-6508-386c-9035-e15401456249 | -18.19156 | -56.55011 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| dd3c8984-5cfc-3b4a-8a2c-251e593007c2 | -18.19053 | -56.52253 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 32dbd14f-d2d0-3985-a334-28e35d3de616 | -18.1903 | -56.54714 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8b65f3c2-681e-3561-bacc-565be494c12a | -18.18976 | -56.55164 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 85ec724e-6f6a-3570-85a2-4cb12d516d90 | -18.18907 | -56.51947 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 382740b4-6956-38dd-9654-7cb0665edccb | -18.18883 | -56.53604 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 172ee96d-1e76-310f-8805-43484856663e | -18.18826 | -56.54053 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fc0e2dca-f21e-3611-8c23-92e2c559a65f | -18.18769 | -56.54502 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 19e8bb83-2ecd-3f71-970e-5f944c09e1d1 | -18.18713 | -56.54951 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 23d9a577-e6b8-3b05-83c7-acb1f9ad528a | -18.18666 | -56.51741 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| afdc7c59-5cee-3ab1-99d0-ff5f79f8dc6a | -18.18609 | -56.52193 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 222c3296-79de-3fdf-a521-5735d558e3a7 | -18.18552 | -56.52644 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| fbb0333a-a9bc-3fa3-953b-bbe07ae08b05 | -18.13559 | -56.45522 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e3556e06-d0b1-3f91-bea6-8bac09521012 | -18.13375 | -56.31947 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b3a7f8ca-80fb-3c1a-a7fc-131fd83fad09 | -18.13319 | -56.32412 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 656f6204-4b73-3beb-80f7-1f5effcdbf1b | -18.13153 | -56.33802 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 4fdc1ae1-6a40-3c1c-8ef9-2d890a8f73b9 | -18.13098 | -56.34265 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 50b8c169-31f6-3329-b73f-db289fef03ef | -18.1298 | -56.31423 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 540f3ebe-9a72-3302-99ce-fb184e2e48d4 | -18.12925 | -56.31887 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9b6b8d82-b97a-3613-86d0-22ec8e9efa2a | -18.12357 | -56.28971 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| b17d606a-de25-3213-a78f-75960c37b0de | -18.12144 | -56.29227 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3b511a94-25bb-3f58-bf81-b6c127efa40f | -18.11907 | -56.2891 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f9a0069d-e38f-3360-b280-02ff877df931 | -18.10287 | -56.43953 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5c8f2a1d-f46f-3468-9d8b-49821579dea6 | -18.09939 | -56.32238 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c6ab371f-0e70-3bde-ac36-8c5231a4c789 | -18.09659 | -56.44068 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f99f81b0-251d-3c27-9e0e-0510436ea77e | -18.09396 | -56.43833 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7f5b5b4c-c1c4-38e0-87ca-d4bb13743b0f | -18.09339 | -56.44288 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 35982ff8-1e57-359b-9eaa-83cbe7de0599 | -18.09294 | -56.41038 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c41b221b-9ef1-3895-9df6-cbaebda4ddb3 | -18.09252 | -56.39833 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b0e76c06-2294-3151-ab24-1e5aa7262648 | -18.09237 | -56.41495 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 9f22a365-75b5-338e-9445-efeb6b46ae03 | -18.09213 | -56.44007 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1703cffe-48d6-3c41-a5af-d2aded5ada50 | -18.09179 | -56.41951 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bdc0a88f-3fbd-3d6c-90c8-5333a826bf32 | -18.09144 | -56.40751 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 508b7563-a788-391a-a4bf-fd51a749eb51 | -18.09122 | -56.42406 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 4f5380a0-0de2-3c37-854d-f6694a197a59 | -18.09091 | -56.41208 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e6a8a09f-a02c-37f4-82df-f222127cd247 | -18.08983 | -56.42122 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 456eab5d-59b0-322a-98df-454864fea98b | -18.08929 | -56.42578 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4609ccdd-5719-3e44-a317-56bfe00c24cd | -18.08926 | -56.33041 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ae391d1d-a663-32d0-af81-4c3b906cfa44 | -18.08905 | -56.40521 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 71b3f3ab-ad5d-3bc2-b122-fa8237289e0f | -18.08848 | -56.40978 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d3b5e61b-bea4-3788-981a-76ad0346bb4a | -18.08677 | -56.42347 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 486cdadc-94f4-31e6-b5de-34e6c25c8210 | -18.08515 | -56.40002 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0804f566-48c4-3955-8810-69eccd637d87 | -18.08401 | -56.40917 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e2f69e07-5f71-37f2-9834-976d03f81da3 | -18.08297 | -56.38108 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 86f022ce-aeb7-34be-b85b-c86c58c74273 | -18.08174 | -56.42743 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| b98ed754-c648-3580-9fcf-8cf85f4d4d52 | -18.0785 | -56.38047 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8fd2ac36-9676-3d33-9ab2-698de594fb9d | -18.07403 | -56.37987 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 00cc21a4-dc90-32c0-8692-f8e2bc4ff6c3 | -10.57221 | -55.89806 | 2024-10-12 05:25:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6cd4c685-3fe1-39f6-9607-4f205ad2f682 | -10.48776 | -55.60852 | 2024-10-12 05:25:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 167b0607-67d7-3829-b668-6e86ac519cfd | -10.48323 | -55.57958 | 2024-10-12 05:25:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d4044f5-8ae8-35bc-b0e2-d1d4891092e8 | -10.47899 | -55.57898 | 2024-10-12 05:25:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09d0d8d3-ae6f-376e-bc28-a0fc92e56248 | -10.47843 | -55.58294 | 2024-10-12 05:25:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1659ac07-c301-301c-9e87-0c39753b2470 | -11.93182 | -56.93117 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d53966b7-173b-3505-9214-fc1104ddf6f1 | -11.93047 | -56.92733 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e219bfb4-e643-33d5-94b3-89ee6deecdb8 | -11.92793 | -56.91638 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85b45230-aba0-3a22-8f8b-4e57c825480f | -11.92786 | -56.93061 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5508446f-255d-3c8f-881d-b48e342171a5 | -11.92613 | -56.91452 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f59b5284-5d4b-3e2a-8d3e-f05766009fc0 | -11.92538 | -56.91972 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa569d80-2bde-34dc-aa7d-bdce00368320 | -11.92467 | -56.91063 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f47db78-4860-3e21-9261-d32763ae0920 | -11.92396 | -56.91583 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d0cb93b8-5a3b-3727-92b9-c5ab8dd8be85 | -11.92325 | -56.92105 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df9b2ab5-50d7-3f87-875a-112103be00db | -11.92216 | -56.91397 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 086f2c85-0041-3147-a862-8155654858d2 | -11.92141 | -56.91918 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c86abd3d-7285-3c74-bb18-5dafd874da81 | -11.9207 | -56.91008 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8988d71f-c2bf-3a48-9239-15f4e21331c5 | -11.91999 | -56.91528 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79191563-bb74-3832-b949-8c171125363e | -11.91928 | -56.92049 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a57307a-f2ae-3ce4-a203-9362fd5705ce | -11.9182 | -56.9134 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6402f60-186f-3430-af2b-b34ce03cae87 | -11.91745 | -56.9186 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c81567d-c5fe-3ec4-b615-169d3a67fcf3 | -11.91603 | -56.91468 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f8c3587b-6608-3fa1-89f8-d05aa9dbf553 | -11.91532 | -56.9199 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a31eeff6-9e42-3663-8746-08829f84adc9 | -11.91424 | -56.91282 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0effe2a8-3e7e-31c8-8a63-5dadfa4441e2 | -11.91349 | -56.91801 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 537f90b6-7573-3fea-a431-11e820463416 | -11.85038 | -56.87759 | 2024-10-12 05:25:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 209fd0b8-b3a9-32e0-a200-35f071867772 | -12.62194 | -56.51552 | 2024-10-12 05:25:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87625e4f-37bf-3ba9-84c6-41816e7d1d40 | -12.62144 | -56.51928 | 2024-10-12 05:25:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26e4c202-918c-38d5-aebe-3ef0a48766ea | -12.61965 | -56.51523 | 2024-10-12 05:25:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d88f5e6-687c-3021-bed5-47f456b82c63 | -12.61912 | -56.51898 | 2024-10-12 05:25:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 321e055f-f64e-3bb0-ab8f-f4d3d42f324d | -17.89886 | -57.32798 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 1fcd5b7c-03b2-373f-b36d-645d1dbbf6a3 | -17.89786 | -57.33593 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 156759b4-66ec-3711-8f3b-78d7797c7032 | -17.89743 | -57.27087 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 154377a4-9275-38a1-9fee-f7fe26229ef8 | -17.89693 | -57.27488 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 2c6ff784-d9f9-3e4f-ad3d-e4ac1d554d2a | -17.89643 | -57.27889 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 2e696670-5d10-3dea-a992-14fc45464d87 | -17.89566 | -57.31943 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| 3c9d0b96-6aae-3517-a087-812390677b3d | -17.89516 | -57.32341 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 2a331795-3e5b-3d89-90cb-75293c6831f6 | -17.89466 | -57.3274 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 316eff3d-998f-3245-ac25-b382d2b4e230 | -17.89417 | -57.33138 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 446b4e18-54a6-326b-9c9d-6ac018cd7aa1 | -17.89372 | -57.26626 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| dee81642-0e29-35cd-aca0-932d60f8f571 | -17.89367 | -57.33535 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 967215dd-9063-3234-993c-152f0c07df5b | -17.89322 | -57.27028 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.3 |
| 4ad1565a-149e-342d-9087-ad2fb624096f | -17.89272 | -57.27429 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| ca36a37f-b902-3606-8d15-f592672af5c7 | -17.89196 | -57.31485 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| e32b3f8a-8351-3cc9-b6cc-615690575bf1 | -17.89173 | -57.2823 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| bdc5344b-8407-3b1b-8ab5-c5d14d7ddb36 | -17.89146 | -57.31884 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.3 |
| d8f55be6-dceb-3448-8eaf-2871a4c4f0dd | -17.89097 | -57.32283 | 2024-10-12 05:25:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.2 |


[Clique aqui para ver as próximas entradas](README122.md)
