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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f172f2dc-007b-3eb6-b00c-91a59ec78d7d | -10.8046 | -44.2553 | 2025-06-30 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 93.3 |
| bbc5578b-9ecf-33df-b05b-52022f5add1f | -10.805 | -44.2319 | 2025-06-30 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 134.2 |
| c941819a-e198-367a-acfb-f4e4b854b121 | 2.75094 | -60.36798 | 2025-06-30 05:27:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44d9b045-d7db-3cc3-beef-936c1da10507 | -4.32042 | -48.07123 | 2025-06-30 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1356aed-9c80-327f-a37b-93c37b21e25d | -4.31933 | -48.07893 | 2025-06-30 05:29:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 729221c5-61ce-324c-a386-f4dc00f86341 | -2.95547 | -60.01665 | 2025-06-30 05:29:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73395f42-3e8b-31ac-a937-57ad60f617ac | -10.8046 | -44.2553 | 2025-06-30 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 8ac8ba67-94c2-3ae2-8013-9766ec918203 | -10.805 | -44.2319 | 2025-06-30 05:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 186.9 |
| c48a744d-4814-3a6f-94cf-128b59a2067c | -9.22868 | -58.74255 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1eff5621-d4d9-3ab6-8a4e-baf5931cee85 | -10.85101 | -53.74231 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc1d9ae9-3712-3ff8-82a5-26481ba06fe0 | -9.25685 | -58.75343 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3674dc0d-5604-3c8b-aa24-4a0eca479422 | -9.71209 | -56.18376 | 2025-06-30 05:31:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54a69e64-e1e7-374f-b50a-bf819c10012b | -12.60805 | -57.87723 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5871808b-c29a-36c2-bd48-4ba24d0be1a3 | -9.35847 | -58.85185 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 91104cc1-bc38-324f-909b-36ee5fa8c8f1 | -10.12643 | -57.77404 | 2025-06-30 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b53f7a64-fb7e-35b4-8e18-ef6c47973247 | -12.10645 | -54.66454 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 78836bda-6bf5-3094-8620-90be98a295fa | -10.87464 | -53.77371 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2676e080-4731-375d-ba7b-05ec14f1d12c | -11.20797 | -55.92355 | 2025-06-30 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0e305a80-ec49-3678-a203-24287583baff | -10.85056 | -53.74589 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cfc0d4e7-36c0-30d9-8b11-7d104033cbdf | -10.12999 | -57.77832 | 2025-06-30 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e196284c-a790-3ae9-b332-f804d96006a8 | -12.63028 | -54.21809 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6cc17cdf-9856-3588-9ac1-87872278f597 | -10.85419 | -53.76084 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 046156e9-3de6-3108-bb07-a9f1172a5d6a | -10.04208 | -59.35647 | 2025-06-30 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f36dfba-74f0-3f1f-bebc-904d29d8cf87 | -12.10086 | -54.66698 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96ec5ae2-393c-3f90-a297-bdb102ed83e1 | -11.19922 | -55.9171 | 2025-06-30 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99c50086-e7d2-3a02-b148-4f4bd7a084a2 | -10.29817 | -57.04365 | 2025-06-30 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89ec11ce-dcf6-354b-91f6-78a61e95c919 | -13.14158 | -56.8095 | 2025-06-30 05:31:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2d736203-e279-3a12-99b1-67cf886c1b31 | -13.08244 | -54.85001 | 2025-06-30 05:31:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 778f151d-438b-39e8-a2f1-f598bd27c6a4 | -12.62817 | -54.23502 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6cd0497-8ace-3908-86a6-1732dcba648c | -12.61308 | -57.87438 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81d4e186-e876-3b1c-a348-26353a5aa085 | -9.2477 | -58.74541 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6c7f28ef-a131-36cc-81e3-b9cb709f8001 | -12.61991 | -54.21321 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 0309839a-c90f-3df3-9a2f-d3647a5297b0 | -9.17148 | -61.40455 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ed6ee53-fd45-309e-868b-f8439de1d596 | -9.23698 | -58.73903 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea30d42a-0192-3a58-90d1-745b61ea00a8 | -9.2356 | -58.74836 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20f79b4b-90d7-3d45-a217-d4da72c20602 | -9.25323 | -58.76055 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 965b3c37-d067-3797-9af1-852d102ca068 | -9.09096 | -59.49473 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f0a67363-a071-3139-946f-56c4555e23e5 | -10.04141 | -59.36091 | 2025-06-30 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26c57bd1-f3be-3686-8524-8c6808b9864c | -9.25253 | -58.7652 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4277976b-2f49-38a3-8baa-793124b767e2 | -9.11334 | -59.04909 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 934733cc-ab42-37bd-968a-2c697a014e86 | -12.10567 | -54.67083 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1323857a-fcf1-300f-a87b-4606ffe57a6a | -9.04223 | -61.22851 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c817616-7787-33c9-9b4e-4892d6cee851 | -10.8033 | -55.85939 | 2025-06-30 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98266cf1-5f98-35a8-8efb-7135a87b92e1 | -13.08764 | -54.8508 | 2025-06-30 05:31:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8e46bf8e-c261-3775-b0d4-60ac0c079ac3 | -10.55239 | -52.04082 | 2025-06-30 05:31:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e1b3f04-552d-3726-8df5-d9a2880c24a1 | -12.10631 | -54.58028 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03e5b15a-5ad5-3493-b33d-ee40bf620f52 | -12.50472 | -58.34907 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41bb926a-e775-350b-9382-8c2ee84bad83 | -9.08368 | -59.4936 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 026e5548-b472-318e-b11f-c3ab5d51f09c | -10.87097 | -53.75924 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3741f4ed-8f77-31fc-a40a-a59af72ea6ba | -9.08305 | -59.49784 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65ed98c0-de1b-3c4f-ae3c-3c947f891abf | -9.24148 | -58.7349 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f6cf66c-f812-3f79-b11b-8130892f2bd8 | -11.94544 | -57.44828 | 2025-06-30 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b44b73b3-2130-34ce-84c1-198891081605 | -12.62985 | -54.22149 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1fa3e5e3-612d-3991-9a51-2b052594f5fd | -10.87186 | -53.75226 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22741882-75ec-3a97-ba92-4fd42f9071b3 | -10.8569 | -53.73946 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb8ad05a-d8b3-3b1a-bb39-e0c93bc2d7d4 | -12.61226 | -57.87786 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a6e57c5-6af1-3947-ad1b-65381795b870 | -9.23386 | -58.73379 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77a54d50-f0ec-35a3-94d4-d9cf35cafb93 | -9.94905 | -52.17882 | 2025-06-30 05:31:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fc5c821-b6de-3525-bce1-1fa7703e6b14 | -9.24804 | -58.76926 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8b97b995-3703-3948-8f0a-78695570a5bb | -10.87776 | -53.74943 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8eaa921-eeed-32bb-b7bb-1775e9e8dbbe | -12.10008 | -54.67325 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a26167ce-9a12-3fd2-b854-eb7968d3403d | -12.62573 | -54.21053 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1baab280-2e7f-3159-98f0-8e4d38d5182c | -12.62033 | -54.20979 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7640c2d4-5488-35f8-ab11-c008abae9ad1 | -11.80499 | -57.35633 | 2025-06-30 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 813f5340-4342-35ff-bbeb-d10ef3fbec57 | -10.12181 | -57.77711 | 2025-06-30 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e9ebb096-d536-3382-b8e5-835720d0b242 | -8.72931 | -64.16166 | 2025-06-30 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d235649e-5cf5-3409-a6bf-67beb979124a | -13.08204 | -54.85324 | 2025-06-30 05:31:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 81fed7a4-f136-3f80-a95f-884609a8d6bb | -10.86143 | -53.74738 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95d5c760-65c9-3d36-bf86-2a7af42302af | -12.10047 | -54.67012 | 2025-06-30 05:31:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aa88dc2-878a-3141-b644-4899d83bc3bd | -9.25773 | -58.75642 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c7c0578-e707-37a8-a97f-448f8d1e62be | -10.30249 | -57.0442 | 2025-06-30 05:31:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e37c512a-1b78-3a01-b4ac-c052cf87706e | -10.86234 | -53.74018 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b0fe8f4c-17aa-30a6-a8fd-e5a3567077d2 | -11.19855 | -55.92223 | 2025-06-30 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6b6b36be-ecfb-3aa8-b1d2-03c4abbf74ed | -9.24079 | -58.73959 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d1d99b0a-5645-3899-8cfc-9d932e5fa52a | -10.87415 | -53.73441 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b8257f91-248d-3c71-820c-9200a9f94b33 | -9.24632 | -58.75474 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7e380149-7657-350e-ac55-520f142939a4 | -8.69395 | -64.12226 | 2025-06-30 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a7bb958-a440-3406-ac8d-b47fde33697f | -10.85644 | -53.74306 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49cf5fae-7a75-3347-b743-5051cb2748d2 | -12.60832 | -57.87772 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37c045fe-deec-31c1-a748-d96e78401856 | -9.23491 | -58.75301 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de8d2c4f-d8f2-3f7e-a7e6-9a5ce8f1637b | -9.0916 | -59.49046 | 2025-06-30 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7af8def-b9c7-3ccc-82a9-e1c17c9167da | -12.6091 | -57.86928 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36062d20-168c-31bd-9d02-0cc557ddf59e | -10.55732 | -52.05065 | 2025-06-30 05:31:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2dd99b7b-bd7f-3013-ad96-49c1ba1092e5 | -10.85463 | -53.75735 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 25d322ad-0b69-336c-810c-8719d44d0c44 | -11.8093 | -57.35692 | 2025-06-30 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afa09fab-6e72-3127-83b3-1598ad424635 | -12.19882 | -49.63214 | 2025-06-30 05:31:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7e4a13e8-48da-38cf-980f-6126aaedd225 | -12.61252 | -57.87835 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 66cb350e-73d5-30e3-8442-c1971b519293 | -10.55183 | -52.04537 | 2025-06-30 05:31:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 72957246-a97b-3a62-9d92-1a921f7bc394 | -10.85599 | -53.74668 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9b0669e5-8bc2-3219-bb42-06750f1d6510 | -11.20325 | -55.92295 | 2025-06-30 05:31:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60f873bb-8e74-3362-ad36-f21b2bd03234 | -10.35037 | -57.50119 | 2025-06-30 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0999cd4e-a41d-30ec-8fd9-404b8424d3f1 | -10.86687 | -53.74807 | 2025-06-30 05:31:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f8f2eba-ae58-30ea-aeba-6ed01a178d92 | -10.35402 | -57.5056 | 2025-06-30 05:31:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c22048c6-dba9-3369-9c96-e8471af8fd8d | -9.24009 | -58.74428 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89f497b8-1071-33e9-98f2-25b162dc2a88 | -9.25552 | -58.76279 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75865652-4118-3656-b2fc-3d265f075f40 | -10.808 | -55.86007 | 2025-06-30 05:31:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ce7dc066-6117-36b7-bf5e-a7b275045689 | -9.24459 | -58.74016 | 2025-06-30 05:31:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 52558ab1-aa1f-3a03-b4fd-704ec8d5206b | -12.60887 | -57.87376 | 2025-06-30 05:31:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1845aa4c-5fa6-3e97-bbdb-eb77630216b0 | -12.62446 | -54.22075 | 2025-06-30 05:31:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 9649f627-dfb8-3525-9115-0c97dfb7b677 | -10.22771 | -54.2936 | 2025-06-30 05:31:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README15.md)
