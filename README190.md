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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40506f33-458a-3d07-bc5c-5d03af4cc4ef | -8.9968 | -45.94148 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 6c623f1a-f9a6-37a6-a4bc-21220a16172e | -11.06057 | -45.86055 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| d274fcbf-0490-3abc-a3fa-e07176b30ee1 | -11.18525 | -47.72178 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80cbd08d-b91c-30b1-847a-0995faca2fff | -6.28964 | -44.90224 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3e7d4e81-5bf8-3436-8839-a108d0c4ce69 | -11.52209 | -51.45475 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d6b6482d-7516-3611-9a12-2f37d42a8e38 | -7.89949 | -54.7243 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1bcbc693-0efc-3884-aefe-7dc6716ab815 | -3.77443 | -41.78319 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 54087214-a418-3a72-81a0-d64d5d69ee9c | -5.87263 | -57.67614 | 2026-10-07 16:37:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e3f55103-7943-359c-aca2-ca10d02a1a6d | -15.96262 | -40.70148 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 437fdb94-5ac9-3bb9-af25-a01e7f0cf931 | -6.98063 | -45.54808 | 2026-10-07 16:37:00 | NPP-375 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c0dd6f33-ce25-34f9-83cb-640816ef8b22 | -3.41072 | -39.73903 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 5fb1f1da-0803-307f-95a8-e9311abe6085 | -6.6825 | -45.58143 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 80e074ea-7d5d-3adc-8412-e03a29c8db23 | -5.72519 | -41.73069 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| b1dee691-67b8-358b-9d79-cf83fd8ddf65 | -3.98862 | -45.71095 | 2026-10-07 16:37:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 24.7 |
| cc8ccdae-8f8e-3fb2-9871-7f9cde85bdce | -5.95334 | -55.3455 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f2748d33-8f88-391d-9d11-85fcb907def7 | -9.4441 | -45.82798 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 29.9 |
| ce9e6255-9b57-32bf-9ceb-8fbb48f88375 | -9.79585 | -46.2407 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1e9141bf-374f-36a9-9704-3d104f8b4c5a | -3.85737 | -42.237 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| b3519383-2f4d-3c92-9903-b349a4959d08 | -5.26269 | -48.0345 | 2026-10-07 16:37:00 | NPP-375 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 761d0398-7365-3cc8-a14a-61fbdd69c507 | -15.67024 | -39.70786 | 2026-10-07 16:37:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 7cede745-f2d6-3c7a-b0db-295b76ea1788 | -11.22211 | -46.23426 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 253b8797-8285-3faa-a3d4-b54818e01c7b | -14.44067 | -40.66562 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS DA SERRA | BAHIA | Brasil | 2903953 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 664da77c-4119-3ed4-a865-828c3cf7e5f9 | -5.7265 | -45.15863 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| b41b1102-2a03-3f7e-9272-c4513eb2d738 | -11.13679 | -48.53606 | 2026-10-07 16:37:00 | NPP-375 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a7c4abb3-bb70-3e31-8e70-3a8f0f0cae9d | -6.3326 | -38.85866 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| de991fa7-cdf1-3185-a7a0-95bb94c3e2fd | -8.75907 | -47.57483 | 2026-10-07 16:37:00 | NPP-375 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f0fdbc38-c855-3287-8620-fc3f5349a075 | -5.96855 | -40.92161 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| fc205e62-05b3-3910-bd81-849e056fe243 | -8.81546 | -47.92188 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9663d4fa-158d-3738-90fe-dead79acbf58 | -3.52064 | -43.84196 | 2026-10-07 16:37:00 | NPP-375 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d7a494c3-3e74-3c3b-ac33-a191878ffa00 | -3.73102 | -39.53436 | 2026-10-07 16:37:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 4f4470e1-6bdc-3726-920d-0be2119829db | -16.5605 | -42.33403 | 2026-10-07 16:37:00 | NPP-375 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 29d28baf-e270-34b2-ad21-122c9c82d1bd | -8.43585 | -48.00144 | 2026-10-07 16:37:00 | NPP-375 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 162ad458-4599-36bc-a517-5c761254de2c | -5.55864 | -43.96788 | 2026-10-07 16:37:00 | NPP-375 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 4d641e31-39b0-3687-a74c-f37daee1d11b | -6.37631 | -55.20624 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 0e71552d-d6c1-33b5-930d-8e13c6a4647c | -9.92324 | -44.80704 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 50ed8855-967b-30d1-946a-5e97e5adf76a | -4.84075 | -40.3935 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1dab60be-ec94-30d6-9548-4565466d5d4a | -7.90556 | -54.72374 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 00b9e882-b62b-36ca-9fa0-bb018ddf218a | -9.90804 | -44.7981 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| bf89a34d-b943-37b1-a4f8-59a9866550d2 | -15.95862 | -41.44881 | 2026-10-07 16:37:00 | NPP-375 | CACHOEIRA DE PAJEÚ | MINAS GERAIS | Brasil | 3102704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 34dc6210-f1ea-3036-9b20-6dd00c73e636 | -8.0687 | -55.29631 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 35849342-95c4-3a5a-8ccd-0db9d04456d4 | -15.96541 | -40.69732 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 1d4b06d6-8228-3a54-b3d7-064dd377d79f | -6.19551 | -39.42926 | 2026-10-07 16:37:00 | NPP-375 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fd7479ab-7e36-3342-a902-4017bb63c503 | -4.1771 | -42.04475 | 2026-10-07 16:37:00 | NPP-375 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 46656a94-0074-3349-a876-10d42f88f9df | -5.84432 | -53.56893 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| e125f9d0-1f3b-3bfa-9084-e3596a03c23d | -17.0192 | -45.9185 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e282ed8a-8ae8-3ddd-9d91-b5bcb837c225 | -7.17791 | -44.31899 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 86d408f7-b34f-305e-a52a-7c23da644f29 | -6.85507 | -43.88939 | 2026-10-07 16:37:00 | NPP-375 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5c889eb5-395a-3761-b5b2-b5bccb8dffd1 | -9.81981 | -47.47862 | 2026-10-07 16:37:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7100492e-731c-3c20-960a-0b231cfd1128 | -9.40458 | -36.68061 | 2026-10-07 16:37:00 | NPP-375 | PALMEIRA DOS ÍNDIOS | ALAGOAS | Brasil | 2706307 | 27 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3a3bc1f9-b540-3b9c-8c48-ccae513b1adf | -5.51201 | -42.81281 | 2026-10-07 16:37:00 | NPP-375 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 03eb3401-09c7-3ce1-94ff-afe1d61b9844 | -7.0586 | -46.53446 | 2026-10-07 16:37:00 | NPP-375 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 91d9ed23-604e-35a7-9f9c-4d3b953b3af6 | -9.42187 | -46.33432 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 93343445-3ef5-348b-af1c-b20948fe4a75 | -7.10212 | -45.24425 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| aa15d0a8-c2a7-3740-bdda-6f79f8b68ccb | -9.34647 | -45.43027 | 2026-10-07 16:37:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 0fa2aaea-ed61-3e45-87f6-d3f9169c9f6d | -7.20599 | -55.12159 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 14884155-c8d7-3305-9cfe-403f92d76f1c | -4.18522 | -43.70453 | 2026-10-07 16:37:00 | NPP-375 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b563e3a6-204e-3daf-afc9-60064d96d4d3 | -6.37112 | -42.92562 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 10.7 |
| b9dc6a0a-577d-3110-b245-18f4c0f612a4 | -11.20095 | -49.42843 | 2026-10-07 16:37:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 218c6136-362c-399c-bce0-0bd180fcfbaa | -6.19674 | -57.74723 | 2026-10-07 16:37:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f8af614f-8749-3f85-85e7-2f4079b25814 | -7.08416 | -52.68159 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d5858193-79c6-3620-ae81-db2b3e5804eb | -9.85988 | -46.06498 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ecb120f5-b2e0-3b73-9904-00d41582d60f | -9.27312 | -50.6647 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9be8980f-8044-3208-a4e6-4a77db6a4ae2 | -4.7659 | -42.59612 | 2026-10-07 16:37:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 27.4 |
| 3e44b435-7a12-3e72-a8d3-d3e15bf825f0 | -6.993 | -43.97399 | 2026-10-07 16:37:00 | NPP-375 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 324e2947-f819-3af7-9457-5bb5fac66f7f | -6.9728 | -40.03265 | 2026-10-07 16:37:00 | NPP-375 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 18.3 |
| fe46cf1f-9012-30bc-b9ee-bfa5ded6255f | -6.00183 | -44.12442 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f7a7fcf-3844-39a2-afed-4430bc5a73c8 | -8.11698 | -48.75672 | 2026-10-07 16:37:00 | NPP-375 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7607d4dd-ff20-31fb-b83d-86b75d0035b0 | -3.87989 | -44.1106 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 44392e89-5c6c-3ef9-a77e-42ab4e22b444 | -6.21374 | -52.78926 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 082cb5ef-ad60-3a75-9e45-e2730336fab3 | -6.44157 | -44.83834 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8ea87e45-2703-3b8e-9d3c-e1ed122a33c9 | -6.21942 | -52.83008 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| df64e4db-4fcf-3cf0-b2a7-efa0c29edb4f | -8.20937 | -46.33631 | 2026-10-07 16:37:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 62e8d52f-561b-3da3-a23e-c4e009560ff8 | -4.93556 | -40.54781 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 57.3 |
| 9c7c7bfc-07e7-391f-b723-cc066ee79f1a | -11.35072 | -51.88172 | 2026-10-07 16:37:00 | NPP-375 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c5164db5-519c-3751-8ff8-978c726dd762 | -6.47787 | -51.23467 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 82848342-79e0-3ea4-9ecc-332bc1e43ec2 | -4.57093 | -43.87925 | 2026-10-07 16:37:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 28ac12a2-d63e-3f31-858f-9471aa7ab66c | -6.22973 | -46.0037 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1d34c5a7-093e-3d03-a580-cdca7c20a7d3 | -9.83383 | -44.79116 | 2026-10-07 16:37:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 29dd39fe-36ab-37fd-877a-b12bf189c7ea | -7.18824 | -52.62725 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 227fa51b-66ea-30c3-a9c6-c810da558dca | -6.48464 | -46.6219 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 495562c3-f64e-344a-837f-dd6a5d1fba49 | -16.03667 | -41.33603 | 2026-10-07 16:37:00 | NPP-375 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| dff38f80-fa25-305c-bdd4-1c301588bd20 | -10.35929 | -48.23644 | 2026-10-07 16:37:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8c4ad6c3-b7d1-31a3-9baf-f026a10d5d8f | -4.84227 | -40.40277 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| e67b4ac5-0057-3914-afd2-db8c6cd6f8cd | -6.01162 | -53.51876 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| ba59f138-0c2f-345c-af52-4b3b987e2d3c | -6.18228 | -44.95095 | 2026-10-07 16:37:00 | NPP-375 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecf63792-199b-3bfb-a74a-64132ea5a690 | -17.02834 | -45.91484 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 7f7192b9-b2d2-3041-b748-899e6e754576 | -6.9409 | -56.6508 | 2026-10-07 16:37:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81b188bb-66cc-3a5d-a6b1-6d0ad9e57261 | -4.26783 | -49.98352 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5b62c99a-a9fb-3992-a30a-f8d26fb5f9ff | -7.16917 | -43.71142 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c5918f45-8fc0-345a-a325-013e85999fec | -11.38591 | -46.70494 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 430282be-65ac-365a-9afd-6e7b20541c61 | -4.27615 | -43.01507 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 35cd5850-2d2d-3b58-a865-54e3aded1f61 | -9.87054 | -46.06339 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 125.5 |
| ec41dfa3-5703-3c42-a9ff-c16001fde58f | -8.40638 | -50.11788 | 2026-10-07 16:37:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b11a2e42-1d50-3208-843b-9c268c0d82f8 | -6.34548 | -38.86021 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ceea3f28-fe19-364d-afec-8fd16436bc8b | -6.9854 | -43.21923 | 2026-10-07 16:37:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| f4dbf903-0874-30cd-9847-4c6d37727da4 | -11.39847 | -50.87244 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0d141f99-9748-34fe-824c-aa4c6851183e | -8.96079 | -47.55206 | 2026-10-07 16:37:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d641de3e-5660-3489-845e-3526690bf618 | -6.92287 | -36.46808 | 2026-10-07 16:37:00 | NPP-375 | SÃO VICENTE DO SERIDÓ | PARAÍBA | Brasil | 2515401 | 25 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e0c09873-7b37-3a39-83b5-1c3c6554afd0 | -3.50611 | -41.95201 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| cc1c3b32-2062-37d5-9998-aea2e3b84efb | -5.73091 | -45.16518 | 2026-10-07 16:37:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |


[Clique aqui para ver as próximas entradas](README191.md)
