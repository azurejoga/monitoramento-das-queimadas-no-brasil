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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8d4e1d2-f1ba-3ad6-bf18-8a7f96b148ca | -17.90402 | -57.51966 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4f70b8d9-4a4d-3dae-895d-7d0457397f2d | -18.06646 | -57.5573 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d33975f5-3ccc-3c9f-bf4e-058fc9e4592d | -16.0051 | -59.54729 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78886b98-e3bf-32ed-8513-f96e37255b36 | -16.0039 | -59.55683 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 06d61389-252b-3a10-b430-f849b9ae70ad | -18.03951 | -57.56224 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8d0ba974-adcd-3998-9c61-f0a1c4be02f1 | -17.82097 | -57.66227 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d255c24f-922b-32b3-bde3-c0c4e2efb050 | -18.06044 | -57.56039 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 38ed4bf4-a562-3d02-95fd-8f5ca9f86083 | -15.97157 | -59.54208 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0ddd4b03-dd9d-3c13-9599-406d6b7d3e84 | -17.90008 | -57.5032 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 224c17b4-9e6a-3cf3-9781-e61a2f5fd02b | -15.97215 | -59.53739 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 692f3b30-15bb-3877-97b9-ed4d0207d5c5 | -18.03387 | -57.56175 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 914aa4b3-ef1a-3711-b8c7-e94c1f3313bc | -17.83863 | -57.65527 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 73416f93-4065-3139-ab5c-71f9bb69cdcd | -17.84987 | -57.65583 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 4ec20e5d-c8a6-3c31-ac5c-ba6fb980ecad | -18.03309 | -57.54946 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| fd91b9b4-f0df-3b08-b875-38fe75f1174d | -16.00865 | -59.55381 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 23aac8a0-9572-3f24-a9e7-2e42494eabe9 | -17.83897 | -57.65201 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b444f1f3-6d64-3499-89ab-b2f8f5c2090d | -17.89803 | -57.66753 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 12286a2f-76bc-3025-84f3-256bc39837aa | -15.9674 | -59.53637 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bbf79ef0-b7a6-3236-8ddf-e829e0cb7f7f | -16.00581 | -59.5416 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26545406-707d-3b3f-853e-138dd5b9ea16 | -18.02856 | -57.55816 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4db5e38f-c476-36a1-89b2-43374e50241d | -17.89764 | -57.67136 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5a662597-b0fd-3613-9798-4a13ef6d3771 | -17.89331 | -57.67207 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 88a2f44a-0169-32ad-975d-5d0c6906ce11 | -17.88857 | -57.66368 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 3314804b-0160-394d-ac1f-198c02322554 | -18.06614 | -57.56039 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d8e0d5a6-5375-39b2-97cb-1a6a65ef9ae5 | -17.90055 | -57.49876 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1a46e896-cc8d-325d-91d0-0b6680cf303e | -17.90957 | -57.52108 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 76a9d8c0-a402-3aaf-a445-37fab60c6fbe | -18.03187 | -57.56141 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 18f9acf0-5dd8-3fc6-9713-24578a8f2b2d | -16.00983 | -59.54385 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7acd05de-a90d-3a07-b297-973d2de6cd80 | -15.97275 | -59.5325 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98dde72c-3222-32b3-92e3-4f16a88eef9f | -18.03785 | -57.55862 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 591eb40d-227c-3698-a929-54c59b8a6726 | -15.97098 | -59.54691 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3cea465c-2197-362f-86b1-48dc957afa3e | -17.90469 | -57.51345 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e0ae400d-c953-3d54-aa9c-057c701435f5 | -17.85154 | -57.58587 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bbb925a3-5e3a-3729-a05a-a67c4b62bdda | -18.02951 | -57.54937 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 61223edc-6de5-3cf3-b20f-7d88fd1241f7 | -17.88816 | -57.66751 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4dc255e7-dd85-3c54-b02d-24f0f6578046 | -17.91983 | -57.6199 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e48f945d-7db0-3e5c-a5b4-776a8250dc28 | -17.83299 | -57.65524 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1289bea8-3c6d-3efb-9ab2-7eae0d5acbd9 | -17.82664 | -57.66205 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 0cc5b42f-8626-3227-b23c-6ee795cd7352 | -17.89336 | -57.51276 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| edcbf91c-7782-398d-b1fb-dbc161b8d037 | -17.89414 | -57.66443 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7603b21d-9e91-3f84-bc79-28e8cd139230 | -15.96681 | -59.54118 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8035faf1-2626-3db0-a105-f5e3f2f358db | -17.84605 | -57.58404 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| da30ed74-f175-3126-be66-a23131227707 | -17.90401 | -57.66423 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 84c0da19-9ba0-30e6-9ed8-92e225fe6783 | -16.00503 | -59.54313 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de7e7879-da95-3982-b85d-572e19534f43 | -17.90439 | -57.66047 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b10bfd09-0f5b-3089-b4c8-6d7629bb342e | -16.0044 | -59.54846 | 2025-10-10 05:44:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1e820731-c024-3329-9de0-4c3159b02862 | -17.90573 | -57.66173 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ec750eb6-b0ac-310d-8183-c98feddb9fab | -17.89393 | -57.50736 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 02e762e4-32ce-35f6-bb9c-0bdd9d831258 | -17.84425 | -57.65552 | 2025-10-10 05:44:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f2f0d24c-e079-3371-9a39-7716911569ab | -2.6777 | -48.40724 | 2025-10-10 06:08:00 | AQUA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1d581ddd-a771-30a9-bb71-449da7fea5df | -4.65041 | -43.19262 | 2025-10-10 06:08:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4f141534-f147-3461-8ee1-0918ef8e50e5 | -3.74049 | -44.38376 | 2025-10-10 06:08:00 | AQUA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7be319fa-f0b7-3249-89ae-afe40e5ac021 | -2.49036 | -47.57303 | 2025-10-10 06:08:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 226fb9d3-da05-3ab8-8d18-944fbe5e7137 | -2.94506 | -49.34168 | 2025-10-10 06:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a2c85167-1cf4-37af-bf46-ea58df672d19 | -2.49169 | -47.56416 | 2025-10-10 06:08:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 0056b4ab-9498-37fc-8d7f-604d9071008f | -2.94642 | -49.33275 | 2025-10-10 06:08:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| c7fc3ae6-30a4-3965-9cac-b79dffabfe9f | -8.20883 | -43.35958 | 2025-10-10 06:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 0d0cc65a-6b89-3df6-8799-964f8cada719 | -14.6781 | -48.05658 | 2025-10-10 06:10:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 24.5 |
| c6b930a4-015b-383f-9d3a-0a7361e78798 | -8.20635 | -43.37874 | 2025-10-10 06:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.1 |
| ccc3100e-3bd1-363d-b6f0-ea9b2ce1cbc9 | -10.15415 | -44.60196 | 2025-10-10 06:10:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 7f2699e0-eae3-3d05-9a1f-cabba1013655 | -7.77612 | -44.04861 | 2025-10-10 06:10:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| c1582f0f-42a4-31e8-b08b-8c7b4556def9 | -5.48283 | -43.06243 | 2025-10-10 06:10:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8478984e-1d99-396c-91c1-76cf196cb964 | -8.20668 | -43.35398 | 2025-10-10 06:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 7f4132cf-5200-3346-8bed-ef91597b91b2 | -13.30749 | -47.99017 | 2025-10-10 06:10:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d316fedd-ae2d-3108-86c6-e97c9ed67c5f | -8.18676 | -43.31261 | 2025-10-10 06:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.4 |
| 7e9ae380-b419-3b4d-bf7a-e7157e9d0c22 | -10.15899 | -44.59575 | 2025-10-10 06:10:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 41c61499-a9a1-3e57-a8d3-3bf440af3e48 | -6.81773 | -42.79206 | 2025-10-10 06:10:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 0344f149-36d6-33b0-8a76-518229f262fd | -7.76845 | -44.04221 | 2025-10-10 06:10:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 63959bd5-048b-345c-bb4c-2ffec94e351b | -6.74575 | -42.84269 | 2025-10-10 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 6932e2d3-7fac-37f6-b7f9-bd312c8c618e | -12.62855 | -45.06194 | 2025-10-10 06:10:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 21933fc3-4b18-3d37-8b38-34529fc27015 | -7.40642 | -45.91834 | 2025-10-10 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a6eb8d64-bbc6-391a-9d33-99a03a486db8 | -6.74645 | -42.83589 | 2025-10-10 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 6f8416c4-da64-327d-946a-93e2874a870a | -14.02298 | -48.14152 | 2025-10-10 06:10:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f7e4ecde-031c-31c5-89f8-67b221976872 | -13.36137 | -47.74245 | 2025-10-10 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8c0e214d-b023-3a33-ad29-65b0c27e0d8d | -7.54203 | -44.59035 | 2025-10-10 06:10:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| c8e8a8f9-2e3b-3aae-8dab-5fb395034ba6 | -13.84465 | -45.84258 | 2025-10-10 06:10:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 36be06ec-fd8f-37c1-b6ba-fb66c2a94a6d | -8.19675 | -43.33323 | 2025-10-10 06:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.3 |
| 0ed16b49-4065-39e1-8be7-7a6f331d2d4e | -7.54 | -44.60506 | 2025-10-10 06:10:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a14e0f0d-874e-34df-a835-b97f73c7aa1f | -13.37104 | -47.74427 | 2025-10-10 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ac9c1eeb-4efb-356e-b7b7-3543eda807e3 | -4.23684 | -48.68518 | 2025-10-10 06:10:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 4efa1f2a-e309-3b89-a9ee-72086a2915ea | -12.63067 | -45.04556 | 2025-10-10 06:10:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 13baf3b4-b204-3624-9837-8fe9ae92616d | -6.72823 | -42.87315 | 2025-10-10 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| f984a7f1-48a7-3173-a866-fd7fe219a37e | -10.1563 | -44.58524 | 2025-10-10 06:10:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 09ca2949-0897-3bd6-9747-66d11a7895b4 | -8.20406 | -43.37311 | 2025-10-10 06:10:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 800302df-f4bc-3c91-9975-6652ef651fbc | -7.40848 | -45.91171 | 2025-10-10 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 66b48f1c-7a6b-30c8-a7b8-146492298e9c | -6.74834 | -42.82336 | 2025-10-10 06:10:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 54d8e485-e35e-38dc-a954-3b00c73d89f8 | -12.70952 | -45.8434 | 2025-10-10 06:10:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 2680403b-60db-308c-bbc3-6eccb6475539 | -13.00062 | -47.89953 | 2025-10-10 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4aba93fe-6b71-3e9f-9736-9ed24f78fac7 | -7.53585 | -44.29625 | 2025-10-10 06:10:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 8de1fcea-24f3-3fe9-822f-f805a88e017f | -12.71143 | -45.82896 | 2025-10-10 06:10:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 114ef109-814d-3ea6-8ccc-03e08eb94a56 | -7.40676 | -45.92353 | 2025-10-10 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| b902e152-8436-3419-822b-1877e2f7652e | -4.40787 | -48.95523 | 2025-10-10 06:10:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| a74b41a4-9f04-3297-a026-d1a69cd9c7d4 | -14.26087 | -45.89923 | 2025-10-10 06:10:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| cbbe8c68-5f92-3007-aa68-c4715da6a98a | -5.48027 | -43.08052 | 2025-10-10 06:10:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 405ee9c6-3484-31fd-9bb9-b5951b21115f | -13.8434 | -45.84946 | 2025-10-10 06:10:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 51c88274-a2e2-3bd8-b43e-d0ff59229d49 | -13.36947 | -47.75552 | 2025-10-10 06:10:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1f5d19ba-b975-3754-9060-2d1d4f9c88ba | -14.01341 | -48.14008 | 2025-10-10 06:10:00 | AQUA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d5478e29-f2d9-34e6-9cd0-fe017c6132c3 | -10.15684 | -44.61155 | 2025-10-10 06:10:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 60b5eb40-5b93-3307-b75a-137e8188d716 | -10.19147 | -44.58953 | 2025-10-10 06:10:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 776c6c0e-1c15-3cc0-bbee-5ac6860db695 | -7.39667 | -45.92209 | 2025-10-10 06:10:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README50.md)
