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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| be5b0e04-2ae9-36e1-ac76-375382181e06 | -7.82261 | -35.23043 | 2024-12-23 03:14:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b7e27b91-1edc-36be-b96c-3f01cf5a163a | -7.23918 | -37.4383 | 2024-12-23 03:14:00 | NOAA-20 | MÃE D'ÁGUA | PARAÍBA | Brasil | 2508703 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 966abd6e-35b1-362d-8f3f-58fd8be9ecda | -6.96855 | -35.23357 | 2024-12-23 03:14:00 | NOAA-20 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a0180758-7b98-370f-963f-6591b045b085 | -6.05149 | -39.43877 | 2024-12-23 03:14:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 040d7ad4-9a26-336f-b1f1-e1d8243ddc26 | -8.91377 | -35.97786 | 2024-12-23 03:17:00 | NOAA-20 | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 7c98297c-40f6-3e9d-a7b2-31ab4480553b | -17.71289 | -40.24694 | 2024-12-23 03:17:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8f7d40b3-2cb4-3f32-9b27-913bee31f264 | -17.70721 | -40.24889 | 2024-12-23 03:17:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1d5fffde-bf9c-3043-8c41-f21032c1ae90 | -11.57601 | -37.55257 | 2024-12-23 03:17:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 785e803c-51a1-3cbb-bc66-42d42eacde2f | -17.70783 | -40.24586 | 2024-12-23 03:17:00 | NOAA-20 | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c4103cfc-37c9-396c-a010-3d87225f1739 | -10.11403 | -36.42039 | 2024-12-23 03:17:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c05f4f84-7daf-3882-a9c5-cf44f332eb5e | -11.57698 | -37.54976 | 2024-12-23 03:17:00 | NOAA-20 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 79a7b64f-2536-3fe9-9e4f-f55586b73ecb | -9.37616 | -35.65494 | 2024-12-23 03:17:00 | NOAA-20 | BARRA DE SANTO ANTÔNIO | ALAGOAS | Brasil | 2700508 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 37cb2b68-b6e6-3966-8f81-0b8a4dfdbd9f | -10.45575 | -37.12639 | 2024-12-23 03:17:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dcfb327b-554c-3e16-8a0f-6b4e8b80390e | -9.99248 | -36.20746 | 2024-12-23 03:17:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 74f73e7c-9fd9-3a5a-9015-17cf3df94b3a | -16.8534 | -39.23835 | 2024-12-23 03:19:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9d399c46-b8ae-3f69-bf85-2f0e15c86c7d | -16.85824 | -39.23924 | 2024-12-23 03:19:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 08d93ba5-0502-332b-a305-d60e0c37d5e3 | -16.85233 | -39.24376 | 2024-12-23 03:19:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f682952d-c7b7-3cd1-a927-9cdb92218ae2 | -16.85501 | -39.25565 | 2024-12-23 03:19:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1e1561e1-395c-3796-8f8b-197cc2c6e56e | -16.85608 | -39.25019 | 2024-12-23 03:19:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c0e70dba-bbd1-3b50-8230-135a547d4236 | -16.85016 | -39.25477 | 2024-12-23 03:19:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 97aefc39-2103-3039-aa55-0d83c5033b42 | -16.85125 | -39.24925 | 2024-12-23 03:19:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7ae2e524-6a0e-337b-b11d-59c4e684dea9 | -16.85714 | -39.2448 | 2024-12-23 03:19:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.2 |
| 118fb9c4-b9be-3c42-a7da-188b20b3d67e | -5.24186 | -36.18442 | 2024-12-23 04:08:00 | NOAA-21 | GALINHOS | RIO GRANDE DO NORTE | Brasil | 2404101 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1e8ff90-9a4a-3dec-b99d-86e5ee9cf7db | -5.1899 | -43.97411 | 2024-12-23 04:08:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07b1de45-96a9-35be-91c5-87fef435c6d6 | -9.31971 | -36.01727 | 2024-12-23 04:08:00 | NOAA-21 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fa77b75e-9f49-3d44-a84c-2ad0008176c5 | -4.87361 | -37.82305 | 2024-12-23 04:08:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1a0ae0e8-fe2f-3c15-a429-6035470b2eec | -7.9206 | -35.19101 | 2024-12-23 04:08:00 | NOAA-21 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 4d9b813b-0976-358b-a668-b850dd89e5e8 | -1.62968 | -45.84285 | 2024-12-23 04:08:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d1f2b38d-f35f-31e7-aba6-a19f341bbe9c | -2.44103 | -51.79066 | 2024-12-23 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c78ae471-0263-3cff-aef6-a2c737c8fae3 | -3.64218 | -40.4767 | 2024-12-23 04:08:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 33b7c5eb-7147-39e3-b3bf-3b2f35015653 | -4.32787 | -44.19417 | 2024-12-23 04:08:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9e2f19ac-c1f4-3d9b-9f70-1c1e53ff0a9b | -2.44704 | -51.79165 | 2024-12-23 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f911372a-f1f0-32b5-b11c-db3c3ff1b895 | -3.09358 | -46.56751 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79a4770b-2925-3c90-a26f-c4d0893f00a5 | -3.92319 | -46.90714 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 370583d1-cb66-3a1d-a27f-e3c57247498a | -2.63893 | -45.69054 | 2024-12-23 04:08:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a783948-bca7-3701-9f6b-4faf283fca64 | -4.45413 | -45.30858 | 2024-12-23 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45fc11f6-ac40-3cb6-a5a5-f35baa08cb31 | -1.68152 | -47.07745 | 2024-12-23 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 31174555-c8bb-3332-a9f9-f03b6c3581e8 | -3.29548 | -45.60903 | 2024-12-23 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9bb18c1c-1300-37c4-a11d-8eee84d94140 | -6.90664 | -43.53843 | 2024-12-23 04:08:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b6c929fa-118b-3b5b-9a37-c8cf5d22ea4d | -3.98649 | -46.34715 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0abf7495-7332-3ed5-8337-c32f5e055b69 | -3.7976 | -46.85154 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffc64245-4b8b-3c18-bb31-8869c78563e7 | -3.8716 | -48.90097 | 2024-12-23 04:08:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de5b4055-cf64-3302-8a9a-03bfb4573a35 | -4.10637 | -46.82071 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f26c15d4-fcd3-3994-8acd-f9675820b7c9 | -3.87469 | -47.28013 | 2024-12-23 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36e3644e-d9c9-34a1-95d9-f2b093cdf2fc | -4.94254 | -41.34364 | 2024-12-23 04:08:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7d94fe7c-9be5-3057-94da-c19b6d8b4ded | -4.45338 | -45.31321 | 2024-12-23 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0fbfda2-e83d-3eff-8479-34c24e97016b | -3.09736 | -54.5997 | 2024-12-23 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32caa0ec-fe2b-3201-b8e1-8779aec00aa7 | -4.08801 | -46.80148 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5d9bfde-b940-3f7f-b74f-7324a27f2f85 | -1.6666 | -52.06421 | 2024-12-23 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f7709cf-8648-3569-9019-c0b118f558d0 | -4.18136 | -43.65316 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 68c496ec-5cf1-3e75-b12b-e939adcb668d | -3.80165 | -46.85544 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c6045f4-a610-322c-87ed-b1d803863404 | -2.46571 | -45.81226 | 2024-12-23 04:08:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 359275b0-3fa9-3179-aef8-e2f8ceaad924 | -2.79353 | -46.7574 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 048afb17-09c6-3fdb-8749-06040d7fd933 | -5.93159 | -45.49094 | 2024-12-23 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5615337-9ba2-370c-8b3e-d9d220c8c7a1 | -4.2293 | -43.78756 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ba45d7b-a16d-3a68-be76-ccfaba549d0c | -4.15345 | -43.64883 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 951dc505-fd5b-37b9-845d-39dfed1acd66 | -6.93553 | -43.53178 | 2024-12-23 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4d5d18f0-53a6-38c5-8b86-c596ef4c03ab | -5.82145 | -35.48189 | 2024-12-23 04:08:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 69eceaa1-e8f7-30c6-89ca-1297c9e037b8 | -2.56442 | -45.50277 | 2024-12-23 04:08:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6126e517-5322-3dcb-918a-2527f8a3fb19 | -6.93611 | -43.52813 | 2024-12-23 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| a3513b90-11bf-3490-9d9b-b6358658ef9a | -4.70457 | -38.04856 | 2024-12-23 04:08:00 | NOAA-21 | PALHANO | CEARÁ | Brasil | 2310001 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 810839ca-4a97-3a38-a3c0-0aa695f0555e | -4.1797 | -43.64107 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2af35ad1-4b8e-3730-b58c-0ba0a7621979 | -4.00886 | -46.99321 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37f6c46a-b205-30e1-8d41-64cb330c699d | -2.42779 | -48.60006 | 2024-12-23 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e837d6a5-d377-32a6-b612-247e3c212f60 | -4.04509 | -46.21895 | 2024-12-23 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72e9a82c-be6f-361c-9c59-0523099891f7 | -5.44957 | -44.81042 | 2024-12-23 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| eb5d6572-db9b-3ea9-b675-378bc725ac02 | -4.01003 | -46.56108 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd1bdfa3-7413-378e-9836-3c95cc423e5b | -3.02006 | -46.99886 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d13d495e-f6c8-3b45-b807-d10178369b39 | -3.99017 | -46.73532 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce4f0a22-3a3b-3465-9bab-d65d7267a334 | -4.10267 | -46.6332 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3579616b-7b52-3c34-ab5f-9d3f1d12a1f6 | -2.70615 | -45.57045 | 2024-12-23 04:08:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ced564f-57c7-3af5-952d-5a19f0b96e10 | -1.94262 | -45.68847 | 2024-12-23 04:08:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b7f9cb30-629d-3af0-8fe0-2264ec6627bc | -3.8012 | -46.8561 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20abcf47-e76d-3134-9362-131cbddc1fe6 | -4.18606 | -43.64603 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9eb919ac-6738-398c-bc45-85048686beec | -4.15161 | -43.66039 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 537830d7-9433-3c8b-aa0e-f6cc2df872cc | -4.15755 | -43.64551 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8d6579bc-689c-34e5-b017-b723d407cef3 | -4.03231 | -46.79315 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7ff4590-5359-37bf-afae-e3e56fb93448 | -5.4935 | -37.83002 | 2024-12-23 04:08:00 | NOAA-21 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2158151b-f105-3f12-878d-9812feb34782 | -2.6824 | -42.69524 | 2024-12-23 04:08:00 | NOAA-21 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7966c3e8-5f9a-381c-bf92-fab523ca88a4 | -6.93951 | -43.52866 | 2024-12-23 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 52fda847-8acc-3bcc-913b-27c3d8cdc1ab | -4.04786 | -49.76653 | 2024-12-23 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c767eae-5e7d-3285-90eb-8fd40ea01c41 | -1.64078 | -45.85194 | 2024-12-23 04:08:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b8ba750-54ca-3d42-a33f-bcfdda9125fe | -4.18666 | -43.64219 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fd2275df-6ea8-33fd-b442-1b85113772fa | -1.7007 | -52.61233 | 2024-12-23 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f971ba90-e302-3f38-84d9-9c8b5584d4b2 | -4.10326 | -46.62957 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6731d50b-4b6c-332a-909f-3f2ef4f39505 | -4.15694 | -43.64936 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ca4bf2ed-4afe-315d-bf43-c70c1cb940ac | -3.35127 | -47.11204 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2316bc5a-638e-3d52-ab0a-7031ddc63689 | -3.99297 | -46.95839 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8430aaea-d6bc-35ef-8a93-d32b139ca74a | -4.62615 | -43.61513 | 2024-12-23 04:08:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a5a85915-3492-38aa-9081-4445d3172e78 | -4.03137 | -50.06147 | 2024-12-23 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 34cf125b-73c1-360a-aaeb-6b07f84f15f9 | -4.01306 | -46.33786 | 2024-12-23 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 466d2f23-7514-3f7c-83a6-301b7ced1f39 | -4.07838 | -47.10247 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01aa063f-35ae-30b0-82d1-31ef6558d077 | -3.0924 | -46.56775 | 2024-12-23 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bdc7c4b-1134-3371-899c-a9ec806e96ef | -4.18318 | -43.64163 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ba0b992-b960-33e0-b57b-e584df79a781 | -4.0046 | -46.99258 | 2024-12-23 04:08:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c26a4ab0-5811-3397-9f26-5429f887e393 | -3.63682 | -50.26026 | 2024-12-23 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6317763c-4470-373a-a110-235c5fc88ec8 | -2.6412 | -46.97503 | 2024-12-23 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3a4d40b5-3eed-387f-88b8-52169ab520ef | -4.16104 | -43.64603 | 2024-12-23 04:08:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1017d410-b715-36ba-9324-183723472ee4 | -6.93892 | -43.53232 | 2024-12-23 04:08:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efb15dcd-5f51-30d2-9dda-8a49bb81525c | -2.503 | -49.06254 | 2024-12-23 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
