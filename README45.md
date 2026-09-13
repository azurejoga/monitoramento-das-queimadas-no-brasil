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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fa5c79e-ce49-327f-9342-10a7d865f3db | -3.22268 | -50.59148 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19c3828b-27ae-3f0c-8569-2a9007819b64 | -5.18056 | -49.35246 | 2026-09-13 05:10:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9797ebe6-3d50-345a-b246-b987f3b404de | -8.57521 | -54.56776 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5996e82-c0f6-3a1d-87a0-b204a7d1dd64 | -3.40316 | -48.88941 | 2026-09-13 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc0f703b-80cb-3303-8d9c-ef306cb295e9 | -2.94569 | -50.41289 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 01dc3b08-26a2-31d6-b51b-ad7df2db473d | -6.59162 | -58.84146 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 3c9621f1-f18a-3bbe-affa-f71d08ebc792 | -6.31439 | -59.96397 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd2a37d7-818e-3af1-b5fc-f28aa43d34f3 | -6.36366 | -57.86997 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 37b3e0e7-a304-346a-a1b8-5a998cfc17bd | -6.27744 | -59.92952 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1df1890e-bae4-3265-9430-03fdc171e659 | -5.20139 | -49.33334 | 2026-09-13 05:10:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 71bffa08-8078-38ec-8386-dabf3d11c3ea | -2.96672 | -50.39837 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc1dba13-b1a0-3d8f-bc16-2e1076dd96c2 | -6.60095 | -58.85128 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c4d3e42-1391-3ca5-b44f-39bf78194885 | -2.67619 | -57.53669 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 64d8f2d5-00a2-3dd8-880e-cc51c257a4b6 | -6.31666 | -59.97377 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b7c63b24-8cc8-383b-abdf-f77e435ba945 | -6.30004 | -59.95685 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e075764-8eb8-3f3a-9f42-416c57817346 | -2.96531 | -50.40775 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2805c575-f68d-356b-b359-476bce208e03 | -3.95494 | -47.61634 | 2026-09-13 05:10:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6d69603-3fbf-397e-8bf0-4acccf45b37c | -6.22252 | -51.68647 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95582853-5de7-3dd1-8f68-f8e0bfda75de | -7.86842 | -54.72502 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 449a6de3-2b95-3aa4-b06d-399b0b0ee46f | -2.95604 | -50.39877 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9c12da8-327d-3afd-88ea-6eda3294ea2f | -6.1804 | -57.74588 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9aa6fd44-19d4-3b00-b239-0c376d3d70e7 | -7.86671 | -54.71356 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c141bdb5-6d34-389b-bda9-c978aabeaa5f | -3.40275 | -58.29017 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be1a92af-0efd-32b6-b4eb-ba53a5965460 | -6.76311 | -45.45624 | 2026-09-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78198de5-f55c-3152-8214-b4e2ab2cf2da | -4.66307 | -56.00291 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 778e66b7-8daf-3bab-8ffc-1907b09fe1fa | -3.73001 | -61.76044 | 2026-09-13 05:10:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df97ff36-8f31-3dc7-aba5-58a0f20e2f90 | -5.12133 | -55.96223 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6bc69f6-290f-3ae0-8013-55cde562758c | -4.45777 | -50.15934 | 2026-09-13 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd390bbd-4a7a-30a3-8593-ea6298e9ad13 | -8.53986 | -54.70685 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a34c423-1223-3c05-8357-3ca7adf5cdd6 | -8.11621 | -54.79604 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9278fa22-ff07-3316-869b-9a1eb0011974 | -2.96792 | -50.42677 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af542f0b-fef4-32ee-9ca8-76342308f65f | -6.31363 | -59.96857 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c134d1bc-acf7-3eff-a986-97eb82efbc53 | -3.8767 | -51.18947 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 253fe9b2-cf82-3a15-8a42-6d84bbdd5098 | -6.17157 | -57.71424 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 90a30e22-75f5-3a29-a1bd-ea1469ecf425 | -8.12186 | -54.80437 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b01e658-039e-38e5-8e73-d95d2728b0cb | -6.08427 | -51.75536 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b86f9d1-2768-3ed5-be71-ea77251a365e | -1.73904 | -55.84657 | 2026-09-13 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00481901-2ac1-389f-84ff-69884563b882 | -8.05703 | -54.8427 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d6166a9-784e-3221-9c38-88a7deded690 | -2.66696 | -57.52734 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| de784874-c383-324e-8f62-8395181ce633 | -3.39758 | -59.23156 | 2026-09-13 05:10:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1b9bc1a-fcc4-3d52-a811-70f6c50ca008 | -6.07258 | -57.86909 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef7b8bb0-b9cb-3987-b1b1-74519853e512 | -6.09684 | -49.66281 | 2026-09-13 05:10:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1cc2895-9341-30dd-89a4-10990ba10d5f | -6.12827 | -57.56831 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ed61633-fab1-363d-afd2-d7c96808fa6a | -6.37896 | -58.29805 | 2026-09-13 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 020e1267-783d-3b76-b25c-df285628900d | -8.05254 | -54.84943 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8be9902d-db22-3f29-aa43-31a4d5a31ee9 | -7.8684 | -54.70258 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a90ed74-cb3d-363b-9695-b8dcb406b8b8 | -3.0517 | -51.27124 | 2026-09-13 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cc33070-151b-3b6e-847f-cf5c46b677b5 | -3.21492 | -48.97267 | 2026-09-13 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3e34a8f-bfa7-3c3b-a4e6-3650228e6d90 | -6.31288 | -59.97316 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9708f53e-44a9-3e1a-9d85-24d322f0752c | -2.85153 | -50.47134 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9388f4a8-80ac-322b-b4bc-905330027384 | -8.53645 | -54.70631 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06e1b591-2ae2-33f4-abb0-b0352c5c500c | -2.68132 | -57.54935 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9337ee17-640e-3ecd-b4ce-efc1369124b8 | -6.86167 | -47.42388 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9117c3f3-1a92-3351-9277-f3410b530e42 | -6.67598 | -58.8794 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abdb1500-3cc8-387c-8b66-50673cb2e5a5 | -2.67474 | -57.50103 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bda5b60-aca1-34a6-a3fb-b9f801f78ae6 | -5.98038 | -57.76763 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fd9c0a47-26f3-3093-ba3d-92dc5cca2c7d | -6.68145 | -45.48433 | 2026-09-13 05:10:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0985e511-784f-3ece-b4c7-475172d31136 | -3.7263 | -61.75544 | 2026-09-13 05:10:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e7fde21-d77c-3b63-8134-81f01f2a3d5d | -5.12464 | -55.96275 | 2026-09-13 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1240de66-ac5a-3936-94ca-f73d48de2142 | -8.12129 | -54.80801 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a68922d7-c0e1-3830-a818-7f40c0ca9260 | -6.67953 | -58.87999 | 2026-09-13 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35fd0299-9c1b-3417-a6a5-f11117e925e0 | -7.1339 | -43.75288 | 2026-09-13 05:10:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4479fff6-e74f-38fc-8316-e7531fc21735 | -3.33792 | -53.26825 | 2026-09-13 05:10:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06e2e105-1f96-34db-a300-28b86112f465 | -4.41262 | -54.85907 | 2026-09-13 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a0b003d6-f3d7-31d5-8d6a-95f62bd80bca | -9.37153 | -50.10332 | 2026-09-13 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 235f3882-f3e8-30fd-aeac-fd82ef7eef86 | -7.87179 | -54.70308 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09792ee4-b514-3922-b133-0ace9ba5228b | -1.22332 | -54.12529 | 2026-09-13 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2ff479b1-fc89-35a2-9ba2-8bbd2a0e0d82 | -2.68193 | -57.54551 | 2026-09-13 05:10:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4dbfc430-22db-3c7d-b964-50daabfbcd26 | -5.28396 | -49.01933 | 2026-09-13 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0df9a358-3e5a-3ee4-a60a-3f27a97e3e4b | -2.21424 | -60.08969 | 2026-09-13 05:10:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e1b1863-2004-3128-9cdd-efb3e04b981c | -4.93307 | -47.71373 | 2026-09-13 05:10:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 603ef00c-b190-3c72-9c4f-97dbee70b94d | -8.38296 | -47.53873 | 2026-09-13 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 685cc0cc-c498-3332-92e7-a9d66ef24f3d | -1.19806 | -54.1992 | 2026-09-13 05:10:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0451995b-fdc7-3759-b807-e16e763ce7ae | -1.73571 | -55.84604 | 2026-09-13 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fd95b6ff-516a-327e-8d49-6b3649156dfc | -3.73512 | -61.7569 | 2026-09-13 05:10:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c21fc37-471d-3da5-ba15-3bc82c6f9edd | -7.36784 | -45.36889 | 2026-09-13 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aac78c9c-5c2b-3be8-8131-5b202008840b | -3.33529 | -42.29581 | 2026-09-13 05:10:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d1511d03-8345-3238-8cd9-38eb934c62d2 | -2.82427 | -51.34249 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8714448-0f70-3909-a40b-5537e0941716 | -2.95761 | -50.41474 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34b646d2-eafc-3dcb-b133-43be490b39a6 | -6.79587 | -59.96259 | 2026-09-13 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bc1cfa1-c600-30b4-8283-147fcfb5204f | -6.23133 | -51.69526 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f795e3fb-375f-3eff-a7f3-ed25576de1f2 | -8.02589 | -54.85739 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1361dd4-cdff-33e6-b941-ca72fc5b387b | -3.87359 | -51.18417 | 2026-09-13 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 20c8e2db-2d52-3452-b4b2-7826d92a7676 | -4.4572 | -50.1631 | 2026-09-13 05:10:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1996277-ef4c-3475-b9f0-e826c334d759 | -6.22888 | -51.68518 | 2026-09-13 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 931bcc9e-ca12-3007-8861-9a4c29991a0d | -6.85163 | -47.43312 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50669590-8c60-31dc-ba9b-282b172600f0 | -6.12755 | -57.68077 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ccc70d0-83b4-3b49-a2a6-57cbce75d222 | -2.96002 | -50.3994 | 2026-09-13 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d3930aa6-0df4-347d-b775-92bf58e1bd34 | -8.03901 | -54.84735 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e7b4be13-d79f-3474-b5f0-cdb90789d7b2 | -6.1388 | -57.6977 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98d0c27e-5e0d-304f-b206-762712a456e1 | -6.08747 | -57.64808 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b58706ba-6677-35ae-8b8a-2391cd6c8af5 | -6.85563 | -47.42918 | 2026-09-13 05:10:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc060a06-d3ee-332a-b36f-7106bc46e415 | -6.16977 | -57.72527 | 2026-09-13 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc0cb279-ed14-35b1-8ae6-becfce4250e8 | -3.73582 | -61.75263 | 2026-09-13 05:10:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 31d7a105-91f3-3705-8415-f463a7679113 | -1.72905 | -55.84499 | 2026-09-13 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b7e347f-923f-34c5-bbab-4b0961ddc3f7 | -2.86465 | -49.62727 | 2026-09-13 05:10:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 473f5a9a-ee72-35a8-a26c-5f9b9235bf80 | -4.36043 | -54.77962 | 2026-09-13 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c031bfd-b7cf-3b31-b383-64c763ddabe3 | -8.04577 | -54.84839 | 2026-09-13 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a5a5843-8760-3a36-8db3-6effc5add15a | -3.16213 | -58.64363 | 2026-09-13 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46f57e9d-9ce5-388f-9145-3903c3f33e7e | -8.61062 | -55.22007 | 2026-09-13 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README46.md)
