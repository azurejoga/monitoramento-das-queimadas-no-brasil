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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b03222b3-f959-305a-8fea-8227a42cff10 | -17.16439 | -56.13195 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7d5953ee-151d-36a9-8b1b-645e6d7c305c | -17.16162 | -56.12777 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3f0d857c-d426-3e8d-8407-ee83a92e4193 | -17.15884 | -56.12358 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7130e053-7f2e-33b7-81ac-ac2df59a2bea | -17.15716 | -56.13446 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| d7b87020-129e-37e1-9f85-28f251e2cba7 | -17.1566 | -56.13809 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a1e5dfc2-6eee-3c41-9535-d2442d97b1a4 | -17.04575 | -56.05351 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| eca14671-5fab-3f85-90f9-2ebe0bfe2a1e | -18.7113 | -57.28438 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7ddf9189-46cc-335e-b121-4016418ed755 | -17.04519 | -56.05714 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 739cfd96-9142-3a51-8e25-d10c86007bf1 | -17.043 | -56.08616 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4c92e271-49e7-3ee3-b551-012f8beef096 | -17.04067 | -56.08615 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 602ed245-3e56-37a7-b077-a3b294c401a3 | -16.82953 | -55.85384 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 72e35fd7-9e91-3025-ba42-e9dcc21d501f | -16.82897 | -55.85748 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fa2b5ea8-99f9-3cf0-8083-addb59cdecf2 | -16.82676 | -55.84966 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 80b6d840-eda9-33b1-9649-48bbab1f56df | -16.82563 | -55.85692 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 585f78ce-54ec-3914-83da-05c3d4092b27 | -16.70631 | -55.95302 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 8722b1ea-eb36-3288-a079-efa3bdaae6e4 | -16.69908 | -55.95553 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b95e8eab-022f-3448-b775-796a6a9449e7 | -16.68405 | -55.96417 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 55f16db2-f410-3d20-adab-b029c5908195 | -16.6708 | -55.89507 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| affae3b8-5b57-34fd-b26e-fcbc1f635de1 | -16.6335 | -55.90042 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 5f5088ff-722c-361e-b8bb-b437300a94fe | -16.63017 | -55.89987 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e34b1261-01e0-33b4-b205-9a07923c484e | -16.62904 | -55.90712 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| b58a5d19-2970-3665-8fd9-75e14f97ee75 | -16.62627 | -55.90294 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 68038305-da12-3db5-b084-d3763e7a77c5 | -16.93296 | -56.62083 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 30f0356b-951f-3a5f-bb2e-ca80445541a5 | -16.93239 | -56.62445 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6eb1e635-b9d8-3b09-9c21-75b321010310 | -16.70687 | -55.9494 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 04042de3-8588-303e-be4c-4f46ea201926 | -16.70297 | -55.95246 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a948cdf3-7fa6-32a5-b9b5-52f67161d299 | -16.70012 | -55.99286 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| e2d89133-90bb-3bca-a3f0-4b3a4d79c01a | -16.69518 | -55.9586 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0703925d-795c-3627-8d80-350bb8ba6f2f | -16.69128 | -55.96166 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 611f458c-0916-3757-8c75-4ab73c42b350 | -16.68795 | -55.96111 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ad3c8d19-119e-325e-803a-432859c133c4 | -16.68739 | -55.96473 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5e37ed23-2001-3650-98c7-20970d95ce3f | -16.63294 | -55.90405 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1653b6ee-549f-3913-8812-5ef98e8fb0f1 | -16.63073 | -55.89624 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 62c1c742-fe4b-3346-81f2-3766994b5ec1 | -16.62961 | -55.90349 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| dcd24331-9c7b-3c57-bdeb-e53cdc7ee0c4 | -18.71071 | -57.28803 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 31f76bcb-82be-34e1-ba65-bd7e983c8870 | -16.6274 | -55.89569 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 1ea690b6-9605-363b-9448-a2a99f716bb0 | -16.62683 | -55.89931 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 63beaf96-dccd-3424-8871-b860cf452aed | -17.01179 | -56.67848 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2295c0ad-e718-3c5f-9829-066e34f0a886 | -16.62406 | -55.89513 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8b8a1d63-5029-350e-ac31-c000ebe5e26d | -17.03566 | -56.67884 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d6356ce2-03f8-3da2-a783-a3e173b6eee8 | -17.01512 | -56.67904 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ebddbbfb-dd6b-35c4-8532-a20739e4764e | -17.01408 | -56.66402 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e01b6142-0195-3c35-8adb-7c6e0012c2fb | -17.01236 | -56.67487 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2ccff18a-8b6f-3bce-8d70-08e1ef5e06a4 | -17.00846 | -56.67791 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| b47c6bda-7588-36c6-b6f2-f20bf6165bac | -17.00789 | -56.68152 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c3a2a6b0-0dcf-33bd-a732-266e8c06e954 | -17.00732 | -56.68513 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 75269e36-b6ff-3fff-a7cc-97d65479dcc2 | -17.00456 | -56.68095 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0ca5ab41-6442-3416-99c1-638679048a6a | -17.00285 | -56.69179 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 773528e0-7f67-3fc9-b32f-5801952c09ff | -17.00238 | -56.67316 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 87e9d5a3-8eaa-3b3c-8212-e37d42230314 | -17.00181 | -56.67677 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1eec8cbd-a23c-3725-b710-9de4a5e7371e | -17.00124 | -56.68038 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| c8de4ded-9a37-3cae-b7fd-0c9eed852905 | -17.00066 | -56.68399 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 0ddb3252-da95-38bb-87c8-2f1d1db3395a | -17.00009 | -56.68761 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 812e61eb-eae0-3717-85ff-5e3d57adbdc7 | -16.99734 | -56.68343 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| e1ea3250-9844-3c14-8e54-b1f6515e99a2 | -16.99676 | -56.68704 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 38dc6ccb-0408-329f-9c62-7425fe24309e | -16.99286 | -56.69009 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| b291e5b6-0d8d-378b-a556-d9d383069f37 | -16.99268 | -56.60473 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| d180ada7-80bf-3c8d-8cb3-fa53685ac91b | -16.98822 | -56.61139 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.5 |
| 694c7848-657e-35c5-9675-6ef93339797e | -16.98432 | -56.61443 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 859d2f38-14a1-35ae-92a4-507e9f90b6e3 | -16.98375 | -56.61804 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.6 |
| 3df09a73-f5a0-3a40-b16d-45ca12435a77 | -17.16772 | -56.13251 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2939a44e-1c87-378e-81ac-0809ec1acbc2 | -17.16495 | -56.12833 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0470eacb-7233-35c8-b869-16ef4dd84834 | -17.16382 | -56.13558 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cc2fc107-2406-3a80-a430-0ac152465f5f | -18.70888 | -57.23512 | 2024-10-08 04:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4fe499a0-9756-315a-8ec8-7667cf8c4684 | -17.16218 | -56.12413 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 752a0e2c-8766-3257-9417-6c74741e88da | -17.16105 | -56.13139 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 22b4ab0a-38be-3f6a-9528-5ad2804403a5 | -17.16049 | -56.13502 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 991a160b-913f-372c-8dd9-68520a80da2a | -17.15993 | -56.13865 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e875f4fb-003b-3561-8fe7-6643729dc528 | -17.15828 | -56.1272 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 1ea7f7c6-97d8-3e9d-b571-1c6088f1a40c | -17.15772 | -56.13083 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3264d6f1-8980-388a-ac26-6b6f66b768da | -17.15438 | -56.13027 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 1edd5a9d-eff6-36b5-b998-935a31210849 | -17.15382 | -56.1339 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a81b78dd-7750-347e-b2b5-f2f4e1b09e2c | -17.15326 | -56.13753 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ed355109-ba4a-3dbb-a52b-900837f8252c | -17.1527 | -56.14116 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8b5def52-1b4a-38e7-b940-eb50201061b3 | -17.15158 | -56.14841 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 914c93c9-8c20-3d9e-963d-0f70ed84cdf0 | -17.14491 | -56.14729 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7505cead-f28d-396c-aca9-0c02ad470e7b | -17.14435 | -56.15092 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| bf31f182-4f2c-3e49-a322-d38b4084e966 | -17.06222 | -56.67537 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| bea1263d-3b01-3924-8c11-1eff961be68c | -17.05082 | -56.05778 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 59b23c59-60a5-35fa-808c-82843cca3a9b | -17.04805 | -56.05359 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 97a88163-e877-3879-9496-224a0aec8171 | -17.04749 | -56.05722 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| a7f03882-51c8-3924-9b00-c1dca5916a84 | -17.04242 | -56.05295 | 2024-10-08 04:59:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c367f3b3-be10-330c-92b5-c8437a9099ed | -17.03899 | -56.67941 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| ad656673-5b00-3b12-93c2-f192453643c4 | -17.0368 | -56.67162 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 37364afa-d643-34af-82cc-8cfd3d8a4ce8 | -17.02796 | -56.66269 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 98520e75-e7f5-3e5d-8c87-26e80b9fb091 | -17.02463 | -56.66212 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7eff074b-5abb-3a4c-9da2-a822a1669498 | -17.01969 | -56.65014 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 78d234a9-3f77-3494-916e-3c6c69ca07e2 | -17.01855 | -56.65736 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2909c00d-4838-329f-a888-e56fd51100e0 | -17.01683 | -56.66821 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7f9bb256-2e48-3356-9bab-0241025da2bd | -17.01579 | -56.65319 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 33944886-80aa-3bf3-87c1-e29ce96f725e | -17.01569 | -56.67543 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 24ab98f2-efc0-3a34-8b22-937c4df61407 | -17.01351 | -56.66764 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| a8462cdc-5356-3739-830d-3aa7b5163a3f | -17.01293 | -56.67125 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 70dd7ede-ca15-33ce-8e9f-8c5296e6bbbd | -17.00961 | -56.67068 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| afd00691-a130-305d-976c-4556e3215989 | -17.00903 | -56.67429 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 72616231-a4f7-30cd-97c8-a039d6a82725 | -17.00571 | -56.67373 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6e186ba5-75eb-30fa-a113-37a6857730b0 | -17.00514 | -56.67734 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 67eac284-0d82-3a2f-85ce-f2430097cb83 | -17.00399 | -56.68457 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8b53f0c5-5de2-3736-b14f-663206041545 | -16.99952 | -56.69122 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| 97f5da70-7b09-360a-9b74-e9c41d56872c | -16.99619 | -56.69065 | 2024-10-08 04:59:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |


[Clique aqui para ver as próximas entradas](README99.md)
