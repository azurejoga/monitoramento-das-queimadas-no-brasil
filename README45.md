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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c144e972-4e0d-3429-b4fd-13ec0ea309ab | -5.76946 | -45.07197 | 2026-09-10 06:37:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 9073c2c8-3325-3dcc-b8e0-927c99d3f0de | -5.75806 | -45.08814 | 2026-09-10 06:37:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 899a56b7-5a4d-374f-8b9a-7f02819eaa2e | -7.75214 | -49.20234 | 2026-09-10 06:37:00 | AQUA_M-M | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 4fee33fb-9def-3163-acd8-847e392446e9 | -2.94103 | -50.4616 | 2026-09-10 06:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 709db613-98a5-3f46-bcd7-39d33c64b99a | -4.3628 | -47.7709 | 2026-09-10 06:37:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fa01aa83-3fe6-3069-86a1-354a99b84e90 | -9.78839 | -47.04971 | 2026-09-10 06:37:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9ac6750b-63c8-395e-9ad7-929628e38596 | -5.76813 | -45.0807 | 2026-09-10 06:37:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| bfd156ca-42ed-33f4-81a4-9cbc53a65954 | -5.6094 | -44.8482 | 2026-09-10 06:37:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 562fc4d8-a8c8-3f65-95b3-b202bc53995b | -4.36021 | -47.77478 | 2026-09-10 06:37:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| a9be999c-38d0-39bf-8813-7cf29b8ffcae | -9.68378 | -43.47182 | 2026-09-10 06:37:00 | AQUA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d2842f7e-a6b8-3256-bb6d-0a6e4ced4c82 | -6.16045 | -44.63473 | 2026-09-10 06:37:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d12166b2-fc0f-39c6-8aa8-06b8d9325f26 | -6.15912 | -44.64356 | 2026-09-10 06:37:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 4bb1ee64-d8b6-3f7e-9645-aca7811c9f21 | -5.75938 | -45.0794 | 2026-09-10 06:37:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 92b9c590-a59b-3eaf-aa06-ab1de0179872 | -2.9342 | -50.47384 | 2026-09-10 06:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f8abcabe-b34b-30aa-9382-7c17769b546f | -6.71092 | -45.45863 | 2026-09-10 06:37:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 83c04e47-15cb-3992-9001-d25f62a4fe5a | -6.71225 | -45.44988 | 2026-09-10 06:37:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| f343dd3e-bec9-30b2-bc45-952c7a0eb1df | -9.33666 | -45.64586 | 2026-09-10 06:37:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7b03940a-429d-3cec-a08d-8cad0b82cc75 | -3.24371 | -47.24582 | 2026-09-10 06:37:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 8681a1fb-02e1-30b7-9bd7-b49784d1ba37 | -9.71486 | -43.39085 | 2026-09-10 06:37:00 | AQUA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 89378808-d21c-38fa-bee7-a1539afed12d | -2.93811 | -50.47993 | 2026-09-10 06:37:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 6875fdf7-11ed-36c5-9c00-b1664ccc7e77 | -9.68227 | -43.48226 | 2026-09-10 06:37:00 | AQUA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.4 |
| ef1beac1-d5cd-341f-95b1-63d2916f7451 | -6.16924 | -44.63604 | 2026-09-10 06:37:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f22735f0-b8b1-3b4d-a1df-d8733d8d1e55 | -4.85848 | -47.4053 | 2026-09-10 06:37:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 160dadb3-5033-3619-a602-76aaec078760 | -7.50627 | -45.26852 | 2026-09-10 06:37:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 81ae81da-afd7-3668-8b15-ec500c390c7f | -10.26251 | -45.20125 | 2026-09-10 06:37:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c5d82048-4b41-31e2-8bc3-79d453adde4f | -6.76081 | -44.57034 | 2026-09-10 06:37:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4d30e017-fa06-3f4f-bd9b-b9c2548e0a55 | -7.25492 | -45.35318 | 2026-09-10 06:37:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5261e884-187b-34a0-b9b2-245f7807fae6 | -5.76681 | -45.08944 | 2026-09-10 06:37:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 37bc5518-b769-3e52-9153-7898afebde21 | -12.8359 | -44.3422 | 2026-09-10 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| cb3a4cf7-46ce-3d76-8c33-c9054310ca13 | -12.8557 | -44.3154 | 2026-09-10 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| ec7f8840-860f-3b32-969f-eeef4eacd2e1 | -12.8363 | -44.3186 | 2026-09-10 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 5c15ad5a-0db1-3723-9c38-10dce56f2fdd | -12.8552 | -44.3389 | 2026-09-10 06:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 5a26ef74-3438-3939-bc17-7bf3f4d09ae0 | -12.82736 | -44.33138 | 2026-09-10 06:40:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 439a60b8-152e-3b68-9917-00e45388647d | -12.82588 | -44.34166 | 2026-09-10 06:40:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4db5d138-1c8a-3f35-a206-1eb71b20901c | -12.84117 | -44.34007 | 2026-09-10 06:40:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 81300e82-b2a2-3bc4-b948-f234f1d60cc5 | -12.64063 | -47.08625 | 2026-09-10 06:40:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7438ff4f-d855-3630-b724-c8c1d3a9ff52 | -15.08332 | -43.11826 | 2026-09-10 06:40:00 | AQUA_M-M | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 1d3eee81-35ed-3c09-a929-6e24cf05e65e | -12.852 | -44.33113 | 2026-09-10 06:40:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 6dec9e9b-02fd-376b-bbf7-eea516b517f5 | -13.44046 | -43.84301 | 2026-09-10 06:40:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 26.5 |
| c11c7e3e-e5f9-3e5c-a2fd-3906164512d1 | -10.42349 | -45.11674 | 2026-09-10 06:40:00 | AQUA_M-M | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7848e2ae-2441-37bb-9b1a-d245e6632ba4 | -12.84262 | -44.32977 | 2026-09-10 06:40:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 5a6b7fbc-4b1a-39d3-8620-eda9304acb19 | -12.83179 | -44.3387 | 2026-09-10 06:40:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 71bc7258-d3d7-384d-ad8d-48e343d555a4 | -13.47909 | -48.53822 | 2026-09-10 06:40:00 | AQUA_M-M | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 37dd0649-f8b0-37a1-9b8a-af5f3eb7875c | -14.91536 | -44.66481 | 2026-09-10 06:40:00 | AQUA_M-M | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f41b8bdd-4bd7-324f-acec-5f48c2662cd2 | -12.85055 | -44.34144 | 2026-09-10 06:40:00 | AQUA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b51cf0e2-44f4-3287-9455-a717fc896984 | -13.44202 | -43.83195 | 2026-09-10 06:40:00 | AQUA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6a592888-6d40-3a22-a5e2-8c17cb6d784d | -12.8552 | -44.3389 | 2026-09-10 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 144.9 |
| ac83c391-0643-3605-9198-1325a2d6b04c | -12.8359 | -44.3422 | 2026-09-10 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 150.1 |
| f95d653c-a489-3f39-b453-eb36da89dd44 | -12.8363 | -44.3186 | 2026-09-10 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 5642d4f7-0f83-3768-8e30-078cf0c67f07 | -6.5453 | -62.8914 | 2026-09-10 06:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 71d5f8dd-14c0-36d1-a80d-0b263da74d90 | -12.8557 | -44.3154 | 2026-09-10 06:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f4d373d9-2d2e-3448-aafc-e9dafc0a1750 | -8.88296 | -70.84035 | 2026-09-10 06:52:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b822168f-3c79-3d97-985c-6b17b9605a6a | -8.88057 | -70.84157 | 2026-09-10 06:52:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d83dd4de-ecfe-3c4b-977e-d6289b1d90aa | -12.8359 | -44.3422 | 2026-09-10 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 4d85ebd9-8070-3828-82bf-cfcc240dea56 | -12.8557 | -44.3154 | 2026-09-10 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 43743f87-92f4-3828-a83a-58efad30f5a7 | -12.8363 | -44.3186 | 2026-09-10 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 880bd015-88e0-32fb-a943-b53b05be1c8c | -12.8552 | -44.3389 | 2026-09-10 07:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| 5f96c2a3-e46e-366f-9bb4-6781d8f0cbb6 | -12.8557 | -44.3154 | 2026-09-10 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 63675215-0609-3090-81d9-4f195621e542 | -12.8363 | -44.3186 | 2026-09-10 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 545047d4-fdf6-3294-9225-627f645a8f5b | -12.8552 | -44.3389 | 2026-09-10 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 821c7e5a-32d9-31b9-bf5b-fa60c1d7f3d9 | -12.8359 | -44.3422 | 2026-09-10 07:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 2443306a-01dc-3eaf-a2ef-a4bb5c0d47bb | -12.8363 | -44.3186 | 2026-09-10 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 5a617b99-830d-3904-ba2a-95b00d621459 | -12.8552 | -44.3389 | 2026-09-10 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| fe217fe0-3de6-37f7-8a7d-58f1832bb73b | -12.8359 | -44.3422 | 2026-09-10 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 2463bdcc-7a74-3e56-a8b9-65dc416dbb02 | -12.8557 | -44.3154 | 2026-09-10 07:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 2aac0ad2-7d74-3cd8-a498-dd992bf2029d | -12.8363 | -44.3186 | 2026-09-10 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| f7148d48-88aa-3e66-8935-130dfe0be8a9 | -12.8557 | -44.3154 | 2026-09-10 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 8eae144c-49e2-3470-a329-b21bf83a2475 | -12.8359 | -44.3422 | 2026-09-10 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 542d0923-c1ff-38bb-b21d-7744ad57cee4 | -12.8552 | -44.3389 | 2026-09-10 07:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 7ff77392-3163-3f69-8c1c-5aa2923bc2c5 | -4.8676 | -56.0039 | 2026-09-10 07:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 30.6 |
| 5a7e4ec6-1065-3b09-bc51-3fc97c34a5a0 | -10.0887 | -46.2493 | 2026-09-10 07:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| ae99753b-efbf-3577-9fd5-9d34622a1c88 | -4.8676 | -56.0039 | 2026-09-10 07:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 60907955-bf64-3c8f-8903-4098dab35f37 | -12.8552 | -44.3389 | 2026-09-10 07:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| dc3742e6-1738-3b12-a873-278c23bb0176 | -10.0697 | -46.2516 | 2026-09-10 07:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 8b3d7aee-71c8-3806-a57d-c3ce1f293b5d | -12.8552 | -44.3389 | 2026-09-10 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 2cb05cac-4326-3f1e-89a3-e63bc54a9d69 | -12.8557 | -44.3154 | 2026-09-10 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| af980f49-a944-3ab9-9c8c-4cab709b9963 | -12.8363 | -44.3186 | 2026-09-10 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ce26c1a8-cbec-30b2-a613-3a71b19d1a81 | -12.8359 | -44.3422 | 2026-09-10 07:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 8a8e4077-9c27-3287-abfd-ebfa5af0b583 | -12.8359 | -44.3422 | 2026-09-10 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 8527b909-372a-354b-823b-c47039a901e1 | -12.8552 | -44.3389 | 2026-09-10 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| bcae2708-160d-3713-8e19-eace70b25337 | -12.8363 | -44.3186 | 2026-09-10 08:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 6f4d71b6-cb20-3b25-9b0e-05e1de768a9c | -12.8363 | -44.3186 | 2026-09-10 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 70.5 |
| e328677c-e65a-35ca-b9ac-b8adc3681e97 | -12.8557 | -44.3154 | 2026-09-10 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 24bd9ebe-7aa0-310e-8b88-5c2346b0b958 | -12.8359 | -44.3422 | 2026-09-10 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.4 |
| f4fa0912-9d8d-3be1-8943-43c39194a146 | -12.8552 | -44.3389 | 2026-09-10 08:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 61fb0f9c-c08e-3bb5-be64-5028b8c83bda | -4.8676 | -56.0039 | 2026-09-10 08:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 19544a22-2c19-35c8-bd90-1fd53034d513 | -6.55196 | -62.89932 | 2026-09-10 08:16:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 79cd9bcf-fceb-39e5-b4ff-b395ff1213a7 | -6.55498 | -62.87694 | 2026-09-10 08:16:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 041995f6-ccc6-388c-a8e7-7939d21663a0 | -6.54298 | -62.89268 | 2026-09-10 08:16:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 0bb90395-7f53-36ca-838c-909c3470bd28 | -9.00012 | -65.4023 | 2026-09-10 08:18:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b93153ef-c8b9-3cb9-95dc-231c27b99e2f | -9.0432 | -65.41528 | 2026-09-10 08:18:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e381118f-c1b8-3a4b-8069-b80220b4dfca | -12.8552 | -44.3389 | 2026-09-10 09:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 4d129106-2d55-3e54-b76a-cd827f14781c | -12.8359 | -44.3422 | 2026-09-10 09:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 0d9d6098-83ee-356c-a62c-474e822f0383 | -12.8359 | -44.3422 | 2026-09-10 10:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 6c808704-aff1-3ee9-9d1a-9a8210933097 | -12.8359 | -44.3422 | 2026-09-10 10:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 29c36e46-c434-38d6-86c8-9f9ba8a95048 | -12.8359 | -44.3422 | 2026-09-10 10:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 405993ac-55a1-3b44-800e-311f6617d788 | -10.6812 | -45.995 | 2026-09-10 10:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 70530b73-3c54-3c32-9bbb-ee34e1c8df83 | -12.8552 | -44.3389 | 2026-09-10 10:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| dcb4f41e-c1ba-3453-9bf5-c14c24b8958c | -12.8359 | -44.3422 | 2026-09-10 10:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| fd863194-81bb-331b-97bd-9c5142f50339 | -12.8359 | -44.3422 | 2026-09-10 10:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 143.7 |


[Clique aqui para ver as próximas entradas](README46.md)
