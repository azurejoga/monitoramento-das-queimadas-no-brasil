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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 50ab79ec-6b6a-3448-b738-61ed3d463ce0 | -3.4478 | -50.5559 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8a988edf-27d1-3d53-ad3e-b2b6a0d38e41 | -6.30232 | -43.78837 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f98e13b2-8c99-3710-8859-d84b0438ea3e | -4.71729 | -47.15551 | 2025-11-26 04:21:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2fa0841-f07a-3bbc-9467-ea8d9813ce21 | -4.15564 | -43.72388 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5aaa8360-3625-3c4e-aefd-6beff1f4ee30 | -3.47499 | -43.42936 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69353392-d04d-3b27-9303-554c76023bcf | -4.78699 | -48.28327 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95cf884f-a118-3a49-9aa2-b1dadc989ae1 | -3.22227 | -50.57405 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ea722ad-4099-3774-af54-60899707cb4d | -8.06784 | -43.1295 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bd0f45d6-5690-3709-83ec-88f3fcbfbac1 | -3.47776 | -43.43334 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae225e41-4cc1-3950-a977-b5696e5987ab | -4.27055 | -45.12515 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 951d35a0-022e-3a26-afe2-a4d60f9e17a3 | -4.56275 | -43.29491 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d1e4142f-c93d-3554-ade6-8c1443162720 | -4.22009 | -45.52863 | 2025-11-26 04:21:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bedfeb8c-333a-3637-bf9b-319f8d661b50 | -4.17605 | -43.72353 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0be175ce-2bb6-39d0-9983-96e41dd33359 | -4.96913 | -43.86544 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| edf5f1eb-ad3a-3174-b1dc-5040b4c45f86 | -10.00879 | -42.33757 | 2025-11-26 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2cd61f83-ce39-3852-8467-47da21171ded | -3.60199 | -40.95121 | 2025-11-26 04:21:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6d8bb1fb-e4ba-3eb5-b357-fafab563f619 | -2.86592 | -51.79192 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f060eb5b-5e3a-3a6d-90ac-2ac5968b8332 | -6.6871 | -42.47956 | 2025-11-26 04:21:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| cfb2aaa6-775d-39c2-b9d9-fe0539da6d60 | -5.60212 | -35.63592 | 2025-11-26 04:21:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 26400c7f-9bcb-3cd9-a23b-2fcf16da474d | -4.55552 | -43.29739 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9345c8f-9526-3fe2-9c88-2034bd5197c1 | -4.59775 | -44.41149 | 2025-11-26 04:21:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1284c034-d411-3ea8-9a25-a73ead6abfa5 | -2.88767 | -51.81227 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 59ce565a-0639-3c99-b2d3-f189c6f8b37a | -2.92478 | -48.22183 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e4516cfa-f8eb-3722-8896-23f8c7b874f4 | -4.1766 | -43.72007 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 018e1c21-7c85-3c45-b536-096fd08d699b | -4.17969 | -48.63905 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39e620b7-0d5e-3c5c-9fae-7e0a7ae84049 | -7.68563 | -43.10941 | 2025-11-26 04:21:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e8984a8b-db37-34f8-a164-d706d693acf4 | -5.28245 | -43.64378 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9ce011a9-c062-36f3-9905-056b085f0a69 | -2.8819 | -51.81689 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 80ebd837-13c3-3604-9431-9656e281ce2b | -4.16226 | -43.72492 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| da8ca2c5-561f-39b3-b288-65517d3e8289 | -6.80095 | -41.71973 | 2025-11-26 04:21:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eaca5278-e638-39ee-997d-b6056b86bed1 | -8.0547 | -43.1466 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 45f8879c-598f-31eb-a933-da06d5d9c889 | -2.49253 | -47.82286 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b64f04bb-5c28-3ed5-bd1b-ed95d818d688 | -5.42158 | -43.05245 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9810d8d-bd2c-313f-ae45-a26c09430227 | -3.75413 | -46.16318 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b134f35e-1169-3f0c-8c42-4e05be936ac3 | -3.41789 | -46.96754 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 001b75e0-39ad-3a32-8407-18ea0a167b1d | -4.96004 | -42.74867 | 2025-11-26 04:21:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e30104b7-920b-3dcd-bcaa-724a4774588a | -4.25336 | -45.12602 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d993e0ed-4129-3a7b-9711-c39783303e2a | -2.75113 | -47.75753 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb86ac70-8c7e-3f44-b40f-5a26a3eee61e | -4.26334 | -45.12759 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ccf926f1-1e5e-3419-b459-3cb052a5579c | -6.57647 | -47.89219 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c264eaf8-8afa-342d-8216-b871c7e92602 | -8.065 | -43.1022 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 86999bc4-d2b3-3b53-8c56-2a0879167a53 | -3.28582 | -42.18063 | 2025-11-26 04:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 561ad3b8-c4fb-3ea5-a551-f12b2f6d68e4 | -3.21855 | -50.5689 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f71442f4-93d1-3141-95f9-c2a1dd14caad | -3.22212 | -50.58646 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ee229ce5-bbea-369c-a1ff-4866e5c7a904 | -3.67405 | -44.17044 | 2025-11-26 04:21:00 | NOAA-20 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| de467704-24f5-3a37-956b-add25d22963a | -3.35746 | -50.30375 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| efe85046-3158-3255-93d3-05099599396f | -8.05413 | -43.1274 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| 8b05f5f9-c15d-3679-9236-0818f2315a5a | -3.4911 | -44.51176 | 2025-11-26 04:21:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9570a13-c651-3d1d-9a44-d0c742d7acf5 | -3.68407 | -43.56869 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37850c63-5641-3dd9-b371-cb2ebcbd254d | -6.56433 | -47.89881 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cb70dd4-2bdd-355e-b2a7-08c7e5fb3d10 | -4.41545 | -42.91322 | 2025-11-26 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8fcf4c70-810d-330a-a2e2-e4b6e7ad67d9 | -6.06242 | -43.25669 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c255c450-724e-3c6a-a759-7c997e4b890f | -8.04156 | -43.11779 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2853c5d5-d8cd-3c4a-ade6-edbebadc17fb | -2.69637 | -49.51494 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37d35c71-f0c2-3321-a0ff-0a3b25a781f3 | -6.31177 | -43.79341 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2fea9e45-6d48-3cae-87bc-f133d8edae6f | -4.7873 | -48.28623 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 298d0c3a-45f1-37a4-94e1-29acd47bb39b | -6.6883 | -42.47189 | 2025-11-26 04:21:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bd23f5dd-f499-3f23-944b-84926de57b87 | -4.57737 | -50.64989 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea85f695-be73-381b-88fc-80b875c757ef | -4.55831 | -43.30143 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a6e6cdd-c9d8-338a-ad58-3b40d3b73607 | -4.71374 | -47.15495 | 2025-11-26 04:21:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15ba43fc-cfd2-3905-8374-c1f319721ff3 | -4.83028 | -43.81913 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1643d38c-69ce-37e4-872e-3bdeae2901b0 | -3.67013 | -38.80964 | 2025-11-26 04:21:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6dd187e-7daa-3196-83a9-ca778213006f | -2.4192 | -48.59515 | 2025-11-26 04:21:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c4d93fb9-bd9c-3e47-8ab7-e5a8a61e19c4 | -7.19607 | -45.91745 | 2025-11-26 04:21:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1f201df-7141-343a-a52b-da263717ac48 | -2.76118 | -45.34744 | 2025-11-26 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e7d6d88-eba0-36a4-a8ba-0d412fb12814 | -2.72481 | -49.79147 | 2025-11-26 04:21:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a0c1f16-41d0-32dd-a827-2237eb05ba03 | -8.0627 | -43.11721 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 9d4b64a1-a6d7-3e96-9d50-03ea58abd384 | -5.28633 | -43.6408 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| dc9986fa-0050-3ce2-8302-aa199aa8f896 | -2.86273 | -42.44057 | 2025-11-26 04:21:00 | NOAA-20 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1dd71523-bb97-3725-bb26-e2d7c9711b95 | -5.03355 | -49.50486 | 2025-11-26 04:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36b53100-c53c-33f2-bd91-21822d6ec2b1 | -4.25725 | -45.12305 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca873282-77c6-3e38-bf1a-3dd355d2a142 | -3.4513 | -50.55452 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9f04a777-0637-3cb2-a545-a1289a56a3b0 | -6.95468 | -39.1395 | 2025-11-26 04:21:00 | NOAA-20 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 535db654-0964-363a-8084-b0a732e440f8 | -2.94592 | -51.57245 | 2025-11-26 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a24950-5103-3531-bdb7-26284106ec02 | -6.56952 | -43.79698 | 2025-11-26 04:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cdf85b7-3fcd-38ed-b093-fbd608758184 | -3.45648 | -50.55077 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 957468e3-f985-31c2-a483-4a9438c4bf09 | -3.25756 | -51.17771 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8fd98952-54b5-3a74-9e54-76005bb64f11 | -6.8095 | -38.57061 | 2025-11-26 04:21:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a70c3c9b-613c-3008-a74d-fa8c1b0627b1 | -4.27332 | -45.12917 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04032044-ed13-3248-bab4-fe93c6f32971 | -2.85331 | -45.23392 | 2025-11-26 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d7bfa7f-021b-3cf8-820e-65e5195c5e6d | -2.97508 | -47.73925 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75012e11-251f-3f64-aa4a-048c362828f1 | -7.56417 | -45.86847 | 2025-11-26 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a477001b-7cb2-3f6f-8067-6a37b9816e87 | -3.98423 | -49.28853 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0e20fb7-8704-3dfe-b0f0-71446d0f93f0 | -8.04899 | -43.1151 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| a48dbd64-809e-32aa-ad83-34d7979da756 | -7.26632 | -39.6699 | 2025-11-26 04:21:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ed3176c7-3fe8-328b-a341-5cfaa62b017f | -7.00869 | -45.17223 | 2025-11-26 04:21:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a77e9fb1-2fcb-3680-bac7-35b0a5c35d50 | -2.74611 | -47.13636 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f24b39e0-3049-3d3a-b3aa-7649160a5f78 | -2.48876 | -47.82227 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a222b4ac-47b5-3cc3-be68-8ad23d8793e1 | -4.16592 | -41.61166 | 2025-11-26 04:21:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 89ed0a5b-efcc-3f59-b6e0-cebc1b0afee4 | -4.27443 | -45.12218 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 50171a36-2137-3da8-88c8-6af26da32f63 | -5.42102 | -43.05606 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3636ce37-e991-386c-bac2-44a3028ae173 | -4.25669 | -45.12654 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 21068660-efe8-3965-8b0e-35c777637a60 | -8.07071 | -43.11076 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c0392d23-809c-33d7-8391-361b98379d52 | -6.5133 | -44.00376 | 2025-11-26 04:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1c6ba8ed-b547-3f7d-9129-ef9f8ab457bc | -3.46836 | -43.42833 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15505bad-2d29-3e3f-9885-a87b60c1361b | -4.72281 | -46.46674 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52301ef-c1f9-3514-bab3-a3658228921b | -3.47113 | -43.43231 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a742e98a-728c-3b5c-a405-49808140b2b5 | -3.90252 | -47.75135 | 2025-11-26 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df7477b5-a7e4-323c-8d79-5ef8bd6323d1 | -4.26223 | -45.13458 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 696647e5-586b-3b72-ac75-b807d86840cd | -4.94154 | -44.7094 | 2025-11-26 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
