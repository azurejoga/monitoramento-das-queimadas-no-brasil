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
| 4b2feba4-ea3b-325c-b69f-d2bd7e7dbea6 | -2.95265 | -39.99518 | 2025-12-02 04:06:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7833c61a-6b59-3090-9362-8cc0c40eeb81 | -1.13991 | -48.09426 | 2025-12-02 04:06:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 784421a5-4cca-319e-bf6f-00e8a2a1350f | -3.23689 | -45.56742 | 2025-12-02 04:06:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 6d7f0521-2edd-30b8-b3d6-ba5215cbe7fb | -2.44706 | -47.08353 | 2025-12-02 04:06:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5420cfae-8a0b-3c74-8981-d8a41d890499 | -3.54962 | -38.9067 | 2025-12-02 04:06:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cb9d6d00-da6d-33bc-aff3-ceef6c761723 | -2.24239 | -45.4859 | 2025-12-02 04:06:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc95c995-47e8-3720-a241-d0f18ff04c24 | -1.4807 | -45.7914 | 2025-12-02 04:06:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 483f0c1c-33b1-361d-8c56-1f96020c0464 | -3.98145 | -38.42685 | 2025-12-02 04:06:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7daf8e46-8afa-323b-bdfa-863f53d2d0b4 | -8.04577 | -43.10825 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 8892f711-a237-35cf-9d27-692c1bc45987 | -5.33442 | -43.56378 | 2025-12-02 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79542b92-82ee-38f9-9752-3ac4077c50e2 | -9.71052 | -36.25828 | 2025-12-02 04:08:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| e2172280-d16a-3647-9626-56a8f5fde733 | -6.55544 | -43.84738 | 2025-12-02 04:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4689fc3b-260b-327d-b25e-22d3c95c829c | -8.04861 | -43.09052 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 768c3bb8-82ed-37d9-a238-5766a93867f1 | -3.858 | -47.05704 | 2025-12-02 04:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7c43ee53-4ab0-3dba-9e91-1b12d9aa8781 | -5.6231 | -44.89365 | 2025-12-02 04:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f702862-aefa-3f28-9a26-ccbda9950bf9 | -6.9928 | -38.15041 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 29231fa8-6239-30bc-bf32-7b360e1827c1 | -8.05195 | -43.09105 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 191fb5c2-1c12-3620-b408-48e7d995df5b | -4.3779 | -43.14559 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 990d5c20-0615-37c3-8682-c1971525cb3d | -4.38133 | -43.14613 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5675d660-d031-3379-b6b3-12549ea819e1 | -4.68543 | -39.69109 | 2025-12-02 04:08:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d6898d1b-337d-392c-85b7-a1104a5d8fc0 | -8.1643 | -43.2181 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 9f4417cc-d0b5-3779-905c-07d90c3d4124 | -8.0553 | -43.09158 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c563277-779a-375d-8ffc-824c640c3ab2 | -4.01555 | -42.44918 | 2025-12-02 04:08:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1eea81f7-b2aa-393d-8bd4-ad2b1bbd279a | -5.33319 | -43.57135 | 2025-12-02 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b56a5df-6a2a-33e6-bacd-7d115f30fda0 | -5.33035 | -43.56697 | 2025-12-02 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6c924185-9a6b-3b7d-baa7-c27b406e9c44 | -6.68395 | -43.54876 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e812d60-6cd5-3d04-aaf6-19cf8d1598cb | -8.04242 | -43.10771 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 39333f48-0bce-32df-b16a-73ca819a5f24 | -8.04968 | -43.10523 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.0 |
| 097fbaf6-0221-37d8-a2a2-2b73cfd8b204 | -8.04804 | -43.09406 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ecd8b00e-4ed9-399b-aabf-1fde1eca641a | -8.67167 | -44.22573 | 2025-12-02 04:08:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89474bc3-17d6-3b0f-a18f-e9ed60096bf1 | -6.60905 | -43.5783 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cff06583-0c43-39ee-b4e8-813064c432e5 | -4.01498 | -42.45275 | 2025-12-02 04:08:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 11098fe9-5e14-3b6d-a51d-7fbb66019e78 | -8.04691 | -43.10115 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| c3a0c428-6e81-34b6-99fc-61feb535b73c | -5.16651 | -44.80094 | 2025-12-02 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e32fb14-c949-3a9d-b646-7ad5d6194b6c | -8.17043 | -43.22276 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| f56a0d44-392a-32ac-8908-aa19f210d51e | -8.16708 | -43.22222 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| a4e8d98f-674e-371d-a2f1-151209a611d5 | -8.17214 | -43.21204 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 038fed96-ea67-3f19-8752-27aef4f3ae9a | -4.38801 | -43.14602 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b80dcead-2242-340e-9e1b-7ae8fdd13658 | -9.71483 | -36.25898 | 2025-12-02 04:08:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 8cb7c015-45e8-3e7f-9e19-c4c2e72ce1e4 | -3.4565 | -50.00295 | 2025-12-02 04:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c2a5444-32bb-3274-9f70-9d5a2c005d4f | -8.171 | -43.21918 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| c2ad0da9-6643-3794-88ba-37109e4c81b9 | -6.58107 | -43.83588 | 2025-12-02 04:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59024bcf-601a-39e7-a4cb-ae65a4d63bdf | -4.38239 | -40.71233 | 2025-12-02 04:08:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 01cf8061-8059-3dff-abf3-46a4ea478287 | -8.05359 | -43.10222 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.0 |
| 3403d09c-7996-35fa-9bda-7974a3915add | -5.94194 | -45.39901 | 2025-12-02 04:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf28f192-0205-3077-939d-b3529aa94963 | -5.48592 | -45.41243 | 2025-12-02 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 19bdba3f-67e8-3288-b423-ca23471b7812 | -4.38251 | -43.13869 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92aae0b8-fb4f-3ddb-ac95-26a0130927ea | -5.33158 | -43.55943 | 2025-12-02 04:08:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f71dc05-19ca-3ec2-bee3-73e5ffb450a5 | -5.11616 | -43.28689 | 2025-12-02 04:08:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1db913d5-7717-3e2b-90ee-47b20fae1be0 | -4.38519 | -43.14175 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bedfaacd-83e3-3d8c-8200-d53f02cf0fcc | -10.19901 | -42.2164 | 2025-12-02 04:08:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e24a6b0-d355-3dcd-be92-f68627df4cb2 | -7.438 | -42.55173 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9e9a753e-77f3-3b58-bbdf-acff6358beee | -5.17088 | -44.7972 | 2025-12-02 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec6e1ef5-842b-3852-986f-b04a161ee7e2 | -6.24067 | -40.29944 | 2025-12-02 04:08:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 33557889-aac9-3be4-aefb-1dcd39f0a24d | -5.17454 | -44.79784 | 2025-12-02 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4ec338df-54cf-3f6c-b29a-aacf71e143c3 | -4.22316 | -44.31236 | 2025-12-02 04:08:00 | NOAA-20 | ALTO ALEGRE DO MARANHÃO | MARANHÃO | Brasil | 2100436 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4706d3af-986f-3795-bb0d-30dc83422c6c | -10.19026 | -36.35031 | 2025-12-02 04:08:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fbaafbbe-5a7c-3df2-80ef-03309f8b3f35 | -4.05016 | -45.18172 | 2025-12-02 04:08:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41546f2a-9e7c-38fa-8cbc-85d65b647240 | -7.79987 | -37.64581 | 2025-12-02 04:08:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| dc07e543-d28a-3477-8b56-270222fc324a | -8.17157 | -43.21561 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 3450062b-039a-339c-9d27-4d292b862726 | -5.79461 | -43.73696 | 2025-12-02 04:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cfce201-acfc-3951-ac26-610d37b93da2 | -4.37447 | -43.14505 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ec589fd-e30e-32ab-97dc-76e5b728d4e4 | -9.7154 | -36.25484 | 2025-12-02 04:08:00 | NOAA-20 | ANADIA | ALAGOAS | Brasil | 2700201 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| fecd7db6-31c2-380a-a95a-105fad52aefa | -8.05025 | -43.10169 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.0 |
| 9d4c696c-8b51-3f32-8d67-9b9f0c6a202f | -8.03965 | -43.10361 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| de5e804c-be7a-3462-aaf5-9cf2af97f9ea | -4.39083 | -43.1503 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 818dcdc5-e8c7-3707-81bc-683edf59ebc7 | -9.87757 | -40.57052 | 2025-12-02 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 94540c1d-7d14-3c40-9ecc-b8ab054ec562 | -4.38741 | -43.14975 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91b1cbfb-7cd2-34ce-b034-c9e55aa262c6 | -4.43375 | -43.86568 | 2025-12-02 04:08:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4da09a82-09ff-341a-8f06-e360cbd54e34 | -2.69512 | -51.89764 | 2025-12-02 04:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b037fec2-c3fe-38ab-a78d-615e1fee0ade | -7.60445 | -43.04068 | 2025-12-02 04:08:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5892dc6d-5e05-3e7d-8990-e1455daf704a | -4.38535 | -43.14296 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 875936d2-f2ad-3081-a3df-8e33d125fd94 | -7.79473 | -43.18862 | 2025-12-02 04:08:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 82987760-47cd-378b-9f43-4f42c9854f3b | -10.48187 | -36.84735 | 2025-12-02 04:08:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ee9af5ed-4799-3d72-8d5e-94cf8bfc1eb7 | -8.05751 | -43.09921 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0506a6c1-8a34-368c-83f4-861c9835b769 | -8.16765 | -43.21864 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| af6eb165-6702-385f-93c1-74e0aafe94dd | -4.37329 | -43.15249 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b409b60e-31f2-35ff-b365-8b3374fc0155 | -3.14942 | -51.31559 | 2025-12-02 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bca5b80f-b069-3cdb-8dd4-45d57457a5a4 | -8.04022 | -43.10006 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b5cb5939-2e01-38af-9671-833573749196 | -4.37269 | -43.15622 | 2025-12-02 04:08:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73043ef9-8717-35fe-8763-6f4db373432a | -2.96137 | -48.59278 | 2025-12-02 04:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd9be20d-8b90-3e34-96c7-873aeccaad3c | -6.61878 | -43.86551 | 2025-12-02 04:08:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69d7323e-8d5d-3928-aefa-0067a778283e | -9.67807 | -37.31115 | 2025-12-02 04:08:00 | NOAA-20 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d5a00b8f-897c-3dad-8ecb-df239991320a | -7.43911 | -42.54476 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 25a163f5-fca9-3c29-bf84-566601c348cc | -4.68206 | -39.69056 | 2025-12-02 04:08:00 | NOAA-20 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7d0289e7-3362-3d9d-83a9-1840c07feed7 | -6.30815 | -43.81269 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc267cca-196e-3de4-8c29-076362953723 | -3.47477 | -51.36548 | 2025-12-02 04:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d03127a9-4496-3541-b90f-5aab2fafa0b0 | -7.43856 | -42.54824 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9f004c20-7533-36a2-ac57-66708e8f4d58 | -5.5934 | -45.18591 | 2025-12-02 04:08:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 295e5ce4-6d2f-3721-87bc-39428adf7514 | -8.04299 | -43.10415 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 8caed153-b98d-3cf2-99b2-91694c4a896d | -8.04634 | -43.10469 | 2025-12-02 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.7 |
| 57c848d3-fafb-31b2-9c7a-63baeab74aa0 | -2.69434 | -51.9023 | 2025-12-02 04:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dbf91a3-69bd-3b87-99e3-f8f83eb8c1d1 | -7.91085 | -43.79357 | 2025-12-02 04:08:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 233699a5-dd16-3560-b4c5-b84849c0cd90 | -10.48079 | -36.85512 | 2025-12-02 04:08:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| eb2143dc-f0f2-3dc9-bcf9-b7673fb15ca1 | -10.77547 | -44.94243 | 2025-12-02 04:08:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 235c768d-01f4-34c5-a7b2-e45dbb391eff | -6.85005 | -42.31797 | 2025-12-02 04:08:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4a33d4c-1fa5-3b1a-913d-808a3d789ff9 | -5.15622 | -37.68952 | 2025-12-02 04:08:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| adeca93b-aac5-3c56-8c02-e90feb486459 | -9.29995 | -40.3653 | 2025-12-02 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 63035f6f-52d4-30d0-89a9-8214b7b781f2 | -5.33881 | -35.54975 | 2025-12-02 04:08:00 | NOAA-20 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 28be6bad-909c-3ff4-b6d2-ab05df6a2634 | -6.67679 | -43.59334 | 2025-12-02 04:08:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README10.md)
