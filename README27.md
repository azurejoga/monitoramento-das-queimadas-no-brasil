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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 053c7186-df9e-339a-816f-2aaa7afb0ab6 | -18.90065 | -54.53218 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 20.3 |
| bf2eb5f5-8246-3476-adb8-0b878d5095cd | -18.89572 | -54.56148 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 821a1e59-607e-3d71-a657-c456e20f4c9c | -18.89441 | -54.55217 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 98d07b5b-1612-3ef6-9c14-ef4d68ce662f | -18.8941 | -54.48554 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 38.1 |
| 69568942-9d41-3c22-a862-04b9def99064 | -18.8931 | -54.54287 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e5c66366-117d-3e8a-8a96-c6efbcbdab9d | -18.89279 | -54.47619 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 23.5 |
| abda5e0c-0bfb-3761-89a0-c78e7d9722fb | -18.88817 | -54.57222 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5e42eca6-e5ec-365f-b10c-91cda7637c25 | -18.88686 | -54.56288 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 64ce901c-2fcc-300c-9cf7-086300388638 | -18.87931 | -54.57362 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 705897c8-e233-3d3a-85dd-ae7ded9d3e78 | -18.87801 | -54.56431 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 0049f166-8643-346b-be0f-c684276583f4 | -18.86915 | -54.5657 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 6974b644-3645-313a-910b-d76544e743ec | -18.86784 | -54.55637 | 2024-10-07 01:30:00 | TERRA_M-M | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 16.7 |
| aa4b2c0f-06e4-3d8b-89fa-0d192b417cdb | -16.64067 | -55.56156 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 15782fe5-8ee3-321e-95af-4118dd8a4659 | -16.63307 | -55.57212 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 6ce0a69a-91ff-31c8-a48d-11ef5fe60b86 | -16.6318 | -55.56288 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 3ef4cbcf-eaff-313b-ae60-aa8ec2307db4 | -16.6242 | -55.57345 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 40c9dcda-af8a-3b1a-a855-3d12ea2a39b1 | -16.62293 | -55.56422 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 33241b2a-392b-3e65-a5a6-4e1823f00cc3 | -16.61912 | -55.53662 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| fc0465ce-b11f-3cc9-aca1-fe03fec5a05d | -16.61661 | -55.58403 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.3 |
| 31b70cf1-83cb-3350-8f59-b97fbf7d207b | -16.61534 | -55.57481 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.9 |
| 5312d9e4-9aef-30f8-9d3e-5fb6b5512d37 | -16.61407 | -55.56559 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 889a24f9-3b4b-3bb3-8ebe-681b8e262766 | -16.61114 | -55.21861 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 424e54ee-d034-3905-a4d4-ff808dd05684 | -16.60774 | -55.58538 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 901b6aab-10e6-3d6f-b3b0-2cfd1123e6bf | -16.60647 | -55.57616 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 003f2a7f-140a-3b36-84a2-95232afac728 | -16.58165 | -56.06889 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| b94bd2fc-2c63-38ab-8995-d7f56fbf4915 | -16.58038 | -56.05954 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 8c573581-0c12-3af9-b71c-ad458985420d | -16.56141 | -55.91971 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 1e79c7f9-39f2-36b8-a3b1-150dffd6c90c | -16.5525 | -55.92104 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b6c0b56a-0fed-3abf-a1dd-a7b1c13dbb22 | -16.35847 | -55.98128 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| cca2d4dd-0393-3cc4-850d-7371bdbb7d18 | -16.15651 | -55.92536 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.2 |
| f58332f7-e3e1-3cd1-8fe8-a716f0336c72 | -16.14 | -55.87127 | 2024-10-07 01:30:00 | TERRA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 7db36670-a94b-341c-be80-dc59e7f5e9ab | -17.19199 | -56.29855 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 57219233-10ea-3621-a0e7-65f5659f9e8d | -17.15356 | -56.14893 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| f3efd6e2-ef54-3ee2-9f94-d7db93ae99f3 | -17.14585 | -56.15974 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 719bc692-7fe5-3786-b4e4-bb181dce9068 | -16.92654 | -55.8311 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d9807bc6-82d0-3551-a938-b8fae89389c6 | -16.92271 | -55.86972 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 844f2503-929e-35f7-aacd-82ac9f408e56 | -16.89597 | -55.87373 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| fb233137-e220-3a27-8a02-3ae37977575f | -16.85882 | -55.80919 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| eb3b8caa-1124-33cc-9e07-452b7b0c35ce | -16.69789 | -55.91199 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 68eb811e-8ac0-324d-8582-a3a696e738ac | -16.69534 | -55.9599 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 6066555c-b6f3-37cb-8918-d1788645d2a8 | -16.69407 | -55.95058 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| 66cb4330-3c34-3680-a441-dd159bde147a | -16.68642 | -55.96124 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| ef3ead5d-1f06-3ca8-a715-b19e9583e2c0 | -16.68515 | -55.95192 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 5508aa37-b362-3002-9b15-f21a08c48b11 | -16.67626 | -55.88675 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| f723e689-e598-3527-8587-3f345b3c43b8 | -16.675 | -55.87745 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 56937bf4-1672-33c2-ba6b-8016da8d4eeb | -16.66863 | -55.89738 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 4ff2b3d4-706d-36bf-9158-cd6307b45e98 | -16.66736 | -55.88808 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 45.4 |
| 709d2246-ef1a-3bde-84ec-9eb19e8b22dc | -16.66609 | -55.87879 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| d250907b-1691-34bf-99af-8c02331a7442 | -16.66099 | -55.90802 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 61288e1d-65f8-32f7-a9a9-187b9b35afa0 | -16.65081 | -55.90005 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 7714c411-204c-3519-9e6e-f55f12de9676 | -16.64317 | -55.91069 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 5b2d87a1-8659-35af-a8e2-6dce0f327b30 | -16.64191 | -55.90139 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 46d827e4-83b0-3a9e-b546-42f1c0f0d829 | -16.62536 | -55.91337 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 09e3f072-67c1-3a57-839c-722c63706c22 | -16.6241 | -55.90407 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 20.0 |
| aa301737-e969-3fa2-963c-83ce13b26cac | -16.61612 | -55.921 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| e98504a7-50d5-3d51-b1c8-3c8aaaa85308 | -16.61485 | -55.9117 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 49e15707-95f1-37de-94a7-3b00647db756 | -16.61357 | -55.9024 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 86cb83e5-47a7-33d3-be18-6141a06a02db | -17.0579 | -56.05339 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 82a073b1-21c7-3dfe-be85-8518b535a65f | -17.04895 | -56.05473 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 20413a61-744f-3299-aee3-59b58fb0256a | -17.03099 | -56.67937 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 6af0c31b-8269-344d-b8ab-1f54216e03b1 | -17.02315 | -56.69048 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| 479176b8-6894-3022-86aa-0b4304a4b1a7 | -17.02187 | -56.68069 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 53.0 |
| c762dfe6-eee3-3854-a5e6-d6af991916b3 | -17.01403 | -56.6918 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.9 |
| 520ad0c2-3f17-3920-abbd-e2baa242217a | -17.01275 | -56.68201 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.4 |
| 2f7266fb-7349-3169-a5fe-b58700f4e2b6 | -17.00491 | -56.69313 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 23.5 |
| ea819d7c-80d6-38e1-be3a-2acf9c2a22a8 | -17.00363 | -56.68335 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| d5cdf905-c717-303f-bfac-860415c4d24a | -16.99631 | -56.69034 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 6946a752-e364-3171-9339-523f28ac3980 | -16.96768 | -56.61499 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 16.6 |
| 532e7a58-313c-3665-b8f7-076f9d4aacb3 | -16.95988 | -56.62605 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 20cdebb5-2f48-3ef2-b926-6022528b609d | -16.9404 | -56.61897 | 2024-10-07 01:30:00 | TERRA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 6c913f46-d9ae-3056-b26a-9bb9dda0e2aa | -15.97163 | -57.2268 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| d1b2a595-f47f-33eb-88ea-5fe68b12e6e0 | -15.9653 | -57.23349 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 844c399b-d4c0-35e1-9239-91cd2eb6ccab | -15.96399 | -57.2236 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 2c408c36-ed3e-388f-9b01-817b54758fec | -15.96269 | -57.21383 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| fa46ad55-bd7f-3347-8e70-58a0b30b2ba6 | -15.95475 | -57.22486 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| cd3a9c8c-fa63-3962-b395-fcceb56d94fb | -15.90877 | -57.16091 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ed3cf51-c55c-338a-887e-034a78b9214a | -15.90747 | -57.151 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 94d005d9-fc88-33a3-ba5f-a115efe2bf63 | -17.85134 | -57.67902 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 0b3c1c44-a9ed-3f41-b9ba-ecf4b9448371 | -17.84311 | -57.69146 | 2024-10-07 01:30:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 5776ede0-c04f-31b2-ac50-5bfcbe18b307 | -17.73536 | -57.07679 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.5 |
| f7f0ed33-3a6e-39b3-afd9-82ffdf712c8a | -17.72603 | -57.07813 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.1 |
| e3852da5-6b37-37c6-ac83-a7d75e842af0 | -17.16711 | -57.35899 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 28.7 |
| 2d26f867-21d1-335d-b39b-f193bab40977 | -17.16575 | -57.34856 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 32.4 |
| 00c9e0c0-b3e7-325d-8aa3-3da05498771d | -17.15644 | -57.42454 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 5c400203-4c1e-33c9-9433-bbae2c111711 | -17.15508 | -57.41402 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.4 |
| a667f43a-9b3e-3eb3-8634-8af066394646 | -17.15499 | -57.33946 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.3 |
| c10109b0-04b2-3f69-bd99-de8061e9213c | -17.15165 | -56.75569 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 38.7 |
| 99155b37-08bf-3970-ad2c-1d50859f1ce3 | -17.15035 | -56.74582 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| ffe81c91-626b-37e8-a935-782cd1c05aec | -17.14831 | -57.36165 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.7 |
| a30a3e3c-a19d-3827-8318-9a0f77012feb | -17.14701 | -57.42586 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 174.9 |
| 95e24dd1-2107-3b8e-92d1-b96fee3f075d | -17.14565 | -57.41536 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 111.6 |
| f0406e70-ea2c-3034-ba53-d33926fa5a36 | -17.14379 | -56.76689 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 971b3058-deb0-3f7e-a49a-6a3d5cfb79a5 | -17.14218 | -56.9702 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 1ba0e3e1-cf82-314d-abc7-7aff821173bc | -17.1412 | -56.74715 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| af6e3e13-92d5-3fc0-9f84-234e4004650e | -17.13758 | -57.4272 | 2024-10-07 01:30:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.2 |
| fe6cef25-12fe-3163-93c6-a909326a20ef | -17.03332 | -56.83962 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 20.2 |
| c79ecc57-14d6-3d6f-b4bd-d3cc09505090 | -17.03203 | -56.82971 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 52fae7ba-3f05-3e64-9280-5fd744410699 | -17.02414 | -56.84095 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 21.0 |
| 320095ac-3895-3dee-883f-893fccc96962 | -17.02286 | -56.83104 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| bb39f560-e99e-3977-bca2-5d61e6397d1f | -17.016 | -56.83796 | 2024-10-07 01:30:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 25.1 |


[Clique aqui para ver as próximas entradas](README28.md)
