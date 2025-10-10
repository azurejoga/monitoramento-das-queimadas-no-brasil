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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 312ae560-26d2-300e-9af6-cb36acc9841c | -17.93829 | -45.01903 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a8e20eda-3526-3002-9d03-b053b1a603f0 | -13.35079 | -47.62994 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 903f10b7-f88d-3f63-858a-08bd2bf22751 | -13.35273 | -47.75438 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0aec762b-c28d-3c9a-844b-6df0fe25b0e1 | -14.68905 | -48.06816 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffbd75a1-8543-3438-8ad5-557fc14d7677 | -16.66968 | -47.5979 | 2025-10-10 04:53:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ba6b30e-4d58-39cb-82ff-807dbda1ae65 | -17.94806 | -45.03463 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 255d185e-f99a-3d96-b1f8-a29a0309ee13 | -13.80432 | -45.82351 | 2025-10-10 04:53:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bf9c4db-2cca-3168-a5e0-97188a2ac909 | -16.26735 | -47.16082 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 22f7cbae-534e-375c-b436-5e77d8f659ba | -13.84428 | -45.83252 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 385b8bd1-0fc4-37d0-99ef-8d18d0af810f | -16.74166 | -43.97824 | 2025-10-10 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 947eab0d-273f-3f12-8401-c0f5d8e5a86e | -18.54087 | -45.07435 | 2025-10-10 04:53:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55670dd7-89e0-318c-947b-be856331c6f6 | -18.07137 | -44.97974 | 2025-10-10 04:53:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e537bbb-b198-3396-9229-42e55bdab3fc | -13.26453 | -48.02568 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 454dbf2c-8696-37d0-b7aa-1de8ec93769e | -14.57309 | -47.46078 | 2025-10-10 04:53:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2c64a61-0307-3496-b19f-585968aafb45 | -17.82228 | -57.65928 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 33995c67-bbea-3ed2-9a9c-abf43677e7dd | -16.3031 | -47.15019 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c1e55b7d-1c17-34cb-a0fa-dfba47ebcc08 | -13.35337 | -47.7494 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33bdfb54-c1ab-33fe-8111-2b3ce0b74ba7 | -17.93263 | -45.01883 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| df46a5ab-89c3-3add-8d9b-1c83b2ca9d13 | -18.7436 | -48.08144 | 2025-10-10 04:53:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3a3c94a3-0bc7-35cc-901c-a7fc890678c2 | -15.24638 | -46.37613 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 88dc1769-6360-3e06-bf0b-861cbdafc669 | -11.72124 | -62.98286 | 2025-10-10 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9026cffc-54e1-36b0-baf7-381c42398141 | -17.82912 | -57.66092 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f47aee58-0944-34c8-a35f-a3cdde7a1fee | -16.05353 | -48.07425 | 2025-10-10 04:53:00 | NOAA-21 | NOVO GAMA | GOIÁS | Brasil | 5215231 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6a2670a-c75e-3ba2-9cfe-819c04517999 | -17.89091 | -57.50545 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| fff645dc-5023-3509-8792-34f180e6922c | -15.39851 | -47.30862 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5b47a369-66ab-3cc7-a38d-cb700de6981d | -11.25931 | -61.4653 | 2025-10-10 04:53:00 | NOAA-21 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20894873-828b-3b26-acf7-58cb86083f9c | -13.32226 | -48.48109 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9beb8806-302b-3bea-b0ab-90db05be7118 | -13.28335 | -48.01609 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 503f0229-9e02-3f5e-8a65-02d8f41637a4 | -15.97402 | -59.542 | 2025-10-10 04:53:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0b6eaaab-be4c-31c1-828f-4adf8e235b85 | -13.83962 | -45.82865 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c3ca6cf-18fd-31ce-8c3e-4a6e45c4f523 | -14.39359 | -46.00769 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48f50903-a1a2-320a-afa3-ef4a8ade649e | -15.91432 | -43.2868 | 2025-10-10 04:53:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a1884cf1-01d9-35fc-9b76-38c0faa95b69 | -15.01354 | -47.56032 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b57024e5-5423-3112-8a88-f065551aa5e9 | -13.40757 | -47.25681 | 2025-10-10 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ed4a8b03-01c8-3f7a-9b84-9c6b81472270 | -13.41213 | -47.25743 | 2025-10-10 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2fdd774c-288d-3cfa-a80c-91641c82224e | -14.44503 | -47.97621 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1254190f-5b02-3462-8600-d3114a510e82 | -17.99498 | -44.96681 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27212e37-9ef6-3f10-8f30-5f1efdb932ce | -18.78497 | -44.61797 | 2025-10-10 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7001b34e-b093-300c-9625-b09d6df9a7d3 | -17.8381 | -57.65004 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 6cd7c834-64cc-31ac-aa33-7699099f6c9e | -13.82454 | -45.78386 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88d1bef7-ec52-3cc2-ad4e-1cd96e1eed46 | -17.98975 | -44.96218 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12c31a2b-c013-34d6-89da-d283bb182d8e | -15.40679 | -47.9936 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1df8e47c-2434-36c1-b480-7f714603cf5b | -13.31714 | -47.99327 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a29497c-90f9-3c94-b7b9-8bee97bf9558 | -17.82982 | -57.6568 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d99d4005-7ce5-39e3-9bad-67c6ba2b18e0 | -13.29906 | -48.48626 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 96f4a2d5-6382-3aee-8775-a0888af3f383 | -11.72187 | -62.97964 | 2025-10-10 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa885944-93ec-3451-b50f-02063419062f | -14.02806 | -50.71788 | 2025-10-10 04:53:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5ff6b6f-823c-3626-892e-4248120e439e | -16.2756 | -47.17254 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 594d5020-5204-32d9-b141-837722c49ea6 | -14.99175 | -47.20273 | 2025-10-10 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 870ad4ba-8883-36dd-af67-1b46dc58446f | -13.84174 | -45.85307 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1777fceb-c1fd-32a8-977a-defa2f847a54 | -15.38378 | -48.03202 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32723809-f358-3433-ab8f-cb2259935819 | -17.90467 | -57.5078 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 03903c4f-e791-361d-86c4-5fea3e33798b | -17.82695 | -57.63182 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7578d4ea-5b48-34a5-b12c-91b57543480e | -13.84036 | -45.82264 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 479d9f76-329f-37d8-9071-a1dfc4695bb0 | -17.93146 | -45.03032 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 434f39c5-5da3-32ae-9b9e-212348efa701 | -16.43895 | -47.81419 | 2025-10-10 04:53:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f4f8c7e5-213d-39ea-b382-a467cc13d3b7 | -18.07177 | -44.97584 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 62802951-b3d8-3dae-8df0-c079d2e20d36 | -13.84531 | -45.86562 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 469ea116-7017-397b-8e91-a7d4fd13a168 | -15.40972 | -48.03248 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9cbf1ac1-0a42-3bf5-a5de-afe1d18a9c9e | -11.71664 | -62.97863 | 2025-10-10 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4fcc7e7-29bf-306f-911a-903317a0a077 | -13.22247 | -47.79139 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87d52a9b-9b06-3421-80e4-1c89a7731a37 | -14.91313 | -49.10118 | 2025-10-10 04:53:00 | NOAA-21 | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3705fd5c-12f1-3e5e-990f-053c3691f647 | -14.94525 | -46.77437 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 957cb929-c8b1-3dd6-a774-faa69480fce0 | -12.08855 | -64.2306 | 2025-10-10 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0199af72-19e5-350a-9119-623c8204c9ac | -13.84072 | -45.81968 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9643d675-5db6-37d5-8f9c-f17a515c29d7 | -13.35773 | -47.75041 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bc908bb3-bf8d-3189-a983-487e5c6f8da7 | -16.74402 | -43.97454 | 2025-10-10 04:53:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 055afa20-ff83-3366-a078-be29f00e456f | -17.81744 | -57.64596 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dd1063da-ac6f-3f04-b363-3c34335a08e6 | -15.38155 | -48.04953 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a551835-644a-3753-85a2-fc322637bb19 | -13.32642 | -48.48196 | 2025-10-10 04:53:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7763fe6-1e9c-3c33-91cf-ee727c20a0c5 | -14.26934 | -45.90018 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4d725b74-e652-3f79-a4ba-c97cec01a9d6 | -17.89373 | -57.50968 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.6 |
| 0a87fb03-c91e-3ea8-a047-5f9248164bf9 | -13.26833 | -48.03035 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eba4276-204d-30b4-861d-c76ac8908aef | -14.43052 | -47.98447 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 963fd816-87fe-317c-a216-e6f5e08d1466 | -14.38426 | -46.00349 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 054ed51b-f77e-3b02-b3a9-c8d23d5ec88b | -14.38391 | -46.0031 | 2025-10-10 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99625dfa-09e0-3986-9c59-36659c543cdb | -12.08778 | -64.23454 | 2025-10-10 04:53:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ec41924-8b92-3ebc-86ce-f367f0b9d95e | -13.35521 | -47.63069 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c804ed7-aec2-3a7c-bfe0-77c2f54f9f90 | -15.42969 | -47.99191 | 2025-10-10 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0e8633aa-8694-349f-8da3-7d9ccd1bba37 | -16.26672 | -47.16599 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dbc4581-4e09-32c9-bc25-a00dd9c7ae52 | -14.42399 | -48.00021 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63b4ffc6-966d-3901-a407-af9af60ba9b5 | -18.77882 | -44.61847 | 2025-10-10 04:53:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b928ae61-0ec9-3538-bcc3-639e0f53566a | -17.93222 | -45.0228 | 2025-10-10 04:53:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 201923e0-def6-3a01-ad94-20e9fb6ac106 | -13.36707 | -47.7475 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 352d323d-313a-3951-a0ad-8e7d757efc57 | -14.02869 | -50.71341 | 2025-10-10 04:53:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43083a03-906a-3429-a91a-31057189e58b | -13.34404 | -47.75229 | 2025-10-10 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 5ed4c5a8-0b37-399b-b494-11a15591dac4 | -14.93165 | -46.76983 | 2025-10-10 04:53:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| c356c7d4-ac71-3d6e-9a83-779675656c18 | -14.69345 | -48.06869 | 2025-10-10 04:53:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd1ea9e7-fab2-30d3-bf3a-2e81bb3c6d56 | -13.31344 | -47.98783 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d7ee9205-80ad-3e73-b015-e0008047ce86 | -17.37942 | -46.90265 | 2025-10-10 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| efa3d88b-7f96-3b98-821c-a8eb6dceb4ed | -17.84153 | -57.65078 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7f4fbeb6-7298-348d-8d25-82a1691e9095 | -13.33066 | -47.99102 | 2025-10-10 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5933a58f-bd1d-307d-85ce-e5543f367851 | -17.822 | -57.61905 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 28c4049b-482e-3ea9-a592-b8aa6068ebd8 | -17.84944 | -57.5831 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e896994c-3809-3cef-bb92-87aacd0637d5 | -11.72185 | -62.97889 | 2025-10-10 04:53:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11f2a6ad-4f3f-351e-9af6-e0863a7e94e0 | -16.268 | -47.15551 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3349aa60-aede-359b-943c-c94d7265b97a | -16.28038 | -47.17883 | 2025-10-10 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b177c2be-e941-3ce8-b182-07b0fcb7a2a7 | -14.26354 | -45.9056 | 2025-10-10 04:53:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7696db78-301c-3450-8b4e-9e1b1b2524c6 | -17.38185 | -46.89849 | 2025-10-10 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 01ef87b3-8067-33ef-a3a5-25a7552f1d81 | -17.84052 | -57.59383 | 2025-10-10 04:53:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |


[Clique aqui para ver as próximas entradas](README41.md)
