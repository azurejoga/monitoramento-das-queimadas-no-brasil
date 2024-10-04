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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23a134c0-bf5c-374b-b6d7-559ad1fcc9c8 | -16.56868 | -57.29508 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| a6df4057-1c1a-3c96-bf96-d79db323eb6d | -16.56809 | -57.29871 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| ffc0e34b-1bd6-3fbe-b4ac-375534361519 | -16.56763 | -57.22126 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fc579ba2-8873-3dcc-bd94-0e3487048e72 | -16.56594 | -57.29087 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 80b08019-f9e4-3a43-9fd9-1d54d48c2bb9 | -16.56535 | -57.2945 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 49afc811-1f03-3ac0-b30d-57f4e959effd | -16.56473 | -57.23939 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 4c4fa019-c613-32cb-ad9f-22e9d9b39b51 | -16.56414 | -57.24302 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 330a7e3d-b00e-3699-9648-f818ed3ab2b3 | -16.56382 | -57.28774 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 152ee507-4541-3b9b-86ba-0c2293f23e5a | -16.56356 | -57.24665 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 22c0f291-0e04-3029-a1f3-68cc804f0812 | -16.56324 | -57.29136 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 19e893f8-cfe5-37ab-935a-94b1825a4c8a | -16.5614 | -57.23881 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 93014ebc-81c4-3249-bc7a-d2463121d806 | -16.56082 | -57.24244 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 2d94a471-4c2c-3622-8cc5-caf4442cb565 | -16.56049 | -57.28716 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8943ae1a-7270-3f0a-a6e1-42e71fccda8b | -16.55991 | -57.29079 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b54f6f70-cd82-36f1-8be6-c8deaa5acafd | -16.55716 | -57.28658 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 2145b8af-bee3-3c6b-a5b0-0689c52afb00 | -16.55216 | -57.39696 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 3345509d-e49d-3bd9-8162-d45d10258a5d | -16.55157 | -57.40061 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| bfd3b2a0-3518-37d1-a1e0-25aa2de5b21c | -16.49432 | -57.29434 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 68f3adcf-067c-314b-b5ee-6da37618b11c | -16.491 | -57.29376 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 8b5afb7a-b734-388c-a4d9-f78ea2e3d944 | -16.48767 | -57.29318 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.2 |
| 3d3af0e4-43f1-3555-90ac-01925fd1b39e | -16.48042 | -57.29566 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 1451346c-835d-3a20-898a-511429fa8422 | -16.47376 | -57.29451 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9902c07b-8c96-308b-8f8c-9d85836ac623 | -16.47317 | -57.29814 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c37a834f-49f5-33fd-bf2c-1fd10638a45d | -16.47043 | -57.29393 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c8b05317-f4bf-3a4d-adc9-61d0bff45618 | -16.46984 | -57.29757 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7ce21017-30a3-36fc-909f-a40951e17572 | -16.4671 | -57.29335 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| afe0599f-d34e-3e18-ab1b-3f3c0bc1845a | -16.45927 | -57.29947 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| dcc9138b-f436-3c8d-9cad-6b05465696ed | -16.4575 | -57.31037 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 11afbf05-9ec6-364f-9dca-f28cb56e0029 | -16.45653 | -57.29526 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| aea228d2-bf72-3fb8-8db2-aa2b4e3a538e | -16.45594 | -57.29889 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ef148ca0-d09a-3d8c-be3e-4e39e48466ee | -16.45535 | -57.30253 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 72542343-4dcb-3071-b0b0-a5dceb45f04a | -16.45476 | -57.30616 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d7a43943-d3de-34a7-bdbf-908404db4ac8 | -16.45358 | -57.31342 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 51eb0b44-6f13-3af9-a7f2-8481031df94e | -16.45211 | -57.30569 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5f23a2b1-b1e9-3d1d-8791-3f0da3f4616c | -16.45153 | -57.30932 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 6560711b-eff6-317a-9213-742a42ff1a66 | -16.45111 | -57.29057 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 48211fc9-3c70-3400-ac1c-cc4a48c00a8b | -16.45095 | -57.31296 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9794a158-e308-3957-8df8-3607e72d39d6 | -16.45053 | -57.2942 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2f31bd5f-5c78-340b-8aae-f5f66402e882 | -16.44995 | -57.29784 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 2ec1cfae-378a-385d-a069-63ec66463b50 | -16.44662 | -57.29726 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 73b412ee-8980-328e-85c1-c81780d60a46 | -16.432 | -57.38828 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c97f8a6b-5daa-32fd-8955-3d192047a5ab | -16.43141 | -57.39193 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 918593ae-35c1-3114-bb08-21f16bf890cf | -16.42925 | -57.38405 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 62b946b6-c006-3c68-a6f2-78b4243afa0a | -16.42808 | -57.39135 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 40764c2d-001f-3c56-bd4c-ba41fd81dc01 | -16.42631 | -57.4023 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 466e5438-d0a6-3d03-bf44-fe2334120127 | -16.42591 | -57.38347 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 01cad2b8-06ea-3c8a-8896-4d2cc1ef58ba | -16.41964 | -57.40113 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e74c157d-b971-3260-8e72-04013a2cc63b | -16.41631 | -57.40055 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 88f3e964-db8d-3548-9802-ba130452749d | -16.41572 | -57.40419 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 518319fd-32f3-3e50-95ec-8bcf76e21937 | -16.41473 | -57.38903 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 31d0718c-f740-3ebb-b917-4b07f179a342 | -16.41356 | -57.39631 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 38e9e69f-bf31-30b8-8d5a-a8bd892f5238 | -16.41022 | -57.39573 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a8bb0330-543e-3431-9273-b3370e1f91f6 | -16.40806 | -57.38786 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 92f54340-4230-3162-bb32-b6b82c681e17 | -16.40473 | -57.38728 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4298075a-27af-32e7-9202-d57ec6989ad9 | -16.40355 | -57.39458 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 09199fac-3668-312b-9f0c-b5f905c84921 | -16.40081 | -57.39035 | 2024-10-04 04:57:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e08da2f8-10d5-31c4-a769-c82a56ae101b | -16.65087 | -57.14539 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c6ee974d-5e0e-3362-a642-c39dcf9f4c50 | -16.64971 | -57.15263 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9df6f13f-3060-3730-8647-37cb1e3cca23 | -16.62845 | -57.17871 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 06108210-599d-3366-88be-d2cb74c7e01e | -16.62787 | -57.18233 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1bc5b42e-212d-328c-88de-2c22b701c94e | -16.62513 | -57.17814 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0700ec83-a56c-3b8e-be69-ad384c4798fd | -16.6189 | -57.19567 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3cbb9c24-e75f-3782-8418-34e57409218d | -16.61558 | -57.1951 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 03aa80cb-be17-3f7a-8ddd-3f6ec9809d0f | -16.61499 | -57.19872 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d5a88c61-ffb5-3cd3-bfb3-e339dbe80b60 | -16.61358 | -57.16499 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 76509ea2-7dd4-3ee8-b0b9-4ed1ce3e4fd3 | -16.613 | -57.16861 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| b72a70f0-2a18-3215-897a-d8bb001aeebc | -16.61225 | -57.19452 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 3e7d471d-2c8f-35d0-9a58-c467812486f6 | -16.61167 | -57.19814 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 7eae8486-c2f6-3e46-a268-2cf0b64f9572 | -16.61067 | -57.18309 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f86003c7-efd9-3b5e-982b-b3cfede1d61a | -16.61009 | -57.18671 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 01e3a6bf-5ec4-37ad-a78a-fb5664603cfd | -16.60951 | -57.19033 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| edd0fdfe-4fd3-3648-b0c7-7b2ec0d9fdf3 | -16.60893 | -57.19394 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 7fccf159-08c5-3c0b-b6ec-ed443a869f02 | -16.60835 | -57.19757 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| f0196be7-fbfa-3a6c-945f-c9b3e98281b3 | -16.60776 | -57.20119 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 9b757918-a3d8-38de-baa2-d41061eec14d | -16.60735 | -57.18251 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 3510f5cb-828a-34b7-9a7a-7ee5d0474839 | -16.60677 | -57.18613 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.8 |
| 903b01f6-ee64-382d-87af-4cfd3ac36627 | -16.60619 | -57.18975 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 2651a6fe-19aa-3d09-82fb-6f98b4f62e5c | -16.6056 | -57.19337 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 1add0504-1044-3cca-b055-4dc9eee09154 | -16.60502 | -57.19699 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 28a01242-8a95-38e6-9417-178af2ff7ef4 | -16.60444 | -57.20061 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 190782c4-1abe-38a1-af72-d66cfff0024a | -16.60403 | -57.18194 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.8 |
| c8bb7ed1-7c88-3f80-886e-7589f506217f | -16.60345 | -57.18555 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.8 |
| af1243c8-d889-328d-a77a-41285a675a74 | -16.60286 | -57.18917 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 242e1648-4f09-3881-9a98-26d3fb51ce9f | -16.60245 | -57.1705 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fd88c0ee-e606-315d-b59c-8cce82387ae8 | -16.60228 | -57.1928 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 71b42602-3712-3435-b668-b7dd9b92431d | -16.60187 | -57.17412 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7f6dd238-5983-3773-999e-b69a107b98f5 | -16.6017 | -57.19642 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.7 |
| cefd0eb5-4a1a-386a-b47e-b2af55c55d5d | -16.60129 | -57.17774 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ffd0a5cc-18e2-3b51-b912-a0609a62d979 | -16.6007 | -57.18136 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| f6e842e2-ef76-3115-94d5-704a24b19d28 | -16.60012 | -57.18498 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 3cc24fb8-003f-3c6c-b4d4-2d93127aee58 | -16.59971 | -57.16631 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d5e96fbe-628c-3295-a47b-5b890cb01e95 | -16.59954 | -57.1886 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| ce1eb2e5-b59f-382e-afe8-1012331d304b | -16.59913 | -57.16993 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c19ef022-efbd-321a-8891-b0c5d07dddd3 | -16.59896 | -57.19222 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 74cff29e-9d1a-3400-9263-0696fb126851 | -16.59855 | -57.17355 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6fd8332a-6afa-3e2e-8382-9c2f72319ffb | -16.59796 | -57.17717 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f444f7c0-f36f-3732-96a0-179f4a617b95 | -16.59738 | -57.18079 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| e15be327-6d5f-3535-8c68-61cc77d62fd5 | -16.5968 | -57.18441 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 42.8 |
| 41dca310-6997-3f5a-909a-1432fc921f4d | -16.59621 | -57.18803 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 744fc12f-de36-329a-9e31-18f01669ba57 | -16.59581 | -57.16935 | 2024-10-04 04:57:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |


[Clique aqui para ver as próximas entradas](README164.md)
