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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9234abd-0f47-3f5e-85a1-9149d58a0644 | -19.6624 | -58.0362 | 2025-01-13 00:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.4 |
| 63a1febf-0c8e-3583-a4c8-a4e5c8cba273 | -28.7599 | -55.6114 | 2025-01-13 00:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 79.8 |
| 2c827c8d-6caa-3d63-9f5f-7398634a6a09 | 2.1768 | -61.8158 | 2025-01-13 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 9bcd29e0-9851-3fb2-af2d-f212f36bcee7 | 2.195 | -61.7968 | 2025-01-13 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 8ac8235c-dcfd-3ddd-a7a4-ae6e520e6907 | -28.7599 | -55.6114 | 2025-01-13 00:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 88.8 |
| da2238f2-bc4c-390d-b0cf-27d927844abd | 2.195 | -61.8156 | 2025-01-13 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 55935001-796b-3019-b550-ec988d3e8e04 | 2.1768 | -61.797 | 2025-01-13 00:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 5bc8d85c-b4b8-3540-a656-b8bb29f75db1 | 2.1768 | -61.797 | 2025-01-13 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 17920971-0165-302b-860d-6290559fb621 | 2.1768 | -61.8158 | 2025-01-13 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 304d6c34-fb32-3b55-a826-d997b67afc12 | 2.195 | -61.8156 | 2025-01-13 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 57bce4eb-7abc-3881-be46-b86d6ec61866 | -28.7599 | -55.6114 | 2025-01-13 00:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 93.8 |
| a133b140-61b0-3e7b-8f92-2d16a927dd28 | 2.195 | -61.7968 | 2025-01-13 00:20:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 72b67ec9-f95c-335a-b186-9cfe690c1ea6 | 2.195 | -61.7968 | 2025-01-13 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| e0799ff2-54c2-393d-8eb3-955c1bf7ed38 | 2.195 | -61.8156 | 2025-01-13 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 35dfab30-d7bc-3749-b500-db9fb61808db | -28.7599 | -55.6114 | 2025-01-13 00:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 82.7 |
| fcc2549f-fe9e-3798-a264-7c928e33d716 | 2.1768 | -61.8158 | 2025-01-13 00:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| c2b0b46b-aa98-3558-8a5b-bc509018c1af | -28.7599 | -55.6114 | 2025-01-13 00:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 79.9 |
| 1dc49527-fc8d-3034-b528-5143d86944ce | 2.195 | -61.7968 | 2025-01-13 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 97340457-436a-3998-91b3-3063a4780dfd | 2.1768 | -61.8158 | 2025-01-13 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 150af349-3407-35fb-ae9c-8d6b3b82c545 | 2.195 | -61.8156 | 2025-01-13 00:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6cc8a406-44d4-3bfa-b2a1-28e5d791e5e0 | 2.8335 | -61.8671 | 2025-01-13 00:48:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0e3fed02-e839-3f58-931d-daa5ccc929a1 | 2.8379 | -61.890999 | 2025-01-13 00:48:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0a955061-8c2f-3351-9533-aa7c177d48e5 | 2.8186 | -61.886398 | 2025-01-13 00:48:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7e395cab-6974-3a80-92f0-a7a209d6463a | -20.078501 | -48.733799 | 2025-01-13 00:48:00 | METOP-C | PLANURA | MINAS GERAIS | Brasil | 3151602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 36666437-2deb-3b41-900a-7045912ef6fc | -1.376 | -52.1712 | 2025-01-13 00:48:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b2ec685-638e-3fe0-bb95-d3390d0e5247 | -20.812 | -48.709801 | 2025-01-13 00:48:00 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9321f26e-01bb-36eb-bb92-b7ed1bef8809 | 2.8431 | -61.869301 | 2025-01-13 00:48:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5c2c475c-a339-39c3-884d-5f70cc0d432c | -20.8104 | -48.702 | 2025-01-13 00:48:00 | METOP-C | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| eefb31a2-ae51-3ec1-b4a6-8825c34413fb | 2.8283 | -61.888699 | 2025-01-13 00:48:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 09285e2a-ca86-39c5-a22a-725fc9aa82c2 | 2.195 | -61.7968 | 2025-01-13 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c0c41de4-bc4f-3d8d-bdbe-d4b374028f5a | 2.1768 | -61.8158 | 2025-01-13 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 58.0 |
| c7d2e961-77f0-324d-88fa-a88df6c8febc | -28.7599 | -55.6114 | 2025-01-13 00:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 81.0 |
| b469658c-655c-3675-bfa7-93534d00a742 | 2.195 | -61.8156 | 2025-01-13 00:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c32194cc-372e-39b7-ab65-db44789e8615 | -28.7599 | -55.6114 | 2025-01-13 01:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 75.0 |
| f2979c2d-a43e-39ea-862f-9e29abc7c389 | 2.195 | -61.7968 | 2025-01-13 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 36b51e2a-1dc4-3f44-83bf-178353c08abf | 2.195 | -61.8156 | 2025-01-13 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 85346302-d35a-3efa-a5b8-fcdbe67230be | 2.1768 | -61.8158 | 2025-01-13 01:00:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 11116c0f-8b8e-385e-b6e0-5776f4cc49ce | -28.75957 | -55.623 | 2025-01-13 01:09:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 35.1 |
| ad256867-6d90-3af0-9e4e-b6e6d557acbd | -29.55167 | -51.80152 | 2025-01-13 01:09:00 | TERRA_M-M | PAVERAMA | RIO GRANDE DO SUL | Brasil | 4314159 | 43 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 9b1719b1-4125-3834-b8c9-ac31ecfd08d0 | -28.75774 | -55.60382 | 2025-01-13 01:09:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 46.5 |
| bd619720-5bb6-3c84-8dc3-dbe39c574933 | -28.7476 | -55.62451 | 2025-01-13 01:09:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 60.1 |
| 48875ff0-9b5a-34c1-b1df-dcd9c4affbe2 | -21.44287 | -48.61468 | 2025-01-13 01:09:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 4a6c4474-f54c-3fbe-bc74-7ba460fdb960 | -20.71756 | -48.6362 | 2025-01-13 01:09:00 | TERRA_M-M | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 01989633-b25f-3d3f-ba64-ea8cc7294058 | -21.44116 | -48.60369 | 2025-01-13 01:09:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| bb176178-7fbe-33d0-918c-ad23e56de2c7 | 2.1768 | -61.8158 | 2025-01-13 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| f98b943b-7ce9-3613-b898-5c63e47042d2 | 2.195 | -61.7968 | 2025-01-13 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| f9dbfd49-6941-363f-b82f-15c836c0b09e | -28.7599 | -55.6114 | 2025-01-13 01:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 87.4 |
| b9a91bb2-e730-32e1-a36b-d81b61be2011 | 2.195 | -61.8156 | 2025-01-13 01:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| cd7a01d4-6c9c-3b9c-bd37-f47f0eb2357f | -19.82151 | -53.83848 | 2025-01-13 01:11:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9c8ec0de-3951-33e5-880b-3c58eed1044e | -19.82014 | -53.82786 | 2025-01-13 01:11:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f015fa47-3ab9-3a91-8738-1b71ff77fbff | -2.01288 | -52.0728 | 2025-01-13 01:15:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef750c48-1e60-384e-aa76-83df3b9f81ae | 2.44253 | -60.64964 | 2025-01-13 01:17:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4414800e-6f82-377f-86e5-c3c82f724e59 | 2.86286 | -60.92375 | 2025-01-13 01:17:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 566c9fee-eaef-36da-b1a1-9a03b5059045 | 2.18199 | -61.80617 | 2025-01-13 01:17:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 71d209ba-39fa-3be9-9f77-c00799c8a004 | 2.17955 | -61.8229 | 2025-01-13 01:17:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4f5c9111-8563-3057-b021-f314330560a6 | 1.11932 | -59.46226 | 2025-01-13 01:17:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 361080a2-a6c7-3ace-a5ba-2f4a73aaef7c | 2.19392 | -61.80793 | 2025-01-13 01:17:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 862600ad-d985-3598-84b0-9f4b7d39b3b0 | -28.7599 | -55.6114 | 2025-01-13 01:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 106.3 |
| 4b2143d9-b76d-34e9-b338-b78d3d20b0b7 | -28.7592 | -55.6345 | 2025-01-13 01:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 78.0 |
| 57d325d5-c512-3faa-80ea-a9107ba601e8 | -28.7367 | -55.6396 | 2025-01-13 01:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 68.0 |
| 67affe28-4ab9-31cf-9fd7-d52abda15bd2 | -28.7592 | -55.6345 | 2025-01-13 01:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 74.6 |
| f4af2cb7-47e3-3b36-9b4f-7336e5f8bbe8 | -28.7599 | -55.6114 | 2025-01-13 01:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 96.8 |
| ee49dc0c-02c4-34e5-99d7-6643d88f4085 | -28.7367 | -55.6396 | 2025-01-13 01:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 112.1 |
| cf75fc14-cea7-3c01-9f15-1d951e9a695b | -28.7374 | -55.6165 | 2025-01-13 01:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 71.9 |
| 5d32e748-8604-3b68-8d8f-ef8e95bc825d | 2.1768 | -61.8158 | 2025-01-13 01:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ae3a6198-304a-3911-8f76-a00036ec4be7 | 2.207 | -61.7999 | 2025-01-13 01:31:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ef16a56a-813a-37d9-82e7-b86b3d00fba0 | 2.1946 | -61.809399 | 2025-01-13 01:31:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1f5cc5fe-3b5a-3525-a8fa-787ec5bb62fc | -28.755301 | -55.5938 | 2025-01-13 01:31:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 1f3599f2-2340-3d93-b136-64ebcfd74de6 | -28.746201 | -55.641499 | 2025-01-13 01:31:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 35f690c0-ba4b-357d-b023-da19b02b4b5a | -28.7411 | -55.620701 | 2025-01-13 01:31:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 40d6c32f-0298-3f1e-884e-0cd27aef8dc4 | 2.2044 | -61.8116 | 2025-01-13 01:31:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f6a3128e-260d-3c29-82cf-c0a3133f3f88 | -28.7605 | -55.614601 | 2025-01-13 01:31:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 2f0ec2a7-3e96-3dce-90be-1bee3428685e | -28.7579 | -55.604198 | 2025-01-13 01:31:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 6505457a-dc0c-38fc-93f0-04a355ac33b8 | 2.1849 | -61.807301 | 2025-01-13 01:31:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 93adcaa9-5a08-36ba-8706-0adffacc9c91 | 2.1875 | -61.795601 | 2025-01-13 01:31:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a9969f14-3227-309d-92d1-ff450561d8c2 | -28.750799 | -55.617699 | 2025-01-13 01:31:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 11f1f62a-ab26-3413-8569-333948fa6ebd | -28.7533 | -55.628101 | 2025-01-13 01:31:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| d397c1ce-c31c-31f4-b007-bd40a287124b | -28.748199 | -55.6073 | 2025-01-13 01:31:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 3e7dc513-0f31-3499-be52-ce3bc83e0fa9 | -28.743601 | -55.6311 | 2025-01-13 01:31:00 | METOP-B | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | nan |
| 2c439a82-908f-3845-9ca3-50622fb54079 | 2.1823 | -61.819 | 2025-01-13 01:31:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 297f564d-24bf-336a-a5f4-79bb1cd20ce8 | 2.1972 | -61.797798 | 2025-01-13 01:31:00 | METOP-B | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 22b78bbb-3c42-3b93-b79b-9504217dc2f2 | -28.7599 | -55.6114 | 2025-01-13 01:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 95.7 |
| c0d98feb-8d26-3902-a769-89201acf0d96 | 2.1768 | -61.8158 | 2025-01-13 01:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| bcd0f25e-0e7b-3354-87ea-7465a91392cb | -28.7367 | -55.6396 | 2025-01-13 01:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 102.0 |
| 1434b5b1-6ea1-331b-8bdc-cbc109585ab7 | -28.7592 | -55.6345 | 2025-01-13 01:40:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 84.3 |
| 26d606f6-a82d-344d-be81-01efe4c51bc7 | -28.7592 | -55.6345 | 2025-01-13 01:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 114.6 |
| 24b1a977-970d-3928-b9f6-ec699abc4458 | -28.7367 | -55.6396 | 2025-01-13 01:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 74.1 |
| 7b8db69f-ed82-380f-9ce6-0023151c4f74 | -28.7599 | -55.6114 | 2025-01-13 01:50:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 131.1 |
| ff6debb6-de7e-393b-a52b-5fed0a36ec05 | -28.7599 | -55.6114 | 2025-01-13 02:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 153.9 |
| c76b799a-c16e-3b9c-ab8d-cbac0bae2a2c | -28.7367 | -55.6396 | 2025-01-13 02:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 158.2 |
| be41253a-f601-39cb-b10d-70c8573d98d3 | -28.7592 | -55.6345 | 2025-01-13 02:00:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 115.1 |
| ce444ca7-2fdd-3fc1-b09c-a084a1d0d4b0 | -28.7592 | -55.6345 | 2025-01-13 02:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 112.4 |
| a0835918-4a95-3aba-afd0-530bdde69872 | -28.7599 | -55.6114 | 2025-01-13 02:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 163.3 |
| fb00ba51-5da4-320f-9696-94d8946d87c0 | -28.7367 | -55.6396 | 2025-01-13 02:10:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 115.9 |
| 6a06b524-dd0f-32e5-aedf-bd5a1208af33 | -28.7592 | -55.6345 | 2025-01-13 02:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 92.9 |
| 24e60cea-3528-3bb0-ad83-881b3890f723 | -28.7599 | -55.6114 | 2025-01-13 02:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 131.3 |
| e4fcdd88-f8be-32b5-a1a4-2791909e8a81 | -28.7367 | -55.6396 | 2025-01-13 02:20:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 98.4 |
| 4a00b6de-df71-3440-82a5-1aacb86869ae | -28.7599 | -55.6114 | 2025-01-13 02:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 183.8 |
| c2ccecb4-170b-38ed-a452-606da85342ba | -28.7592 | -55.6345 | 2025-01-13 02:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 182.7 |
| b2b6ffe3-8dda-3831-ae0e-5f3d80ebd3ab | -28.7374 | -55.6165 | 2025-01-13 02:30:00 | GOES-16 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 108.5 |


[Clique aqui para ver as próximas entradas](README2.md)
