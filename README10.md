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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c1d83220-0042-3a88-94ae-e96d35f02008 | -8.08013 | -47.1209 | 2025-06-10 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ebcf51a-92ba-3807-9668-75d81b523269 | -9.22379 | -48.86283 | 2025-06-10 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a75c42ba-95e1-38d0-a01e-d0da023c075d | -14.23862 | -45.49118 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29e7dd11-d333-3e6f-a0ba-b51884040dbe | -11.83575 | -60.9255 | 2025-06-10 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de2767cf-6715-39d8-8bbd-2c8e7650758c | -11.90264 | -47.44987 | 2025-06-10 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28aa7b60-6a08-3f93-aa2a-ae89dfd03b80 | -10.277 | -47.60796 | 2025-06-10 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 42effb93-ab59-300f-a841-9962f2d7cacb | -11.13944 | -53.94897 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed67afe1-e226-3b3d-a522-7cf3b70f9f0f | -9.09222 | -49.64784 | 2025-06-10 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cae6adf-81cc-38a6-8ead-311cfeb9c6da | -8.80796 | -49.55286 | 2025-06-10 04:40:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38fa65a3-8cca-3d46-81cf-86f9514a4d2c | -10.22121 | -46.92666 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 08a68f94-af0f-3edc-9c42-acc0d4450170 | -10.65549 | -44.48434 | 2025-06-10 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb2addcf-de85-377c-a8c3-59965c52a9c2 | -14.21285 | -45.49147 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05a2c606-610d-36d0-8a0f-d9c17da768d4 | -9.41284 | -48.43665 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 587f3f6c-3c73-3935-8cef-2cf9b9b401c3 | -7.27401 | -49.57327 | 2025-06-10 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b80c607-a7ea-3e64-ada2-23e74caa89d9 | -11.57739 | -48.13927 | 2025-06-10 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e5d3340-5175-3906-92b5-88cadbdcaa8a | -14.23915 | -45.48718 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 45f80dd8-185b-3f5a-a5fc-ef4bdf144487 | -9.20984 | -48.86433 | 2025-06-10 04:40:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cc614e00-690f-3fe3-9e9e-67078b6c17f8 | -9.7586 | -49.23047 | 2025-06-10 04:40:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5ac22fbf-5e11-38d2-96a5-8be98bd0a29e | -10.21328 | -46.92986 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1ccb81e5-aa21-329d-958f-c630ef54470c | -11.14017 | -53.9447 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69b62887-d3d9-3137-91e9-61eb173bbce6 | -12.71975 | -54.97095 | 2025-06-10 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 24a4fe33-5df9-3c61-8826-273f7d74166f | -10.22235 | -46.94455 | 2025-06-10 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e29b2a32-fab0-3452-b5da-5c16162b5887 | -6.87396 | -47.2485 | 2025-06-10 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9d8125e-c1c0-3e8e-9313-ca325c4c34c4 | -10.30804 | -57.14129 | 2025-06-10 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b5beedd-b585-3c03-a600-feabb553e0be | -8.60952 | -46.56651 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b9a5094a-bd4d-374b-815c-5735ec6cb3d8 | -11.56761 | -47.43949 | 2025-06-10 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abddd1ae-5f6a-3d28-8cbb-af72c9294447 | -10.41164 | -48.18169 | 2025-06-10 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c7a007d-fb4e-35fb-a111-322169833a18 | -12.42657 | -47.80244 | 2025-06-10 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39243f06-c969-3e2b-a901-0ef13cda09ab | -14.19232 | -45.48452 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ee01f9b-19fd-31bc-b1bf-c516e08d7a77 | -8.60702 | -46.58382 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a24aa6d0-30e3-3edf-91e1-5a6f51b72142 | -10.75858 | -44.45513 | 2025-06-10 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d795e67-71da-3bcf-8d12-940da9857c1f | -11.76702 | -54.36982 | 2025-06-10 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be163bbd-0c47-3ed1-bf48-e69ba0f9346c | -13.51885 | -47.86156 | 2025-06-10 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9458dd02-5ee7-3000-96fe-01c6ad94088a | -6.86287 | -47.85444 | 2025-06-10 04:40:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c797a88c-6998-30d2-942e-f4fcbc2c1975 | -14.20495 | -45.48627 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 914a4b88-e9ff-3226-baf5-49e18439e763 | -9.16654 | -50.02617 | 2025-06-10 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a74217d4-0994-3cf6-8e7a-915c39e4b970 | -11.78657 | -54.78139 | 2025-06-10 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24761a0b-9618-3cf0-894c-5877b4dafc9e | -9.39205 | -48.43021 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f29636ef-f8f8-3e0a-975a-85b207fdffbc | -6.87048 | -47.24798 | 2025-06-10 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e27ea455-4310-3c3a-9719-d1d3695d8001 | -14.216 | -45.50008 | 2025-06-10 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e45400d-e13c-3ea1-a359-8ec25959d55b | -11.57122 | -47.44003 | 2025-06-10 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44ee513c-8b0b-3118-8bd5-8873fb991d68 | -10.95436 | -54.38092 | 2025-06-10 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bccd70cb-4b36-34e6-8f3d-1be4df91b87b | -9.39488 | -48.43442 | 2025-06-10 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a527ab0-6208-32cd-a5fc-57d84b2defb4 | -12.29342 | -50.10477 | 2025-06-10 04:40:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e4430849-12e5-3e9a-8ad5-289e578993fe | -7.664 | -46.07982 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c15c5146-ea5a-3f45-99b0-961f5494be12 | -13.06574 | -49.2506 | 2025-06-10 04:40:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96ee0b47-99dc-3b31-a66b-1902d0efaf99 | -8.60399 | -46.57895 | 2025-06-10 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98e1acbf-08ad-30f0-9c03-c1041670cb09 | -10.65122 | -44.4837 | 2025-06-10 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa874f18-18c6-3947-908b-69a5b776a983 | -6.88611 | -47.23848 | 2025-06-10 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0da856fe-9524-3c99-a429-bf68b64f6154 | -11.89901 | -47.44933 | 2025-06-10 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6974c9c-f715-3c75-8ae1-7f3c9b4b244b | -12.21467 | -49.6192 | 2025-06-10 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 657d54f1-e44e-3d18-9555-a51928c9bb19 | -8.96808 | -47.96544 | 2025-06-10 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b000755a-cf1a-396e-bd20-fb65009becf2 | -11.8984 | -47.4536 | 2025-06-10 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa5ce977-4607-362a-af16-98f4cbe2b80f | -11.36924 | -56.55836 | 2025-06-10 04:40:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1263e695-50d4-3c57-969d-7756237e9a1e | -8.41177 | -46.83903 | 2025-06-10 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2f65c787-581e-3a53-b012-6227e911fea7 | -8.316 | -47.91911 | 2025-06-10 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63593c75-5f43-3f7d-845c-c5e4a1e06978 | -7.61675 | -49.92471 | 2025-06-10 04:40:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 763af9b2-1968-3b7f-b840-8a95089a84e5 | -8.96751 | -47.96924 | 2025-06-10 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b88e5aaa-4ffc-315c-bc7e-72c2973c3f81 | -19.38481 | -55.11773 | 2025-06-10 04:42:00 | NOAA-21 | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5e7d71e-e137-36cc-a80d-7edc0710b195 | -18.81732 | -46.43732 | 2025-06-10 04:42:00 | NOAA-21 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 422f82e8-46cf-36bc-a0c7-2c61bb9fb285 | -13.79057 | -54.31473 | 2025-06-10 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43d78ace-63ef-33df-ac2d-4d0b3775790c | -18.93754 | -48.97822 | 2025-06-10 04:42:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77090ac8-3ddd-325e-b737-3e867c942cbf | -20.09921 | -50.87091 | 2025-06-10 04:42:00 | NOAA-21 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 815c342b-a8aa-3143-853f-34b5d41bde79 | -14.03179 | -55.13022 | 2025-06-10 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b8a77de-e892-3e63-9685-e3fda702e87d | -14.02729 | -55.13409 | 2025-06-10 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15692bac-64e0-3b8b-ac37-38f98aad3837 | -13.58735 | -54.28494 | 2025-06-10 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 237ea076-814b-3f3a-ae57-9da5c9583082 | -14.02808 | -55.12956 | 2025-06-10 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b1f4e34-adb0-3edf-a9a9-64f84bb00802 | -15.56882 | -47.85596 | 2025-06-10 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b225647d-b907-359d-9268-014681c27267 | -14.84424 | -52.28346 | 2025-06-10 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 4e6791f7-8da7-36fd-8a08-46aa36028bf1 | -13.59259 | -54.2829 | 2025-06-10 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a38e6da-0ce9-3002-b2dd-7dc87a45f571 | -17.41252 | -49.52799 | 2025-06-10 04:42:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c05164e4-5633-30ce-bf88-d12ec555284c | -17.38117 | -44.99146 | 2025-06-10 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 99476898-56f5-30f0-ad7e-a1055b3b691c | -20.10262 | -50.87148 | 2025-06-10 04:42:00 | NOAA-21 | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1315c36a-0d85-3bc0-a504-434de4b8f7ac | -13.59164 | -54.28135 | 2025-06-10 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b5d9416-6149-3a27-a062-d8b203ae7311 | -20.421 | -45.58486 | 2025-06-10 04:42:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 837a4166-567b-3730-8c4b-84367bd4e26b | -15.38613 | -47.12414 | 2025-06-10 04:42:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cafc6cd-941f-3762-99c1-20761812053e | -12.71026 | -58.03378 | 2025-06-10 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 371618c5-909c-33d4-8c0a-b0c4aff77fbb | -13.58832 | -54.28649 | 2025-06-10 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c37e7b44-636f-3826-8fc3-923a6a1938ce | -12.70996 | -58.03142 | 2025-06-10 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab42f259-365c-387a-a61b-9b105ad99c30 | -15.08027 | -48.94512 | 2025-06-10 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84ec5a56-aa50-33a5-857c-e9bf4ca02eca | -14.84367 | -52.28705 | 2025-06-10 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a33bca9-df1d-39ff-bde1-0bbc8d272055 | -13.58902 | -54.28229 | 2025-06-10 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4580cff-f879-31f9-a81b-78588429e3fd | -16.68374 | -43.88665 | 2025-06-10 04:42:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94745976-79fb-365a-8fc6-93d61903c4bc | -15.36421 | -47.90777 | 2025-06-10 04:42:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61fd88e-5b48-3974-975f-b370ecb4803a | -12.71113 | -58.02912 | 2025-06-10 04:42:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07093133-cfce-3c62-b36a-016669c30801 | -20.08852 | -51.23451 | 2025-06-10 04:42:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff35906f-2b9c-343c-8e0d-5cc04c7b3eda | -14.03257 | -55.12571 | 2025-06-10 04:42:00 | NOAA-21 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6ce846e3-587c-3c14-b236-c8a910aa54ab | -14.54183 | -52.65912 | 2025-06-10 04:42:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2059bcfa-2443-3e28-9c76-2b1ac24ca75a | -13.59092 | -54.28554 | 2025-06-10 04:42:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ea3e9a8-fc45-3766-8b27-a2898651a165 | -20.76383 | -46.77081 | 2025-06-10 04:44:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 957a5223-141a-356a-b775-240ce1ed89f2 | -21.59159 | -57.58845 | 2025-06-10 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b222806d-0cd8-3996-8fff-49bcb21362a0 | -21.75255 | -53.27517 | 2025-06-10 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6bdb717d-7639-3cc9-bc1b-01f6de6e25ff | -21.7553 | -53.2794 | 2025-06-10 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8bc24ab1-2bfa-3cf1-89c5-03924804e06a | -21.0299 | -55.64641 | 2025-06-10 04:44:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1117eb78-a15c-3d99-9e40-aab931122f9f | -20.82363 | -54.95853 | 2025-06-10 04:44:00 | NOAA-21 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 513cf794-8879-334d-acd4-436d2693f262 | -20.99729 | -51.79293 | 2025-06-10 04:44:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 76005d26-5032-3a58-a0b5-57fd3a1dde5b | -22.43552 | -42.69266 | 2025-06-10 04:44:00 | NOAA-21 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 48246131-000c-3afc-b983-4442a99d07c7 | -23.23782 | -51.28655 | 2025-06-10 04:44:00 | NOAA-21 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e8d15f3b-0d0a-383d-8810-245900b34745 | -21.1913 | -55.74121 | 2025-06-10 04:44:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1bc0eadc-6a9a-31c4-8fb7-cb02516be437 | -5.2108 | -43.3067 | 2025-06-10 04:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |


[Clique aqui para ver as próximas entradas](README11.md)
