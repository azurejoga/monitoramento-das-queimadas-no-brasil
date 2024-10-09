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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7011daa8-a110-36c7-a37d-b383fe240810 | -13.398 | -61.9182 | 2024-10-09 04:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 84.5 |
| eef3c624-a4f5-3cf1-920d-64ec627b1b75 | -13.417 | -61.9169 | 2024-10-09 04:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| d01c7fba-85b6-3bbd-a827-d73b2850652c | -13.8764 | -44.5386 | 2024-10-09 04:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b6a9c7b7-05bc-3c95-b9fb-18a98fe1a280 | -13.9158 | -44.5081 | 2024-10-09 04:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 9011b6f8-d754-36b7-93a2-6ea8cd09b8fb | -13.9343 | -44.5518 | 2024-10-09 04:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 67ee6310-5298-3f25-97bb-249a040cb2e1 | -13.9348 | -44.5282 | 2024-10-09 04:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 65f18cf9-a144-37c8-becf-81cfe4848363 | -14.0782 | -51.0945 | 2024-10-09 04:16:25 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 52610ee4-ae8d-357c-b9e2-b7b58fc820bc | -14.0975 | -51.0918 | 2024-10-09 04:16:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 188.3 |
| a851f727-b24f-36f0-9730-ba4de2de6dc7 | -14.0979 | -51.0703 | 2024-10-09 04:16:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.8 |
| e0e251a9-76fb-3213-9025-f49f362320dd | -14.1168 | -51.0892 | 2024-10-09 04:16:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 42a75bf5-b185-37b3-8364-c1b915549cee | -16.8045 | -57.4402 | 2024-10-09 04:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 67.3 |
| a1e9b272-8711-3b8a-b996-19307ab3802d | -16.8898 | -55.8039 | 2024-10-09 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 113.4 |
| c0eff297-0869-3468-b67c-be5e171ecd96 | -16.8901 | -55.7831 | 2024-10-09 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.0 |
| fa6d2d53-4b32-3901-8ab4-0715dce1e4a2 | -16.9091 | -55.8222 | 2024-10-09 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 31646c3c-2756-3fe1-a09a-10d93b68ba85 | -16.9094 | -55.8014 | 2024-10-09 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 252.5 |
| f68f3abc-f0e1-385b-90a4-f8ccb91ffbc2 | -16.9098 | -55.7806 | 2024-10-09 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 175.1 |
| 3bbd1b19-972e-32e9-8f7f-53207dd2de7e | -16.929 | -55.7989 | 2024-10-09 04:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 82.8 |
| 4092bbe7-04f5-3da2-8200-f23894d1724d | -17.0623 | -56.0308 | 2024-10-09 04:16:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| f2cd2df7-a290-3f9a-b8ea-9e942682dcb1 | -18.1193 | -56.3921 | 2024-10-09 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 105.4 |
| 10975916-62ec-3d5d-9f0b-c6c718beaaab | -18.1196 | -56.3713 | 2024-10-09 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.2 |
| ed8f2946-9c37-37b3-99a9-4ceee04349a7 | -18.1391 | -56.3895 | 2024-10-09 04:16:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.6 |
| b7d0a834-2929-3f4a-a6a9-77588b8080a1 | -18.6597 | -57.2137 | 2024-10-09 04:16:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 54.5 |
| 39db6e78-6cd9-37db-8c82-58b6271000b9 | -20.103 | -55.9647 | 2024-10-09 04:16:58 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 3bff6b4f-dc6c-3fdb-b688-699df1526da6 | -20.3346 | -48.7307 | 2024-10-09 04:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 282.3 |
| dd45d3b9-f075-3f27-94e3-fb57e3d3a92b | -20.3352 | -48.7076 | 2024-10-09 04:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 149.3 |
| bc9a81fc-b6c7-320f-86f6-91e8bfefdc4a | -20.3551 | -48.7262 | 2024-10-09 04:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 23525ea3-1da1-3cab-88bf-a9101db52ca8 | -20.3557 | -48.7031 | 2024-10-09 04:16:59 | GOES-16 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 700957ac-a696-382a-bbf2-c63aabf136ae | -13.02748 | -40.3312 | 2024-10-09 04:17:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b71705d5-6138-305f-9a71-1e04238cf565 | -14.72067 | -42.67953 | 2024-10-09 04:17:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| acc11a09-4e29-3dee-a3de-99c7d291bcdb | -14.78414 | -42.84339 | 2024-10-09 04:17:00 | NOAA-21 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4559d909-925a-3933-9e15-0a5ca75f14d7 | -13.89612 | -44.27959 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8bd292d-5fd7-3291-a49a-42396a518bf5 | -12.4957 | -40.86498 | 2024-10-09 04:17:00 | NOAA-21 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 20f5f00d-3d5c-37bb-8fdd-512799c643d2 | -13.89425 | -43.80326 | 2024-10-09 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e8ed93e-1d9d-3667-9445-305133005088 | -13.8747 | -44.13069 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67155efa-897a-3e24-aa45-8eed11fcd213 | -10.71352 | -37.06074 | 2024-10-09 04:17:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a7599323-a4c7-3850-b89e-5ede3bb0b08e | -10.71335 | -37.062 | 2024-10-09 04:17:00 | NOAA-21 | MARUIM | SERGIPE | Brasil | 2804003 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9a64acd3-4f4b-384f-bd57-1f2c162f1d85 | -12.84593 | -39.85372 | 2024-10-09 04:17:00 | NOAA-21 | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3df6ab2b-6b99-31d9-a4bc-319c78685483 | -13.21965 | -39.93069 | 2024-10-09 04:17:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d4698f1-c08d-365f-b9a3-3d08c4cfc482 | -13.21947 | -39.93197 | 2024-10-09 04:17:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a9d56c90-323f-3852-a5a4-ad064fa0e27b | -13.06326 | -39.93298 | 2024-10-09 04:17:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 900a6e0e-5ec8-3366-8173-d57ff065cca9 | -17.10174 | -41.19864 | 2024-10-09 04:17:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b7dfd53e-2581-3dbd-beb1-336c6fc79f60 | -17.48898 | -41.18155 | 2024-10-09 04:17:00 | NOAA-21 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2a505894-58dd-3ec2-8476-064cb8abbdf5 | -17.48734 | -41.1799 | 2024-10-09 04:17:00 | NOAA-21 | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7ca098a7-a764-3535-9faa-867e3cc03dc6 | -20.34803 | -41.84591 | 2024-10-09 04:17:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 25449130-c368-3e5b-b714-c53f19630592 | -20.29325 | -41.85822 | 2024-10-09 04:17:00 | NOAA-21 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9c41b642-3ada-3bae-8480-4218c83f4ccd | -20.62098 | -40.96155 | 2024-10-09 04:17:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| bc7c373e-84e2-3c29-bd34-c9aa3c912d9a | -20.61688 | -40.96122 | 2024-10-09 04:17:00 | NOAA-21 | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 132868ac-e11d-39b3-9709-60deaa9e476d | -20.35187 | -41.84657 | 2024-10-09 04:17:00 | NOAA-21 | IÚNA | ESPÍRITO SANTO | Brasil | 3203007 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| c9e59be8-f5cb-34ce-9853-b7ea4147dcc9 | -20.26974 | -41.36159 | 2024-10-09 04:17:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8bbbeb02-11ef-36c5-87fe-a4de0cb24ff3 | -20.26683 | -41.36009 | 2024-10-09 04:17:00 | NOAA-21 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 785bd6ad-047b-3ae7-ab88-dc13153171ce | -22.30396 | -41.8825 | 2024-10-09 04:17:00 | NOAA-21 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6aba06d7-f67f-319f-9849-f63d5938a34b | -13.87975 | -44.53833 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51754567-c5ed-314f-8729-1abfc4a94fd2 | -11.96475 | -41.58752 | 2024-10-09 04:17:00 | NOAA-21 | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ad55c904-5765-3bb8-952d-704f1fb42f15 | -13.36034 | -41.32222 | 2024-10-09 04:17:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c7f3fba3-26e8-31db-9a89-cd6b46b92922 | -12.49634 | -40.86049 | 2024-10-09 04:17:00 | NOAA-21 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f33264cd-df8b-3480-8779-9fb7b0f282a7 | -14.13376 | -41.69003 | 2024-10-09 04:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fc0879c9-edaf-366e-b7b5-2f7a013b3e53 | -14.12066 | -41.67884 | 2024-10-09 04:17:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ddbd1cdc-5998-398c-ab8c-df286fd1f1ca | -15.7307 | -42.24167 | 2024-10-09 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e57d3210-b55e-3a70-9fbe-6fd2186b02b1 | -15.61322 | -42.35719 | 2024-10-09 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7541d23c-bb73-31e8-a03d-eb2dd200c631 | -15.61264 | -42.36127 | 2024-10-09 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72c81d55-4638-3fb6-babe-ea31d984281e | -15.6115 | -42.36934 | 2024-10-09 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| cdb1c880-9dd8-3325-baed-bc6fdfd5696d | -15.60854 | -42.36473 | 2024-10-09 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 7074fb07-98d4-3fd7-a292-51abf1a53857 | -15.60796 | -42.3688 | 2024-10-09 04:17:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| efd26b03-7ae2-30c4-a4ad-84d8c3cb58e0 | -15.96731 | -41.3666 | 2024-10-09 04:17:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b466182f-bde8-3d96-8d94-adcb43132e94 | -15.27293 | -41.64129 | 2024-10-09 04:17:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b6564cfb-d3b7-3f3d-80b4-00bede4f5be6 | -15.26928 | -41.64071 | 2024-10-09 04:17:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 80be74c9-6ce0-31fc-8bd8-e8f9d877e2bd | -17.10779 | -41.32669 | 2024-10-09 04:17:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9f5d9e83-563d-3f5f-9c41-6a12aa379a9e | -17.10336 | -41.33073 | 2024-10-09 04:17:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| f77c1210-36ea-3c76-8f0f-692658ec25ed | -17.09959 | -41.32994 | 2024-10-09 04:17:00 | NOAA-21 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| a15ef73c-9b63-3184-8b8b-15e04fb6c396 | -16.65826 | -42.2255 | 2024-10-09 04:17:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a684d8b-3e33-3c44-b223-eb5a34504d9a | -16.65466 | -42.22492 | 2024-10-09 04:17:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0de8461e-0cbb-3159-9275-4efdc3251041 | -16.65106 | -42.22435 | 2024-10-09 04:17:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 543aa617-c083-3a99-a967-6e99f991b045 | -13.84064 | -44.56844 | 2024-10-09 04:17:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8352f19-ff0f-3d42-b3a3-32b504693545 | -20.01033 | -42.43909 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 69fb1464-746e-3d7e-b7c4-84699348a2c6 | -20.0029 | -42.43811 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 7a6c8c6d-065f-3e99-81e9-6a40d243ddfc | -20.0023 | -42.44251 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| eaa9884c-4018-324b-9b5e-573caca3423b | -19.99985 | -42.43276 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 2618a146-4070-33be-8e9a-99cc66ec78b3 | -19.99179 | -42.43641 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| bf1fe296-efa2-39b6-9008-79d92cee385b | -19.97325 | -42.43365 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 36faa70c-8191-31fb-b3f9-b2540a493c7a | -19.82686 | -42.3815 | 2024-10-09 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 0f5ca2e8-26e5-3120-a29a-a2e34c826b17 | -19.82629 | -42.38577 | 2024-10-09 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| c2d555ad-4509-3436-a278-3a6fd64f4e52 | -19.80477 | -42.40546 | 2024-10-09 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 0a1f1699-2813-368b-8001-4b9aa53963d0 | -20.68092 | -42.33459 | 2024-10-09 04:17:00 | NOAA-21 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 260dbd1d-b022-36e3-b8bd-1d7bb3c72478 | -20.58202 | -43.28045 | 2024-10-09 04:17:00 | NOAA-21 | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6a45b6cc-e462-3604-90e2-f41549bd2e11 | -20.22776 | -42.89434 | 2024-10-09 04:17:00 | NOAA-21 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3dc2aa02-f02d-3196-bedb-f8533bbde606 | -20.00601 | -42.44305 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| fe06e262-fc73-376c-ac91-d08174baf9ef | -20.00169 | -42.44696 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 111b950f-c5a2-3c96-82de-af8a45e19279 | -19.97695 | -42.43429 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 318835f6-444a-36b2-87a3-bac4decf0395 | -19.97633 | -42.43882 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 6fbabb52-97f3-3f74-8674-bfa05b29d12f | -19.8343 | -42.38243 | 2024-10-09 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1971373f-6807-3336-808b-503b09e144df | -19.83232 | -42.36902 | 2024-10-09 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 583f19e3-1ec5-320a-bce4-779075ec2930 | -19.83057 | -42.38204 | 2024-10-09 04:17:00 | NOAA-21 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 8fa9b21c-1c95-397a-bbb6-3f72dd63d36d | -20.37754 | -42.20934 | 2024-10-09 04:17:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 565b7f7d-1c7c-334b-a076-7cae2f35d2c0 | -20.23139 | -42.89487 | 2024-10-09 04:17:00 | NOAA-21 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| f5c9c807-2dba-3a52-a325-dc2815c041e0 | -20.22714 | -42.89885 | 2024-10-09 04:17:00 | NOAA-21 | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 5747ce61-91aa-3cca-9d2f-f948868e2851 | -19.99859 | -42.44195 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 07ccd530-bcd1-3a1c-8715-78c2618d4730 | -19.9955 | -42.43693 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5005e962-62ed-383f-8c55-48ae8dcc9f1c | -19.99089 | -42.18819 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| bf0ed227-d7a7-3c84-9d95-d03b6cc18ecb | -19.98994 | -42.44995 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 78c92198-34f2-3cd7-a422-6e37c26aa3c8 | -19.97573 | -42.44328 | 2024-10-09 04:17:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |


[Clique aqui para ver as próximas entradas](README83.md)
