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

## Dados Diários - Página 350

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86543978-7d03-392a-84ee-57f5463d28a9 | -1.76894 | -47.8884 | 2026-10-08 16:39:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23f4377a-213e-3509-b37a-711084d94c50 | -2.78363 | -57.63911 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 65cece58-bc2f-3850-8191-4e2b89fa1314 | -5.30791 | -45.72441 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 2946abd0-0246-321e-ad28-e76cb1e7cdfd | -6.25435 | -52.8838 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 65fa239d-b949-3bf5-81f0-dfb1dd4b29c3 | -2.5798 | -56.17902 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| abba698a-2a82-3a5e-995b-5b579d274c92 | -3.25798 | -57.87492 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 530802d7-d9e8-33a8-97a3-17f7127397cb | -6.74278 | -55.14372 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 91259714-24b2-3bcc-960e-d47480055103 | -5.45698 | -42.89539 | 2026-10-08 16:39:00 | NOAA-20 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 4ca5b0a3-f29c-3536-bc72-2678464a9db5 | -4.58164 | -38.94867 | 2026-10-08 16:39:00 | NOAA-20 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 11.8 |
| c632e077-bd02-306d-b98c-f479c352e9cd | -5.32649 | -40.89301 | 2026-10-08 16:39:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e278240a-b1c3-33b5-a928-0f5942450fdf | -6.50687 | -55.39962 | 2026-10-08 16:39:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 46c6cbd6-6847-3fec-b2e3-e7ea52965617 | -1.41773 | -55.34723 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d3d5c970-4468-32fe-bf7b-41377a8cb43f | -5.94788 | -45.69281 | 2026-10-08 16:39:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4e324173-ed4b-353c-b6dd-9eb1843eea16 | -3.94371 | -56.02075 | 2026-10-08 16:39:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 6d048308-2228-32b1-a551-d2c5519e990b | -3.79206 | -41.67122 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 14.7 |
| bd817a93-9881-3880-8a1b-aacce4c7537a | -7.18508 | -52.61868 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9e74c99a-2bde-33b6-8188-4264dec71db3 | -6.05034 | -51.73547 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 55c509c9-bc1c-3a3b-afe5-141153fc60be | -3.89024 | -40.98269 | 2026-10-08 16:39:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5c080d06-35db-3b3f-a1bc-4ad80a988b8c | -6.39099 | -52.72242 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| aaac53eb-7408-3194-8753-3df3808ce39d | -3.89703 | -41.59776 | 2026-10-08 16:39:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| f7f3530d-691c-32e3-a03f-5c55db7f490c | -2.0886 | -56.61885 | 2026-10-08 16:39:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b2f081fc-e58d-3216-8a40-075ca3f78f6a | -3.15948 | -50.44108 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 41011ce5-f370-33cc-b053-42a25655f2a2 | -3.50644 | -45.19683 | 2026-10-08 16:39:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 67d3f0ba-5071-311f-86a3-4f6331eff8a4 | -2.82599 | -57.61735 | 2026-10-08 16:39:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 4f09367b-6ec5-33ac-939f-55c4de57b4d4 | -3.17263 | -58.62861 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| ca5a9f4c-b3a3-316b-a076-cc84e4bf7864 | -6.83652 | -52.86867 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7a84aa46-5015-3094-aa75-bc22a3584ea8 | -5.30407 | -45.72146 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3347d2b6-4c84-35e8-ab04-ddf1f367d4af | -4.0608 | -55.32861 | 2026-10-08 16:39:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 8bfda9c5-8d5a-34d0-8f96-505aff0a2bda | -4.96312 | -55.11884 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 694b3853-0d81-32d9-bb6e-795b1bc67961 | -3.1232 | -53.79285 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 46ceea4d-1814-3517-9986-1debd3b78518 | -2.49475 | -56.16672 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8ce07100-d856-3c11-8c96-009a4f25da27 | -3.98781 | -59.3434 | 2026-10-08 16:39:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 33dc206b-1b39-3bb6-964c-ff1def0a9869 | -2.13566 | -54.46099 | 2026-10-08 16:39:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| a764be3c-97d3-3cfa-9008-a928b05cf0c6 | -3.09924 | -53.95676 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 940033e3-92cf-30bf-9c67-1f5bd432c348 | -6.08684 | -49.70901 | 2026-10-08 16:39:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 1e4dd07d-7c4c-3459-a7ac-bbe72ce0ab4d | -3.19528 | -42.96396 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 6d86c6ef-9db2-3974-aed7-d7c4812105bb | -2.52226 | -56.43104 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5d96b27-a9c1-30cb-a6b9-c64645487782 | -4.09651 | -44.13688 | 2026-10-08 16:39:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 24.7 |
| e4c6cbdb-4043-3a82-af80-6af1283dcaec | -3.8272 | -57.16797 | 2026-10-08 16:39:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| c050bd19-0f4b-3f54-9482-6f6e805f8e77 | -5.4175 | -45.86303 | 2026-10-08 16:39:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 4a866409-f406-3fec-a2e4-36ae6db39c77 | -0.71476 | -57.43217 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| aa7b279e-9707-32cd-ba33-077c7e638596 | -1.3344 | -56.40154 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 697c8598-41dd-329f-b1b8-5909dee192e4 | -6.04285 | -53.48837 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 7588adf7-bc9e-3ee0-9704-6e15a5a7c0f3 | -3.77887 | -45.27409 | 2026-10-08 16:39:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d414180a-3c2f-322c-9bc5-80b6aa5b586a | -3.17588 | -54.61138 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| f300dd75-c1db-393b-9367-7a59d75a2280 | -4.67507 | -40.23332 | 2026-10-08 16:39:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6c127441-a3b5-37d4-b924-534d77a611dc | -4.37529 | -43.90383 | 2026-10-08 16:39:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2697f704-029a-38af-83e8-46cc4d2845ff | -3.02094 | -57.87851 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 64d0e473-c3d4-36a4-ac03-6b4e4587b5c1 | -3.51332 | -59.33742 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| e815bd91-f9c4-3ee9-a184-f97dc22efc71 | -3.02704 | -57.87756 | 2026-10-08 16:39:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b93d7020-6c0c-350a-9e41-308b63ea6f71 | -6.03969 | -51.72111 | 2026-10-08 16:39:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8a513ac6-3863-3932-b4b4-743e1b27e679 | -2.50355 | -56.15127 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bc6b653f-6091-3e33-a8b6-a8b3c758e362 | -2.78144 | -54.06955 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 6944b4b9-2d6d-3449-936e-3ddd6b6eacb0 | -4.59111 | -43.17538 | 2026-10-08 16:39:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 880dc4a1-7f26-3628-a369-f3fef0d84f78 | -1.70778 | -55.03099 | 2026-10-08 16:39:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 935ba7ac-ba22-3e77-bd0d-3d753129c632 | -3.01495 | -54.0526 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 25c7d65c-c9dd-3b03-8898-c78f2808aef9 | -3.61809 | -60.32352 | 2026-10-08 16:39:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f2f6032b-71c5-3dfa-bad4-c54793b9be88 | -3.16649 | -50.59186 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 72443088-b5fe-3dcc-9580-a01e0dfd49c7 | -2.99918 | -54.75873 | 2026-10-08 16:39:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8f6a5cac-8959-31c9-bc88-8e9f86b7bd94 | -3.71821 | -45.09397 | 2026-10-08 16:39:00 | NOAA-20 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0182f67d-e3e1-3fd9-b3f0-28ff5b5431c9 | -3.7342 | -39.52698 | 2026-10-08 16:39:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 5d801b91-037d-331a-ae43-134658ed9bc4 | -6.73693 | -55.14103 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 41cb4c54-f9f6-354e-b4d4-cd7179fb8862 | -3.26661 | -42.95755 | 2026-10-08 16:39:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 7bed2057-660d-318b-8ca6-7bec22200bfe | -2.50217 | -56.06742 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ac492b27-39ff-30ad-b3f7-dbaddb56f119 | -3.20246 | -50.5494 | 2026-10-08 16:39:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 998995ca-c4b2-39d4-91da-a13c40e9922a | -3.16481 | -58.63068 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7649db7d-842d-36a5-91bd-66b12a19d6e6 | -2.77673 | -54.07022 | 2026-10-08 16:39:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 7b3737db-b398-3878-9b18-d80e11e492ed | -6.45188 | -53.69266 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 0d3acd9b-afd3-3142-91a8-c883c2334cf8 | -3.31022 | -53.6964 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| c146eced-a830-366b-9b6f-2211131b6e76 | -1.33286 | -52.44679 | 2026-10-08 16:39:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 98508001-1257-3183-97d7-e09f53af1515 | -3.50703 | -43.83479 | 2026-10-08 16:39:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 21dc12da-b4c5-3d25-8ded-ae322372a4b4 | -3.57663 | -58.99507 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 56cff31b-fec7-394b-b258-c15f75e803ce | -2.30973 | -57.98661 | 2026-10-08 16:39:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d646c1ca-4465-36b2-82eb-df35c7a2b26b | 0.53975 | -50.76951 | 2026-10-08 16:39:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 7f0a417c-218f-3947-9b65-28e4448a5ff8 | -3.5635 | -54.66769 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 9fe1a2d1-da6f-341c-b2e8-4b830a1a6c87 | -3.6735 | -54.27372 | 2026-10-08 16:39:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9ea4533f-9d6e-3d6e-9ef7-6f81689a00c7 | -3.22535 | -53.96384 | 2026-10-08 16:39:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 53c8426a-b0a7-3788-9fd0-8210c22cb388 | -2.51952 | -56.2595 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 33e3bcdf-34b8-3e5e-bdd2-a45985684673 | -2.90519 | -56.94879 | 2026-10-08 16:39:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ff7b7f9e-d492-3ef9-ad4a-b88fb582cf4b | 0.38277 | -51.15559 | 2026-10-08 16:39:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 95a33248-fce1-3b3b-838e-12e08216839c | -0.72767 | -57.43256 | 2026-10-08 16:39:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 8902e0e8-22d3-3849-814c-855bd64ee99e | -4.74118 | -54.60869 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.4 |
| f1833386-c8fa-314d-9d44-d973121c6b9b | -7.00303 | -59.11425 | 2026-10-08 16:39:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2cb13284-09ac-3673-b7b6-8b813f4860a6 | -5.68608 | -53.49079 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8e043e00-47bb-30d1-8fac-54d691a9ed5f | -6.17071 | -53.4265 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e9175200-0632-3b8b-aa44-ca2465a1bd47 | -2.08414 | -46.57137 | 2026-10-08 16:39:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 153.1 |
| c249bf39-fb1b-3365-ac9c-79dbba192ea6 | -3.50393 | -59.27202 | 2026-10-08 16:39:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| a43f99a8-1b22-3671-a61c-acc550a7144b | -0.77567 | -49.26618 | 2026-10-08 16:39:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d45a908b-7d32-3552-b030-abbf8b93ce2f | -2.98573 | -54.05948 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 28.7 |
| 240cd7f2-1941-34d7-92e7-48dd781bf55b | -3.44493 | -59.55078 | 2026-10-08 16:39:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 0e9359b4-f7dc-3102-96ea-cabe94d7cc6f | -6.04762 | -53.48772 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d9c99905-3b05-3e0f-a51b-a7b0460d74a3 | -5.08828 | -46.21909 | 2026-10-08 16:39:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1997ac84-e418-32c4-a607-cf71ccb2cf47 | -3.98806 | -43.3892 | 2026-10-08 16:39:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 66e102f1-83f9-33ad-b7b6-d689b4a524e6 | -2.4625 | -56.0595 | 2026-10-08 16:39:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4a972a3e-c28d-375d-8a59-22ecf267569b | -2.95126 | -59.16229 | 2026-10-08 16:39:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a20ce93a-428c-3a23-a809-5bac6d6c4470 | -2.2123 | -56.91969 | 2026-10-08 16:39:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bbe0c91e-e855-3c25-81dc-dbb0b93aeb84 | -5.60633 | -45.54529 | 2026-10-08 16:39:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 5c5ccf01-805b-3b8c-91e9-5c17b61f2bd5 | -2.87666 | -54.21352 | 2026-10-08 16:39:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| b59e8d4c-15e8-3756-9f42-bf48b4e68413 | -1.70093 | -50.38 | 2026-10-08 16:39:00 | NOAA-20 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e7647fa1-d4e7-3111-82c9-bce2c4459089 | -5.85754 | -53.45639 | 2026-10-08 16:39:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |


[Clique aqui para ver as próximas entradas](README351.md)
