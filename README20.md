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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 449cca71-7f7e-3666-af96-d0483580b51a | -8.79054 | -66.72275 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9adc97de-126b-3bb4-8f2f-6829ce625820 | -8.99989 | -65.91663 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5502bc7f-013f-3aec-a99d-39d34eb1d109 | -9.10981 | -65.93491 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74f4fe86-893f-33d1-baf6-5e3c026c81f3 | -10.92951 | -68.58565 | 2025-10-22 06:08:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 60ef5bce-c37c-395b-bc6b-78ee77e2f13e | -10.75436 | -69.05383 | 2025-10-22 06:08:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b36ee02-2813-319f-a6e3-739f6596e8cb | -12.38084 | -63.87554 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6011f306-9c1f-37d3-8fcf-ce5c5583c0e7 | -12.2743 | -63.87262 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 80b9c56d-4f20-38ab-be88-d3c560894631 | -8.85608 | -66.79299 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c39944c5-fe04-3ad4-b3b3-07ad827c76ad | -9.00631 | -65.93486 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 046e09f9-1109-346d-9513-5453abf8da1c | -12.27469 | -63.86934 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 167bee88-e273-3725-96b6-fe787ec3c8bb | -9.57028 | -65.21954 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81e719f9-c38f-3df1-b2ce-6486ae342fb1 | -9.00655 | -65.92434 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0b3ee18a-5759-30af-b00b-6a76597d170b | -9.74683 | -67.70598 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 096004b7-dcee-3f92-893c-cd850ff6aae7 | -9.00253 | -65.92997 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8d4542c-9183-3f37-b5b0-4378a31c4d2a | -9.75134 | -67.10587 | 2025-10-22 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c430d363-139a-31cd-8181-a112bd1c80f7 | -9.01123 | -65.93128 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ca99a54a-8af7-34d5-97f0-b27235d351e6 | -9.11417 | -65.93549 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3440993-e365-34c5-8b0d-0bc2f4a8b4aa | -12.27466 | -63.87012 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5cba1f92-e493-3cf3-9fba-a600c884ef74 | -10.01146 | -67.8711 | 2025-10-22 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e955db0-ba3c-39ac-b3f6-5f26ea0ff18f | -9.10923 | -65.93913 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4ccbceb-942a-3c82-b456-964db16c5a37 | -9.73197 | -67.47337 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72428ac9-990e-33a8-8572-22d8dd10901a | -10.87001 | -69.21076 | 2025-10-22 06:08:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31cb0200-123e-36e3-a17f-97609e2abf59 | -10.08202 | -65.16682 | 2025-10-22 06:08:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6799e64-cad4-3985-91ee-8b96e43e8841 | -12.27424 | -63.8734 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9d04e00-5cdf-3312-a2b3-b9ec914d6991 | -9.89893 | -64.88565 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d7c87e1-9885-34b6-9449-239961e444d6 | -9.72255 | -67.48256 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d1e9d57-e3b5-3ae6-a29d-52ff615e6986 | -8.99845 | -65.91882 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5ffe6199-4476-39fd-b5ad-8995d53d7fbf | -12.13773 | -63.21444 | 2025-10-22 06:08:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32d60555-6aaf-353b-916d-eb673e2f9b83 | -10.01607 | -67.86673 | 2025-10-22 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69077c33-2f73-30de-ae51-5c5718988aa5 | -8.99932 | -65.92087 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 902096d6-da8c-3353-b408-86f4b67851f2 | -12.37627 | -63.86938 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e25b88ef-c9e3-38a7-be77-3a57b9c346d4 | -9.71858 | -67.48199 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7f6cedf-23ec-39b5-b143-88320e78235c | -9.01066 | -65.93551 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87f0f74d-6a3c-375f-bf77-0368cd4e113d | -12.13315 | -63.20645 | 2025-10-22 06:08:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 42479959-94bd-3cba-85e4-139e2c28417a | -8.99496 | -65.92021 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09b9d475-82de-3d61-8d5d-929718c664d0 | -8.98974 | -65.91753 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6999979-04c2-3835-88ca-4dffa2eab394 | -8.79002 | -66.72647 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7970fab2-66fa-3257-8983-152d21874cdf | -9.72726 | -67.47796 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 780a54b8-bd87-34a9-bcff-94199f4b8cd5 | -12.13358 | -63.20863 | 2025-10-22 06:08:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a816b064-1728-3d9b-9a7e-abfb630a32f2 | -9.00196 | -65.93421 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5541bf28-4e67-30d3-9f83-3127103794dc | -9.56567 | -65.2189 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 432d3e2d-5a62-378a-9d98-3c63018f842a | -10.48406 | -67.84773 | 2025-10-22 06:08:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e687e14-943a-34ab-8348-a9c775b71833 | -9.37939 | -64.49423 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a880cc23-7b56-39e7-b505-a05dcdf80438 | -9.64171 | -67.68379 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4abc2051-c789-3369-afbc-f789069b92ce | -9.01238 | -65.92282 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e2b33724-06a0-350d-a001-d7cfb2148749 | -9.58 | -67.41071 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 897713a2-f0d5-3274-a910-48c185c2e3c0 | -9.00574 | -65.93908 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6727bf6f-7c88-36a3-8fb4-930590489f99 | -9.00535 | -65.93276 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f01ba7d1-7116-3073-a86d-eb0bdcafdc1c | -9.09663 | -67.68495 | 2025-10-22 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5ba6ba79-0c69-334a-914e-20c4846be78a | -12.38163 | -63.86893 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82e0d34a-5e49-3b9d-80bb-d13c69eedbe4 | -9.79943 | -67.03086 | 2025-10-22 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b62a2061-3318-3d5d-a999-1b191cef20a1 | -8.97591 | -65.88946 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 090797b0-ba62-3d21-b550-25af7dcd7c01 | -9.00039 | -65.93635 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bca959e1-0b22-3c37-a4fa-f74dc9672ef8 | -9.10544 | -65.93431 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e94f6f9c-ae26-3f99-b356-983ea4f35ec7 | -9.0028 | -65.91947 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 67507f27-ee34-3ada-9e31-56f9ca17785b | -9.79995 | -67.02718 | 2025-10-22 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6bf6df84-b094-31f6-af9d-e345df7a6a3b | -10.59178 | -63.47702 | 2025-10-22 06:08:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9f193fd-c907-35de-a8b7-fe74c06ac1da | -9.01296 | -65.91859 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae7e3608-5f36-3614-8bd2-365179c0f648 | -8.87462 | -66.7806 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de29ce77-9e4c-320e-b409-3e6b15d4be94 | -9.71663 | -67.41015 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1fffd4f-f3b6-3110-97d6-6e1a34a67c2c | -12.38112 | -63.87336 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b6f3ec6-dc2d-3a7c-892b-39bf2fa91df9 | -9.78219 | -63.81296 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3c13d09-dceb-38de-9fd6-2f159835dfda | -9.90991 | -65.02198 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d3473aa-5b4d-392a-bc8a-1c8e84fb7cbd | -12.38124 | -63.87224 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6aea77a-a2c5-3691-b07b-d5727f82b099 | -9.11038 | -65.93067 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71cdc22f-e72d-3f77-b31c-34a110e2bf2c | -8.99215 | -65.90058 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 814752ac-c9a1-35d2-a81d-2f141f99149a | -10.26632 | -68.81052 | 2025-10-22 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffaa97c4-8891-3e22-8a1c-474745b503e8 | -12.13225 | -63.2137 | 2025-10-22 06:08:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 77103c95-6b0a-305c-8981-a4ef944a3bdf | -8.99409 | -65.91818 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4764cbe4-d075-3181-b648-1e3dee545b9d | -9.93352 | -68.21983 | 2025-10-22 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1065706-4e57-30e0-be6f-fd2e739e0c87 | -12.13818 | -63.21081 | 2025-10-22 06:08:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21d97631-2c12-3f43-b712-5693123e0e9c | -9.57489 | -65.22019 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ba001775-8a2f-3159-a8d6-46e0d23bc56e | -8.72557 | -69.66821 | 2025-10-22 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14bc67a2-c516-303a-a8d7-101cdc6fd625 | -12.37636 | -63.86824 | 2025-10-22 06:08:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 545f2e6b-a2d8-3b79-948e-d510ebdcfc35 | -9.93732 | -68.22042 | 2025-10-22 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2527f125-d423-31b0-8bf9-bfba81350087 | -10.72252 | -68.54512 | 2025-10-22 06:08:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62e9f318-799b-32be-911e-5d3f6e1fa9e4 | -8.99155 | -65.90481 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fd9e28e-a165-3d27-80b0-7a138a66d148 | -12.13316 | -63.21227 | 2025-10-22 06:08:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d7f81b55-c224-33bf-b83f-504b67ffecb6 | -9.00776 | -65.91589 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d1fce495-2c04-3751-90f3-d71e540f8e2a | -10.29779 | -68.00004 | 2025-10-22 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53c5bc9a-473c-3ff9-b470-9f9f7c35217c | -8.63544 | -66.76521 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18888086-fe96-3ef9-857e-5579f5621a72 | -9.84824 | -66.37801 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2eadb50-3b7a-3ef7-84ad-73c6e4ca121d | -9.7317 | -68.8868 | 2025-10-22 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b36fe90d-b784-3926-8991-2f25ae0b4dfa | -8.87803 | -66.77992 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93f7afcb-e2d8-349d-a1c9-d18e97152e03 | -9.71461 | -67.48141 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1822e2fe-c6ba-3c93-b179-0720c9c6db9a | -9.81127 | -67.59093 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82da0a1d-2eac-3280-b00c-f80a8482e400 | -9.62378 | -68.59939 | 2025-10-22 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c39bd59-588c-37a6-b7a7-abd269f93dc8 | -9.73123 | -67.47855 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 14f67b34-c9fa-3fa2-ba50-acf3a8ef6ef2 | -9.42611 | -69.00304 | 2025-10-22 06:08:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b1dad5e-5989-322a-83a2-cbefcf9e5fbc | -10.65349 | -69.07993 | 2025-10-22 06:08:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c6a41711-db19-315c-9b47-2a4e6f3206da | -9.00099 | -65.93212 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 44c01b52-84cc-3c8d-94e8-3f296801f9b1 | -8.88289 | -66.69434 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d5d1de00-418c-3ef9-a192-e729b55782f4 | -8.99274 | -65.89635 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2a7f245-afe1-3e08-84aa-0e63b605135a | -9.55079 | -66.6504 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1477e169-2bde-33a3-ba7f-428ea919011d | -9.01444 | -65.94036 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 28b6f93b-10af-3f89-9e0a-39e75c0c6635 | -9.11474 | -65.93128 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa2cbec7-3ee6-318c-b55f-567ffea41898 | -8.99785 | -65.92305 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b9b97f2f-d66e-33d3-9b58-f2d794d4098c | -9.71712 | -67.40666 | 2025-10-22 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23f3ccb6-8d62-301c-b375-0eb21e0862e2 | -9.00595 | -65.92854 | 2025-10-22 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 183c1cb5-9832-3ca6-94dd-942fa96759e1 | -9.97636 | -65.11581 | 2025-10-22 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README21.md)
