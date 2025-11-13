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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36b00636-c4ce-3682-bba8-8ad44983bc47 | -5.30934 | -40.90755 | 2025-11-13 04:12:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2e4e1f2f-7ffe-32ff-8782-62061bdd6cbd | -5.5931 | -41.09234 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8cd4bc2e-c81f-3f28-b6e1-c9e447cf6cc8 | -4.64179 | -48.7519 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4c6e826-7b4a-358e-9f06-fe71af1eda8a | -4.69334 | -49.65275 | 2025-11-13 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 663c1cc1-fbf5-389f-803e-998fae6e1c9e | -5.31465 | -40.92343 | 2025-11-13 04:12:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 96451e70-367e-33b1-a5ea-c765847fbf29 | -3.9549 | -44.42245 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc810b03-728f-374a-a415-84f718432966 | -4.45144 | -38.39516 | 2025-11-13 04:12:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5dbb2464-3317-306c-bd7a-96af2875e90f | -2.52706 | -47.80726 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4ae14c40-27ef-3559-8f61-0ae442a91836 | -5.32822 | -35.55519 | 2025-11-13 04:12:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 92946dfe-7827-3f93-a18a-821a05ee78e8 | -5.25747 | -36.64816 | 2025-11-13 04:12:00 | NOAA-21 | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6406fc09-a0bc-32d2-a8be-bbbd85a01808 | -2.17364 | -48.37207 | 2025-11-13 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 32e41ef6-9116-33c1-be0a-8b6d794dd1a5 | -2.73239 | -45.47894 | 2025-11-13 04:12:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 22a0dced-9dcf-3a9e-a11a-55912a2b9366 | -2.4523 | -49.25996 | 2025-11-13 04:12:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5496365f-62fc-3b07-82b3-cadf304022a6 | -5.41468 | -42.56918 | 2025-11-13 04:12:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d818acf4-8d73-33f4-93ce-723bb57bb264 | -6.10893 | -41.53241 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 31c04a40-34d7-35e1-95bd-d98987287d0c | -4.68767 | -45.8516 | 2025-11-13 04:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4fd5ad22-a05b-385b-8fdd-b969ff713b72 | -4.45609 | -46.55968 | 2025-11-13 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c1e42653-3b4a-389e-988e-c39ed7cb151a | -4.71805 | -46.45255 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18de57e8-dbf9-3c21-8e2a-d7583dc35b4c | -3.95431 | -44.42618 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 06cd6120-f7b9-39de-be1a-bf766450d00e | -4.24211 | -49.67268 | 2025-11-13 04:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33589867-affd-3263-9ad2-1639bb95862b | -5.16062 | -44.6595 | 2025-11-13 04:12:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e873fba4-3fe0-3da9-bcaf-dfe6e62f2144 | -4.09888 | -48.02076 | 2025-11-13 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7455d944-0074-38df-8692-09518e1ccbb9 | -6.10463 | -41.5829 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 810ab5ce-ba2e-3e8d-b837-fefddcd2623e | -6.10182 | -41.5788 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a7b14e23-f7bc-366a-85a4-76499d303ba4 | -5.90106 | -42.26341 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 4fefd0d9-a6a1-3262-b304-8f626a813621 | -3.78261 | -42.75547 | 2025-11-13 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 86950b58-509c-3ac3-87d5-df90353249b8 | -3.29177 | -52.1114 | 2025-11-13 04:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79b459cf-19e0-32c7-8b5a-1f0dc2985039 | -4.21116 | -48.57107 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| c87a921b-5e25-3b23-bb71-360c152b9078 | -3.86043 | -49.79741 | 2025-11-13 04:12:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8cb325a0-65d0-35e7-a6c7-eb1f1f3a3e9f | -3.12679 | -46.03763 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04cc2119-f9c1-356c-b4e3-c08f5b4ad27e | -5.32385 | -45.19389 | 2025-11-13 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| e01fec25-0a65-3bc1-8046-e55d937d6d7e | -2.4324 | -48.04842 | 2025-11-13 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da13e214-325d-3b7a-a354-6c56059a53de | -6.35614 | -39.79346 | 2025-11-13 04:12:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fdb26592-652d-38b9-ba10-61d9be8e1fe4 | -4.21049 | -48.57508 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 5bb273e7-5d00-3118-8ea2-9750fb8dd42f | -4.61318 | -42.79829 | 2025-11-13 04:12:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbef3cb5-c89d-35bd-a258-fd673d357327 | -5.56147 | -41.04985 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 99be3604-a213-33f3-b0e8-73ca4b57241e | -5.89166 | -42.25839 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 420c1a1b-779e-3751-8d23-ed9215c5dd88 | -2.16924 | -48.37139 | 2025-11-13 04:12:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 674ea065-03ab-396d-8895-6c081915f4ac | -3.39817 | -50.17842 | 2025-11-13 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2093d02d-d0d2-379a-981c-fee90b48c31b | -3.13149 | -49.24417 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f70f136-d893-310c-a46d-af646b50197b | -3.16353 | -50.62533 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74dd3d79-938f-35c8-96a3-64d1fbc04476 | -1.794 | -48.06996 | 2025-11-13 04:12:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a8d03d1-5be6-3b9b-b233-f7ebfca96005 | -6.08585 | -41.63823 | 2025-11-13 04:12:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab96a6b0-e290-3c5c-ad9c-cf2a0a4ec391 | -4.42608 | -40.74383 | 2025-11-13 04:12:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 27a3a871-2883-39a3-b48d-4737952ebb1e | -3.15127 | -45.8155 | 2025-11-13 04:12:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6bcb914-fbec-3448-8039-6d7d4a1f54b1 | -3.37408 | -48.41 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 50f960ae-0771-3b20-8da7-d1e2a7c10747 | -4.60569 | -43.38585 | 2025-11-13 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60c893c8-0441-3865-b0f8-b896a893b2ec | -3.14473 | -40.18002 | 2025-11-13 04:12:00 | NOAA-21 | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| b545409c-eafa-383d-b4b2-5b17e0105596 | -4.93682 | -48.54695 | 2025-11-13 04:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7001b51-11a3-3811-835e-bafe30f36deb | -4.70781 | -47.01535 | 2025-11-13 04:12:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 896bc216-4820-39a6-a649-2522d0601783 | -4.10367 | -48.01762 | 2025-11-13 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1712ca27-31fc-3581-bc7b-f2a131289394 | -3.8496 | -40.95343 | 2025-11-13 04:12:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8f08456e-eb4d-3c34-8387-6f84c21fa19a | -3.08938 | -49.27405 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e6070b1d-58c1-3a9d-b7c0-4b2195ebf184 | -2.63989 | -49.20125 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5468aaf-3fd8-38a7-a2a5-44240353f817 | -3.08553 | -49.26855 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9957bb35-5e2b-3ead-8c6f-d699c588c47f | -5.59366 | -41.08871 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8cc4e5f5-9c45-3bbe-a402-dfabaefe7d34 | -3.15896 | -50.62154 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6221fdc-132b-318a-969b-67cdc45f8bda | -4.63744 | -48.75123 | 2025-11-13 04:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f3ee5d5-0902-3ca7-8780-297c5851a2ef | -5.58971 | -41.09184 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1846266c-149d-3de3-b51d-ff9cb296887e | -4.04394 | -46.12376 | 2025-11-13 04:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 280099c4-defe-32a5-8431-9635de8a8ee9 | -3.46898 | -43.1918 | 2025-11-13 04:12:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 99d646a7-2f04-36a1-a760-b230f96b93e5 | -5.74579 | -42.73443 | 2025-11-13 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5ae57202-a4c2-38a8-9223-933ece290afa | -5.32322 | -45.19773 | 2025-11-13 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 8f27fffa-96f5-3489-acd4-27fd97c8fdef | -4.26446 | -46.84918 | 2025-11-13 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c69f20f-7c80-33bb-9266-9d897aababda | -5.59534 | -41.07782 | 2025-11-13 04:12:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7ff4d0c0-2ee6-3e18-9cbb-0902d648ba1c | -2.15855 | -47.56048 | 2025-11-13 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9e75f307-2d3e-3270-8f31-5469748b9227 | -4.57023 | -41.54586 | 2025-11-13 04:12:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1d0c56ab-183f-3280-a751-f43d5ca5cb6c | -3.46676 | -43.1843 | 2025-11-13 04:12:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a8ac5616-f264-3831-a92b-fe3e0a94dc3f | -0.72024 | -48.64503 | 2025-11-13 04:12:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2b208bd-850e-327d-88e0-ed94065d29d3 | -4.5122 | -41.96457 | 2025-11-13 04:12:00 | NOAA-21 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2fb55b04-f676-30cf-99ec-9e14b31f82b7 | -3.15847 | -50.6245 | 2025-11-13 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be70ec36-a868-37b7-ada5-416f165e1e38 | -5.44514 | -44.6586 | 2025-11-13 04:12:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2e33f6fa-a163-306c-ba9d-fe3952f1d6d2 | -3.46344 | -43.18379 | 2025-11-13 04:12:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c40c4859-7b84-396d-b438-94a3f7286d1c | -4.71952 | -46.44349 | 2025-11-13 04:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d55f0655-714e-3a63-bb80-9da3eb5b08c5 | -2.62982 | -49.20473 | 2025-11-13 04:12:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a24120dc-232a-3439-ab80-7b616ced143b | -2.8664 | -51.46952 | 2025-11-13 04:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 83c0b82a-9422-313d-b302-9fb410933dc1 | -4.84563 | -42.37708 | 2025-11-13 04:12:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fc7abc5c-4162-30d0-b30c-85fbe6b16408 | -4.10785 | -48.01826 | 2025-11-13 04:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c58ac86a-524a-3220-b0fe-0f5284093f74 | -5.36392 | -45.07803 | 2025-11-13 04:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dba4b0e3-80a5-308f-944e-5de6ce6511ba | -3.58318 | -41.72699 | 2025-11-13 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 81bfafd0-4d0d-387b-96fb-01ea3c19f69d | -2.89083 | -48.07745 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a4807d7-5e37-3be8-89f8-71100a83e35b | -3.46399 | -43.18031 | 2025-11-13 04:12:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec12b903-3e15-3c13-aa6d-a3b9f664acec | -2.8951 | -48.07807 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f1eec4cf-1f67-3543-89c6-3b3119f83473 | -5.26249 | -42.99619 | 2025-11-13 04:12:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e583adf2-fe4a-3d9b-9987-f83eeb11dba8 | -5.25374 | -46.17866 | 2025-11-13 04:12:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e4fff80-ea70-3861-8b3a-d19187316fcc | -3.34157 | -48.37956 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a3838e3e-555b-3b03-8546-226d7714233c | -2.90133 | -48.0668 | 2025-11-13 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d96b3992-0c67-370d-9e3a-dd320fdb571e | -3.67026 | -45.68984 | 2025-11-13 04:12:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d10ac22-c0f4-3b55-970c-0e22252f60df | -4.68337 | -45.85522 | 2025-11-13 04:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8e87d65-8ccc-3076-a8ce-468a5bd5e512 | -3.57117 | -44.16236 | 2025-11-13 04:12:00 | NOAA-21 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68185142-158f-3e5c-b710-968fdbbfabcf | -2.39732 | -49.39309 | 2025-11-13 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3917fae4-7d57-3873-8157-17ef47b3568d | -5.89663 | -42.74736 | 2025-11-13 04:12:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd00b3c6-0b12-391e-9a1d-7b00b04b0bc3 | -3.34025 | -48.38775 | 2025-11-13 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53f32a42-214f-35b2-956a-351297782ca0 | -4.45684 | -46.55511 | 2025-11-13 04:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 878c1cbb-5596-3234-9f43-af58e4704380 | -3.76785 | -47.72637 | 2025-11-13 04:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69cc6b0e-3471-3e8b-86df-caac6ed8ca60 | -4.56116 | -45.77723 | 2025-11-13 04:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d82a6f9c-34ed-3639-b1f5-7a92b55dae7f | -1.79246 | -48.06973 | 2025-11-13 04:12:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76e5dc3d-4c1d-3e0d-89a5-2f82d06a2b14 | -4.93255 | -48.54631 | 2025-11-13 04:12:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16683cc7-3a8c-3fa2-920d-7cc76d07fa7b | -3.40397 | -50.1738 | 2025-11-13 04:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bf503f64-8728-35e2-9e38-78797ec52b6f | -3.22506 | -45.58976 | 2025-11-13 04:12:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 26.6 |


[Clique aqui para ver as próximas entradas](README16.md)
