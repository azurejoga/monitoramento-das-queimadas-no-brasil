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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bfd3642-2cc5-3fc4-b471-35018376f0df | -16.6598 | -55.889198 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d73f963c-c20d-3bbc-9dd2-498fc16a3fd2 | -16.661301 | -55.8965 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b370a5e-d61f-3203-887e-fd42afb7b649 | -16.662901 | -55.903801 | 2024-10-07 01:20:54 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57bb08e9-3c2d-3b30-bf29-9a8911924ad4 | -16.8417 | -56.730301 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7fe737e6-897c-3c04-b804-d1378da2a295 | -16.8433 | -56.7379 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 778a67fd-1fc0-37b9-b047-600697b9dad3 | -16.8449 | -56.745602 | 2024-10-07 01:20:54 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e4ef438-fae2-3b6a-a91f-3fb7129fb4a9 | -16.561899 | -55.9119 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 97b97310-b8b2-304a-9a80-c0d91c25298a | -16.831499 | -57.164101 | 2024-10-07 01:20:56 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fdcb8415-1428-3c42-8890-4225caf82cab | -16.552099 | -55.914101 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5a2caa8c-e784-35a2-9e40-b294c9df74e2 | -16.553699 | -55.921398 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 15a279a1-c220-31ae-889d-23757336189f | -16.560101 | -55.9505 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4b395f16-d01c-3c15-aadc-a3f182a3c7d0 | -16.5616 | -55.957802 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0772e09e-062f-3cc8-9ffe-67249c1f8c33 | -16.5632 | -55.965099 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1afd6821-f631-3c63-b62a-23c809e585d1 | -16.582399 | -56.0527 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e144ac53-d6c8-3a71-b296-1040f7cbf77f | -16.584 | -56.060101 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4c093889-5b07-3c19-8c55-6004cee653af | -16.572599 | -56.055 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 54e3cd9d-39d2-36cd-a16e-d627bdbecd12 | -16.5742 | -56.062401 | 2024-10-07 01:20:56 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0efaf34-724d-3f65-ac08-5f6c63e76987 | -16.919201 | -57.678101 | 2024-10-07 01:20:56 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 193124ba-b5ff-38a9-8d6b-054ebc6fd8fb | -16.921 | -57.686401 | 2024-10-07 01:20:56 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3bc341b7-c9d5-3948-85b7-84533a35ad7f | -16.909401 | -57.680199 | 2024-10-07 01:20:56 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| aaaab413-a2fb-37e0-ba43-738516ff3127 | -16.9112 | -57.688499 | 2024-10-07 01:20:56 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6dbe2c18-3e32-33f2-a266-30453d27048b | -16.823 | -57.366199 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8648cf8b-2212-34f9-9ccf-9f777887e12d | -16.824699 | -57.374298 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c19afdd7-3484-388c-a55b-05cfe822c94b | -16.84 | -57.446899 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a934cce7-2ffe-34a3-9511-f0bb3621e1ad | -16.811501 | -57.360401 | 2024-10-07 01:20:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 05093801-5cb0-33b9-9b74-2dc2c2d56619 | -16.8132 | -57.368401 | 2024-10-07 01:20:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 53f7ae9e-a6b5-323b-ba10-a8e3b2dc5ec7 | -16.814899 | -57.376499 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03832e9a-deec-350f-93fb-400e3dbb8b7c | -16.816601 | -57.384499 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9bfd1207-401d-3b97-adf2-d09ef58cb869 | -16.826799 | -57.432899 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6a619375-cd89-33eb-b7b2-dbcdba06e50a | -16.828501 | -57.441002 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e8e7268-9f4c-3357-9a16-59d2f804057b | -16.8302 | -57.4491 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7d07cfc9-a207-3ec1-8f15-609d81a7f5db | -16.805201 | -57.3787 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a97a803b-e3e2-3ee7-b6b3-2cf90454fa1e | -16.806801 | -57.3867 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4426462c-72b3-3ce5-91c7-0f353cbef110 | -16.8085 | -57.394798 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9fd3521d-5e58-3cb4-9d6f-1ccc7cd087fd | -16.8102 | -57.402802 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fd9552fa-b92f-31b0-bdf6-d6965fd52bb7 | -16.8153 | -57.426998 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d0db5cc4-a3fb-3f76-8d7b-9675652d36b6 | -16.816999 | -57.435101 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cb9bb3be-0098-38b1-ab09-2bc4fb97a444 | -16.818701 | -57.443199 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2ab367af-fe06-3175-b199-460e3cf13891 | -16.820499 | -57.451302 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| caf92ff3-02f6-34db-82c1-d2f6cb746cfc | -16.795401 | -57.380901 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cd55c4b8-771f-32a5-8688-31002ea302dd | -16.797001 | -57.388901 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6493126e-132e-3dc0-a07c-00bc9973be38 | -16.7987 | -57.396999 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7f12cf74-430b-3f4c-ad55-829547cc805c | -16.8004 | -57.404999 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ed13abdc-dd74-31e4-af16-2bc6e807b22d | -16.8055 | -57.429199 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f99277c2-dbde-3cd5-a0c6-d4fd9b50bfea | -16.807199 | -57.437302 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 542e8708-f4be-3ab2-93cf-e42224bc545f | -16.808901 | -57.4454 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a57018e-ae80-30d0-80ef-c5052f387f23 | -16.817499 | -57.485901 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4d6661e-5bf7-33db-8eaf-46ac95976ac9 | -16.819201 | -57.494099 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b0e6fab1-1079-3f61-9b07-b585ee0dfdad | -16.785601 | -57.382999 | 2024-10-07 01:20:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 82e2ecb2-7f10-39e4-a19b-0abf6f5195ff | -16.787201 | -57.391102 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 689bff41-c3b0-3f22-8b78-a8bf782d5dbf | -16.7889 | -57.399101 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2006cf68-5828-3b89-99af-4f8885944c45 | -16.7906 | -57.4072 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e483c725-a506-32fc-81fa-3a75d4c86bcc | -16.777399 | -57.393299 | 2024-10-07 01:20:57 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1cde7252-422b-3f60-aeb5-4031544ba2e8 | -16.7791 | -57.401299 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0dcbba34-aac5-3a28-b1d4-a41b6cab1d59 | -16.7808 | -57.409401 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 20f3897b-cc70-3e39-a631-e6b7c2cb7b00 | -16.782499 | -57.4174 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b5dcac15-d1b8-3187-9bd1-2cb13fcaf354 | -16.784201 | -57.425499 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| deeced49-7426-3270-8ecf-6e399c4d6061 | -16.7859 | -57.433601 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 74cf4f90-9435-3f75-a09e-4803b646226a | -16.7876 | -57.4417 | 2024-10-07 01:20:57 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 25ceb271-ae17-3ca6-af71-8cce339b34b3 | -16.772699 | -57.419601 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5de6de6c-e6a4-3b41-8aa8-23094bdabac4 | -16.774401 | -57.427601 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f6338acf-7926-355a-bdab-24db7701fa5d | -16.7761 | -57.435699 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9bc0ad17-ae66-331f-885a-e264b08b2acb | -16.7778 | -57.443802 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c4f7b0e0-718c-3860-90c8-d0997cb4a6c9 | -16.783001 | -57.468102 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| adaf5eac-8121-3c2f-915b-f54962428600 | -16.7847 | -57.4762 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8a92592f-8807-3594-8b67-bcbd7ebe7cc6 | -16.7715 | -57.4622 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4a38e147-6194-3d1e-80cf-e52cc462e8aa | -16.773199 | -57.470299 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 826857b1-ad62-3df1-a3d2-439351de4c75 | -16.7749 | -57.478401 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1292c5f3-a21e-318e-a73c-a84ec695a9c6 | -16.7766 | -57.4865 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8e976e03-02e2-3eb0-90d8-7e1ffc4176ed | -16.778299 | -57.494598 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 67f29747-ed49-3b44-b1f8-d262ac6d5dda | -16.7801 | -57.5028 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 269f3442-d400-320f-9ba5-60d3fe219f64 | -16.763399 | -57.472401 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cc8e0ddf-2b47-3a0c-bfa8-7dd2fc0849c4 | -16.7651 | -57.480499 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bf0ccc86-e51f-39ed-8847-6376ec5dfd5f | -16.7668 | -57.488701 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eeea9026-823f-30fc-9a78-a87b9acdb231 | -16.768499 | -57.496799 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 985800ad-c894-3881-b209-8f7859a925dd | -16.7703 | -57.504902 | 2024-10-07 01:20:58 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cfac7777-1152-3c9e-b6cb-53186c3b44ac | -16.620701 | -57.1371 | 2024-10-07 01:20:59 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e59e64b-1b6d-300f-a09a-022e8f092b28 | -16.6224 | -57.145 | 2024-10-07 01:20:59 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f0043a95-9c79-3ef4-bf27-83f5ffcae5b0 | -16.359501 | -55.9739 | 2024-10-07 01:20:59 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31906256-c759-37de-b2a5-d190b9cf82df | -16.1387 | -55.857601 | 2024-10-07 01:21:02 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d6646c99-da98-3c83-9d96-51286ee79756 | -16.1402 | -55.864799 | 2024-10-07 01:21:02 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dae12f90-f7db-3cc3-9eba-9f5fa1ac43d7 | -16.1513 | -55.915298 | 2024-10-07 01:21:02 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7869f6fb-1da0-3c74-bc64-876a9c28c41e | -16.152901 | -55.9226 | 2024-10-07 01:21:02 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9034264a-24a2-3483-a098-4bf96128c362 | -16.497801 | -57.719398 | 2024-10-07 01:21:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a87dbeed-b887-374f-9019-581cf3d40b19 | -16.499599 | -57.727699 | 2024-10-07 01:21:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8bd7046d-d229-305f-94f2-4e81c0ab7324 | -16.501301 | -57.735901 | 2024-10-07 01:21:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89fe82f4-bf70-3ff2-8cbb-31dcf8beaeda | -16.503 | -57.744202 | 2024-10-07 01:21:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3b535008-a3be-3d51-aee9-a088b0457bff | -16.488001 | -57.7216 | 2024-10-07 01:21:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1dce190f-5cdd-3f86-9f0d-677603421ca7 | -16.489799 | -57.7299 | 2024-10-07 01:21:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cf4a43d0-abe9-3ce2-a110-e1b55e7bb505 | -16.491501 | -57.738098 | 2024-10-07 01:21:03 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6f0e9c95-4f04-3a86-97b8-82120c2cdb33 | -15.8939 | -55.4025 | 2024-10-07 01:21:05 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9797ece7-3ca6-31fb-9fb3-da4351188a2f | -16.120399 | -57.5816 | 2024-10-07 01:21:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a2c02863-0981-3293-9557-7d4e284b54c0 | -16.1038 | -57.551701 | 2024-10-07 01:21:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 580db8b0-9858-39de-93d7-b07b24c94c74 | -16.105499 | -57.5597 | 2024-10-07 01:21:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 77a9b0ab-1c41-33e3-a229-a2ee77449704 | -15.9711 | -57.2173 | 2024-10-07 01:21:10 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7dc1e85b-4aa8-3b91-b82e-6f03a89d7f91 | -15.9597 | -57.2118 | 2024-10-07 01:21:10 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46f8bf88-8273-399c-afe4-cdd3bbbbd972 | -15.9614 | -57.219501 | 2024-10-07 01:21:10 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 374885c4-87a3-3a9f-bfa8-3a9780854c2c | -15.963 | -57.227299 | 2024-10-07 01:21:10 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fa42beb1-6960-34db-b549-c1868bdb30f4 | -15.9039 | -57.143101 | 2024-10-07 01:21:11 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e453fc6a-f2a9-328e-8934-bca4146bec79 | -15.9056 | -57.150799 | 2024-10-07 01:21:11 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README23.md)
