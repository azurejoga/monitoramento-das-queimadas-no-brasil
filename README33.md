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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64b42e73-b28d-3793-b63b-1368901fbb90 | -12.98715 | -56.89282 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df75450e-e968-39b2-9507-7d5b9160c29b | -18.28416 | -45.52217 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d24f9e1d-1dad-3d85-af04-fea4ff40e3a0 | -17.80362 | -44.31647 | 2025-08-22 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87ec5bec-0898-3140-b498-e27298d8e9cb | -20.43598 | -46.5033 | 2025-08-22 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64350259-d114-36fa-b349-84e219691a8b | -14.73546 | -56.038 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 484196d0-2fb6-3c11-aa35-a8e231c56b58 | -13.36299 | -46.26717 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d4c3235-1a66-3963-a742-3814c0f503c4 | -20.2392 | -46.60065 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64fbf46b-7c4a-3b7e-a2ed-d48b64be41ff | -17.14522 | -47.73348 | 2025-08-22 04:21:00 | NOAA-20 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0b67d5b7-c539-37cf-9819-e6206c96d264 | -13.03239 | -46.31845 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 55d6928e-2866-3e89-a1e9-6fcc17f5e026 | -20.33743 | -46.55405 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7beb3ff-24f9-30fa-b295-fa19051f4773 | -17.35027 | -48.16754 | 2025-08-22 04:21:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 215e7424-3754-3479-aa20-4f19d3377462 | -13.02688 | -45.19578 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5f4a099-40f1-312e-99ec-9ff31bcc7443 | -12.98622 | -56.90094 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dba037f5-e7a6-3bc7-9998-97863627bcb7 | -14.30576 | -47.07001 | 2025-08-22 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbcc29b8-d047-3e38-855b-0ef1ac421793 | -12.98791 | -56.89271 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f429b4e-2d90-3867-96c9-b9eb63455f85 | -14.35216 | -51.95866 | 2025-08-22 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f096938-f29b-3664-8d6c-a3ee72f6c5be | -13.64363 | -45.7092 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 908e4c7e-a5d0-313b-a1a1-981f7b341447 | -13.02857 | -45.20713 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f4ad270-2d79-3df2-937e-2e5e55a66853 | -15.8311 | -48.27179 | 2025-08-22 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b90145ce-e5ef-3e0c-b9de-1a0d5ac5ca60 | -20.30638 | -46.62325 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c98ea63-3d94-36a3-9188-2344ab3c0d71 | -13.64972 | -45.71385 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 156fa743-79d4-3b88-b621-5960c2242197 | -14.75715 | -56.03918 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e820fd4-191b-3852-a0e9-cf2902e2d1d1 | -13.00021 | -45.23584 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 96584048-c45c-339a-b503-0c57657c8359 | -13.36079 | -46.25957 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7cbaf554-f149-3cab-b9da-3c4f83807792 | -14.91295 | -49.45221 | 2025-08-22 04:21:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdf3c534-c82c-3c6a-bade-dabd39767b66 | -12.97983 | -56.89968 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a07844ae-f017-30d1-bb46-18e2bea08b11 | -11.90044 | -55.89834 | 2025-08-22 04:21:00 | NOAA-20 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31778688-124a-39c3-b625-2005e2daea2c | -13.64695 | -45.70974 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45f9f38e-63c9-3e91-9831-03a27377b453 | -15.55487 | -51.6974 | 2025-08-22 04:21:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 112e7ee4-5db7-3abf-a58f-a0635eddc8e1 | -20.25149 | -46.6566 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee98e035-33e7-3882-b7d6-ee6b5bea9626 | -13.14085 | -54.92327 | 2025-08-22 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27d515a5-b479-376c-897a-18803c64bf8f | -17.61307 | -46.69974 | 2025-08-22 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a83cb414-aaa9-36d5-a45f-86f318b90912 | -18.75019 | -43.85284 | 2025-08-22 04:21:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be46cb02-30f7-3e1f-8307-80d4543109ea | -16.5007 | -46.73875 | 2025-08-22 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1d1d7f2f-21fb-37c9-9ca6-256cf168aa1c | -13.38048 | -47.50116 | 2025-08-22 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5743c96e-b879-38a0-b309-061b2e5eeee3 | -14.7661 | -45.40214 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bafee0cf-606e-36bf-9ae3-2153cc2e9d39 | -13.14472 | -46.89513 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 958e179b-7c4a-3406-99f7-eb1fb0bb746c | -13.02968 | -45.19992 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04367383-cbe4-3212-b023-880e7270e56e | -12.95467 | -46.27319 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13592551-46fa-38c8-9975-7d934b2272a8 | -16.8148 | -49.28296 | 2025-08-22 04:21:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11ac4c59-179e-3195-b561-fc2a23e1c8f2 | -12.95245 | -46.2873 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 28463c6d-90de-3c5e-9445-9199bcc4758a | -15.59022 | -50.30757 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 255f775b-346a-3693-9f7e-562971d66135 | -12.98796 | -56.88876 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11876e39-a500-3717-bff1-55fd0da48652 | -12.92763 | -46.18536 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca14d5bf-e78a-37ab-8ede-3bfcf7dd45e1 | -19.93988 | -44.57365 | 2025-08-22 04:21:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| f7d82a0a-6175-3512-ad91-e9ca78f5fec9 | -16.78914 | -47.66443 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e2d29c63-11e8-31ca-bf5b-d9fe2a1ba7f5 | -14.87095 | -47.94586 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 609a6740-9d92-3944-b280-3dd66ebaf7ff | -12.96021 | -46.25961 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 432adb91-157c-3866-81cf-e835e400714a | -14.75189 | -56.03809 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0e9cbd89-4fe0-3e54-b768-3d86134a4293 | -15.15619 | -47.95313 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ea32eb07-cb2b-3870-8312-6efefe14f57a | -16.28584 | -48.73021 | 2025-08-22 04:21:00 | NOAA-20 | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca0b6d45-36ca-3505-9128-e387296e6af9 | -13.39015 | -46.24643 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3de4187-30f6-319a-ac7e-2d60d1fc0f56 | -17.67247 | -54.05087 | 2025-08-22 04:21:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb87f43f-be02-3bc5-9fb1-d7b6fee6c28d | -13.13968 | -46.90542 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 297edf44-fb6c-3045-bec3-df21af86126b | -13.02909 | -46.31791 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e40234a-5fb3-3512-a0d0-933ca330a3cb | -12.43018 | -48.70439 | 2025-08-22 04:21:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5344e8a4-4a36-367a-bbb0-e9f475d762d2 | -13.49378 | -47.04816 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 790bdac7-a47a-3ad0-aa50-63e092600dae | -13.7126 | -42.68811 | 2025-08-22 04:21:00 | NOAA-20 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 75db70b2-a095-34e3-890c-e2af75322998 | -14.64641 | -54.91294 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| aa34773f-afc1-3179-9693-befb194429d9 | -14.79326 | -59.6548 | 2025-08-22 04:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a611e36d-b04d-3167-90a0-ecc73b14554f | -19.71288 | -48.9805 | 2025-08-22 04:21:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 447e39ab-7334-35ff-bf71-d0a7984d9500 | -20.30301 | -46.6227 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dae7ecaf-e53a-3841-b399-b6fc768acf4f | -14.79208 | -59.66031 | 2025-08-22 04:21:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28954210-f485-38c5-abb0-7b67bc317d3f | -18.28261 | -49.61777 | 2025-08-22 04:21:00 | NOAA-20 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 06608a78-18e0-3e05-bc14-e08d6a455014 | -18.26645 | -45.52336 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 007e7ed3-c38f-362b-abac-8e173e15bf59 | -20.30525 | -46.63078 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e433bb6-7313-3818-be43-8ed1f960222a | -13.14918 | -46.88847 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 12f0a212-69f4-385e-9653-ca54e48145a1 | -15.63345 | -45.1512 | 2025-08-22 04:21:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1f3e278f-eb50-399e-a5e7-e37e7ca8083b | -16.78193 | -47.66688 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 69fd97cb-1b2a-3f9e-8156-cdc050696eef | -12.95525 | -46.24794 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 11773220-2da4-3917-90a5-3487f0db9e98 | -14.63314 | -54.85013 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7d6bda8-c8ce-3420-8305-295cf0fdf34b | -17.3951 | -44.25066 | 2025-08-22 04:21:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0fd6184-3092-3fa2-9dfc-ee0fdd57b36b | -20.30866 | -46.60794 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22f20f7f-f813-3bf2-89e2-8aa14dc6425a | -20.13507 | -47.46237 | 2025-08-22 04:21:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21049df1-b5e3-3d3f-b33c-87207832bbfc | -12.93812 | -46.18345 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2730c629-2850-31c9-91d5-c8bd16a82afd | -13.37988 | -47.50493 | 2025-08-22 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c31dc99-ed14-33eb-88b0-77d0592faf7e | -13.17251 | -46.91076 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62dc0c47-f4e6-3402-b4b4-43665016c1e0 | -12.50109 | -53.81143 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3a08b3b3-e5f1-31f8-a8d7-efca67742935 | -13.53374 | -47.03291 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c73cae50-61a2-30eb-8ec7-1a2ab8d41019 | -12.96352 | -46.26016 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f123d8a2-afef-332d-83e0-6c9b02aebf94 | -12.95854 | -46.2702 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64c46041-9f30-3fd5-ae5c-59fa1d63cd44 | -12.94969 | -46.28323 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7acd0ec2-0b63-3b9f-bc84-d15300029a2c | -16.52112 | -42.51627 | 2025-08-22 04:21:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b283ecf-813f-325c-a721-405536425e4f | -18.2887 | -49.60278 | 2025-08-22 04:21:00 | NOAA-20 | BOM JESUS DE GOIÁS | GOIÁS | Brasil | 5203500 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3b8debb6-5cac-3dea-abee-4613a70af993 | -16.61141 | -43.35803 | 2025-08-22 04:21:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 118db500-974a-3322-83ae-90811fa1280e | -13.03747 | -45.19375 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f158747-56e4-33b2-b818-6bfbf44b5f64 | -19.10475 | -52.86112 | 2025-08-22 04:21:00 | NOAA-20 | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17676c3a-6d5f-32d2-9334-297b0acce26d | -12.98958 | -56.88051 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f31f631a-6220-3cdc-9488-85ce4eafbfb9 | -19.67637 | -48.99304 | 2025-08-22 04:21:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 001fbf2d-7573-3ede-809e-4c9e7fd57ec0 | -13.48771 | -47.04347 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 531e85d1-4372-32f6-acd8-3bcce6bcc0e5 | -13.43092 | -57.16702 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea01e92b-1818-3175-b163-c24c40e4540e | -13.0235 | -45.17306 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57045741-9b1e-3cf7-9c8e-202b594c27e7 | -12.49066 | -53.8147 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7587996-68b6-35f7-87ab-52fb38dbe66e | -12.48592 | -53.81379 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11bcee2e-3094-362b-b70d-9f4040d2ba6e | -16.48134 | -45.09359 | 2025-08-22 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2d3ccaea-374a-306b-ba6f-ba25e8955c84 | -13.02964 | -45.17773 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c05db5e8-a503-3ac3-92c5-e0af9ccb25f8 | -14.516 | -47.85586 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| baff9859-a0b3-3525-a396-e87bb19a91f7 | -20.33684 | -46.55794 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9509b9af-e016-3779-812d-9916d8207ca2 | -12.95025 | -46.2797 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 745e1caf-b6f9-38a5-aca8-87adfb44c4bd | -15.5618 | -50.31998 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README34.md)
