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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10617a9b-0911-3851-96c8-21bc555747e2 | -23.02982 | -47.52706 | 2025-08-08 03:47:00 | NOAA-20 | RAFARD | SÃO PAULO | Brasil | 3542107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b7b26dc9-8b9f-33eb-bb3a-80c491e60122 | -21.78302 | -43.3362 | 2025-08-08 03:47:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c40f3e7a-42ca-36c4-80c9-4eb7da68c467 | -19.29785 | -47.43639 | 2025-08-08 03:47:00 | NOAA-20 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 86ff2613-46e7-3ee4-bf46-f7a97d0dbefb | -18.77884 | -47.46923 | 2025-08-08 03:47:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 23b974d4-3af0-3757-bdc2-27848826e6dd | -22.22284 | -44.73261 | 2025-08-08 03:47:00 | NOAA-20 | ALAGOA | MINAS GERAIS | Brasil | 3101300 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 65a98712-78f7-309f-96d4-8d7710b8b862 | -22.83286 | -43.59851 | 2025-08-08 03:47:00 | NOAA-20 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| acc9c9ee-9dd3-3a2c-bba3-acc1d313353d | -20.5722 | -41.72033 | 2025-08-08 03:47:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| bd00d731-4045-3145-81f4-7db4cabdb9e6 | -21.00649 | -43.27639 | 2025-08-08 03:47:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 6e1286f2-16ea-3575-835b-ff14690cf514 | -18.85465 | -45.13353 | 2025-08-08 03:47:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68b3806a-0e38-3ff2-ab95-8c20255cbdee | -22.24179 | -48.54321 | 2025-08-08 03:47:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f588704e-0db9-3027-b52a-6a8d8b847d40 | -22.04338 | -47.02307 | 2025-08-08 03:47:00 | NOAA-20 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c3cc34f-bf80-32d3-9af5-45313eece639 | -18.77949 | -47.46613 | 2025-08-08 03:47:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3bf65cff-219f-3e81-8ae2-42a8ac04fedd | -10.6247 | -44.767 | 2025-08-08 03:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |
| becfe693-e989-3db4-aea9-e8eecad72af3 | -8.9213 | -60.7489 | 2025-08-08 04:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 02b956f6-9461-399b-95f0-2968669ccf61 | -20.062 | -47.5663 | 2025-08-08 04:10:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 383e17a4-e33b-3589-89d9-d7d3dd5de0fa | -20.0613 | -47.5897 | 2025-08-08 04:10:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 92ddf6f7-cdd6-3657-9995-22d4b746bb2f | -15.5688 | -50.1404 | 2025-08-08 04:20:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 2edd9c6e-56b6-37bd-a1f4-c14bc1602c51 | -8.9213 | -60.7489 | 2025-08-08 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 005eedb4-bcbd-3daf-8c1d-6d8db7178682 | -7.3731 | -44.6546 | 2025-08-08 04:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 8f002606-021d-3882-901a-218967ebf853 | -15.5492 | -50.1435 | 2025-08-08 04:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 41.8 |
| 3543d0a8-6bfd-3712-9336-61f68f56f67a | -15.5497 | -50.1215 | 2025-08-08 04:30:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 40.1 |
| c388688b-103e-350f-a262-f61bff3efb22 | -6.28729 | -44.22405 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a5ba8cf-55e8-3621-9923-df1bd7c12ead | -5.07235 | -37.71569 | 2025-08-08 04:32:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 42dc0d4e-d4ed-3504-92a2-c64b62fb47e1 | -4.06166 | -46.93679 | 2025-08-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8adb1506-764b-3886-9b72-fcbf7a19eb07 | -6.66679 | -44.74594 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b6e9acf-7625-353f-83ab-2da07a3481a9 | -4.09418 | -46.92409 | 2025-08-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a4b0a4b-1a43-3dc5-a41b-774cb28a2044 | -6.12332 | -42.96001 | 2025-08-08 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f999f093-a807-3052-9401-9fcbe0a05534 | -4.09033 | -46.92705 | 2025-08-08 04:32:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 850ab7a0-dc91-32ee-9aeb-d5f6dae3bbbf | -5.5409 | -45.37431 | 2025-08-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd0e6d3e-b351-3b6c-ab6b-141a3335d770 | -4.12196 | -46.32677 | 2025-08-08 04:32:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30d23f0b-3fbf-3d76-bfdf-4d133409a1fd | -5.57618 | -44.08043 | 2025-08-08 04:32:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9eddaa1f-07b8-3c0a-9b23-5ad69adf56b4 | -4.06551 | -46.93384 | 2025-08-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b65d3fb3-0c8a-3a5d-bdb2-856dacaddf49 | -6.26085 | -45.26112 | 2025-08-08 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64d23fc8-a8a7-329a-b817-0ab2675dd87b | -6.65256 | -42.00765 | 2025-08-08 04:32:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9cd7bf8-b349-3ee5-b2fa-28c0e3887c47 | -6.46391 | -44.5753 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84afccf2-7523-3e47-899c-53df18e362b6 | -5.99198 | -40.38491 | 2025-08-08 04:32:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0aa7334-e4a9-3243-a4b9-a3e1fb09cc8f | -3.58752 | -41.65481 | 2025-08-08 04:32:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 061c33f3-bbdf-3bd3-a99c-2fa4d4afb322 | -6.80938 | -44.76668 | 2025-08-08 04:32:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b20b14a-ae72-3ed9-baba-aea1338c962f | -5.7754 | -43.88536 | 2025-08-08 04:32:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0d5a79b5-02ae-3032-b500-006be48bfdd6 | -6.29038 | -44.22902 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 76840aa8-6894-30ad-9bfb-ecdebf8e6848 | -3.59175 | -41.65543 | 2025-08-08 04:32:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6adc1e4a-3196-3f43-8cd7-1dbb04d6d19b | -3.96824 | -47.88159 | 2025-08-08 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65b715eb-f38e-3fbb-ae99-b341d79646c9 | -6.64186 | -41.8644 | 2025-08-08 04:32:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ac00bb4a-0ba4-33e4-9707-66d0b2f2d670 | -4.0033 | -47.09398 | 2025-08-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5281e8ab-0c5e-3105-b9ae-750a9a87fffd | -6.96904 | -42.87 | 2025-08-08 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 4466aa45-a30f-3a17-b3e3-c1c284ac4823 | -6.55687 | -39.0116 | 2025-08-08 04:32:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c7afbf69-ca89-3650-8c88-dfbe0829572f | -5.57685 | -44.07595 | 2025-08-08 04:32:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 01c3f2d8-0a5d-3829-b425-24ef0c078de3 | -5.54439 | -45.37483 | 2025-08-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d9f25aac-6b9e-3f3d-ad2b-fc789dd04d1c | -6.26498 | -45.25771 | 2025-08-08 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 918747f1-280d-3489-9aa4-a526c6ae993c | -4.6665 | -41.9656 | 2025-08-08 04:32:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8f91436d-927b-37b8-a9d8-645fdcea0fa0 | -3.66322 | -41.75711 | 2025-08-08 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a017371c-2a9b-3d9b-9ec7-7a63826b117a | -4.60152 | -46.59269 | 2025-08-08 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a7174fe-deeb-345e-b0eb-b7346ba40a60 | -4.7442 | -47.48937 | 2025-08-08 04:32:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27aaf37a-7a90-3ae2-bba0-4cd5c90b3c7f | -3.96878 | -47.87814 | 2025-08-08 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bff7108-4a39-3ef3-ab5d-a51d02ac5ac4 | -3.68089 | -39.81494 | 2025-08-08 04:32:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ee475654-9767-3361-bfab-59edae71acd4 | -6.84686 | -44.31113 | 2025-08-08 04:32:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3f91263-b69d-3ac7-a3d3-d6ada04a98fb | -4.02862 | -48.06141 | 2025-08-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f9ffa68-e1bb-302d-a395-e062507a476b | -3.59657 | -41.65217 | 2025-08-08 04:32:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a7c12ee7-e70c-3766-9343-5a48b2be11e4 | -5.61053 | -37.52943 | 2025-08-08 04:32:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2223b19a-78ab-3441-ad0d-cd93850a6dc2 | -4.0622 | -46.93333 | 2025-08-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77de70f3-8e39-3ee5-a055-14a36b2607ef | -5.89928 | -42.73131 | 2025-08-08 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ba7f6ac7-6112-3b4a-b630-93e8b11b8f49 | -4.65382 | -42.51144 | 2025-08-08 04:32:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 494310cd-7525-3a11-b31f-817ad07bb4e4 | -3.68124 | -39.81445 | 2025-08-08 04:32:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 08d5cbca-eefb-394f-ba35-70861b9de391 | -4.60097 | -46.5962 | 2025-08-08 04:32:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1646b429-640b-3c21-b30b-c2a79e333080 | -5.42948 | -47.15079 | 2025-08-08 04:32:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 37468e3e-7207-3290-9f8e-0d1a3f35facc | -5.14072 | -42.90292 | 2025-08-08 04:32:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab42cb24-90da-3159-bc50-208d1b9dd1bd | -7.03619 | -42.55345 | 2025-08-08 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 42da455a-a270-3830-bfc0-e60bf1455f72 | -6.12786 | -42.95716 | 2025-08-08 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 83564808-6dd8-3780-916f-6ceb25601653 | -5.89876 | -42.73492 | 2025-08-08 04:32:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 514638ca-f025-3a7f-9f73-f3ce89805bd8 | -3.66264 | -41.76097 | 2025-08-08 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a7124a01-26d9-350c-9930-0b0edd1c7103 | -4.00384 | -47.09052 | 2025-08-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 187a0b56-53e0-307b-b99d-1c932ecf1573 | -3.99999 | -47.09346 | 2025-08-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c621cdb2-17b5-3892-9c8c-c8bc9d65ebca | -7.02474 | -42.54393 | 2025-08-08 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bb0568f8-bad0-3381-b9af-12ccd56f3c23 | -6.2048 | -42.80408 | 2025-08-08 04:32:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 36f99262-9457-3a2d-8d72-e558da17b547 | -5.35231 | -42.79887 | 2025-08-08 04:32:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| c3b930b3-6389-3bf8-b59a-979556270f2f | -3.82266 | -41.55886 | 2025-08-08 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b5139002-9660-3899-af7e-81b75d0d06ba | -6.12384 | -42.95654 | 2025-08-08 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 2d1d7bcb-c9ff-3acb-84bc-e0e3b701032e | -6.64572 | -44.63562 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d7cfac9-3fde-3ae2-b68b-e1c17299dc0e | -4.92009 | -46.72808 | 2025-08-08 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c4bda2f-8967-3dac-b010-2df5ca09dbc6 | -6.96851 | -42.8737 | 2025-08-08 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 389e0e14-5713-3476-a8bc-d96f7276555e | -5.54499 | -45.37095 | 2025-08-08 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b385c818-873c-3b19-a05c-56f3bc1341de | -6.5564 | -39.01493 | 2025-08-08 04:32:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bda8fb0b-06f5-3536-b4f9-ba16524f2581 | -6.44295 | -44.59092 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c634275-4ed6-3e92-99d2-dc7a5dfbdc9a | -4.02477 | -48.06435 | 2025-08-08 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2386cf05-5b44-3a71-b399-651ffd23864e | -4.00053 | -47.09002 | 2025-08-08 04:32:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6caeebe1-ee1e-353c-980b-262253c86d4a | -7.03564 | -42.55726 | 2025-08-08 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| f0bddd94-35f1-3544-9602-94abb801f050 | -6.26145 | -45.25716 | 2025-08-08 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31056f11-3cfa-3bc2-8497-bc15206c71d2 | -4.91955 | -46.7316 | 2025-08-08 04:32:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eec84f77-993c-35f4-bbac-dd76534f9431 | -5.97131 | -43.03348 | 2025-08-08 04:32:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7a341871-3a98-3c70-aaad-ef50f53de45d | -6.64595 | -44.63364 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df7e4964-0029-3e48-abb9-374f227d0982 | -5.60621 | -42.28225 | 2025-08-08 04:32:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9029c095-ccc9-3702-87ff-57902ee51f95 | -3.66743 | -41.75769 | 2025-08-08 04:32:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 627a91f0-e14d-3548-a7ef-7f4a02fdc62a | -7.39808 | -39.67997 | 2025-08-08 04:32:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 50674ac0-bd1b-399b-a1dd-f179a72bbdbd | -7.02 | -42.54712 | 2025-08-08 04:32:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b1fdab3e-f6cb-3296-a9fa-2e7f7a272ef4 | -6.96548 | -42.8657 | 2025-08-08 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 65ada455-f2f2-38d4-80f1-4013fd499f74 | -5.59868 | -47.15544 | 2025-08-08 04:32:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24ebe595-0a09-3e3a-b4a8-16fd1b3adee0 | -3.35777 | -43.1711 | 2025-08-08 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d60e94b-357a-3e9d-a992-e0017c781695 | -6.64533 | -44.63784 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f59a19d3-785d-3ec8-8607-b8f01b642c60 | -6.44674 | -44.59015 | 2025-08-08 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 59b1e7e6-c696-362d-9bf9-deb47702d65d | -3.35849 | -43.1664 | 2025-08-08 04:32:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
