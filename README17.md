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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8e46d09-2af5-3595-9620-825c5fb9469a | -11.0942 | -51.4711 | 2025-09-13 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 87a3e1c1-39f4-3ffa-8cb7-5f0a647cf637 | -9.5324 | -54.6277 | 2025-09-13 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| cc148e5f-07b8-30dd-b97a-c58cacafdfb9 | -9.5135 | -54.6494 | 2025-09-13 02:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 8b9b94c7-a218-3465-a4ad-7437e5f8b3f3 | -3.2305 | -47.135 | 2025-09-13 02:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| ed99844b-f08d-39b5-9128-32315fdabf09 | -11.1508 | -51.4863 | 2025-09-13 02:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e9012b24-ccf4-3c52-af03-8250cccb2b4c | -15.2526 | -51.4036 | 2025-09-13 02:50:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 552fde15-9f80-3240-9dba-cbc0bda53530 | -16.1001 | -49.9457 | 2025-09-13 02:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 5132bc61-a96b-3fb5-8490-8c41f63cb37a | -11.8281 | -50.562 | 2025-09-13 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 581cfbad-0d77-3b01-bee7-574a3adb52e6 | -11.8659 | -50.5791 | 2025-09-13 02:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 9c04b866-25e3-3ac0-9755-df77fe453161 | -11.7388 | -46.6005 | 2025-09-13 02:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| ae67ec1c-7bb5-32a3-97bc-42957f03d2c5 | -11.4306 | -45.6215 | 2025-09-13 02:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 34.2 |
| e994c6ec-93ec-3bc6-8e04-c6e386594e1a | -11.4076 | -50.7378 | 2025-09-13 02:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.9 |
| dfa0df96-47ee-32d3-9367-0a970836d266 | -21.6187 | -46.8115 | 2025-09-13 02:50:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| 1a9cb9ba-4ad8-3397-83ee-06768a875ca6 | -3.2507 | -46.7829 | 2025-09-13 02:50:00 | GOES-19 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 78c1901e-e6ab-379a-903b-8edb1ae29a5a | -3.2305 | -47.135 | 2025-09-13 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f189331c-3124-34b2-a99d-4e563d9c31c6 | -9.2844 | -59.3986 | 2025-09-13 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| f409a285-3f69-3b3f-b229-d9d8edb1ca9e | -9.2503 | -51.2472 | 2025-09-13 03:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 51e3941f-f4ca-3814-90e5-d44eb49d47a5 | -12.006 | -47.7505 | 2025-09-13 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1dcb4605-707a-365d-8b78-7f7307a34d7a | -9.5006 | -55.9588 | 2025-09-13 03:00:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 73708f95-ff63-3c2f-a0f8-538fe673797e | -11.8472 | -50.5598 | 2025-09-13 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 155.4 |
| ca5facda-645f-3ad5-8e92-c518e3246f63 | -9.2656 | -59.4191 | 2025-09-13 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 185.4 |
| ba143b62-55a7-30ff-b717-6e74fc3ffefb | -11.8659 | -50.5791 | 2025-09-13 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 56221589-f393-3f00-a61d-0bfe8ef55d4b | -16.1001 | -49.9457 | 2025-09-13 03:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3ce0c899-6959-3bb0-9335-dc334c9ff249 | -11.8281 | -50.562 | 2025-09-13 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 73190739-a6aa-3093-90a9-228cdbb80cd3 | -11.7384 | -46.6231 | 2025-09-13 03:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| da362191-42c7-38ec-8a2c-afd1f893b067 | -11.431 | -45.5985 | 2025-09-13 03:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 48ed2a21-762e-37dd-899a-4ad5fcc05ce8 | -16.3418 | -51.5434 | 2025-09-13 03:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 117.4 |
| 8dfce1a9-40db-3736-b695-c56df04f5a43 | -16.0805 | -49.9489 | 2025-09-13 03:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 5f1becbf-44b5-34e4-a2c1-f78d421d2f1a | -10.6583 | -46.2468 | 2025-09-13 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 089db1e0-154d-31e5-9648-5df95cb2accc | -9.5324 | -54.6277 | 2025-09-13 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 208.0 |
| 4436a2ce-d95d-3288-b44c-a2c57b9d4c46 | -9.9765 | -50.2907 | 2025-09-13 03:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| dfbc8c32-e632-3047-bda5-2e9ecc0c96d2 | -15.2526 | -51.4036 | 2025-09-13 03:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 403a14f8-2ae4-387c-b7ec-27d2c2830665 | -13.0891 | -48.2663 | 2025-09-13 03:00:00 | GOES-19 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3e519461-ec94-3386-8d4a-7994db18c00d | -8.1004 | -50.1821 | 2025-09-13 03:00:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 75eaa1a9-e62c-30af-b363-44b30b39deed | -12.0056 | -47.7728 | 2025-09-13 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 1d6ead09-bfec-3d77-9c8b-2099ab3cb42b | 0.6904 | -50.6481 | 2025-09-13 03:00:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 9739d18a-360d-3775-89b8-eaaf1f87ec58 | -11.7388 | -46.6005 | 2025-09-13 03:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 23a57578-b09d-3770-bced-22c03db89c6f | -15.1165 | -52.4918 | 2025-09-13 03:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| eaae5ce1-b24a-30ec-b332-e6ab9ad3bbaa | -15.253 | -51.382 | 2025-09-13 03:00:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 3d0bda38-968f-34e9-97a7-d7f7fe9cdd9b | -3.2321 | -46.7836 | 2025-09-13 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 9b0ff25f-06d2-39c0-8073-4a67fcbdc5d7 | -15.2036 | -56.6803 | 2025-09-13 03:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| a35028a2-0b87-31d8-9748-e50f451391e9 | -11.8468 | -50.5813 | 2025-09-13 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 186.2 |
| 9f331dab-a51a-3183-af53-503633c8f600 | -11.9869 | -47.7531 | 2025-09-13 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 2cf5f02e-025f-343b-ab3f-e604eb115168 | -16.08 | -49.9709 | 2025-09-13 03:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 36.7 |
| a03c4e3c-76ff-3324-8e71-583800621346 | -9.2472 | -59.4007 | 2025-09-13 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 9ef4cd19-1258-39fa-a1a3-88a333bf5875 | -9.5135 | -54.6494 | 2025-09-13 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 030e9506-e475-318a-a0ea-3e1d5fcfed3d | -21.5912 | -48.419 | 2025-09-13 03:00:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 81036a51-4eb9-3d72-88c0-0f8e09612577 | -9.2658 | -59.3997 | 2025-09-13 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 160.7 |
| add74036-eef5-30f0-bedd-d8e66e813e17 | -11.9865 | -47.7754 | 2025-09-13 03:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| e1a877f0-676f-3179-8b75-6756643081c3 | -3.2282 | -47.6371 | 2025-09-13 03:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 6db286a8-89bb-36b1-a645-3216b914a3a7 | -9.2843 | -59.418 | 2025-09-13 03:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 25b68afc-2761-39d2-adbc-afee46d4c1b5 | -21.6187 | -46.8115 | 2025-09-13 03:00:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.6 |
| 67d8278b-6885-335f-8180-4b901451dc07 | -15.2229 | -56.6782 | 2025-09-13 03:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| f7643897-c9be-3a1e-a196-26fd743c6666 | -10.6579 | -46.2694 | 2025-09-13 03:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 88c0d3a6-4efe-34c1-8416-3569681b543c | -9.5322 | -54.648 | 2025-09-13 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9c217286-015c-3743-b3c1-0ccd2ab16a3f | -9.5326 | -54.6075 | 2025-09-13 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 4978aa7a-9678-3adb-b2a9-d578128862a3 | -9.5137 | -54.6292 | 2025-09-13 03:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 206.5 |
| 34f1f03a-3c42-3073-9004-08a9e2732772 | -16.3422 | -51.5217 | 2025-09-13 03:00:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 2ea35955-c76d-3dfc-8fe4-87e5592a640a | -11.8278 | -50.5835 | 2025-09-13 03:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| bceea66d-43a4-3d34-96d5-2270dd1d20ac | -11.4076 | -50.7378 | 2025-09-13 03:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 8decb7b2-1d2b-32c7-93da-9daaf1634817 | -9.5139 | -54.6089 | 2025-09-13 03:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| cc915c67-21fd-371a-8c4b-2ee52705b559 | -15.1161 | -52.5131 | 2025-09-13 03:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 259a59c7-f22b-38e5-ac89-09c347ef89c0 | -3.2282 | -47.6371 | 2025-09-13 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c31b448d-ce95-3277-9903-d67a94f373a7 | -9.5004 | -55.9788 | 2025-09-13 03:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 94d80c96-a81c-343b-891a-514a73ba1d20 | -9.2658 | -59.3997 | 2025-09-13 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 201.0 |
| 86722fdb-2867-3d67-9354-0a8a298fdcd9 | -9.5324 | -54.6277 | 2025-09-13 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 279.9 |
| a04efc82-9ae3-3c49-8ad3-ff0488c805e1 | -16.0805 | -49.9489 | 2025-09-13 03:10:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 089f180e-be7e-3f64-b6e3-c79a3dbd687c | -9.5139 | -54.6089 | 2025-09-13 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| e1945d14-4fa6-3001-ae26-d51ae3474394 | -15.2229 | -56.6782 | 2025-09-13 03:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 123.6 |
| a028a15e-0611-3cb1-98c9-a46e31147977 | -9.5326 | -54.6075 | 2025-09-13 03:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 109.7 |
| d6c52c50-2ad2-3c5b-a224-25f40f13b6de | -16.3418 | -51.5434 | 2025-09-13 03:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 95fc4598-6ad4-3787-b548-a893a6d2f1f6 | -3.2305 | -47.135 | 2025-09-13 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| ea6ab2f6-7b78-3d1a-bdac-0caab3e8cef2 | -9.5006 | -55.9588 | 2025-09-13 03:10:00 | GOES-19 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 9f2cc558-0c8e-3195-b005-b432a50bacde | -11.8472 | -50.5598 | 2025-09-13 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| c2db54c9-9da9-3c98-a2cf-3952c821cd69 | -21.6395 | -46.8061 | 2025-09-13 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.0 |
| 978bd7ad-94f1-37d2-92d5-27043740ac12 | -9.2844 | -59.3986 | 2025-09-13 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 3e6cc01d-9f11-375e-86ba-2a41eed0b148 | -9.5137 | -54.6292 | 2025-09-13 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 203.6 |
| bb246d44-d93c-3e0a-a5ce-82e0ac795f42 | -21.6187 | -46.8115 | 2025-09-13 03:10:00 | GOES-19 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.8 |
| 03e08f81-beb0-3676-af00-ccb106bdfc1d | -15.2036 | -56.6803 | 2025-09-13 03:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 209.4 |
| 5d9e5088-de19-3c09-8b49-b180c074a2e8 | -9.2843 | -59.418 | 2025-09-13 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.6 |
| a8f3cb14-2777-36d0-a4e7-9fd4f7bcddaa | -15.2033 | -56.7007 | 2025-09-13 03:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 9874668f-306d-34b3-bd8c-ab729b24b9df | -11.8281 | -50.562 | 2025-09-13 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 7cfae925-e2d3-3eaf-a46e-977f7f8a028c | -11.8468 | -50.5813 | 2025-09-13 03:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| ca36c5e9-9a3a-34aa-9f84-d8dc4634d846 | -8.1004 | -50.1821 | 2025-09-13 03:10:00 | GOES-19 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d8015767-4fb7-36d6-a869-a1ecb246e4e3 | -9.5135 | -54.6494 | 2025-09-13 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| e8858438-bbbd-3ecc-91fa-7400b8876443 | -21.5912 | -48.419 | 2025-09-13 03:10:00 | GOES-19 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 5bb9cab2-2584-3dc2-a413-636fae6e59c6 | -16.3422 | -51.5217 | 2025-09-13 03:10:00 | GOES-19 | ARENÓPOLIS | GOIÁS | Brasil | 5202353 | 52 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 113b10ca-7d23-3eb8-a826-bdc204680964 | -9.2656 | -59.4191 | 2025-09-13 03:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 195.6 |
| bd0e4585-0c7a-3ebc-8330-eeadda3871a9 | -9.5322 | -54.648 | 2025-09-13 03:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 9a4f978e-6809-3428-92e8-7265095fae4b | -9.2503 | -51.2472 | 2025-09-13 03:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 9e69b318-1f48-350e-acd5-67b669b742f0 | -15.1165 | -52.4918 | 2025-09-13 03:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 28b54c20-679f-3fba-9db9-95e92940de8a | 0.6904 | -50.6481 | 2025-09-13 03:10:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 39bed149-4fca-39e8-a836-be720051b8bc | -3.2321 | -46.7836 | 2025-09-13 03:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 16e47206-c171-333c-9e22-ee4e883e9e5c | -4.93991 | -37.93581 | 2025-09-13 03:15:00 | NOAA-21 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b2051796-63dd-3397-8854-fbb3b39045bb | -6.51248 | -35.12635 | 2025-09-13 03:15:00 | NOAA-21 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c2e7a895-ff9e-338f-8866-f2159333c2fe | -5.58844 | -35.71838 | 2025-09-13 03:15:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5e8332b4-979b-38c8-91b6-4e75611a71c5 | -7.55992 | -42.64161 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ff8665ac-25db-39f2-8245-bf310121affc | -11.44934 | -43.56991 | 2025-09-13 03:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb8099f5-885a-36d1-ba3f-a795839cf2c6 | -7.56563 | -42.64917 | 2025-09-13 03:17:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f4ef4cbe-b6dc-374f-9475-e6b488e5c9ca | -10.76647 | -41.33719 | 2025-09-13 03:17:00 | NOAA-21 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |


[Clique aqui para ver as próximas entradas](README18.md)
