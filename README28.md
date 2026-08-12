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
| c251f616-a7d1-3708-9490-dd9f08ac8f24 | -11.81211 | -51.88548 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5437cfe3-b124-36d2-b2e2-5929250be7c3 | -7.91379 | -45.11356 | 2026-08-12 05:10:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2fe0dc8-488a-3271-9146-e42ed43ebaec | -9.3651 | -47.45215 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b33423a6-5712-3afd-b59f-7ebf0dbbb97b | -6.54014 | -43.12857 | 2026-08-12 05:10:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| bf764462-ed33-3dc2-abb6-d0ff586546df | -8.95428 | -60.50433 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82c01bc8-f9cb-35cb-9033-4804179b0c83 | -8.9511 | -60.57016 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bd4aeb99-5c30-3b69-b564-867d520f447a | -8.36206 | -47.75362 | 2026-08-12 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f262dff5-03a6-3456-a8f2-c98d8f95caed | -7.41675 | -60.00103 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63a23a57-3892-3208-a06d-fb175bffe55b | -12.14269 | -48.26985 | 2026-08-12 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5753d44-a5b5-34ca-bd95-f8e0afb56dc2 | -7.41503 | -60.00363 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 893a4d0e-09c0-3d5f-bf45-90d24aa1417f | -9.327 | -47.53539 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8537a7de-8bb5-39b3-b983-43c8c50caffa | -6.5477 | -43.12366 | 2026-08-12 05:10:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 94f56659-cc7e-3e57-8728-5a9f92ef0b76 | -9.76094 | -60.76404 | 2026-08-12 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1c97bdf-c510-3d10-9f62-54635f42c547 | -8.94976 | -60.50827 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a2e8a674-10c5-3501-a681-011ce616cd03 | -8.35712 | -45.98439 | 2026-08-12 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5355a52f-5a69-37af-a4fd-42ce9832a6b9 | -11.61174 | -54.6543 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1b973fb7-f02f-3792-bd4a-2cb8bdc70398 | -6.60952 | -59.00289 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59af5363-48ce-3acb-8ee1-68f7ef842924 | -8.94224 | -60.50699 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df6d2547-598f-3c4c-87fe-d40dfb1e63f4 | -11.82432 | -51.85207 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a796b8bd-de80-3607-a299-1e3ea03f2be6 | -12.18306 | -50.15315 | 2026-08-12 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| af6e6dc8-2aeb-3041-93a8-5f7364d9535d | -8.96179 | -60.50565 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d850128-73f5-3558-b374-0e28c01e0888 | -8.0733 | -46.52126 | 2026-08-12 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b1b56e7d-e3c0-36c9-bad2-3afcff35d33b | -11.78815 | -51.84787 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9820078b-98f1-349c-b182-2510937d09f8 | -5.67957 | -49.82354 | 2026-08-12 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d3e8c67-15dc-301d-8ac5-e5cfe8562e4b | -6.0106 | -47.41187 | 2026-08-12 05:10:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 920802db-f3c5-33dd-bb98-e763b581217b | -8.9571 | -60.53604 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8775f573-dad8-3e50-8573-b68c1702a1e3 | -8.90271 | -60.58092 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05820678-1482-3d12-a1c5-8f955b7145a9 | -8.95829 | -60.57423 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4a66f54-de6a-3f67-b08d-699caf3bb8d4 | -9.76548 | -60.76007 | 2026-08-12 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66defba6-305a-30ee-b637-f564fd425676 | -7.38231 | -45.11188 | 2026-08-12 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c64c424-6f2e-3f0d-bea8-451bbae8da32 | -10.36758 | -46.38617 | 2026-08-12 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| dcd7150d-38ac-3e75-8d6f-7fe0d8a62491 | -8.95188 | -60.56547 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d38a9a8-3477-3533-b55d-591dfa54d67e | -8.89828 | -60.56115 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 85804467-c46f-39f5-9002-c791f8e6f922 | -11.94312 | -46.33315 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c5d7a9d9-c2f2-362d-949a-f0a8d6f4cc4a | -12.03386 | -47.80194 | 2026-08-12 05:10:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fae8349-11c5-3c08-9e9d-4b79cd1ed422 | -4.45622 | -55.66241 | 2026-08-12 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 701b1489-34ce-34e3-9025-5f046d84609d | -8.89594 | -60.57498 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dac925c-4c99-313f-a9c6-11b0878e1ac8 | -11.9817 | -46.36372 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23fe105f-cbc3-3d9f-baa2-3f39862e3d55 | -7.68675 | -55.16269 | 2026-08-12 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1cfb05f-7270-3491-b8a8-da42a79dec9c | -6.59079 | -59.01333 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 759e7adb-4480-33a7-a66d-0e17ce4201e5 | -2.94531 | -60.92617 | 2026-08-12 05:10:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14f6a452-0c1a-3843-95fc-52a9541d8434 | -6.84783 | -59.09915 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 980a0cbc-4f45-31c5-a2a0-9b5ae5847de9 | -9.75794 | -60.75875 | 2026-08-12 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92da1133-96ba-36d0-abb2-5616455287e0 | -8.95257 | -60.58472 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef5561f8-5a29-38ab-9f92-91307f4cad1d | -9.34068 | -47.51366 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b0f8603a-505a-3999-9af3-33e9fc2686a3 | -11.4672 | -46.61247 | 2026-08-12 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce73397a-0ffb-318e-be40-f9493b1f2946 | -9.75937 | -60.77336 | 2026-08-12 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07e2441e-8333-35bd-a06c-159a67742db3 | -11.46385 | -44.55531 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c5119d67-112d-3c98-97e4-6cb7ab206af4 | -8.95532 | -60.56894 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf71b274-7756-3ea1-a810-b5fcfb18b5f7 | -11.95424 | -46.39121 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 36f866ee-44dd-3843-a6dc-a12526f7f951 | -8.96185 | -60.50851 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43e1cf17-cd01-352b-8ecd-3da2ed737c9f | -12.18243 | -50.15802 | 2026-08-12 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a7d0d0b-6883-34f2-8bce-3998ae02362b | -11.60705 | -54.66166 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68aabf70-b16a-3af6-a321-a16ac07c313e | -11.49005 | -54.60028 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47bb8b29-da5c-3aba-be96-d35ab862c00d | -11.60415 | -54.65717 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c4ddd4a-b011-34ec-a578-625c138e2e0e | -7.41203 | -59.99855 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3759675a-8fb4-303b-9289-1ff3b79e7aba | -8.60071 | -45.41237 | 2026-08-12 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a286b729-48b9-3b4e-8964-bc5f0982403d | -8.95723 | -60.53321 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0c2db8db-7484-3a5b-a204-d15031c3151b | -11.97201 | -46.39367 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 805c3fcf-25d2-3d65-97b4-f63e01f0e7bf | -8.98425 | -60.53589 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f817745-8a9d-3e87-8271-7e8f24d02fd2 | -8.9579 | -60.53143 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f9ed9492-2c77-3ce8-8823-4e249a95d03b | -9.47248 | -60.51759 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 03c353f5-1f68-3013-b71a-4454cda4e64a | -11.81738 | -51.84839 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f1508cf-026e-36f2-ba81-d1291218edf6 | -9.6202 | -48.33128 | 2026-08-12 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c9c6be6-7d5c-3ee5-a9f4-c0af7636c387 | -11.92781 | -47.38219 | 2026-08-12 05:10:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afec2e3a-4ed3-3f95-a7c0-fb0097f08db3 | -8.9467 | -60.52667 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8d7f161c-3ea3-3bd0-88c4-2d2989ac56e7 | -9.51877 | -47.42927 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f332477-77f5-3fea-8533-d369f82d9f99 | -9.12972 | -46.39788 | 2026-08-12 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 09ebcd2a-e790-365a-9dd3-bd21152e12cd | -11.47615 | -44.57792 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| abd48b2d-ffa1-3f48-a341-5f47e4de7da0 | -7.00224 | -44.83074 | 2026-08-12 05:10:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 87667bee-8914-33af-94b4-8fd59d214327 | -6.96976 | -58.99652 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2adce836-742a-3be4-a3d6-3774e2e0a3a4 | -11.98452 | -46.36768 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4890775d-3b60-3805-a9bd-9b8c79d500db | -9.47558 | -47.82929 | 2026-08-12 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fff5e2ca-18e2-3dc6-9580-3aa7d6b49f95 | -11.95429 | -46.34078 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 45b42534-a5b7-34c3-9ba7-c7499fd075ce | -8.95352 | -60.50891 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 88e74a14-f977-38e2-90b7-9ad85cfa3a70 | -10.36278 | -46.37742 | 2026-08-12 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dfcec262-aef8-3d09-90d5-5e321636b6f6 | -11.47305 | -46.61294 | 2026-08-12 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4449cfd6-e45a-30da-a89b-d6f801717e66 | -6.60709 | -59.00335 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e0713a03-5ded-3d8d-a6ed-a05548620118 | -6.54852 | -43.11762 | 2026-08-12 05:10:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 716c0a3e-bc84-35cd-8539-3182e5824af4 | -11.60593 | -54.64534 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 979add60-659b-3b17-9b7d-262e6ae49b2c | -11.49996 | -54.60581 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a841ce0d-f74f-39a2-a511-c5f41ed7d065 | -11.95299 | -46.3516 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4f730976-9188-33ea-b631-233d6e562ab6 | -8.89971 | -60.57566 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41a4429d-87b9-3b5c-b531-770096942002 | -6.99802 | -42.6441 | 2026-08-12 05:10:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a9d04310-aecd-3e00-a519-5665a315082e | -6.34238 | -44.05964 | 2026-08-12 05:10:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d357565c-b422-3cf1-a702-78c83d5ae498 | -9.76171 | -60.75941 | 2026-08-12 05:10:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 350c7096-50f5-3648-8fbc-b086e064026b | -11.48343 | -44.57295 | 2026-08-12 05:10:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 70006059-c675-3b8c-a859-1b01876423fc | -9.62521 | -48.33223 | 2026-08-12 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d22384a-55ac-35be-8525-acc42d06a289 | -8.94752 | -60.4985 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1fd082a-2649-3f7f-91fe-a255fac9a824 | -8.95551 | -60.54529 | 2026-08-12 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 09432e6d-1da1-34d7-8b1a-3633b78948b9 | -7.41302 | -60.0004 | 2026-08-12 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 15f05d7d-9725-3411-a87f-58101d066db4 | -9.90368 | -60.26991 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ca0a2e1-ffdd-37d6-86ed-08f6190088d5 | -7.72174 | -46.21834 | 2026-08-12 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e89753d-325d-3146-b266-1115f11c9b83 | -11.82843 | -51.85266 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f35841b5-9bde-3ef5-954a-449cba3f13a3 | -11.94891 | -46.33519 | 2026-08-12 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 62dca9f4-149c-33e2-9228-f6d21af404ec | -11.84077 | -51.88486 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4abefbc4-152e-3b9a-9a1e-7c6b2ea69d2d | -9.72032 | -60.20141 | 2026-08-12 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4840a174-e279-312b-8ee1-076bbc3102e0 | -11.81265 | -51.88173 | 2026-08-12 05:10:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da600753-f01a-38ad-9001-0df465fbde3d | -12.6085 | -47.86522 | 2026-08-12 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 718f9185-d55c-383b-be21-308b8867703d | -11.49528 | -54.61319 | 2026-08-12 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
