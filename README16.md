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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 879b9671-6dce-3706-99a9-7b019507cbd5 | -16.9837 | -45.819401 | 2024-10-05 01:07:08 | METOP-B | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 085c79d9-8b8a-3064-84c8-23650cdcfbf0 | -18.8158 | -53.755199 | 2024-10-05 01:07:10 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| addca80e-726c-3622-9800-4f2248d430c4 | -18.817499 | -53.762501 | 2024-10-05 01:07:10 | METOP-B | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 185cc593-a737-35d4-9213-22e3c9097841 | -18.501801 | -52.7715 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0c758867-a29a-3eb9-85c8-6600c20ebd23 | -18.5035 | -52.779099 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 519f5c3c-ffd6-38a6-b20b-547383d44155 | -18.505199 | -52.786598 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 31ed1880-0bf4-3bb7-bac3-ad3b17c9a77d | -18.506901 | -52.794201 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6404452d-0073-31f1-9ba5-d66aafeb1956 | -18.490299 | -52.766399 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 65d57979-6018-3caa-b4a8-20b7d69ec329 | -18.492001 | -52.773899 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| defb91f5-6d0b-3fc0-b50c-2916aa62cee6 | -18.4937 | -52.781502 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 220f7bcd-cdb0-3ae1-9b10-5a127a2cf75a | -18.495399 | -52.789101 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f656d2f0-851e-3942-99c3-58ac881b9f21 | -18.4972 | -52.7966 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2e41bce6-2fbf-3745-bef4-7d6937cfe716 | -18.480499 | -52.768799 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 962e80ac-13ba-3a19-80f2-9fd1680fa46e | -18.4823 | -52.776402 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1aac7c07-40d7-3c14-b9ce-eebc03355099 | -18.483999 | -52.784 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 81b71cce-3ce1-39e8-b914-d33dce55dec0 | -18.485701 | -52.7915 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c75cd223-063b-3732-abdc-53d89baf0c54 | -18.4874 | -52.799099 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 303fe689-cb1e-3ac0-b9b2-ee72f0caad41 | -18.489201 | -52.806702 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 46bd5dcf-e6c4-3457-9639-7cba66dc40f1 | -18.4909 | -52.814201 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 632a8b9f-6035-37bc-b584-3c780ad2173e | -18.492599 | -52.8218 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 243db4d1-704e-3b05-812a-64c2cff5cae8 | -18.4725 | -52.778801 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f1366fd5-2669-3d8d-9c8b-ddf9c3e2fe4a | -18.474199 | -52.7864 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b8d56338-3a4a-36b1-b75c-9331b94c8ba4 | -18.475901 | -52.793999 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1d246183-4a5f-314d-a132-2184fc87c445 | -18.4776 | -52.801498 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ba741443-ad69-388c-807f-6031e991fa18 | -18.4811 | -52.816601 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5c517192-7600-3361-bca3-2a518aaa671f | -18.4828 | -52.8242 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 02960e65-227c-36fa-9888-a5f19d0975e6 | -18.484501 | -52.831699 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bc305d62-b63f-3966-9a48-9bd5d5a9b669 | -18.4862 | -52.839298 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 466c50df-43f4-36c5-b447-f6daf97ad43f | -18.464399 | -52.788799 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2d80f4af-9186-363d-8c23-6f5083868bb3 | -18.466101 | -52.796398 | 2024-10-05 01:07:12 | METOP-B | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8371d28a-e7c4-32b5-afea-c59e067866f4 | -18.8804 | -54.470699 | 2024-10-05 01:07:12 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f9b83c48-1b96-3234-b083-f89dd9c648c4 | -18.882 | -54.477901 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e967eb63-3e19-364e-9759-10790d728ac6 | -18.891399 | -54.521198 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 489f2a3e-9077-3f84-9659-4c4678c142db | -18.881599 | -54.523602 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 25997a9f-4e91-32ce-b64c-4cd8953c3faf | -18.8832 | -54.5308 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f55a0bce-f508-3da9-890b-32f3b98a503f | -18.8848 | -54.538101 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 1e6882e8-dc4c-3d28-8364-cffe0780dfc8 | -18.8577 | -54.460899 | 2024-10-05 01:07:12 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 76390699-6bac-3f2b-86af-1dc1ae1b8bdc | -18.871799 | -54.525902 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8110e414-3c43-328e-9290-7f7a51efc1cd | -18.8734 | -54.5331 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 8c2aa474-01aa-3869-bc38-4c9d1aa11916 | -18.875 | -54.540401 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e92fcf73-655d-3d68-8122-9460ca83898b | -18.8479 | -54.463299 | 2024-10-05 01:07:12 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 60310b94-3105-3973-a33c-9a12db5236da | -18.8589 | -54.513802 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 64b2215d-463b-388f-9a7e-ece547b67d8d | -18.8605 | -54.521 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 50e20520-ee58-310b-881f-bc5a9f8d3cf9 | -18.862101 | -54.528301 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a3983aa3-4557-3125-b056-f47b2a776302 | -18.863701 | -54.5355 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 88767247-d2dc-3bd5-9d85-256d02b32a88 | -18.8491 | -54.516102 | 2024-10-05 01:07:12 | METOP-B | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 30ff19a0-3d64-3172-a94c-c77c0d898316 | -18.8507 | -54.5233 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 90640c0b-0f88-36e2-8217-d56b9e38887f | -18.852301 | -54.530602 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a83684f2-e136-3c60-97dd-0271f46fa7a4 | -18.853901 | -54.5378 | 2024-10-05 01:07:12 | METOP-B | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 4c15347b-b113-3d33-ab79-6e55360fc98a | -18.2978 | -54.208199 | 2024-10-05 01:07:20 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a294805c-ef31-3623-87ff-a3593a66eeec | -18.2994 | -54.215401 | 2024-10-05 01:07:20 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b71792f1-a385-39c2-8129-d044a803ee01 | -18.288099 | -54.210499 | 2024-10-05 01:07:20 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e30da16a-4cfd-3d25-90ac-1c37f55985e3 | -18.2897 | -54.217701 | 2024-10-05 01:07:20 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 68da9b60-cc4a-329a-92a9-f21399fde4ed | -18.2913 | -54.224899 | 2024-10-05 01:07:20 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ced4d31c-146a-3ad9-827b-249cd2f54050 | -18.278299 | -54.212898 | 2024-10-05 01:07:20 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3b8ee678-5e3a-3795-ae75-7c9c6a184121 | -18.2799 | -54.2201 | 2024-10-05 01:07:20 | METOP-B | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 72d7dd71-98e7-3664-8ff1-16d94999448e | -18.7008 | -57.2752 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d65ed853-f6be-36ef-8249-839132b07924 | -18.702499 | -57.2836 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 979b1270-2bad-3bea-b23d-ad6d7f634e89 | -18.704201 | -57.291901 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cf1f97ca-fb95-3b38-b132-50933db50da8 | -18.6877 | -57.260799 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 1d070111-1cef-3845-88bd-de3b1efefe61 | -18.689301 | -57.2691 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6f738637-1335-3f4b-a6c9-c549cacb7a42 | -18.691 | -57.277401 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| d94dbf31-0f4d-3480-97c9-f38ca8391466 | -18.692699 | -57.285801 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7a25464d-27de-33b0-b728-c69a43fa4636 | -18.6779 | -57.262901 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 43780e58-9b66-3330-9642-081a8c39fef3 | -18.679501 | -57.271198 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 0e6ffd3b-f0ce-3932-a44f-c46d9a242921 | -18.6812 | -57.279499 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 24bd84f8-48e9-3a3b-83bb-4f581b4d4718 | -18.682899 | -57.287899 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 4d7aad1e-847a-313d-9eef-48ee17811da3 | -18.684601 | -57.2962 | 2024-10-05 01:07:24 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 9bed80a0-c1f0-3a40-a836-f52151f510ea | -18.6583 | -57.2673 | 2024-10-05 01:07:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| cc82f9d1-b43d-3936-abcc-6d6ed8e68c6b | -18.666401 | -57.256699 | 2024-10-05 01:07:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 7d31cfee-3664-3f68-a7b3-a254a3cc16b2 | -18.6681 | -57.265099 | 2024-10-05 01:07:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 5bd37901-1174-3ab1-9d65-c292e92fe172 | -18.669701 | -57.273399 | 2024-10-05 01:07:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 51bff3c6-fd28-30ff-ac67-37999d7c5d53 | -18.6714 | -57.2817 | 2024-10-05 01:07:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 79b3f183-a962-3193-be07-102d51d155a8 | -18.659901 | -57.2756 | 2024-10-05 01:07:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 3c81ff64-2215-37ce-b52c-40f0b868e2f2 | -18.6616 | -57.283901 | 2024-10-05 01:07:25 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 6ebbeaf6-9f96-3eb6-bc83-0351341d6226 | -17.1208 | -51.716999 | 2024-10-05 01:07:30 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 68040323-64f2-365a-8520-01624e3cbeb6 | -17.122801 | -51.725399 | 2024-10-05 01:07:30 | METOP-B | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 198611db-5962-3000-a9c8-a5882b8d2f96 | -15.7704 | -48.196701 | 2024-10-05 01:07:38 | METOP-B | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | nan |
| eda251ce-934e-3f4b-8a0a-f5a1dde792fc | -16.0816 | -50.231998 | 2024-10-05 01:07:41 | METOP-B | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6674f281-f509-3988-9573-fee1e47441ab | -16.084101 | -50.242298 | 2024-10-05 01:07:41 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e9690a52-c1d9-32ca-a298-c13ebdcf7d8d | -16.0744 | -50.244801 | 2024-10-05 01:07:41 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5ff18ce9-a6c9-3354-8839-15fafac4052c | -16.1187 | -50.426899 | 2024-10-05 01:07:41 | METOP-B | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 494a9a1d-2c07-3b5d-9846-6dd78224cfa8 | -16.121099 | -50.436798 | 2024-10-05 01:07:41 | METOP-B | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e35a34b9-3010-3f15-a453-077d41ec36df | -16.104099 | -50.4519 | 2024-10-05 01:07:41 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8ac2fd66-9539-3cbb-95f9-a24b6466de08 | -15.4036 | -47.695 | 2024-10-05 01:07:42 | METOP-B | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 72bd9471-ea05-3af9-b577-23c2738a3049 | -16.077299 | -50.426998 | 2024-10-05 01:07:42 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ba6e73db-12bb-3359-96d9-9bae164c40ff | -16.0798 | -50.437 | 2024-10-05 01:07:42 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 30366e5c-29b3-30b4-8d0b-cce81ad22e4e | -16.082199 | -50.446999 | 2024-10-05 01:07:42 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 86af0756-8d70-3147-b92d-aae149abe282 | -15.7455 | -49.916901 | 2024-10-05 01:07:45 | METOP-B | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| eee02778-5404-3b44-8f71-82cdb47fc067 | -15.7482 | -49.9277 | 2024-10-05 01:07:45 | METOP-B | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 652ac2f6-5a0e-38ec-b26e-a50e199faf4a | -15.7508 | -49.938499 | 2024-10-05 01:07:45 | METOP-B | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 535d7969-c303-3a02-8d36-267049f88fd8 | -15.7385 | -49.930302 | 2024-10-05 01:07:45 | METOP-B | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4bfc9b0d-be68-351e-b394-a30826ea23e1 | -17.153601 | -56.142601 | 2024-10-05 01:07:45 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fc1bbc11-be09-379d-83a4-a35d42af4c0c | -17.145399 | -56.152199 | 2024-10-05 01:07:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a4d2a305-7c5c-3411-bcb4-17b0575fca66 | -17.146999 | -56.159599 | 2024-10-05 01:07:46 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 439c7501-f1cb-3905-9ee0-da6c23545f26 | -17.063 | -56.054798 | 2024-10-05 01:07:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 31167acd-e239-3bd4-880e-66889a83e7d5 | -17.0646 | -56.062199 | 2024-10-05 01:07:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 877874aa-a8e9-30d4-a383-29016fe13507 | -17.0532 | -56.056999 | 2024-10-05 01:07:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ec793d11-392b-3786-b603-a84c864cd031 | -17.0548 | -56.0644 | 2024-10-05 01:07:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 70f60e72-f02a-314a-a3d8-d32918dff085 | -17.0564 | -56.0718 | 2024-10-05 01:07:47 | METOP-B | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |


[Clique aqui para ver as próximas entradas](README17.md)
