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
| 3e226207-377e-3482-a153-3bcacfaf08c4 | -6.55333 | -55.14918 | 2026-07-10 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c4e2d2ac-9d21-33b9-a265-674ec9a440eb | -6.56427 | -55.15824 | 2026-07-10 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5313dbfa-5c1f-3a60-a5b9-cefaf5ecb5bc | -6.57242 | -55.14649 | 2026-07-10 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ca30df22-99ad-37d8-80d7-db019138f1d7 | -4.3394 | -47.77876 | 2026-07-10 00:22:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 6809f6d4-bbbd-33c5-b368-92dc6d048643 | -2.76503 | -48.57984 | 2026-07-10 00:22:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4903fdd0-95d6-3228-90f7-e39d390bf001 | -4.34631 | -47.77193 | 2026-07-10 00:22:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 152.2 |
| 1a043be5-f27c-3c50-a193-8513cd0fd4c0 | -6.55472 | -55.15958 | 2026-07-10 00:22:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 805e9af4-358d-3559-b9a1-2dc231124ec6 | -4.35113 | -47.77706 | 2026-07-10 00:22:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 92935ca7-fc59-31eb-9c45-bd28ff29947e | -4.34878 | -47.76059 | 2026-07-10 00:22:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 86fe7b9b-4eee-3594-a653-370bd541b660 | -4.34383 | -47.75551 | 2026-07-10 00:22:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| b17a7669-4b1a-301b-beff-90d941a310a6 | -6.42595 | -55.79794 | 2026-07-10 00:22:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 0301f327-3685-3261-8217-c5edd309bcb1 | -4.15695 | -54.98193 | 2026-07-10 00:22:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 68e1216f-53dc-3f90-9fdb-6250bf3fa49c | -8.0367 | -47.4219 | 2026-07-10 00:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| c75ebdac-606c-32d9-b0ae-4aa10164a522 | -15.462 | -49.6303 | 2026-07-10 00:30:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 9cbadeb1-755e-3909-b0c1-24a038afdf74 | -10.8589 | -44.4338 | 2026-07-10 00:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| d77bc36a-c678-3a9d-9d66-c6c6fdf646c1 | -12.3561 | -47.413 | 2026-07-10 00:30:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6600fb69-962c-3b91-bdde-d607618b2e6f | -15.4616 | -49.6524 | 2026-07-10 00:30:00 | GOES-19 | URUANA | GOIÁS | Brasil | 5221700 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 63838992-80f0-3623-97ae-09dd7a8c534a | -4.3402 | -47.7645 | 2026-07-10 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 0df431d9-aa2e-364c-a4b1-3cf3e4c6ccb7 | -4.3588 | -47.7636 | 2026-07-10 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c2f08abc-1286-3655-8841-8a1928e300b6 | -12.718 | -45.4536 | 2026-07-10 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 0e30119e-14c4-3514-ae46-675321a36dea | -10.8585 | -44.4571 | 2026-07-10 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| fe6bc45f-9ccc-33ac-8800-db98b507243b | -4.3402 | -47.7645 | 2026-07-10 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.5 |
| c0bc4c78-879b-3e0c-8af0-b1875457e8e2 | -12.5003 | -43.7621 | 2026-07-10 00:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 029641ab-1036-32ac-9e97-06f822fba016 | -12.3561 | -47.413 | 2026-07-10 00:40:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| d8205920-5b52-3d55-8563-a34a4a766535 | -10.9907 | -49.3886 | 2026-07-10 00:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 05f3252f-e676-3f68-903b-18a0299357b2 | -12.6987 | -45.4566 | 2026-07-10 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 11f4c9e8-303c-3f11-9066-5a15ec66fb1f | -10.8589 | -44.4338 | 2026-07-10 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 9b4ca65a-0eea-38e9-ad1f-b729585a1eee | -10.1478 | -50.167 | 2026-07-10 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| f8074032-ad32-38ee-9d85-34de47d53b40 | -12.6987 | -45.4566 | 2026-07-10 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.5 |
| b362166e-b13c-36bb-a57e-034bc941de38 | -12.3561 | -47.413 | 2026-07-10 00:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 972dc748-6fe3-36cb-a31b-5f39bdf5a2ba | -8.0367 | -47.4219 | 2026-07-10 00:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| b820ec00-09c7-3bb9-95d4-e971f6041636 | -12.718 | -45.4536 | 2026-07-10 00:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c0fa0072-9cee-3a83-8511-d4682230d59d | -10.8589 | -44.4338 | 2026-07-10 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 7d4002a2-10a5-3688-8135-5a8b12fb0f72 | -10.1286 | -50.1902 | 2026-07-10 00:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.9 |
| b6a52ea0-71ce-34ea-b845-c0acc03994fb | -4.3402 | -47.7645 | 2026-07-10 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 0fa39837-7dcd-3e6f-a643-ca1f5e36dbb3 | -4.3402 | -47.7645 | 2026-07-10 01:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| ed699c91-1baf-379f-a453-fc563eb279aa | -12.718 | -45.4536 | 2026-07-10 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| a8eeeefa-1d85-379d-a68c-8865d7bf3355 | -12.3561 | -47.413 | 2026-07-10 01:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 103.0 |
| 1c72f4f7-5d21-3f99-af72-b0ef8e6a9f25 | -10.8589 | -44.4338 | 2026-07-10 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 639c41fe-f5de-34cc-a414-b95e1d6138fb | -10.1286 | -50.1902 | 2026-07-10 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 791686bf-80af-3637-ad37-45fc7be4d701 | -10.1478 | -50.167 | 2026-07-10 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 5209bf4c-8cc6-3c00-a689-6b6f5aa353f6 | -12.6987 | -45.4566 | 2026-07-10 01:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 08601df0-d56e-3713-b7f4-10b2822e1c13 | -10.1289 | -50.1689 | 2026-07-10 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 4f3cd10b-5654-323f-a3d0-a2bf8ddc0c92 | -10.1475 | -50.1883 | 2026-07-10 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| bba869a2-51b2-320d-8c8e-b41ba5378c01 | -10.1289 | -50.1689 | 2026-07-10 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 0043a8eb-ec61-3206-b224-411425dbe56c | -10.1286 | -50.1902 | 2026-07-10 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 146.1 |
| 6204b86d-cb25-3d15-b2f4-a1ff6ba67a7c | -10.8589 | -44.4338 | 2026-07-10 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 788166a4-b571-32e8-9518-51b5603ede81 | -12.3561 | -47.413 | 2026-07-10 01:20:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| dcdebf70-8385-3b81-a402-8ed646afdd83 | -10.1478 | -50.167 | 2026-07-10 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6768aa67-93bc-3156-9205-9e8b242d6c5e | -4.3402 | -47.7645 | 2026-07-10 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b9594144-e5f1-3ab3-87e3-798969a55f0b | -12.5003 | -43.7621 | 2026-07-10 01:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 0973aa9f-0259-3e1f-b1b2-7e6030bfd3ee | -10.1475 | -50.1883 | 2026-07-10 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 8f628ed3-ea26-3ed6-be30-9402c0a3831f | -21.764799 | -56.292801 | 2026-07-10 01:25:00 | METOP-B | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| efad497e-8107-38fc-a53f-6b701308d53a | -10.1286 | -50.1902 | 2026-07-10 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 0e17a4ac-e836-3773-ae89-63c9a736e12e | -12.718 | -45.4536 | 2026-07-10 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| f1a207dc-2bf8-3eee-97a8-cb64783f1ed8 | -12.5003 | -43.7621 | 2026-07-10 01:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 7de36f58-7ab3-3010-84d2-c6d7d1a59bb3 | -12.6987 | -45.4566 | 2026-07-10 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.7 |
| c0242f02-9f82-3aa9-a95d-16041b43af31 | -4.3402 | -47.7645 | 2026-07-10 01:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| e54b0a1e-a8c9-3fd3-9e1c-2478602936ba | -10.1289 | -50.1689 | 2026-07-10 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| a6da91d2-1aa3-3099-874e-513d9d5eed6e | -10.8589 | -44.4338 | 2026-07-10 01:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 7486d52a-8c24-3d00-ba39-b16bab2b2411 | -10.1286 | -50.1902 | 2026-07-10 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 832098c2-7a84-3598-8d20-3737d6fcfc4e | -12.718 | -45.4536 | 2026-07-10 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 569a56ed-e1a2-3fcb-80ac-00d298512b0b | -10.8589 | -44.4338 | 2026-07-10 01:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.8 |
| dac002d2-30ba-396b-8663-db71a89c54fd | -4.3402 | -47.7645 | 2026-07-10 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 44e6a6ce-c638-3952-afeb-fd92ff1d5dd8 | -12.5003 | -43.7621 | 2026-07-10 01:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3661a5a7-ad80-30b3-80b6-8d0c780faf9a | -12.6987 | -45.4566 | 2026-07-10 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| d6711323-58fb-3747-a7f7-f9ee442c1d6a | -12.3561 | -47.413 | 2026-07-10 01:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| bfa842c5-dbad-3bb5-8a48-fdb81cfefe79 | -12.5003 | -43.7621 | 2026-07-10 01:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 9a7b2e85-bf87-3b64-9db7-25a4acf656b2 | -21.7693 | -56.300301 | 2026-07-10 01:51:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2a4b143b-3573-382d-a68a-e8a1d92e0128 | -21.7656 | -56.286598 | 2026-07-10 01:51:00 | METOP-C | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4d2f7fe5-6152-34f0-986e-dcaa28e58f76 | -18.037001 | -54.360901 | 2026-07-10 01:51:00 | METOP-C | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 174c51c5-43cb-3776-9b8b-9c628a88a99a | -10.1286 | -50.1902 | 2026-07-10 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 2b4bcf8e-3baf-3071-8bdc-34339e772e61 | -10.8589 | -44.4338 | 2026-07-10 02:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 4355cccc-c11d-3c97-b07d-146335a8f537 | -12.5003 | -43.7621 | 2026-07-10 02:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 70.1 |
| d775de23-f60e-3b08-ac61-687674a47f7b | -12.5003 | -43.7621 | 2026-07-10 02:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 62.0 |
| b5eb4080-39d4-3e95-a754-afedfa66c3d2 | -12.5003 | -43.7621 | 2026-07-10 02:20:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 437faf11-e458-3c40-8f5a-918dd02588c1 | -8.0367 | -47.4219 | 2026-07-10 02:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 680d62fd-823b-3da9-ae51-1c96efbd710e | -12.5003 | -43.7621 | 2026-07-10 02:30:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 6c83d1a1-4dde-3272-ac23-7e5a818605b1 | -8.0367 | -47.4219 | 2026-07-10 02:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 426ae66e-a116-380c-bd5f-9d9dcd72d370 | -12.5003 | -43.7621 | 2026-07-10 02:40:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 6ab306c1-c194-30b9-805f-ae49bd221f14 | -8.0367 | -47.4219 | 2026-07-10 02:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 16ab0105-debe-3f8b-8683-6e1bace1ed33 | -12.5003 | -43.7621 | 2026-07-10 02:50:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| cbe1cec2-c14c-362b-be9f-d421597d00f0 | -10.1286 | -50.1902 | 2026-07-10 03:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 1a609004-ddfc-3f4d-a3b6-a392adb95096 | -10.1286 | -50.1902 | 2026-07-10 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| d1600cd7-710a-3258-953a-2b6e1844cf66 | -11.41593 | -41.41868 | 2026-07-10 03:28:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 887f3a69-d524-36e3-83ab-24963ae2e137 | -11.44481 | -39.50919 | 2026-07-10 03:28:00 | NPP-375D | SÃO DOMINGOS | BAHIA | Brasil | 2928950 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eec084f6-708a-3b44-bad1-c8298a18a0b8 | -10.85477 | -44.44962 | 2026-07-10 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 84e558dd-6ae9-3798-a3bd-34b9f665dd26 | -6.49974 | -42.212 | 2026-07-10 03:28:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 07450f99-e8f5-31fb-bdba-507cf46c4f25 | -10.85626 | -44.44246 | 2026-07-10 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dff3f0ba-8f86-366c-baac-f9dc6e5716a4 | -6.49938 | -42.21089 | 2026-07-10 03:28:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e3e88da1-be44-3ff5-86a1-caede1f55216 | -6.4982 | -42.2173 | 2026-07-10 03:28:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 71b24d9c-ad68-324d-903f-309239b82b0e | -10.85734 | -44.4409 | 2026-07-10 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ae39e9ed-db17-3640-b7a2-e245276dab02 | -6.50502 | -42.21865 | 2026-07-10 03:28:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 25b0d8f5-72c4-3cd9-8cf6-1db821e8e479 | -4.98093 | -37.47803 | 2026-07-10 03:28:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| f6917cc6-5e6e-306a-9e53-323dec075118 | -10.85581 | -44.44807 | 2026-07-10 03:28:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 12768f44-fb85-3b10-b68d-6790d014df3b | -11.41505 | -41.4231 | 2026-07-10 03:28:00 | NPP-375D | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1174f1bf-3bcc-343d-8aa1-74b0d890dd35 | -4.98146 | -37.47489 | 2026-07-10 03:28:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a19906f4-d405-3a5c-8a18-3352d0ad3f91 | -6.49851 | -42.21843 | 2026-07-10 03:28:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| deaabbbc-77d6-39b6-be5e-0d5142afede4 | -10.1286 | -50.1902 | 2026-07-10 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| c4f61204-0ed3-31ef-b89e-9b740bd0b2f2 | -13.26512 | -45.15042 | 2026-07-10 03:30:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README4.md)
