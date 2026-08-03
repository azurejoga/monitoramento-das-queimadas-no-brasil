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
| 2a7bbc64-e2bd-3a2b-ba58-7f7ab4c396a2 | -10.58307 | -46.78616 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 67445642-7bfd-348b-8d1d-15c0f7aeafc3 | -6.43625 | -47.9821 | 2026-08-03 03:45:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ad34003f-e60d-31a0-bf2a-60fd8d151464 | -6.77493 | -47.02866 | 2026-08-03 03:45:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcebc7bd-e7fa-3387-aabe-4255b39a59a9 | -7.17785 | -42.33911 | 2026-08-03 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90f17942-fe71-396e-b2c6-5a587db16914 | -12.18815 | -39.77185 | 2026-08-03 03:45:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a67d075d-d1c5-33f3-bb3b-f17f467d6fa0 | -7.35637 | -43.86389 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aba03b8a-5967-3e67-a4b6-d4e8e23a67b7 | -6.4373 | -47.97643 | 2026-08-03 03:45:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d81521e-462f-3386-9b08-764fb3c16326 | -10.57493 | -46.79747 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 40643752-8a4e-31ce-a248-a1efa68e9ccf | -7.62222 | -45.30659 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d9011c0-74ad-3163-acd7-49941acf9e8e | -7.562 | -45.04037 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 73bce51e-d6f6-3f9a-b842-33e97ea71e98 | -10.56914 | -46.79641 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b6dc994b-bf71-3671-89b7-9be8663e1509 | -7.34588 | -46.61077 | 2026-08-03 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a3f31c2-a06d-33b1-ad32-0b28ff7711ac | -10.57649 | -46.78925 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c368ed5d-2338-3e57-9cd1-e2eb3e962a22 | -7.35679 | -43.85589 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01b10ade-31c8-340c-bc08-c249935e6300 | -10.57064 | -40.15106 | 2026-08-03 03:45:00 | NOAA-21 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1780929-7949-3702-96e5-1ace9bf69473 | -10.62545 | -46.75351 | 2026-08-03 03:45:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f9f4773-ac08-3a53-a337-ac35a56dfc8f | -7.3624 | -43.85364 | 2026-08-03 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cabaeea7-64eb-3694-a6d2-260fd807b0f4 | -7.35064 | -43.86116 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13a8b764-b161-3559-9bec-82af9726b519 | -6.77123 | -47.02604 | 2026-08-03 03:45:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d7c65bb8-d028-331b-890a-c65d1749a0ea | -7.36187 | -43.85661 | 2026-08-03 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6a39dc72-d5cd-3f88-9fcc-4ee43da73064 | -7.34557 | -43.8604 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 46daa04a-844e-351b-8806-0546a472c05c | -7.15334 | -44.04824 | 2026-08-03 03:45:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0f9ae18-6fef-3394-80cc-94c0afe93c5f | -7.55587 | -45.04325 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2136ea22-35d9-3411-90c6-6f5419e2335d | -6.85602 | -44.79163 | 2026-08-03 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bed6f25b-e206-323c-99d9-3ad7f3236256 | -8.34022 | -45.98551 | 2026-08-03 03:45:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8896221-6796-32f3-adb2-72ec1e0ddcc6 | -7.56338 | -45.04052 | 2026-08-03 03:45:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa88d651-6ebc-3237-b1fb-7baf765c0044 | -8.23773 | -46.24987 | 2026-08-03 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b08041f4-814b-3c26-90a2-f6d158d59cec | -6.85643 | -44.79917 | 2026-08-03 03:45:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c9b363f-b315-3008-b8d4-91433e16b51a | -7.35689 | -43.86085 | 2026-08-03 03:45:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0515250d-c7f8-3f29-bf9a-3b151a5510b7 | -7.1773 | -42.34002 | 2026-08-03 03:45:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 64c81086-190a-3a87-992b-1db7e1e1dcc5 | -19.7727 | -42.08103 | 2026-08-03 03:47:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bbf29e63-9db6-3437-9994-749e76173c7b | -17.965 | -47.13261 | 2026-08-03 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b25f576b-b671-3ef2-9db6-94a245339cf4 | -18.77525 | -41.93752 | 2026-08-03 03:47:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 333bdc01-ff64-3616-ace3-dd48c6e322ba | -19.22919 | -46.99587 | 2026-08-03 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 05741038-bc09-3b3f-8114-0a60d0098d9f | -17.96831 | -47.14271 | 2026-08-03 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10dae786-7a2e-31ae-8a8f-2de359648747 | -19.23413 | -46.99722 | 2026-08-03 03:47:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23cffdc4-7949-3fc5-a437-37312317bddb | -18.25584 | -49.40753 | 2026-08-03 03:47:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b63c6528-0ae7-3863-95da-72139afa6afb | -19.76902 | -42.08036 | 2026-08-03 03:47:00 | NOAA-21 | PIEDADE DE CARATINGA | MINAS GERAIS | Brasil | 3150158 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1cf9c5e-4960-3bc3-a422-d81389f8cf15 | -20.87687 | -45.55098 | 2026-08-03 03:47:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5651c311-cf58-3d44-bf8b-f7028fb41203 | -16.22356 | -45.49427 | 2026-08-03 03:47:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 768aac4e-99b7-34d6-82ce-9a5dbcc1e5af | -21.01895 | -40.85738 | 2026-08-03 03:47:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d40ac897-3a39-3c38-8b27-75f9d64b1283 | -21.64433 | -43.05516 | 2026-08-03 03:47:00 | NOAA-21 | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| bc6ee563-283b-3b48-8cb6-b07682778cea | -21.64057 | -43.05436 | 2026-08-03 03:47:00 | NOAA-21 | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 72eca4b3-19ee-314f-b938-a84af8b15880 | -20.87782 | -45.54626 | 2026-08-03 03:47:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7bbc892-cfd2-34d3-95d9-ec8ccece423d | -21.64143 | -43.04956 | 2026-08-03 03:47:00 | NOAA-21 | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 60823bf3-1d8d-3783-8a0f-320fd6cd39d3 | -17.96563 | -47.12952 | 2026-08-03 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5be01998-f636-3a78-8399-0b62a1599a2f | -18.89894 | -43.45205 | 2026-08-03 03:47:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| be41b54b-3857-37c1-ab9e-c8366f61bd14 | -18.25684 | -49.40299 | 2026-08-03 03:47:00 | NOAA-21 | PANAMÁ | GOIÁS | Brasil | 5216007 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1ac4bcf6-1a62-3b95-a210-a6544ecee46b | -21.64477 | -43.05327 | 2026-08-03 03:47:00 | NOAA-21 | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 312aca11-e746-3ad9-956e-5cad71a90848 | -18.25372 | -43.65157 | 2026-08-03 03:47:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 09936903-ee66-344e-875c-a8ac2125dde1 | -17.64325 | -42.23979 | 2026-08-03 03:47:00 | NOAA-21 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1a2d42a4-4971-33c1-94e9-af1f9d719681 | -17.86932 | -40.05056 | 2026-08-03 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a8271a77-3b1e-37cc-bd07-a812f0915029 | -16.33607 | -43.33607 | 2026-08-03 03:47:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16e133e7-e9f4-30ce-9854-4a67f96a03f4 | -21.01828 | -40.86139 | 2026-08-03 03:47:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 83d5fe1c-4037-3ca9-a4e0-bad3e78cb6e6 | -18.58373 | -43.83317 | 2026-08-03 03:47:00 | NOAA-21 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68c829b2-3a3f-3e62-8ce5-92997e43de52 | -17.86867 | -40.05449 | 2026-08-03 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 37c262f7-49ff-38b3-b5a4-4eadd1fe2f5f | -21.64388 | -43.05811 | 2026-08-03 03:47:00 | NOAA-21 | ROCHEDO DE MINAS | MINAS GERAIS | Brasil | 3156205 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b79b66ef-9ce5-3314-8a5d-39f63bbbade9 | -16.66665 | -49.13502 | 2026-08-03 03:47:00 | NOAA-21 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bf0f0ff-2258-3515-9adf-a1bfebfd83a5 | -23.5961 | -46.02387 | 2026-08-03 03:49:00 | NOAA-21 | BIRITIBA MIRIM | SÃO PAULO | Brasil | 3506607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ef77704e-5de3-3ee9-85a5-fba0d5af5b7b | -22.89457 | -43.41124 | 2026-08-03 03:49:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c88a2480-0d78-3a25-a6c4-b9ce903602d8 | -23.27959 | -46.09768 | 2026-08-03 03:49:00 | NOAA-21 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| d87171e0-0112-3378-82c2-be56d5f65ba1 | -23.31644 | -47.236 | 2026-08-03 03:49:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e77ce613-1f6b-339e-b175-fca0da71cb82 | -23.57429 | -45.6576 | 2026-08-03 03:49:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2a25421a-4d46-3e0a-a388-9f02ed479665 | -23.57351 | -45.6615 | 2026-08-03 03:49:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5b7c1b22-36cc-3170-a8ea-f8682362650a | -21.50675 | -48.8192 | 2026-08-03 03:49:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c8026058-a98a-381f-b258-0bb570b04afa | -22.89488 | -43.40933 | 2026-08-03 03:49:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c319acf1-e862-36a5-8540-584b4eebc44a | -22.15979 | -47.36582 | 2026-08-03 03:49:00 | NOAA-21 | LEME | SÃO PAULO | Brasil | 3526704 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fa80f6fb-cc07-3be5-a2ad-98a783dd4109 | -23.57837 | -45.65925 | 2026-08-03 03:49:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 91e9630b-346e-354d-9f05-0479040fae0a | -22.68149 | -43.76286 | 2026-08-03 03:49:00 | NOAA-21 | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| f9ffeebe-0b34-37ea-a657-ccddd11f7570 | -15.2256 | -52.9012 | 2026-08-03 03:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 1b2ad9ac-89bb-3ed6-990c-5d6d5a75c908 | -1.6408 | -54.4545 | 2026-08-03 03:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 424e525d-5be3-3992-b77f-1ec1cd8b549b | -1.6591 | -54.4543 | 2026-08-03 03:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| e2a3541e-e23b-32d0-a818-57df2fec3756 | -15.245 | -52.8986 | 2026-08-03 03:50:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 07224f55-7735-3b8c-b64c-e8aa0677c8d7 | -15.2252 | -52.9224 | 2026-08-03 04:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 991f9949-a4b5-3342-b0e3-7fdfa786f3f1 | -1.6408 | -54.4545 | 2026-08-03 04:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 3f4bc28c-ab5d-31c8-b138-b27821a1c368 | -15.2256 | -52.9012 | 2026-08-03 04:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 61f0ea2d-5afc-3fe7-aa69-5b66b3e00d78 | -15.2447 | -52.9198 | 2026-08-03 04:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b6c02721-7993-372b-806a-a5ae119760bf | -15.245 | -52.8986 | 2026-08-03 04:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 139.2 |
| e2c0d608-5383-3bad-9650-1765d4f7e4f6 | -1.6591 | -54.4543 | 2026-08-03 04:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 812a9ed3-359f-354e-a0a7-e8b23815c996 | -1.6408 | -54.4545 | 2026-08-03 04:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 00384832-1b27-370f-9c9f-d89885c10e9b | -1.6591 | -54.4543 | 2026-08-03 04:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 0d62236b-d430-3e0e-8913-ecdf3f6b5df7 | -1.6408 | -54.4545 | 2026-08-03 04:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 4527749a-8b52-36cd-8e18-2d73fc3ccbdf | -1.6591 | -54.4543 | 2026-08-03 04:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 0baab209-1a58-37df-bd66-35d95370efa7 | -1.6408 | -54.4545 | 2026-08-03 04:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 09586401-cae6-3b57-b01e-1c89134783be | -1.6591 | -54.4543 | 2026-08-03 04:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 2ecef8b8-a2d0-3762-a046-b0aed32ea975 | -2.75194 | -49.47539 | 2026-08-03 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db2de554-e13e-3dd7-b3b6-b8f3d98245b2 | -1.64265 | -54.46265 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4557d2fb-e598-3157-b977-075d74a3ffde | -3.11255 | -47.92022 | 2026-08-03 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8561b55c-5b65-30c3-8a7a-ad578387152b | -1.63788 | -54.46189 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 12d7be8d-73cc-3005-8a7a-927cec05b53d | -1.63871 | -54.45672 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 127159d5-369a-3a64-ac68-e4828ee138fd | -3.1131 | -47.91675 | 2026-08-03 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94f594b6-c05a-3cec-97e1-11cc591c7cfb | -3.11642 | -47.91727 | 2026-08-03 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a90ebc48-b365-30e4-93f9-8e7ac795b33a | -2.75663 | -49.46833 | 2026-08-03 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 071d58e8-1736-3d98-8905-fbfcdeb5a5aa | -1.65467 | -54.44885 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6813a8c5-21f3-33c2-8384-93a7facc0256 | -3.02585 | -39.97239 | 2026-08-03 04:36:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b905e914-e9d3-3b1f-8e26-b2ffc9383972 | -2.75255 | -49.47159 | 2026-08-03 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9b3534f-d8bc-32c0-ab8f-93580d4dd8e8 | -2.15816 | -49.11024 | 2026-08-03 04:36:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 131d082d-a0da-3e90-9539-1e308aa35715 | -1.64431 | -54.45237 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6a3b8477-22fb-3228-ac28-ffcf60606afa | -1.64907 | -54.45321 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 536c169b-6cd3-30e7-b652-3d4fc9bc8831 | -1.6586 | -54.45483 | 2026-08-03 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README4.md)
