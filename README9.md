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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b98a87b9-b3e4-3a45-a5fc-cdd4c1431ea5 | -4.1762 | -44.2486 | 2025-11-18 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 285.6 |
| 08de1652-6ef8-3b3a-a5ab-aff649d7a3ce | -5.4192 | -43.0347 | 2025-11-18 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| d852e5b7-5576-3187-90a5-b250b0f0c2ac | -11.5291 | -48.9559 | 2025-11-18 00:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 769ec7db-cf93-32c4-83e7-92c99eab0e0a | -10.3535 | -48.9174 | 2025-11-18 00:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| a06cbdf5-8ecc-33ca-97f1-27b9cab100d6 | -9.3969 | -48.4523 | 2025-11-18 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 6435e9fb-7d26-34b9-b771-03daa014bdfb | -3.4769 | -46.0879 | 2025-11-18 00:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 109.1 |
| d17ba175-0a7e-3b0c-b35f-59e1d46f869a | -9.1124 | -44.3334 | 2025-11-18 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 281.8 |
| f3540e46-c7f9-36b8-a8dc-14e97c1f5c5e | -3.4771 | -46.0434 | 2025-11-18 00:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2da3b501-6bbd-3a80-881b-78ed8f2ab7fa | -5.419 | -43.0582 | 2025-11-18 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 147.7 |
| 23ff22da-4f6a-3dcf-88c4-f892b2f1848d | -6.1138 | -42.9569 | 2025-11-18 00:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 87.1 |
| 4477b704-9613-3b57-9695-5db00ccc0c01 | -2.8298 | -45.4195 | 2025-11-18 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 12edd56f-fbc1-36d2-9ad2-5a03334e893c | -4.1781 | -50.2091 | 2025-11-18 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| b383db7b-a8f2-378a-b175-58d821342692 | -2.8491 | -45.2388 | 2025-11-18 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 86.8 |
| c6736a5b-371d-35a3-bb1b-706cb9f53625 | -2.8677 | -45.2382 | 2025-11-18 00:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 162.5 |
| cf86db75-20a1-3fc4-b901-13b719932574 | -6.1326 | -42.9554 | 2025-11-18 00:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| a53a6108-1710-3632-9a69-1c8b6937da1f | -3.1256 | -45.7449 | 2025-11-18 00:20:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 3c9a62e2-8ab9-3929-8145-ead5e869db18 | -17.8999 | -40.0629 | 2025-11-18 00:20:00 | GOES-19 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 185.9 |
| 0432f0eb-d722-3d73-89b4-53f8e85b64d2 | -2.5238 | -47.8115 | 2025-11-18 00:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| b7995734-b527-3894-ae5f-e0ba3f85f5bb | -5.4379 | -43.0333 | 2025-11-18 00:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 4755d448-93bb-3a83-9238-6231c9d087ef | -4.1782 | -50.188 | 2025-11-18 00:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f9b654e2-8f50-3854-8fa5-86c61ca06efc | -12.7378 | -45.4274 | 2025-11-18 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| ab406d91-a229-35fc-b5fc-037c9db695e8 | -9.0934 | -44.3356 | 2025-11-18 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 332.0 |
| c3358d2a-cc98-32de-9864-a88da5cd32d1 | -11.51 | -48.9583 | 2025-11-18 00:20:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 46563496-8ab6-325f-ae31-2acea921f98c | -4.1949 | -44.2476 | 2025-11-18 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 282.8 |
| 3c95ab24-b1d8-327b-bd80-8e430fa5cbbe | -4.195 | -44.2247 | 2025-11-18 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 208.1 |
| 22a54df0-5d50-36f9-bcbc-5ace1fb0052b | -4.1764 | -44.2257 | 2025-11-18 00:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 52b558f5-58b8-3f87-afa3-459d3dc13c5c | -17.8991 | -40.089 | 2025-11-18 00:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 247.9 |
| 934cb026-ce06-3601-815c-05778f3f8f5b | -9.1127 | -44.3102 | 2025-11-18 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 7011e147-6e8c-311b-baa7-a9d0537163a8 | -3.4584 | -46.0664 | 2025-11-18 00:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 76.4 |
| cba11e0a-0f3c-3950-8ddf-c155033f0de9 | -12.7386 | -45.3812 | 2025-11-18 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 113.2 |
| 8160d0a0-52f0-31f2-9260-a5ab0b155839 | -9.3972 | -48.4305 | 2025-11-18 00:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| b879861c-5a17-3edc-9f5d-f53bd041f866 | -9.0745 | -44.3378 | 2025-11-18 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| ca8aab05-3a3c-3740-9704-9b0f112bee6f | -3.3555 | -44.3798 | 2025-11-18 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| 24cc7729-d36c-36bd-bfc3-c720ea5eee88 | -12.7382 | -45.4043 | 2025-11-18 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 17e7f351-c2d2-31e2-aa3a-ef3c17b423e6 | -9.0937 | -44.3124 | 2025-11-18 00:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 122.7 |
| cd107410-6c88-3369-abb3-0562ecf59b62 | -2.8678 | -45.2156 | 2025-11-18 00:20:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 82.8 |
| 07114f8d-0f7a-3945-bdcb-be8b0e07ea21 | -12.7579 | -45.3781 | 2025-11-18 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 24dccf36-5801-399c-9616-54b0874ce784 | -3.3554 | -44.4026 | 2025-11-18 00:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 52be925e-1ac6-3206-9b88-1859381992bf | -12.7575 | -45.4013 | 2025-11-18 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 60.2 |
| d638fad5-0428-360f-990a-4f87cc5a04a2 | -3.0236 | -47.8396 | 2025-11-18 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| beb611eb-49ea-3305-8555-b1770b9d2d2e | -17.9194 | -40.0833 | 2025-11-18 00:20:00 | GOES-19 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| b7dc7fae-2561-3ebc-a474-bebbaee8a9a3 | -11.5291 | -48.9559 | 2025-11-18 00:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8d11cd5f-bc14-3e4f-b926-9cf2475a8a1f | -2.5238 | -47.8115 | 2025-11-18 00:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 2f6302cb-b5d1-342e-9a28-9aa6fdbc6163 | -3.0236 | -47.8396 | 2025-11-18 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 63927f7f-f7c5-326d-a001-a27bd92e5ea4 | -8.2851 | -44.0095 | 2025-11-18 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 6cb2fd69-de89-3b1b-9aac-212644174577 | -12.7193 | -45.3842 | 2025-11-18 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 2bb272ba-5ba4-3ca6-ae7a-566d8288fd27 | -5.4192 | -43.0347 | 2025-11-18 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 62e808dc-0e51-3c53-b74f-c7d88bfbf02a | -3.4584 | -46.0664 | 2025-11-18 00:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a5804e37-1ce1-3ffe-b824-f2b504816b61 | -9.1124 | -44.3334 | 2025-11-18 00:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 0a03f42f-f47c-3d85-bd8d-436c1eadc2dd | -3.477 | -46.0656 | 2025-11-18 00:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 268.6 |
| 1e611739-3a78-3867-bcef-d2ad572fce25 | -2.8677 | -45.2382 | 2025-11-18 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 171.9 |
| dafaacf1-c5e8-3d83-8415-b3feeccd732c | -8.3043 | -43.9842 | 2025-11-18 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 130.3 |
| d1842c6d-435a-359c-8211-3cd65c7314ca | -3.1256 | -45.7449 | 2025-11-18 00:30:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| dda3654a-126e-3cf0-9e35-4569e883c1ea | -12.7579 | -45.3781 | 2025-11-18 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| d6dedb5d-377f-3763-8362-843083f5edea | -9.3969 | -48.4523 | 2025-11-18 00:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 2385ce37-c758-38ee-a07a-b0be19e23efe | -9.3972 | -48.4305 | 2025-11-18 00:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c5af47e2-90d3-3e99-a9ec-d1a14dc24c9b | -3.4769 | -46.0879 | 2025-11-18 00:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 125.0 |
| afb7cec8-e069-34b2-bb3d-a33382651860 | -4.1764 | -44.2257 | 2025-11-18 00:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 224.4 |
| 7cdab8d5-8a8c-3f55-b774-37c4dc9ea300 | -5.4379 | -43.0333 | 2025-11-18 00:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| f827c0b2-1de0-3353-817a-d60eca8e1de1 | -4.195 | -44.2247 | 2025-11-18 00:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 240.2 |
| ed81b84c-1ec4-35f4-a3da-2ceac9584a3b | -10.3535 | -48.9174 | 2025-11-18 00:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 878246a4-64b2-3d5d-8413-dda889d4e6e9 | -9.0934 | -44.3356 | 2025-11-18 00:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 6adaeac2-ea2a-367c-8b01-1ec8b99891f7 | -12.7386 | -45.3812 | 2025-11-18 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 183.7 |
| e1e04636-de78-39a7-8e36-2ccc5c39b193 | -8.3037 | -44.0307 | 2025-11-18 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 0b0af945-9379-3023-82ef-62ea884b9edb | -8.2854 | -43.9863 | 2025-11-18 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 5d73d23f-348b-3d44-b0fc-72a5c380969d | -8.304 | -44.0075 | 2025-11-18 00:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 233.1 |
| 6e563b58-135f-3d30-85f5-260cec49f22b | -3.3554 | -44.4026 | 2025-11-18 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 679e0ee4-cccd-38ce-9513-8a2e3f8e4e3b | -4.1762 | -44.2486 | 2025-11-18 00:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 797b22b6-dc68-32ea-95c2-fafa8d234933 | -2.8298 | -45.4195 | 2025-11-18 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5ff48537-b85b-3e9b-9355-1884b9de2380 | -3.2506 | -43.0449 | 2025-11-18 00:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 916bd4c7-dfeb-3c3f-bd95-ce96206316c1 | -4.1781 | -50.2091 | 2025-11-18 00:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 628c9640-2cd7-3740-9cb2-91f5e530c6bf | -3.0714 | -45.4107 | 2025-11-18 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 100.2 |
| 554dbfba-c99f-3150-bad1-487a9f60d65f | -12.7382 | -45.4043 | 2025-11-18 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 04ca54a0-5bae-3a0b-bab5-e6cc8a5439a5 | -2.3347 | -55.7945 | 2025-11-18 00:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 28129958-0efe-3cb0-8c53-b355249afbe3 | -2.8491 | -45.2388 | 2025-11-18 00:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 44e5fed8-8c88-32f3-9348-2d3f3a7024e2 | -3.3555 | -44.3798 | 2025-11-18 00:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 98.0 |
| be2b38bb-393c-38db-bf1c-f05cb9f8f017 | -4.1949 | -44.2476 | 2025-11-18 00:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 238.6 |
| bd19afa7-58de-3efe-8e8d-91be35dc3b3f | -2.8678 | -45.2156 | 2025-11-18 00:30:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 6e162a2c-3d54-3b3e-8337-b186718adea5 | -2.7194 | -45.1531 | 2025-11-18 00:40:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| ecb02e02-650d-359d-8da0-206333fac79b | -8.2854 | -43.9863 | 2025-11-18 00:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| d6fbc42e-7cda-3399-86e3-f8e3f82d1ead | -2.8678 | -45.2156 | 2025-11-18 00:40:00 | GOES-19 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 87ec5839-ad2d-3e10-8147-aab54e8ac07b | -3.3367 | -44.4034 | 2025-11-18 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 2de72583-7582-3cb8-a7f9-e82606095720 | -3.0236 | -47.8396 | 2025-11-18 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 3d8660e9-571a-30e7-94df-854f9f8dd70f | -5.338 | -43.7623 | 2025-11-18 00:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 7b1fa0ec-69ec-32a4-bb05-901540f17e91 | -9.4765 | -40.3613 | 2025-11-18 00:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 210.7 |
| cba05b0e-051c-3e4b-b04f-8cebfd728837 | -9.0934 | -44.3356 | 2025-11-18 00:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.8 |
| f8a2edec-19ce-360b-a478-890ed93d699e | -11.51 | -48.9583 | 2025-11-18 00:40:00 | GOES-19 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3153ebd5-60ac-3960-9dfa-478002a91633 | -2.5238 | -47.8115 | 2025-11-18 00:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 1aab7b1a-5160-3527-a1a9-17b7e699ebdb | -12.7382 | -45.4043 | 2025-11-18 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| dbdf1fa7-4014-30ff-9c3b-007bd77231b2 | -4.1949 | -44.2476 | 2025-11-18 00:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 197.5 |
| 2b970bf1-fb68-3079-85a4-09ca891bb401 | -5.3382 | -43.7391 | 2025-11-18 00:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 4f1c4b32-f66b-3e73-9153-c6742ffba58b | -2.8677 | -45.2382 | 2025-11-18 00:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 136.0 |
| 69cd17ca-d36e-38fd-9ff6-5b149d7640f9 | -3.3369 | -44.3806 | 2025-11-18 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 7fdb0727-e034-3429-8672-4fd343433da3 | -4.1781 | -50.2091 | 2025-11-18 00:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 6fb3b565-12ce-3862-b500-53996e1273e3 | -4.1764 | -44.2257 | 2025-11-18 00:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 197b7497-dc42-3abc-a4ec-7ae03ba0f90c | -2.3347 | -55.7945 | 2025-11-18 00:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| 544bb7ef-dc9f-3777-a896-47ef543e44e6 | -4.195 | -44.2247 | 2025-11-18 00:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 202.8 |
| f1223b69-a48a-30bd-8e9e-5344385a1fc4 | -8.304 | -44.0075 | 2025-11-18 00:40:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 2c940d9d-6cc8-3cc7-91be-de5841fe025f | -3.3555 | -44.3798 | 2025-11-18 00:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 698cefbb-8dba-3b78-be1b-1d4a105c06b8 | -4.1762 | -44.2486 | 2025-11-18 00:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |


[Clique aqui para ver as próximas entradas](README10.md)
