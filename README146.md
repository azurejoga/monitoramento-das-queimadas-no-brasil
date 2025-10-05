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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4bce5955-5b00-3fed-afcd-a983eced6470 | -17.93027 | -57.60499 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8543e2ab-cf32-3dbc-822f-98560b93ac99 | -17.94756 | -57.58858 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 99cef394-475e-305f-a5e6-29388fcee833 | -17.85973 | -57.60497 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| e22a2bc7-885e-3d78-8aba-042e8fcb8303 | -17.96104 | -57.56085 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a2ac2810-f134-3690-885c-5b847b5b4719 | -17.85094 | -57.63638 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f3f83fa5-e630-3a41-8b70-71ec78b4e454 | -17.95134 | -57.60044 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| c94c2924-5d1c-333c-b1af-54eb35537bf2 | -17.86587 | -57.63062 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 043df7c9-a450-3ccc-b5e0-1d45e83e8194 | -17.94081 | -57.60263 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| da5a22b2-f7ff-3ddd-aa95-3f4589f53a4a | -17.96014 | -57.56869 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 97816f04-4925-32fc-8023-19a3a3eeb780 | -15.56818 | -52.47701 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 423a8f0e-4346-3273-8035-0453743152c8 | -17.96325 | -57.58638 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7a5ecfe5-264e-3574-86e4-92bda9103691 | -15.31113 | -56.93682 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95c2ee25-acae-39cf-a65f-dc38bd8e7f06 | -15.57963 | -52.45167 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ff216870-3554-3afe-bce2-1c13fc1a78ab | -15.5817 | -52.50097 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13fee5b2-37a6-32ce-9948-ea1e7189f1aa | -15.22925 | -56.85764 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 884d74cd-1dec-31eb-bc3e-0f8ef53f26f3 | -17.95642 | -57.60097 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 006eb7de-7893-3f06-af3a-b807ac4d87a0 | -17.9245 | -57.61056 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 48985542-aff7-31bc-89eb-8d51b0d14501 | -17.94048 | -57.60556 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e77ef1e3-f6ee-3c7a-ae64-7e9b48a8f0a6 | -17.84578 | -57.63676 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 902c100a-edc0-3fc8-8132-3479b6858707 | -17.95716 | -57.54978 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| da3900eb-71ae-374c-96c3-5e4465fc03e6 | -15.91432 | -59.51271 | 2025-10-05 05:38:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38af41bb-356a-3bc7-aa28-0e6311bdf356 | -17.96868 | -57.58392 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7875a289-ecf3-34e2-a37f-c70e55ed9f70 | -17.89513 | -57.64376 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 92c7e608-dadf-36a0-af63-4e23fee2377e | -15.58836 | -52.50291 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1b53167f-f2d4-3f5f-8e1e-fc3dd8b852b7 | -15.2193 | -56.8536 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0a78dc8-2518-3c23-a216-f05a92c48013 | -17.94556 | -57.60603 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| bd7a5b9c-4d1b-3341-9303-325c0f9d3ede | -15.24435 | -56.86211 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26932f5b-9639-35b7-aa31-277086507882 | -17.95878 | -57.58047 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2fd31321-d4aa-3d3a-9353-c6ef6fbc61e6 | -15.23892 | -56.77573 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 280dcd10-a1b9-31a2-b0c1-55fc352e5181 | -17.88503 | -57.64257 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 8ba7e5b5-3105-31e4-847e-5e824bb6543e | -16.11995 | -53.97802 | 2025-10-05 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fe41189e-9730-377d-bfc5-88e3f0d19bcb | -17.95607 | -57.604 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| f36d35fb-7064-3006-9294-deedc8d33c24 | -17.86673 | -57.63275 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 97ab1335-ffe6-3d9b-a764-76fa4f240a54 | -17.95746 | -57.59198 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9ea7f81a-60f3-3b1b-b8ca-3d14ae5fc092 | -15.2344 | -56.85815 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cfd343d3-3916-365d-b7f5-853b9b3cc81b | -14.85842 | -60.07031 | 2025-10-05 05:38:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e58eb5e8-d4ed-31ac-8d6d-ea8fd8afe0b0 | -17.95169 | -57.59742 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 8c7ed104-7c54-307a-8824-6ed5293d371b | -15.22584 | -56.79793 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33e474b1-bacc-38d3-be5d-99f6fa8b63e4 | -15.23955 | -56.85868 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f7913a95-e7b9-3213-9b80-6bb5b6ea2689 | -17.96045 | -57.56603 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| aeb5fda4-423b-35fa-a501-f38080a0e8ba | -17.9616 | -57.556 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1c79c8f0-b83e-3845-a12a-9beb1fdbb90b | -15.19563 | -56.833 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8c4c6ee-b6c6-38c6-99a2-8c7559879bc9 | -15.57908 | -52.45731 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2399ffcb-3734-307b-a455-b471419d3789 | -17.88976 | -57.64603 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dbac87e7-ba1e-3388-ba57-2c39cd6d4066 | -16.1277 | -53.98526 | 2025-10-05 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2151494e-e827-3ed6-a5f9-da40919f37db | -17.89546 | -57.64085 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 22ba8f0f-e03a-3c91-a92f-4b0a76619eec | -17.33274 | -54.19999 | 2025-10-05 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3e6e0e7-0408-38bf-acc6-35f71234dc1b | -18.17455 | -53.3662 | 2025-10-05 05:38:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 822340e2-f437-312e-89cb-f2c8cb626fce | -17.95269 | -57.58869 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d010285b-9b74-34c3-a68d-f3e0f769afaf | -17.87513 | -57.59293 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| dbb9cee0-6561-38f0-8ff9-8b2def278305 | -15.57125 | -52.46725 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f09ab672-2378-329d-9224-c9dceba2f2de | -18.16828 | -53.36168 | 2025-10-05 05:38:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 700f5f8a-a067-3ae4-b7c0-472e8fa99e45 | -15.22006 | -56.80259 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7fead62b-2612-37df-b18b-0ea1e80ec610 | -17.85551 | -57.63168 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| cc1aee06-cec9-3b29-9034-3f4a57b5c470 | -15.23941 | -56.7716 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47eb1391-7c51-37a7-9a64-3ffe5de3f578 | -17.87092 | -57.63129 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9ec220d0-7e79-389e-a5e1-c1b9b2591739 | -18.17311 | -53.3602 | 2025-10-05 05:38:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8f327060-c8a9-37f1-982e-9e0e6de8ea27 | -17.86515 | -57.6025 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 03b97a86-7f55-374a-895f-0695d244ff87 | -17.9619 | -57.55338 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f28e62da-b0c6-397e-a2d1-881c96a15564 | -17.93538 | -57.60521 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d97f44fa-349c-3701-bd6b-ce8ee43a1363 | -15.24469 | -56.85926 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df1bbd03-04c1-3005-98c3-c67e057050fd | -17.96394 | -57.58038 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9740a943-f58a-36ba-9207-fd2b29a285c6 | -16.38108 | -52.1685 | 2025-10-05 05:38:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 18ed152e-db2a-3dc7-8185-93be54650d61 | -17.33222 | -54.20523 | 2025-10-05 05:38:00 | NOAA-20 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3af6e844-528c-368c-a77d-ccbf435bfa31 | -15.31082 | -56.93939 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0c530ea-b3e9-3ac8-9d70-9c5bad512e6e | -18.24887 | -53.33621 | 2025-10-05 05:38:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 735a9217-064c-34af-a10a-9e9401dedbf0 | -17.8416 | -57.62859 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4f8650b2-654d-3357-b586-cd11799c319d | -15.2392 | -56.8616 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8e1122d0-5944-3dd1-9e12-6aba34184c2d | -17.95614 | -57.5586 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 543367ee-d010-3c54-b52e-c14c6bee69eb | -17.96075 | -57.56337 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4eecd059-0e14-3213-89bc-6459cdc2155c | -16.15047 | -57.58125 | 2025-10-05 05:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 3403e0df-90ef-34d4-a09a-d71826226d74 | -17.95814 | -57.5861 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 490a2bcf-b277-3a76-b772-7f82b8ca6f8e | -16.38173 | -52.16171 | 2025-10-05 05:38:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 79d7786f-d600-3827-ae93-95e475864e41 | -16.1494 | -57.58143 | 2025-10-05 05:38:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 6ee1fcd3-ae49-3312-b63e-ea4266fd7bcf | -17.95677 | -57.59797 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| ad12d23e-2a98-37f7-98bd-f5f585323d9a | -17.93504 | -57.60817 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5a710896-3b40-3ded-9c9d-abee1aa13fd7 | -17.8847 | -57.64546 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 79894027-b30d-3ecc-a2e8-3c8f9099a7d4 | -15.20973 | -56.84626 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 307b4469-19cf-31ef-aa3c-77d5ae5a33e7 | -15.60239 | -52.49966 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47403334-f07f-3fc1-83ef-9128e5b8a38e | -17.91773 | -57.62508 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 5b6fb531-3346-3943-b253-5ec0cad6a4cd | -17.90051 | -57.64143 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 22245998-dd10-3cab-8399-4508470c4231 | -16.12147 | -53.98447 | 2025-10-05 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 295ab555-9261-395c-b078-81b768b1693d | -16.12668 | -53.97387 | 2025-10-05 05:38:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f78181b2-14f7-3c77-8b3d-8b3f21dd78f3 | -15.19594 | -56.83031 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e34e6675-3184-3b76-9dc9-1d76ce37b02e | -17.9126 | -57.62508 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| b90d5470-0d49-3c5c-8949-86154adbcb3e | -17.84616 | -57.63349 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ad67a04d-1843-398c-87ce-49ecd0dbd5d3 | -15.57068 | -52.47314 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad0314b7-3c15-39c4-bf6a-073bfbfd8dfc | -17.93057 | -57.60234 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| b9b738e3-6b72-37cc-80e3-bfbbbcd46e6d | -15.21374 | -56.81195 | 2025-10-05 05:38:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f78382a5-81df-3d3f-a673-e993d77fd0b8 | -15.31653 | -56.93502 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63eab39d-3047-3bc4-8b87-f3303e2b699e | -17.94013 | -57.60862 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e6d854a1-abd2-3b39-8220-e85499ab23c3 | -17.88084 | -57.63417 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 018e0f1b-a4df-3ede-b6ba-b96280095cc6 | -17.95236 | -57.59158 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3bfb331a-0ac5-33fc-af3b-c3f889b10149 | -17.88056 | -57.63665 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| a2f0ec46-4d91-361e-8429-e3aa164d6a10 | -15.60072 | -52.51653 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b6a9568e-92b1-3b7f-91ff-080b376585cb | -15.59393 | -52.51598 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7c26532a-da93-3277-8966-d4c5c0523c85 | -17.94724 | -57.59136 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 99875b62-e8ff-31a4-9d89-25aca1de5339 | -17.89008 | -57.64311 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 1be3bcdc-8f4e-3a3c-a156-1776909ec0a0 | -17.88669 | -57.58131 | 2025-10-05 05:38:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f6a0666f-00c0-3159-8083-30bdcee04661 | -15.60125 | -52.51123 | 2025-10-05 05:38:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README147.md)
