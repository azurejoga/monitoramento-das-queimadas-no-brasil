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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56d4044d-8f02-3840-9e1e-94652f1d8eca | -4.45206 | -49.61915 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e1f2e458-3967-36dd-8856-705084e727ac | -4.45144 | -49.62297 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8f436034-1840-3409-b331-ec24b61f2b16 | -5.06211 | -49.79874 | 2024-10-04 04:32:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d48bea2-f705-337d-9c00-ec40d7e7e3ce | -4.65617 | -49.53374 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b8904dcd-64b8-387d-9b7c-bc9e15bbe32f | -4.47537 | -49.74142 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15c49220-a457-33ae-80f6-26cbd7b8b6b9 | -4.06374 | -49.25663 | 2024-10-04 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb877015-b5d4-3cb4-aa4c-f78efdfe9325 | -4.04033 | -50.38685 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d869c5d3-056f-3a77-8bef-99c38ad01cac | -4.03671 | -50.38628 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c97ea56b-e643-30db-84a3-3f996323c9ae | -4.03497 | -49.56713 | 2024-10-04 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8451915b-6020-3345-b7ab-fd1f479d493f | -4.02799 | -49.566 | 2024-10-04 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6f7d3dce-2efd-3fce-8402-43063c568ba1 | -3.99271 | -49.67232 | 2024-10-04 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4ecfe38-3c5c-3bc2-bfdb-ca3046d06d04 | -3.92875 | -49.68971 | 2024-10-04 04:32:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49098796-aa88-3569-963e-98c5a478e92d | -3.84643 | -49.39368 | 2024-10-04 04:32:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52548d62-6ce6-3914-9140-bb009713c72e | -4.38057 | -50.42456 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c6cef3a0-e30b-369f-9696-bb5efb8b5bd2 | -4.3799 | -50.4287 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 16b7a8fe-be20-3a17-88e6-26c6247c00ac | -4.66423 | -50.88225 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c33a5e30-7da1-39e9-b777-fa31d9edef95 | -4.66351 | -50.88657 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ec9d401-8c9c-3f28-a37a-cd1003dccfb7 | -4.66203 | -50.88392 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8b84ec05-6729-3ba6-81a7-c69aa4b0a1a5 | -4.65982 | -50.88599 | 2024-10-04 04:32:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ea9ce7a7-e572-38c5-84f6-7bc700dfae3f | -5.6427 | -49.71251 | 2024-10-04 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6a22a2c-2f37-392f-8651-1fb063c01a36 | -5.63924 | -49.71195 | 2024-10-04 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 81d0b471-6ff4-3d30-a5ca-b90a8b454083 | -5.53949 | -50.94019 | 2024-10-04 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 506c34dc-cce9-3c31-9629-40ecab8712c3 | -5.51668 | -50.04354 | 2024-10-04 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d031f5b-2bd2-3748-b90c-acbc426ff1f9 | -5.51317 | -50.04301 | 2024-10-04 04:32:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3db71739-4fbe-37cc-a433-5c50d363a700 | -7.82686 | -50.52961 | 2024-10-04 04:32:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdd4f588-d831-33b4-b746-c10e78101386 | -7.82048 | -50.52454 | 2024-10-04 04:32:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfafb312-7ada-3fce-b9ee-4c3ce859bdac | -7.80654 | -50.23759 | 2024-10-04 04:32:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b3a6e7ef-c0d9-3a0f-8779-1691d9a2fc71 | -9.32891 | -51.12277 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9daae856-a93b-34c1-8b7a-212ad34175e9 | -9.32825 | -51.12677 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e54e9a00-643c-3ac2-89cb-ca484a39ee87 | -9.32759 | -51.13077 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d361c923-9d7a-35ad-850b-ac73ac84dbeb | -9.32693 | -51.13478 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2c0872a-98c6-3e57-bab8-1911ea92ed0c | -9.32537 | -51.12219 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71558fb2-4ca8-3f5f-bb12-fa4dd2eeddc5 | -9.32471 | -51.12619 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 067e0877-4853-359c-a58b-353b43319388 | -9.32405 | -51.1302 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 336e2c2b-16a3-3f5c-96bc-dbc2a1876a03 | -9.32339 | -51.13421 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f295e7b-f533-3087-b47a-b8a722d0e51c | -9.32183 | -51.12161 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee5c42ae-9106-3528-a54c-adffaa35a1c3 | -9.32117 | -51.12562 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d509eac-5946-3201-9cd2-84561b0d9cf5 | -9.31918 | -51.13764 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5bec0092-e55c-3a5f-ad7d-ffd09f8b5745 | -9.31895 | -51.117 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3581b41b-ea63-3d70-915f-75d040dc79f3 | -9.31829 | -51.12103 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71ea346c-7845-3369-b40a-d00955d773d0 | -9.31762 | -51.12504 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 06605825-c321-3595-aab2-21ac7e00aa3b | -9.31608 | -51.1124 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30bfd362-2ed1-3ff7-8ae3-14466e411a2e | -9.31564 | -51.13705 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 000f08c7-e4ba-3b74-89e8-b89415c1d321 | -9.31541 | -51.11642 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed7af09b-af3c-3890-b0e0-5452d50e1108 | -9.31475 | -51.12043 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 74fe8e9a-ac95-3a63-969f-263e44b34a41 | -9.31254 | -51.11183 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dc18d536-1f55-3aa4-ac5c-366faa5ee72a | -9.309 | -51.11125 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72cdd5c8-0223-3ce0-8286-3dc9aeab8fd9 | -9.30833 | -51.11525 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e1ee5b7-b296-393d-9457-5eb07c7ac5cf | -9.30546 | -51.11067 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d082614-044b-343b-af7a-59a432a07e6f | -9.30479 | -51.11466 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a67f0ab-ccf5-3f24-981e-53ebfe282245 | -9.30437 | -51.07349 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 659bb31e-3e58-3e06-b13e-62858be41647 | -9.3037 | -51.07749 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd7e5788-cb9d-37c0-89dd-550dd22f266e | -9.3015 | -51.06892 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5cf2a6f6-a148-3ee2-98d5-a6e7f3285857 | -9.30083 | -51.0729 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0b9e3b3-f4f7-317d-bbd5-1cd3e9c25b44 | -9.29929 | -51.06039 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 611d758e-d84d-3111-a51d-7c02b237cc32 | -9.29576 | -51.0598 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7ee2dc0-e587-371a-9183-bbf0e0cefc32 | -9.29222 | -51.05923 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a8706ccc-c1b2-3af4-aa97-1ff69c66e5ad | -9.18848 | -51.31597 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27ffc065-b747-33af-95ae-092c0fea49ac | -9.1196 | -51.52972 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a20bb750-538f-3f0d-a775-f759c82b74be | -9.11822 | -51.53794 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41e15860-adb9-3790-af5c-693f3a1b11bd | -9.1174 | -51.5207 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dde089f1-4b91-3532-bec2-4084a5cde090 | -9.1167 | -51.52486 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb27781d-4911-38cf-bafa-e8e86a4a31d1 | -9.1138 | -51.52002 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9bfb2f90-eb38-3f3e-b03d-69e0b43e4ba2 | -9.11172 | -51.53238 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fac571f4-f7b3-3094-aa94-8f0252a86930 | -9.11104 | -51.53644 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f89efb58-41ee-3d87-bbfb-22b1864b2a8b | -9.11087 | -51.51535 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 059f228f-4143-3815-92cf-93228eaee886 | -9.10742 | -51.53587 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e62ea148-82cc-361c-a23d-cb2c970d62af | -9.106 | -51.52055 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07b47881-7a22-37e5-9031-cb9369e4bf67 | -9.10533 | -51.52465 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61342d95-a522-3273-ae10-67ab81b59668 | -9.10517 | -51.52712 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a4cac28-7dc6-3a73-9526-40b4d835676d | -9.10466 | -51.52874 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4daf0ce0-e3f1-30bf-ac98-c6c4e584ea9d | -9.10448 | -51.53121 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ce2c9289-9bb3-3f3e-9a19-aa3dafc069c7 | -9.10379 | -51.53533 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49b5aedb-8426-31dc-8a17-faac95f4cd46 | -9.10237 | -51.52002 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2658fab9-6b57-396d-b07c-f61bba87ad12 | -9.1017 | -51.52412 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3be897cc-b1fc-366a-967c-d610179ffee5 | -9.10103 | -51.52824 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8936b096-2a6f-3ce0-8860-a0385567f1dd | -9.10084 | -51.53072 | 2024-10-04 04:32:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 81fd69bd-8e39-3a57-a461-b9b6ed65ad67 | -9.33254 | -50.79546 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a16e1253-cebe-3805-92b7-4b9e5d6c0067 | -9.33189 | -50.79934 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5c04040d-4157-3fdb-826a-2172a71484ad | -9.33164 | -50.79548 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| abdd76ba-f804-3fcf-b881-051b5217a902 | -9.33125 | -50.80323 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 68f4986a-2908-36d8-9cc8-ce9e1e9dec54 | -9.33101 | -50.79938 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6f9eaff3-5ed7-37fc-9121-0cde7abf2dac | -9.3306 | -50.80711 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 38686d8e-6c9c-3be5-ad40-f30072e9f084 | -9.33038 | -50.80327 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 08c537da-97b2-35b2-8855-1818a78de6e6 | -9.32975 | -50.80716 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 784151b0-5fe2-3b32-8b30-700763b32231 | -9.32905 | -50.79486 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 528d99e5-e597-32de-a33f-bfb434f054bd | -9.32878 | -50.79098 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3fac23f9-34f7-33ab-b9f8-0d711e75ff96 | -9.32841 | -50.79873 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 48dfb106-e821-38c2-99da-adc5b3b7abf6 | -9.32815 | -50.79487 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ffdb816c-4960-3ab9-bd72-44faabeb03e3 | -9.32776 | -50.8026 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 686b9f67-ee5b-33d6-b04a-918c51bd61e9 | -9.32752 | -50.79875 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cfe87beb-729c-3308-9ec6-ae6d9fa42dc6 | -9.32712 | -50.80647 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b7cd5fe2-75fa-305e-bcfa-ac0c9c269ad9 | -9.32689 | -50.8026 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2286dd0c-4123-32a6-85f6-7ce1158b4d1d | -9.32647 | -50.81037 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 97938aac-0f82-333d-ba48-114c5f939c5b | -9.32627 | -50.80648 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| fe6532a5-f2c6-3c32-a6a5-02531f329a5f | -9.32592 | -50.78649 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58e75bd9-09e0-306a-9a9e-5180b829b168 | -9.32564 | -50.8104 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 94397d78-de12-318b-ba41-e0b8f7c34d13 | -9.32529 | -50.79037 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 60c9a1b8-49a2-322a-a17c-07e6c4270de3 | -9.325 | -50.8143 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b3408c5-f912-3ba9-b798-8c920b9273a7 | -9.32466 | -50.79425 | 2024-10-04 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |


[Clique aqui para ver as próximas entradas](README108.md)
