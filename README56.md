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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f166eaeb-58df-329c-828b-4202c157c1f0 | -17.92424 | -57.50321 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 705eab0c-878a-3176-8759-1d8268140e9a | -17.84544 | -57.5947 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c0388acc-ea3e-35c0-85ce-9c9641b92145 | -17.26709 | -46.97021 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 44fc7ab9-1812-373c-b047-e30980e2a957 | -17.53325 | -46.75139 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| cd795c1a-3494-3625-91a6-585679c5587c | -18.06544 | -57.5243 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d3908343-0871-3d96-9545-6a979b90dd55 | -15.97329 | -59.53819 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9967bab3-20ff-3ae4-9e0f-4f399c7b5f19 | -17.52959 | -46.75176 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1763ffb4-ef5a-3ad8-90d3-25f13ff67984 | -17.83029 | -57.65037 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0a2c4a99-dd53-3c0f-97ad-9d6e7000631c | -18.0439 | -57.52517 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 4d0164bc-f1e9-3362-a78c-9914b00efdf7 | -14.94351 | -59.4213 | 2025-10-09 05:14:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f25aac53-3f97-3126-8ac9-279b0913df57 | -17.85411 | -57.58398 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 74ede46c-7041-377f-8224-ae117a716c7f | -16.01897 | -59.5275 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2054ef26-9b32-3569-820c-a8820a9a639b | -16.37875 | -46.38709 | 2025-10-09 05:14:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a9036256-3ee3-3310-9bc9-08cdbf4716eb | -17.85938 | -57.57218 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 319aa872-9d35-305b-849f-54acd4f92c41 | -18.01535 | -57.5251 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3a1a3b1d-3c13-3ad9-a3c9-758753e90be9 | -17.27472 | -46.90919 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e35cab5-e16f-3f5a-913b-8b2bb651c4f7 | -17.89775 | -57.66382 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ba74deb4-9691-333b-9837-e6f14f8bfe25 | -17.8251 | -57.63719 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2fc61901-fb1c-3f36-93f6-c2ae9aa200a2 | -18.02233 | -57.52628 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c31ad470-cc70-34f1-a280-2e6b6f26b22c | -17.85176 | -57.60017 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f4303887-021d-3654-9ae8-0b15eead944a | -15.99253 | -59.54504 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 723b1ee8-1c7a-3f8c-a5a2-1f77c22f64cd | -17.82917 | -57.63356 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0b4c2c77-d973-398b-94f3-7f3ffc0cb28d | -17.27372 | -46.971 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 98225629-32eb-3223-9441-104f9c6959d5 | -16.60753 | -58.15901 | 2025-10-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 6ef7d1e6-d8c0-3091-8f3c-be8ef94d069e | -18.24485 | -55.38363 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bfb7fb84-89fc-3ad9-9a08-1f0e4c245099 | -15.2852 | -59.23754 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 674d7619-2ee2-3024-bf0f-93cb88dba435 | -17.52652 | -46.75073 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| d21860b6-3b66-353c-8c86-c25a1ddfc425 | -19.46697 | -55.47784 | 2025-10-09 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 07829ace-50ee-3136-b821-a15ca84baaad | -18.06713 | -57.5374 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 43a93ad8-1f31-3b93-a1de-f4b98e798c32 | -17.89542 | -57.6553 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 60561cda-6633-3ebd-bba9-030694a1e4bd | -17.63427 | -47.20775 | 2025-10-09 05:14:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 793fff1f-36a4-3672-9db1-afc36f4947bc | -18.04102 | -57.52027 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fba8cc6b-a95b-31a4-856f-c824bf5fa904 | -17.82691 | -57.62462 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bae2d8a6-f9cf-3711-9891-39e7fb36fd13 | -17.92879 | -57.52143 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e0696f4d-089e-315d-a33e-c5967253efd3 | -21.18887 | -57.3059 | 2025-10-09 05:14:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f20c7820-427f-3bd3-948c-0c5d9cfd89b0 | -18.24955 | -46.99377 | 2025-10-09 05:14:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 41879784-9144-3b22-8cf3-cc8a35fd99d0 | -18.03871 | -57.56143 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 6cdb2d33-c674-35fe-b5da-da5dcff18235 | -17.84827 | -57.64867 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| fad74c81-b2f8-34af-bda5-094cf0e7f9fa | -17.82624 | -57.65382 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c331a0da-e79b-3921-9f6b-96b576ebd90e | -18.02014 | -57.56664 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| d971c5e2-a9ea-3263-8822-9c0d824f3fe7 | -17.89485 | -57.65928 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d1b115a3-98e7-34e2-b1c4-498f32e15342 | -19.18317 | -46.50535 | 2025-10-09 05:14:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5556cebf-3f5b-3e81-a039-43f01d342d55 | -17.89196 | -57.65473 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 03eb5253-2a7f-32e8-a349-9571e64251d3 | -15.97989 | -59.53929 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fc1f491d-9e90-3d50-b238-359f72bcac99 | -17.39482 | -46.89336 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab757409-43d9-345c-aaa2-d48ae07f4543 | -17.71828 | -56.73471 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6b04e754-114a-3b35-8e1e-7fe13d928386 | -17.84774 | -57.60338 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b16e9e4f-cc9a-351e-9f64-49d7e5f68645 | -17.97779 | -57.5033 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 177f6644-8a77-3e58-8320-05ed3c7bd868 | -18.06196 | -57.5237 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9e6c599d-3fa4-3c03-991d-50c4706da4c1 | -18.02474 | -57.55944 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1c4507f8-2df9-3f33-97b2-fb0eb7ce3a2d | -17.38905 | -46.88311 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3d48ddb-99dd-3813-9ef6-bb94ff3a1cdc | -17.71585 | -56.77857 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 3e0755d2-656d-3645-b86d-43dcfee159c1 | -17.8477 | -57.65258 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 49a78ccd-8440-32d5-8990-178dcfb9a552 | -16.60415 | -58.15846 | 2025-10-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c4c63b8b-dcc0-3042-af6c-c523f27af52d | -17.39207 | -46.89242 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe2415be-1e49-32e9-abd7-51c26f70f75f | -17.84889 | -57.59546 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 43842e65-1e12-3927-9d44-7e9c3a9926c9 | -18.01188 | -57.49908 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 91513e16-27a6-386c-969c-255641060c8d | -17.99907 | -57.48855 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 79134897-7cf0-35a3-b573-dc3980b3521d | -17.85065 | -57.5833 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 6bd1e622-6c13-3066-ad53-e392fd90a8fb | -18.04107 | -57.5698 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d3d7d1bc-c537-3cfd-a5f6-daae1bcad947 | -16.70471 | -47.59159 | 2025-10-09 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9908b96-ba6c-356a-9a08-715d0f47d952 | -17.90236 | -57.65639 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 7f79d5b0-aff1-31c2-8cec-02b98cc972e7 | -17.84198 | -57.59407 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6fbd180d-ad9c-3d9a-ad98-0bd8f7fa71c3 | -17.38083 | -46.89911 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92639989-3100-3be0-ad73-748e1d5a0a48 | -17.85531 | -57.57571 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| b7b50d78-5205-370f-84c2-49d37b9b8f08 | -17.91543 | -57.51506 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 779f2118-eec1-38a2-b7a4-67252c37ca97 | -18.05846 | -57.52318 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 22f10921-6c61-3918-b30a-f4e80c7dc508 | -17.52285 | -46.75112 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 19b36ba4-97f4-340f-93ad-6f723b84df37 | -17.26805 | -46.90861 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c633fcda-47c1-3161-beaa-9259ddf96834 | -15.99197 | -50.98455 | 2025-10-09 05:14:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da892b68-ba06-321d-aba5-fe2b8041bb22 | -18.03811 | -57.51559 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 7eafd565-6da4-36a5-95f2-6c07e08bf6f2 | -17.99208 | -57.48741 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7d5dafa6-1e4e-39df-9c1e-e12395ecdcf7 | -18.0613 | -57.55313 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 2a0ca5ff-7223-3a97-92f6-df69d220d83f | -18.00896 | -57.49444 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| afd45d9f-cb33-3fa2-8233-5cff6241b03b | -17.93062 | -57.50851 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8b03fa73-f78c-3fec-b9d2-4dfde0cb9930 | -17.96382 | -57.50109 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 8dbbcf19-d486-3528-baa3-8fcaf92a5cf1 | -16.70575 | -47.61908 | 2025-10-09 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d272037b-8c2c-3bcd-a238-3849d902d86d | -18.05724 | -57.55655 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.1 |
| ec640936-2f31-3a03-8fb2-c9f57fed0260 | -21.99773 | -56.01876 | 2025-10-09 05:14:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c439fca9-0869-347a-9f95-c8e24169c8d0 | -17.38962 | -46.87693 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5709193a-eb3d-305b-ba0a-4057e3b3ced4 | -19.19067 | -46.4992 | 2025-10-09 05:14:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f057e162-1635-3052-b1a1-1f0badc038d8 | -17.89428 | -57.66327 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 40bb214a-1b2e-366d-b185-b25202877687 | -16.42311 | -47.82539 | 2025-10-09 05:14:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f59eec82-db15-3e4a-b25f-cc549fdcc71b | -16.28724 | -47.12906 | 2025-10-09 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65762a19-118f-3913-9c4f-a7755dd02fd9 | -18.01538 | -57.49957 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2e992997-b915-3cca-a250-44c3406948e3 | -18.06893 | -57.52491 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2744439b-d430-3989-9153-f31f261f337b | -17.2166 | -47.6548 | 2025-10-09 05:14:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| bb3cfb9a-7503-3598-9d3f-54bf1c472b48 | -17.92074 | -57.50268 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 0ee36608-731a-37a5-b088-fada30f547c7 | -16.01841 | -59.53106 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aec708c-6287-3a37-a980-3434435eec85 | -16.14474 | -57.56303 | 2025-10-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bcd28bc1-eb74-378c-9c15-197cd43b22b1 | -15.99163 | -50.98747 | 2025-10-09 05:14:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 61f0ebd4-d682-35ee-975f-c006e97e566a | -17.64083 | -47.20843 | 2025-10-09 05:14:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| eff8af81-e673-34a3-823f-40948bcf83f2 | -16.00298 | -59.54309 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 645ce015-2937-318c-853d-0c3a01bc29b5 | -16.28666 | -47.13509 | 2025-10-09 05:14:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e6b2906b-4330-3af4-b65e-909fb3ad775d | -17.26882 | -46.97228 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 914a9440-724e-31d3-967c-fa7e68d05411 | -17.91724 | -57.50219 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 6b7b1166-61a2-3c84-8d4d-f65c8a4196c5 | -17.7255 | -56.73582 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3d3e57c0-fa32-3518-8232-6085d307332f | -17.21294 | -47.65359 | 2025-10-09 05:14:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 16f9d212-5f61-3137-a00d-946c21377ea8 | -17.85119 | -57.60408 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d04080e3-18b5-370e-83cf-c72f40121d27 | -18.02528 | -57.55564 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |


[Clique aqui para ver as próximas entradas](README57.md)
