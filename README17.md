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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2666be5d-4d7c-3c61-a263-86771fc944bb | -15.97124 | -56.62566 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1602f888-ab1d-3d7a-a9e9-5110c2bd4f5d | -17.73508 | -57.24901 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 18ae31aa-0a26-3bce-8cee-52f95b04b154 | -17.56015 | -57.1812 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a1d291f3-849f-3d78-8723-7e720f21d79b | -17.51895 | -57.20631 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e332cc28-cf63-3197-9832-215eca77be4e | -14.6022 | -56.04005 | 2025-12-02 05:29:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bd3e2c7-266e-378c-976e-32914843da86 | -17.55047 | -57.15459 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 8e68cef7-5fd4-3a52-9fa0-d34d89f2bccd | -17.50779 | -57.19223 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 3361fe84-07e5-3c18-90e9-ecec2419db63 | -16.33138 | -57.56974 | 2025-12-02 05:29:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1adcb50a-eb5a-3110-98c6-28059ebb6351 | -17.51469 | -57.20572 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7f986a9b-1a96-3a7a-9103-7e6107f4b4bc | -17.49927 | -57.19104 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ad9e3e8f-ae16-3dc1-b9d4-3bde6a7536ae | -16.76578 | -55.10594 | 2025-12-02 05:29:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 8.8 |
| ae547274-25fc-3c65-adfa-0ee3b0650feb | -17.49874 | -57.19516 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f4afe1fd-4e6f-3d08-a3b4-2722cb3ae1eb | -17.503 | -57.19574 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| f70990d9-e8ef-38eb-ad8b-adc271fd61c1 | -14.07766 | -56.16561 | 2025-12-02 05:29:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d64172b1-a79e-3604-8228-7ffb315a96e6 | -17.55589 | -57.1806 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d6b37b1c-84b0-345f-8b1b-e2c9247dff29 | -17.51821 | -57.20464 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 48e313b6-dfd6-3832-b207-d9be6bdc715b | -17.52267 | -57.211 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 6ad32e6c-b13a-3698-923c-18765769d593 | -14.07331 | -56.16506 | 2025-12-02 05:29:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 283073bd-2062-3f24-9f21-756ec026ea4f | -16.76513 | -55.1114 | 2025-12-02 05:29:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 9e7d444e-baf3-3a95-b329-ada8ef34983c | -15.11834 | -52.94417 | 2025-12-02 05:29:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d569b22-307b-3ed2-8133-dbc439a41ad8 | -17.51097 | -57.20103 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 7f3ba564-0982-3ed2-911c-174770bd25bf | -17.49076 | -57.18987 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 1cd02edc-2ebb-3486-954e-9de380b6922b | -17.52195 | -57.20935 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d4bab7ed-3dbd-3490-b04c-1e1000ac37a2 | -17.51841 | -57.21041 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2cf32f1b-8e77-3946-adbf-0280fbf628b3 | -16.76094 | -55.10529 | 2025-12-02 05:29:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5e0b4333-a8c6-3736-8bdd-a605ad0f9c71 | -15.12381 | -52.94487 | 2025-12-02 05:29:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f749398-7475-3fd0-9316-9b9b197a7925 | -15.11792 | -52.94782 | 2025-12-02 05:29:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc575a56-e489-3186-ad26-666b8c642080 | -17.51446 | -57.19993 | 2025-12-02 05:29:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7713ab4e-f0af-39d8-901d-8862ea570981 | -13.02656 | -57.21924 | 2025-12-02 05:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fbca2744-bc4b-3dd5-b844-33e69891698c | -8.0513 | -43.1001 | 2025-12-02 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 113.1 |
| 720d2edb-9506-34a6-8dbd-c8c47f563eef | -8.0324 | -43.1022 | 2025-12-02 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.3 |
| f0669f1d-0bd0-3dbf-8a02-d5a9eb4f8cd4 | -18.84754 | -57.72913 | 2025-12-02 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8363d664-423a-34e5-8687-8446882b0927 | -19.78601 | -56.67079 | 2025-12-02 05:31:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| be6b9afd-a140-3e4b-901c-f349fa84b06a | -18.84747 | -57.73167 | 2025-12-02 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| ba54a2e9-8051-382f-8e0b-ebc8c3695671 | -19.78998 | -56.67622 | 2025-12-02 05:31:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b660c89a-0afd-3531-aa48-525f5e92de54 | -19.78429 | -56.68523 | 2025-12-02 05:31:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 44968bf3-82f2-3dad-be29-016cc88781a0 | -18.84845 | -57.72367 | 2025-12-02 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 62c25e45-c3c0-3c98-8b9a-950a77f7bf2c | -19.78372 | -56.69004 | 2025-12-02 05:31:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 282d7160-6241-33b6-8f4d-a59aa7368fe9 | -18.84796 | -57.72767 | 2025-12-02 05:31:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0841e497-1d27-3051-9c03-ac6e139e3ab5 | -19.78941 | -56.68103 | 2025-12-02 05:31:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f39cbc27-7bce-39b2-bf42-924ddfee0bf2 | -8.0513 | -43.1001 | 2025-12-02 05:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 116.2 |
| 3912a140-a06c-3d12-ba09-061f1afea7a1 | -3.40567 | -42.45373 | 2025-12-02 05:44:00 | AQUA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 85fbbb7c-5450-3cba-93d7-c030ae61bd73 | -2.51342 | -45.28778 | 2025-12-02 05:44:00 | AQUA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 22.3 |
| f50234b9-85a6-37af-9d47-77c1baceface | -3.25984 | -45.55347 | 2025-12-02 05:44:00 | AQUA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 424257ea-a268-3232-9609-f6c6052ec16b | 3.48614 | -51.26388 | 2025-12-02 05:46:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66a73b1b-8f24-37ce-be93-e40b9cfe4860 | 2.01405 | -55.7115 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cac06f20-a33d-32c8-b9c4-28c4a79c830d | 2.0146 | -55.71476 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 600233d7-ea5b-3a74-99ea-28e7c3a2c0c6 | 2.01184 | -55.71078 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af71ff7b-2af3-3d05-a1af-f16758310149 | 2.00637 | -55.71131 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3c716e89-a19b-3631-92ca-90c3048c2c0a | 2.01569 | -55.7213 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4faae576-adcb-32fd-8826-ff31ed0ad48f | 2.01884 | -55.7198 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c018d576-7e95-3f59-9629-057edb666cce | -8.04132 | -43.09583 | 2025-12-02 05:46:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.4 |
| a46fc212-20d8-391b-bbd4-8f6961ebe00e | -8.17105 | -43.22004 | 2025-12-02 05:46:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 4a35be87-76fa-36be-ace6-595cac84933d | 2.01627 | -55.72475 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 296283f7-8f1f-3880-a484-769824fbf118 | -8.05177 | -43.10322 | 2025-12-02 05:46:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.0 |
| 15109a95-94ab-3749-bfec-ea1bc40e5830 | 2.00915 | -55.71547 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b15b5150-69f2-3a3b-9a24-9fe927cb25cd | 2.00692 | -55.71471 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 21ecfdad-e0e9-389a-a391-d5c20f611b0a | -8.05314 | -43.09427 | 2025-12-02 05:46:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.9 |
| 1981af8f-3a59-3558-aafd-c4433a473601 | -8.03996 | -43.10479 | 2025-12-02 05:46:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| c6f25c44-709d-3d56-b770-8e370e405d4e | 2.01238 | -55.71412 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 760838a3-9c3a-38e3-8ca5-c992ced3654c | 2.00859 | -55.71212 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a53bb80-1a2f-3fab-be9b-7440cdd80212 | 2.01939 | -55.7232 | 2025-12-02 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d2fa953-3486-3fe7-b814-62cf753924dc | 3.47916 | -51.26509 | 2025-12-02 05:46:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8e90f71-f30b-348d-bcba-23f6d551650a | -8.17243 | -43.21101 | 2025-12-02 05:46:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 65c88606-685e-3c96-bc66-0ab91f5ce447 | -8.0513 | -43.1001 | 2025-12-02 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| 029aa2f1-5f8c-3ff6-81c4-76fb09ae0056 | -2.5145 | -45.2949 | 2025-12-02 05:50:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 62c95ea4-5ef5-38d6-8b1c-384fbff13517 | -2.5146 | -45.2724 | 2025-12-02 05:50:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 369bacbd-c598-3aed-a39b-a1b280d59dda | -8.0703 | -43.0981 | 2025-12-02 05:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| d955cbd1-501d-3455-afe0-7f1ee53c3163 | -12.04247 | -54.25114 | 2025-12-02 05:50:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| add94d93-eaee-3a7d-85f9-45168b094739 | -14.0735 | -56.17184 | 2025-12-02 05:50:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6ec53233-7e00-3fe2-a848-3ad017d49fa8 | -12.04326 | -54.2439 | 2025-12-02 05:50:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 120e994f-0e98-3191-9c51-4f206f24d351 | -14.07413 | -56.16599 | 2025-12-02 05:50:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ea92f865-ce41-36ec-a2b8-a8d1cab70599 | -17.50017 | -57.19767 | 2025-12-02 05:52:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6a9e928c-26ce-3eb4-b9ea-539ffba6c605 | -17.50658 | -57.19833 | 2025-12-02 05:52:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5aa3cf5f-06c1-3f09-aa42-33b869a4a5a3 | -17.51299 | -57.199 | 2025-12-02 05:52:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c0bd4e97-23b5-347d-aebe-88b97d437acb | -16.76277 | -55.11548 | 2025-12-02 05:52:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8366364c-13ee-388f-af96-17567b186074 | -17.5071 | -57.19289 | 2025-12-02 05:52:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 56c334cd-2b12-3db0-adc2-7027bee5a5d9 | -17.52478 | -57.2112 | 2025-12-02 05:52:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 69f026a1-0a48-3463-a0ed-ecc6ab607215 | -17.53119 | -57.21186 | 2025-12-02 05:52:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| dfefe511-3a23-39b2-aba8-040f8338a0a0 | -17.51248 | -57.20444 | 2025-12-02 05:52:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c725342c-8d07-3df7-bb49-5f8bc718789c | -16.76342 | -55.10824 | 2025-12-02 05:52:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f0698c79-c5ef-3f4d-9b1f-6a3c55af2cb8 | -17.51837 | -57.21053 | 2025-12-02 05:52:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2c309c32-edee-3108-a697-e643056112d7 | -8.1633 | -43.2055 | 2025-12-02 06:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.6 |
| 4455786c-b64d-37c2-ad89-558d2de1fac4 | -2.5145 | -45.2949 | 2025-12-02 06:00:00 | GOES-19 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 8aee4d0a-f83d-3efc-98a2-0838e1bb59eb | -8.0513 | -43.1001 | 2025-12-02 06:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.3 |
| 5482a125-13c1-353b-9d8e-1f83109e5eca | -8.0513 | -43.1001 | 2025-12-02 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 056e2167-d0ec-32c1-aeac-99f4920a4c6b | -8.163 | -43.229 | 2025-12-02 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| e01395cb-32c2-3868-91a4-1418942d41fb | -8.1633 | -43.2055 | 2025-12-02 06:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 1e200384-28bc-3f74-84af-56dec13c0218 | -8.0513 | -43.1001 | 2025-12-02 06:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| 5327f747-920b-3c89-bc7a-49686c27dab4 | -8.163 | -43.229 | 2025-12-02 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.2 |
| d7c84535-3cc1-330a-a282-7d1eddd13198 | -8.1633 | -43.2055 | 2025-12-02 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 68.1 |
| b306ba3a-8a1e-3d3d-b246-ab42b576aa15 | -8.1822 | -43.2034 | 2025-12-02 06:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.8 |
| b812124e-8988-3c20-8308-4c215ea72a89 | -8.163 | -43.229 | 2025-12-02 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.8 |
| 1b03d3fd-c154-34b0-ac6e-646e05d79740 | -8.1633 | -43.2055 | 2025-12-02 06:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 8a4f1a50-c8cd-3dde-9c37-bc73d6e0513c | -6.42875 | -37.89676 | 2025-12-02 11:36:00 | TERRA_M-M | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 658cc83e-c2f0-3d9a-99cc-80891c3613b0 | -6.7785 | -37.31689 | 2025-12-02 11:36:00 | TERRA_M-M | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 2e52e313-58ee-3383-af1d-baee6325f3b5 | -6.1069 | -38.52364 | 2025-12-02 11:36:00 | TERRA_M-M | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c9a90e35-e8e7-3304-821a-bb446ae500bd | -6.77723 | -37.32595 | 2025-12-02 11:36:00 | TERRA_M-M | SÃO JOSÉ DE ESPINHARAS | PARAÍBA | Brasil | 2514404 | 25 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 74b3027d-2aaf-331d-975b-f42d59829a0c | -8.43162 | -36.5721 | 2025-12-02 11:36:00 | TERRA_M-M | SANHARÓ | PERNAMBUCO | Brasil | 2612406 | 26 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 4a4dc0c9-85c2-3143-a3ca-8366a1239ce7 | -7.82051 | -35.37516 | 2025-12-02 11:36:00 | TERRA_M-M | LAGOA DO CARRO | PERNAMBUCO | Brasil | 2608453 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |


[Clique aqui para ver as próximas entradas](README18.md)
