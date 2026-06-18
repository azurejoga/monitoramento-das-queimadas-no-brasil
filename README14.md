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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 99cb8604-c882-3dec-8d86-80f884a5baa0 | -14.08928 | -59.46552 | 2026-06-18 07:26:00 | AQUA_M-M | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 1f4ab878-bd07-3d51-aa00-fb1342f092a2 | -10.91108 | -56.84334 | 2026-06-18 07:26:00 | AQUA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 5efad7e1-0dd7-3293-b5c3-28982bad3214 | -10.14991 | -56.61032 | 2026-06-18 07:26:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 920ad3e8-5b93-32c1-aad7-c3615b912d43 | -12.8354 | -44.3657 | 2026-06-18 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ce2002f8-b400-3d82-99d6-0a170001e0f5 | -8.9261 | -46.9602 | 2026-06-18 07:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| f82312fb-d80e-351c-b66b-9ce582c220df | -8.9072 | -46.9621 | 2026-06-18 07:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| deccca5e-d038-3da9-b032-635a04ec46e7 | -12.8354 | -44.3657 | 2026-06-18 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 46576dff-ccef-3a99-99fa-f9dbf62db74f | -8.9072 | -46.9621 | 2026-06-18 07:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| f80eb695-8f31-3228-9b36-43e9a4bfdbbb | -8.9261 | -46.9602 | 2026-06-18 07:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 3dc58b24-051a-38a2-af75-74923366d19e | -12.8354 | -44.3657 | 2026-06-18 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 204a9bd7-c965-3fb1-8567-56fa2b51778b | -12.8354 | -44.3657 | 2026-06-18 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 1e94850c-1099-34ef-bf11-18993a936761 | -12.8354 | -44.3657 | 2026-06-18 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.3 |
| cde8997b-4732-3a93-8342-183fb86f3840 | -12.8354 | -44.3657 | 2026-06-18 08:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.5 |
| af3d0d25-36f4-354b-99c9-7f870eb528a2 | -12.8354 | -44.3657 | 2026-06-18 08:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 427e4080-9618-329c-9416-0fbb58534079 | -7.72153 | -44.1651 | 2026-06-18 11:30:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d4950c5e-cea2-3bcc-a386-ba888eb9f279 | -5.2937 | -43.95755 | 2026-06-18 11:30:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 7a676a15-1a62-3735-931a-5066401415de | -7.13145 | -40.84604 | 2026-06-18 11:30:00 | TERRA_M-M | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| d3aa6593-4eb4-3528-9cfa-e7407fdde38b | -10.92119 | -46.39413 | 2026-06-18 11:32:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| b173acc8-837e-3f38-a939-ac26e11a8949 | -12.76822 | -44.5437 | 2026-06-18 11:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0947a6a3-d04e-3f72-966e-c81d8613dcf5 | -16.02862 | -43.46708 | 2026-06-18 11:32:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| de3ee4f6-f6e7-3f7e-a190-363629004314 | -8.48069 | -47.55042 | 2026-06-18 11:32:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| d5f90a8b-1d4b-306e-b60d-48a2e17bff19 | -12.84057 | -44.37422 | 2026-06-18 11:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 4652ce40-7658-385d-b756-0d8a8d064979 | -14.98884 | -45.44178 | 2026-06-18 11:32:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 68772141-f5d2-30b4-9b6e-9f2d3ba529ab | -12.20272 | -43.88177 | 2026-06-18 11:32:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 8de7143c-12b2-38c7-9605-1e81f8668745 | -12.42626 | -48.72738 | 2026-06-18 11:32:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d25ce995-5b2c-3f01-b538-e1ef575a2070 | -11.87336 | -43.79845 | 2026-06-18 11:32:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8d7fc207-246d-3af2-b0e2-3764d287d5f5 | -16.02635 | -43.42024 | 2026-06-18 11:32:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 40bc0821-ade8-3b52-9e0f-41604763cb9f | -8.48466 | -47.55709 | 2026-06-18 11:32:00 | TERRA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e7c90c55-646c-39e7-9941-afde10f1b7ac | -15.4239 | -47.6223 | 2026-06-18 11:32:00 | TERRA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e7791c3b-7302-3b67-8099-24c9ad055187 | -10.75493 | -43.61814 | 2026-06-18 11:32:00 | TERRA_M-M | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 633245c3-97a9-3696-b99b-dbc508c107b7 | -15.24919 | -39.24793 | 2026-06-18 11:32:00 | TERRA_M-M | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 494d7c25-4d4d-37e7-a5ea-89d4192933db | -14.14429 | -45.40129 | 2026-06-18 11:32:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 86c2a8ee-84e2-3ade-96ff-e56a7888c5d7 | -12.65608 | -47.66549 | 2026-06-18 11:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c40683db-e0a6-33f0-ac66-642d570223f0 | -10.93193 | -46.4647 | 2026-06-18 11:32:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 74e24173-c8d1-3d9f-a8e7-6dd0b875c754 | -10.91057 | -46.39243 | 2026-06-18 11:32:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 15790cc3-9322-3085-b69d-f9237226e3b6 | -16.02731 | -43.47618 | 2026-06-18 11:32:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb914bdb-b7cf-310c-b98f-18392e98248f | -10.93406 | -46.45113 | 2026-06-18 11:32:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c9be6b2e-37ac-31a2-9e5f-52e103356613 | -12.84202 | -44.36448 | 2026-06-18 11:32:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.9 |
| 267f53a4-2f3b-311f-85ce-0121f9e7627e | -9.02559 | -44.24949 | 2026-06-18 11:32:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| add7515a-14d3-370b-8887-9fa9c945ff32 | -10.89997 | -46.39067 | 2026-06-18 11:32:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c31e03f6-4961-36b8-b9bb-eb12ef486461 | -11.25414 | -46.62339 | 2026-06-18 11:32:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| a4cc3abe-f4c1-379d-8886-a883b712c153 | -9.38495 | -40.55943 | 2026-06-18 11:32:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 5b089544-da49-34d9-8a58-f3ca7766bf55 | -12.65353 | -47.68111 | 2026-06-18 11:32:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d89d7fde-35bf-326d-bf68-37c94a1b6962 | -8.92692 | -46.97253 | 2026-06-18 11:32:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 343044c6-eba7-3f60-9d18-b46bf6c0369f | -12.11115 | -41.10423 | 2026-06-18 11:32:00 | TERRA_M-M | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 01bc88ce-f7c3-353c-964b-723b9f2749dc | -10.91909 | -46.40746 | 2026-06-18 11:32:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 0be7992a-9ffa-31d8-a734-453ba6a6b07b | -12.10985 | -41.11354 | 2026-06-18 11:32:00 | TERRA_M-M | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 20.8 |
| 3ba9f133-5860-30c5-be2a-dacd7781fc2b | -17.58253 | -42.71827 | 2026-06-18 11:34:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |
| ae116a3b-b646-375d-8022-1e18a7036f0c | -17.58123 | -42.72765 | 2026-06-18 11:34:00 | TERRA_M-M | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 119ad5dd-52ca-325d-b54a-72a3d5af30c8 | -18.70378 | -40.48597 | 2026-06-18 11:34:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 86f2204e-c90c-3188-9ae3-f173e8003277 | -18.69376 | -40.48463 | 2026-06-18 11:34:00 | TERRA_M-M | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| fb9121ab-0612-3bd1-ac6d-43f17b8c8ab5 | -11.0622 | -52.4603 | 2026-06-18 11:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 3c557697-2269-33a5-b321-387b94a52bca | -11.0622 | -52.4603 | 2026-06-18 12:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 252.7 |
| 8dbd5544-971e-39e6-8b03-9cf6ae995b08 | -12.7746 | -44.5162 | 2026-06-18 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 6996060c-5059-3a28-82d8-b85b2fdbabd6 | -11.0622 | -52.4603 | 2026-06-18 12:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 334.6 |
| 608c8bbd-5b50-327a-bc9a-de968b5d6fa5 | -12.7746 | -44.5162 | 2026-06-18 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 226.5 |
| d6bf6bd3-c800-358e-82a0-cff02c3e6e7c | -10.9222 | -46.3936 | 2026-06-18 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6a6ddc8b-c1d1-319c-8f2d-10583da2fbd9 | -12.7548 | -44.5428 | 2026-06-18 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 1197f36d-c393-3c59-9832-6ebd865e81af | -12.7741 | -44.5396 | 2026-06-18 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| 225480ef-9bbe-3d8a-82e1-7bf6b793e040 | -11.0622 | -52.4603 | 2026-06-18 12:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 309.5 |
| 2a76f022-0914-35f4-9b05-0b3872e1b47c | -12.7741 | -44.5396 | 2026-06-18 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| 128c0763-6679-3c73-b8b2-3948abb9cd45 | -11.0622 | -52.4603 | 2026-06-18 12:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 376.5 |
| a06c994d-7a71-3ac7-a712-f2e2213ca82f | -12.7548 | -44.5428 | 2026-06-18 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| d5f0057c-9b64-32d9-afee-04fdb3333c93 | -12.7746 | -44.5162 | 2026-06-18 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 349.7 |
| 7dded0b2-b584-3457-b86a-8a3c45df5c43 | -11.0622 | -52.4603 | 2026-06-18 12:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 416.5 |
| 1565751f-9079-3e17-afb5-e13e0a9a198c | -12.7746 | -44.5162 | 2026-06-18 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 371.6 |
| 585c19da-cb98-3fa5-ab8c-ad190ff0b29a | -12.7741 | -44.5396 | 2026-06-18 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 266.4 |
| 22de1826-21e2-3fa0-a8f3-65817b07044a | -10.9222 | -46.3936 | 2026-06-18 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 71ad5633-a320-3302-a569-242bb3f10c29 | -12.7548 | -44.5428 | 2026-06-18 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 4c7d4b74-40ab-3634-a778-33d3ea036ab7 | -12.7741 | -44.5396 | 2026-06-18 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 276.6 |
| 3ced7e3b-435e-3665-b4fa-e832ed243b40 | -10.9222 | -46.3936 | 2026-06-18 12:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f77446d6-41dd-3aa0-b258-52de0cc6666e | -12.7746 | -44.5162 | 2026-06-18 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 486.1 |
| 0707d262-0741-3ef4-a05d-7d69d3357a86 | -11.0622 | -52.4603 | 2026-06-18 12:50:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 343.0 |
| 85d37b3c-1f64-312c-9616-ac2fde9d1fb1 | -12.7548 | -44.5428 | 2026-06-18 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| eaf5aa60-cc39-3fd9-b1b8-aeb284d49cca | -12.7746 | -44.5162 | 2026-06-18 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 563.6 |
| b51b51bc-0634-3e27-a077-d7aa6de424d7 | -11.0622 | -52.4603 | 2026-06-18 13:00:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 312.8 |
| 20863bf4-b7f7-36e9-8d45-d44d7a5b0496 | -10.9222 | -46.3936 | 2026-06-18 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| dfa16560-9745-384f-9ce7-5aafe638cc31 | -12.7548 | -44.5428 | 2026-06-18 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 2c617c74-c96f-318d-9ea8-c30514105a73 | -12.7741 | -44.5396 | 2026-06-18 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 282.1 |
| 95805314-711b-3877-a49d-9a7b2bbdcb96 | -1.27143 | -57.85435 | 2026-06-18 13:06:00 | TERRA_M-T | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| fb14167f-6ae9-3a5b-9a48-a65e3f7a58f8 | -10.9222 | -46.3936 | 2026-06-18 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 8a281ea1-939e-306c-b6af-76012c4c89cb | -14.7457 | -52.6683 | 2026-06-18 13:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 0a6a39e5-5b59-3400-bd32-12ba58493900 | -11.0622 | -52.4603 | 2026-06-18 13:10:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 369.8 |
| f6d41c5e-1590-3d67-bc52-f534f6ca8389 | -12.7548 | -44.5428 | 2026-06-18 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 9aaa9baa-21e8-3bf0-9df7-1c0656da6385 | -12.7741 | -44.5396 | 2026-06-18 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 314.3 |
| d664e2f0-4139-36f2-97ce-5065605f008f | -10.1491 | -56.6314 | 2026-06-18 13:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 67f79057-2ac5-3576-9e31-bc81d79eb5fe | -11.0622 | -52.4603 | 2026-06-18 13:20:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 468.7 |
| 38fd0af9-973d-396f-b683-8d983509c386 | -14.7457 | -52.6683 | 2026-06-18 13:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 7cd04f3c-bb86-3b62-a4eb-03f65c1fe72b | -10.9222 | -46.3936 | 2026-06-18 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| 111b99d6-7e02-3208-b3d9-a3e4a6ad1a3d | -10.1493 | -56.6115 | 2026-06-18 13:20:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 6cc15c74-9dec-3075-ba6b-e072eb12a59d | -10.9226 | -46.371 | 2026-06-18 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 2f0f1c66-ba7c-3937-897b-e36a696deee1 | -12.7746 | -44.5162 | 2026-06-18 13:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 477.3 |
| 82537bf3-5f91-307c-89dd-233272aaa4fb | -12.7746 | -44.5162 | 2026-06-18 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 375.5 |
| 6573843f-7c73-3f37-9d89-0a558d0be446 | -12.7548 | -44.5428 | 2026-06-18 13:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 0f1cfb68-c4a7-309c-a2ad-e222748c1cda | -10.9222 | -46.3936 | 2026-06-18 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 236ab844-1719-3722-8fad-bee201fc1570 | -14.7457 | -52.6683 | 2026-06-18 13:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| 011b8c78-84cc-3b72-8bfa-f8460c63705f | -11.0622 | -52.4603 | 2026-06-18 13:30:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 463.3 |
| ab847256-140b-3fcc-a93d-dc6428b03398 | -12.7548 | -44.5428 | 2026-06-18 13:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| db19352c-88ce-390d-a997-7face5e39b3e | -10.9226 | -46.371 | 2026-06-18 13:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 01c0617b-87b4-39c4-9b38-4c4d4c31b133 | -11.0622 | -52.4603 | 2026-06-18 13:40:00 | GOES-19 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 401.7 |


[Clique aqui para ver as próximas entradas](README15.md)
