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
| 24a80507-8359-3c08-b498-258eebca0504 | -3.29293 | -51.93143 | 2025-10-31 01:13:00 | TERRA_M-M | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| bc8f2c1c-3b3b-381a-812d-e49195079fd9 | 1.28014 | -60.44765 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 23bcc540-5b1b-3a08-9c4e-3cfdbd0ec3d4 | 1.32091 | -60.41654 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 848a2fd7-458f-359b-b4fb-2ce64913d024 | 1.29157 | -60.43086 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 83b1ea85-61e0-377e-84e3-51359f3c25e1 | 1.29282 | -60.42183 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 1fe0e78d-c720-3818-bf12-d3d437e20afb | 1.28263 | -60.4296 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| afda0881-3d1a-36b1-b342-8bbb2e820411 | 1.32216 | -60.40751 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 58fa9c82-c085-3642-b579-f86bb2edeaf2 | 1.2712 | -60.4464 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 34c6b2ee-5354-3f51-9e7e-ef02d60cc712 | 1.28138 | -60.43864 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 1f1fff8f-1eb2-36fa-88d3-7fbc93058ae6 | 1.29032 | -60.43989 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 91ad465f-5abd-3ff8-a2aa-30f0bb7870f0 | 1.27245 | -60.43738 | 2025-10-31 01:15:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 7737c4ff-a080-3dac-8d58-4119bbaa20cf | 3.1338 | -60.70516 | 2025-10-31 01:17:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4631de57-62c9-33b3-a618-eef9314c5475 | -4.5584 | -45.6335 | 2025-10-31 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 4f9bbb19-dcf1-3bcc-88fa-edcc2e6bcbd9 | -9.8631 | -44.8425 | 2025-10-31 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 208.1 |
| aaf79a0a-1192-3bda-8aa5-2345244b2658 | -14.2535 | -45.9837 | 2025-10-31 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 168.9 |
| e2c482cb-27cf-3779-89ab-e7847276756a | -5.0401 | -43.5973 | 2025-10-31 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| f4b4c97f-a3b2-3a35-bebf-16daf3aeffaa | -5.0399 | -43.6205 | 2025-10-31 01:20:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |
| d89859aa-0025-300c-8412-cab1636d687a | -14.2729 | -45.9803 | 2025-10-31 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 3108b93d-3ba5-3027-a1a8-a26a425775ff | -5.0607 | -45.7613 | 2025-10-31 01:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 08eee911-e5a8-3c77-b4f9-bbff9262b568 | -8.101 | -45.1549 | 2025-10-31 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 258612e0-33e7-3818-a73d-3dabfeccc1fe | -10.9397 | -44.1663 | 2025-10-31 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| cc2b971b-e286-3e49-bdce-454e900c62d3 | -12.1548 | -47.9968 | 2025-10-31 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 67db3b4a-99ed-3335-8204-57bbfaa34b74 | 1.2852 | -60.4265 | 2025-10-31 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 57fdba0f-24e1-3867-a8d5-0cd3196ab296 | 1.2852 | -60.4454 | 2025-10-31 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 88cd3c0b-3c2a-3f69-831d-d97a92b76b7c | -2.3178 | -48.5717 | 2025-10-31 01:20:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 59fdc750-c4fe-30c2-8532-96d99ca6130c | -14.234 | -45.987 | 2025-10-31 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5da86377-a934-3340-a239-5a93efb51776 | -5.0793 | -45.7601 | 2025-10-31 01:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3438ab64-eeed-309e-bfd0-2654775a018e | -4.5583 | -45.656 | 2025-10-31 01:20:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 45.6 |
| e3f99398-61f8-3cec-90de-5aee56256e99 | -9.9869 | -36.3578 | 2025-10-31 01:20:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 04719b83-7c6d-3551-bcdd-e35fe289703c | -10.9401 | -44.1429 | 2025-10-31 01:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 6305c242-a99a-310b-984f-7d59b0864901 | -10.5458 | -48.7002 | 2025-10-31 01:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 40311d85-d72a-333b-9aad-1ede758274d0 | -10.5293 | -44.7798 | 2025-10-31 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 105.1 |
| 58cf7826-e9bb-3f28-956e-bffbb2a49804 | -4.0634 | -47.4943 | 2025-10-31 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9f491e82-d805-3556-8331-c33e98cdff62 | -10.5483 | -44.7773 | 2025-10-31 01:20:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 145.5 |
| 6d93c926-2fe7-3d7e-b48e-e9bda5775cb1 | -5.7072 | -48.8784 | 2025-10-31 01:20:00 | GOES-19 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b3bcfed5-7887-3970-ba90-bffe9de3ebde | -9.8627 | -44.8656 | 2025-10-31 01:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 83e816d3-ac09-3bd5-a166-ed3fe72b6745 | -14.253 | -46.0068 | 2025-10-31 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.9 |
| a8791020-e8fe-3ec8-8725-94dd1f726e5f | -10.4005 | -44.4963 | 2025-10-31 01:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 482701ca-6548-323d-8785-3bcbfdff4e8a | -5.0401 | -43.5973 | 2025-10-31 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 45df6ed1-c7d6-3ef4-8cf6-00004ca668da | -9.8627 | -44.8656 | 2025-10-31 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 4626c63e-6683-362a-80d5-1be22ee4cd9a | -9.844 | -44.8449 | 2025-10-31 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 50.0 |
| ba0666a4-9608-303b-a2b4-77f321a3ca20 | -5.0212 | -43.6218 | 2025-10-31 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 87e0f3a5-e704-3fe1-a99e-084ed7a1ae51 | -10.4196 | -44.4937 | 2025-10-31 01:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 7f5b57a8-b90d-3b01-9fd4-21e2c783b2d9 | -4.5583 | -45.656 | 2025-10-31 01:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 0ff7416a-1989-3a4c-8098-151f13790260 | -5.0399 | -43.6205 | 2025-10-31 01:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| fdd67e45-c5ca-3920-9325-6935ab3096b1 | -2.3178 | -48.5717 | 2025-10-31 01:30:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 0f276c86-2ded-3818-af96-ca18c4ca329a | -14.2535 | -45.9837 | 2025-10-31 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| a2c155a5-f329-3212-a790-f69dfa8fff16 | -9.8437 | -44.8679 | 2025-10-31 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 7d8f1bdb-fcf2-3c6d-ac5a-8a0c8215ebc8 | 1.2852 | -60.4454 | 2025-10-31 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d09f206b-84e4-3975-80e5-42fdae9bb19e | -9.7421 | -48.0228 | 2025-10-31 01:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 5ffe7f5e-a27c-372b-a239-278e87c64f77 | -5.7072 | -48.8784 | 2025-10-31 01:30:00 | GOES-19 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 51f8bb9b-f0e6-3edd-8014-fd9ddd0c9e85 | -4.5584 | -45.6335 | 2025-10-31 01:30:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 4ed05001-fcb9-373b-b3c2-aa1a849fecb2 | 1.2852 | -60.4265 | 2025-10-31 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8eb02c9a-ebe2-39ed-8042-ce8833c959b5 | -9.7232 | -48.0248 | 2025-10-31 01:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| e0a999b8-5e74-3fdd-9b05-8879c424a2bd | -12.1544 | -48.019 | 2025-10-31 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 3f9400c5-5b44-3b9c-9d48-ffc79e0a23e5 | -9.8631 | -44.8425 | 2025-10-31 01:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 0e14b959-6911-31b7-a026-55a9ccc18d6c | -14.253 | -46.0068 | 2025-10-31 01:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| da84e4ad-de46-3bee-81be-0e6a16d41d46 | -5.0793 | -45.7601 | 2025-10-31 01:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 21e80538-47c3-3ccf-94f3-ba1c56ee316c | -10.5483 | -44.7773 | 2025-10-31 01:40:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 2aeac038-052c-3255-aaca-c4d919f7f17a | -14.2535 | -45.9837 | 2025-10-31 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 5dfa2f76-1844-3fa3-b499-f79a59860b06 | 1.2852 | -60.4265 | 2025-10-31 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.2 |
| efaf1b17-150c-3bb2-b28f-6635ed38dd3d | -9.7421 | -48.0228 | 2025-10-31 01:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 90e87b43-7a57-3615-b289-13d0cbff8293 | -9.8631 | -44.8425 | 2025-10-31 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 449e1d28-23d4-36e4-9732-a28f3d365b84 | -10.5458 | -48.7002 | 2025-10-31 01:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| a965cf2d-548a-3506-9769-0437d35f5b10 | -14.2729 | -45.9803 | 2025-10-31 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| f5765a0f-8140-3246-9db6-1705e86abcab | -5.0401 | -43.5973 | 2025-10-31 01:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| acbf3a62-05de-3270-b19d-6c8f168096b2 | -9.7232 | -48.0248 | 2025-10-31 01:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 85.7 |
| aa48a24e-6e7c-3048-a64b-cc1ea8d52617 | -14.253 | -46.0068 | 2025-10-31 01:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| dbcc9d37-24f7-36b3-9e0f-bf2d54770482 | -5.0399 | -43.6205 | 2025-10-31 01:40:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 147.2 |
| 0c8c40e8-9846-31fb-9afd-b74eba9dd70c | -5.7072 | -48.8784 | 2025-10-31 01:40:00 | GOES-19 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 785d9210-8f11-37cc-bcbe-854046277fc0 | 1.2852 | -60.4454 | 2025-10-31 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.3 |
| fc5e2bf7-16c1-339f-8363-ca3cc699ec4f | -3.5252 | -47.5389 | 2025-10-31 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| aad059d9-5343-3a2b-a747-ba5a91236cdc | -9.8627 | -44.8656 | 2025-10-31 01:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 68.9 |
| a07fbaf5-2c72-3d44-9df2-da289d3a79a8 | -2.3178 | -48.5717 | 2025-10-31 01:50:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| c1cc2b06-ffa4-3aa9-8671-dbf2f96242ef | -9.7421 | -48.0228 | 2025-10-31 01:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 3333b221-e8fd-38ec-b9be-b215a01fe92c | -9.8631 | -44.8425 | 2025-10-31 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 80.1 |
| b14952cf-9c7f-3b2f-b127-388c5abf541d | -9.8627 | -44.8656 | 2025-10-31 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 77.3 |
| c98f6c42-626e-37d5-a026-e3dfa904652c | -5.0212 | -43.6218 | 2025-10-31 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 46d8a81a-41ca-313a-baa0-89ca1897afd1 | -14.2535 | -45.9837 | 2025-10-31 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 69e0eedf-5e3f-3009-a08e-3a1091952d63 | -5.7072 | -48.8784 | 2025-10-31 01:50:00 | GOES-19 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 085c3504-fe82-3011-9f17-185e820e4a7e | -14.2725 | -46.0034 | 2025-10-31 01:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 853a5c8b-fce2-3bdb-b651-44e768a96768 | -14.253 | -46.0068 | 2025-10-31 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 122.0 |
| a87304f6-edc9-3421-ab95-3cfd535be930 | -5.0399 | -43.6205 | 2025-10-31 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 5dc9368b-bccd-3f69-a349-493f936b4ef5 | -14.2335 | -46.0101 | 2025-10-31 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 1e35ed68-b7da-3f9e-8258-2d86f129caa8 | -5.0401 | -43.5973 | 2025-10-31 01:50:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a79768e6-0c1f-3d8a-beb2-359c5b1e5d8b | -14.2729 | -45.9803 | 2025-10-31 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 7a95bdbd-c082-3ec6-9d50-e1f82e7bd8f1 | -14.234 | -45.987 | 2025-10-31 01:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 0f4cce97-c467-3137-8ffc-36632ff8390e | -9.8437 | -44.8679 | 2025-10-31 01:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 43.2 |
| 09ba6a26-7180-3d50-b2c6-5f6312d26841 | -10.5293 | -44.7798 | 2025-10-31 01:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 59.9 |
| a825951b-a0e7-3e4c-8fe4-91a47d403052 | -8.0824 | -45.134 | 2025-10-31 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 33f5d85b-fe12-310e-b9f6-83b25737b88d | -5.0401 | -43.5973 | 2025-10-31 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 734aa70a-4c0f-360b-8cd0-8f1dcf1599c2 | -2.3178 | -48.5932 | 2025-10-31 02:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| c6e0f6df-e308-3908-ac30-9c2ee2a6f9ac | -14.2725 | -46.0034 | 2025-10-31 02:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 0b559d27-66ee-39b0-a1ae-ddd28e79e4e7 | -9.8627 | -44.8656 | 2025-10-31 02:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 9ab934b2-e534-3b25-8ba0-17ab6618cf7c | -14.2335 | -46.0101 | 2025-10-31 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 450235be-99d1-3ba1-b2d9-d4cbf37dca60 | -5.0212 | -43.6218 | 2025-10-31 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 58574256-4e76-39aa-8a8c-82f28179c39f | -10.5458 | -48.7002 | 2025-10-31 02:00:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| a9cd4624-5182-306a-93f5-412e08764afb | -14.2535 | -45.9837 | 2025-10-31 02:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 124.1 |
| e0adc02a-7973-392a-98ce-96d42ebff75c | -5.0399 | -43.6205 | 2025-10-31 02:00:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 121.6 |
| 6626f141-34f5-3344-97c0-399ae04801b6 | -2.3178 | -48.5717 | 2025-10-31 02:00:00 | GOES-19 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |


[Clique aqui para ver as próximas entradas](README5.md)
