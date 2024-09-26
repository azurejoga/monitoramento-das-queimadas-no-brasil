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

## Dados Diários - Página 168

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62d37c8f-b2d5-3b94-9059-8b825dd04206 | -9.76462 | -57.78912 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3bd8c1d-b40c-3485-ac81-1f55b7bab5c3 | -9.76444 | -57.79342 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11a50315-b3e3-30ff-a1b8-c02d10195163 | -9.76396 | -57.79703 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e31d4ea1-e422-370d-947b-1d4e23b4995f | -9.76371 | -57.79633 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc8266f8-ddcb-3cc4-901c-db9474d240ab | -9.76133 | -57.77455 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d5ec0b7-16b4-39a0-863c-1547917cc440 | -9.76046 | -57.77742 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca067b5c-1e07-334c-aa25-e6b42a1ca6c2 | -9.76001 | -57.78103 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8cf0eb1-f9ed-3268-9ecc-9c15661fdab3 | -9.75988 | -57.78543 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42bb1b8e-56d7-38a0-b92b-483e8fd65c35 | -9.7594 | -57.78905 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b65f179-68b5-3bbb-a4f4-7557bed7e68d | -9.75892 | -57.79263 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aea58244-5b01-3463-9438-07f349109517 | -9.75864 | -57.79192 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff355752-d9ae-3762-a525-aa86a8cbb2af | -9.69775 | -58.08585 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0556b20a-907e-3b7a-8678-8ba75bbd2541 | -10.88091 | -57.46004 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32a4afb9-7b0e-32c0-a03c-fed531ddc38d | -9.69233 | -58.08511 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 35209b39-5fc8-3d18-8e2e-1b88cf742c3d | -10.86792 | -57.46013 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37b6529d-e292-396c-b038-32f71d89c4e8 | -10.8674 | -57.46416 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6d537ee3-191c-3eaf-b880-1e36bcea95a9 | -10.8664 | -57.47201 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0dd19ebb-f0ff-31c2-8012-83b5690ebced | -10.74648 | -57.54963 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf59e8d1-0f4f-3637-8eaa-af5d946ec478 | -10.74376 | -57.55173 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8e6875a3-1272-3405-98a5-4605321545e9 | -10.74074 | -57.54926 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c273074-f5a7-30ba-a7d4-4880b1ad0536 | -10.29648 | -57.62757 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41570628-1092-311e-806d-2a0566aa4d51 | -10.29084 | -57.62692 | 2024-09-26 05:48:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b308cce2-838c-3c81-8908-8e7a5fcb6c75 | -11.29166 | -57.52052 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40291d07-59eb-33c1-83a4-1feee33ab2a1 | -11.28695 | -57.52061 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bddc7b23-085a-37a4-b44f-c2d2fa66196e | -11.28591 | -57.51982 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b21d966b-6fe5-3699-8f6a-e8977e9e8bee | -11.2854 | -57.52383 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52984567-8462-30ca-ab70-f97c70d21b79 | -10.90257 | -57.42598 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31da2a95-f5f8-34f7-a828-bf10551fd3e8 | -10.89784 | -57.4169 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43f0a89f-1a58-3b95-a47f-56e7958ec4f0 | -10.8973 | -57.42132 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 080b213f-3461-3adf-8209-b0d7fb83b90c | -10.89208 | -57.41618 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5174b252-4079-3684-8a43-5bf88d6639c5 | -10.89154 | -57.42064 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e102ab8c-3360-364b-a874-118845f52701 | -10.88284 | -57.44419 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8568837-398a-3b5b-86f4-5dfe66574eec | -10.88186 | -57.45218 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dad210e4-5ced-3b0c-be31-4e0ffc9e915b | -10.88138 | -57.45614 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a864327-88e7-3614-ae24-f8e7caf61b42 | -10.87809 | -57.48315 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c59cf25-593b-316d-8e43-07e8f4a17e86 | -10.87367 | -57.46069 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93709fba-55b3-3ad8-97bf-f46f4c26f894 | -10.8723 | -57.48301 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 915a19f2-d17c-3176-aa64-562e92bf38bc | -10.87216 | -57.47246 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c43b4b5-d2c9-3f24-bd9c-9d074a4a298d | -10.87117 | -57.48018 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76bfd9c6-7edd-37f2-86a0-1bf71586d9d5 | -10.8694 | -57.4589 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3fdb0b4c-528a-3eba-b923-360a22f5db97 | -10.8689 | -57.46299 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 41b83b26-662e-3f83-83c1-3c4e08b8b48f | -10.86795 | -57.47084 | 2024-09-26 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6c1982f-9fe0-3dd3-82d0-21e9ffafce46 | -10.46927 | -59.13126 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47ed4040-dd38-31e4-96b9-ead356614549 | -10.46417 | -59.13057 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 885fe574-94ab-35f0-90fc-f6c0c9948d38 | -10.45873 | -59.13249 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66ee6128-f5d9-33ff-bea5-7b52dfcd9936 | -10.45836 | -59.13537 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a489bd74-6ad0-38fb-a032-5a73bfda3a58 | -10.39343 | -58.89094 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecb1c8ae-50e2-3399-8fcc-80c5e1cdd29c | -10.39302 | -58.89415 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fe8a5cf-6ceb-390f-8ba9-463449e9b395 | -10.39261 | -58.89734 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7542522-2726-331b-a66c-f7214eb7c824 | -10.38821 | -58.89053 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00b919f8-3e1c-305b-a3a5-1e642b855f48 | -10.3878 | -58.89375 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05cf4f6d-01d2-354d-aa3a-7c891b343184 | -10.3874 | -58.8969 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec80ec6e-8d55-38e0-9374-57211a57ad00 | -10.387 | -58.9 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a195d762-642c-317e-9d10-eaf282b572d9 | -10.38299 | -58.89021 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5259f063-f3e2-3bff-b582-6f5d5d0b1e83 | -10.38258 | -58.89339 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b70ccfaf-c9d7-3b06-a7a1-214aa00beb79 | -10.38139 | -58.90272 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5af4f84d-8632-362f-ad72-e3ccb63000da | -10.38099 | -58.90583 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 813110d7-0eb4-3a10-9fc6-29b5e8c73300 | -10.37657 | -58.89919 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ceb27507-dbca-30e6-a894-831f8df06904 | -10.37618 | -58.90229 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5bd6a91-4e0f-3c05-a119-8ed62a36cfdc | -10.37178 | -58.89549 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aabe1a7-2cad-3de0-b248-3f79dab0d7ec | -10.37138 | -58.89865 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c287b32a-f4f8-3ba5-a680-8fd14cfec974 | -10.37098 | -58.90176 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06748ff4-339e-3705-95bb-74de0e67b0d5 | -10.36476 | -58.89558 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1416b6e8-f724-320a-8f36-df6b95d736c4 | -10.36431 | -58.89896 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd99e261-8e93-3620-a905-e3984f47fe48 | -10.36117 | -58.89609 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bbac4859-e34d-331a-935c-df2107191789 | -10.36074 | -58.89951 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dff49a25-1e26-3a6c-b9f8-fa46238b25d4 | -10.36032 | -58.90285 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e29742f-fd3e-3239-8fbf-345314d5a740 | -10.35922 | -58.89763 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a73f35b3-a692-34e0-99f7-fc0fe94bb017 | -10.35835 | -58.90414 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 696fc0ca-5dd8-3ed8-a951-a2d9e7a5621e | -10.35152 | -58.91584 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 277169d5-305a-39a9-8977-54050645a567 | -10.35109 | -58.91908 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b1cc8d8-27c7-3212-8594-4ed304558ccd | -9.39125 | -59.63705 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40140ac6-206d-37cf-aeb5-006e91e01458 | -9.39052 | -59.63224 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c551c46b-8469-3cb2-befb-6eee0d48bfb2 | -9.3905 | -59.64245 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0bad6508-0126-36e0-83e2-edeb2134740a | -9.38982 | -59.63765 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 824e5175-46ae-3370-a1e0-ee61546bbec3 | -9.38911 | -59.64308 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| adc92e9b-95c4-3d2f-ba5d-d18634cb0227 | -10.05287 | -59.35484 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 58ec1f13-13d5-36a2-a2e8-e167796c135b | -10.05208 | -59.36074 | 2024-09-26 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07f387b3-1ad8-3a2a-9e72-a833f22408fa | -10.03343 | -58.81678 | 2024-09-26 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e67b4f26-61ad-3594-bf5d-9ba9274fe613 | -10.03302 | -58.81984 | 2024-09-26 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a7100b0-c312-3c7e-8dc6-90f2cd46db5c | -9.66727 | -58.42928 | 2024-09-26 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd7f95ad-1532-3055-9c6a-9664254f4e40 | -9.66685 | -58.43256 | 2024-09-26 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9abf02d-6612-3b6d-83b0-1e997e5192e0 | -9.66781 | -58.43256 | 2024-09-26 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b43d9b2c-09a8-3066-9d77-69e80a369493 | -9.66253 | -58.43184 | 2024-09-26 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52c4d668-c1c1-358c-8d69-3bbf9e029431 | -9.66209 | -58.4351 | 2024-09-26 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8226bfc2-82a4-3438-9fa7-902a37be9294 | -9.66156 | -58.43182 | 2024-09-26 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcdc7727-1212-3eb8-a009-5fb1e5c5c437 | -9.66115 | -58.43507 | 2024-09-26 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| afd10b67-8caa-38a1-85ac-8446b0401e4b | -9.66102 | -59.04361 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 633f6ac8-cf7d-35ff-99cb-fb2401a83e26 | -9.66063 | -59.04654 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bc813f9-9b76-3614-a0de-0cb4e356192e | -11.72643 | -59.29013 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a37e6371-c38e-3344-b046-d2e7cddcdbef | -11.72605 | -59.29314 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7132f902-87a0-39f9-a1cb-f76223da5974 | -11.72129 | -59.28951 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 251fb925-a6e2-3b88-b1d4-9a90291405a8 | -11.72091 | -59.2925 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a34a0465-c36a-32b0-9902-9f2301067330 | -11.65174 | -59.99919 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c7804e3-e39e-3ca0-858d-97a60e589523 | -11.65105 | -60.00454 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef4f9846-45a7-36b5-836a-c482049a400f | -11.27333 | -59.18653 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88fcb10c-f19d-3070-84ca-213fbdb219e8 | -11.26819 | -59.18587 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4e18591-301e-360e-9647-30ad2bf9d95a | -11.26345 | -59.18213 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba7c0962-10b4-3667-b115-6e0ab9239b9c | -11.26305 | -59.18516 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57207cb0-0c15-3c88-925f-ed95275fa718 | -9.26024 | -60.70747 | 2024-09-26 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README169.md)
