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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5b181c8-f5f3-3848-a7c4-8d8b4219f396 | -16.18263 | -57.45073 | 2026-05-08 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cca5f3f3-9c48-3567-8212-e7dc7f5b643a | -21.70974 | -48.42162 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58a4311f-9e16-3c8e-afaf-8291a21e7bd0 | -21.70927 | -48.42127 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5411bc5d-4255-3691-a823-a9064b81c237 | -16.42597 | -52.79597 | 2026-05-08 05:10:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cc92fe35-649d-3885-8be6-e4f0ee9b51c4 | -20.72227 | -55.17159 | 2026-05-08 05:10:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a5570499-4f54-34fb-afe0-f91ebbadcfac | -16.1611 | -58.48884 | 2026-05-08 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| cfbbae8b-2cb9-32ba-a02e-96c4bb56de06 | -20.72436 | -55.17452 | 2026-05-08 05:10:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07e011b8-5f4f-369c-a4c9-e626a759c447 | -21.37985 | -48.54647 | 2026-05-08 05:10:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e58c4b2e-65cf-3597-8ecf-4aa3d47695af | -18.43797 | -54.70778 | 2026-05-08 05:10:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae6197bb-35e1-3c2d-88bf-1789bab8d076 | -21.70435 | -48.41681 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69bc3af0-c885-33b2-9450-3ec7d9a6dc0a | -16.6018 | -58.23907 | 2026-05-08 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c935b6ed-2d0f-3688-a319-92eb8b3c4d23 | -18.50822 | -55.50772 | 2026-05-08 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| f48563ab-3a12-375e-a490-8cc3e0d28059 | -17.94391 | -52.96114 | 2026-05-08 05:10:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 488e0844-8a69-343b-a77f-0d5dca7b8dd3 | -20.72165 | -55.17625 | 2026-05-08 05:10:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 255a9c98-4f35-3203-865d-e3416943acb9 | -18.49872 | -55.49755 | 2026-05-08 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 09c93bca-3861-3020-a038-8309770d0974 | -20.22062 | -46.84132 | 2026-05-08 05:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0bc4b40b-a98f-3b0e-bfa8-60ed895f7ba2 | -21.69814 | -48.41586 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 849924b6-300c-3d74-8842-d08ce84b0f44 | -16.165 | -58.48582 | 2026-05-08 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 3c1de470-251a-3033-be50-1793e628a7d9 | -18.24949 | -51.26244 | 2026-05-08 05:10:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8083f82a-226d-3f93-8740-aa88c6a070e4 | -18.50933 | -55.51495 | 2026-05-08 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ffec5ab0-ce6a-3960-b21a-4d4ec2e71d26 | -19.78071 | -54.43191 | 2026-05-08 05:10:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16922c16-4951-39e6-8509-ecd7721a29bf | -18.50761 | -55.51197 | 2026-05-08 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9f9dac9c-42c0-32ab-a3cc-2e5580be8dd8 | -20.21518 | -46.83155 | 2026-05-08 05:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b21af91d-4c8f-33e7-a672-e3d1276f0bb7 | -21.70474 | -48.41233 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f42a105c-f87a-3327-b9a5-f99628a005cf | -20.21433 | -46.84106 | 2026-05-08 05:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0c65ce4b-462e-3a8f-a1b7-f13f68598f62 | -20.21477 | -46.83619 | 2026-05-08 05:10:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9584b125-8f18-36f3-8bfb-516c1a1e2d6f | -18.50403 | -55.51141 | 2026-05-08 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ede8ea90-9ea6-33a1-9934-6d505e192d16 | -21.69857 | -48.41621 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53e8c127-1c0d-332e-857c-cee2c31d62ca | -16.16832 | -58.48639 | 2026-05-08 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| be1035a4-8e4e-3b61-a841-475c233d0fac | -21.3763 | -48.5453 | 2026-05-08 05:10:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 192b12f9-eecd-3765-a7cf-88a45694600d | -21.70394 | -48.42133 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9144aa3c-e25b-306a-bac1-b85be9b67734 | -18.2489 | -51.26744 | 2026-05-08 05:10:00 | NOAA-20 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b4de193-86ea-3903-88c0-614512af269f | -16.59849 | -58.2385 | 2026-05-08 05:10:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 6d4ff79e-4f46-36ab-ac5e-b23cafa0ccd5 | -21.71013 | -48.41727 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2547c18a-8778-30fa-8c63-341b1ecf2b14 | -21.38198 | -48.54616 | 2026-05-08 05:10:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6ee3052d-9a5f-3804-b8b2-8bbce2b54656 | -18.51179 | -55.50828 | 2026-05-08 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 68008b43-8370-3eab-9a1d-f4d5ba6058e2 | -21.70969 | -48.41692 | 2026-05-08 05:10:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 783f4aec-758a-3c6f-8146-0ebb3d82b772 | -18.50281 | -55.51991 | 2026-05-08 05:10:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1024200a-b099-3864-8779-f177a3ec8a8a | -19.64425 | -51.09835 | 2026-05-08 05:10:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8258084a-979f-31fa-9359-1fd7909256aa | 3.42707 | -60.57938 | 2026-05-08 05:53:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbd37102-1679-3aca-88f2-51751444287d | 2.90308 | -60.36803 | 2026-05-08 05:53:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4152b11-ddb3-3e7d-bea2-a1d4190a658c | 3.25423 | -61.19566 | 2026-05-08 05:53:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca52284a-a713-3ba2-be3a-403a0ef95e8d | -9.41918 | -65.61323 | 2026-05-08 05:55:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cb2f254d-66e8-319a-835a-e49e2db6a60c | -11.84718 | -57.84523 | 2026-05-08 05:55:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3d2f96b-ee7a-368f-8365-c7da5c06cb7c | -7.77844 | -63.40679 | 2026-05-08 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4169a2c-c3a1-3cb3-b62a-cca0acb34b8e | -7.78147 | -63.41471 | 2026-05-08 05:55:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3982801b-dfb4-3f7e-a462-9da1b0621a04 | -9.24731 | -60.33479 | 2026-05-08 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 314e0c1b-435f-387b-a2ae-6a9990ec0e35 | -14.31817 | -57.73569 | 2026-05-08 05:57:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cdda9e8b-c384-3c6a-9300-a81b481b087e | -9.4468 | -46.1211 | 2026-05-08 11:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5916f1db-09bf-326c-8fd2-fc65318cf57e | -8.6933 | -49.0833 | 2026-05-08 11:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a4092880-80eb-3202-be56-e66e1317c2f4 | -8.6933 | -49.0833 | 2026-05-08 12:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 549d9b63-3897-3191-82ac-2365a68899d1 | -9.4468 | -46.1211 | 2026-05-08 12:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| bb4195d5-5a92-3fd6-b4b9-480b5aa811a2 | -8.6931 | -49.1049 | 2026-05-08 12:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| bc58bcf1-7d82-30ff-b025-e2a7e622ab8b | -8.6933 | -49.0833 | 2026-05-08 12:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 4e617e92-b7ed-33b1-8698-7cc2e67f32e8 | -9.4468 | -46.1211 | 2026-05-08 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 89ce9ed0-631b-36b5-aee3-e40f4ccfb097 | -8.6931 | -49.1049 | 2026-05-08 12:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 8c9351e3-0660-393b-9489-98d0a36bb239 | -8.6933 | -49.0833 | 2026-05-08 12:20:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 09849f52-f612-3b74-bfa1-32c482df36de | -8.6933 | -49.0833 | 2026-05-08 12:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 04e432b8-6bc0-35b3-ade4-28d24a9f937f | -8.6931 | -49.1049 | 2026-05-08 12:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 30f3c1c9-a0d2-3a79-9ebd-09381b667fe0 | -1.31672 | -53.14337 | 2026-05-08 12:36:00 | TERRA_M-T | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 5611e8a9-ea0f-3a9c-af6b-d3cb66632a24 | -12.35482 | -50.01246 | 2026-05-08 12:38:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 28.3 |
| a7e97dd8-fcfd-3e90-9506-6f4f98553576 | -11.20378 | -55.91476 | 2026-05-08 12:38:00 | TERRA_M-T | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e8561aed-4d43-3467-a779-728edefe9dba | -12.35388 | -50.01928 | 2026-05-08 12:38:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 35f1915c-54df-38e6-a7b1-969dac439321 | -11.73801 | -54.79557 | 2026-05-08 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4ad08897-49c4-39a8-b724-22ce5a3cc36f | -8.695 | -49.07853 | 2026-05-08 12:38:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| e97969ff-22f6-370e-9e9c-3a96c715e740 | -9.38335 | -50.93137 | 2026-05-08 12:38:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 727e16ec-8915-3ba1-9fa5-42cf78ad8781 | -10.05008 | -51.66341 | 2026-05-08 12:38:00 | TERRA_M-T | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3bbb7ff2-597e-3e10-822d-3e26c30c5a86 | -12.42195 | -49.66868 | 2026-05-08 12:38:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 757d6181-664e-3023-a774-ecf1ba36e348 | -8.6985 | -49.04891 | 2026-05-08 12:38:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7da0a8f8-57f3-3fc1-90d0-336db22569d3 | -10.66754 | -49.68247 | 2026-05-08 12:38:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 0cdc77c1-a16f-3136-9f91-7f8b8ab51794 | -8.55915 | -51.56694 | 2026-05-08 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 19.2 |
| 1e99c681-d4e0-3363-8918-29ba31127056 | -8.69773 | -49.07239 | 2026-05-08 12:38:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| a2afc7fa-931e-371b-a065-37f7d6790db2 | -10.6684 | -49.67733 | 2026-05-08 12:38:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 0fbd188f-261c-3830-b796-88919dc64628 | -8.54872 | -51.57227 | 2026-05-08 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 1d34a88b-c995-3ef6-95b2-a5dc50c6bdf9 | -9.38597 | -50.90973 | 2026-05-08 12:38:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 33.0 |
| fa4c9006-359c-31bd-b186-07883976880b | -9.40521 | -50.68084 | 2026-05-08 12:38:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| a4765bd3-8522-332a-a28e-cf7d16f1636f | -8.69405 | -49.10166 | 2026-05-08 12:38:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| da8f86f1-4750-3e6f-a601-a7e2e352973a | -11.74818 | -54.79687 | 2026-05-08 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| db6ef8fb-512f-3656-aa12-b86a6cf94018 | -11.30939 | -54.72104 | 2026-05-08 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ca13dd38-3843-39d3-9a9b-41a6ebe1f20a | -11.80334 | -56.9921 | 2026-05-08 12:38:00 | TERRA_M-T | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4ce113cf-f164-3e83-93d4-8d9595ce89f8 | -10.68252 | -49.68425 | 2026-05-08 12:38:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| efb9381a-10fd-384e-aa2a-0712ef2523f7 | -8.55669 | -51.58556 | 2026-05-08 12:38:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| fc81cc7c-a20b-3a2f-a374-412f062d4847 | -8.69153 | -49.10788 | 2026-05-08 12:38:00 | TERRA_M-T | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 227ffefc-11b0-3be6-b434-e74067ebc267 | -10.92635 | -55.14116 | 2026-05-08 12:38:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 79e76067-3749-3af8-a380-789de1b56652 | -11.293 | -54.76746 | 2026-05-08 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 3e270092-ed2a-30dd-8dc3-a8b01155b418 | -11.29455 | -54.75558 | 2026-05-08 12:38:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 0bc1aedd-5dbe-3af1-b57f-e5e3edfcca73 | -8.6933 | -49.0833 | 2026-05-08 12:40:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| d07ef1b8-d02d-36da-8f43-a94317e087c9 | -14.00446 | -56.64393 | 2026-05-08 12:40:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| a973f817-b85f-3a2d-ae89-b7573d47a514 | -15.44475 | -56.32884 | 2026-05-08 12:40:00 | TERRA_M-T | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f4d49305-eed0-354c-a57e-de837d02719f | -14.20238 | -57.4216 | 2026-05-08 12:40:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 2ae735c4-3041-380a-991e-188cb4b42ac0 | -14.00582 | -56.63381 | 2026-05-08 12:40:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 5595ea49-df3d-3175-89a9-0e64237249fb | -14.20105 | -57.43118 | 2026-05-08 12:40:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 104761e2-f3f2-342c-8eeb-693785c0d05f | -14.00718 | -56.62369 | 2026-05-08 12:40:00 | TERRA_M-T | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 08730347-a27e-30dd-b6c1-133ce8da8cbb | -17.93566 | -52.95481 | 2026-05-08 12:42:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 746c07b4-8940-33e1-8e22-bba2323c6866 | -8.6933 | -49.0833 | 2026-05-08 12:50:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 2029ab97-269e-38ac-b706-b3cf135582c5 | -8.6936 | -49.0618 | 2026-05-08 13:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 25ce798f-f5f1-32d9-998e-01cebcdecdad | -8.6933 | -49.0833 | 2026-05-08 13:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 14877c4b-4c66-39e9-b6ac-72b974cade8c | -9.4468 | -46.1211 | 2026-05-08 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 4c5f5452-1b63-3ba0-9423-f42a31cfb311 | -8.6936 | -49.0618 | 2026-05-08 13:10:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5648783f-7460-3c02-986c-937525f112bb | -14.0118 | -56.6215 | 2026-05-08 13:10:00 | GOES-19 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 65.7 |


[Clique aqui para ver as próximas entradas](README11.md)
