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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4259683c-a440-3a41-b8db-76bdece3c057 | -5.8789 | -43.245098 | 2025-09-04 00:08:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92728fb9-c45a-3b3d-a637-489a763c188a | -23.2894 | -46.1586 | 2025-09-04 00:08:00 | METOP-C | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 154af4df-d87c-3d5f-9deb-6abcf6833cf9 | -6.2343 | -43.5504 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 800fe903-779f-3c76-bf5e-ea3ad1287c0a | -4.9543 | -42.058998 | 2025-09-04 00:08:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5b2bf8ba-87ee-3342-869b-7015de17e434 | -6.2159 | -42.4524 | 2025-09-04 00:08:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4227da3d-7bf9-3d4e-bcb9-1c1484ef28dd | -6.2226 | -43.543701 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d5740e0-924a-3977-8f27-22ca26b1c690 | -6.2363 | -43.559299 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f57f79b8-7657-3880-9b19-258ef38eb790 | -16.309601 | -45.6889 | 2025-09-04 00:08:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ac6ba081-707c-3fe3-bd70-14425fc2b0e5 | -6.2542 | -43.316101 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c244c0be-b90e-34d8-9104-d9e84efd1c5e | -4.9658 | -42.064201 | 2025-09-04 00:08:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 29a1feef-9101-3508-b94c-042fb1f50f94 | -6.5388 | -43.905998 | 2025-09-04 00:08:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a46180eb-94a5-3f0c-9eac-ecd261a5d06f | -6.1505 | -43.311501 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| b3224f65-9909-3ba6-bce0-9d23ac654e99 | -6.2452 | -42.6292 | 2025-09-04 00:08:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ab203fac-adad-3608-87ab-c676f66f2d86 | -7.6917 | -50.3144 | 2025-09-04 00:08:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b03b7ba5-3977-3b97-8419-88da6c992a6a | -17.166201 | -46.245499 | 2025-09-04 00:08:00 | METOP-C | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd2ac78-af34-3723-a0f8-9fb40412c9e9 | -6.2304 | -43.5326 | 2025-09-04 00:08:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6115edbd-1514-3234-9c8a-09eda0eace05 | -6.8351 | -46.392399 | 2025-09-04 00:08:00 | METOP-C | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bfb8149d-f83c-3736-aa75-28cfe50c9696 | -23.2955 | -46.133202 | 2025-09-04 00:08:00 | METOP-C | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2de24bc5-9b45-3b8a-aba5-581e2807098f | -7.6959 | -50.285999 | 2025-09-04 00:08:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6173eea-56ca-35cf-bb81-8307f134c834 | -6.266 | -43.322701 | 2025-09-04 00:08:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3a1138c1-11b4-3cb5-b00e-e02c11b1dbf4 | -5.877 | -43.236599 | 2025-09-04 00:08:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 643943ee-bc14-37c2-a183-701e8d6ee041 | -5.6073 | -45.028702 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 815406b8-727f-3368-a09c-d2b81b6ed20c | -6.2874 | -43.604401 | 2025-09-04 00:08:00 | METOP-C | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 52a88959-3950-3404-8d7d-ab638d48f1ca | -4.9641 | -42.056801 | 2025-09-04 00:08:00 | METOP-C | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf71b98f-4385-327b-99f7-0a6163945c24 | -6.589 | -44.3209 | 2025-09-04 00:08:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4da407f-0eba-3c10-ac60-bc584bf5b6c1 | -5.5928 | -45.009499 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d54e874b-1961-3256-b019-2392cdfd4eb4 | -5.6026 | -45.007401 | 2025-09-04 00:08:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7244cba8-ae77-390d-b67e-13d32fa927a0 | -6.1188 | -42.938202 | 2025-09-04 00:08:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 560484e7-cb6b-3bfe-8806-0e7231a33321 | -6.7931 | -44.4546 | 2025-09-04 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 1540b38e-487c-31d8-a866-b7503bf63694 | -11.2005 | -55.0195 | 2025-09-04 00:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| fb84b5ba-77a2-3d0b-afa6-9f367310eec0 | -6.797 | -44.0859 | 2025-09-04 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| c742bc34-a4bd-3c2f-ba94-b9e261bdea3a | -6.7933 | -44.4316 | 2025-09-04 00:10:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| da4b344f-0d87-3ff2-aa44-f859e8581a0e | -9.4833 | -47.6104 | 2025-09-04 00:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 474bc549-6c3a-3a20-9a89-b1c2460bd9a1 | -10.4661 | -50.3693 | 2025-09-04 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 1f303ebf-4f66-3f9e-b0eb-dd60655d4f8f | -13.75 | -46.9346 | 2025-09-04 00:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 3a85b193-620d-3879-accc-355b96e72aa3 | -6.7832 | -63.1474 | 2025-09-04 00:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| a20a58ad-e286-3e88-9676-e6769fe6ebda | -4.9951 | -56.256 | 2025-09-04 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 38d70c14-00f6-33b9-84d1-e0a7867fcc5e | -2.9434 | -49.3655 | 2025-09-04 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| fe82f4a1-10c9-349b-854e-513977e0ef90 | -5.6077 | -45.0492 | 2025-09-04 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 39c1a002-cff9-3103-b927-6f62bacbf5b5 | -12.9859 | -54.7891 | 2025-09-04 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 5c1321e3-e1b8-3b80-b975-982f6de8d19f | -18.131 | -51.7752 | 2025-09-04 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 297.2 |
| a353f637-4245-3285-b160-32cb71b797c6 | -12.9668 | -54.791 | 2025-09-04 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 126.0 |
| b34da29b-a368-38ca-bc3b-d01bfc20aa54 | -5.6081 | -45.0038 | 2025-09-04 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 206b08b4-c61b-3ed8-ba47-477a75e827d4 | -20.1024 | -44.118 | 2025-09-04 00:10:00 | GOES-19 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.5 |
| 1ebb1141-6882-32ae-863d-798331dc1b2a | -8.6604 | -68.7473 | 2025-09-04 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| f06ef564-1fd2-3e21-8f5b-fabacdb51857 | -7.6492 | -63.1008 | 2025-09-04 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 8c0ae3db-041e-3253-ba6d-4b00a189cf87 | -12.6341 | -56.9926 | 2025-09-04 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 533c7ba8-9015-3af4-a5a8-842c0cbaafc1 | -2.9804 | -49.3644 | 2025-09-04 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 43b8d06e-fbc1-386a-9f08-8596cdaaf005 | -11.6599 | -54.5297 | 2025-09-04 00:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 163.3 |
| d44d519d-f87f-3cf5-8a9d-da8e2ee94161 | -10.4469 | -50.3926 | 2025-09-04 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c33f45f9-4480-3677-b9c8-41927d0eb958 | -7.7066 | -50.3188 | 2025-09-04 00:10:00 | GOES-19 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| ea80d9ba-22c8-3fc7-9d70-799806495fe0 | -5.6266 | -45.0252 | 2025-09-04 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| cb8733f1-6e5d-3ccb-bc5e-b99d63e06c79 | -11.5969 | -52.113 | 2025-09-04 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| f19a060e-45ed-3613-8763-2ceeab533f4b | -6.7782 | -44.0876 | 2025-09-04 00:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| c5fbfd44-90d7-308f-952b-ac8151b1a7d7 | -12.9861 | -54.7685 | 2025-09-04 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 97fbaa04-56ef-33c6-8269-21ccc1195aba | -10.4472 | -50.3713 | 2025-09-04 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 5a6dab10-f7e0-33d0-b529-9295fd09d2bc | -18.1505 | -51.7937 | 2025-09-04 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 218.3 |
| 8d660a89-ceee-3af0-bba7-ebe2ed0f8ae8 | -8.6603 | -68.7657 | 2025-09-04 00:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b2a21bf3-e578-382c-ac38-c08b25b28b13 | -2.9619 | -49.365 | 2025-09-04 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| fbb1414e-d9c7-3b7c-bfbe-4bb4b59b9794 | -5.0135 | -56.2553 | 2025-09-04 00:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| f5453888-3257-3926-b987-d8348eb2aa0a | -5.8896 | -57.7318 | 2025-09-04 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c1f9f18d-d173-3841-82cd-5c0fc4d3c706 | -7.6307 | -63.1015 | 2025-09-04 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 2fb82ea6-bdc6-39bd-b4e9-6d716bffe5c7 | -13.7495 | -46.9573 | 2025-09-04 00:10:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| efd00e45-7ed6-3cc6-8bbf-d20228793481 | -5.6079 | -45.0265 | 2025-09-04 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 291.7 |
| 93924929-5053-3861-aa8f-80425f5037e9 | -10.4664 | -50.3479 | 2025-09-04 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 30caa34a-a6ca-37ae-8b92-7306427bb3ba | -4.9589 | -42.0523 | 2025-09-04 00:10:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 54.3 |
| dcbcbf1b-9229-3c6a-b37e-a619f4332595 | -6.7833 | -63.1286 | 2025-09-04 00:10:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| bc8bb8c2-274f-3978-977c-a2607815481e | -7.6306 | -63.1203 | 2025-09-04 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 1abe27c7-2c90-388e-8bc9-a477c98a0d4b | -11.5779 | -52.115 | 2025-09-04 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 0935834a-1ed0-3527-ac35-c04e90e29953 | -18.1305 | -51.7971 | 2025-09-04 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 256.5 |
| b7ce5d55-e59c-3d3d-94f3-c9f27a9e0940 | -10.4475 | -50.3499 | 2025-09-04 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2f761d97-d81a-35b4-a2b5-59d475bff2ac | -11.8708 | -51.5357 | 2025-09-04 00:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| ed58f574-d087-32c5-a1c4-503662fe106d | -11.0568 | -45.146 | 2025-09-04 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| aeb7cd00-791b-3437-8705-122d026666a6 | -2.962 | -49.3437 | 2025-09-04 00:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 2d9f8b0d-c53d-3615-b67d-2b9c8e87a0a8 | -5.908 | -57.7311 | 2025-09-04 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 5eb3a360-5af4-3437-ab4c-e927135e2701 | -18.151 | -51.7719 | 2025-09-04 00:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 247.6 |
| 4ec811d3-9904-3dcc-9d3c-d9bcb93c8622 | -7.6491 | -63.1197 | 2025-09-04 00:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 5685aba5-2a43-371c-a22c-3f652bf5e995 | -12.967 | -54.7705 | 2025-09-04 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 30ed96f3-aa66-385e-80ca-12c02939bd04 | -13.75 | -46.9346 | 2025-09-04 00:20:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 99.5 |
| a484b7ab-8051-3003-adc4-ad4b439a08f0 | -10.5129 | -57.776 | 2025-09-04 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 6cb5bfef-2864-386d-a656-f2f70b15b0d1 | -12.967 | -54.7705 | 2025-09-04 00:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| ec93500b-3516-327a-8767-1995f2e3b08d | -11.6601 | -54.5093 | 2025-09-04 00:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| cd0d3789-c410-3544-a378-c8ecc89ec6b7 | -10.4469 | -50.3926 | 2025-09-04 00:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 6414afcf-51e7-3205-9199-bd41ec713539 | -5.8525 | -57.7722 | 2025-09-04 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| ed417502-3ac9-3781-9056-deaa220489d0 | -5.6079 | -45.0265 | 2025-09-04 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 214.5 |
| d421b805-0d5e-38c3-b893-1ceba51fad56 | -22.6567 | -43.6825 | 2025-09-04 00:20:00 | GOES-19 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 64.1 |
| 601ebbb9-83dc-30b1-b5ee-aeb458829a5e | -18.131 | -51.7752 | 2025-09-04 00:20:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 7df3256c-deaa-3073-b42c-9f646e647f72 | -8.0799 | -45.339 | 2025-09-04 00:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| ffcf8a84-c104-3576-8683-c798542ce94e | -6.7782 | -44.0876 | 2025-09-04 00:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| d874a8c1-8bf7-3e56-a370-bb120a5045f9 | -6.2484 | -42.6394 | 2025-09-04 00:20:00 | GOES-19 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 553b6fa7-f064-30c4-9798-abfd9f257fc0 | -6.7833 | -63.1286 | 2025-09-04 00:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| ab45c13b-f989-347d-9c43-18e5cc02ab28 | -5.6266 | -45.0252 | 2025-09-04 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 08580b26-587c-3a02-be38-0f6a22aa12da | -11.5779 | -52.115 | 2025-09-04 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 86829519-0515-3d55-9a73-d74a5dc76913 | -2.9619 | -49.365 | 2025-09-04 00:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 9e600824-9142-3a6f-b398-ac97fef892f2 | -6.7832 | -63.1474 | 2025-09-04 00:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 12a1fadc-0e48-3d98-9698-963deedaa87d | -5.5892 | -45.0278 | 2025-09-04 00:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 7e7fbdbf-58cd-3555-b6f2-517dbb76ee2d | -8.3641 | -48.3334 | 2025-09-04 00:20:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| d85b35a6-1180-3d54-8045-8ac974cc2843 | -7.6675 | -63.119 | 2025-09-04 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7cf3ef3a-0b5a-3d3c-8d82-6423bb9c6f8b | -10.5316 | -57.7747 | 2025-09-04 00:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 22393bae-897b-3eaa-8cd3-0019cbd304c8 | -7.6307 | -63.1015 | 2025-09-04 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 90.9 |


[Clique aqui para ver as próximas entradas](README5.md)
