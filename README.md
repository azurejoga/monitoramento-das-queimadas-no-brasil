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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39c8590a-7573-31b7-85bf-b6c24e57f3ee | -4.155 | -42.006199 | 2025-01-03 00:54:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ac8d9bc8-baf0-3ea0-bb9d-2bdaeef51d57 | -5.6293 | -44.8354 | 2025-01-03 00:54:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 10ff06f6-ba1b-38fb-aa54-8f6fb7b59e08 | -4.1611 | -42.0308 | 2025-01-03 00:54:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2bd77565-fc61-3777-9f70-7c3a87953c55 | -21.8351 | -56.402401 | 2025-01-03 00:54:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 42daa115-7197-3b1f-af49-96962861a946 | -2.5768 | -51.909698 | 2025-01-03 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80d2df49-8d89-361f-9a25-cb1d88604845 | -4.1707 | -42.0284 | 2025-01-03 00:54:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef47ceff-aedd-3e93-bb24-0011482275ef | -2.3681 | -54.645699 | 2025-01-03 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab0fed43-af5a-3404-b8a7-82c196a9a103 | -10.6151 | -44.319 | 2025-01-03 00:54:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e151e8ca-751b-3ea4-938f-04f84bd77ec0 | -3.4836 | -51.189602 | 2025-01-03 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c8dc789-7cdd-3b4c-8317-3404cab03ce5 | -2.8514 | -52.791302 | 2025-01-03 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e94222a-38e5-3ddb-8437-4e480706402a | -2.5752 | -51.902802 | 2025-01-03 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3cd6ad2-b50e-39e1-be04-3e56a617f127 | -4.1768 | -42.052898 | 2025-01-03 00:54:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 15ce5015-ae87-3471-8bc0-c10584350b3d | -2.3583 | -54.6479 | 2025-01-03 00:54:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaab528c-1c22-3cf9-9734-76e7319a0539 | -9.289 | -43.153999 | 2025-01-03 00:54:00 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ea14e85-57f4-301a-b459-b92e8b12bab0 | -3.1133 | -52.0 | 2025-01-03 00:54:00 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e253f9f0-6841-3dea-8dbc-c1b6811b56d6 | -2.518 | -51.922901 | 2025-01-03 00:54:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc1ef25a-fd64-314b-be99-4787bdb7cd9a | -3.4852 | -51.196701 | 2025-01-03 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d59c7666-5580-3e97-a084-2b3c821b2080 | -3.4819 | -51.182499 | 2025-01-03 00:54:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4ff7db9-da40-3a51-8965-efc677df74c8 | -10.6087 | -44.3349 | 2025-01-03 00:54:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8acdb00b-38fb-346b-bd2d-23127394b984 | -2.8545 | -52.804901 | 2025-01-03 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb3f4ca-544a-3eeb-a279-5d21975e198f | -4.1671 | -42.055199 | 2025-01-03 00:54:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 032fa5dc-c275-3196-b546-31692e668172 | -10.6184 | -44.332401 | 2025-01-03 00:54:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 131b4cd9-3a17-3933-be6a-2137d0dcce11 | -10.6054 | -44.321499 | 2025-01-03 00:54:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 639fcdf8-f817-377f-8104-372de3051276 | -2.853 | -52.7981 | 2025-01-03 00:54:00 | METOP-C | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27869087-2569-3f94-a28a-b82535920d0e | -21.825399 | -56.404202 | 2025-01-03 00:54:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| cfe40be8-a0ec-362a-9a93-4e08dbb24185 | -3.1117 | -51.993099 | 2025-01-03 00:54:00 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73a97c94-0236-3310-b92d-da9157299b2b | -21.82824 | -56.41539 | 2025-01-03 01:06:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 2f3f9555-f0d8-3c67-aef1-a623c05ad4ea | -21.82847 | -56.42207 | 2025-01-03 01:06:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 3a4e9784-da9b-3797-ad55-580c254ef37d | -21.82627 | -56.40112 | 2025-01-03 01:06:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e59042bc-6cd4-348f-9bb0-63177fdd1a9a | -3.48638 | -51.18242 | 2025-01-03 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 007c9623-cce8-3966-8431-12b443c894c2 | -10.61728 | -44.34403 | 2025-01-03 01:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 26ae3c89-a4ff-36c8-a978-443154879da4 | -3.48786 | -51.19286 | 2025-01-03 01:09:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 0456f514-d346-3d5d-afc8-3e283a0cd9fd | -9.23995 | -60.344 | 2025-01-03 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 611b01d7-5925-36ee-b3a8-d7122f905ea7 | -10.61302 | -44.31864 | 2025-01-03 01:09:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 2d868d13-c929-3f47-86bc-0a7612e67f90 | -9.24261 | -60.33837 | 2025-01-03 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.9 |
| f6900bd5-2294-3ec0-9f36-454e0e1d339b | -2.57513 | -51.83586 | 2025-01-03 01:11:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d66e638f-6284-317e-b731-ad2cd4648be3 | -2.57686 | -51.91584 | 2025-01-03 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bda80b70-8749-3087-bb82-96cb32394d8a | -2.84912 | -52.80329 | 2025-01-03 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e58c05cf-cc3e-3b8a-b3cf-9c83fb4559c7 | -2.51391 | -51.92131 | 2025-01-03 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| c73e669a-3c3a-3f7f-965f-0a2bf483e63c | -2.84783 | -52.79417 | 2025-01-03 01:11:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e70c3dae-b9c6-3e32-825e-a7a66d9b30f6 | -2.57549 | -51.90604 | 2025-01-03 01:11:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| bef99975-035e-3931-be53-9cd1453ba4b6 | -1.72086 | -53.23564 | 2025-01-03 01:11:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1d2862ef-4dbd-3506-9dff-824ad1c64981 | -21.820101 | -56.4221 | 2025-01-03 01:37:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a5be9c53-d963-386d-a8a4-ffd32dafc861 | -9.2284 | -60.334099 | 2025-01-03 01:37:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 08044f3b-4cd1-3143-b9d3-bbec9dca9e20 | -21.8298 | -56.419201 | 2025-01-03 01:37:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 33b5301f-1aa5-3388-841f-5fbf7afeb790 | -9.66508 | -36.063 | 2025-01-03 02:47:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 23869e33-f57c-3c13-a1f6-e1f2d3f46d97 | -9.86976 | -36.28298 | 2025-01-03 02:47:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.3 |
| b88759f3-7a96-3467-9ce4-26586d70261a | -10.12504 | -36.37159 | 2025-01-03 02:47:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 212323e1-61a3-378b-8966-8b72b7689820 | -9.86822 | -36.29045 | 2025-01-03 02:47:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.3 |
| 7880b966-0e9b-3413-9e34-d2dee63e2850 | -6.75817 | -35.06182 | 2025-01-03 02:47:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 40b956aa-969d-35b1-87a3-91d6768272ed | -9.86936 | -36.28328 | 2025-01-03 02:47:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.6 |
| 9114dbe4-0bdd-3bc6-9c01-93f7929c8b48 | -9.87512 | -36.2924 | 2025-01-03 02:47:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| 1f99889f-90f1-364a-ada6-1c96001d97ea | -9.67222 | -36.06484 | 2025-01-03 02:47:00 | NPP-375D | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4c0b1186-2d98-3bb9-9a24-7bebdb0056ad | -6.75934 | -35.06729 | 2025-01-03 02:47:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 0103b074-e05b-3cd8-b19e-b9cd577b3998 | -9.86787 | -36.29076 | 2025-01-03 02:47:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 27.3 |
| b0716a19-a619-3a84-b65f-16c566631ae2 | -9.86669 | -36.29788 | 2025-01-03 02:47:00 | NPP-375D | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| f0e0a850-5fc1-3f35-b9a9-75c9d3b3d191 | -6.7569 | -35.06858 | 2025-01-03 02:47:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d1dd83d2-1ba6-3c35-b6cf-6679ed832bd2 | -6.76067 | -35.06044 | 2025-01-03 02:47:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5cd8e5b3-7204-383c-bdb9-02fac9516625 | -6.77999 | -35.23256 | 2025-01-03 03:08:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cbad1185-4187-35e9-9919-d97fe90896e6 | -6.99758 | -35.19647 | 2025-01-03 03:08:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c5c7bda4-4e45-3a79-b1dd-cfd1b8f77dbc | -7.08098 | -35.28061 | 2025-01-03 03:08:00 | NOAA-20 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 28a1c4f8-6532-3b6b-a36e-cd97503e7359 | -7.08001 | -35.28611 | 2025-01-03 03:08:00 | NOAA-20 | MARI | PARAÍBA | Brasil | 2509107 | 25 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c1bc9c22-191e-3bc2-b147-fc3ed6e22f6b | -6.90874 | -34.88898 | 2025-01-03 03:08:00 | NOAA-20 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 49e912b5-6928-303c-9c09-b8d2b3bd9511 | -6.77509 | -35.23175 | 2025-01-03 03:08:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e5d8f6be-7527-34a9-9187-edf726edbb67 | -6.90945 | -34.88624 | 2025-01-03 03:08:00 | NOAA-20 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0a4b201b-bc70-371c-a5b1-08015c8b3817 | -3.8574 | -40.46015 | 2025-01-03 03:08:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3441b569-f58c-3af7-9616-4c6789822147 | -3.85865 | -40.45325 | 2025-01-03 03:08:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f06e7bd3-46da-3b84-8291-9d69aa52c63b | -7.47514 | -35.05377 | 2025-01-03 03:08:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 07a4900e-874d-3ccf-a888-149af6252de3 | -6.77019 | -35.23095 | 2025-01-03 03:08:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 75c43589-e187-36af-83ab-91c5787874b9 | -6.77603 | -35.22637 | 2025-01-03 03:08:00 | NOAA-20 | ITAPOROROCA | PARAÍBA | Brasil | 2507101 | 25 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0e169eb8-a9ab-3327-818d-2aa69198b8c3 | -6.75583 | -35.06614 | 2025-01-03 03:08:00 | NOAA-20 | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 976b15a6-c103-39ae-9662-8af7670318b6 | -12.18442 | -41.36835 | 2025-01-03 03:10:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 16.6 |
| a2fb058b-ea42-394a-a257-a759cf98fcfb | -8.39465 | -36.80891 | 2025-01-03 03:10:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3693c6ab-e1db-38f2-a799-2bee3cb65d66 | -10.09999 | -36.34386 | 2025-01-03 03:10:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8062bde1-a229-39c0-88fb-f5e66ac7c620 | -11.01083 | -40.86784 | 2025-01-03 03:10:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 048c146a-1cbd-3b16-bdb0-55d6690ea55d | -9.66593 | -36.06571 | 2025-01-03 03:10:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| b19ed2c4-1d88-3f1a-b181-8aa03cd833b8 | -8.39931 | -36.81327 | 2025-01-03 03:10:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 576aff51-15c0-3300-bf85-258363fe2467 | -10.29248 | -37.53771 | 2025-01-03 03:10:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8fd72953-95dd-3016-bf7c-4582d23e1a23 | -10.78833 | -37.25409 | 2025-01-03 03:10:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8424cfa4-e6da-362d-8684-64082637598e | -9.87266 | -36.28873 | 2025-01-03 03:10:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| f8bdce26-cd9b-3b21-8cde-2fadfbdb828f | -10.78893 | -37.25084 | 2025-01-03 03:10:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a75b599b-4065-341c-b112-e52dc04b87d8 | -8.40065 | -36.81346 | 2025-01-03 03:10:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2d02b09f-8acc-3edf-9e00-8fc8fad400f4 | -12.18567 | -41.3624 | 2025-01-03 03:10:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 38.4 |
| a9737b7b-4037-3190-a471-3eaa622b7ca3 | -12.18011 | -41.36538 | 2025-01-03 03:10:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| a189a940-8900-345a-970e-06434a5c7003 | -8.39597 | -36.8091 | 2025-01-03 03:10:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dfe9384c-5e37-36f4-84df-af7cc1ebd000 | -10.73448 | -36.98908 | 2025-01-03 03:10:00 | NOAA-20 | SANTO AMARO DAS BROTAS | SERGIPE | Brasil | 2806602 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 55fd3d68-2203-3b1c-b13b-4527417d74ae | -12.18126 | -41.35966 | 2025-01-03 03:10:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 78c67c33-0d4a-35b5-99cc-12cc8bda999d | -10.29185 | -37.54111 | 2025-01-03 03:10:00 | NOAA-20 | NOSSA SENHORA APARECIDA | SERGIPE | Brasil | 2804458 | 28 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dbd0437b-bc53-3a18-8f18-58ef8e990184 | -8.39993 | -36.80995 | 2025-01-03 03:10:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2d1fd9dc-5d85-3081-9036-389904b034e1 | -9.86769 | -36.28777 | 2025-01-03 03:10:00 | NOAA-20 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| dc755735-e732-318f-b362-91effad1bab0 | -8.39404 | -36.81222 | 2025-01-03 03:10:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9b4b9320-62b7-3e04-94af-6edfdf7497a9 | -10.79416 | -37.2518 | 2025-01-03 03:10:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b7f94b49-73c9-32c5-a014-b25f2a9ea21b | -9.34218 | -35.97669 | 2025-01-03 03:10:00 | NOAA-20 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f5ea9482-2bba-31c3-a085-716abbfb2568 | -10.98205 | -40.47677 | 2025-01-03 03:10:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 79f9a86d-42a6-3dc5-9944-c215d248c282 | -10.79356 | -37.25503 | 2025-01-03 03:10:00 | NOAA-20 | LARANJEIRAS | SERGIPE | Brasil | 2803609 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| abdac745-d6a2-381d-a312-31caaeb9ed26 | -10.98936 | -40.47334 | 2025-01-03 03:10:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a7ec87cd-b414-3159-bbdb-b25019d64c27 | -8.39538 | -36.81242 | 2025-01-03 03:10:00 | NOAA-20 | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 385186a5-74ce-3edd-811a-33cca546aaf2 | -9.66695 | -36.06011 | 2025-01-03 03:10:00 | NOAA-20 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 61425fca-ed41-301a-9218-5ccaca4dd7f5 | -15.64559 | -39.19408 | 2025-01-03 03:12:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1fb49629-2e47-3b6f-8b30-74e5a5e1a7c2 | -1.6202 | -46.20738 | 2025-01-03 03:59:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README2.md)
