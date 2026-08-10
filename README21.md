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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a0b0de5-3cf3-3939-9df4-ea72b2f2ca2a | -8.97148 | -60.53918 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aff84b0-46c6-3958-97d5-d8645e54a8d8 | -7.69714 | -55.16615 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b45576c-f09d-3f7a-bcd3-86b76eeaf01a | -6.85289 | -56.40503 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a3c6aa38-aaad-3488-ab46-99849d4c6529 | -7.69071 | -55.16949 | 2026-08-10 05:48:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9fb31992-07b5-370f-a40f-3bf70e3be296 | -6.13639 | -57.70675 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aba76641-6c72-3d85-9a75-d62f252aabdb | -6.84569 | -56.40065 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 79f5113d-117a-3983-9230-0eefe3a03259 | -6.83443 | -56.41963 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e6e1ac1-39d4-32a2-8601-abdec8b8b505 | -6.83991 | -56.40305 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3890d145-a56a-334f-95e3-e5ae52998e35 | -8.9422 | -60.52351 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 938bffae-bf9c-3471-80df-e2e04e71ecab | -8.94941 | -60.53234 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f95ddb20-45ee-3a63-902a-ee970e566a27 | -10.93781 | -57.11732 | 2026-08-10 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57bef89b-6835-3994-8239-9dc6636ffc41 | -8.6336 | -66.53391 | 2026-08-10 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22547f3c-ba26-3364-9c38-af0d6e50083c | -6.14043 | -57.71283 | 2026-08-10 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4bf1700e-62b2-372e-b118-09302b3b9782 | -8.63748 | -66.53094 | 2026-08-10 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 091b7cac-b272-3ef4-9f15-74b755d75ec7 | -8.95784 | -60.5759 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f97b1ee2-66fd-369d-8c38-e380353be807 | -9.37354 | -57.36274 | 2026-08-10 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a39bfc22-65bd-33b3-88d6-bbd4301e43b0 | -8.89353 | -60.56668 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e19da39b-66cc-3845-9eb3-c0b084d8fb84 | -6.81021 | -56.43676 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98763fa7-cb30-39f8-a31a-1b536bb131c5 | -10.90986 | -56.36998 | 2026-08-10 05:48:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0185412e-52a1-3ee7-a522-6eafbe3c3ba7 | -9.7216 | -60.20455 | 2026-08-10 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2ba9d3b-32f1-34f5-830d-b9de8c400f3e | -10.24425 | -63.27287 | 2026-08-10 05:48:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 824856ad-0095-3948-acb9-1be86765ce30 | -7.15166 | -59.62283 | 2026-08-10 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4017c8ef-bbd6-3ea4-ade5-8b768be338e9 | -8.95662 | -60.54111 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d6445bec-7338-3830-8e4c-de0e139fa318 | -8.89136 | -60.58185 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c3e3679-3f03-3074-8ff5-a20de4b7302e | -8.97979 | -60.54046 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3dc12d70-ec0e-356c-95b6-4b4d4cea8f33 | -8.89659 | -60.57488 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a5b046ba-b569-3958-b490-8225c869c934 | -9.04894 | -60.3848 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fea88987-e551-30fb-9e8b-774fcbd4ac62 | -5.69 | -60.23145 | 2026-08-10 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30b87b20-5784-37f4-8b3b-5c86550c7946 | -7.66218 | -62.55043 | 2026-08-10 05:48:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37706424-6175-388e-9c63-87f4c35f6a7f | -8.94164 | -60.52733 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3ebecec-0138-37ab-8d56-b02cbd5c0f21 | -6.84611 | -56.41428 | 2026-08-10 05:48:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| caa0da47-b9b5-3dd2-9fae-14e96f0b3e90 | -8.94108 | -60.53115 | 2026-08-10 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ea7838e-2097-39b7-b702-39c757826669 | -8.9039 | -60.5769 | 2026-08-10 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| c333b132-1a18-3791-9e7c-aceb9733fc03 | -14.13817 | -54.02429 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| be6bac55-fad3-3105-8470-9cb058699a5e | -14.13024 | -54.02308 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7982d772-47dd-3511-87db-41e71b0bcc39 | -15.96945 | -54.22293 | 2026-08-10 05:50:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4456ca7d-6971-3a91-880d-919a6577dc3c | -14.31483 | -54.92741 | 2026-08-10 05:50:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3083f103-ef49-3e31-a011-e92355430302 | -14.13195 | -54.01744 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d585475a-7985-321d-bba1-6f06cc8d2882 | -13.86732 | -53.66419 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a23057b8-7fb4-335b-b29c-0c2843007ed3 | -13.85005 | -53.69619 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4287733b-03f9-3856-8ace-70fa13b534ac | -11.81705 | -63.04063 | 2026-08-10 05:50:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b5d3ccc-1c3d-3de0-b0b4-f7ed1e701512 | -14.13877 | -54.01835 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3627a80-8a8a-3f97-838f-5b7dc8c8db5b | -14.1377 | -54.01797 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 98504da4-2e1a-3915-9eb7-39fddb15e3dd | -11.83886 | -56.94843 | 2026-08-10 05:50:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e3cb4077-4c30-3bc7-8062-8faec480e253 | -13.85041 | -53.69488 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b59d4e0-93f4-3f28-b382-55af4943c571 | -13.86039 | -53.66314 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 450eac59-8b73-3253-ab67-776622aa9989 | -13.84419 | -53.89163 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d37ff9d4-5992-3f46-8ebf-741e2407fe6c | -13.86098 | -53.66176 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b9c62b45-a4d0-3093-a19f-1e371fd985e7 | -14.13836 | -54.01182 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ed3f03b0-092b-37de-a913-c410692258bf | -14.13706 | -54.02391 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 198c706b-62e2-381b-a0a8-79de214ecd97 | -13.86791 | -53.66277 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c55742cd-0df8-3e67-9dbd-0ce64769767b | -14.13939 | -54.01217 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e773b03-cad6-3911-ad89-330d5136beb2 | -13.84289 | -53.69959 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 486e8315-d6d1-3b50-82fa-f63bffdcc957 | -14.13088 | -54.01708 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5e22a5b3-12b5-33c5-a044-e74ecdacc2f7 | -11.81771 | -63.03615 | 2026-08-10 05:50:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35b974bb-bbea-301c-acb0-b90379e26d99 | -11.84439 | -56.94924 | 2026-08-10 05:50:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39729246-72db-3c96-9187-15a76d2d9e6b | -14.13135 | -54.02343 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b134686c-b87c-3043-90a9-23afa57c505c | -13.84256 | -53.70088 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b375c594-faa3-3d63-a3ff-1fc209a8d737 | -14.13258 | -54.01118 | 2026-08-10 05:50:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e4baccab-ac35-36fa-8f53-c96b9a937dbe | -8.9039 | -60.5769 | 2026-08-10 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 1b5716e4-855b-3fef-ae55-177098dcd3b4 | -2.36171 | -67.21353 | 2026-08-10 06:31:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5fbea112-38f6-3b65-9ce2-e6b8339eaf99 | -2.3635 | -67.2177 | 2026-08-10 06:31:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13db6996-0b9b-30b8-b666-6ea4353b7726 | -2.36408 | -67.21391 | 2026-08-10 06:31:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e25e1242-6d94-3c9a-b22a-7219aea51a46 | -2.36117 | -67.21733 | 2026-08-10 06:31:00 | NOAA-21 | TONANTINS | AMAZONAS | Brasil | 1304237 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57033e05-b7c5-338f-b006-eaa8a30c544d | -6.96105 | -71.66974 | 2026-08-10 06:33:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 92236cbe-5450-3954-aa50-8999b90fe642 | -4.44684 | -47.91851 | 2026-08-10 06:37:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 4b1bdd58-e0a1-3dff-b167-6b7a0095476c | -7.61293 | -42.75832 | 2026-08-10 06:37:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a2178c0f-b208-3cc6-a2ef-ab9f6035911c | -4.45596 | -47.91988 | 2026-08-10 06:37:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2dd5ae78-c744-36ab-8ed3-7e6423d66535 | -4.45743 | -47.91035 | 2026-08-10 06:37:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 755eea9e-421e-35a9-81b7-65b86ad32543 | -4.44831 | -47.90897 | 2026-08-10 06:37:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| e206769f-d89e-342d-8876-13be4c86319e | -15.38323 | -53.76353 | 2026-08-10 06:40:00 | AQUA_M-M | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 37.1 |
| bc542c6f-2f30-335d-bcdf-8bc6f739bc93 | -11.6239 | -51.09286 | 2026-08-10 06:40:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a63ccbc6-671a-3595-8e6e-370cd0c67811 | -7.23496 | -49.86985 | 2026-08-10 06:40:00 | AQUA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 40860f6f-4756-34e7-ad6d-6d83e9f47caf | -11.47221 | -50.55959 | 2026-08-10 06:40:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| cbec5a34-d062-317e-a695-2a619cf11cbc | -15.08283 | -52.68682 | 2026-08-10 06:40:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 515b931f-02c9-386a-8fbb-0a2045b80162 | -11.46253 | -50.55799 | 2026-08-10 06:40:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 9298d752-d585-3c43-b194-a95122384852 | -11.47396 | -50.54861 | 2026-08-10 06:40:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3fbf8eaf-86fb-34df-8c72-78818068bb28 | -8.28374 | -46.4184 | 2026-08-10 06:40:00 | AQUA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6c604d6b-320d-3f09-a7e9-50c908b169b4 | -11.04319 | -44.27774 | 2026-08-10 06:40:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 663d801b-c438-3de5-b353-f85c12f90940 | -17.01087 | -51.29196 | 2026-08-10 06:40:00 | AQUA_M-M | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 648e93ea-f83f-39ee-8296-862937837865 | -8.28506 | -46.40951 | 2026-08-10 06:40:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ab1c6310-af09-30c2-9790-98a1817c5f0b | -15.14747 | -52.71862 | 2026-08-10 06:40:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6b55979c-a6ed-346c-aace-cc20fd309714 | -14.12594 | -54.01283 | 2026-08-10 06:40:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 49a6cfbe-962b-3440-bde1-e6130f0a5029 | -13.6324 | -46.21951 | 2026-08-10 06:40:00 | AQUA_M-M | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bf66462c-fefc-3666-a14a-95c6a4e45797 | -8.29385 | -46.41084 | 2026-08-10 06:40:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 615112fa-a9ca-3b0e-aa1e-845479671620 | -16.0619 | -50.79651 | 2026-08-10 06:40:00 | AQUA_M-M | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 503a23e9-ef3d-3b75-928a-8a608917efa7 | -8.31275 | -46.40464 | 2026-08-10 06:40:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2c316f94-ce60-3de9-aecc-3775b58f8738 | -15.03983 | -46.56626 | 2026-08-10 06:40:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 84afbe63-a4ff-329a-9729-cebe734fca97 | -8.30263 | -46.41217 | 2026-08-10 06:40:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7e718e22-68da-3489-9594-4606c46630f6 | -15.03841 | -46.57613 | 2026-08-10 06:40:00 | AQUA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 54128119-b61b-3dcc-8e85-53242ce70bc8 | -15.03216 | -46.55451 | 2026-08-10 06:40:00 | AQUA_M-M | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5a21e3aa-bb61-32e8-8432-7954696ce3fc | -15.039 | -46.5581 | 2026-08-10 07:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 545cb4b7-7e4a-3aac-a34c-a61d208086fc | -15.0385 | -46.5811 | 2026-08-10 07:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 8788e6c7-2138-381b-ac6a-7e76c45de2d1 | -15.039 | -46.5581 | 2026-08-10 07:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| af1ff31c-84c2-3c9b-a354-fe4138ab53c0 | -14.2872 | -45.3069 | 2026-08-10 11:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 8c0251f6-a4dd-3f83-9dba-e107f67c5ada | -8.55385 | -45.35785 | 2026-08-10 11:36:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 204c3cd0-cdb3-3e40-96b1-a62947ef02b8 | -7.61905 | -42.77213 | 2026-08-10 11:36:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 46.1 |
| e165c3af-b91e-330a-b46c-ece165eb3d8a | -7.62036 | -42.76255 | 2026-08-10 11:36:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| bce85cb9-d59c-3f8a-abff-a7e5fa9306b5 | -8.07997 | -44.35078 | 2026-08-10 11:36:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 505127a0-3600-3b7a-9658-7e27e33a5fd0 | -7.6108 | -42.7744 | 2026-08-10 11:36:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |


[Clique aqui para ver as próximas entradas](README22.md)
