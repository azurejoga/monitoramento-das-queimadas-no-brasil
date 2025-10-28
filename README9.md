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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 987a40b0-1623-328b-8504-9f4b40df9d32 | -7.9693 | -46.7423 | 2025-10-28 03:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| bde72bd7-3081-3dcd-8c5c-c708676d3879 | -7.965 | -45.509 | 2025-10-28 03:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 35233bc7-1f58-3c83-b143-2951f85a36c0 | -7.9464 | -45.4882 | 2025-10-28 03:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 5c71fece-b22c-326a-81cb-811a4c87bc07 | -15.1555 | -46.5832 | 2025-10-28 03:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 350.3 |
| a498b675-a94e-3e3f-a38c-e71415ccd27b | -7.9882 | -46.7406 | 2025-10-28 03:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 3c471f4c-dc93-30de-a8f9-d35644080bac | -15.155 | -46.6062 | 2025-10-28 03:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 3a2cfc7e-9171-37f2-bf3b-5da2a2c193de | -15.1751 | -46.5797 | 2025-10-28 03:20:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 5b5e449e-7ee1-3911-a413-ad050b6aa59b | -6.8274 | -41.20636 | 2025-10-28 03:21:00 | NOAA-20 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 83c08a97-d85e-367a-bd6f-eef525b49094 | -6.13509 | -41.72123 | 2025-10-28 03:21:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 14096638-af03-332b-ae02-81848b490295 | -6.68275 | -42.0453 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 431924e9-257d-3df1-9414-fb043542b415 | -5.65983 | -41.14315 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f7bc16aa-4fbe-3742-af6b-ddcd18cb6a8a | -4.44936 | -43.65229 | 2025-10-28 03:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1d302af7-0fc2-37b5-a97c-963cd4b53af3 | -5.58935 | -41.31844 | 2025-10-28 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7c1316c8-6860-3248-a007-d1cfb2259a28 | -8.04567 | -41.11396 | 2025-10-28 03:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e54914fa-9a35-3923-8914-1c1e189d32f0 | -4.46252 | -43.23483 | 2025-10-28 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 18f50ba5-10a7-351c-9710-1075f1ec6d0e | -6.16125 | -41.54131 | 2025-10-28 03:21:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| faed73f8-b428-37f6-9576-283d9c3e6682 | -3.58167 | -43.60714 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ade9ce64-36ff-3d54-a46e-5a5cd55cfdbc | -4.46135 | -43.2413 | 2025-10-28 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 9a288bc6-af5d-31cf-8744-26a96e18037d | -3.5707 | -43.62744 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dea8e320-6bc1-3729-9cd6-e6f2a52d3245 | -8.04638 | -41.1072 | 2025-10-28 03:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f086455e-3603-31fb-b091-5ee36630b7ea | -6.87828 | -43.59262 | 2025-10-28 03:21:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d11dee38-6602-3e2b-a490-1b1e2841c99c | -6.12867 | -42.69973 | 2025-10-28 03:21:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| db1d0ab2-9c0b-3790-8c2a-d725c1caf95d | -6.70052 | -42.05395 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| bd63872a-5231-3cf0-b668-2607c11132d4 | -4.45442 | -43.24012 | 2025-10-28 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 025d7d14-6efb-3708-8095-22c0c970b1ab | -4.46328 | -43.23537 | 2025-10-28 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c792e157-7241-3fdb-94de-abd1659eb061 | -5.6398 | -41.10473 | 2025-10-28 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c71070d9-e3e7-3c96-bfcf-ff4afcb9d5a1 | -5.45734 | -40.88795 | 2025-10-28 03:21:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 87714002-4d02-3826-af78-7c48bdc6e795 | -6.69873 | -42.05164 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a1e1384f-87d3-36ce-9cdd-fc762c234a20 | -5.65817 | -41.1406 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 941fa71a-0782-3cb8-ad45-f88e1cb8d756 | -3.58753 | -43.61584 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 14490f54-07dc-3eb7-9672-7ddea8c86ab1 | -6.68722 | -42.04425 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 8afa2b69-8484-3eb8-8a75-9d20a32530d8 | -6.68808 | -42.05149 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| bfedaa7e-3c91-3ee3-9991-f527860aaa64 | -3.5779 | -43.62854 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6725124b-0bd6-3a57-944c-4aee587ccde0 | -5.59012 | -41.31413 | 2025-10-28 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e42a23cc-f11d-3dcf-bc41-75ad06708310 | -6.68365 | -42.04034 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| f9ec97a0-d97c-3ac7-b601-6813c6826831 | -4.50464 | -42.84755 | 2025-10-28 03:21:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a8ca5e3-1f3f-3906-acee-2e2046ad6041 | -5.97782 | -35.34151 | 2025-10-28 03:21:00 | NOAA-20 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 78142551-ed2f-329d-a1ed-756611deb4bd | -7.60326 | -43.59342 | 2025-10-28 03:21:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f2c1e29-c6b5-3fc5-a2c2-b29bb94686f5 | -3.44131 | -41.8555 | 2025-10-28 03:21:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8f12c63b-b844-3c30-b75d-411ff07ec57e | -8.19522 | -44.44487 | 2025-10-28 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c004147-1436-3340-beb1-cc443a7948b7 | -6.11824 | -41.71363 | 2025-10-28 03:21:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| efe83bc7-b675-3b01-a160-21ad106f2e2d | -6.60779 | -42.06711 | 2025-10-28 03:21:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| fa3232d1-5b48-3862-8d94-7183aa48cbfc | -6.64648 | -43.39172 | 2025-10-28 03:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0132940-f43e-3382-99bb-4cb812a2379c | -6.42466 | -42.33527 | 2025-10-28 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2c5e6278-78eb-3bfc-81c0-9df174943090 | -8.18866 | -44.45229 | 2025-10-28 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 52d8ae63-93db-3209-b02d-b8b290ca3bdc | -5.79633 | -35.6001 | 2025-10-28 03:21:00 | NOAA-20 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 11f89cfc-e0d0-3de8-964b-118e9ab97575 | -6.58386 | -42.7006 | 2025-10-28 03:21:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a366eadc-4f10-3ae5-b5c6-6c60fdcfda8f | -6.68629 | -42.04921 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 972859ed-c440-3501-bcac-9ae1058bf5f3 | -6.58468 | -42.69796 | 2025-10-28 03:21:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fe564221-1305-32c5-9b29-864fe1711a9f | -6.6943 | -42.05271 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| caf13634-940c-380d-91d9-be13891a2c39 | -5.65898 | -41.14777 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f505c69e-5ed3-3441-9ec3-3cb0b6be754d | -6.12765 | -42.70513 | 2025-10-28 03:21:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ab03bdc8-7a1e-3863-a5bc-76d3ea714098 | -7.59769 | -43.58588 | 2025-10-28 03:21:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d932e52e-6b2d-3924-b931-bc7a0161dd31 | -4.50405 | -42.84081 | 2025-10-28 03:21:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff092171-3d6c-34bf-9d55-4bd4878b7755 | -5.60278 | -42.77482 | 2025-10-28 03:21:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b65d805a-5aea-3cb7-957c-9cb63ac1cfa6 | -8.0449 | -41.11541 | 2025-10-28 03:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| eb1c8f9f-d644-3d52-b387-e29b212dd379 | -5.62735 | -39.65926 | 2025-10-28 03:21:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f3c2e4fa-91b1-323e-bad1-ad5bd2d19e89 | -6.48331 | -42.23151 | 2025-10-28 03:21:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b74cb96f-b128-3e13-b861-b65f16c5624e | -6.69251 | -42.05042 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 08e41af9-573c-3186-8784-09fe4369bff6 | -3.57324 | -43.61307 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e73ee6c3-9bdb-3ab1-8ff8-ec40b9046d7b | -3.57198 | -43.62023 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 02cc2df7-435e-3d45-b495-66cc85df166c | -3.58502 | -41.06402 | 2025-10-28 03:21:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ae6cf247-ee5f-3d1b-9237-29c24fe14f35 | -7.09775 | -39.56147 | 2025-10-28 03:21:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0dc2ab78-84c4-3331-9f93-bc915dc1883c | -6.58494 | -42.69483 | 2025-10-28 03:21:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59535caa-9dc6-3659-afad-432bcddfbac3 | -6.69433 | -42.0407 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 7f091cb8-9b03-3b53-91e9-320e2833f9aa | -7.09244 | -39.5607 | 2025-10-28 03:21:00 | NOAA-20 | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e298e9a8-dc27-3931-9b56-608544f065ce | -9.0513 | -38.94245 | 2025-10-28 03:21:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0450afce-f416-3957-a8d9-8ba38e77fb5f | -5.41905 | -35.67038 | 2025-10-28 03:21:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9c02b38b-41b5-3dab-8b20-23ed7b699d50 | -5.21472 | -37.38861 | 2025-10-28 03:21:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50f4de07-100c-3e98-babd-c2ce79475e31 | -3.44227 | -41.84998 | 2025-10-28 03:21:00 | NOAA-20 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 7fbc9435-0c96-3b9a-b9bd-38aa031c2f85 | -6.64755 | -43.3861 | 2025-10-28 03:21:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| be793d8a-d3fe-345d-9de5-fb7d2d0c999b | -7.96792 | -38.28018 | 2025-10-28 03:21:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 92904c58-7f80-36cf-a491-8d713b879a6b | -6.70227 | -42.04419 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 8ab0aee3-b545-3449-8985-a22fc7a118aa | -6.68986 | -42.0416 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 43cdef1f-c62b-32e9-9f64-dacbb8b84b6f | -4.45649 | -43.65334 | 2025-10-28 03:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 714ecb54-cbad-3d7a-9515-52f0e1ee4884 | -7.59972 | -43.58657 | 2025-10-28 03:21:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c46c2873-e97d-3c6e-88ce-2e7c0656526a | -5.65899 | -41.13597 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1d8368b5-9fd6-3ae6-9eba-2c72b0ad911e | -6.12923 | -42.70279 | 2025-10-28 03:21:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| be97a0ea-3103-376f-a4d8-fc61375f9309 | -5.65619 | -41.11679 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fbeb013b-ba5e-3e58-8214-54ff4572528d | -5.65134 | -41.14431 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1550d21c-970a-30d5-8fd4-4131d1e581d1 | -6.58573 | -42.69214 | 2025-10-28 03:21:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d39b1dcd-972d-3dad-a260-a194f2ee3e5c | -3.57663 | -43.63578 | 2025-10-28 03:21:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a47ce09d-f214-38ac-8a5a-5b2afe49dc4e | -7.59652 | -43.59217 | 2025-10-28 03:21:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02d4eff5-fc3d-3a9b-968f-924a6854a08e | -5.65654 | -41.14993 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4807fb55-16ae-3c1c-b17d-d5a5e8b63d6a | -5.62889 | -39.65652 | 2025-10-28 03:21:00 | NOAA-20 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 4cbf0cab-4a2c-3bec-99f0-2c9a8e948785 | -6.12389 | -41.71284 | 2025-10-28 03:21:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| da5ac30c-f7fb-34a8-864f-264cdd8537b3 | -4.50296 | -42.84704 | 2025-10-28 03:21:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07192001-149d-336b-9780-dac0335ca73d | -6.12967 | -42.69439 | 2025-10-28 03:21:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 373e8aff-3c2c-3460-a76e-3b3ea2419812 | -3.57839 | -41.06569 | 2025-10-28 03:21:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e9461eaf-96b6-3d2c-ae6e-7216eb3b470f | -5.65778 | -41.10774 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f1a12a62-7db8-3607-82fb-1d8d2c27f1b2 | -4.45291 | -43.65103 | 2025-10-28 03:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 4f9f4c1d-c139-307c-b7a3-5ad275bac83a | -5.60935 | -42.77638 | 2025-10-28 03:21:00 | NOAA-20 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ca1d9a38-8e17-36b0-90d4-b4e8964d276b | -5.65697 | -41.11231 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4cf7485b-fd6a-3405-bda3-763b633214b2 | -4.51079 | -42.84215 | 2025-10-28 03:21:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b2945e0-3c63-35c0-9618-a13fe11a3d85 | -6.69519 | -42.04776 | 2025-10-28 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 7ecdba20-0d99-367f-af74-d1da4ca8eee8 | -4.50577 | -42.84133 | 2025-10-28 03:21:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37ac46bb-0d58-3119-9923-99b031af3c49 | -5.66416 | -41.14175 | 2025-10-28 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 791ccdd9-8ecf-3014-9054-7e063d2cfeb5 | -5.64063 | -41.10006 | 2025-10-28 03:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 121dcc02-9490-3ad0-8273-f2c3e149de32 | -6.60867 | -42.06235 | 2025-10-28 03:21:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a1e762a7-134a-3107-be1b-2a8d2dddc809 | -8.04564 | -41.11129 | 2025-10-28 03:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README10.md)
