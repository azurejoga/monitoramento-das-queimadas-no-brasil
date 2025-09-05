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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 791d77a6-804e-3ded-9d75-35bd1d1dba00 | -12.48562 | -48.09171 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7eff5061-1b06-3061-a30f-395dbc84ddbc | -12.98332 | -48.07632 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e7ec5f4-9159-3400-90a5-aa0e450e7382 | -11.39777 | -43.59966 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 68b8ea77-c15a-34f7-aaec-26ec9fc79432 | -8.51985 | -51.33036 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6508656-127e-3844-9dda-94e0d736a598 | -11.58228 | -52.18304 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44029bdc-883a-3179-a0dc-8e486a38352a | -8.91689 | -45.11504 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c7d6a7a0-94d2-35f5-95ef-493af0a9d12a | -5.49179 | -60.12781 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 480e137e-452a-38c1-9f3d-8c80be152848 | -10.52509 | -57.77941 | 2025-09-05 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfd38624-68d9-3ba4-9ec4-97de64645272 | -10.97448 | -45.98565 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e70c9839-d4e7-337f-babd-ae6139048a0e | -5.4984 | -60.12909 | 2025-09-05 04:36:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 154164f0-99cd-350a-a4a0-cb3557738a8c | -9.06364 | -47.00756 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0f54f95-3d3a-3710-8336-2b8e209fe18e | -11.87628 | -40.95104 | 2025-09-05 04:36:00 | NPP-375D | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f2381e47-7bf7-3505-b2bc-14836cf14a92 | -12.87316 | -48.01547 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d76e80a2-260f-3c3e-99bd-658f3ff1b450 | -9.71213 | -51.07693 | 2025-09-05 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6a9c6876-5710-3b71-9531-5edae48d2d58 | -9.32825 | -55.20944 | 2025-09-05 04:36:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8613740d-d6fb-311a-a2a6-2dbf4098c24c | -10.98537 | -45.93698 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08dd744f-05ef-3c1c-a2a7-9bf39990e0f3 | -10.98335 | -45.99955 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c94ca6d-64f9-3c3a-acd4-95f310f035db | -8.09353 | -45.33407 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f0f74654-604f-3a32-92bb-b35d5c41c568 | -12.71224 | -45.07541 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 265ed8c6-e197-3e13-bbba-ecd215d6e05e | -9.79811 | -48.32957 | 2025-09-05 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea6b5aca-dc57-35ff-b212-ed8ae058f1cf | -7.22804 | -56.85401 | 2025-09-05 04:36:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20ee59bd-7b72-3875-8d63-cb5b3de0006a | -12.50859 | -48.07684 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00325351-bf89-313c-ba6e-8b0c760d7566 | -11.71997 | -48.34559 | 2025-09-05 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 13e5340b-6f41-3883-b276-db80cedd22c1 | -10.97397 | -45.96451 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b236c879-3996-3c5a-885c-84a57f123b21 | -7.74465 | -48.8073 | 2025-09-05 04:36:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 511ed549-a58f-3ce0-8736-f2b0c485a308 | -10.07213 | -48.07035 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78fdef54-3409-3a41-a26f-f93bb1828a98 | -8.34973 | -52.52308 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4f7accdf-5c15-38c4-bea8-9c7538d90952 | -11.99046 | -46.75332 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 23ac3e5d-f55e-379b-836a-2bb21b4e234a | -11.0047 | -47.15228 | 2025-09-05 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e0a64eb9-45bb-3c40-98f5-a051fbe134fa | -10.23077 | -50.5414 | 2025-09-05 04:36:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd9fb420-5a8f-376b-a5d2-5fa6773009e0 | -8.90588 | -45.86673 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a074c044-df10-3ba7-99fd-a16e6d99cb83 | -9.50586 | -57.81682 | 2025-09-05 04:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31ec9fc2-875d-30e0-be98-d545ac226643 | -12.91606 | -48.03662 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b13a6674-7379-3608-b2ed-2a002876ddfc | -11.00744 | -45.93626 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e5949353-9ecd-3347-9846-80f626f4c304 | -7.77308 | -50.3186 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33ef28b3-fe87-321c-8d8d-4a0d80d0ca58 | -8.88166 | -47.23333 | 2025-09-05 04:36:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a91e18c6-b293-3594-957d-e2bfd4b7daa9 | -11.80867 | -44.25946 | 2025-09-05 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28b58daf-7921-3eee-8a28-c9711254b6a1 | -8.8971 | -45.78068 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4edecafb-275d-3597-ac77-d7c7d15bec3c | -8.02009 | -44.77478 | 2025-09-05 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b88c1ad5-416e-3c5c-bb16-b2f552235a61 | -11.98989 | -46.75724 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ea94ebe1-aec7-3c20-845e-cc7df48fe46a | -8.09294 | -45.33807 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 51383b21-4e90-3dc0-a301-e6e28682eb3e | -9.44222 | -46.81354 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3381fa07-0278-33cf-a3bf-3725f7f87127 | -11.64326 | -52.21991 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2c3ec642-5796-3327-88f8-d1fdefbc3763 | -8.02128 | -45.41119 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0cdbd711-8aa3-3d84-8510-e49acc435b74 | -11.02179 | -45.06247 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05dcb079-8f00-3807-8916-04d920167092 | -8.09234 | -45.34211 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b39e2082-4a7f-3950-bc9a-1a4483f3a3d4 | -12.50131 | -48.07936 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c4d0f23a-9178-3684-93e7-b650a8b1b504 | -7.68074 | -50.26411 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3d883f05-374d-36a6-9730-96d8d5d9ee71 | -13.66146 | -47.92481 | 2025-09-05 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65788a3a-a34d-3575-be1c-b57e95044913 | -10.32939 | -47.82313 | 2025-09-05 04:36:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 92f43f49-9597-3275-a559-5de56483807a | -10.03916 | -48.1339 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 19dbf5dc-76c1-39c4-92f8-ef5a6e0e7532 | -8.37016 | -52.54839 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c67a947a-63a6-3e6b-a80b-0fea932e5c3d | -13.23061 | -51.81356 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dead55d9-0ec6-39e2-a2be-d6cd5a1a3f5a | -12.8941 | -48.02202 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3518117-b5f2-3b20-be15-f6fbda925852 | -8.19387 | -49.60045 | 2025-09-05 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29ad72f5-0636-36b9-b489-f4764d7b3443 | -13.00981 | -45.22271 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ab975c9d-2c97-3cac-abc2-0594dc91fd79 | -10.06543 | -58.39235 | 2025-09-05 04:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e116796-597f-3c88-8c8f-d1f8f4f39646 | -9.08171 | -47.00281 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fae3e792-3e56-37b4-9ea7-3e91eed1adcc | -11.65477 | -54.51907 | 2025-09-05 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f58aaf1-1298-387e-b1c8-493563e115e3 | -12.52371 | -48.06823 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c54c3046-250f-345c-85f6-c037b29da9c5 | -8.09592 | -45.34259 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1e492fa4-6c6d-365c-a5b1-3c5ef87ac396 | -13.00014 | -48.05665 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00938047-f73e-302f-b2b4-c020d3869bb8 | -10.76189 | -48.29166 | 2025-09-05 04:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15679c23-34a3-3213-a3da-19a98d6f032c | -7.61805 | -47.93913 | 2025-09-05 04:36:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| afcfa4c2-6b09-3480-808b-c708233dc101 | -8.98217 | -45.52692 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3ea287f-f905-3102-804a-11e64bab39be | -12.86078 | -48.00606 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b0c40e5-9a86-3372-bfb4-e33e800d9a84 | -7.82171 | -46.08598 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d25e2d88-c1a0-3dea-a7e7-01f3d0dca485 | -12.94086 | -48.05526 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0da2af47-6e63-3e75-a0ee-58c36934308f | -12.71157 | -45.08014 | 2025-09-05 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 46a9aeb6-13a1-3d91-98f1-3a1c54de3b17 | -10.5146 | -57.77736 | 2025-09-05 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc3d66a2-bffc-3b93-ab0e-8468a203b95b | -11.17166 | -50.02395 | 2025-09-05 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0099c069-6028-3e90-845f-1268e5828d43 | -11.90825 | -46.64953 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8422e448-484e-31ec-856a-d7a6bf76be4c | -10.06611 | -58.38875 | 2025-09-05 04:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f59824c-c57b-3e96-84cc-61527faaa78c | -11.99395 | -46.75388 | 2025-09-05 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4398a900-f14c-3e4e-9126-c8e02a679e1c | -11.92875 | -46.65621 | 2025-09-05 04:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0fdd7107-6673-3067-bc2a-b0a482af1e44 | -9.08004 | -47.01364 | 2025-09-05 04:36:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0314e698-33b2-3e22-97d3-db3c71544407 | -12.96167 | -48.05481 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15049b21-e02b-3ab2-a369-7247d796362a | -8.52416 | -51.32666 | 2025-09-05 04:36:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d7ff3916-3147-351a-8de9-8e703ac14f31 | -11.68681 | -52.20393 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba7e86a6-c3ce-3e15-9d69-2615f85c015b | -8.09038 | -45.47771 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03036e5e-31f0-300c-a760-eec23c31e1ee | -13.74418 | -46.93123 | 2025-09-05 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 50b0a842-7d23-3b8e-b78d-7c1d7b78020b | -12.49752 | -53.84791 | 2025-09-05 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f33fea24-d470-31bd-a548-eaaa59aa6165 | -8.36849 | -52.55818 | 2025-09-05 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c7e2975e-0fb8-3a55-bf2a-d738acc5e258 | -11.00509 | -45.92751 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd2d789e-2de3-3ea2-9112-f0c272cd9d2e | -7.68423 | -50.26455 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 7680ffae-616d-3998-bd38-c963e3dd1f69 | -13.47403 | -46.83566 | 2025-09-05 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b17f4960-a2d4-3466-9a2a-cad9707a5da3 | -7.72598 | -50.31463 | 2025-09-05 04:36:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ade80db-d4b6-3180-aa49-b35190a24228 | -12.97375 | -48.07116 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3aa0f5f0-7a4d-388c-9711-f80dac689826 | -10.97458 | -45.9604 | 2025-09-05 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a28dd0c9-8fa9-32b7-8b3d-94d4af3c10ce | -10.09825 | -48.07818 | 2025-09-05 04:36:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d8808187-b639-3bc7-b6bf-223147825e3b | -8.01833 | -45.40664 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d3768b5-03b7-3294-8b84-e803fb9a8fe2 | -11.39056 | -43.56034 | 2025-09-05 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5277ff88-eb47-3db3-8dac-dd8fd226ff42 | -9.98524 | -51.63166 | 2025-09-05 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 858b52f9-ba04-3c02-8bc0-7c76f51a3d31 | -9.07775 | -47.006 | 2025-09-05 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fcba3bf9-42fe-353d-9fe5-5c7189cef230 | -11.31363 | -55.22381 | 2025-09-05 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 22fbfa04-5e14-32b7-8ca4-e7cd2f06b742 | -12.48618 | -48.08809 | 2025-09-05 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2364c2a2-b035-3661-8c9b-40966f64b86c | -8.9094 | -45.86722 | 2025-09-05 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48f15bad-d886-31b5-ab7a-4298a1dd4c47 | -8.01947 | -45.42323 | 2025-09-05 04:36:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f573a97-ab3e-3d3d-ae78-335cd06867d1 | -8.48273 | -45.08536 | 2025-09-05 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 83c5fe9f-2aa5-3da4-86c0-39b9df042d24 | -8.55964 | -47.49279 | 2025-09-05 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README29.md)
