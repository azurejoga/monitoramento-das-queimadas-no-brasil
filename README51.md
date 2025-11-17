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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0ac01697-0c52-372a-890d-4c80c0c6c0bb | -9.7169 | -43.95292 | 2025-11-17 05:59:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| eab623d1-f9f2-36bf-83bb-91980aed32ad | -3.2357 | -50.48521 | 2025-11-17 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| f482c7f6-f855-3dfb-9768-2762b185fb86 | -5.88409 | -43.97633 | 2025-11-17 05:59:00 | AQUA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9c3c0ab-b6e4-3f01-8ec9-b90000bd23cb | -6.12886 | -41.81761 | 2025-11-17 05:59:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| fde47923-8107-3beb-ac00-590cd341b7db | -12.71685 | -45.41129 | 2025-11-17 05:59:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 2e45df3b-4b64-3a25-a8bb-162fafbe4576 | -10.92879 | -48.67064 | 2025-11-17 05:59:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0eb67a27-957c-31c0-8542-07581a9a8e84 | -6.29864 | -43.78822 | 2025-11-17 05:59:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4328cf6b-dc2b-3102-a11c-6f0aeb101759 | -12.7973 | -46.43658 | 2025-11-17 05:59:00 | AQUA_M-M | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f9088159-9202-34b4-9631-9009540a8277 | -5.35505 | -44.86076 | 2025-11-17 05:59:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b73e1b8-a66e-30c5-b874-ec0b3cccef18 | -3.40444 | -50.12182 | 2025-11-17 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fcdea3dc-9a72-39e5-bbdd-aaf20bbe73a2 | -4.09405 | -48.02457 | 2025-11-17 05:59:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c65b3d47-eb63-3cb1-a982-09f57555d62d | -3.39441 | -50.18507 | 2025-11-17 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5bc74696-4afa-3a84-bc2a-2e6a47c58b28 | -2.50221 | -47.82055 | 2025-11-17 05:59:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 185f2ee5-d69b-3315-8630-cea120240af8 | -7.12539 | -41.65606 | 2025-11-17 05:59:00 | AQUA_M-M | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 1e115d41-643c-316d-89f5-d41e3a3d3936 | -2.51206 | -47.82197 | 2025-11-17 05:59:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 01a3a839-10b9-3580-89df-afe56d94857f | -4.40329 | -45.83039 | 2025-11-17 05:59:00 | AQUA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a24306d6-f5ee-3f6c-994d-83bb9a9c8931 | -9.57252 | -49.11123 | 2025-11-17 05:59:00 | AQUA_M-M | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 96c4b1a6-23df-321f-a1a8-19a736c87efa | -3.22552 | -50.50776 | 2025-11-17 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 240897b3-9e64-3155-ac2c-44492aa9fb2b | -12.70244 | -46.77104 | 2025-11-17 05:59:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 25763353-848b-32f0-b39e-bd5ad7b845b5 | -4.68267 | -46.30746 | 2025-11-17 05:59:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4839c90b-b59f-3c4e-be68-2e86b28423df | -3.24015 | -50.49287 | 2025-11-17 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 75598cfb-ac03-3d84-9db9-ae6f101853ca | -8.53843 | -46.05854 | 2025-11-17 05:59:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 29e69300-af3e-312a-810b-870316f76184 | -11.67372 | -44.7201 | 2025-11-17 05:59:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d8ed4ef-ab29-3f72-8e90-b1c0a7fdd7f3 | -8.30019 | -43.93795 | 2025-11-17 05:59:00 | AQUA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5b28b719-3980-3f0c-9c85-e54129d01151 | -9.33114 | -46.57381 | 2025-11-17 05:59:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| c3af6b40-ce3f-37db-a498-25232b25c9d5 | -3.7527 | -51.06147 | 2025-11-17 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 5c8acb92-7749-34b7-906a-55f0dfed689b | -6.12125 | -41.81077 | 2025-11-17 05:59:00 | AQUA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| c1e7043f-ade9-3b14-bc14-ed75e61a7f4d | -7.09373 | -42.72453 | 2025-11-17 05:59:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 29f946d8-062c-3f34-9b11-76891331a287 | -7.69793 | -42.94381 | 2025-11-17 05:59:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 8e670f76-f4d0-39af-98e3-0ef4cf8b3945 | -10.66249 | -49.36098 | 2025-11-17 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 34251f5d-c026-358a-a9b2-6f46c2105b01 | -3.87428 | -44.99178 | 2025-11-17 05:59:00 | AQUA_M-M | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 40a47c17-8158-3d40-b827-bd423002f54d | -10.918 | -48.67872 | 2025-11-17 05:59:00 | AQUA_M-M | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 3637bc23-b9d7-3aba-8ba8-64e1b481269b | -3.29791 | -50.07694 | 2025-11-17 05:59:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 0632acb5-27bd-3341-8e76-96d0d6f7418b | -11.78489 | -44.65104 | 2025-11-17 05:59:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d50317b6-b7e5-38e3-b4d0-236e8add6134 | -12.8494 | -46.46866 | 2025-11-17 05:59:00 | AQUA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e3470c90-4166-35d5-9e74-27c7ba9f8171 | -5.03288 | -43.60561 | 2025-11-17 05:59:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 107bcc72-5d59-347b-9dd4-4d39ec172363 | -3.06753 | -45.19841 | 2025-11-17 05:59:00 | AQUA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| acd3922b-1860-3c83-8e46-2cbaf3430f24 | -11.81935 | -47.5878 | 2025-11-17 05:59:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 9edf8a30-9bb5-34aa-be3c-3e54b58cd299 | -6.68053 | -42.04548 | 2025-11-17 05:59:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 36.5 |
| 523a2834-0ba6-3b52-9011-d1fd22d48a5b | -4.72889 | -46.37582 | 2025-11-17 05:59:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 66b85d1f-9a43-35b2-93cb-47703675fd4e | -6.38955 | -42.28693 | 2025-11-17 05:59:00 | AQUA_M-M | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| d863c09c-b51e-3d1f-bf5c-723cf181e9d9 | -5.32799 | -43.04186 | 2025-11-17 05:59:00 | AQUA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3280025c-88eb-3ac5-8b71-6f0f6d1d91f5 | -11.80997 | -45.30318 | 2025-11-17 05:59:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ea39bbaa-dc62-39bb-8f68-643d5cf3a053 | -3.21414 | -43.3558 | 2025-11-17 05:59:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| da0705a3-00d7-38c5-96f9-e08e5efd9f43 | -3.23313 | -50.50202 | 2025-11-17 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| b224f8a8-7949-3eb6-9081-a81a4f47b0a4 | -3.22822 | -50.491 | 2025-11-17 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 8b518143-d786-3605-909c-3e16908e02d5 | -10.55175 | -44.82132 | 2025-11-17 05:59:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4dde7654-e4cd-3d85-a8dc-0a3e692ab8d3 | -11.83676 | -49.20168 | 2025-11-17 05:59:00 | AQUA_M-M | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| e133281d-e0d6-3fc1-97ea-7b17eb576369 | -12.86532 | -46.03811 | 2025-11-17 05:59:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57d9fad1-8b48-3a92-acc1-503d0f918a04 | -11.20016 | -49.40793 | 2025-11-17 05:59:00 | AQUA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| bbfd238d-16e3-35d7-b5a3-4591b4b68eb5 | -3.2212 | -50.50006 | 2025-11-17 05:59:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 925b64a5-ccbb-3c51-8e04-15aeccc7d506 | -5.83628 | -48.83132 | 2025-11-17 05:59:00 | AQUA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3323a59b-0a32-340a-a134-44bfaf40d28b | -6.8527 | -43.14452 | 2025-11-17 05:59:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eb8764a5-19dd-3148-bb24-55bbd09dc84b | -9.3237 | -46.56363 | 2025-11-17 05:59:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2793cfe6-c32a-3c28-ad26-44967bd6465f | -7.21895 | -47.98162 | 2025-11-17 05:59:00 | AQUA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 32027939-8b27-361d-ad00-2b2fcf8f4322 | -4.69157 | -46.30885 | 2025-11-17 05:59:00 | AQUA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f476d910-8a36-3e53-9bc7-23b9b566de8b | -11.80094 | -45.30189 | 2025-11-17 05:59:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 183e134a-1bd8-3523-a2d8-36ddb97a5131 | -6.48128 | -47.18808 | 2025-11-17 05:59:00 | AQUA_M-M | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a70f488b-fa12-3757-9e11-38a24f926058 | -11.81189 | -47.57732 | 2025-11-17 05:59:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c0a90b05-3747-354d-b997-ad6469edbfeb | -5.03426 | -43.59616 | 2025-11-17 05:59:00 | AQUA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8f65fb60-6ba2-3af0-b7c3-2628325d4e6f | -4.65584 | -46.73127 | 2025-11-17 05:59:00 | AQUA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| eb6ebe17-6639-38f8-b69a-ceb13bff83a8 | -6.67204 | -42.03186 | 2025-11-17 05:59:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 141a5983-a393-35b3-92fc-8988b4281622 | -11.69531 | -48.86369 | 2025-11-17 05:59:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c6ce24d8-f0c5-3e82-a1c8-67f7ffdc8554 | -11.40084 | -43.3247 | 2025-11-17 05:59:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.2 |
| e4af36e2-689c-34c6-a185-2797e3bc2e25 | -11.69687 | -48.85373 | 2025-11-17 05:59:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 566fe6c5-f610-3f0b-a707-3a926bbd7a08 | -3.34179 | -43.49106 | 2025-11-17 05:59:00 | AQUA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 76b5d966-3e34-350f-b6f5-858371bdf52a | -12.43323 | -44.74369 | 2025-11-17 05:59:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 478a5c2e-e7b7-3fb2-b1f5-9fd6eade053a | -4.01314 | -48.80669 | 2025-11-17 05:59:00 | AQUA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 95628445-5256-39c2-bdc3-05df2ca7565d | -2.50391 | -47.80944 | 2025-11-17 05:59:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 0bae22ff-7aec-32c8-922f-4c67dd06f7a8 | -11.70457 | -48.86522 | 2025-11-17 05:59:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 6a40616d-7558-38ea-8084-b13162780e8a | -9.44808 | -44.85649 | 2025-11-17 05:59:00 | AQUA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 12.2 |
| c1eeee47-714a-33eb-96f9-8a4aa630cf38 | -7.96988 | -50.00385 | 2025-11-17 05:59:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 98cf8cee-2dfe-3fe2-878e-13dca9fd8168 | -6.44355 | -43.81516 | 2025-11-17 05:59:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b49b9d06-99a9-39b6-82b4-66bfe216594c | -9.4571 | -44.8577 | 2025-11-17 05:59:00 | AQUA_M-M | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3c86e995-e165-344e-b554-d66f483a5b87 | -11.70614 | -48.85521 | 2025-11-17 05:59:00 | AQUA_M-M | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| e87c8654-6835-3bee-bb6f-c404d9720faf | -12.87718 | -46.46375 | 2025-11-17 05:59:00 | AQUA_M-M | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 555c71fd-7829-3e1b-a232-47b219b989aa | -3.76849 | -47.74147 | 2025-11-17 05:59:00 | AQUA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bb5acb20-d530-3791-91c8-8a5029dc09fd | -12.69365 | -46.7697 | 2025-11-17 05:59:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 8135fde5-7f0a-3caa-abd0-be686b77f832 | -10.66074 | -49.37189 | 2025-11-17 05:59:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 27.3 |
| a55543fd-b55f-335d-9e3d-4e8629417ab7 | -9.32235 | -46.57248 | 2025-11-17 05:59:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 810b6427-0902-3a4b-9859-78152b228e44 | -11.70353 | -44.44641 | 2025-11-17 05:59:00 | AQUA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 34c4cb38-6c09-38d1-8ac1-268c4936a6e5 | -8.527 | -46.07484 | 2025-11-17 05:59:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 25dbb348-0709-309e-aa17-ca51b3a0eb32 | -4.99444 | -44.3602 | 2025-11-17 05:59:00 | AQUA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 8e8eb89b-e7b8-37c6-a548-923da9bf5136 | -14.64789 | -46.53425 | 2025-11-17 06:01:00 | AQUA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 6a7ab179-3e14-3706-8c8f-300b649d7b23 | -14.64657 | -46.54329 | 2025-11-17 06:01:00 | AQUA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 43567fd0-df5e-3a8d-b51d-92476616d11e | -14.51738 | -48.02227 | 2025-11-17 06:01:00 | AQUA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 244af9d4-4e02-31c6-b35b-0683698cbbe1 | -13.27221 | -47.28656 | 2025-11-17 06:01:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9058c097-ad5c-341f-8bf9-69912c18ff34 | -13.27086 | -47.2955 | 2025-11-17 06:01:00 | AQUA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0474a4b8-ce7e-39a9-aa1b-d678398559fe | -14.6492 | -46.5253 | 2025-11-17 06:01:00 | AQUA_M-M | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e06f39e6-3c26-33aa-a31f-9da0233305e9 | -6.6875 | -42.0296 | 2025-11-17 06:10:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| 20d718b2-5c3a-3e56-b2b6-d791923e59ff | -3.2344 | -50.4952 | 2025-11-17 06:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a91fc89f-c195-3e12-a39e-c4f574952c31 | -3.8582 | -44.4252 | 2025-11-17 06:40:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 9097ae0b-3d2b-3ceb-b34d-890d86973191 | -3.8396 | -44.4261 | 2025-11-17 06:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| f2048e28-c862-36c5-842e-ba1c9d22bcc4 | -3.8582 | -44.4252 | 2025-11-17 06:50:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 589237af-b5cb-3910-8007-dc55290b7cf5 | -3.8396 | -44.4261 | 2025-11-17 07:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| e39bd150-1aa3-338d-9acb-1c8ac811c9df | -3.8582 | -44.4252 | 2025-11-17 07:00:00 | GOES-19 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 2f1f0393-962e-3707-93af-7abcdb45d5cb | -3.2344 | -50.4952 | 2025-11-17 07:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 6718468c-b5ee-33e0-904e-e45c84ec1892 | -3.2344 | -50.4952 | 2025-11-17 07:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 907c2a1f-d9c0-3fe8-9f97-00fbf0eb8530 | -3.2344 | -50.4952 | 2025-11-17 07:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.8 |
| c0913f32-ca31-39cd-abd0-004df3d8f1a1 | -2.8863 | -45.2375 | 2025-11-17 09:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 92.5 |


[Clique aqui para ver as próximas entradas](README52.md)
