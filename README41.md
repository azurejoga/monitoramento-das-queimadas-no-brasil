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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49042427-e908-3023-a366-399dc6990011 | -11.51302 | -51.88154 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2195c8c5-222e-3cd1-bc7a-aece8bfbe15a | -11.6961 | -60.1905 | 2025-08-24 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91d8258e-93da-3056-94f3-5ff059769a65 | -9.80488 | -61.20785 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5ef58b72-433e-3226-a42a-a839ea451e94 | -7.60758 | -46.2694 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 818bcaa9-7a96-3e70-a045-ed2fcf89fa3f | -10.80949 | -46.38883 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93182526-bd07-3e48-985f-2b41a320aa10 | -10.4157 | -47.19585 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| daaf1065-0e6b-3a22-a2cd-a83673c5d61d | -11.19059 | -55.0298 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aca7f1d2-d15a-3188-9c9b-aa7ff29db82a | -9.20508 | -59.48076 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0be6be7d-dd8d-3f9b-9889-4ed3474dde77 | -8.84023 | -49.89655 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8fe2eb4c-82d1-3eb2-9d6a-9f146f1f58cb | -11.12663 | -44.79314 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d19b034-3e2c-378c-b7f4-7af5a66a0321 | -8.35269 | -49.30405 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47577af0-fcbc-3755-b08d-83408b483d8d | -11.52978 | -51.86778 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 03320215-a9f5-3dd2-87be-cff184e5ab22 | -8.63388 | -62.63037 | 2025-08-24 04:34:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 63925070-7075-3ab1-a84f-47e0e597db14 | -13.47267 | -47.02218 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d02bc231-6ae1-36dd-aa89-deb258ecfb0a | -5.75188 | -57.59869 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09565388-fe3a-36f2-9de6-70dd965fe49d | -8.0697 | -49.64768 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e240358e-4d1a-3977-9a83-e5fcd049a5ee | -9.16399 | -59.47303 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f9922901-d66b-3aba-9281-71dae91eea5c | -6.58632 | -59.87367 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b02a5b7-e62b-3b6e-8d37-04b197ef6901 | -10.70522 | -51.58415 | 2025-08-24 04:34:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9b54c0d-bffb-3e65-a464-fb04eb32a338 | -6.95992 | -44.42209 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddf5a476-bf16-3ad1-93ba-a46f97103cb9 | -9.19832 | -60.76913 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a8079ce1-ace1-3456-8c00-e4ad1fd44c75 | -12.73729 | -48.11106 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a44b784-9373-337b-a4c8-ed8a88d76086 | -13.48329 | -47.02303 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 570a96e2-f774-3f48-9c08-b22739be13dc | -11.31462 | -47.85725 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3a91f73b-84f8-3177-ba12-be9ab433d0de | -9.19162 | -59.46259 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 111e5490-4453-33a7-a27b-1b111bcac9f8 | -11.52168 | -50.46648 | 2025-08-24 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bde39408-463d-3552-a2ee-2b38358e8845 | -5.43479 | -60.16634 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3aed05c3-ca43-3bca-995a-2e8c76de4a96 | -8.8626 | -52.04436 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2ea522d7-7180-3f41-b015-9197fd69f645 | -10.41111 | -47.17999 | 2025-08-24 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 57e2751e-81a2-381b-8c07-2f75f8b5b508 | -9.50828 | -60.51276 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 41844fee-fec2-3f33-b41c-4ddc60dc3bbc | -5.74885 | -57.58322 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e489e65b-23e0-376c-bb18-34f70a2debdf | -7.93051 | -45.91823 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e30a0e79-af7a-36d5-9dd6-00456d3cea2a | -9.19055 | -59.62107 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 13eaefe3-99af-3143-bbcb-de630e740702 | -10.76341 | -48.26449 | 2025-08-24 04:34:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25317b38-aae2-366e-b8e6-59ab71281ae9 | -8.84244 | -49.90428 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f314fe1-d235-33d0-81b5-cdebe18efc80 | -9.15586 | -59.49153 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f0b34e55-0814-3138-aa53-19d299e19b1a | -6.46319 | -53.39959 | 2025-08-24 04:34:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ffd4b08-71a5-379b-817c-5194da95260d | -13.48771 | -46.89178 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8407f585-97a5-398e-b637-b08352ab4d99 | -8.91272 | -62.44925 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8104eca6-4a22-3d81-a46e-e5907ba3606a | -11.50805 | -51.86503 | 2025-08-24 04:34:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7dcdefb8-e638-3502-ad3b-09a9a2ebf994 | -8.91109 | -62.42039 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 19.4 |
| b299dc36-a5c5-3c40-af06-de7508ad0cdc | -6.6868 | -58.85886 | 2025-08-24 04:34:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 796a5afa-ec4b-3b93-ba00-d244d6cb16d1 | -12.20429 | -47.11053 | 2025-08-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29e1a8d4-649e-3009-bc75-dce774a628b6 | -11.18141 | -55.03239 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cb95de48-f25b-3017-bafe-b36a2c331511 | -7.65563 | -46.27672 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74dbc07d-b3e8-36dc-bf41-51b278ddfc19 | -9.95613 | -60.19248 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0973fb3-5edb-3da8-bd7f-02ba32251c7b | -8.06104 | -44.99212 | 2025-08-24 04:34:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f00922f8-21c3-35bb-956d-e158d8f4375d | -12.54792 | -45.61804 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d3ae11c-68da-3340-ae82-b9a9b4e34ac3 | -7.18428 | -44.67603 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b747704f-2406-3829-a5c2-52b83e46c22d | -12.73449 | -48.1068 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0faa130e-b96d-3528-b7bf-8317d0badca2 | -10.10648 | -57.7688 | 2025-08-24 04:34:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8aa9824-209a-386a-a0ef-330ed7a566de | -10.8253 | -46.40335 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4ca5855e-b4b9-3703-8ee9-b2fb65f35e87 | -13.04401 | -45.2272 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe8cac15-29a6-32f9-93d2-8e68bdd2c9d8 | -8.23228 | -47.46309 | 2025-08-24 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebf6fb13-4987-319e-8e01-03b030297f2f | -13.39239 | -46.34792 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06f0b334-bb8b-322d-b830-f9918a905f50 | -13.17146 | -46.92906 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15be785b-4f8a-360a-90e0-b498fd6757a8 | -5.75201 | -57.597 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b853bda-ef29-3a25-994a-7e3921991319 | -11.18635 | -55.02906 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c3ba49d-d149-3fc2-837e-d74cc054f51d | -11.1861 | -55.02834 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb3b77ff-169b-3204-8c08-e9183139327d | -5.42627 | -60.17628 | 2025-08-24 04:34:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4345f9c6-f764-3894-966b-de94e3ff5778 | -8.89908 | -62.43212 | 2025-08-24 04:34:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ce9e136d-322b-34e7-91b3-dac2aa7bf18e | -8.52904 | -48.87782 | 2025-08-24 04:34:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dab4c6bd-7096-3657-bc02-d6635cdf252d | -5.79499 | -59.22017 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 623caab2-a20e-340b-9f30-b0facaab64e0 | -13.4703 | -46.88581 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b8664f7-7629-3b73-8dd8-560c9203d848 | -9.16064 | -59.49034 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fe3c6c59-246a-3820-bacf-a24556c32b76 | -9.25068 | -48.19785 | 2025-08-24 04:34:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| baf07025-f981-391f-8c46-5a4a664b88aa | -7.17517 | -44.66164 | 2025-08-24 04:34:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56cbba18-c0b6-3668-8453-55d09b52c317 | -12.7345 | -48.12941 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e558d24a-994e-3095-bba0-3f86df79e4ab | -13.3359 | -43.19138 | 2025-08-24 04:34:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0823aee2-78a5-38c1-be78-216f08fd2d2b | -12.73562 | -48.12201 | 2025-08-24 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5e9befc-26d5-3fdc-adce-1153ec437e24 | -9.16488 | -59.4999 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 895e2e2b-b4b7-3bbe-8e78-64ca25a617cf | -11.1833 | -55.01969 | 2025-08-24 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e45986d8-46bd-37c4-9d5b-1f38a04202ea | -9.1846 | -59.62007 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e78e84d-2fe1-3ae6-ba54-b77bb4a369ca | -7.46929 | -44.89512 | 2025-08-24 04:34:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b335798f-52a8-3f06-8c6c-93a5cd49d71b | -13.4344 | -47.03223 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bb08009-237b-32a2-9191-0a80e019c223 | -13.03703 | -45.22122 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f583bfe5-9e29-3cae-8f80-d980c5e072f6 | -5.74395 | -57.57871 | 2025-08-24 04:34:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2160ed10-4e51-3824-bd05-e387f8b607db | -9.1591 | -59.47417 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e73450c4-a0ec-3ff0-ae2c-ff008dc34c92 | -8.76683 | -49.97729 | 2025-08-24 04:34:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6d29c43-4759-3251-849c-d50dc0f6f106 | -9.16373 | -60.81132 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f48836e-39c6-34c0-8fef-3efc99915b29 | -9.25291 | -59.63412 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| aa96aacd-7686-3019-ba77-cf822ddb8283 | -9.10382 | -61.43126 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d4c36a98-a534-341e-be45-1b9c95698514 | -10.47573 | -46.88715 | 2025-08-24 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a572240-f16d-376d-899f-f45ddd566c56 | -5.80898 | -59.21252 | 2025-08-24 04:34:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05ec7af1-715d-344b-8051-d64bf63121ad | -9.68406 | -48.3421 | 2025-08-24 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f9eab65b-20fd-39bc-b7c8-e49076a4d3ae | -9.17013 | -60.81241 | 2025-08-24 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aa6386cc-2544-38a7-8fde-205d68775a02 | -7.9183 | -45.90445 | 2025-08-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c1d22a97-14a3-3629-abc9-17872e78b108 | -13.36091 | -47.50559 | 2025-08-24 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 327dd89b-c36e-38cd-8d8d-825d918c79f2 | -11.10562 | -44.77522 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 72b6aa89-303c-3f92-b2af-9a0e63f7d541 | -11.3314 | -47.85994 | 2025-08-24 04:34:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 10914f44-7ffd-3d80-b103-fd2d1da81436 | -13.45361 | -47.02359 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad2e93ee-83f1-3f00-afb5-a604e6790ce7 | -13.5027 | -47.03762 | 2025-08-24 04:34:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b65d8765-d43b-3ed0-a5a0-536273c66a0a | -10.60328 | -44.32824 | 2025-08-24 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 31.6 |
| bda5c84e-eb7a-31df-bb0b-d7b3eb5a48cb | -10.60113 | -50.16043 | 2025-08-24 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57bd36e9-e7a6-35aa-a05d-adc2ca1c5c49 | -9.51719 | -60.52223 | 2025-08-24 04:34:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c5f7fd4-0c87-37d0-8f9e-4076b2b8d0a2 | -13.04154 | -45.21694 | 2025-08-24 04:34:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bed6267-cb1c-35c9-963f-528ae77399bc | -6.918 | -52.85489 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0299a957-c61f-3da9-94cb-9827b31939c8 | -6.65391 | -55.42063 | 2025-08-24 04:34:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0f504c3-7085-39ef-8d69-bf3f82e2a549 | -11.52943 | -51.91315 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98bedfa8-fb61-3bd0-9512-36ff89d9024b | -11.51924 | -51.86602 | 2025-08-24 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README42.md)
