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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e35c2354-fde2-3b70-98fd-832f99eb4d5c | -18.62514 | -47.3336 | 2025-09-15 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| dc70108d-5249-393c-99bd-065c9e97163a | -19.872 | -42.49194 | 2025-09-15 03:32:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 6db6e574-a2da-3504-b6b2-3f6091951e81 | -17.14185 | -48.52681 | 2025-09-15 03:32:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 39e3bf68-ed3f-312f-bcaf-afaf3bf1f20c | -20.52731 | -47.48075 | 2025-09-15 03:32:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be90bf39-3352-3f0f-a143-db08a935a609 | -14.49482 | -47.35032 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 367d90d9-c2be-3f93-ab03-12bc39b2ef6a | -18.61579 | -43.9017 | 2025-09-15 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b535a01d-3ea7-3ff6-afea-73f17a0fa426 | -14.93804 | -46.54934 | 2025-09-15 03:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bb8d2c90-5059-3364-bbc6-3f4e8169d055 | -18.61736 | -43.90914 | 2025-09-15 03:32:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bba2d391-edd2-36b5-b94a-5955b72c8e86 | -18.59448 | -47.20814 | 2025-09-15 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2b918269-ef5a-3cc8-8928-a101f9e4789d | -18.58485 | -48.15787 | 2025-09-15 03:32:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ddd8de2-a9bc-3714-b806-6d3ee5f9c6d7 | -19.97358 | -44.11912 | 2025-09-15 03:32:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d6a645e0-574b-3052-bb51-fb4bac7274a9 | -14.50541 | -47.34225 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| db8d77e5-98ca-3e7a-9330-b3e3f0f470cb | -14.93679 | -46.55506 | 2025-09-15 03:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dec79fb1-fd6c-3871-98ea-07b833f318fa | -14.49579 | -47.3459 | 2025-09-15 03:32:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d885e2b-105f-38d7-abf0-e62e28440042 | -20.85813 | -46.21488 | 2025-09-15 03:32:00 | NOAA-20 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| efd63958-3c23-3d34-a57d-c26896b3f8d9 | -16.28477 | -45.6875 | 2025-09-15 03:32:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db8ce43d-eeae-3ed5-8b23-e9c403420411 | -16.28337 | -45.68266 | 2025-09-15 03:32:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad4db402-073f-3b70-b408-67d3949543de | -16.78613 | -49.09753 | 2025-09-15 03:32:00 | NOAA-20 | BELA VISTA DE GOIÁS | GOIÁS | Brasil | 5203302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| accb7608-63be-3c06-b485-a1237e88b999 | -14.93676 | -46.58607 | 2025-09-15 03:32:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 2683b6be-bb0f-3d01-b6cf-a962a09d3744 | -14.94299 | -46.55745 | 2025-09-15 03:32:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 7cfe420c-cbd1-37d5-839e-f62f183e8fb7 | -14.59608 | -46.60018 | 2025-09-15 03:32:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52514a26-0514-3174-b5c3-d405cb56a5c4 | -17.3397 | -42.65837 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14cb83d6-b585-39e9-805a-6763af6be74c | -18.71006 | -44.27898 | 2025-09-15 03:32:00 | NOAA-20 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 47807c3a-7686-3b6a-bc47-7d18d9256f93 | -17.34451 | -42.65946 | 2025-09-15 03:32:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 04db86cc-ab7e-3069-8e9f-ca9574f11212 | -23.24689 | -49.52045 | 2025-09-15 03:34:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d1f2e0ee-837b-3394-9c30-fe448bd2ab2f | -23.47241 | -47.37485 | 2025-09-15 03:34:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| f5b2e2ad-4c84-3d7d-ade3-672f56b526ea | -23.47912 | -47.372 | 2025-09-15 03:34:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 574215fa-f787-3667-8842-298c2410ee47 | -21.55301 | -45.88454 | 2025-09-15 03:34:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f34b3b0b-f225-39cd-9d15-4b79bc57f078 | -23.47808 | -47.37643 | 2025-09-15 03:34:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a49b7ab9-5c7b-3804-b6c1-b7d9c2ec64ec | -21.75608 | -45.50684 | 2025-09-15 03:34:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 038aa5f7-aa1b-3c0b-a79c-f4bfc9c143d2 | -21.92442 | -46.55981 | 2025-09-15 03:34:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9d21f5e1-ecbb-3c2f-ab7a-f883a82faf10 | -21.75687 | -45.50323 | 2025-09-15 03:34:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 95ab746e-ce52-39af-bebd-8f146de01528 | -22.2101 | -48.35736 | 2025-09-15 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a0938a4-7e8b-3b41-aa1d-8fd2793fcbe2 | -21.63017 | -46.81463 | 2025-09-15 03:34:00 | NOAA-20 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 6699b0ee-f583-33ae-ac8b-f6f167d84962 | -23.24744 | -49.51519 | 2025-09-15 03:34:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ba121fd1-f21b-30e2-ad0f-ee12fc16f4ca | -23.59532 | -47.39366 | 2025-09-15 03:34:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1ff19a46-3c6d-3dc7-ba18-6786b6b7b51e | -22.20645 | -48.35555 | 2025-09-15 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14b39dee-c9b3-3961-a8a0-522ef8f00f9b | -22.97088 | -46.25291 | 2025-09-15 03:34:00 | NOAA-20 | JOANÓPOLIS | SÃO PAULO | Brasil | 3525508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 70a6ee17-e224-3806-8cc9-5c8a955d87b3 | -22.21161 | -48.36143 | 2025-09-15 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bd246841-3c99-3159-92ef-d9e052bdf055 | -23.24825 | -49.5149 | 2025-09-15 03:34:00 | NOAA-20 | SARUTAIÁ | SÃO PAULO | Brasil | 3551207 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 6b64287b-eb77-3717-98cd-197113e6636b | -23.48016 | -47.36756 | 2025-09-15 03:34:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 48319769-4d26-3c0a-9363-4db9149edd04 | -23.14658 | -46.99816 | 2025-09-15 03:34:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 670b2a6c-a631-3a04-9ca6-c97b06bfc771 | -23.47345 | -47.37043 | 2025-09-15 03:34:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 16.0 |
| dbd99f0b-4c42-3ba2-88e1-053693a5edce | -24.83801 | -50.35753 | 2025-09-15 03:34:00 | NOAA-20 | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 3872e9d3-2eb2-3069-a540-c9db1e32099b | -21.76065 | -45.52632 | 2025-09-15 03:34:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| eee6ccea-2c38-387c-9244-2b930b5a8f92 | -21.75749 | -45.52601 | 2025-09-15 03:34:00 | NOAA-20 | MONSENHOR PAULO | MINAS GERAIS | Brasil | 3142601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f101e62c-3bb2-3e57-8259-6db049b0886f | -21.92349 | -46.56394 | 2025-09-15 03:34:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f9d52c77-0483-3478-88c5-d5c9a0a46795 | -23.59634 | -47.38925 | 2025-09-15 03:34:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a933af30-5136-3741-9775-674cb115d5e8 | -23.45582 | -50.80101 | 2025-09-15 03:34:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3dfc8611-18e0-3e4c-8bbb-c3bd16cead65 | -22.20538 | -48.36008 | 2025-09-15 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 080e555a-88ee-3cff-bdfb-8aec9b474cb1 | -23.00646 | -47.54958 | 2025-09-15 03:34:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 90c051ea-0c55-3315-a1f9-5fd048cd6dd6 | -23.47447 | -47.36607 | 2025-09-15 03:34:00 | NOAA-20 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| e58feb64-8cdb-3df2-9362-640a53650297 | -23.00539 | -47.55411 | 2025-09-15 03:34:00 | NOAA-20 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 724c68ed-4513-379c-8b85-74cb61656b02 | -22.19907 | -48.35904 | 2025-09-15 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 443d00b1-31d5-3c4a-b21f-bc323df6371e | -22.20384 | -48.35614 | 2025-09-15 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 321a3bfc-ef6d-3b0d-a0ee-60a452ab1f69 | -24.83954 | -50.35159 | 2025-09-15 03:34:00 | NOAA-20 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 298f1ef6-5812-39ef-bd18-234e48571161 | -22.20016 | -48.35447 | 2025-09-15 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 067c1715-c900-323f-af1d-dd16af048f14 | -23.78006 | -51.65444 | 2025-09-15 03:34:00 | NOAA-20 | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 27f35870-fd6e-3c99-bf05-a7e7871b2e1a | -21.55387 | -45.88064 | 2025-09-15 03:34:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1ab21fbf-d5b7-36a4-99b0-0b983d6ede7e | -22.71183 | -43.23948 | 2025-09-15 03:34:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 21c56f7a-4fca-3fcd-9304-12cf0aee34c3 | -21.75964 | -48.12613 | 2025-09-15 03:34:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8aadb03f-77a5-32cb-aca1-1f914960fdc8 | -22.19751 | -48.35521 | 2025-09-15 03:34:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56f24db7-a362-3eae-8e5d-c5a89ffa0385 | -21.92533 | -46.55577 | 2025-09-15 03:34:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 83c551a8-336b-3145-813b-3894c2bf12fc | -21.09757 | -47.99532 | 2025-09-15 03:34:00 | NOAA-20 | SERTÃOZINHO | SÃO PAULO | Brasil | 3551702 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16f78d87-79c8-3b7b-bf54-d1b5223c2e0b | -22.1964 | -48.35977 | 2025-09-15 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31c469bb-76e7-37f6-be52-969340edf662 | -22.20274 | -48.36068 | 2025-09-15 03:34:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ed46e1d-d9a0-301a-9bf9-d810fe9d0d1e | -21.54847 | -45.87923 | 2025-09-15 03:34:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7d2994a7-e51e-3e1b-acbe-e17e7df04883 | -23.45398 | -50.80801 | 2025-09-15 03:34:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| bb20c3b2-e38a-3aec-9c50-e430bfb015fc | -23.14156 | -49.6395 | 2025-09-15 03:34:00 | NOAA-20 | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1dd0cab1-9a11-3597-b5bd-70cc909fb573 | -12.7879 | -47.9318 | 2025-09-15 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 66af3b72-69e4-3a9e-9906-5d703c6beb39 | -14.8028 | -51.6175 | 2025-09-15 03:40:00 | GOES-19 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 445e16f6-8031-309e-a8e9-f86fac51a53a | -12.9791 | -47.9713 | 2025-09-15 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 693c254d-1152-3793-9beb-05bdb7de42fd | -23.4754 | -47.37 | 2025-09-15 03:40:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.7 |
| a4458f3b-9309-378c-889b-6e8a48987da5 | -12.7875 | -47.9541 | 2025-09-15 03:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 67683d73-6fd5-3ac1-a67c-30ed1bcab941 | -12.7875 | -47.9541 | 2025-09-15 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 17838c11-773c-3e0e-a520-2f94447a9bd7 | -12.9791 | -47.9713 | 2025-09-15 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.1 |
| fb4c3b82-7df5-31aa-ac3a-b33c8cb3b583 | -12.7879 | -47.9318 | 2025-09-15 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 48d2cb26-04c8-3b9a-a4ed-ff4edd54a4ed | -12.9984 | -47.9685 | 2025-09-15 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| e6a0f123-358b-38d3-bc04-668965140ffd | -23.4754 | -47.37 | 2025-09-15 04:00:00 | GOES-19 | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.8 |
| 7ae4c375-8658-3ff0-8537-f45e44f080ed | -5.40156 | -45.93124 | 2025-09-15 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b563c6c-a84a-37aa-9073-32c27cc531d9 | -8.18884 | -46.76548 | 2025-09-15 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e870bdcd-4945-34f4-ac9d-c9608bb6d4ec | -8.92159 | -45.47169 | 2025-09-15 04:19:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c2cefe18-b83c-30de-af30-eef6ca04652e | -7.67663 | -44.48806 | 2025-09-15 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d3027d2-8b36-35d6-99dc-cae137bf0eb7 | -6.91343 | -46.16379 | 2025-09-15 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87919115-ff47-33c6-aacf-f99d79712c2f | -9.00365 | -47.05379 | 2025-09-15 04:19:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8c12bcd0-1da9-3bbc-b247-ce1d02a9b231 | -7.37077 | -44.35438 | 2025-09-15 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 932f986b-869f-3762-9566-f7f672bbc8d6 | -7.15212 | -37.32814 | 2025-09-15 04:19:00 | NOAA-21 | SÃO JOSÉ DO BONFIM | PARAÍBA | Brasil | 2514602 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 693c40ab-67d2-30d9-9e03-37f8cc62b70d | -7.9795 | -45.66169 | 2025-09-15 04:19:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d3b91fd3-b10f-3b6c-a526-4eca53242032 | -8.89475 | -46.20293 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1fc7eb8-ca65-3dc1-b5c2-deabd69e60ba | -5.77866 | -43.74164 | 2025-09-15 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8437335c-c423-36cc-a632-19a828b0ccb1 | -7.88118 | -43.57265 | 2025-09-15 04:19:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| d8e7e12b-a366-352f-99aa-1d7353bfdb6a | -3.65214 | -54.06102 | 2025-09-15 04:19:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8f4c8534-3c3b-3174-8cae-d8e20f73e297 | -8.18547 | -46.76494 | 2025-09-15 04:19:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76ad9b85-e79d-308f-b302-dc65cb56ad7b | -6.03458 | -43.11754 | 2025-09-15 04:19:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e6f3def5-0f54-322d-be9d-01087d636d21 | -6.99898 | -44.55907 | 2025-09-15 04:19:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 407216d8-48d6-3938-b3e6-c11922f5cd9b | -4.17609 | -48.57042 | 2025-09-15 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| d5cfee08-3020-34e5-8544-85871c17fcbe | -8.897 | -46.16735 | 2025-09-15 04:19:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b28f11a-d613-3874-8299-954d06b4582f | -5.69581 | -49.20158 | 2025-09-15 04:19:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ea8ccb4-c0cd-3ebd-b9f1-14a3599c30df | -3.22548 | -47.63046 | 2025-09-15 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54af42a2-aa82-3e7d-8957-a389b3f2ce3a | -7.05368 | -44.14025 | 2025-09-15 04:19:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README16.md)
