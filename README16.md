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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e1cfde8-c883-3e4b-945f-1855e703116d | -4.122 | -46.678001 | 2024-09-27 00:36:06 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c362cfae-3add-306e-b84a-118359afd5c8 | -4.1237 | -46.6856 | 2024-09-27 00:36:06 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e71f8dc2-9478-3164-bdfd-04db3e1bcfb8 | -4.1255 | -46.693199 | 2024-09-27 00:36:06 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fb41c49e-4778-3aff-ab19-801f84c329f9 | -5.0213 | -50.755798 | 2024-09-27 00:36:07 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a9cacc4-111a-34d5-bbae-1c9e68373b8c | -4.107 | -46.792702 | 2024-09-27 00:36:07 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab30b2a5-f9a4-3cd6-aca7-bcc7f3b89e12 | -4.1087 | -46.800201 | 2024-09-27 00:36:07 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f652fbb4-b72c-323b-a857-90dc425642d1 | -4.0989 | -46.802399 | 2024-09-27 00:36:07 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8c2d4dc9-5089-30c1-b245-4d4a71741824 | -10.7056 | -64.1516 | 2024-09-27 00:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 48b53ac2-1f75-3d65-a027-04fdde9d63cc | -10.7057 | -64.1327 | 2024-09-27 00:36:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 393d7c0a-6768-3d43-a6db-22aead17b8d0 | -10.8541 | -57.435 | 2024-09-27 00:36:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 395a3511-798e-3bf0-a81b-520b3b2ad750 | -10.8729 | -57.4336 | 2024-09-27 00:36:08 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 695917f4-5cd8-30d6-93ce-293477c61e25 | -10.9264 | -54.2692 | 2024-09-27 00:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 297.3 |
| 380592f0-b125-3254-aef2-e255a5eeaa5b | -10.9267 | -54.2488 | 2024-09-27 00:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 292.3 |
| 8fffbadf-b107-3268-a987-2aa6ee853666 | -10.9453 | -54.2676 | 2024-09-27 00:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 156.4 |
| 3c10384e-1f0b-3284-ac59-bb082dc1e2e6 | -10.9456 | -54.2471 | 2024-09-27 00:36:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 04f68e42-1441-3b21-b9a6-7521cfb85967 | -11.1219 | -50.8328 | 2024-09-27 00:36:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 4c256e07-c3bd-3216-8d5f-73c7dbc24cad | -3.9117 | -46.434502 | 2024-09-27 00:36:09 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f54068e9-bb34-3f23-924d-82fa1b84ae9c | -3.9134 | -46.442299 | 2024-09-27 00:36:09 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 10d769d2-56a8-327f-8f2e-9394cf0c6421 | -3.9152 | -46.4501 | 2024-09-27 00:36:09 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 172bbdf2-422a-3da3-af3e-91eeae0e7a63 | -3.9036 | -46.4445 | 2024-09-27 00:36:09 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 787b0e27-67fe-3d22-bdd0-3bf7b428338c | -3.9054 | -46.452301 | 2024-09-27 00:36:09 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 28040973-28a6-3fa0-91b7-206cefcc109a | -3.3511 | -44.180401 | 2024-09-27 00:36:09 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6216260f-f9d8-3728-bd5e-c4c0edebf646 | -3.3413 | -44.182701 | 2024-09-27 00:36:10 | METOP-B | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8aded888-aa79-30d5-b96d-0fa853a14d1c | -4.2472 | -48.133499 | 2024-09-27 00:36:10 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04fbd10a-6620-3eb0-9b0d-84d002e1441c | -4.2487 | -48.140499 | 2024-09-27 00:36:10 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be884a37-b1fb-373c-b032-b884449adcc5 | -4.2503 | -48.1474 | 2024-09-27 00:36:10 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58edc42f-d714-36e7-8f51-35a1d235962b | -4.3684 | -48.6698 | 2024-09-27 00:36:10 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5e09233-2907-3995-a68a-0646111b63a3 | -4.37 | -48.676601 | 2024-09-27 00:36:10 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e5c937f-5caa-334e-93b4-a4e9dbc809e7 | -4.2174 | -48.1838 | 2024-09-27 00:36:10 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d67931e4-25b0-3088-b41d-a6af68744d0b | -11.2788 | -65.2793 | 2024-09-27 00:36:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 16133bba-39e5-3af8-a3d6-48d40d376273 | -4.1261 | -47.963402 | 2024-09-27 00:36:11 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a147643a-a9b1-3156-8d5b-40d7243b0df7 | -4.1163 | -47.965599 | 2024-09-27 00:36:11 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00b3ec65-9ccb-3ea8-9715-c2ce328d25c5 | -4.0464 | -47.929901 | 2024-09-27 00:36:12 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 950def65-d38f-39ed-a569-ed3298ca70f9 | -4.2012 | -48.613602 | 2024-09-27 00:36:12 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3f4d4cc-b13b-3322-a642-b4bef4a0ab50 | -4.1899 | -48.609001 | 2024-09-27 00:36:12 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a5712b6-df29-37f0-8a86-a45e5f4d5729 | -4.1914 | -48.615799 | 2024-09-27 00:36:12 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd68c37a-611a-31d9-aa97-613f6e2594d0 | -4.193 | -48.6227 | 2024-09-27 00:36:12 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9159779d-b7da-3183-abf7-9b5265edbea9 | -11.5872 | -63.9596 | 2024-09-27 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 9a1f2a07-def9-3b44-8f41-c4b7c6d5e398 | -11.5874 | -63.9406 | 2024-09-27 00:36:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 25e626f5-9502-3c0b-88f5-3d2ec5e7b55d | -4.5029 | -50.092701 | 2024-09-27 00:36:13 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b08f6039-d091-35d4-a322-bebc36b33016 | -4.5045 | -50.099701 | 2024-09-27 00:36:13 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6eb18ee-2b6d-345a-9e76-bbbd2f22592c | -4.0812 | -48.265099 | 2024-09-27 00:36:13 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f7371e-a10d-39b9-9063-72294466c40c | -4.4931 | -50.094898 | 2024-09-27 00:36:13 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 861507cd-6172-3f2e-8d82-bdff4a3650c3 | -4.4947 | -50.101898 | 2024-09-27 00:36:13 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17f9e631-5a0c-31ed-a414-a811b39278ae | -4.6338 | -50.725101 | 2024-09-27 00:36:13 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc084c79-44f4-3e24-8c88-05268df9fb4d | -3.9716 | -47.8731 | 2024-09-27 00:36:13 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd431651-aa8f-3174-b320-19a67e53236d | -3.9732 | -47.8801 | 2024-09-27 00:36:13 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe06edd9-4085-3206-bc50-f96963b98655 | -4.6111 | -50.9468 | 2024-09-27 00:36:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d57fc58-8521-32d9-9c96-4ffe19a32639 | -4.6128 | -50.954201 | 2024-09-27 00:36:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6adfc841-cb5f-3abc-bf3e-2da04fb8a543 | -12.1672 | -50.8004 | 2024-09-27 00:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| ea03d01d-cd46-3f81-839b-11f6d86c98b2 | -12.1675 | -50.779 | 2024-09-27 00:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 38ab06cb-326d-37f3-a557-0f7a4d7a8bc4 | -12.1863 | -50.7981 | 2024-09-27 00:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 272.8 |
| 7eaee9fb-bf1a-3764-bf0c-990a7fefc29e | -12.1866 | -50.7767 | 2024-09-27 00:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 2af1eb1f-6c64-351a-a390-b824ac3499d7 | -12.2053 | -50.7959 | 2024-09-27 00:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 5b09dc9c-7ed5-35e3-bf93-5466f133dd88 | -12.2057 | -50.7745 | 2024-09-27 00:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 000169c6-583d-30cb-923d-e91f8c3363db | -4.4123 | -50.4701 | 2024-09-27 00:36:15 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78ec3403-193e-3d55-9786-5400f5d002f7 | -4.4139 | -50.4772 | 2024-09-27 00:36:15 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52cf0de6-cbaf-3082-b8b2-cf93047676ff | -3.8913 | -48.336498 | 2024-09-27 00:36:16 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b50898cd-1d42-3583-80d5-8709404c530a | -3.8928 | -48.343399 | 2024-09-27 00:36:16 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 355166a8-35d8-34d3-bf9a-916a7790311d | -3.8944 | -48.3503 | 2024-09-27 00:36:16 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7585c789-aa38-330c-8411-922632a18a35 | -3.8763 | -48.361599 | 2024-09-27 00:36:16 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a77a906-3548-35bb-97ca-03c3adb24cc7 | -12.4503 | -54.9858 | 2024-09-27 00:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 1f6731a2-be4c-32ea-b0a5-3587e02eb26d | -12.4501 | -55.0063 | 2024-09-27 00:36:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| d2480624-a9f6-3230-8c07-259b9d7964ef | -3.6951 | -47.608002 | 2024-09-27 00:36:17 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f852704-5ca7-3d3e-981d-4138e6f83679 | -3.6967 | -47.615101 | 2024-09-27 00:36:17 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6217fe-6a68-3657-902d-ed201442f968 | -12.6636 | -54.6782 | 2024-09-27 00:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 51d96e60-0249-3a00-b9c8-a9af3b52886f | -12.6639 | -54.6577 | 2024-09-27 00:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 83629bc2-9e5f-3187-98ed-823cff7cc31d | -12.6824 | -54.6968 | 2024-09-27 00:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 7c32d06f-0598-3643-ab22-d1d1fa3fd8e6 | -12.6826 | -54.6763 | 2024-09-27 00:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 0d0de191-0933-3eaa-910b-c8a72dc8784d | -12.6829 | -54.6558 | 2024-09-27 00:36:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| b2649e32-1d05-3796-97a5-dc36abbd64c4 | -12.8437 | -54.0422 | 2024-09-27 00:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 232f7dad-9060-3c2b-a76e-2a40f69c1810 | -12.844 | -54.0215 | 2024-09-27 00:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 6b0492b2-5316-3f28-8f17-a3a0e0acab2d | -12.8628 | -54.0402 | 2024-09-27 00:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 136.5 |
| f958f08c-f470-3e08-a695-27df980cbf5b | -12.8631 | -54.0195 | 2024-09-27 00:36:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 0f16012b-f497-3288-84f0-5169cbc0d44d | -3.8592 | -48.9697 | 2024-09-27 00:36:19 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 026558b7-e0e8-3527-ab50-1b670f233fef | -13.4413 | -44.0267 | 2024-09-27 00:36:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 4cc8dd2e-6ac6-3037-82d5-e7c19d9892cc | -13.4418 | -44.003 | 2024-09-27 00:36:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1945873f-0955-3218-bab8-f7447a20cf24 | -3.2174 | -46.777901 | 2024-09-27 00:36:21 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ac3ba31-1f6b-3c61-bc28-73c5b87bdd36 | -3.2192 | -46.785599 | 2024-09-27 00:36:21 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f91d5fe3-7a54-3f3f-8183-e29973372316 | -3.2076 | -46.780102 | 2024-09-27 00:36:21 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfceaabf-7b2c-310b-b99c-af44acee0553 | -3.2094 | -46.7878 | 2024-09-27 00:36:21 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb729b75-8519-3ae4-b685-a671ec2328d5 | -4.0536 | -51.030102 | 2024-09-27 00:36:23 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb6bef59-4111-3c71-971a-c97ef8cf625d | -4.0553 | -51.037498 | 2024-09-27 00:36:23 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f0287630-b6cc-3259-aa5d-f19a20befe45 | -3.4618 | -48.807098 | 2024-09-27 00:36:25 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a26a7965-9e73-3667-8f69-d1d104190868 | -3.4634 | -48.8139 | 2024-09-27 00:36:25 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dfb710cf-afec-3f25-8654-0f7b3538ea01 | -14.0521 | -57.927 | 2024-09-27 00:36:26 | GOES-16 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 03cd34a6-f339-33b4-96a1-3738e0ae2a7c | -14.0524 | -57.907 | 2024-09-27 00:36:26 | GOES-16 | CAMPO NOVO DO PARECIS | MATO GROSSO | Brasil | 5102637 | 51 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 55f9e4d2-dd59-330c-8157-2177d5b2e886 | -3.8757 | -51.1549 | 2024-09-27 00:36:27 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 916d4b58-90fd-35d3-b0dd-4248c67fa9da | -3.8773 | -51.162399 | 2024-09-27 00:36:27 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a6d543f-8330-3212-86fc-3298b1b42eb7 | -14.7109 | -45.5096 | 2024-09-27 00:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 98c60213-a116-3204-9a18-b89d557d41b7 | -14.7114 | -45.4863 | 2024-09-27 00:36:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| de04507e-0725-3b25-9054-ee649d6b0e3c | -3.303 | -49.107601 | 2024-09-27 00:36:28 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d7bc64a-d8a6-3718-b3cb-3ff653998ccc | -3.5654 | -50.365898 | 2024-09-27 00:36:29 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb3bf9c0-5363-39a4-8b3d-68be78544dff | -3.567 | -50.372898 | 2024-09-27 00:36:29 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64736a09-a42a-3ddb-9451-0fd5febec89b | -3.5686 | -50.380001 | 2024-09-27 00:36:29 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea6f858f-3dcc-39be-afaf-9363523646cb | -3.5701 | -50.387001 | 2024-09-27 00:36:29 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc352a58-e28d-3cc4-b3ed-22c0483d0ac0 | -3.5556 | -50.368099 | 2024-09-27 00:36:29 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74c98f06-c2dd-38aa-92c4-0d5ae9402d15 | -3.5572 | -50.375099 | 2024-09-27 00:36:29 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d7ab0f35-62b6-3fc3-97c4-283bafaf526d | -2.7198 | -46.719601 | 2024-09-27 00:36:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 57dc4dec-ffc8-34d5-a500-02dc4ab4babf | -2.7216 | -46.727402 | 2024-09-27 00:36:29 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README17.md)
