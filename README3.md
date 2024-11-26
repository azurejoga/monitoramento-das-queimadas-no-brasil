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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31acd6ae-28a2-3520-9e11-30cbcb1b63f7 | -4.41778 | -44.6537 | 2024-11-26 00:30:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 48c3ae24-2364-3b5e-a4db-bb388a399c30 | -3.11622 | -45.08674 | 2024-11-26 00:30:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 54d26290-c686-3438-93d2-298e70d06603 | -3.5025 | -50.46314 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 93ad2a2d-6e0d-3575-873a-37e46729ff0d | -2.5444 | -46.40428 | 2024-11-26 00:30:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9ae18d06-3c19-314c-8eda-ddf56c450e2c | -3.2521 | -45.68303 | 2024-11-26 00:30:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 606a6338-e3d5-3d34-87dc-734f5fc09e53 | -3.71631 | -50.18954 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b7ee83ae-7761-35cd-b476-1091e7202713 | -2.80542 | -53.01408 | 2024-11-26 00:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e460586a-e306-3aaa-96df-e4d50e164d40 | -2.18783 | -45.96959 | 2024-11-26 00:30:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a0c1f771-d135-3e84-80cd-081128dfddc0 | -2.57962 | -45.47612 | 2024-11-26 00:30:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8a6882d5-be2a-3f67-81ae-f238ddab4995 | -4.64407 | -50.67928 | 2024-11-26 00:30:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| f1163b9c-2929-32dc-915d-ed7cc9ef18b3 | -3.15647 | -45.44386 | 2024-11-26 00:30:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d8f78572-b42b-3e05-b85e-e0a4ffe19383 | -1.86521 | -44.76912 | 2024-11-26 00:30:00 | TERRA_M-M | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 27.2 |
| c43759b1-8657-390d-ab7b-e3bab60ca010 | -3.58549 | -50.36492 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 646af592-f756-363e-a23b-57a3c6b587e0 | -3.72499 | -50.1951 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 8a5afd57-02f8-31a8-b948-047816ba7c86 | -2.17976 | -45.59801 | 2024-11-26 00:30:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 14b0a85d-6391-3d0c-beb0-eb568b27f8b0 | -2.5782 | -45.46587 | 2024-11-26 00:30:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d88e52ea-4834-38dc-b1c8-0358d50cd627 | -4.31753 | -47.51748 | 2024-11-26 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b28e19a3-9158-3c14-bd98-b27a0476c349 | -3.07963 | -49.50796 | 2024-11-26 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| d31e8d55-49b6-3809-b398-bfda84c3ddfb | -3.39327 | -44.17056 | 2024-11-26 00:30:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 89bf9ca6-922e-317e-8f31-3596e0d8cb1d | -1.44839 | -47.11539 | 2024-11-26 00:30:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 687f88f6-4d32-3293-ae2a-e7750d82979c | -2.53322 | -45.59441 | 2024-11-26 00:30:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 91a0e68a-1486-34e9-83e0-04a877ee28bf | -2.48975 | -45.422 | 2024-11-26 00:30:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 528fe76d-7f12-37cc-8886-069ab6e5ae09 | -2.59959 | -45.41073 | 2024-11-26 00:30:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 35de2bbe-3cc4-3557-b56f-27f3fbd0f076 | -3.07864 | -49.20584 | 2024-11-26 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 1740bec4-7e73-3730-a415-e2315d6f8233 | -3.84038 | -41.56162 | 2024-11-26 00:30:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 1e49fe11-bd00-3274-aca4-a2384a86b9f1 | -4.5042 | -45.20892 | 2024-11-26 00:30:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| b1c5915f-c517-3e28-ab96-8c09cc8efce3 | -3.18373 | -48.44784 | 2024-11-26 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 221.2 |
| a0163e9b-3615-339c-8d56-b4488979d180 | -4.32182 | -45.88487 | 2024-11-26 00:30:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 02250746-b49b-3d3d-8876-a33bcad603ee | -3.33239 | -44.06322 | 2024-11-26 00:30:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1aa9de29-4cd6-332d-b2c5-52d3997bd1c1 | -2.18933 | -45.98046 | 2024-11-26 00:30:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 17e8df79-14a1-340a-ab8e-30411a64be9d | -2.41791 | -45.63748 | 2024-11-26 00:30:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 1f272c26-ad90-343e-b0e0-8315ea8b5067 | -3.27966 | -50.02022 | 2024-11-26 00:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| e1cec4cc-a58f-34d9-8097-82977a86b76a | -3.17178 | -48.44948 | 2024-11-26 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 9ead5236-c1b4-3f94-b2f4-7c5fc5208746 | -3.33744 | -45.8535 | 2024-11-26 00:30:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7be2e317-8e34-3539-a6da-3b5c9e1d5b5b | -2.98565 | -49.58991 | 2024-11-26 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 378ddc6d-4771-3aeb-83b9-8f0cdb20baaf | -4.42729 | -44.72257 | 2024-11-26 00:30:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 910aff75-f8cc-3c42-a837-cde9fc29956d | -1.93512 | -45.75663 | 2024-11-26 00:30:00 | TERRA_M-M | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a798a02e-589f-3ca9-b881-3d938daa5cea | -3.29996 | -47.01998 | 2024-11-26 00:30:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| aab85cb4-bdaa-3795-9149-d249ddf64795 | -3.29105 | -50.25845 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 8f1c7b5a-d9e9-30b3-a7b3-2797d48cf7dc | -4.50275 | -45.19847 | 2024-11-26 00:30:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| d2d73dad-770b-31b9-9feb-a65b7c530683 | -4.32342 | -45.89638 | 2024-11-26 00:30:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| ff8dbfc2-1df2-34eb-9ccd-a8c7970b8146 | -1.46929 | -47.11251 | 2024-11-26 00:30:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 6b0977ca-f8d1-33bf-bb82-be185fcb63aa | -3.38676 | -44.19029 | 2024-11-26 00:30:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 145bfda5-ba63-3bbd-a102-1de2b6d652fb | -3.2967 | -51.17006 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |
| b3374816-d123-3fb3-ad8a-ff985e8c6fe8 | -3.24091 | -45.67367 | 2024-11-26 00:30:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| db1ef504-0322-3dff-b995-ca1cdaced206 | -2.92411 | -45.16623 | 2024-11-26 00:30:00 | TERRA_M-M | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| b737252f-b76c-35e7-87a9-08e8f3bc65f4 | -2.59817 | -45.40054 | 2024-11-26 00:30:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| dd3ac2ad-fb1b-394a-8cd3-95beea6f8647 | -3.392 | -44.16132 | 2024-11-26 00:30:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 3471d121-bba7-3a7a-8f4b-26d5570bfef7 | -4.31556 | -47.5028 | 2024-11-26 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| fe4a6143-e3e3-3538-b2d0-baaf265f33e2 | -2.92112 | -42.62758 | 2024-11-26 00:30:00 | TERRA_M-M | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| a998d5a4-078d-314f-9ef5-04883220ecc1 | -3.91315 | -42.41097 | 2024-11-26 00:30:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 86.4 |
| b64237ed-38b1-3048-a3b7-ed22f6f0dd2e | -3.66395 | -41.55194 | 2024-11-26 00:30:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 890de507-6df7-3f8d-a685-b547a4961e6d | -2.12688 | -45.32218 | 2024-11-26 00:30:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 2f60a6e3-d55b-3822-b188-2d46b55157ab | -2.33109 | -46.12202 | 2024-11-26 00:30:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80a8c8ea-15e7-30e6-8290-b7c8f130ab9f | -3.92717 | -50.52343 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| f9a4a456-bb31-3225-b890-2a2ef2a1a90b | -3.4634 | -50.8384 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| cc176e55-57b3-3379-bc01-98d692bebd84 | -1.87434 | -44.76783 | 2024-11-26 00:30:00 | TERRA_M-M | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a46dcf08-e864-3f1f-9ba4-95d0446f215a | -3.68638 | -50.22409 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| feb7e2ea-6582-3e95-aa7f-8e2f9b4d7eaf | -3.92457 | -50.53038 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 7dfe1292-ea13-3b2b-8b21-26ed0c6f3f03 | -1.59934 | -47.45685 | 2024-11-26 00:30:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 16.6 |
| d0ea5e19-ab3c-3140-b483-f6b3663ebd03 | -1.82973 | -45.58728 | 2024-11-26 00:30:00 | TERRA_M-M | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 219147c0-9f37-31aa-8afb-f572436ad59c | -3.73023 | -50.18766 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 164c56b6-66ce-3437-97ec-1e48301dc98a | -4.66135 | -47.9432 | 2024-11-26 00:30:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 85bf20f2-59c2-3a1c-ba73-0d6938a6b5e9 | -2.80847 | -53.00738 | 2024-11-26 00:30:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 90763cd1-6c6b-3fa7-b0c9-ab4bc2103293 | -2.92235 | -42.63642 | 2024-11-26 00:30:00 | TERRA_M-M | PAULINO NEVES | MARANHÃO | Brasil | 2108058 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 23612c28-c6df-39d0-a6b4-28b3b84b61cd | -3.60282 | -50.3874 | 2024-11-26 00:30:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 190.1 |
| 23e0c020-8bfa-3ece-9351-f521a3499d60 | -3.39454 | -44.17979 | 2024-11-26 00:30:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 1e450e2f-1cac-3e6d-916a-7cadff49e24f | -2.15285 | -45.57671 | 2024-11-26 00:30:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 6cc77f3a-ac48-3226-8136-b90258e7ea74 | -3.97383 | -48.04515 | 2024-11-26 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 5c53aec2-50e7-302f-8502-505c2774d03d | -3.9784 | -48.05112 | 2024-11-26 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 176.2 |
| 79b86827-7cab-3bd1-85a7-05ac86e803f8 | -3.07605 | -49.18668 | 2024-11-26 00:30:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 7f74d6b6-1d59-3de9-b77b-4bfa533ca45c | -3.2944 | -50.28234 | 2024-11-26 00:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 9938b449-f9fe-3369-896f-8016d8423812 | -3.1414 | -45.0875 | 2024-11-26 00:30:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 73b840ec-f439-3524-be6e-61511251aa4e | -3.14275 | -45.09745 | 2024-11-26 00:30:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 4e43cedc-dd7d-3a80-9b8d-b6a0e035a555 | -3.19568 | -48.4462 | 2024-11-26 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c7bb40cb-6b1f-3b56-beaa-727f82965325 | -2.48027 | -45.42332 | 2024-11-26 00:30:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c577237f-7c3c-350b-9e98-c8d274890fd5 | -1.56698 | -45.68441 | 2024-11-26 00:30:00 | TERRA_M-M | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 51ec6984-e278-3b77-8bb5-ac4b8d58ea7b | -3.38549 | -44.18106 | 2024-11-26 00:30:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 560e735a-81ec-3e2b-a009-222daf428d78 | -3.28593 | -50.27829 | 2024-11-26 00:30:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 82565941-0e25-30e5-9fb5-b0ade3207218 | -3.18143 | -48.43108 | 2024-11-26 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 468.9 |
| 0f934964-174f-32ac-b1ac-c31efa6bd5b8 | -3.1695 | -48.43272 | 2024-11-26 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 28.5 |
| dfa58bfd-b59d-3ef1-b41f-361321c0cbbf | -1.47671 | -47.1179 | 2024-11-26 00:30:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 57647f5d-932e-3b07-a0da-2d21370ef3c2 | -3.90551 | -42.42109 | 2024-11-26 00:30:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 027b956e-46ad-3b1c-b2e8-36c8c740254d | -4.42866 | -44.73246 | 2024-11-26 00:30:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| b749e82d-2566-33f6-a333-f791179c0c6d | -2.92955 | -48.01935 | 2024-11-26 00:30:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 42966b00-80ab-395b-80ae-35e2ec547d44 | -3.38296 | -44.1626 | 2024-11-26 00:30:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 449c79c3-9ee5-3c2f-92e7-a1294af74d64 | -1.60449 | -47.46404 | 2024-11-26 00:30:00 | TERRA_M-M | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 77404037-077b-3668-ac7f-6a0e955be51f | -3.19336 | -48.42942 | 2024-11-26 00:30:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 37.8 |
| b05df269-b9e4-34b9-aab4-79dbc0241f52 | -3.48452 | -48.23095 | 2024-11-26 00:30:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 12d8ebc9-a5bd-332b-a874-d6d35209782f | -3.97589 | -48.06104 | 2024-11-26 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 617.0 |
| 82f3fce4-6c72-338b-beba-180558678345 | -3.84168 | -41.57082 | 2024-11-26 00:30:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e759cc3c-3645-3a8c-8df0-7eacafd24f3a | -3.38422 | -44.17182 | 2024-11-26 00:30:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 4d1ea5e1-bf22-3168-9c71-5e7e1fc8f756 | -2.49116 | -45.43219 | 2024-11-26 00:30:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d05c0df-018e-3af3-ac96-e6a61cf95d32 | -2.53467 | -45.60482 | 2024-11-26 00:30:00 | TERRA_M-M | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 14.7 |
| b6c24b58-cdb9-3754-835f-33a74451afdf | -2.17625 | -45.60497 | 2024-11-26 00:30:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2eff0a1c-6a12-3849-8050-55f00e444db5 | -2.71873 | -46.26213 | 2024-11-26 00:30:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 560414e7-1129-33f3-9f7e-4d1924741cba | -3.91562 | -42.42868 | 2024-11-26 00:30:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 34.9 |
| 99485ef1-3d50-3836-9817-6effc7e78647 | -3.96664 | -48.05248 | 2024-11-26 00:30:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 986fb171-cde8-3af8-8a8f-fb4a2c929804 | -1.77134 | -46.06863 | 2024-11-26 00:30:00 | TERRA_M-M | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 0bed0af4-4a24-35c7-815d-86d8c99bb60a | -1.82395 | -46.29152 | 2024-11-26 00:30:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |


[Clique aqui para ver as próximas entradas](README4.md)
