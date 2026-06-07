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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ee649b97-f367-309f-93e3-b9c9cfd86aae | -12.36736 | -47.89642 | 2026-06-07 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50d264ce-7416-3d3b-afde-fd389354b30b | -10.83169 | -60.75598 | 2026-06-07 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| de7a29ac-4b4e-3de8-8c96-34a483c9889a | -12.04057 | -45.27622 | 2026-06-07 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db4341dd-030f-3516-89cb-c73543ce5efb | -12.72596 | -54.20063 | 2026-06-07 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73b5f2df-f3bb-3024-8f0b-195683687e90 | -14.24079 | -47.97068 | 2026-06-07 04:53:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02922e08-d007-3a60-8a36-d512baa319c4 | -12.49802 | -46.27472 | 2026-06-07 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8184c8f-cf62-3d84-8f21-930e3c1c46be | -16.50033 | -43.50043 | 2026-06-07 04:53:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 565d16da-5aa4-3f12-a0b1-ec8d8d1f3748 | -11.54637 | -52.79278 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 75a2cb6c-49fa-3cd2-95c7-c744ca1b75be | -11.79076 | -57.34936 | 2026-06-07 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b1e76be-5aed-3f3f-86ae-c6284f2d3f85 | -11.54969 | -52.7933 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1388cc67-2e91-30af-85d8-aa22cc658c8c | -10.12466 | -57.77052 | 2026-06-07 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fde04c80-d76a-3174-a911-91113900fb23 | -15.40872 | -55.86819 | 2026-06-07 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fca18990-f139-35b6-a8e3-0542b3cddef0 | -12.06743 | -48.07684 | 2026-06-07 04:53:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d6066ac-56b0-30bb-890b-7a69bba5211e | -11.54305 | -52.79225 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e472c6a-4e2b-399e-a2e1-3ed9e5521798 | -14.28564 | -57.53838 | 2026-06-07 04:53:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5ce556d-3db1-3431-959e-f474519e53dc | -11.55735 | -52.80886 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 41b6bce3-4a09-3e80-9053-6be977f3513f | -10.77124 | -54.10145 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb8352ca-ea9a-3c4b-8119-a88648ac194c | -12.50274 | -46.2757 | 2026-06-07 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b9953da-a47c-3a0d-b50c-6a09f0163964 | -12.06565 | -48.43018 | 2026-06-07 04:53:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 418bb97c-f8f3-3434-85a2-0120888caeca | -11.26927 | -53.96701 | 2026-06-07 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f81023d4-52ac-32c8-a77e-fe5c0957fc2c | -11.08666 | -48.26883 | 2026-06-07 04:53:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 10ef1a1b-58f9-3857-9cb2-2e91bbcde6ba | -11.87511 | -43.90083 | 2026-06-07 04:53:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5b60429-b1cc-30f2-92ea-499ccf4c24d9 | -14.64036 | -54.51191 | 2026-06-07 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 203fd587-5f86-3d95-96d9-2865b213bf34 | -10.57484 | -57.31898 | 2026-06-07 04:53:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 16e06e9c-0582-3645-a8a7-7a310ce00239 | -9.81325 | -57.82066 | 2026-06-07 04:53:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1118c9c8-72c4-3684-8e41-d08811e27a99 | -11.72515 | -56.84443 | 2026-06-07 04:53:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a70838c9-e464-3a6d-94b8-8e742776e8b1 | -12.04602 | -45.27386 | 2026-06-07 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24bc17a3-de04-331a-8ba5-7eab62e82f29 | -10.84442 | -53.74368 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92645429-e5f3-3db3-b67f-b746e576c484 | -11.47371 | -47.33957 | 2026-06-07 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| daeca38c-de52-3b92-a59f-67988218fa2c | -12.4096 | -47.4927 | 2026-06-07 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 25daa806-c5c2-3d81-9a85-14bfc3923508 | -12.04095 | -45.27319 | 2026-06-07 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91998096-0c64-3b7a-820a-c30f8bcb41c2 | -11.55301 | -52.79382 | 2026-06-07 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f84bdd59-79d2-3a24-89be-2b0bc0091bd9 | -13.11928 | -53.5321 | 2026-06-07 04:53:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26fab048-ef06-374d-b3cc-8452c888fafa | -14.53685 | -58.81973 | 2026-06-07 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16c1a2c3-7bb1-3bf2-8e7e-9f280b82bc1f | -15.4026 | -55.86345 | 2026-06-07 04:53:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7f9497ec-c1b2-380c-a886-9ff8316ebeea | -10.82992 | -60.76582 | 2026-06-07 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cfdc80cc-e5e9-3a05-b14a-da33b8cb98e0 | -12.06707 | -45.975 | 2026-06-07 04:53:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71c5e749-dfbf-36fe-8774-856c55ea667c | -11.26871 | -53.97052 | 2026-06-07 04:53:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c24504e-0a08-3e51-8d51-fcd87efebea9 | -13.36304 | -43.20147 | 2026-06-07 04:53:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 418cfd6c-a29e-342b-8dbc-3d0a326a3a4a | -13.36429 | -43.20556 | 2026-06-07 04:53:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b7a23cb2-21bc-39f4-be09-8b016864874a | -10.86256 | -53.73586 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de656638-398d-3306-a17f-0c168c9ea885 | -12.36838 | -47.89328 | 2026-06-07 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 35a1364b-0faf-37cb-9c28-33792018bb6e | -14.24957 | -47.97131 | 2026-06-07 04:53:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 736fef61-aefa-3fd5-aff1-6c8e46525a7c | -10.85432 | -53.74526 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c178239d-1252-3a2a-b26c-de90d18dbe21 | -14.64311 | -54.51599 | 2026-06-07 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f966fffd-bbf3-310f-b6e8-0d77bd46133f | -16.04534 | -50.55998 | 2026-06-07 04:53:00 | NOAA-21 | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 600bbf29-d058-3044-8f05-da2be53ac155 | -10.59908 | -55.42207 | 2026-06-07 04:53:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a563a74d-9acf-3c36-b67f-6c2340a790d7 | -10.85102 | -53.74474 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe6484fd-13f2-3e82-92f7-4ba6367624e5 | -11.5151 | -56.11773 | 2026-06-07 04:53:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cdd09e2e-974f-3cbf-9203-a0f673a05f5f | -10.8372 | -60.75187 | 2026-06-07 04:53:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| efb11489-60de-38c9-86bc-1de3aed53b72 | -9.21088 | -64.08614 | 2026-06-07 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e6035a5-8c01-33ef-926c-75d11ab4576d | -11.47471 | -47.3386 | 2026-06-07 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a6b4478-5e3a-32b5-98e2-48fb6f14f074 | -12.50028 | -46.25676 | 2026-06-07 04:53:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 607a6cf1-cc55-3d69-898c-5e9c004765c9 | -12.81218 | -54.86116 | 2026-06-07 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 851de85a-4d53-3327-8bba-2c24716b8c66 | -13.49739 | -56.56881 | 2026-06-07 04:53:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87b66a52-8490-30d1-bfdb-86b66fb90ddf | -11.57377 | -48.14429 | 2026-06-07 04:53:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e3a02aa-3762-381d-ac74-57252bb28b41 | -11.47749 | -47.34445 | 2026-06-07 04:53:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d55b0bfc-5511-3de8-98b0-1ffb7c6918c0 | -11.61929 | -55.1825 | 2026-06-07 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e0b3b07-9739-317a-ad30-ccb3081b00aa | -10.86201 | -53.73935 | 2026-06-07 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c7ec5a7-a57e-3812-82ce-7b54ecf64e0a | -16.78811 | -54.1694 | 2026-06-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50ece01d-b2bd-3844-a7d4-5b8e378a717b | -17.99527 | -54.27565 | 2026-06-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a45f38c2-a6da-383c-9720-bcabaa32e431 | -16.97483 | -54.78993 | 2026-06-07 04:55:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1ed25d7-2f94-3a3e-9b96-08e49a73b8e3 | -20.50522 | -54.57132 | 2026-06-07 04:55:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ab6d76c-1f82-3ca2-9c4d-17669f53cffd | -21.98922 | -57.60614 | 2026-06-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eee26da1-0d4e-361a-8ef0-0051100c070c | -16.79861 | -54.16739 | 2026-06-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3eb06bd8-8c6e-3539-ab01-331a1f3f6002 | -19.96569 | -47.20798 | 2026-06-07 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b56d05e7-5242-3cd0-9bda-02d100e6510d | -19.6872 | -46.03082 | 2026-06-07 04:55:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5e5e0d32-3da8-37b4-9253-3d384f211b09 | -21.42642 | -50.82634 | 2026-06-07 04:55:00 | NOAA-21 | RUBIÁCEA | SÃO PAULO | Brasil | 3544400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b3ce9a3e-f4f0-33e4-9982-68823c06a6d0 | -23.76898 | -47.44489 | 2026-06-07 04:55:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5fcc6491-da34-3ea3-9d9f-24dd34276c58 | -16.79143 | -54.16993 | 2026-06-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19ecf24b-e949-3e00-b09d-b5a1bc0cd0cb | -21.33183 | -49.18613 | 2026-06-07 04:55:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 02899a27-d3fe-3d84-bd52-46c09d8ce604 | -21.98525 | -57.60927 | 2026-06-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6620728-0886-3222-aa11-e7a04e8c84d8 | -22.17465 | -50.38478 | 2026-06-07 04:55:00 | NOAA-21 | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e99b244a-9439-3504-8b6c-71d40816d19a | -22.38116 | -47.01763 | 2026-06-07 04:55:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a7ff788-ea25-366e-84c2-46421eab2343 | -23.76929 | -47.44172 | 2026-06-07 04:55:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 71260904-30ac-3115-9c84-cc7af1f24cf7 | -17.99805 | -54.27986 | 2026-06-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 18999394-242a-3779-9bbf-07b72f82ba25 | -17.99472 | -54.27932 | 2026-06-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44c9e6ba-029a-3b5d-90e1-2190a9260109 | -18.00137 | -54.28041 | 2026-06-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 216125e4-ee29-3ee0-99b0-c2626660cedf | -21.98462 | -57.61306 | 2026-06-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fdd8bcc0-7ef2-3d63-a2e5-7583a5090aa7 | -19.96224 | -47.20684 | 2026-06-07 04:55:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9dfb002b-4f3d-34d9-8679-204a100b7f12 | -18.46309 | -54.70806 | 2026-06-07 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 584c11f9-fc4f-368f-871d-3c6c5d1aecbf | -19.68756 | -46.02726 | 2026-06-07 04:55:00 | NOAA-21 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb396955-0cae-3855-8e89-83ffd68f4c76 | -23.82325 | -48.71439 | 2026-06-07 04:55:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c31f28b-5b79-30d2-8af8-a5962d3483c0 | -16.79475 | -54.17046 | 2026-06-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 893b4f60-5b04-3b41-abbc-ce183576a953 | -22.7024 | -43.36352 | 2026-06-07 04:55:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| c7e72da7-3f42-32d5-9bfc-bfd6cb089b5d | -18.00415 | -54.28462 | 2026-06-07 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5e32e71-1d46-314a-bcaf-731deedd4ba3 | -21.98798 | -57.6137 | 2026-06-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fc928c7a-a1a4-3514-bb35-52fc7cb25bc6 | -21.33237 | -49.18156 | 2026-06-07 04:55:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5d0c7dda-e2d2-314f-b40e-caa7e126ea55 | -23.76698 | -47.44354 | 2026-06-07 04:55:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 595d74a9-322c-34e9-9756-e44dad2b171e | -16.79807 | -54.171 | 2026-06-07 04:55:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| afbf2f7e-108b-382e-9b42-e7f7db8ef18d | -21.9886 | -57.60993 | 2026-06-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1062bc84-3ec8-32f3-90f8-f57d4d7eedac | -16.5993 | -58.2354 | 2026-06-07 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7e38d1c1-dbd8-3f76-a57f-8d729596a5bb | -22.17419 | -50.38876 | 2026-06-07 04:55:00 | NOAA-21 | QUINTANA | SÃO PAULO | Brasil | 3542008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e9ad5550-77ab-3acf-b42e-d22ef2b3c981 | -18.46364 | -54.70441 | 2026-06-07 04:55:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 43977f04-1862-30ae-8435-5c7615d6f1e0 | -17.7893 | -52.0999 | 2026-06-07 04:55:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09b022f3-0873-3757-bc81-33f76a70e34d | -21.98587 | -57.60549 | 2026-06-07 04:55:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ce3078d-ca2b-3925-9c40-8a460f04f8d1 | -25.05572 | -50.87644 | 2026-06-07 04:57:00 | NOAA-21 | IVAÍ | PARANÁ | Brasil | 4111407 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d7a89fdd-57b9-3fdc-bba1-7ae99c4b65da | -30.40049 | -54.25764 | 2026-06-07 04:57:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 9ea95f32-c930-389c-a2fd-7fc8b3a8c9e7 | -5.80738 | -45.12548 | 2026-06-07 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 92230785-192e-36e1-ac0d-f1e8c17deb53 | -5.8001 | -45.12487 | 2026-06-07 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README7.md)
