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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28876623-8b9e-3f99-9df5-457874f1ea4b | -10.1427 | -63.657902 | 2024-10-08 01:47:53 | METOP-B | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 50e13b48-5e27-36d4-8417-c7a54db6b38a | -10.1329 | -63.660099 | 2024-10-08 01:47:53 | METOP-B | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3952bdd6-08f5-34c0-85de-0e11ebae91d8 | -9.9602 | -64.931801 | 2024-10-08 01:48:01 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 48eeed1a-bf6a-38c5-9270-17ad38806f5a | -9.7362 | -64.221901 | 2024-10-08 01:48:02 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4a3bd87e-b934-3a22-92e4-7dc62a58119c | -9.5425 | -63.561298 | 2024-10-08 01:48:02 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| cdd36ba1-bddc-3c63-bf49-eab3d45d20e7 | -9.5443 | -63.569099 | 2024-10-08 01:48:02 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 18fbc64d-b4e2-3006-a0ce-cd21acc3243d | -9.5462 | -63.5769 | 2024-10-08 01:48:02 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2884bb57-41e7-31ca-bff4-1c4107aa7f6c | -9.5676 | -64.206398 | 2024-10-08 01:48:04 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2b508e8d-df3f-398f-a366-ba67b325e589 | -9.5693 | -64.213799 | 2024-10-08 01:48:04 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fa54de21-8a7d-384a-955c-832f5424c1ee | -9.5595 | -64.216103 | 2024-10-08 01:48:05 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8235d0fa-5102-3b7b-a1b2-086390d9ad0a | -9.7484 | -65.225304 | 2024-10-08 01:48:05 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4d44826f-7230-31ce-b20c-7f7e80308d66 | -9.9473 | -66.757202 | 2024-10-08 01:48:08 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| eaf9f287-9d4c-3f5c-b8b8-c311d8bf51f0 | -9.9488 | -66.764198 | 2024-10-08 01:48:08 | METOP-B | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| b11dd108-38be-3545-8a5b-51deaac10633 | -9.7182 | -66.559799 | 2024-10-08 01:48:11 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| de9b3bb2-9acd-3b93-ad85-c56fed6913d4 | -9.7198 | -66.566803 | 2024-10-08 01:48:11 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 35db50b9-2189-37af-a4ab-7fbce0e826af | -9.7213 | -66.5737 | 2024-10-08 01:48:11 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 112c207a-0453-376a-bafa-21507911241e | -9.4539 | -66.713997 | 2024-10-08 01:48:15 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a582a88-e67b-3f25-a849-266d213b9eb4 | -9.4555 | -66.720901 | 2024-10-08 01:48:15 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b9dab097-a39f-3878-9c25-ed2f086b7585 | -9.457 | -66.727898 | 2024-10-08 01:48:15 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 85e1e925-a968-325d-9bba-6bf421b7341f | -9.4025 | -66.528801 | 2024-10-08 01:48:16 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08874d20-46ff-38b6-8f3f-f3cccbdf3826 | -9.404 | -66.535698 | 2024-10-08 01:48:16 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ee3793fa-8438-3238-bc6d-92d84fb60815 | -9.4056 | -66.542702 | 2024-10-08 01:48:16 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 606119b0-c679-34ce-b0a9-c0e24403defc | -9.4426 | -66.709198 | 2024-10-08 01:48:16 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16038015-687b-39ae-9891-9e250ca7ff08 | -9.4441 | -66.716202 | 2024-10-08 01:48:16 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c128f3bd-5777-3532-9f94-6ef70a987261 | -9.4457 | -66.723099 | 2024-10-08 01:48:16 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e74687c5-9139-3202-99db-790c2d2d1c34 | -9.5786 | -67.417099 | 2024-10-08 01:48:16 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e10d3fa4-7651-3c99-8160-1b817b8d70a1 | -9.5688 | -67.419296 | 2024-10-08 01:48:16 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ad9a3e7-c6db-309d-9796-8b8a25c411dc | -9.5672 | -67.412102 | 2024-10-08 01:48:16 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 609def6f-1f2d-3752-af7c-b47a1266e199 | -9.1621 | -66.053001 | 2024-10-08 01:48:18 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e32fa6d4-8103-3bed-b0ac-068066ffcec5 | -9.1606 | -66.046097 | 2024-10-08 01:48:18 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 30471e93-2b62-3727-824b-9de7fbe44e81 | -8.5461 | -67.121399 | 2024-10-08 01:48:32 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 89af2452-d0f3-3505-81a0-4b3fef7aed44 | -8.5446 | -67.114403 | 2024-10-08 01:48:32 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1d4d5991-8f78-3e25-bb44-ec3eb8c7d2e0 | -2.4348 | -66.470497 | 2024-10-08 01:50:08 | METOP-B | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8b3fc6ff-077f-3789-b0c1-8cf16fde82e9 | -2.4332 | -66.463402 | 2024-10-08 01:50:08 | METOP-B | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9478d98f-fe3a-3e42-b957-8e7be5df0155 | -5.5716 | -44.8927 | 2024-10-08 01:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 99427098-579a-3e70-9345-9b1bfd8b5030 | -5.5718 | -44.87 | 2024-10-08 01:55:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 4992d0ce-5187-3f7e-a653-0338c440bccf | -6.2043 | -47.3051 | 2024-10-08 01:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 136b3fd9-ee88-36f0-824e-ba8e4af2301e | -6.2045 | -47.2832 | 2024-10-08 01:55:41 | GOES-16 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f40b8d0d-c9df-3b17-a4bd-314a1f162a61 | -9.4086 | -66.5624 | 2024-10-08 01:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 41c4cc14-0fbc-3d87-96f7-de9306e04595 | -9.4087 | -66.5438 | 2024-10-08 01:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 93d722b7-6d5b-3dbc-b644-2e08140eb6a8 | -9.445 | -66.7289 | 2024-10-08 01:56:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| c6b882b2-520e-3ed8-aff9-98f461110582 | -9.4635 | -66.7283 | 2024-10-08 01:56:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| f8ff30c5-8f92-3338-b4c3-76c2aaaad1b7 | -9.5351 | -63.5771 | 2024-10-08 01:56:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 733fb01f-7446-30b8-8a36-ed9ab8e07e6c | -9.5537 | -63.5764 | 2024-10-08 01:56:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.5 |
| d22df51e-3df9-31f9-846b-34d41af0441f | -10.1448 | -55.2078 | 2024-10-08 01:56:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| e4ac0694-42cc-38ac-8e8e-ff0567314677 | -10.1451 | -55.1876 | 2024-10-08 01:56:04 | GOES-16 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 8b917fc6-8c2b-36a6-9f3a-8364a2f0797c | -10.6256 | -55.9154 | 2024-10-08 01:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 32d49e99-3f14-3a5c-a86e-67ca6f3694ef | -10.8754 | -63.9169 | 2024-10-08 01:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 7f10000e-078f-3858-b8d0-27402c000084 | -10.8755 | -63.8979 | 2024-10-08 01:56:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.3 |
| f45adb24-3941-329c-878d-02f32a0d28c1 | -11.2292 | -51.2879 | 2024-10-08 01:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 109c86c1-c1de-3d99-9f36-f08950971314 | -11.2295 | -51.2667 | 2024-10-08 01:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 52693a77-5964-3a6a-bd86-4ce5e76b999d | -11.2479 | -51.3071 | 2024-10-08 01:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 1551ae3e-18bb-3a11-b5f5-327b965cd20c | -11.2482 | -51.2859 | 2024-10-08 01:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 121.8 |
| b0fb3841-b025-33d4-b27a-c683a4532557 | -11.5233 | -65.137 | 2024-10-08 01:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 529d6b11-b3a8-3c47-a98e-ddc0b0ebde5b | -11.6806 | -64.0312 | 2024-10-08 01:56:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 992559aa-9260-3fd3-a7b2-a5c193c8597d | -12.3616 | -47.0986 | 2024-10-08 01:56:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 7fe3302d-5c19-3122-8cb7-668225702dec | -12.5717 | -53.0753 | 2024-10-08 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 3b07819b-93a2-39ba-905e-25ceebb31754 | -12.572 | -53.0544 | 2024-10-08 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 526e84ef-b6f0-3eae-b22b-6e2df8d497e8 | -14.8177 | -50.7974 | 2024-10-08 01:56:29 | GOES-16 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 101.7 |
| a6c99814-00e1-394c-908c-1716c32ba50f | -16.5462 | -57.7344 | 2024-10-08 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.1 |
| 5ffad694-2306-3be9-a25e-6829d779ed72 | -16.5466 | -57.714 | 2024-10-08 01:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.4 |
| 17add528-c812-31d7-b587-b45667e09a64 | -16.5658 | -57.7322 | 2024-10-08 01:56:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 36.4 |
| ca793fb5-3bf7-366f-bf3b-3e7bca11964a | -16.6531 | -57.1305 | 2024-10-08 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.3 |
| 9e6e63c2-3340-334d-8556-31030a4f5d52 | -16.6534 | -57.11 | 2024-10-08 01:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 33.5 |
| e396964e-3e22-3193-a799-585757efb743 | -16.9211 | -57.4881 | 2024-10-08 01:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 7ce68d0a-3556-303c-b3a1-05e75c00b684 | -17.0123 | -56.6773 | 2024-10-08 01:56:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 45.3 |
| ddc778a3-fd61-3888-987b-9d0d0d21dec6 | -17.3353 | -55.0156 | 2024-10-08 01:56:43 | GOES-16 | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| 5396722a-6e10-3bf8-aaf8-04883a3203c2 | -18.6192 | -57.2603 | 2024-10-08 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 87e5b4a7-560b-3548-a27c-0395d74c4f40 | -18.6195 | -57.2396 | 2024-10-08 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 47.2 |
| cb8771c3-918a-339e-b0b7-112ccb787077 | -18.6394 | -57.237 | 2024-10-08 01:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.3 |
| efa071aa-15aa-3eaa-95df-fa576c3fa748 | -19.0039 | -50.2502 | 2024-10-08 01:56:52 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 62d599ad-535a-3930-b718-a3876dedb80e | -19.0045 | -50.2277 | 2024-10-08 01:56:52 | GOES-16 | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 0c7380e2-f255-332c-b385-e743aaa7dcb6 | -20.4144 | -43.9356 | 2024-10-08 01:56:58 | GOES-16 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 126.0 |
| 197f9163-f996-317a-ad7c-af944fa471d5 | -20.3732 | -43.9468 | 2024-10-08 01:56:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 133.0 |
| fe3d8d0d-6c1c-3e64-914d-fd8ffcf06120 | -20.374 | -43.922 | 2024-10-08 01:56:58 | GOES-16 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| fb4334b2-51b0-32ee-81fa-68c49743ec7a | -20.3938 | -43.9412 | 2024-10-08 01:56:58 | GOES-16 | MOEDA | MINAS GERAIS | Brasil | 3142304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 261.4 |
| b04159fa-73e8-39ec-a8fe-e7d7cbd164b1 | -20.3946 | -43.9163 | 2024-10-08 01:56:58 | GOES-16 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 89.9 |
| 65c3c660-f9eb-3397-92af-8fb5acd05b48 | -20.6602 | -45.9105 | 2024-10-08 01:57:00 | GOES-16 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 9aad67aa-d495-3c12-afc1-5fc70b09bca2 | -20.43 | -48.78 | 2024-10-08 02:03:26 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 72a9b7df-b827-351c-b2dc-7b8963bf9163 | -20.43 | -48.84 | 2024-10-08 02:03:26 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c874dd5f-6f1a-3799-a80c-78ed3bf1f722 | -20.34 | -48.84 | 2024-10-08 02:03:29 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 8700df3c-8304-31d4-82ac-66bd6ad10182 | -20.34 | -48.78 | 2024-10-08 02:03:29 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3f647de7-ffea-3992-bb2f-e722db1c6bd8 | -20.37 | -48.86 | 2024-10-08 02:03:29 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 74973cf0-8288-3282-8681-286dd2601c54 | -20.37 | -48.8 | 2024-10-08 02:03:29 | MSG-03 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 210504f8-437a-3e24-be2c-b006fdbbfd08 | -20.4 | -48.87 | 2024-10-08 02:03:29 | MSG-03 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d834aad4-dc8c-3c7a-972f-a052f1d1de0d | -20.4 | -48.82 | 2024-10-08 02:03:29 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ac7a2af3-f221-35df-bbb6-55bcb75c24bd | -20.4 | -48.76 | 2024-10-08 02:03:29 | MSG-03 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 964c97c0-5050-3b75-8d65-2eedbfb5139c | -5.5716 | -44.8927 | 2024-10-08 02:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 47950eb1-e82a-3a49-927c-866b6a78ae62 | -5.5718 | -44.87 | 2024-10-08 02:05:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 70c2b5da-0fe4-3ec4-9bb5-b2e2406f85b1 | -6.4402 | -38.8327 | 2024-10-08 02:05:42 | GOES-16 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 76.1 |
| 07d1a1db-1f1a-3df0-8240-ff6d16106407 | -9.4087 | -66.5438 | 2024-10-08 02:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.3 |
| a4efee1f-e9b6-3819-a2fd-edeb6ac758a3 | -9.445 | -66.7289 | 2024-10-08 02:06:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9ec57b6f-a07e-3d93-828d-bf8b82bbcbe5 | -9.5537 | -63.5764 | 2024-10-08 02:06:01 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 312bb2b4-befa-3935-bb5f-f49ad107d3d2 | -10.0653 | -45.2761 | 2024-10-08 02:06:03 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| dffbc0ae-b351-3118-9e85-fdbad409ac60 | -10.0843 | -45.2737 | 2024-10-08 02:06:03 | GOES-16 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 04542148-fdca-37b1-8da5-52332315b597 | -10.6256 | -55.9154 | 2024-10-08 02:06:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| e77a1b28-1665-3a85-a682-5665ca960619 | -10.8755 | -63.8979 | 2024-10-08 02:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 83.7 |
| a510e015-9e2d-3617-a006-a4570afe95aa | -10.8754 | -63.9169 | 2024-10-08 02:06:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 86.1 |
| bf6d1297-4fdf-302b-b5e5-739ef022e657 | -11.3473 | -50.9784 | 2024-10-08 02:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 177.1 |
| c2b6d4fb-425a-3066-9bbf-cd84c5db0389 | -11.3078 | -51.0889 | 2024-10-08 02:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |


[Clique aqui para ver as próximas entradas](README25.md)
