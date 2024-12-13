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
| 0db71c44-4a9d-3e5c-bf1b-4932c243e2cb | -7.86154 | -35.20958 | 2024-12-13 03:02:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8ac07ae9-e0c8-3b7f-9713-24bad9db123a | -5.44966 | -36.87735 | 2024-12-13 03:02:00 | NOAA-20 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ffeb1f1e-ec67-3930-80d6-842758b93c8e | -7.75372 | -35.14759 | 2024-12-13 03:02:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7623acb1-e655-3d71-832a-f0388f12b347 | -7.77643 | -34.95777 | 2024-12-13 03:02:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 68d8ccea-af6f-3f43-8a92-43a0716d061e | -10.19723 | -36.37743 | 2024-12-13 03:02:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5693626c-9851-3478-83e9-43dbea0bd87d | -7.77703 | -34.95441 | 2024-12-13 03:02:00 | NOAA-20 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| da413828-2daf-3c95-bf2f-6974bd820715 | -7.34757 | -34.8504 | 2024-12-13 03:02:00 | NOAA-20 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| cd3255ae-595c-35bb-b4c5-b0d265dba2e0 | -7.69979 | -35.26244 | 2024-12-13 03:02:00 | NOAA-20 | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 632b3785-4755-357d-9acb-70b4fe5c4193 | -7.85896 | -35.20649 | 2024-12-13 03:02:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7764469b-c55c-3b54-8e68-69795f1e6428 | -9.47124 | -37.07531 | 2024-12-13 03:02:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ed7ed01c-d27a-3f60-a7fe-d37758fe5cff | -4.71985 | -37.36699 | 2024-12-13 03:02:00 | NOAA-20 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6bb84d76-a120-322d-a385-97c7e2c3bf05 | -7.20539 | -38.91331 | 2024-12-13 03:02:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d6107d5c-d02c-3115-a1f0-5ed47cc7c67b | -10.19793 | -36.37373 | 2024-12-13 03:02:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 86d94807-517f-3a9a-9d9b-f9bcecb87029 | -7.20414 | -38.91983 | 2024-12-13 03:02:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dc1aed27-9c44-3776-8e06-b94287eac5a3 | -7.50088 | -35.45343 | 2024-12-13 03:02:00 | NOAA-20 | MACAPARANA | PERNAMBUCO | Brasil | 2609006 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| db42b68e-906c-39bf-b647-9079220d4c12 | -10.20281 | -36.37847 | 2024-12-13 03:02:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ea44449b-1fd2-3690-93ac-d9280a1807b2 | -7.3476 | -35.23403 | 2024-12-13 03:02:00 | NOAA-20 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 33511766-bc7f-3193-bdba-f53824fd4d18 | -9.4721 | -37.07085 | 2024-12-13 03:02:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d23da6ac-8cb2-396a-978d-0abd55d4c045 | -9.46819 | -37.07093 | 2024-12-13 03:02:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 777fc196-c995-3c9f-8437-220ceebd844e | -2.4923 | -51.8233 | 2024-12-13 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 2c84b500-1c61-3d76-a265-ea8d32e3fc4c | -6.9349 | -43.4934 | 2024-12-13 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 266c4db7-2726-37e8-852f-6ce94c7870b5 | -6.9346 | -43.5168 | 2024-12-13 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 301.6 |
| c048d297-2bc9-3d1c-9a49-9a51eebbc43a | -13.6933 | -54.7555 | 2024-12-13 03:10:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 9b002b44-3411-31eb-a724-a44dd1dd7fe6 | -6.9158 | -43.5185 | 2024-12-13 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 306.4 |
| b69f4999-3dc7-306c-94b2-dbb18718e624 | -5.211 | -43.2833 | 2024-12-13 03:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 123.4 |
| a6ba2d57-b041-31b6-b90f-e185090a0258 | -11.2148 | -53.833 | 2024-12-13 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 2459a5a2-e4b7-3a28-ad5b-17fb454ef93f | -11.1959 | -53.8348 | 2024-12-13 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| dac66ac8-48e5-3271-aea3-a04b93e8ed4e | -11.2151 | -53.8125 | 2024-12-13 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| e1d80f04-bb63-3ba8-8de3-5b4fbe40b00f | -2.4923 | -51.8027 | 2024-12-13 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.9 |
| 391bdc85-2929-3bcd-833a-12f2c95061a5 | -11.1962 | -53.8142 | 2024-12-13 03:10:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.9 |
| c9bbbd90-9133-3c19-920c-72b24e2042c0 | -6.9156 | -43.5418 | 2024-12-13 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 225.9 |
| df2fe73b-97b7-357c-bdba-7c36ceea9b44 | -2.5108 | -51.8023 | 2024-12-13 03:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.3 |
| 37ccd1dc-9369-398b-97ad-7c1f55dcf98a | -6.9344 | -43.5401 | 2024-12-13 03:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 201.7 |
| bb57e3a3-24c1-3196-b782-e5678620cdc7 | -5.2108 | -43.3067 | 2024-12-13 03:10:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 89da48cf-1efa-3b66-9fcd-ea235b122cd2 | -3.2686 | -46.9142 | 2024-12-13 03:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| df14ee2c-6cd2-319a-9b3a-b4aebf8bbfe8 | -11.2151 | -53.8125 | 2024-12-13 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 219b2b11-f704-3cb5-b2e1-6c2fbe05c619 | -5.2108 | -43.3067 | 2024-12-13 03:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| 470cce96-4adf-3cee-a758-9139c59b8c92 | -11.2148 | -53.833 | 2024-12-13 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 85a72c7c-7780-368e-b56c-75797f46cdee | -2.2296 | -53.7228 | 2024-12-13 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b3c0e821-84f4-3e34-8f32-26e145d57976 | -6.9344 | -43.5401 | 2024-12-13 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 230.2 |
| 32ebb7b5-738a-3866-ae6a-858ef9699484 | -5.211 | -43.2833 | 2024-12-13 03:20:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 4330d051-42ae-37b7-99f8-ff32e04d9238 | -6.9346 | -43.5168 | 2024-12-13 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 309.9 |
| b1a2a604-602e-3cc7-b335-aa4cd15611f3 | -6.9156 | -43.5418 | 2024-12-13 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 258.5 |
| b534d1bd-66a4-34f4-a17b-e2bd61b194b7 | -2.5108 | -51.8023 | 2024-12-13 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 100.0 |
| 267a7629-81b5-3cc2-899c-8e6919b11ab5 | -11.1962 | -53.8142 | 2024-12-13 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| ef42378d-cc29-33e5-aa1c-b573aa6322b9 | -11.1959 | -53.8348 | 2024-12-13 03:20:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 129b6748-a279-3f27-b2f0-1fba95fa32b0 | -6.9161 | -43.4952 | 2024-12-13 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| ef0d6464-6a21-3bd1-bac8-9e96dfb1ce57 | -2.4923 | -51.8233 | 2024-12-13 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 548081c6-c1db-3f44-89e5-65651c2c8690 | -6.9158 | -43.5185 | 2024-12-13 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 309.8 |
| 2b7eded9-94c7-3079-8a8c-2f8d03280918 | -2.5107 | -51.8228 | 2024-12-13 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| b7f97213-2576-3082-aa59-db31417c276e | -2.4923 | -51.8027 | 2024-12-13 03:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 111.8 |
| ce7ad587-0cf1-3099-b711-7e39502f713e | -3.2686 | -46.9142 | 2024-12-13 03:20:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1a61bd3a-2f73-377e-abe5-d4f5531307ae | -6.9349 | -43.4934 | 2024-12-13 03:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 4cf99152-5515-34aa-96ca-8eb0e052c56c | -2.8196 | -53.0629 | 2024-12-13 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 14b913ba-8258-3444-9597-0d9957bd469d | -6.9346 | -43.5168 | 2024-12-13 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 251.4 |
| 9bc580ac-3a0e-39c6-857b-710cbbfcc67c | -11.1962 | -53.8142 | 2024-12-13 03:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| cd3a97e1-3fa9-3631-b8df-d07e95f5a8e3 | -2.5108 | -51.8023 | 2024-12-13 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 64832ebd-49a9-38ac-864c-63b06a01cc58 | -5.2298 | -43.282 | 2024-12-13 03:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 7d7805f4-52e8-31c0-94fd-e3b34fcd3998 | -6.9344 | -43.5401 | 2024-12-13 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 183.5 |
| 8f33558d-f515-3ea1-9c1d-fc4854d9b147 | -2.4923 | -51.8027 | 2024-12-13 03:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| ecf5a27e-7f6f-3db5-b717-59e95226946f | -5.2108 | -43.3067 | 2024-12-13 03:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 46a61631-1517-32ca-ab63-6a7bf54ee0a6 | -11.2148 | -53.833 | 2024-12-13 03:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f56ca2ac-f0b3-3c9f-8121-ff4ab652c61c | -11.2151 | -53.8125 | 2024-12-13 03:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 4b525d31-6b95-34fc-a940-9b3a7a294f36 | -5.211 | -43.2833 | 2024-12-13 03:30:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| a9ad673c-fce5-3a21-8797-86b84d0d0822 | -11.1959 | -53.8348 | 2024-12-13 03:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c5d8d427-37fd-3751-9748-4428f3b211d2 | -6.9349 | -43.4934 | 2024-12-13 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| e52d9edd-7aa9-34fa-add9-cfe0b3f565c6 | -6.9156 | -43.5418 | 2024-12-13 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 339.7 |
| c28ce41e-3e95-3cce-9191-1fb1a01be53c | -6.9158 | -43.5185 | 2024-12-13 03:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 358.4 |
| cab085e5-cc42-3a65-8512-eb183c9332e8 | -13.6933 | -54.7555 | 2024-12-13 03:30:00 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 48.2 |
| cfc44797-2fac-3726-820f-9b818d72a79b | -6.9158 | -43.5185 | 2024-12-13 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 303.6 |
| 547a676b-b962-3434-a603-717f002aa56c | -11.1959 | -53.8348 | 2024-12-13 03:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| da7dbec1-f228-31d6-9c4a-15e99a6b314b | -13.0644 | -52.0326 | 2024-12-13 03:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 55.4 |
| bc199fdb-1177-370d-9158-1259f6ae3a09 | -2.5108 | -51.8023 | 2024-12-13 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 215ff8c0-fbd9-31f6-b15d-928696737fec | -14.7848 | -52.642 | 2024-12-13 03:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| ba236802-76b5-35f2-9804-f01c8e9a6e94 | -11.1962 | -53.8142 | 2024-12-13 03:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| e94b7144-cb0c-3e5e-9f11-5d2a887301ce | -14.7655 | -52.6446 | 2024-12-13 03:40:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 26ad57da-cd81-363d-8fca-a2c0c11a6bbb | -11.2148 | -53.833 | 2024-12-13 03:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 1c57e8b3-7812-3291-82bd-753d9cacaa6c | -2.4923 | -51.8027 | 2024-12-13 03:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 4f822cae-eeeb-3828-ac36-fbdaf36fbbd9 | -6.9349 | -43.4934 | 2024-12-13 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 504a2373-7a65-3ded-a058-5a7bca8e263b | -5.2108 | -43.3067 | 2024-12-13 03:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| aca1c5aa-210a-3420-a4ca-e5b9b8c33014 | -6.9156 | -43.5418 | 2024-12-13 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 354.1 |
| e93e429b-1352-3d4d-8f5e-4731fe693400 | -11.2151 | -53.8125 | 2024-12-13 03:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 556911e0-9907-3748-83f2-80296a700324 | -5.2298 | -43.282 | 2024-12-13 03:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| db1ce7ed-1df3-304c-a74c-b913bba79740 | -5.211 | -43.2833 | 2024-12-13 03:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 45b03836-74bd-38fb-919c-aacbe6bbd70a | -6.9344 | -43.5401 | 2024-12-13 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 174.3 |
| bc3eb49f-b70b-36b5-a9e9-dec3aca370b9 | -6.9346 | -43.5168 | 2024-12-13 03:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 225.3 |
| bf0094cb-6edc-3f48-87e8-aa9e58dd4467 | -6.9344 | -43.5401 | 2024-12-13 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 4cf6642f-07cd-3f6d-ad23-2c10441e7039 | -12.5499 | -57.6996 | 2024-12-13 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 7c57ab0c-1911-36fa-91c6-adabb3962eb6 | -6.9156 | -43.5418 | 2024-12-13 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 257.8 |
| cf3d8808-faa2-3a13-b94d-baa9f2c9a6d4 | -13.0644 | -52.0326 | 2024-12-13 03:50:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| aa1dda89-d70d-3537-8ae5-fd73ed9b1b84 | -11.2151 | -53.8125 | 2024-12-13 03:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 40ed5e31-ac20-31cd-964c-a828254aa123 | -12.5497 | -57.7196 | 2024-12-13 03:50:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d2928f4a-f5b4-342b-a267-2d8c261fb800 | -14.7848 | -52.642 | 2024-12-13 03:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| b2b2e6fc-c716-37e0-a37c-8139d418d110 | -2.4923 | -51.8027 | 2024-12-13 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 565eee62-8b04-384b-a192-6c2f3f411ee8 | -2.5108 | -51.8023 | 2024-12-13 03:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 8e958e24-b2e5-38c9-8a5b-4d29d5009e58 | -6.9346 | -43.5168 | 2024-12-13 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 111.6 |
| fb234dba-046e-3dc1-b1e8-3c7db6cefc0d | -6.9158 | -43.5185 | 2024-12-13 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 198.6 |
| 2174fa7f-67ff-3e37-ad3c-f45cc341b2eb | -5.211 | -43.2833 | 2024-12-13 03:50:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| dba4d227-d8f7-314f-afff-5d57f5a60a00 | -11.2148 | -53.833 | 2024-12-13 03:50:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 17992b0e-bf63-3d86-b82e-27a6dfec9d89 | -14.7655 | -52.6446 | 2024-12-13 03:50:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.6 |


[Clique aqui para ver as próximas entradas](README10.md)
