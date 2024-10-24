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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc21e7f9-23b5-33a0-a45a-61afb7e45372 | -17.02922 | -57.51139 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 9899afd4-b49f-307e-8832-67ed72c29943 | -17.02708 | -57.49549 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a5c33ff5-29ed-303b-a238-986f36f5879c | -17.02691 | -57.46418 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 51ec363c-e0e2-3d04-9438-2fad7c706c33 | -17.02659 | -57.49932 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| dd4c98c7-9bcc-3df6-a83b-2f6d1a7e9b91 | -17.02585 | -57.37337 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ea9d3d09-0c57-3fdc-bee4-f095f6ce006f | -17.02561 | -57.50699 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| c6b5df8c-3547-35f4-91b8-84144f96fcb2 | -17.02543 | -57.47571 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d7130278-ca00-3e9f-be72-3b390e5b66a3 | -17.02462 | -57.51463 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| bb501688-584e-3db7-89e4-338300a7adca | -17.02413 | -57.51844 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| eeb8853e-3aff-323d-a42d-1f1bf73f66d9 | -17.02248 | -57.49874 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 27d00c24-d00f-3af4-a753-fad32d054393 | -17.02229 | -57.46745 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 5251b14d-bc8b-3e00-8a91-cde38f0382d5 | -17.0218 | -57.4713 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 39720969-3fe7-3fa2-a04b-f6e3cb117b1c | -17.021 | -57.51023 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| cf55d988-7127-3a9a-9616-f6c3f3413adc | -17.01983 | -57.48667 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8115e0f0-6433-3836-92cc-7f92bdff15a3 | -17.01953 | -57.52168 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| a6107908-8f75-3fbc-afd5-0e83747e8123 | -18.06278 | -57.26189 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9543fa1a-9a64-30b2-9526-e2f8e660b968 | -18.06226 | -57.266 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f4c5efd8-816e-3eca-8705-e5e90490157a | -18.05802 | -57.26542 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 18da6d8f-03a5-3e54-8799-bb86d1dd8bd6 | -17.95598 | -57.22359 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 45e9e57a-1df4-3106-b2e3-bf21db9643cc | -17.95546 | -57.22771 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 3a831392-32f4-312e-8230-cbaa4c3c7a2a | -17.95174 | -57.22301 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 40d199b3-516b-3e51-87f9-99d3946f5dea | -17.94057 | -57.20892 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 22d0335c-ce77-30b3-95f5-1e03e26933cc | -17.93746 | -57.23358 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8bb5fa30-6ce3-3576-9d94-06cd523bbdc0 | -17.93632 | -57.20833 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 1252564f-eae1-3952-b311-5476a76ff804 | -17.93528 | -57.21657 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| c2d9fe77-72de-3e08-8f15-5809263042dd | -17.93477 | -57.22068 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4023fd82-4669-3f6a-9d32-e79c45b67d03 | -17.93425 | -57.22479 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 07ee997e-a140-3b99-85af-934e28bcc47c | -17.93373 | -57.2289 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 638ef533-c416-3e77-9a8b-c71e4a47ac87 | -17.92474 | -57.23184 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6facd0d5-8464-392d-b73e-c8ad66b002ff | -17.93322 | -57.233 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 824791d9-d007-3400-b5ed-45bdfbc08869 | -17.9327 | -57.23711 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| a2976236-5a7e-3ddc-b44b-605caef51ea5 | -17.92423 | -57.23595 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 95b8da1f-e5e0-398d-9efd-3d9b91aaea53 | -17.92269 | -57.24824 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 41014a80-4a27-3686-a700-95c3f94cfb7a | -17.9205 | -57.23126 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f8f2bbbc-bbf0-33ce-aa52-d8cdf35f27f2 | -17.91999 | -57.23536 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f1e32d2c-6367-3467-aff3-6434205e05a7 | -17.31203 | -57.28209 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 8ca9e0f7-792c-3433-9e9b-e7d22d3a50fa | -17.28423 | -57.26607 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b3f40c06-c700-3b30-b4ee-c7f044c4c52c | -17.28004 | -57.26549 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 40d74382-77ce-3200-9562-74fdb975c733 | -17.27953 | -57.26948 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 45a7a2f8-0eef-3f84-97da-9e399253e469 | -17.27534 | -57.2689 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ab44f0e8-db0c-3104-b032-4ab7673a43ad | -17.27129 | -57.30075 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9e7f75e5-686b-3faa-8fba-16bceeab847d | -17.26963 | -57.28028 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 888d62c1-0dc9-30b6-875b-c712ec43d15b | -17.2631 | -57.23056 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 2de7cdba-eb36-3b3f-9a96-8805a03bb7a7 | -17.2626 | -57.23458 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 43dee4c6-730d-3fa7-8c39-1e3077e2ce9c | -17.26242 | -57.30356 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3b8ea78b-dc3f-3df4-bd31-62a849011eed | -17.26209 | -57.23858 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 8b3b2c2c-9011-35d7-83fc-d3f3bc81581c | -17.26192 | -57.30753 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5c68e7e2-6b88-3681-9777-cb29ef382be3 | -17.25824 | -57.30298 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2aa5cb6a-d874-39c3-8fdf-de3621d5140b | -17.25589 | -57.25401 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 79e75ae8-0c95-3154-b1c0-76534f5f9d52 | -17.25169 | -57.25343 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 76220dd0-0133-3db4-afb2-c783181f2a78 | -17.2475 | -57.25285 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 13eb7715-7888-3673-824f-43e62c18486e | -17.2448 | -57.24026 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 0f9f4884-48a2-3fee-8395-4e07dc9a7193 | -17.2406 | -57.23968 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.5 |
| 28ca0419-87a9-30c4-99df-73ce5ce66bc3 | -17.2401 | -57.24368 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| a20b8143-9c6b-3984-95a4-a3c1a563ff44 | -17.23613 | -57.27562 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bdcd2cf9-89e8-3392-94b3-36c88ea0a2d7 | -17.2359 | -57.2431 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3e28005b-79ad-3d7b-9d60-49b9e129a471 | -17.23536 | -57.27309 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f1721b16-4841-325b-8b86-39b36a72d172 | -17.23507 | -57.51846 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 0c7ffa98-5753-3c66-93e6-e7bce307b57d | -17.23491 | -57.2511 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 97c4d13c-86a8-3e01-8c33-f17ece249d53 | -17.23431 | -57.24862 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 53e51304-d7e9-3da5-beec-eb6a570682dd | -17.23144 | -57.51402 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| a061791b-6b11-3250-92b0-2d1bb8e831bf | -17.23095 | -57.51788 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 41fb685c-f648-311d-ac2a-91a033c0ebbd | -17.22959 | -57.25203 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 91c80761-b7ed-3c03-a2c9-45a9ddbb58c3 | -17.2254 | -57.25145 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2e84f2aa-1f43-3652-a25e-2bb67f40a9fa | -17.22488 | -57.25543 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2ce405b2-3bb8-38c7-a0d5-6df5919d975b | -17.22418 | -57.50517 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fe55eb40-8fcf-36f3-aa17-f97b207071b1 | -17.22222 | -57.52058 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 01b81e4b-994d-3a83-af6a-2faa6f72d674 | -17.22103 | -57.49688 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3ce0a02c-86fc-3703-87bc-8a2b7c3b0edf | -17.22054 | -57.50073 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 640bb327-a80d-308a-b7fe-beb56ff943a6 | -17.21915 | -57.29914 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 95a3fb3e-6ab5-3cf0-864a-b7c16cebb717 | -17.2181 | -57.52 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| d1cbe1f6-d3b5-3667-b6ac-55edc760bb4f | -17.21761 | -57.52385 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 4a2c1eb7-8a16-3736-94d0-786b2fad3470 | -17.2169 | -57.4963 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 660ee4fb-bc3c-32ad-9ece-07c3fd83f76a | -17.21326 | -57.49186 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 5e979b4d-5458-33df-b9fd-0d2153bc2625 | -17.21277 | -57.49572 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c67c5a59-9411-342e-a9d0-859c09ed5c7d | -17.20986 | -57.51885 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d36f7fb8-c4f5-33d9-807c-3375e59af343 | -17.20865 | -57.49514 | 2024-10-24 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 285a6ce5-33d1-3ea1-8614-9099722d7a7a | -17.9992 | -57.25316 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cb61fdc7-b69f-38d9-a34a-2d611d2441d6 | -17.95866 | -57.2365 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 3c625a43-9271-3a73-9b45-41c98a1d6377 | -17.91948 | -57.23946 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| e66cae12-5284-3fef-bccc-d90787502ad8 | -17.82834 | -57.57701 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| f90938dc-5597-3f2a-b6d2-c12bf090b1b2 | -18.03551 | -57.3412 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 7964ff93-9e08-3efc-8d5d-94fbb965bade | -17.92847 | -57.23653 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c9d09154-e8aa-303e-a073-b7d2f7e26a00 | -17.9232 | -57.24414 | 2024-10-24 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.7 |
| 309ba2be-f031-33b0-a6ca-ee99bfaf3ded | -17.79079 | -57.50812 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9b7081b6-dc30-388d-b82a-5c66db289e00 | -17.7893 | -57.51991 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 80e59fb0-1263-3425-b2c2-362c1c8f97a4 | -17.78645 | -57.57516 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 8c9752dd-0075-3992-b390-e56a3404fd15 | -17.78514 | -57.51933 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ef078400-5392-3524-8c92-c6f1a441cba6 | -17.78464 | -57.52324 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 5aad395d-c070-335e-b669-032b743f7e5a | -17.78132 | -57.58236 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c276efcb-dac3-369d-bec8-64cfef53aa68 | -17.77999 | -57.52657 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| a360f002-9676-3ae0-b002-b635c02efbd5 | -17.77718 | -57.58179 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 650156b2-06a3-3834-8acf-c24f47519389 | -17.77701 | -57.55004 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a651455b-8f3c-39d1-ba15-eab2bbd60b13 | -17.77669 | -57.58567 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 716bfc85-44cd-3900-b38a-e6ae148e91fd | -17.77566 | -57.49402 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 9d8ee03a-821d-37a0-a002-3c3eb0cf229e | -17.77516 | -57.49795 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2ac963ca-f702-3efd-8749-1f30f02ee9ca | -17.77255 | -57.58509 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.2 |
| 28cdb402-f3eb-362a-b31d-17d9172b26c8 | -17.77249 | -57.48557 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| afaf1d02-18a6-33a7-aff0-94f33fd25d2c | -17.76734 | -57.49286 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 83afd506-066e-36df-b296-423f61d36cde | -17.76428 | -57.58394 | 2024-10-24 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |


[Clique aqui para ver as próximas entradas](README105.md)
