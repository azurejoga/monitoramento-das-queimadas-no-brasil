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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c15f3590-0001-36fd-b6e0-e4c17660ef68 | -11.7687 | -47.0909 | 2026-07-28 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 911cc4c1-e442-36b8-b740-6d8a6daf773a | -20.7435 | -49.4197 | 2026-07-28 01:00:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 61.7 |
| fb4bc1dc-444a-384d-b5ae-9a93e0404b1a | -17.3034 | -42.6678 | 2026-07-28 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 9e5d37d7-1534-3240-a435-84369a1fc6ab | -14.288 | -58.9837 | 2026-07-28 01:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 98f80f4b-e2f0-3e6b-9f67-3f4231b32335 | -10.3825 | -49.5634 | 2026-07-28 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3219c02f-9466-376a-ac6f-a2c3138dcf9f | -16.4734 | -48.9957 | 2026-07-28 01:00:00 | GOES-19 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 140.8 |
| 21c3e63a-1bbc-34fc-b453-49b97e440f67 | -10.9588 | -43.0565 | 2026-07-28 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 1633c45a-4167-347a-9102-ef72e4c0c8c5 | -14.2691 | -58.9654 | 2026-07-28 01:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 83597621-d0b4-392c-b260-d48f0df5408d | -11.7879 | -47.0884 | 2026-07-28 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| fab2018d-9974-3a5f-98a7-b2772b983429 | -14.2885 | -58.9438 | 2026-07-28 01:00:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 39fa2fd0-3239-3f17-8dac-b379a4da1e79 | -13.3226 | -45.1013 | 2026-07-28 01:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| fff85d6d-8d10-3230-92b4-4b05ae9a2bb9 | -16.4537 | -48.9991 | 2026-07-28 01:00:00 | GOES-19 | GOIANÁPOLIS | GOIÁS | Brasil | 5208400 | 52 | 33 | nan | nan | nan | Cerrado | 182.7 |
| a668e76e-7569-36cc-a2d3-e901577afa5c | -20.7223 | -49.4471 | 2026-07-28 01:10:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 8a5b11a0-3166-3b49-873b-62b3be1c947d | -13.3028 | -45.1278 | 2026-07-28 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| cc3472bc-c32a-30be-aea0-c9c5946c44f9 | -10.3825 | -49.5634 | 2026-07-28 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 371b1b1a-1d03-30a7-8cef-655e6ef7706b | -10.9588 | -43.0565 | 2026-07-28 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 06971a20-4db5-315e-807b-122d8071a151 | -11.7882 | -47.0659 | 2026-07-28 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 44.1 |
| 7b9ac3ad-4391-3888-a338-2d5dc397e37d | -12.8543 | -44.386 | 2026-07-28 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 130.0 |
| 66772baf-c95c-3bd4-9c81-8f5453996964 | -14.3074 | -58.9621 | 2026-07-28 01:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 1d95cbb7-9f95-3bf7-8ca7-b617bd15de9c | -14.2885 | -58.9438 | 2026-07-28 01:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 089402fe-cd3d-3ea8-8d15-08e3d12ff55e | -20.723 | -49.4242 | 2026-07-28 01:10:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 193.1 |
| 2bae66fe-b4ad-35a8-aed9-8185bf964a1d | -14.2691 | -58.9654 | 2026-07-28 01:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 6d598f8e-6466-32fb-8269-a5c78bb7eaaf | -10.9397 | -43.0593 | 2026-07-28 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 5ead9752-7dd8-3c05-8696-ce4989599f92 | -11.7879 | -47.0884 | 2026-07-28 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 35a90047-bda4-3fdf-a877-2c6cb5eb661b | -14.2882 | -58.9638 | 2026-07-28 01:10:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 213.4 |
| f5b23faf-7193-363d-83b1-f051a9b6430c | -13.3032 | -45.1045 | 2026-07-28 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 208.9 |
| f5941cb8-c6da-3c12-aec1-37928722f436 | -10.3822 | -49.5849 | 2026-07-28 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 46cf01c0-46b8-3e72-91e6-dee805dbbd71 | -12.8349 | -44.3892 | 2026-07-28 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 404aecbb-0e60-3350-bd14-b0ce6be54ccc | -13.3226 | -45.1013 | 2026-07-28 01:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 870590e4-a5ff-3eed-8ac2-98d449f3c8b4 | -17.3235 | -42.663 | 2026-07-28 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 3fc8faa9-f628-3631-a237-06b4e5c46986 | -17.3034 | -42.6678 | 2026-07-28 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 730fae9d-4c24-366f-a862-5c50c68ceedd | -13.3032 | -45.1045 | 2026-07-28 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 1d4c1624-7060-3328-8a75-3866cb470b8e | -10.9588 | -43.0565 | 2026-07-28 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 702c61c3-bfcc-376a-b535-a9ea8edcfca9 | -17.3235 | -42.663 | 2026-07-28 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| b04b786c-e44a-390e-a2f6-800e11443bbf | -14.3074 | -58.9621 | 2026-07-28 01:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| bbbe1e89-6216-3f0e-b13c-231e70892048 | -14.2882 | -58.9638 | 2026-07-28 01:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| d18aabcd-ddaa-3b2b-a585-9b609d584949 | -20.7223 | -49.4471 | 2026-07-28 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 1355099f-ddd6-3b9f-9f47-7004cb0a1033 | -10.3825 | -49.5634 | 2026-07-28 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1eb93690-512a-3e2e-bc96-f0d1cb7c80b5 | -20.723 | -49.4242 | 2026-07-28 01:20:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 136.4 |
| 3b196e64-7837-38fe-bde2-2175059c461d | -12.8543 | -44.386 | 2026-07-28 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| a599015d-b687-3dd7-93e4-75ed9078abd2 | -17.3034 | -42.6678 | 2026-07-28 01:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0a3ed378-9ba6-3f75-973b-7da0626dab35 | -10.9397 | -43.0593 | 2026-07-28 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 150.7 |
| e8e439a4-0818-373e-8f8e-549bc19d87e1 | -13.3028 | -45.1278 | 2026-07-28 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 66.5 |
| ae3105fa-206f-3d83-a65e-0452f339a6ac | -10.3822 | -49.5849 | 2026-07-28 01:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.9 |
| eade9c38-1b62-353e-bdc2-8bf6bba09f70 | -13.3226 | -45.1013 | 2026-07-28 01:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 50.9 |
| edb8db37-9269-37ae-86a5-ec85b1b5647d | -10.9401 | -43.0355 | 2026-07-28 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 0e008728-1f15-3982-9e51-19f132ff8384 | -20.7429 | -49.4427 | 2026-07-28 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 3d888f5e-f05a-3b96-b655-47074cd71de7 | -20.7435 | -49.4197 | 2026-07-28 01:20:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 76.8 |
| f1bc8665-673e-36bd-8b8d-f87bb25ed694 | -17.3034 | -42.6678 | 2026-07-28 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a06e91f4-9c4f-31f3-865a-32dbf33f5889 | -17.3235 | -42.663 | 2026-07-28 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.0 |
| db497c4d-9414-38f1-85c3-3966acd65e61 | -14.2882 | -58.9638 | 2026-07-28 01:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| fb3463fd-a81a-3500-9673-d00f04c89b77 | -10.9401 | -43.0355 | 2026-07-28 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 6558a9c9-cf8f-351b-952d-f2701e34f7a0 | -20.7223 | -49.4471 | 2026-07-28 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 4ef23927-adb3-3c9e-a635-f033b1e93d35 | -20.7435 | -49.4197 | 2026-07-28 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 1eb164ba-3493-3f59-bb72-d3d278a01b37 | -10.9588 | -43.0565 | 2026-07-28 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 84a7ab2e-11a5-3315-9dfa-df7cc66b1795 | -14.3074 | -58.9621 | 2026-07-28 01:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 44281563-2bc2-3fa0-8578-4b131a83a480 | -12.8349 | -44.3892 | 2026-07-28 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 4b780cfe-fd12-30b6-9fa5-0ee87e4a147b | -12.8543 | -44.386 | 2026-07-28 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| b917af00-77b5-3a5e-9a8f-f697953041f7 | -10.3822 | -49.5849 | 2026-07-28 01:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 50fbbaa3-9436-3889-97e6-43ef19d02859 | -20.7429 | -49.4427 | 2026-07-28 01:30:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d9228447-9001-32c7-847f-41d140c95b85 | -13.3032 | -45.1045 | 2026-07-28 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 9b86f6c8-26d5-376e-8234-676b4d94af44 | -13.3028 | -45.1278 | 2026-07-28 01:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 56c27c67-7821-3e6a-9ffe-cca8bbe323cc | -20.723 | -49.4242 | 2026-07-28 01:30:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 4a1460e1-36ea-33a6-b3fc-38ca4725d5f4 | -10.9397 | -43.0593 | 2026-07-28 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 234.3 |
| bf76eb39-a608-3a86-9da4-8e377cb581c4 | -14.3072 | -58.982 | 2026-07-28 01:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 635e77ab-9b34-39a8-b837-a8502c39e4e5 | -14.3266 | -58.9604 | 2026-07-28 01:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 87c6fd5f-8974-36c3-9b22-e5e48c8b730c | -11.9868 | -45.5417 | 2026-07-28 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 32f3613e-08e0-3304-a4fc-44adf18f941f | -13.3032 | -45.1045 | 2026-07-28 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 53a297d0-629c-3577-9635-2d39d86bfa27 | -17.3235 | -42.663 | 2026-07-28 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| ab037443-1488-336c-9805-5c1fefbf5b84 | -12.8543 | -44.386 | 2026-07-28 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 15ac0d4c-499c-3755-9fbf-8fc24f6463d6 | -20.7223 | -49.4471 | 2026-07-28 01:40:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 21ad5368-e2d7-361f-85ea-8c0cf9c88a71 | -13.3037 | -45.0812 | 2026-07-28 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 38d262e3-f3aa-36ac-9508-736d983cce6a | -10.9397 | -43.0593 | 2026-07-28 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 273.1 |
| 58130b95-674b-38af-be47-bf39ed37fc9e | -10.3822 | -49.5849 | 2026-07-28 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| dad40c8f-76dc-34ab-b427-63f2535eacd9 | -13.3226 | -45.1013 | 2026-07-28 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 61121b4d-b0cb-336a-80fa-ea73040d6f32 | -20.723 | -49.4242 | 2026-07-28 01:40:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 150.3 |
| db127c6b-d1fd-3f2e-9517-375bbf7bfda0 | -17.3034 | -42.6678 | 2026-07-28 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 2de432f9-27d2-3a09-9e64-46163d4d401b | -10.9588 | -43.0565 | 2026-07-28 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 8d564a46-28e3-3a35-b6d2-6c5399577506 | -10.9401 | -43.0355 | 2026-07-28 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 75099c5b-8cf3-3574-bdb2-a49a7ae5290f | -13.2838 | -45.1077 | 2026-07-28 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 4b8c2698-e27e-3176-a0a3-605439f5ad3c | -11.7687 | -47.0909 | 2026-07-28 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| cbbd5719-0205-39ea-9deb-e79c5ab34bbc | -13.3028 | -45.1278 | 2026-07-28 01:40:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 49.5 |
| c96dbe08-e893-3c88-bcce-29f3b9327e30 | -11.9676 | -45.5445 | 2026-07-28 01:40:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 59.9 |
| c6fb4fcc-4d3e-35c5-b5a5-3a556ed80b8a | -11.7879 | -47.0884 | 2026-07-28 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d8c3a515-019c-393e-9240-a4cf24a7f697 | -14.3074 | -58.9621 | 2026-07-28 01:40:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 53e78cfc-f494-3ac8-b421-cb1fb281d5d4 | -10.9397 | -43.0593 | 2026-07-28 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 309.3 |
| 3138bd67-88bf-3a07-a022-9bfda158c5b8 | -13.3028 | -45.1278 | 2026-07-28 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 44cce954-b2ea-36b5-b33e-95429363c6cf | -10.3822 | -49.5849 | 2026-07-28 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| c5ad8006-2e72-3d83-a57d-42b589ad2fc6 | -10.9401 | -43.0355 | 2026-07-28 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 8b244177-39f6-32e9-8d67-72ded44ee162 | -20.723 | -49.4242 | 2026-07-28 01:50:00 | GOES-19 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 2b766384-c14f-3cbe-b187-2680c443b9c6 | -20.7223 | -49.4471 | 2026-07-28 01:50:00 | GOES-19 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Cerrado | 106.4 |
| a5d4428c-26fa-3b4f-90ee-f2c17ca59878 | -11.7687 | -47.0909 | 2026-07-28 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 2b6223f1-2b67-36fe-b967-a95b486783f4 | -12.8543 | -44.386 | 2026-07-28 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 282828f5-0f74-3135-9072-0b5a97b3b3bd | -13.2838 | -45.1077 | 2026-07-28 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 466f033e-89ac-3bab-a02d-bdc434ea5521 | -10.9588 | -43.0565 | 2026-07-28 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| e0858250-9ba6-3292-9c46-8a4cb197d95f | -13.3226 | -45.1013 | 2026-07-28 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 5e248d31-a408-39b1-8336-de01621065bc | -17.3235 | -42.663 | 2026-07-28 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 93.1 |
| a65d5360-93e5-30d4-af06-2517074e9f7f | -13.3037 | -45.0812 | 2026-07-28 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 416d954a-3870-3cc1-9932-006580577d9a | -14.3074 | -58.9621 | 2026-07-28 01:50:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 2ebdd55f-1101-3449-9598-7056d46ac0f2 | -13.3032 | -45.1045 | 2026-07-28 01:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |


[Clique aqui para ver as próximas entradas](README7.md)
