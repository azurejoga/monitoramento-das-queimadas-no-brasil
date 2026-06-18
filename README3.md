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
| 5d48a8c3-2d24-3ca4-adcf-8193ef5f0de7 | -9.4391 | -40.3171 | 2026-06-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1402.6 |
| db0af3c8-a5be-3c55-aa51-54008ecbd034 | -9.42 | -40.3198 | 2026-06-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 882.2 |
| b9fae562-f2c9-3abb-b6df-e556372b052d | -9.4387 | -40.3419 | 2026-06-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 809.1 |
| d0620197-c806-391d-9323-14b7b6c2c0f5 | -7.7176 | -44.1611 | 2026-06-18 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 115.7 |
| f5c7d691-2c82-3853-b398-a31ea5e625e5 | -10.9164 | -56.8536 | 2026-06-18 01:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| fa0a1e1b-5923-32a3-b051-42bbd841364f | -9.4196 | -40.3447 | 2026-06-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 589.6 |
| 7c66ffc5-88b7-3112-8cc7-8378175e4aac | -9.4578 | -40.3392 | 2026-06-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 140.9 |
| 35f58998-5085-34db-81f3-3019e6510c2a | -12.8354 | -44.3657 | 2026-06-18 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| f2ca3263-cd50-3319-97fd-332c91228f93 | -9.4582 | -40.3143 | 2026-06-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 281.0 |
| 07de6756-1041-3df0-a7e9-bd7ddcd58340 | -9.4196 | -40.3447 | 2026-06-18 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 138.0 |
| 79a26ea8-754a-3068-ae4a-ce40f11508e6 | -7.7176 | -44.1611 | 2026-06-18 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 94.9 |
| c3dcbc9f-c70a-3c1f-afc6-7d8ef2d81fac | -9.4391 | -40.3171 | 2026-06-18 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 337.3 |
| 9a4ee684-c372-3983-af83-86898b8b3443 | -9.4387 | -40.3419 | 2026-06-18 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 155.2 |
| 95a75cc9-cc8d-3d3c-a0bb-0f8a47f94c30 | -12.8354 | -44.3657 | 2026-06-18 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 82cba112-ce99-35a3-9de5-4b3b40634aab | -9.2152 | -47.9241 | 2026-06-18 01:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 5e2eaed6-ec79-34ed-ba89-91189d05e9ce | -10.9164 | -56.8536 | 2026-06-18 01:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 8d325f4e-125b-369b-a615-60166a187fc8 | -9.42 | -40.3198 | 2026-06-18 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 298.0 |
| 78e622ae-b435-3ae3-be19-38af5a490c8a | -7.7176 | -44.1611 | 2026-06-18 01:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 03ef44d2-0b19-3a09-ba31-7f378cfadb8c | -10.9164 | -56.8536 | 2026-06-18 01:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 7ff2a0af-40a4-3eea-b881-c6dee1541313 | -12.8354 | -44.3657 | 2026-06-18 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 45f734c1-7fc0-3f25-9b06-5ffe01e536ff | -9.2152 | -47.9241 | 2026-06-18 01:30:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 790bece9-f762-32f3-ac48-0e6a1839d0fd | -7.7176 | -44.1611 | 2026-06-18 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 9ffc4d47-6e94-3c60-ab7f-28f8f48bf47b | -9.0155 | -63.5411 | 2026-06-18 01:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 58.1 |
| ff9d6ba5-c753-31fc-9a93-8d7f89971be8 | -9.2152 | -47.9241 | 2026-06-18 01:40:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| b3aebf15-1108-3859-aae5-b7eedca1e223 | -12.8354 | -44.3657 | 2026-06-18 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f8dfdf16-6e5f-34ac-82c6-55d0404ad43c | -10.9164 | -56.8536 | 2026-06-18 01:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| aaea987f-b4e3-39ca-912c-f7577f410a97 | -12.8354 | -44.3657 | 2026-06-18 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 6f2dc508-aa4f-373c-b4c3-f6f401e0f933 | -10.9164 | -56.8536 | 2026-06-18 01:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 0981435e-53e6-3daf-8e1e-96f43450688c | -7.7176 | -44.1611 | 2026-06-18 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 6fe642df-d8a5-3f50-95d2-ba1edacd9228 | -9.2152 | -47.9241 | 2026-06-18 01:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b5262863-4ccb-3024-98d5-0672f6b1cb82 | -12.8354 | -44.3657 | 2026-06-18 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 9bdaf1fa-3ede-36f3-9f9b-1011893a1985 | -12.8548 | -44.3625 | 2026-06-18 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.4 |
| a0ad7c32-4750-311a-9f3e-926bc08d0ac8 | -10.9164 | -56.8536 | 2026-06-18 02:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.1 |
| cf2cfda7-bc42-305a-8cd5-c295d92377af | -9.0155 | -63.5411 | 2026-06-18 02:00:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 4695c4fa-5903-39a4-abc9-a8a3d07b03d3 | -9.5147 | -40.3558 | 2026-06-18 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 92.6 |
| 75b71a70-118f-3e6a-a278-449f6b56a63a | -12.8354 | -44.3657 | 2026-06-18 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.0 |
| fd7e14cb-e08f-3821-bdb6-94b9372adc9c | -9.5339 | -40.3531 | 2026-06-18 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 315.6 |
| fe49b013-5361-3891-b491-d5bb9451bd00 | -10.9164 | -56.8536 | 2026-06-18 02:10:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 361e10a0-e96e-3874-a4fd-6415f29a9c3b | -9.5152 | -40.331 | 2026-06-18 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.1 |
| f1a28e70-6eb0-377b-97d1-66f083cab26e | -9.5343 | -40.3282 | 2026-06-18 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 249.7 |
| bcde5720-e7db-3112-b7ac-0b8bd08a1941 | -9.5152 | -40.331 | 2026-06-18 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.9 |
| a9d6f2ca-6bf0-3ba4-8440-c50c910af76e | -9.553 | -40.3503 | 2026-06-18 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 177.8 |
| a0483ae8-4487-3b61-bd64-f889bedfc4dc | -9.5339 | -40.3531 | 2026-06-18 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 378.9 |
| 340009b6-11da-3d6d-b1e2-49b27bc6eb7e | -10.9164 | -56.8536 | 2026-06-18 02:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 684e54f4-1c80-3042-ab72-cf4bcecd89a8 | -9.5147 | -40.3558 | 2026-06-18 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 97.7 |
| d0bbddf1-4447-3930-bf70-7855b56ed31d | -9.5534 | -40.3254 | 2026-06-18 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 128.0 |
| 3befdddc-68f5-3efa-a562-cb9f64fc43e2 | -9.5343 | -40.3282 | 2026-06-18 02:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 309.5 |
| dfd8e8bd-a75b-354e-92a7-e4820ebe891f | -9.5339 | -40.3531 | 2026-06-18 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 150.1 |
| 5ad59b2a-3c0c-39ef-8d49-c1cd95965860 | -9.5343 | -40.3282 | 2026-06-18 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 112.4 |
| e72b08ff-98a5-3ca9-9710-24f12ffc42f3 | -10.9164 | -56.8536 | 2026-06-18 02:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| fbfd3623-1509-3c2b-99c6-fb83c8da312b | -12.8354 | -44.3657 | 2026-06-18 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 5ecc7267-7296-318c-b7ae-2ca60934e02d | -9.0155 | -63.5411 | 2026-06-18 02:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9c6e9fa6-4ae3-3ad0-a449-52d0eabc6ef5 | -9.5339 | -40.3531 | 2026-06-18 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 118.0 |
| ed463a85-ab41-3696-ac85-0632a266ffec | -9.5343 | -40.3282 | 2026-06-18 02:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.8 |
| b38fa5dc-6e7f-3e05-9493-654c56a0bfbf | -10.9164 | -56.8536 | 2026-06-18 02:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 6863fc32-3968-3bf8-81f5-9602b07e3bac | -9.5339 | -40.3531 | 2026-06-18 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 113.2 |
| 4a4c5859-bb5d-3f01-9c40-e469b871d0c5 | -10.9164 | -56.8536 | 2026-06-18 02:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |
| c2cb260d-a249-3ede-bb20-8ca5b8344ec6 | -9.5343 | -40.3282 | 2026-06-18 02:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 136.0 |
| 7cdc10d1-6403-3e5c-bdff-bec22ec86722 | -9.5339 | -40.3531 | 2026-06-18 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 151.0 |
| 61d4f823-750e-385f-8be1-ae29bfc1fe61 | -9.553 | -40.3503 | 2026-06-18 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 00aa78ab-81e0-36c1-9f63-413ae4bdb2f2 | -9.5534 | -40.3254 | 2026-06-18 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.7 |
| a8f04f36-b58f-3112-a9c1-b38acedeb037 | -9.5343 | -40.3282 | 2026-06-18 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 170.1 |
| e69f0638-c06c-3193-a700-c00c7c562214 | -10.9164 | -56.8536 | 2026-06-18 03:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 946b06bb-5eda-36ba-a6fd-143217b41b91 | -5.61142 | -37.53479 | 2026-06-18 03:04:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 4.9 |
| ff51ec01-8c99-3f1b-9e0b-369e43334714 | -5.61233 | -37.53401 | 2026-06-18 03:04:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cf068a80-8d2a-3baa-aa9f-259a6e06c0bc | -5.61238 | -37.52933 | 2026-06-18 03:04:00 | NOAA-21 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b9fe3a39-edad-3597-8562-2479a660affc | -9.53943 | -40.34627 | 2026-06-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.8 |
| aad4a358-65cb-369c-ae11-300281a02354 | -9.53796 | -40.3534 | 2026-06-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 60b77a5a-ccb6-32b5-976f-6433fa6f5020 | -9.53764 | -40.33802 | 2026-06-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.7 |
| ebecbe4e-c262-3de7-b3ca-a78c149cb0f4 | -9.53621 | -40.34517 | 2026-06-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 43e4e20c-a5c0-33a7-ae26-1f98ba172aed | -9.54332 | -40.34658 | 2026-06-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 23af1993-0593-3f06-af7f-0d8b300d5b48 | -9.54475 | -40.33943 | 2026-06-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 59.7 |
| 304d9ed0-fbe4-3108-854c-4d49c29527b7 | -9.28983 | -40.24913 | 2026-06-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 4effa0fc-e1bc-3d47-b00d-6a8736c980ea | -9.54091 | -40.33914 | 2026-06-18 03:06:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 103.6 |
| 32889006-4b60-3df0-9f1d-cfaca177d5ad | -9.5343 | -40.3282 | 2026-06-18 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 58d30867-e80a-3b99-9871-1e9836bf8adc | -9.5339 | -40.3531 | 2026-06-18 03:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 260f6d77-cf37-3be5-85e8-26f4a39b32da | -9.5534 | -40.3254 | 2026-06-18 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 139.7 |
| 6351f301-e8cb-3876-b550-4ad488b69acc | -9.5339 | -40.3531 | 2026-06-18 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 233.3 |
| 60a76d5d-7ef3-3ca3-a696-7cee6768e4f7 | -9.5343 | -40.3282 | 2026-06-18 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 273.2 |
| 59e6b7eb-9aaf-3cb0-9139-23de12190d78 | -10.9164 | -56.8536 | 2026-06-18 03:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 52f01f34-02e6-35a1-b378-8a2ddefae57b | -9.553 | -40.3503 | 2026-06-18 03:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 138.5 |
| ac494338-a4d6-3939-8aa7-ca665a1ac3c1 | -10.9164 | -56.8536 | 2026-06-18 03:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 672a13fb-7dfa-3aea-ba0e-e804060085ff | -9.5343 | -40.3282 | 2026-06-18 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 125.9 |
| b9c8aed8-4a1d-3502-92b0-00d114349f6d | -9.5339 | -40.3531 | 2026-06-18 03:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 121.3 |
| ff61defd-b566-3e76-8dcd-f309e940e26e | -10.9164 | -56.8536 | 2026-06-18 03:40:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 04b98658-b274-38e6-b261-11b00dbd2a70 | -6.40141 | -44.17739 | 2026-06-18 03:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de9f41c5-ce58-3fdf-b5fe-07ed27cd3c67 | -7.72594 | -44.16747 | 2026-06-18 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0c464893-f380-31b8-b8c2-9207aa41dbad | -5.29457 | -43.70105 | 2026-06-18 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 439da6cf-4e00-34b3-892c-014873c474f9 | -8.91107 | -46.97174 | 2026-06-18 03:40:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 95174cfa-8cd3-3a8f-bdfb-6fe5e61ab0fa | -7.71346 | -44.16516 | 2026-06-18 03:40:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| befed97b-fd08-3f90-93b7-7f682f0129ee | -6.39514 | -44.18283 | 2026-06-18 03:40:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4cb1fde-d4c6-30d4-9c41-ba9055624f46 | -6.28887 | -43.6389 | 2026-06-18 03:40:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 276d17ce-88b6-3a4f-b282-f710b6eab6ff | -5.80926 | -45.07124 | 2026-06-18 03:40:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94d12070-ffa2-3d93-b4d8-bc0968234062 | -5.61087 | -37.5308 | 2026-06-18 03:40:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 26a86820-eba3-3cef-a8af-cc484d0d25e0 | -11.9897 | -38.96292 | 2026-06-18 03:40:00 | NPP-375D | SANTA BÁRBARA | BAHIA | Brasil | 2927507 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e023b37e-ed4f-303f-8e18-74f42c15eca2 | -5.29827 | -43.69244 | 2026-06-18 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4869034-9726-3d38-b138-51b0e79bcbed | -5.28896 | -43.96053 | 2026-06-18 03:40:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6b6d4af6-7577-3382-9790-3a1203085e15 | -5.60979 | -37.53133 | 2026-06-18 03:40:00 | NPP-375D | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cb0b3b12-194f-3cdb-a66a-1d5b0e631eee | -8.90953 | -46.97953 | 2026-06-18 03:40:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ed40d88-20ef-352c-9293-bdf2801a58f4 | -5.29628 | -43.9566 | 2026-06-18 03:40:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |


[Clique aqui para ver as próximas entradas](README4.md)
