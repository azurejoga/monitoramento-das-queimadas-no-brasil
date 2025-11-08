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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ea13c835-9d6a-33df-9fea-7cdcb50cad3a | -9.50305 | -45.08031 | 2025-11-08 04:38:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8ee86d0d-221b-3daa-955b-9df382d5ffd8 | -9.32685 | -47.82649 | 2025-11-08 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 33d63a7e-633d-3258-b0fd-ea8960917f96 | -10.11542 | -47.51168 | 2025-11-08 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7b73da5-c414-3a5b-8615-a76e886befab | -11.72886 | -59.30938 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48fc625e-afd7-3616-9711-209980d673d7 | -9.04984 | -46.99977 | 2025-11-08 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3895571b-5193-3717-96dd-dca01de0236e | -11.90795 | -58.93573 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b9f90ffd-0dc8-37ac-96d1-c253c76a846d | -10.61399 | -52.18039 | 2025-11-08 04:38:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b00a9e38-7853-3f2a-bf29-8ee3e6a243e5 | -10.57741 | -49.25275 | 2025-11-08 04:38:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56c3f667-020a-3aac-babc-aa31aa9ea899 | -11.68798 | -44.14277 | 2025-11-08 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f12c9872-8522-3619-ac1a-649bc30341f4 | -10.50321 | -47.89157 | 2025-11-08 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0599463-8612-3cf1-ba3d-fa4d4fe5c77e | -9.04589 | -47.00289 | 2025-11-08 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f2a99e1c-6e63-3e7b-953f-e5fe8134c8ba | -10.81547 | -44.34735 | 2025-11-08 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f3fe6a0-d844-3dc7-8626-7ff6fa6583e7 | -8.11872 | -55.08854 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5202b518-5460-3dca-b1f6-108c15529261 | -11.09822 | -45.19152 | 2025-11-08 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71c73128-b557-3ccd-b5ad-a6e4ad86579b | -11.05448 | -47.64587 | 2025-11-08 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 90d970c2-fe43-323a-b7c1-958bbfcf6b27 | -11.07759 | -54.1012 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90409a06-7793-35e8-ae8c-7e0a8a9e0378 | -13.23567 | -46.7057 | 2025-11-08 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7f37a4a2-c40d-3620-9347-aa990a1b193b | -14.08732 | -50.47342 | 2025-11-08 04:38:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3874e7b0-8b47-389d-8d3e-7f900fc2b361 | -10.99305 | -44.85775 | 2025-11-08 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d3d8fefa-5fca-36c9-b70c-f959ca513e7e | -9.15937 | -51.30612 | 2025-11-08 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22b77014-0ad8-3e7c-83a3-5e45ea7b8006 | -11.09755 | -45.19601 | 2025-11-08 04:38:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38ff450e-7d7a-310a-9fb2-404e56ca63d6 | -10.53107 | -47.86677 | 2025-11-08 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee82b9f3-1ab3-3109-a904-8533479000b7 | -11.73672 | -59.31039 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c63f05b5-c647-384e-b2d3-21aca7ffa12d | -14.9785 | -52.98238 | 2025-11-08 04:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a11dd310-2390-3590-9369-5972b9285d7e | -10.36285 | -47.33036 | 2025-11-08 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e438f67-c170-31fd-a841-554dfba76a31 | -9.94442 | -55.5473 | 2025-11-08 04:38:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a38da99-b46e-3afb-b199-319b94887c55 | -7.93027 | -55.01258 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3e1005d5-c6eb-3fb1-93a8-fcf92eb4f871 | -13.23922 | -46.70623 | 2025-11-08 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 588fd587-2254-3dd2-8ecb-4bfbfc4d684f | -9.32296 | -47.82951 | 2025-11-08 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e351d05-bea5-301b-91a8-00f81120b49b | -9.22391 | -45.18564 | 2025-11-08 04:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eccc7343-d412-31bb-b5f4-017130e7e896 | -10.9936 | -53.98615 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 098c829f-7305-32f4-939c-4f7b3194814b | -15.33301 | -50.19955 | 2025-11-08 04:38:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3df5b4ee-e731-3a8a-9e50-ac0eeb2a4f08 | -11.20102 | -53.82199 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eba07f14-3e85-3d86-9081-3688c92c1f8e | -11.7296 | -59.30553 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99ec741d-fe9e-3444-82a4-035fd7415ad8 | -10.81155 | -44.34678 | 2025-11-08 04:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cc3f9cd-ea08-3d8e-8f7e-f57498d17338 | -11.87195 | -62.89254 | 2025-11-08 04:38:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60d586c5-1e99-3dc3-aba6-1332c99d038d | -11.86303 | -62.88912 | 2025-11-08 04:38:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cee04a52-34fd-31e2-84d9-33fa50a1323b | -15.23213 | -43.27894 | 2025-11-08 04:38:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fb3e5865-403e-3a4b-ac17-5f17b003650b | -9.05435 | -46.99303 | 2025-11-08 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89daa6fb-c58a-335b-b71c-5d43b0bc4ba3 | -8.12035 | -55.0793 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e2a4ee5-d701-3d5e-92a9-9da157e1231a | -9.04645 | -46.99924 | 2025-11-08 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f50771d-7dc1-3efe-874f-c16c1dd6b013 | -9.16292 | -51.30671 | 2025-11-08 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d40ab854-f7e6-3702-9a0c-4b35a804fd5b | -9.77925 | -62.50144 | 2025-11-08 04:38:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bab99263-9b9c-31af-ac7e-916b78a1064a | -9.76265 | -55.61829 | 2025-11-08 04:38:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84eaeceb-b91c-3c4f-a7f8-97057a1cd127 | -10.36229 | -47.33401 | 2025-11-08 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a342a763-ff5f-3dba-8640-c5213847bb9b | -15.23398 | -43.28115 | 2025-11-08 04:38:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bdbb5991-5308-309a-96ee-e329989a50a4 | -11.73378 | -59.31428 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 38b883fa-8b29-3d83-943e-20a38ffd3015 | -9.24237 | -48.55986 | 2025-11-08 04:38:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7545ad2a-5aee-3d7d-8592-c6f7ad8e8c62 | -11.69248 | -44.13984 | 2025-11-08 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73d514e8-5f80-3296-b006-4817595c6b82 | -14.70599 | -52.84562 | 2025-11-08 04:38:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a08992b3-4558-3e3a-a6d6-60a839202b0c | -8.74571 | -48.31963 | 2025-11-08 04:38:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b938a706-4d1c-39b6-95a5-8d428fc32040 | -12.45512 | -63.15416 | 2025-11-08 04:38:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2679e538-1d36-3e00-9a1e-87e47a286ddb | -11.72101 | -59.3198 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33f45863-d1e3-34cd-b7bd-eec42d709781 | -9.4869 | -47.35593 | 2025-11-08 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2768b09e-8c59-36eb-9bbf-88dacba21ae8 | -15.22951 | -43.28054 | 2025-11-08 04:38:00 | NPP-375D | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9e5ed09b-44ee-3d3f-875d-52defbffab1a | -10.37051 | -49.8708 | 2025-11-08 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a410c58-14ef-30b4-bdfe-cf24c2a16077 | -9.16124 | -50.56513 | 2025-11-08 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 29016830-db97-31fe-bde0-9e3d70ec983e | -10.99762 | -53.98689 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71f3436a-83e8-39b9-a5f9-6e008af49e81 | -7.91039 | -54.82434 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9477934d-7d26-38fc-8f04-ee6eeab2ad6c | -9.38538 | -50.72514 | 2025-11-08 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 177e2a75-d6cf-3540-a9e2-754372734a8f | -11.20322 | -53.83298 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1cd38897-bd36-3c84-a10d-83e75807a77e | -9.22024 | -45.18516 | 2025-11-08 04:38:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e157224b-c676-344d-8b08-4b6e9aa0addf | -13.938 | -50.05537 | 2025-11-08 04:38:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfa33670-176d-3dd3-ae9f-5d95221934b8 | -9.62696 | -48.88695 | 2025-11-08 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6386a6d5-f4b9-3674-98df-f6bb9e784004 | -8.15661 | -54.84788 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd0c1ff4-2c77-3fd6-bb86-15f74adaac5b | -9.07725 | -61.69181 | 2025-11-08 04:38:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b47381ac-e258-3637-bd04-1831b6734471 | -13.94133 | -50.05593 | 2025-11-08 04:38:00 | NPP-375D | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4e709759-c4dc-3214-bec1-5b634ec0f83c | -10.99296 | -53.98971 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 330cd2be-8922-3b02-9ee2-60e82cf8bc41 | -8.32522 | -55.03699 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bebdb169-a827-304e-abc0-35f68f7d32f7 | -10.99 | -53.9823 | 2025-11-08 04:38:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da051634-e495-3092-81a7-6a98a5744532 | -10.36715 | -49.87025 | 2025-11-08 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b70d069-a646-3c92-a8a0-b6196ff19e17 | -13.95471 | -47.41272 | 2025-11-08 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 334b6ca0-2d46-3c3b-b65b-6809e6c86354 | -13.95412 | -47.41666 | 2025-11-08 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 047d59e7-365e-3cef-9657-f965c47ab5ef | -11.72739 | -59.31704 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1f281a27-d456-3898-80b5-094d2a7d2ddf | -10.75453 | -44.80322 | 2025-11-08 04:38:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8439275-724e-330a-9e55-36d8d8a279d1 | -11.7239 | -59.31591 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f08ac59-39e0-35b6-8ccc-3c46fcc0c722 | -9.50241 | -45.0847 | 2025-11-08 04:38:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 522c77e9-b572-38e5-971b-94925b1577ae | -11.72798 | -59.32484 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9793edc-2a10-3d95-9dff-fce53b18d87f | -9.04533 | -47.00652 | 2025-11-08 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79737791-a93b-3bf9-bbbd-16bf3e2f47bc | -10.9526 | -48.02785 | 2025-11-08 04:38:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76c41577-9d3c-34b6-aee8-7e7ec822f0ac | -9.65077 | -48.88724 | 2025-11-08 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52838ac8-db2c-34d3-977b-086ab38bd373 | -10.26551 | -49.04419 | 2025-11-08 04:38:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3388a703-f3b1-3df4-925f-cf614bbe124c | -9.13515 | -51.29795 | 2025-11-08 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ae43411-4d75-3954-8bc2-cb8aeea8ab5a | -10.71438 | -47.73771 | 2025-11-08 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8ffdf661-0587-3cc7-b223-6edaaca0b091 | -11.72954 | -59.31702 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83a62f5e-3cc4-30b7-bfc1-aef05d1846be | -11.90941 | -58.9281 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa5a3957-f9b1-3bdb-9208-72c51d0c0f79 | -16.09231 | -49.38885 | 2025-11-08 04:38:00 | NPP-375D | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9a8aae4-9e86-3bff-a3d8-c3b4754ab55d | -10.51358 | -42.42785 | 2025-11-08 04:38:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 377c0b6c-ae85-3016-a3d4-d5cc08d28170 | -11.72589 | -59.32488 | 2025-11-08 04:38:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c3a771f-401b-316a-8b94-19a669878960 | -8.38117 | -54.82565 | 2025-11-08 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9facf538-5e52-33ec-9010-f0497678edd7 | -10.3589 | -47.3335 | 2025-11-08 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93592bb8-2d75-3fa9-ac33-f404e1c04a61 | -11.71643 | -61.42579 | 2025-11-08 04:38:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e35cdac1-7951-3374-81f1-e632a63fcba6 | -14.09066 | -50.474 | 2025-11-08 04:38:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 74cf9b86-2bce-32f4-8300-c43c3046f36b | -14.48936 | -52.14322 | 2025-11-08 04:38:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adcbe2bd-b767-38b4-a561-1f1c2da7fc87 | -9.04928 | -47.00341 | 2025-11-08 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4432dccf-1a7b-3ebd-ac53-f08b7d75393e | -10.71572 | -47.73742 | 2025-11-08 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0739b5b-46cf-3c77-a1a5-27708e157188 | -9.13448 | -51.30198 | 2025-11-08 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d45081b2-2fa3-37c5-bac8-3770ce45d937 | -9.91532 | -47.85009 | 2025-11-08 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 404a10fb-d6a7-36a7-b2b6-214a49947295 | -10.88505 | -49.5487 | 2025-11-08 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 02cf4373-9acb-3789-a784-6919f58fff7e | -11.66345 | -47.97359 | 2025-11-08 04:38:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README28.md)
