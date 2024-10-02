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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e83fde3-9ac8-3c85-9e8c-6df615278402 | -16.1002 | -50.34844 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b208363-f1a6-3b94-b9d2-ffd62a32f8bf | -16.09879 | -50.31391 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 867582ac-c6ea-3751-9519-290d74b499af | -16.0984 | -50.31726 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc1f7e66-7512-3ea2-ab99-dfbf7efb77eb | -16.09832 | -50.36481 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| af3ee4c3-d550-3b18-86fc-04c680776c69 | -16.09301 | -50.36428 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6713acc5-6c91-31f2-977f-a0c668a0d79b | -16.09268 | -50.36716 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0d93fd91-f692-3648-801f-1a05c2324dfb | -16.0877 | -50.36376 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b02e9a70-1947-3274-aeba-00ff9d4677dc | -16.08738 | -50.36664 | 2024-10-02 05:12:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b71643cb-fecc-36e5-a924-2faee41c4ea4 | -16.08718 | -50.32129 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e843e28-8d7f-3caa-902e-ef0afb4cd968 | -16.08646 | -50.32756 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dabc4616-f835-33f3-bcc1-42a5e03e91f6 | -16.0861 | -50.33072 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb551219-eea2-3ef7-8581-3907e81682c7 | -16.08574 | -50.33388 | 2024-10-02 05:12:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c351de2-65c1-3cb6-87e4-2bf82e19cd76 | -15.37129 | -51.55647 | 2024-10-02 05:12:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c1196dbb-103a-33b8-87a0-c2d6e2185c63 | -15.36581 | -51.56124 | 2024-10-02 05:12:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31cfc116-579b-349b-b450-5ff021d832ea | -18.25256 | -50.81484 | 2024-10-02 05:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5e3cc8e-c4ee-3788-b6cc-a7df4cf237ad | -18.2522 | -50.81816 | 2024-10-02 05:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8af736d8-a7bc-3689-9412-9b6aac4d6157 | -18.25183 | -50.82161 | 2024-10-02 05:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 008c67f5-ab68-3321-bf75-8beb40a49722 | -18.25141 | -50.82543 | 2024-10-02 05:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f15f8707-882b-3245-802d-edcd9d5e1fb1 | -18.24718 | -50.81514 | 2024-10-02 05:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b965dc3-c69a-3650-b40b-6508be867ef4 | -18.24681 | -50.81856 | 2024-10-02 05:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adf7d862-0b4a-3038-bffc-6fa9b872ef67 | -18.24644 | -50.82198 | 2024-10-02 05:12:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c0a5c5ac-601d-373b-8804-247d42624590 | -13.14112 | -51.22402 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 99bfcafd-d5ee-3c25-b2bb-76e297620c61 | -13.14043 | -51.22928 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 784b276a-425d-3d8e-9a2b-c507ae55dcbd | -13.13632 | -51.22338 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f4f72706-02d2-3ab5-822a-ff17e04a5d8f | -13.13564 | -51.22864 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 60a460f2-c8fc-3066-ac62-d90775fa853a | -13.13152 | -51.22273 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 49564bd7-2ea0-3747-b647-eeb567b64116 | -13.13084 | -51.228 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 610d40c3-a6c0-38ce-a4c5-f1961eeaee40 | -13.12834 | -51.43321 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 3fc58572-7a01-3a47-8351-c60c64dcf620 | -13.12604 | -51.22736 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a559b824-8e5c-36a3-8db3-0321ba783891 | -13.12456 | -51.42882 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 462ded0e-5442-3d06-953a-07e4d67df5c1 | -13.12428 | -51.42748 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9a9270cd-3fd2-3ece-9e38-9a2852a61abf | -13.12393 | -51.43392 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 50245f8f-bac5-3207-ab14-1c1b65f45a40 | -13.12361 | -51.43256 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9e5e1ab5-f9c0-3c69-b3f7-c398c06223b0 | -13.12125 | -51.22672 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 501f29c8-856b-3da1-b84e-7ec3eca9e2ea | -13.11955 | -51.42683 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 04614f95-bf2d-3c19-841a-65a01230881e | -13.11888 | -51.43193 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 3436126a-ae64-3656-b6b1-03e7486f4df3 | -13.11821 | -51.43702 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 5848a2e3-14f0-31a9-a0f9-ab49c1c3fadf | -13.11548 | -51.42107 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| c0718c49-f00f-3507-a6c7-ae23fd7170ef | -13.11482 | -51.42619 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.2 |
| f9a361bf-166f-333e-9a66-fcf979a84a45 | -13.11415 | -51.43128 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 97493b51-e128-3c6d-8e8d-0efb2ec52194 | -13.11075 | -51.42044 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 9c66b4e7-4ff7-3a27-9f78-5e684e64f48c | -13.11009 | -51.42554 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| e0f5ed29-ef1e-39b3-81c4-676c4738b56b | -13.10602 | -51.4198 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| dcbceb5f-8c9b-3947-99fc-9a4f89a75a8a | -13.10536 | -51.4249 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| d4f56267-84da-3ef1-9aa2-b7e46df759dc | -13.10526 | -51.38843 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f40a2ce-e2dd-3d77-8290-f2557cb8c45d | -13.10129 | -51.41916 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8dff78f9-496b-39a1-b4fe-b8f04be8cda2 | -13.09722 | -51.41341 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff537500-2a50-3db3-a126-7ecbb63fdf48 | -13.09314 | -51.40764 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62b1aaf9-cf05-377a-80b8-117b4d1a11c9 | -13.09248 | -51.41276 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f622ad61-c7b8-3abd-84b1-4a661bc9e2d0 | -13.08972 | -51.39676 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6c98dd9-1663-3de2-bd50-ab7a89b11322 | -13.08906 | -51.40189 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b6cb17e-4b24-370b-9db2-09c887127c69 | -13.08841 | -51.407 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f976ba81-6086-30c9-ae6b-17d08096b2dd | -13.08498 | -51.39612 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| acb90b23-ca24-39c6-82ae-0f595297250d | -13.08433 | -51.40124 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| bc979109-56f2-3e34-8d29-6dbb4fdcd036 | -13.08367 | -51.40636 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 78f72cf6-a84a-3073-b3ef-0f085eebeb2b | -13.08024 | -51.39548 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| df9d58a8-976f-36f6-94d9-da5077a297cc | -13.07959 | -51.40059 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 75cb15ec-1fc1-3d82-811d-4e93faa352c1 | -12.97052 | -51.52827 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3965265-4614-3030-95d2-bc8fcbba9b6e | -12.96713 | -51.51761 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| fc9cbd46-b8b7-31c1-9179-ae47f414b3e9 | -12.96648 | -51.52262 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| f001adfa-8be1-3c4b-93fb-2f547bddb412 | -12.96583 | -51.52764 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f505d9a-6470-3128-8c3c-523097fe416f | -12.96518 | -51.53267 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16fde16b-b721-35c3-8fd1-8ccd51c3c2b8 | -12.96373 | -51.50695 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b2e12299-d424-3aad-a370-9bcd32146d80 | -12.96308 | -51.51198 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdd2b994-f406-30b4-ac10-73ea81deb749 | -12.96243 | -51.51699 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| dfc900ac-232e-313d-aa78-84cd5e99aeec | -12.96179 | -51.52198 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| e943ffc3-4b8f-325b-9c26-d5be5895199a | -12.96114 | -51.527 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 71872f4f-64e5-3ac0-85f3-b59d3153d348 | -12.96097 | -51.49125 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3446e01c-690e-382c-9fe7-6f4c2d37bef1 | -12.9605 | -51.53202 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60ce6b3e-87e1-3b5f-b03e-95707ff6ccd7 | -12.95774 | -51.51635 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 7dd4f2d1-343b-3505-a51a-f0e24199382d | -12.9571 | -51.52136 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| b454fa98-7ac8-3c8f-a3cc-65333bf8699f | -12.95646 | -51.52637 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b74d6827-0ddc-3a7a-98ca-0a50d34b777f | -12.95305 | -51.51574 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 214c5b78-543f-3001-b3f6-71b5c151f917 | -12.95241 | -51.52074 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 88fb1dd9-edec-3c92-9a47-ed5552a6d408 | -12.95028 | -51.50004 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| eea8700e-1fc1-3e7f-9974-e8d6eac520ee | -12.94623 | -51.49438 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f4fe0b09-8a9d-337b-a0aa-d7e6bc810d4f | -12.94558 | -51.49941 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 16a4126b-2dca-3625-95d1-a531fb6e0bab | -12.93354 | -51.40512 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f186c93-db7d-3d65-8a52-8061f9fb13bc | -12.9329 | -51.4102 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c6e2f5e-77cb-3a65-b819-acd97e449c5c | -12.93243 | -51.40883 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 852f0caa-ae86-348f-b60e-3b8bcaff7f24 | -12.92882 | -51.40446 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 649581c2-c613-3f12-ac16-b9b8a34d62c0 | -12.92818 | -51.40956 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26d6fd6e-c379-39bb-bb6f-1b18386a2156 | -12.92771 | -51.4082 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb9bd6b9-f2d6-3782-bb04-3cee3c7467a2 | -12.89913 | -51.29488 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7b5073c-a08a-392b-9f86-c909bf0e73fb | -12.89512 | -51.32581 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97459a53-e02b-3bc4-ae07-76f8bbb2c0a3 | -12.89038 | -51.32516 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 387e093b-88da-309a-94ab-275f61a79587 | -12.88563 | -51.32452 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6d7f3f9a-7876-302b-a6da-cdd548d5684b | -13.18524 | -51.2525 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 840351a1-6b7b-3c74-b547-11cdd1df549c | -13.18458 | -51.25776 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bcd48f9f-5c70-3697-8db9-bc9230ce6574 | -13.18045 | -51.25185 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 85862c2b-6ff0-3eb1-ac90-aa24b1c3c943 | -13.17979 | -51.25711 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| fd2098d3-c4ca-32ce-aaf5-76b7dcd19945 | -13.17631 | -51.24593 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fcd87f8c-39fa-3fe4-b673-296b4e0d6f04 | -13.17566 | -51.25121 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b1b1a3b5-63af-30ca-ac27-2306edc16c2b | -13.17262 | -51.2443 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 405d5b2c-8553-3622-8103-14d0ee8703d4 | -13.17193 | -51.24956 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 4b45f41b-8f05-3866-ae8d-8fc1ac0c65e9 | -13.17152 | -51.24529 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 120b1112-3338-31bf-8986-fb987d8deb56 | -13.16783 | -51.24366 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.6 |
| a892376d-c0b4-3b77-a88d-08870ef8994b | -13.16738 | -51.23937 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b01baf86-2593-369d-a37d-b559adba53c8 | -13.16672 | -51.24464 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 3897d845-e6d3-36c0-986d-3e38e9373b2c | -13.16373 | -51.23776 | 2024-10-02 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README139.md)
