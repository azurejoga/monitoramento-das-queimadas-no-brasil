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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60b5cad9-f2a4-3d86-b9b1-b73d86be8847 | -3.0706 | -54.17258 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| dd8a8c19-ac0a-367b-9066-6e898c8dc37b | -4.30402 | -50.78222 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0dcd743c-e503-3849-8794-c026d6263ba8 | -2.82713 | -54.1229 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 293832d6-1c03-3799-b5da-f33e803dea63 | -6.35075 | -42.52229 | 2026-10-05 04:38:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 62b5e722-9b62-365d-896b-2a17290a365a | -6.20694 | -52.83379 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d6d07755-08b0-341d-8957-17e57fe7d00f | -3.10327 | -53.71452 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 0054cf01-f89c-3b66-94df-163e7890bcec | -4.04224 | -48.99538 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6ae3006-51ba-31de-9e0b-83817e22932b | -5.68524 | -53.49615 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9c0f1f5-8629-35cc-b929-796280465ba1 | -3.11481 | -53.70745 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 55059867-61ba-38a2-a28f-fb8eefd3d33b | -1.19479 | -53.38427 | 2026-10-05 04:38:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a73d2e9b-11d8-3bb5-9947-78a32791b950 | -3.91245 | -49.71389 | 2026-10-05 04:38:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c669f258-1d6a-3cf2-90e3-a960f7d55213 | -2.98175 | -54.09658 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90312ed7-2f2b-314b-affd-933377e5436b | -4.03858 | -48.99474 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 24d692f9-b220-390f-83ce-c9f2e6dace1a | -2.99824 | -54.22225 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cf8be88-f854-31b4-8d1a-1293b9b5873d | -2.93254 | -54.16546 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df100317-a533-3103-8253-7fe0144b219a | -3.45305 | -42.97818 | 2026-10-05 04:38:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36e1ca27-4c94-3c86-a094-2a0504bf4c3b | -2.95885 | -54.10555 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2994d39-ef91-3d86-9704-48558c683a02 | -2.82192 | -54.12201 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b266d3fb-9349-35ed-92d2-cfccb160d47f | -7.71813 | -45.46183 | 2026-10-05 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04153280-b240-3159-a066-046c3f90a2af | -6.42838 | -43.72407 | 2026-10-05 04:38:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9217a4b6-f742-399b-8dda-226ae3a6d588 | -3.11242 | -53.72208 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be6100b9-7c95-33b7-bc15-c1aa7c9d09f0 | -3.12303 | -53.70937 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60c1aeeb-4266-3f82-a9fe-66d0e68c6828 | -7.71533 | -45.4577 | 2026-10-05 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf9ce22c-39fa-35db-a31b-76b4606c19ce | -3.06539 | -54.17168 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b1f694ae-5d46-3519-ad75-fd31c13e3b36 | -3.09582 | -53.72826 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8575fcc7-5f7f-3b55-8c1b-a5362bb05aef | -2.94417 | -54.12661 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df0416bf-f8aa-35d8-8aaa-1669b40183fd | -3.11799 | -53.70853 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a5ef1586-fdb4-3f43-b671-bcc1f7a5ce9d | -3.05471 | -54.2346 | 2026-10-05 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64d37c38-98d9-33d5-a0ad-66df0f8eb98c | -7.72204 | -45.45883 | 2026-10-05 04:38:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0aed44d1-df5a-30d9-a168-fd347078378f | -3.15318 | -50.43217 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 88d9b51d-4417-3d0a-9db4-780a7104b672 | -3.12158 | -53.72961 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 549fba2a-1e33-3b02-bf2c-2e18126fc522 | -3.05002 | -54.23052 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92bb5266-9afd-3419-b9aa-709adda61ca7 | -3.09542 | -51.09593 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 316f03f9-cb43-3d5d-b777-c573b0abd5bd | -3.4698 | -50.09238 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac8e3922-990d-3037-ab88-16457d9d2013 | -3.08624 | -54.17518 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| a168846d-2ee3-335a-84ab-49192d8a8565 | -3.98454 | -55.82002 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8584138d-b572-305a-948a-0cb33c404396 | -2.69848 | -49.03968 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5023a902-b6d1-3eb8-853e-576bf5453089 | -3.31067 | -53.83872 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c457936a-5e6a-3c14-8edd-37fb0a8105db | -3.45289 | -42.9792 | 2026-10-05 04:38:00 | NPP-375D | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad66d684-136b-3dfa-a2ef-df92683498ca | -4.11377 | -49.07954 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b9f407b7-a4f1-35b7-8441-902fc476d81a | -3.12758 | -53.72463 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a8ab9930-56e6-3770-9841-48a52d2f75ba | -6.90771 | -43.67105 | 2026-10-05 04:38:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 98717a6f-007a-3b31-93eb-9338822b0d7a | -3.84993 | -50.31182 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac0b38f6-be14-3075-9868-ce41601c8301 | -3.11967 | -53.74134 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 294e7674-1b59-3e5a-8ae0-8d3a15212bdc | -3.71127 | -50.64967 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bf1c7ad6-7193-31c9-9c9a-f29bcb801f04 | -3.15956 | -50.44382 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f4b39c81-c3ba-3749-8c45-08978137ae8c | -4.10713 | -49.07412 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8fc2e34-1f48-36fd-aea1-2d4f150238a2 | -1.24913 | -55.87926 | 2026-10-05 04:38:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d2ed961-5471-3f4f-ae02-159d3c1eeba7 | -2.97498 | -54.10501 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3eb18bdd-f0c1-3913-bd8e-408ce6d18d2b | -3.57399 | -55.41628 | 2026-10-05 04:38:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e60538e-a2e9-3624-9347-1023eaa931bb | -3.117 | -53.72585 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67c03aee-08ee-3473-bbbf-845ead7f3fa1 | -3.12808 | -53.71022 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a4e0c733-e23b-3497-bd42-f7e8e3cdc635 | -3.04947 | -54.2337 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e31e8f35-447f-33ae-b88d-4d8ebf4986bd | -2.84863 | -51.2879 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77146455-5339-30d1-bac3-5c5d2ffd300b | -3.16924 | -41.39855 | 2026-10-05 04:38:00 | NPP-375D | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f32077a2-9903-3501-9139-274325a854a7 | -3.10859 | -53.74548 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f92741a-672c-33b5-8dd7-ba9c412f4ae5 | -6.23688 | -52.68738 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34614324-c3ff-3d6f-9745-8f5753a934cb | -6.06563 | -42.9098 | 2026-10-05 04:38:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 01251a12-4ce0-337c-948e-2932b222986d | -3.50526 | -54.61065 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4df0695c-3e8d-384b-928b-2a2386a8bfc8 | -2.25604 | -51.88665 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a5d7e681-ae53-3426-829c-828427914943 | -2.81097 | -54.12336 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 657147f7-a450-3cb7-bbc2-8cf20250a71f | -3.1129 | -53.71914 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61d811f3-56f6-322c-bd80-bab56c0361f9 | -1.45958 | -53.60323 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e44795d-b9ac-340b-b8bd-7a7af9ed5fbb | -2.93897 | -54.12567 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4ea25fa-7bae-3110-8686-70f339b4bcb8 | -2.81722 | -54.11797 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a08a380c-ce33-3852-aeca-f4edfa07a9e6 | -3.07581 | -54.17348 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 7de8127d-ddd1-3fa2-a5ee-7613800ac0fa | -4.64947 | -46.31161 | 2026-10-05 04:38:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 528b9530-7540-3900-bd04-53d312127a6c | -3.39919 | -50.1527 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 94701e9a-700c-3ba5-a1ce-cc45fe60d8ba | -6.71411 | -45.98474 | 2026-10-05 04:38:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77643b01-64db-37d1-af01-0b12c3d4d264 | -3.07265 | -54.19215 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8e174f1-7025-3199-b81a-06d2aba65210 | -3.12758 | -53.71313 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 84fe6fc5-4fbd-31fc-8c87-1d35ac0393ad | -2.44976 | -56.38124 | 2026-10-05 04:38:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9c17639-e6d3-3f7f-adff-a5eac0df988d | -3.10305 | -53.74757 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 83725ac6-a275-3bdc-8b43-8cec25ee2e76 | -3.10257 | -53.75051 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f9e5370-8895-30cb-8ed4-a2b9dd8bccaa | -2.90771 | -54.08822 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87a684dc-f0ee-3e14-b775-2adaec3578f2 | -3.04693 | -54.21704 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c8c5956-f0ee-384f-b724-56e21bafb1f8 | -6.81937 | -38.53092 | 2026-10-05 04:38:00 | NPP-375D | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a834d871-74b8-3347-b1b6-e3c961f2af61 | -2.81462 | -54.13378 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1cd635dd-5a26-3f71-a2ca-bfa2d7eb02aa | -1.08286 | -54.11005 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f30ac4b6-e158-3298-b973-6b6785bc5c75 | -2.69921 | -49.03523 | 2026-10-05 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dc27173f-e7b9-31ea-9363-ed3ad5ee0404 | -3.12591 | -50.34143 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c946df5-19f2-3477-8343-d515fbe34e7b | -3.12062 | -53.75399 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bbc4393-fa0a-34d2-9dbd-09cdfdd8e65c | -4.10961 | -49.06758 | 2026-10-05 04:38:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d529dc1d-272e-3d0c-9458-1b2285fdc941 | -4.11389 | -50.80328 | 2026-10-05 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c4684df-e878-3c94-81d0-dfcc33fec684 | -3.11455 | -53.75901 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1ecc10e4-1ca9-35c1-b353-79a66cb4d5ed | -3.15495 | -50.44659 | 2026-10-05 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 26b178b1-d7a2-3292-9593-8054b85a780a | -1.09466 | -54.10511 | 2026-10-05 04:38:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c028e5e-5aec-324f-8ac7-02242ed9da79 | -2.82295 | -54.11573 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 818c7644-df32-3d6c-8c66-7464c3f8252e | -2.94213 | -54.13912 | 2026-10-05 04:38:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bdf02689-33ec-38e5-a8bf-a31f0d101ff1 | -3.10087 | -53.72913 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7644f57b-06b5-32d4-a223-306875db0843 | -5.9983 | -53.52505 | 2026-10-05 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4390fe90-339b-32b8-92d9-1f589f444155 | -6.219 | -52.68434 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa0aebb0-9ada-37fa-9bce-a59ef22d2b0d | -3.46536 | -54.60071 | 2026-10-05 04:38:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 932765a3-7c49-39ba-9aad-705ca0b4f6ec | -4.30749 | -50.78644 | 2026-10-05 04:38:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22814e81-73fe-383b-b97e-b2f0b042916f | -2.85104 | -53.91219 | 2026-10-05 04:38:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| facd5499-99bc-3f7f-8bd9-2b9a1614d8a8 | -5.06305 | -40.45654 | 2026-10-05 04:38:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 276e4a57-5f94-35d4-9012-ce52d88de0c9 | -3.11749 | -53.71144 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 99a4c803-9aa8-38df-a98b-b2281e1b883e | -2.5376 | -58.03091 | 2026-10-05 04:38:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d1a8add-f2d0-3de0-a0c7-3fee8e50f4f7 | -6.23766 | -52.68282 | 2026-10-05 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c53a75-0846-3301-a943-40ec686e41de | -3.1271 | -53.72755 | 2026-10-05 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README20.md)
